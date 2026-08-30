def dft4(vector):
    roots = (
        (1, 1, 1, 1),
        (1, -1j, -1, 1j),
        (1, -1, 1, -1),
        (1, 1j, -1, -1j),
    )
    return tuple(sum(row[k] * vector[k] for k in range(4)) / 2 for row in roots)


def conjugate(vector):
    return tuple(value.conjugate() for value in vector)


def inverse_dft4(vector):
    return conjugate(dft4(conjugate(vector)))


for vector in ((1, 2j, -3, 4 - 1j), (2, -1, 0, -1)):
    assert conjugate(dft4(conjugate(vector))) == inverse_dft4(vector)

vacuum = (2, -1, 0, -1)
assert conjugate(vacuum) == vacuum
assert dft4(dft4(vacuum)) == vacuum

transported = tuple(
    phase * value for phase, value in zip((1, 1j, -1, -1j), vacuum)
)
left_path = dft4(conjugate(transported))
right_path = conjugate(dft4(transported))
assert left_path != right_path

print("bare_real_fourier_2cell=parity")
print("real_even_vacuum_2cell=trivial")
print("transported_2cell=nontrivial")
print("required_order=source_then_transport_then_compare_then_scalarize")
