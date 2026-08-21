# The Literal Euclidean Chain Misses the Gram Vertical Excess

The Tor-one character gate identifies where an invariant Gysin map could
land, but the literal physical chain must first meet the supported locus.

For two independent real planar vectors \(a,b\), their Gram matrix

\[
H=\begin{pmatrix}a^2&a\cdot b\\a\cdot b&b^2\end{pmatrix}
\]

is positive definite. With \(d=(a^2,b^2)^T\), the Kummer radicand is

\[
R=d^T\operatorname{adj}(H)d
=
\det(H)\,d^TH^{-1}d.
\]

For a nontrivial independent pair,

\[
\det(H)>0,
\qquad
d^TH^{-1}d>0,
\]

and therefore

\[
\boxed{R>0.}
\]

The vertical excess equation

\[
w^2+R=0
\]

has no real solution. Geometrically, the planar circumcenter has positive
squared radius, and making the loop point null requires an imaginary normal
displacement.

Consequently the literal Euclidean chamber used in Benincasa Entry 1217 does
not meet this vertical excess:

\[
\boxed{
\Gamma_{\rm Euclidean}\cap\{w^2+R=0\}=\varnothing.
}
\]

The complex supported coefficient complex remains mathematically valid, and
the Tor-one orientation gate remains the correct necessary condition for a
continued Gysin map. But nonzero physical activation would require an
independently specified complex contour continuation or relative chain. It is
not supplied by the literal real sheet \(y_i\ge0\).

This closes the frozen Euclidean branch without discarding the complex
nearby-cycle object:

- algebraic vertical excess: present;
- derived Tor/character packet: present;
- literal Euclidean-chain pairing: zero by empty support;
- analytically continued pairing: unresolved and requires new chain data.

The exact checker exhausts 2,112 ordered independent integer plane bases in
the box \([-3,3]^2\), verifying positive \(\det H\) and positive \(R\) in
every case as a finite regression of the proof.

Artifacts:

- `research/nima/check_rank_two_vertical_excess_real_support.py`
- `research/nima/results/rank-two-vertical-excess-real-support.json`
