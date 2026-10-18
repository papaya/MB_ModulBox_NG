#!/usr/bin/env python3
"""Extrait les symboles embarqués (lib_symbols) d'un .kicad_sch
vers un fichier .kicad_sym, en filtrant par préfixe de bibliothèque."""
import sys, re

def extract_blocks(text, start_idx):
    """Extrait le bloc S-expression équilibré commençant à start_idx ( '(' )."""
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

def extract_symbols(sch_path, lib_prefix, out_path):
    with open(sch_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # localiser la section lib_symbols
    ls = text.find('(lib_symbols')
    if ls < 0:
        print("Pas de section lib_symbols")
        return 0
    lib_block = extract_blocks(text, ls)
    if lib_block is None:
        print("Bloc lib_symbols mal formé")
        return 0
    # trouver chaque symbole enfant de premier niveau
    out_syms = []
    i = 0
    while True:
        idx = lib_block.find('(symbol "', i)
        if idx < 0:
            break
        block = extract_blocks(lib_block, idx)
        if block is None:
            break
        m = re.match(r'\(symbol "([^"]+)"', block)
        name = m.group(1)
        if name.startswith(lib_prefix + ':'):
            short = name[len(lib_prefix)+1:]
            # renommer le symbole racine sans le préfixe de lib
            block_new = '(symbol "' + short + '"' + block[len('(symbol "' + name + '"'):]
            out_syms.append(block_new)
        i = idx + len(block)
    if not out_syms:
        print(f"Aucun symbole avec préfixe '{lib_prefix}:'")
        return 0
    content = '(kicad_symbol_lib\n  (version 20231120)\n  (generator "audit_extract")\n  (generator_version "9.0")\n'
    for s in out_syms:
        # indenture de base
        content += '  ' + s.replace('\n', '\n  ').rstrip() + '\n'
    content += ')\n'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"{len(out_syms)} symbole(s) '{lib_prefix}:*' extrait(s) -> {out_path}")
    for s in out_syms:
        m = re.match(r'\(symbol "([^"]+)"', s)
        print("  -", m.group(1))
    return len(out_syms)

if __name__ == '__main__':
    extract_symbols(sys.argv[1], sys.argv[2], sys.argv[3])
