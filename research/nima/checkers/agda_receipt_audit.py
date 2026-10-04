"""Source-bound verification shared by the headless Agda proof packets."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
OWNER = ROOT / 'research/nima'
IMPORT = re.compile(r'^\s*(?:open\s+)?import\s+([\w.]+)', re.MULTILINE)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().lower()


def verify_receipt(module, stem, negative_modules):
    receipt_path = OWNER / 'results' / (stem + '-formal-audit.json')
    receipt = json.loads(receipt_path.read_text(encoding='utf-8-sig'))
    schema = ('marici.nima.graded-boundary-coherence-formal-audit.v1'
              if module == 'GradedBoundaryCoherence' else 'marici.nima.agda-proof-packet.v1')
    assert receipt['schema'] == schema
    assert receipt['module'] == module
    assert receipt['passed'] and receipt['positive_exit_code'] == 0
    assert receipt['ignore_interfaces'] and receipt['inputs_stable_during_check'] and receipt['no_new_window']
    assert '--ignore-interfaces' in receipt['args']
    assert Path(receipt['args'][-1]) == OWNER / 'agda' / (module + '.agda')
    assert digest(Path(receipt['command'])) == receipt['compiler_sha256'].lower()
    assert digest(OWNER / 'checkers/check_graded_boundary_coherence.ps1') == receipt['checker_sha256'].lower()

    # Follow local imports of the formal root and rejection controls. All
    # Cubical sources are checked separately against the complete inventory.
    pending = [module + '.agda'] + ['negative/' + name + '.agda' for name in negative_modules]
    visited = set()
    while pending:
        name = pending.pop()
        if name in visited:
            continue
        visited.add(name)
        source = OWNER / 'agda' / name
        assert digest(source) == receipt['owner_source_inventory_sha256'][name].lower(), name
        for imported in IMPORT.findall(source.read_text(encoding='utf-8-sig')):
            relative = imported.replace('.', '/') + '.agda'
            if (OWNER / 'agda' / relative).is_file():
                pending.append(relative)
    for name, expected in receipt['library_source_inventory_sha256'].items():
        assert digest(Path(receipt['library']) / name) == expected.lower(), name
    controls = receipt['controls']
    assert {c['module'] for c in controls} == set(negative_modules)
    for control in controls:
        assert control['exit_code'] != 0 and control['correctly_rejected']
        text = (OWNER / 'results' / ('agda-' + control['module'] + '.log')).read_bytes()
        assert b'[UnequalTerms]' in text and b'false' in text and b'true' in text
    return {'source_bound_receipt_sha256': digest(receipt_path), 'local_sources_checked': sorted(visited)}
