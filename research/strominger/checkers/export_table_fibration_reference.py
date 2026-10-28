"""Execute the existing finite reference functions without their report-writing main.
No source equations are rewritten; this is not a fresh Agda compilation.
"""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'research/nima/checkers/check_table_fibration.py'
NAMES = {'normal', 'transpose', 'unique', 'fibrate', 'restore', 'unpack_reversed', 'twice'}

def main(output):
    raw = SOURCE.read_bytes()
    tree = ast.parse(raw.decode('utf-8'))
    definitions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in NAMES]
    assert {node.name for node in definitions} == NAMES
    namespace = {}
    exec(compile(ast.Module(body=definitions, type_ignores=[]), str(SOURCE), 'exec'), namespace)
    cases = []
    for dims in itertools.product(range(3), repeat=3):
        nl, ns, nt = dims
        pairs = tuple(itertools.product(range(ns), range(nt)))
        for assignment in itertools.product(range(-1, nl), repeat=len(pairs)):
            rows = namespace['normal']((label, s, t) for label, (s, t) in zip(assignment, pairs) if label >= 0)
            twice = namespace['twice'](rows, dims)
            cases.append({'dimensions': dims, 'rows': rows, 'sourceFibers': namespace['fibrate'](rows, 1, dims),
                          'twice': twice, 'four': namespace['twice'](twice, (nl, nt, ns))})
    assert len(cases) == 147
    result = {'scope': 'Fresh finite execution of the existing reference functions; no fresh formal compiler closure.',
              'source': str(SOURCE.relative_to(ROOT)).replace('\\', '/'), 'sha256': hashlib.sha256(raw).hexdigest(),
              'functions': sorted(NAMES), 'cases': cases}
    dest = ROOT / output
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {len(cases)} existing finite reference tables exported')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    main(parser.parse_args().output)
