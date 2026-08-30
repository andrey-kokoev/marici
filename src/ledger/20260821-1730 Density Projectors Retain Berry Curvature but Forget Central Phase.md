# 1730 — Density Projectors Retain Berry Curvature but Forget Central Phase

## Complex rotating-kernel test

On a chart of \(\mathbb{CP}^1\), let

\[
|\psi(z)\rangle
=\frac{(1,z)^T}{\sqrt{1+|z|^2}},
\qquad z=x+iy,
\]

and define the rank-one density projector

\[
P=|\psi\rangle\langle\psi|.
\]

A gauge change \(|\psi\rangle\mapsto e^{i\alpha}|\psi\rangle\) leaves \(P\)
unchanged and changes the local Berry connection by \(d\alpha\).

## Curvature from density

Write

\[
P=\frac12(I+n\cdot\sigma).
\]

Then the Berry curvature is reconstructed directly from the projector path:

\[
\boxed{
F=-i\operatorname{Tr}(P,dP\wedge dP)
=\frac12n\cdot(dn\times dn)
=\frac{2,dx\wedge dy}{(1+x^2+y^2)^2},
}
\]

up to the fixed orientation convention.  The checker verifies the cleared
polynomial identity

\[
N\cdot(N_x\times N_y)=4(1+x^2+y^2)^3
\]

for the stereographic numerators.

## Narrow result

Hermitian-square readout forgets the local central phase of an amplitude lift,
but a varying density projector retains the curvature of its tautological
amplitude line.  Hence geometric Berry holonomy is not generally invisible to
density transport; it is recoverable from the path of projectors.

What density cannot recover is an independently tensored flat central local
system with the same projector path.  Entry 1729's real sign is of that type
unless a source connection identifies it with projector-induced transport.

No new Cut carrier stratum is required.

## Durable artifacts

- `research/benincasa/checkers/complex_kernel_berry_curvature.rs`
- `research/benincasa/results/complex-kernel-berry-curvature.json`
- `research/benincasa/complex-kernel-berry-curvature.md`

## Next falsifier

Pair two amplitude lifts with the same projector path but different flat
central twists against a labelled interference reference.  Test whether the
supported comparison recovers the twist or whether it remains physically
invisible.
