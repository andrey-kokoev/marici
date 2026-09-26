"""SCC audit of the recorded fresh Agda check; never invokes a compiler."""
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / 'research/nima/results'
NAMES = ('SourceRelativeComparisonCompletenessRegression.agda',
         'SourceRelativeComparisonCompleteness.agda',
         'SigmaPiComparisonDecomposition.agda', 'WholePackageSigmaPi.agda',
         'ProofRelevantCoherenceClosure.agda', 'IndexIdentityCoherence.agda',
         'IndexIdentityCoherenceRegression.agda')

def errors(receipt):
    found = []
    if receipt.get('schema') != 'marici.nima.agda-check.v1': found.append('wrong receipt schema')
    if receipt.get('module') != 'SourceRelativeComparisonCompletenessRegression': found.append('wrong target')
    if receipt.get('passed') is not True or receipt.get('exit_code') != 0: found.append('compiler did not pass')
    if receipt.get('ignore_interfaces') is not True: found.append('closure not freshly checked')
    for name in NAMES:
        actual = hashlib.sha256((ROOT / 'research/nima/agda' / name).read_bytes()).hexdigest()
        if receipt.get('owner_source_inventory_sha256', {}).get(name) != actual:
            found.append('stale or absent digest: ' + name)
    return found

receipt = json.loads((RESULTS / 'agda-SourceRelativeComparisonCompletenessRegression.json').read_text(encoding='utf-8-sig'))
found = errors(receipt)
for mutation in ('stale-source', 'failed-compiler'):
    bad = copy.deepcopy(receipt)
    if mutation == 'stale-source': bad['owner_source_inventory_sha256'][NAMES[1]] = '0' * 64
    else: bad['passed'] = False
    assert errors(bad), 'bad receipt accepted: ' + mutation
result = {'schema': 'marici.nima.source-relative-receipt.v1',
          'passed': not found, 'errors': found,
          'classification': 'checked_witness_completeness_relative_to_named_boundary_theory',
          'source_files_audited': len(NAMES), 'negative_receipt_checks': 2,
          'global_resolution_law_basis_complete': False,
          'scope': 'Audit of compiler receipt and owner source digests, not a substitute for Agda.'}
(RESULTS / 'source-relative-receipt.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
raise SystemExit(0 if not found else 1)
