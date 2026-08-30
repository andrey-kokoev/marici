# Common-dilaton Hessian and residue packet

## Frozen benchmark and domain

WP468 freezes the full tree-level scalar curvature data of WP467 before any
phenomenological fit. Canonical kinetic terms are used for the 24 real adjoint
coordinates, four real Higgs coordinates, and the singlet. The source
coefficients are fixed to

\[
\lambda=\rho=\eta=y=a=1,
\qquad \sigma=1,
\]

solely as the declared exact benchmark. This packet does not promote those
coefficient values to numerical source-selection authority.

## Full Hessian theorem

The exact 29-dimensional Hessian has rank 17 and spectrum

\[
0^{\times12},\qquad
16^{\times8},\qquad
36^{\times7},\qquad
206-2\sqrt{10009},\qquad
206+2\sqrt{10009}.
\]

The twelve zero modes are exhausted by eight diagonal-`SU(3)_F` gauge
directions, three electroweak Goldstones, and one common-dilation direction.
Both mixed radial eigenvalues are strictly positive because
`10009 < 103^2`. There are no additional flat or unstable physical modes.

## Exact radial poles and residues

In the canonically normalized ordered channels
`(flavor radial, Higgs radial, singlet)`, the mass-squared block is

\[
R=\begin{pmatrix}
100&0&-100\sqrt3\\
0&4&-4\sqrt2\\
-100\sqrt3&-4\sqrt2&308
\end{pmatrix}.
\]

The checker constructs each spectral projector exactly as a polynomial in
`R`. Its diagonal entries are the pole residues seen by the three declared
radial source channels. The generated JSON records the massless dilaton and
both massive poles without choosing eigenvector signs or chart phases.

The remaining fifteen physical scalar modes have mass squared 16 with
multiplicity eight and 36 with multiplicity seven in singlet-scale units.
Together with WP448's independently frozen flavor-vector triplet/quintet
poles, this supplies a source-separated tree-level spectral packet.

## Instrument boundary

The exact common-dilation pole is physical, not gauge. Consequently the
classically scale-invariant portal is not yet a viable detector model: quantum
scale breaking or an independently admitted relevant deformation must lift or
otherwise physically type this mode. Any such modification requires a new
Hessian and new residues; the present projectors may not be transported across
that change by coordinate analogy.

Widths are also not inferred from curvatures. They require the complete
mass-eigenstate vertices, open-channel thresholds, and a declared
renormalization scheme.

## Smallest falsifiers

- Hessian nullity other than twelve.
- A null direction outside the two gauge orbits and common dilation.
- A nonpositive massive eigenvalue.
- Radial projectors that fail idempotence, orthogonality, or completeness.
- Reusing these residues after lifting the dilaton without recomputation.

