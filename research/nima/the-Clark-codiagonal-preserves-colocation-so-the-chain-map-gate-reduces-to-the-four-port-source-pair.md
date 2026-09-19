# The Clark codiagonal preserves colocation, so the chain-map gate reduces to the four-port source pair

## Clark lifts

The Green observation and characteristic port are

\[
\mathcal O_{\rm Cl}=S_{\rm Cl}\mathcal O_{01},
\qquad
W_{\rm Cl}=W_{01}S_{\rm Cl}^*.
\]

For the canonical rigged transpose,

\[
W_{\rm Cl}^{\times}
=S_{\rm Cl}W_{01}^{\times}.
\]

Therefore

\[
\mathcal O_{\rm Cl}+W_{\rm Cl}^{\times}
=S_{\rm Cl}
\left(
\mathcal O_{01}+W_{01}^{\times}
\right).
\]

Hence the fixed Clark codiagonal introduces no new colocation obstruction.
The characteristic-to-Green chain map exists whenever the underlying
four-port source pair satisfies the oriented relation

\[
\boxed{
\mathcal O_{01}=-W_{01}^{\times}.
}
\]

## Kernel qualification

Because `S_Cl` is a `2 by 4` codiagonal, it has a nontrivial kernel. Thus

\[
S_{\rm Cl}
(\mathcal O_{01}+W_{01}^{\times})=0
\]

does not imply full four-port colocation. It proves only that the defect is
invisible after Clark projection.

For the cone comparison, this distinction matters: the relative kernel of the
four-port packet must be retained. A defect lying in `ker S_Cl` can disappear
from the two scalar Clark outputs while remaining nonzero in the lifted cone.

Therefore the source-strength gate is the unprojected identity

\[
\mathcal O_{01}+W_{01}^{\times}=0,
\]

not merely its codiagonal shadow.

## Relation to confinement

The repository constructs forcing columns and observation rows as distinct
ports. Identifying them by a positive metric would be the known RH-bearing
positive-colocation theorem. The present rigged-transpose identity is weaker
if the pairing is indefinite, but it still requires an independent source
comparison between the characteristic forcing and Green observation systems.

It cannot be obtained by defining either port as the transpose of the other.

## Finite next test

On the four zeroth/first reciprocal moment channels, form the full defect
matrix

\[
D_{01}=\mathcal O_{01}+W_{01}^{\times}.
\]

Test both:

\[
D_{01}=0
\]

and the weaker projected condition

\[
S_{\rm Cl}D_{01}=0.
\]

If only the second holds, the scalar Clark chain square commutes while the
cone-level comparison fails on the retained relative kernel.