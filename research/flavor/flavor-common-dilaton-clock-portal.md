# Common-dilaton flavor-clock portal

## Source operation

WP467 repairs WP466's independent relevant-deformation kernel by making the
electroweak and flavor order parameters relational outputs of one dynamical
real singlet `sigma`. With canonical kinetic terms, consider

\[
V=\lambda\sum_{i<j}\left\lVert
[X_i,X_j]-iy\sigma\epsilon_{ijk}X_k
\right\rVert_F^2
+\rho\left(\sum_i\operatorname{Tr}X_i^2-6y^2\sigma^2\right)^2
+\eta\left(H^\dagger H-a\sigma^2\right)^2,
\]

where `lambda`, `rho`, `eta`, `y`, and `a` are positive. Every summand has
canonical dimension four. The action is gauge invariant, contains no measured
flavor coordinate, and preserves the oriented adjoint-triplet geometry of
WP447.

## Exact zero-energy family

For any nonzero `sigma`, the irreducible spin-one configuration

\[
X_i=y\sigma J_i,
\qquad H^\dagger H=a\sigma^2
\]

annihilates every square. Positivity makes it a global minimum. The flavor norm
and electroweak convention `v^2=2H^dagger H` give

\[
f^2=6y^2\sigma^2,qquad v^2=2a\sigma^2,qquad
{g_Ff\over v}=g_Fy\sqrt{3\over a}.
\]

The flat common dilation of `sigma` remains, but it cancels from the requested
dimensionless clock ratio. Thus this operation genuinely removes WP466's
independent `mu/v` scale fiber.

## Selector boundary

For fixed source coefficients `(g_F,y,a)`, the portal selects a proper
relational subspace with one value of `g_F f/v`; it is not a texture
rigidifier. It descends under the full weak-basis groupoid because it uses only
simultaneous-conjugation norms and the Higgs singlet norm.

It does not yet select a numerical value. The exact coefficient-hostile pair
`(y,a)=(1,1)` and `(1,3)` gives respectively `sqrt(3) g_F` and `g_F` while both
actions satisfy the same declared symmetries and positivity conditions. The
selector has therefore moved the remaining freedom from a relevant scale to
dimensionless source coefficients.

The `sigma` radial direction is also flat at tree level. This does not spoil
the ratio selection, but it means the absolute pole masses still lack detector
units until dimensional transmutation or another independently fixed relevant
deformation chooses the common scale.

## Classification and next gate

- Operation: source-derived relational selector for `g_F f/v`, conditional on
  `(g_F,y,a)`.
- Presentation effect: none.
- Physical readout: not yet; no singlet/Higgs mixing spectrum, decay widths,
  or calibrated likelihood is attached.
- Smallest exact falsifier of numerical selection: the coefficient pair above.
- Successor: derive or fix `(g_F,y,a)` through the complete coupled RG/source
  geometry, determine the common radial scale, compute the enlarged Hessian
  and pole residues, and then recompute flavor-current and collider likelihoods
  in that same domain.

