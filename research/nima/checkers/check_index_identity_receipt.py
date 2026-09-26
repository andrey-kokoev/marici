"""Dependency-free SCC freshness audit; does not invoke or replace Agda."""
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / 'research/nima/results'
SOURCES = ROOT / 'research/nima/agda'
NAMES = ('IndexIdentityCoherenceRegression.agda', 'IndexIdentityCoherence.agda',
         'SigmaPiComparisonDecomposition.agda', 'WholePackageSigmaPi.agda',
         'ProofRelevantCoherenceClosure.agda')

def validate(receipt):
    errors = []
    if receipt.get('schema') != 'marici.nima.agda-check.v1': errors.append('wrong schema')
    if receipt.get('module') != 'IndexIdentityCoherenceRegression': errors.append('wrong target')
    if receipt.get('passed') is not True or receipt.get('exit_code') != 0: errors.append('compiler did not pass')
    if receipt.get('ignore_interfaces') is not True: errors.append('not a fresh closure check')
    for name in NAMES:
        actual = hashlib.sha256((SOURCES / name).read_bytes()).hexdigest()
        if receipt.get('owner_source_inventory_sha256', {}).get(name) != actual:
            errors.append('stale or absent source digest: ' + name)
    return errors

receipt = json.loads((RESULTS / 'agda-IndexIdentityCoherenceRegression.json').read_text(encoding='utf-8-sig'))
errors = validate(receipt)
bad = copy.deepcopy(receipt)
bad['owner_source_inventory_sha256']['IndexIdentityCoherence.agda'] = '0' * 64
assert validate(bad), 'altered source digest was accepted'
bad = copy.deepcopy(receipt)
bad['passed'] = False
assert validate(bad), 'failed compiler receipt was accepted'
report = {'schema': 'marici.nima.index-identity-receipt.v1',
          'status': 'pass' if not errors else 'fail', 'passed': not errors,
          'classification': 'checked_index_transport_and_recursive_comparison_relative_to_declared_index_types',
          'errors': errors, 'checked_source_count': len(NAMES),
          'tampered_and_failed_receipts_refused': True,
          'scope': 'Freshness audit of a recorded Agda check; compiler execution is the separate PS1 runner.',
          'global_resolution_completeness': 'not established'}
(RESULTS / 'index-identity-receipt.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report, indent=2))
raise SystemExit(0 if not errors else 1)
