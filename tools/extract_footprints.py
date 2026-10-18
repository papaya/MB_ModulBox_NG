#!/usr/bin/env python3
"""Extrait les empreintes d'un PCB (footprints embarques) vers un dossier .pretty.
Usage: extract_footprints.py <pcb> <out_dir> [lib_prefix]"""
import re, os, sys

def extract_blocks(text, start_idx):
    depth = 0
    i = start_idx
    while i < len(text):
        c = text[i]
        if c == '"':
            i += 1
            while i < len(text) and text[i] != '"':
                if text[i] == '\\':
                    i += 1
                i += 1
        elif c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return text[start_idx:i+1]
        i += 1
    return None

pcb_path = sys.argv[1]
out_dir = sys.argv[2]
lib_prefix = sys.argv[3] if len(sys.argv) > 3 else None

with open(pcb_path, encoding='utf-8') as f:
    text = f.read()

os.makedirs(out_dir, exist_ok=True)

i = 0
extracted = {}
while True:
    idx = text.find('(footprint "', i)
    if idx < 0:
        break
    block = extract_blocks(text, idx)
    if block is None:
        break
    m = re.match(r'\(footprint "([^"]+)"', block)
    full_name = m.group(1)
    if ':' in full_name:
        lib, name = full_name.split(':', 1)
    else:
        lib, name = '', full_name
    match = (lib_prefix is None) or (lib == lib_prefix)
    if match and name not in extracted:
        block_new = block.replace('(footprint "%s"' % full_name, '(footprint "%s"' % name, 1)
        extracted[name] = block_new
    i = idx + len(block)

for name, block in extracted.items():
    fn = os.path.join(out_dir, name + '.kicad_mod')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(block + '\n')
    print('cree:', fn)

print('%d empreinte(s) unique(s) extraite(s) de %s' % (len(extracted), pcb_path))
