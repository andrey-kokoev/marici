"""Check the source-bound fresh Agda receipt; does not replace compilation."""
from pathlib import Path
import hashlib
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--reduction', action='store_true')
options = parser.parse_args()
ROOT = Path(__file__).resolve().parents[3]
OWNER = ROOT / 'research/nima'
receipt_name = 'retained-comparison-reduction-formal-audit.json' if options.reduction else 'retained-comparison-formal-audit.json'
receipt = json.loads((OWNER / 'results' / receipt_name).read_text(encoding='utf-8-sig'))
expected_module = 'RetainedComparisonReduction' if options.reduction else 'RetainedComparisonStructure'
assert receipt['module'] == expected_module
assert receipt['passed'] and receipt['ignore_interfaces'] and receipt['inputs_stable_during_check']
assert receipt['positive_exit_code'] == 0
assert receipt['erasure_control_exit_code'] != 0 and receipt['erasure_control_correctly_rejected']

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().lower()

assert digest(Path(receipt['command'])) == receipt['compiler_sha256'].lower()
assert digest(OWNER / 'checkers/check_retained_comparison.ps1') == receipt['checker_sha256'].lower()
sources = ['RetainedComparisonStructure.agda', 'negative/RetainedComparisonBadErasure.agda']
if options.reduction:
    sources.append('RetainedComparisonReduction.agda')
for name in sources:
    assert digest(OWNER / 'agda' / name) == receipt['owner_source_inventory_sha256'][name].lower()
args = receipt['args']
assert '--ignore-interfaces' in args
include_paths = [Path(args[i + 1]) for i, arg in enumerate(args) if arg == '-i']
library = include_paths[-1]
for name, expected in receipt['library_source_inventory_sha256'].items():
    assert digest(library / name) == expected.lower(), name
negative = (OWNER / 'results/agda-RetainedComparisonBadErasure.log').read_bytes()
assert b'[UnequalTerms]' in negative and b'false' in negative and b'true' in negative
print('PASS: source-bound fresh Cubical Agda check of ' + expected_module + ' and erasure rejection.')
