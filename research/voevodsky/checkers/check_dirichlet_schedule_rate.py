"""Exact ideal-series obstruction; does not evaluate Agda exp/log terms."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
AGDA = ROOT / 'research/voevodsky/agda'

def index(k):
    value = 0
    for _ in range(k):
        value = 1 + value + value
    return value

def precision(k):
    return F(1, 2**k)

def main():
    m, n = 7, 9
    # includedThrough counts zero-based successor indices, inclusively.
    first_count, last_count = index(m + 1) + 1, index(n + 1) + 1
    block = range(first_count + 1, last_count + 1)
    lower = F(1, 32768)
    # For positive ideal term t_j = j^(-3/2), t_j^2 = 1/j^3.
    squared_margins = [1 - lower**2 * j**3 for j in block]
    assert len(squared_margins) == 768
    assert min(squared_margins) >= 0
    block_lower = len(squared_margins) * lower
    budget = precision(m) + precision(n)
    # CONDITIONAL endpoint comparison errors, not proved for Agda terms.
    endpoint_errors = precision(m + 2) + precision(n + 2)
    residual = block_lower - budget - endpoint_errors
    assert block_lower == F(3, 128)
    assert residual == F(23, 2048) and residual > 0
    invalid_lower = F(1, 1024)
    negative_residual = 1 - invalid_lower**2 * last_count**3
    assert negative_residual == -1023  # Deliberately false bound is rejected.
    files = ['RationalLogConvergenceContract.agda', 'RegularCauchyStructure.agda',
             'CanonicalDirichletTriangularApproximation.agda',
             'CanonicalDirichletRegularPartialSum.agda']
    result = {
        'schema': 'marici.dirichlet-schedule-rate.v1',
        'passed': True, 'arithmetic': 'exact Python Fraction; no external dependencies',
        'source_sha256': {p: hashlib.sha256((AGDA / p).read_bytes()).hexdigest() for p in files},
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'ideal_exponent': '3/2', 'stages': [m, n],
        'term_counts': [first_count, last_count], 'block_cardinality': len(squared_margins),
        'term_lower': str(lower), 'block_lower': str(block_lower),
        'required_budget': str(budget), 'conditional_endpoint_error_sum': str(endpoint_errors),
        'conditional_obstruction': str(residual),
        'negative_control_squared_margin': str(negative_residual),
        'verified': 'Ideal positive power-series block exceeds the prescribed Cauchy budget.',
        'not_verified': ['Agda exp/log identification with ideal positive powers',
                         'Agda endpoint approximants within the assumed ideal-sum errors',
                         'Inhabitation or impossibility of CanonicalDirichletCauchyBoundary'],
    }
    output = ROOT / 'research/voevodsky/results/dirichlet_schedule_rate.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
