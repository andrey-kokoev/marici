# Canonical messenger-tensor grammar

## Frozen shapes

WP492 freezes the ten tensor shapes required by WP491, separately in the up
and down Standard Model charge sectors. Spectator color and flavor identities
are factored out.

The canonical shapes are:

- \(Y_H\): the normalized cyclic fixed vector \((1,1,1)/\sqrt3\);
- \(Y_S\): componentwise connector incidence
  \(\delta_{\alpha\beta}\delta_{ij}\);
- \(Y_X\): the oriented-port dot \(\delta_{ij}\);
- \(Z_A\): identity on cyclic entrance labels;
- \(Z_B\): identity on oriented-port labels.

The up/down shapes are identical but their ten scalar normalizations remain
independent RG coordinates. No coefficient value is chosen from a desired
fixed point.

## Authority partition

The cyclic entrance direction is uniquely fixed, and the \(SO(3)_P\) dot and
symmetric port mass have one-dimensional invariant shape spaces. Those shapes
are symmetry forced.

Cyclic symmetry alone is weaker on the entrance side. Its general intertwiner
commutant has dimension three, and its symmetric mass commutant has dimension
two. Therefore componentwise \(Y_S\) incidence and identity \(Z_A\) require an
explicit diagonal-incidence locality axiom. The packet declares that axiom; it
does not misreport it as a theorem of cyclic symmetry.

## Exact contraction data

With the stated normalization, the shape Frobenius norms squared are

\[
\lVert Y_H\rVert^2=1,
\quad \lVert Y_S\rVert^2=9,
\quad \lVert Y_X\rVert^2=3,
\quad \lVert Z_A\rVert^2=\lVert Z_B\rVert^2=3.
\]

This removes WP491's tensor-shape ambiguity. It does not yet provide the ten
scalar normalizations, retained quartics and Standard Model couplings, scheme,
loop order, or finite threshold maps. The beta vector field must be derived
from those frozen inputs before any fixed-point search.
