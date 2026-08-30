samples = ((2 + 3j, 5 - 7j), (1j, -1j), (4 - 2j, -4 + 2j))

for a, b in samples:
    t = a + b
    odd = a - b
    assert (t + odd) / 2 == a
    assert (t - odd) / 2 == b
    corners = (a, b, a.conjugate(), b.conjugate())
    assert corners[2] == ((t + odd) / 2).conjugate()
    assert corners[3] == ((t - odd) / 2).conjugate()

a = 2 + 3j
b = -a
determinant = a * b.conjugate() - b * a.conjugate()
assert determinant == 0
assert a + b == 0
assert a != 0 and b != 0

print("four_corner_values=two_complex_degrees")
print("conjugation_port=scalar_redundant")
print("zero_square_rank=one")
print("next_nonredundant_rung=constructor_path_2_cell")
