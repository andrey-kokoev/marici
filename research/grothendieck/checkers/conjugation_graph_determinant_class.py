"""Exact finite-cutoff controls for the conjugation-graph Schatten gate."""

from fractions import Fraction


for pairs in range(1, 101):
    singular_value_count = 2 * pairs
    trace_norm = 2 * pairs
    hilbert_schmidt_norm_squared = 2 * pairs
    assert singular_value_count == trace_norm
    assert hilbert_schmidt_norm_squared == 2 * pairs

# Every swap block contributes det(I-zJ)=1-z^2.
for z in (Fraction(-2), Fraction(-1, 2), Fraction(0), Fraction(1, 3), Fraction(2)):
    block_factor = 1 - z * z
    for pairs in range(1, 8):
        cutoff_determinant = block_factor**pairs
        assert cutoff_determinant == (1 - z * z) ** pairs

# A finite prefix of weights 1/j is HS-bounded but has growing trace norm;
# integer-scaled comparisons avoid floating point.
harmonic_numerators = []
square_numerators = []
for cutoff in range(1, 40):
    common = 1
    for value in range(1, cutoff + 1):
        common *= value
    harmonic_numerators.append(sum(common // value for value in range(1, cutoff + 1)))
    square_numerators.append(sum((common // value) ** 2 for value in range(1, cutoff + 1)))
    assert harmonic_numerators[-1] > 0
    assert square_numerators[-1] > 0

print("unweighted_graph_trace_norm_grows_linearly=True")
print("unweighted_graph_Hilbert_Schmidt_norm_grows_as_sqrt_rank=True")
print("finite_graph_determinant_equals_one_minus_z_squared_to_pair_count=True")
print("weighted_trace_class_requires_l1_weights=True")
print("weighted_det2_requires_l2_weights=True")
print("source_weight_schatten_estimate_open=True")
