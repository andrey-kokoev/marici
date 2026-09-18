"""Minimal compositional model for amplitude phases in coherence space.

A phase carries one degree-four Grassmann weight. A two-phase history is
composition by exterior multiplication; chart Jacobians are scalar weights;
multiple lifts of one history are combined by branch summation.
"""
from dataclasses import dataclass
from itertools import permutations, product
import sympy as s
from momentum_twistor_super import (
    multiply_super_five_brackets,
    super_five_bracket_product_component,
)


@dataclass(frozen=True)
class CoherencePhase:
    weight: dict
    name: str = ""


@dataclass(frozen=True)
class CoherenceHistory:
    phases: tuple
    jacobian: s.Expr = s.Integer(1)
    branch: str = "rational"

    def __post_init__(self):
        if not self.phases:
            raise ValueError("a history requires at least one phase")

    def full_weight(self):
        """Materialize a two-phase degree-eight exterior weight."""
        if len(self.phases) != 2:
            raise ValueError("full materialization is currently bounded to two phases")
        product = multiply_super_five_brackets(
            self.phases[0].weight, self.phases[1].weight)
        return {m: s.factor(self.jacobian*c) for m, c in product.items()}

    def component(self, labels_by_component):
        """Evaluate one canonical component at arbitrary history depth.

        The antisymmetrization factorizes into four determinants because each
        five-bracket is a fourth tensor power of one fermionic linear form.
        """
        depth = len(self.phases)
        if len(labels_by_component) != 4 or any(len(x) != depth or len(set(x)) != depth for x in labels_by_component):
            raise ValueError("each SU(4) component needs one distinct label per phase")
        linear = []
        normalizations = []
        for phase in self.phases:
            labels = sorted(set().union(*(set(m) for m in phase.weight)), key=str)
            reference = next((r for r in labels if phase.weight.get((r,r,r,r),0) != 0), None)
            if reference is None:
                raise ValueError("phase does not expose a nonzero diagonal component")
            norm = phase.weight[(reference,reference,reference,reference)]
            coeff = {i:s.factor(phase.weight.get((i,reference,reference,reference),0)/norm) for i in labels}
            linear.append(coeff);normalizations.append(norm)
        determinants=[]
        for labels in labels_by_component:
            determinants.append(s.det(s.Matrix([[linear[p].get(label,0) for label in labels] for p in range(depth)])))
        return s.factor(self.jacobian * s.prod(normalizations) * s.prod(determinants))


def sum_history_component(histories, pairs):
    """Descend multiple algebraic lifts by summing the same component."""
    return s.simplify(sum(history.component(pairs) for history in histories))
