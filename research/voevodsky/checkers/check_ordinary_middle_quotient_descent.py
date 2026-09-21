"""Exact quotient-descent fixtures; not an analytical Clark certificate."""
import json
import sympy as s

# An isotropic relation is not a radical: changing a lift changes its pairing.
G = s.Matrix([[0, 1], [1, 0]])
k = s.Matrix([1, 0])
t = s.Matrix([0, 1])
assert (k.T * G * k)[0] == 0
assert (k.T * G * t)[0] == 1
assert ((t+k).T * G * t)[0] != (t.T * G * t)[0]

# Model E2/R2 dimensions. Annihilator observers pair perfectly with the quotient.
F = s.eye(8)
K = F[:, :2]
A = s.Matrix.hstack(*(K.T.nullspace()))
Q = F[:, 2:]
assert K.T * A == s.zeros(2, 6)
assert (Q.T * A).rank() == 6
lift_change = s.Matrix(2, 6, lambda i, j: i+j+1)
assert (Q + K*lift_change).T*A == Q.T*A
assert (Q + K*lift_change).T*F != Q.T*F

# Grouping differences in the relation image vanish only against allowed observers.
D = K * s.ones(2, 8)
assert D.T*A == s.zeros(8, 6)
assert D.T*F != s.zeros(8, 8)

print(json.dumps({
    'passed': True,
    'checks': {
        'isotropic_relation_does_not_imply_descent': True,
        'annihilator_observers_are_lift_independent': True,
        'quotient_detection_rank': 6,
        'full_observer_lift_dependence_detected': True,
        'grouping_difference_in_relation_image_annihilated': True,
    },
    'scope': 'Exact abstract descent fixtures, not actual ordinary Clark observations.'
}, indent=2))
