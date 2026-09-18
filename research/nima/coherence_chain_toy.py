"""Parameterized connected k-phase coherence-chain toy family."""
import sympy as s
from coherence_amplitude import CoherencePhase, CoherenceHistory
from momentum_twistor_super import external_supertwistor, super_five_bracket


def connected_chain(k, x_values=None, z_columns=None):
    """Build the connected chain for a coherent positive moment-curve sequence.

    ``x_values`` may be an iterable of at least ``3*k+2`` increasing values;
    the historical default is x_i=i^2+3i+1.
    """
    if k < 1:
        raise ValueError("phase count must be positive")
    n = 3*k + 2
    xs = ([s.Integer(i*i + 3*i + 1) for i in range(1, n+1)]
          if x_values is None else [s.sympify(x) for x in x_values][:n])
    if len(xs) != n or any(xs[i] >= xs[i+1] for i in range(n-1)):
        raise ValueError("x_values must provide a strictly increasing coherent sequence")
    z = ({i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)}
         if z_columns is None else
         {i:s.Matrix(col) for i,col in enumerate(list(z_columns)[:n],1)})
    if len(z) != n or any(col.shape != (4,1) for col in z.values()):
        raise ValueError("z_columns must provide 3*k+2 four-component columns")
    external = {i:external_supertwistor(i,z[i]) for i in z}
    labels = tuple(tuple(range(1+3*j, 6+3*j)) for j in range(k))
    phases = tuple(CoherencePhase(
        super_five_bracket(tuple(external[i] for i in q)), str(q)) for q in labels)
    component_labels = (
        tuple(1+3*j for j in range(k)),
        tuple(2+3*j for j in range(k)),
        tuple(3+3*j for j in range(k)),
        tuple(1+3*j for j in range(k)),
    )
    return CoherenceHistory(phases), labels, component_labels
