#!/usr/bin/env python3
"""Fusionne les symboles extraits de PEC_16_V0.2 dans ksir_2023.kicad_sym."""
import re

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

with open('/tmp/ksir_2023_extract.kicad_sym') as f:
    ext = f.read()

syms = []
i = 0
while True:
    idx = ext.find('(symbol "', i)
    if idx < 0:
        break
    block = extract_blocks(ext, idx)
    if block is None:
        break
    syms.append(block)
    i = idx + len(block)

target = 'Mes_Librairies_KiCad/symbols/ksir_2023.kicad_sym'
with open(target) as f:
    content = f.read()

added = []
for s in syms:
    m = re.match(r'\(symbol "([^"]+)"', s)
    name = m.group(1)
    if re.search(r'_\d+_\d+$', name):
        continue
    if f'(symbol "{name}"' in content:
        print(f"  deja present: {name}, ignore")
        continue
    last = content.rstrip()
    assert last.endswith(')'), "fichier cible mal forme"
    insert_pos = last.rfind(')')
    new_block = '  ' + s.replace('\n', '\n  ').rstrip() + '\n'
    content = last[:insert_pos] + new_block + last[insert_pos:] + '\n'
    added.append(name)

with open(target, 'w') as f:
    f.write(content)

print(f"Symboles ajoutes a ksir_2023.kicad_sym: {added}")
