"""Check divisor matching and Cech obstruction for the odd resonance kernel."""


def boundary_divisor(i_degree, c_degree):
    half = i_degree // 2
    return half, half + c_degree


numerator = boundary_divisor(11, 1)
quartic_relation = boundary_divisor(4, 0)
derived_kernel = tuple(x - y for x, y in zip(numerator, quartic_relation))
intrinsic_odd = boundary_divisor(7, 1)

assert numerator == (5, 6)
assert quartic_relation == (2, 2)
assert derived_kernel == (3, 4)
assert derived_kernel == intrinsic_odd

# On P^1, h^1(O(d))=max(-d-1,0).  The established positive transition
# divisor has degree seven, so there is no Cech H^1 gluing obstruction.
degree = sum(derived_kernel)
h1_dimension = max(-degree - 1, 0)
assert degree == 7
assert h1_dimension == 0

print("numerator divisor: (5,6)")
print("quartic Koszul divisor removed: (2,2)")
print("derived resonance kernel divisor: (3,4)")
print("compactified line: O(7), H1=0")
