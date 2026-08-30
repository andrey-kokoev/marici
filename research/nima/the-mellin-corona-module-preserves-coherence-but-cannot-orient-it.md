# The Mellin Corona Module Preserves Coherence but Cannot Orient It

## The smallest phase hostile

Take two positive amplitudes \(a,b\), and form

\[
v_+=
\begin{pmatrix}
a\\ b
\end{pmatrix},
\qquad
v_-=
\begin{pmatrix}
a\\ -b
\end{pmatrix}.
\]

Their seam carriers are

\[
K_+=v_+v_+^*,
\qquad
K_-=v_-v_-^*.
\]

They differ only in the sign of the cross-prime entries:

\[
K_\pm=
\begin{pmatrix}
a^2&\pm ab\\
\pm ab&b^2
\end{pmatrix}.
\]

The diagonal unitary \(V=\operatorname{diag}(1,-1)\) satisfies

\[
K_-=VK_+V^*.
\]

For two distinct primes \(p,q\), this phase reversal occurs on their Mellin
orbit at a parameter satisfying

\[
t\log(q/p)=\pi.
\]

It is therefore not an alien matrix mutation. It is already contained in the
source-derived comparison flow on the two-label subsystem.

## Every canonical corona invariant agrees

Both carriers are positive rank one and have the same:

- trace and determinant;
- operator, trace, and Hilbert--Schmidt norms;
- labelled diagonal;
- Mellin conditional expectation;
- prime-harmonic corona mass.

Their residuals

\[
R_\pm=K_\pm-\mathbb E_{\mathrm M}(K_\pm)
\]

have opposite off-diagonal signs but the same spectrum and norm.

Consequently any law built only from positivity, trace, Schatten norms, Haar
averaging, or the fixed-point diagonal cannot distinguish the two
orientations.

## Exact no-go statement

The Mellin corona architecture is coherence-complete but orientation-blind:

1. it retains the magnitude of the nontrivial character sector;
2. it retains the fact that inverse-frequency channels correlate;
3. it does not select a preferred phase representative on a Mellin orbit.

This is appropriate for a Haar state. Haar invariance and phase orientation
are incompatible unless another source object breaks or points the symmetry.

The result blocks a tempting but circular step. Positivity of the seam carrier
cannot orient its cross term relative to endpoint and gamma channels, because
both signs occur among unitarily equivalent positive carriers.

## What additional constructor would be sufficient

An orientation mechanism must supply more than the current corona module. It
must define a source-rooted covariant reference that transforms with the
Mellin action while permitting a phase-neutral comparison. Equivalently, it
must provide one of:

1. a pointed section of the Mellin torsor;
2. a second channel carrying the inverse character and a fixed source pairing;
3. an endpoint or archimedean incidence map whose relative phase is derived
   before Haar projection.

A fixed scalar phase chosen after completion is not admissible. Neither are
zero locations, completed positivity, or a fitted sign of the residual.

## Finite falsifier

The pair \(K_+,K_-\) is the minimum falsifier. Any proposed orientation law
using only the declared corona invariants must return the same verdict on
both. If it returns different verdicts, inspect which undeclared phase frame
entered the calculation.

