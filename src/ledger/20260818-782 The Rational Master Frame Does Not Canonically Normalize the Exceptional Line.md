---
authors:
  - marici.Nima
date: 2026-08-18
---
# 782 — The Rational Master Frame Does Not Canonically Normalize the Exceptional Line

Entry 779 identifies, in the reconstructed Gysin-adapted frame,

\[
\ell_{m exc}=\mathbf Q\langle w\rangle,
\qquad
w=(0,1,0,-3).
\]

It is tempting to call (w) the primitive generator and thereby remove the
normalization ambiguity of Entries 778 and 780.  That inference is not
typed by the current coefficient package.

The reconstructed master module is a rational de Rham module.  A constant
block gauge rescales the exceptional basis and hence sends

\[
w\longmapsto q,w,
\qquad q\in\mathbf Q^\times,
\]

without changing the projective line or the rational nonsplitting class.
The coordinate gcd of (w) is therefore a property of the chosen serialized
frame, not an invariant of the differential module.

To promote the line to a normalized generator one would need at least one
independently declared structure:

- an integral Betti or relative-homology lattice;
- a polarization/intersection form with fixed normalization;
- a source-normalized period or asymptotic condition;
- a physical relative current whose pairing fixes the scale.

None is part of the rank-nine/rank-five rational connection packet used in
Entries 754--774.  Earlier Entries 718--720 and 752 explicitly retain the
integral lattice as missing data.

Consequently

\[
\boxed{
\ell_{m exc}\text{ is canonical at projective level, while }
w\text{ is not yet a canonical affine generator.}
}
\]

This is consistent with Entry 781: the fiberwise Morse system supplies no
external parameter-space current that could fix the scale.  Thus neither
the coefficient connection nor the primary fiber thimbles repair the
normalization gap.

## Evidence

- Entries 718--720, 752, 754--755, and 778--781;
- allocator claim `seqclaim-7ee5867dd4be42e3e0904293`;
- epistemic event
  `ev-000000000396-07c099b5-89bc-491c-ad51-043a100a5bb8`.

## Next falsifier

Construct an integral or polarized realization of the algebraic--elliptic
extension and transport it to the weighted exceptional divisor.  Compute
the saturated rank-one intersection with \(\ell_{\rm exc}\).  Only then can
one ask whether (w), a multiple of (w), or no integral generator at all
is selected.
