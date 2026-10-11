"""Execute the unchanged finite computations under the admitted NumPy profile.

uv run --with scipy python research/nima/checkers/collect_continuum_diagnostics.py

This transports full finite data to the exact SymPy comparison, not a continuum
certificate. Separate admitted dependency profiles avoid an unapproved combined
NumPy/SymPy environment. Only the inspected receipt-write statements are omitted.
"""
import ast
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'quarantine/20261007-continuum-evidence'


def load(path):
    tree = ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
    body = []
    removed = 0
    for node in tree.body:
        if (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Attribute)
                and isinstance(node.value.func.value, ast.Name)
                and node.value.func.value.id == 'out'
                and node.value.func.attr == 'write_text'):
            removed += 1
        else:
            body.append(node)
    if removed != 1:
        raise AssertionError('Expected exactly one known receipt write: ' + str(path))
    tree.body = body
    namespace = {'__file__': str(path), '__name__': '_retained_diagnostic_'}
    with redirect_stdout(io.StringIO()):
        exec(compile(tree, str(path), 'exec'), namespace)
    return namespace


def main():
    receipts = [ROOT/'results/continuum-limit-test.json',
                ROOT/'results/machian-metric-larger-carrier.json']
    before = {str(p): p.read_bytes() if p.exists() else None for p in receipts}
    data = {}
    sources = [Path(__file__).resolve()]
    for version, root in [('original', ARCHIVE), ('current', ROOT)]:
        paths = [root/'checkers/check_continuum_limit.py',
                 root/'checkers/check_machian_metric_larger.py']
        c, g = (load(p) for p in paths)
        data[version] = {
            'direction_matrices': {k: c[k].tolist() for k in ('G', 'vecs')},
            'permutation_matrices': {k: g[k].tolist() for k in ('G4', 'G4_ind', 'G_d4')},
            'grids': {str(L): c['cubic_grid'](L) for L in range(2, 9)},
            'declared_status': [c['result'].get('status'), g['result'].get('status')]}
        sources.extend(paths)
    if before != {str(p): p.read_bytes() if p.exists() else None for p in receipts}:
        raise AssertionError('Historical receipt mutation')
    packet = {
        'schema': 'marici.nima.continuum-diagnostic-transport.v1',
        'evidence_role': 'full finite data from original/current code; not a continuum theorem',
        'source_sha256': {str(p.relative_to(ROOT)).replace('\\', '/'):
                          hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'historical_receipts_unchanged': True, 'data': data}
    out = ROOT/'results/continuum-diagnostic-transport.json'
    out.write_text(json.dumps(packet, separators=(',', ':')) + '\n', encoding='utf-8')
    print('Collected original/current matrices and full grids L=2..8; old receipt paths untouched.')


if __name__ == '__main__':
    main()
