"""Run preserved larger-carrier diagnostics without promoting their conclusions.

uv run --with scipy python research/nima/checkers/collect_generation_diagnostics.py
Uses the previously inspected write-suppression loader. No historical receipts
are created. These raw matrices are inputs to an exact source comparison.
"""
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import runpy
from collect_continuum_diagnostics import load

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT/'quarantine/20261007-generation-evidence'
RECEIPTS = ['carrier-minimality.json','subgroup-gram-hierarchy.json',
            'full-12x12-gram.json','gram-from-carrier-geometry.json',
            'symmetry-breaking-hierarchy.json']


def main():
    before = {f: (ROOT/'results'/f).read_bytes() if (ROOT/'results'/f).exists() else None
              for f in RECEIPTS}
    originals = {}
    for name in ['check_small_carriers.py','check_subgroup_gram_hierarchy.py',
                 'check_full_12x12_gram.py','check_gram_from_geometry.py',
                 'check_symmetry_breaking_hierarchy.py']:
        originals[name] = load(ARCHIVE/'checkers'/name)
    try:
        with redirect_stdout(io.StringIO()):
            runpy.run_path(str(ARCHIVE/'checkers/check_larger_carrier.py'))
    except NameError as exc:
        if exc.name != 'json':
            raise
        larger_error = {'type': 'NameError', 'name': exc.name}
    else:
        raise AssertionError('Expected the preserved missing-json defect')
    full = originals['check_full_12x12_gram.py']
    sub = originals['check_subgroup_gram_hierarchy.py']
    after = {f: (ROOT/'results'/f).read_bytes() if (ROOT/'results'/f).exists() else None
             for f in RECEIPTS}
    if before != after:
        raise AssertionError('Historical receipt mutation')
    paths = [Path(__file__).resolve(), ROOT/'checkers/collect_continuum_diagnostics.py']
    paths += [ARCHIVE/'checkers'/name for name in list(originals)+['check_larger_carrier.py']]
    data = {
        'schema': 'marici.nima.generation-diagnostic-transport.v1',
        'evidence_role': 'raw preserved code data, not physical generations or mixing evidence',
        'full_base_gram': full['G_base'].tolist(),
        'subgroup_cross_probe_matrix': sub['M'].tolist(),
        'declared_block_size': 4, 'declared_n': full['n'],
        'up_indices': full['up_indices'], 'down_indices': full['down_indices'],
        'doublet_indices': full['doublet_indices'],
        'larger_script_execution_defect': larger_error,
        'historical_receipts_unchanged': True,
        'source_sha256': {str(p.relative_to(ROOT)).replace('\\','/'):
                          hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    (ROOT/'results/generation-diagnostic-transport.json').write_text(
        json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print('Preserved full numerical implementations executed; old matrices retained; larger-script NameError reproduced; no old receipt writes.')


if __name__ == '__main__':
    main()
