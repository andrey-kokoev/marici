"""Exact finite checks for the Krein graph completion theorem."""

import sympy as sp

identity = sp.eye(3)

strict = sp.diag(sp.Rational(1, 2), sp.Rational(2, 3), sp.Rational(3, 4))
strict_graph_metric = identity - strict.T * strict
assert all(strict_graph_metric[:index, :index].det() > 0 for index in range(1, 4))
assert strict_graph_metric.det() > 0

threshold = sp.diag(1, sp.Rational(2, 3), sp.Rational(3, 4))
threshold_graph_metric = identity - threshold.T * threshold
assert threshold_graph_metric.det() == 0
assert threshold_graph_metric.rank() == 2

hostile = sp.diag(sp.Rational(5, 4), sp.Rational(2, 3), sp.Rational(3, 4))
hostile_graph_metric = identity - hostile.T * hostile
assert any(value < 0 for value in hostile_graph_metric.eigenvals())

# Direct Krein restriction equals the graph metric.
a = sp.Matrix(sp.symbols("a0:3", real=True))
krein_norm = (a.T * a - (strict * a).T * (strict * a))[0]
graph_norm = (a.T * strict_graph_metric * a)[0]
assert sp.expand(krein_norm - graph_norm) == 0

print("strict_contraction_graph_positive=True")
print("unit_singular_value_graph_nullity=1")
print("expansive_coupling_graph_indefinite=True")
print("graph_Gram_determinant=det(I-CstarC)")
print("physical_relative_chain_pushforward_constructed=False")

