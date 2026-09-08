# 1837 — The Polar Active-Soft Section Is a Morse–Bott Focal Segment

## Correction to the naive weighted picture

Entry 1836 isolated the polar section

\[
1+u\cdot n=0.
\]

This means that the loop point leaves one focus directly toward the other
focus in the same region wall.  Along the open focal segment,

\[
\boxed{
|\ell-C_e|+|\ell-C_b|=|C_b-C_e|.
}
\]

The radial dependence does not merely begin quadratically; it vanishes
identically along the segment.  The correct object is Morse--Bott.

## Transverse normal form

Let \(s\in(0,R)\) be distance along a focal segment of length \(R\), and let
\(\rho\in\mathbb R^2\) be transverse.  Then

\[
|\ell-C_e|+|\ell-C_b|
=
R+\frac{R}{2s(R-s)}|\rho|^2+O(|\rho|^4).
\]

Thus the owner wall has local form

\[
q_1
=
\delta+\kappa(s)|\rho|^2+O(|\rho|^4),
\qquad
\kappa(s)>0.
\]

If the second region wall cuts the segment transversely,

\[
\partial_s q_2\ne0,
\]

then taking its residue leaves

\[
u\,
\frac{d^2\rho}{\delta+\kappa|\rho|^2+\cdots},
\qquad u\ne0.
\]

The generic polar collision therefore produces an ordinary grade-zero
logarithmic line, rather than Entry 1836's generic-direction second-Rees line.

## Classification

Both ingredients are already frozen carrier data:

- the occurrence-resolved edge-soft endpoint;
- the second labelled region wall.

The focal segment and its transverse Morse coefficient arise from their
physical distance geometry.  No new carrier stratum is required.

## Qualifications

This is a conditional local normal form.  It does not prove that the
dehomogenized physical discriminant reaches the polar section.  If it does and
\(\partial_s q_2=0\), a deeper tangency remains and must be retained as an
excess complex rather than normalized away.

## Next falsifier

Solve the polar boundary equations on the focal segment.  Determine whether
the second wall has a real transverse zero, a tangential zero, or no zero for
the source-compatible deformations.  Only the first two activate the polar
coefficient.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_polar_soft_morse_bott.py`
- `research/benincasa/results/five-site-region-pair-polar-soft-morse-bott.json`
- Entry 1836
- allocator claim: `seqclaim-22d6ef5c4bbe17c9f780e9a1`