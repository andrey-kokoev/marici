"""Validate the fresh completed-arithmetic proof receipt, without launching Agda."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
OWNER = ROOT / 'research/nima'
SOURCES, RESULTS = OWNER / 'agda', OWNER / 'results'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().lower()


def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def main():
    audit_path = RESULTS / 'completed-component-arithmetic-formal-audit.json'
    positive_path = RESULTS / 'agda-NativeRationalComponentArithmetic.json'
    audit, positive = load(audit_path), load(positive_path)
    assert audit['fresh'] and positive['ignore_interfaces']
    assert positive['passed'] and positive['exit_code'] == 0
    assert audit['positive_receipt_sha256'].lower() == digest(positive_path)
    assert audit['checker_sha256'].lower() == digest(OWNER / 'checkers/check_completed_component_arithmetic.ps1')
    assert positive['source_sha256'].lower() == digest(SOURCES / 'NativeRationalComponentArithmetic.agda')
    checked = {}

    def visit(name):
        path = SOURCES / (name.replace('.', '/') + '.agda')
        if not path.is_file() or name in checked:
            return
        checked[name] = digest(path)
        assert checked[name] == positive['owner_source_inventory_sha256'][path.name].lower(), name
        for dependency in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)', path.read_text(encoding='utf-8'), re.M):
            visit(dependency)

    visit('NativeRationalComponentArithmetic')
    expected = {
        'ComponentZeroDenominator': ['[InstanceNoCandidate]', 'Constraint 0'],
        'ComponentBadFractionCancellation': ['[UnequalTerms]', '6 != 4'],
        'ComponentBadSignedCancellation': ['[UnequalTerms]', '0 != 1'],
        'ComponentBadScalarReadout': ['[UnequalTerms]', '3600 != 4200'],
    }
    assert {item['module'] for item in audit['controls']} == set(expected)
    logs = {}
    for item in audit['controls']:
        name = item['module']
        assert item['correctly_rejected'] and item['exit_code'] != 0
        assert item['expected_markers'] == expected[name]
        assert item['source_sha256'].lower() == digest(SOURCES / 'negative' / (name + '.agda'))
        log_path = RESULTS / ('agda-' + name + '.log')
        log = log_path.read_text(encoding='utf-8-sig')
        assert all(marker in log for marker in expected[name])
        logs[name] = digest(log_path)
    result = {
        'schema': 'marici.nima.completed-component-arithmetic-receipt.v1',
        'status': 'pass',
        'formal_audit_sha256': digest(audit_path),
        'checker_sha256': digest(Path(__file__)),
        'local_import_closure': checked,
        'negative_control_log_sha256': logs,
        'scope': audit['scope'],
        'not_verified': ['geometric free-component hypothesis', 'physical weight descent from the full Carrier', 'arbitrary-n Python compiler correctness'],
    }
    (RESULTS / 'completed-component-arithmetic-receipt.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
