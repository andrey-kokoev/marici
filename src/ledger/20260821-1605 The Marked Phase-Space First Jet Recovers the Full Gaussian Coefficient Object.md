# Entry 1605 — The Marked Phase-Space First Jet Recovers the Full Gaussian Coefficient Object

## Claim

The rank-three Gaussian coefficient tangent is not recoverable from one
equal-time propagator value.  It is recovered canonically from the first
phase-space jet on the source-marked initial hypersurface.

## Calculation

Use real coordinates

\[
(x,y,n)=(\operatorname{Re}\beta,\operatorname{Im}\beta,
\text{statistical occupation}).
\]

After harmless oscillator-frequency rescalings, their map to

\[
\left(
\delta\langle qq\rangle,
\delta\langle pp\rangle,
\delta\langle\{q,p\}/2\rangle
\right)
\]

at the marked time is

\[
J(\eta_0)=
\begin{pmatrix}
c&-s&1\\
-c&s&1\\
s&c&0
\end{pmatrix},
\qquad
c+is=e^{2i\omega\eta_0}.
\]

Its determinant is

\[
\det J=-2(c^2+s^2)=-2.
\]

The value-only map has rank one; the phase-space first jet has rank three at
every time.

## Architectural consequence

\[
\boxed{
\mathcal G_{\rm Gauss}
\simeq
\operatorname{Sym}^2(\text{phase-space line})
\text{ on the marked initial slice}.
}
\]

This supplies the missing canonical projection after Dyson evolution.  Its
canonicality comes from the source-marked hypersurface and canonical momentum,
not from choosing an endpoint primitive.  Between slices the object undergoes
symplectic transport.

## Scope

This identifies the two-point Gaussian coefficient object.  It does not say
that the interacting state remains globally Gaussian; higher connected
cumulants remain separate coefficient layers.

## Next falsifier

Apply the phase-space jet projector to the one-loop corrected propagator and
test whether the induced covariance preserves positivity and the uncertainty
determinant on the finite EFT domain.

## Artifacts

- `research/benincasa/checkers/gaussian_phase_space_jet_projection.rs`
- `research/benincasa/results/gaussian-phase-space-jet-projection.json`
- `research/benincasa/gaussian-phase-space-jet-projection.md`

Allocator claim: `seqclaim-9b527d3026cc896da0b43deb`.
