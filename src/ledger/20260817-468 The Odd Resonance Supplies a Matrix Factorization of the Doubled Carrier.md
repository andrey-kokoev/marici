---
id: 468
date: 2026-08-17
title: The Odd Resonance Supplies a Matrix Factorization of the Doubled Carrier
---

# The Odd Resonance Supplies a Matrix Factorization of the Doubled Carrier

Benincasa Entry 467 proves that ordinary reduction to (z^2=0) is mistyped:
the exact image is contained in ((z)), not in ((z^2)).  The doubled carrier
must therefore be represented by

\[
[\mathcal O\xrightarrow{z^2}\mathcal O]
\]

and the lift requires an explicit homotopy.

Entry 464 gives the normalized odd first-Cartier symbol in its intrinsic
boundary frame:

\[
d_-=-6z.
\]

It has the unique scalar linear complement

\[
h_-=-\frac z6,
\]

and the two compositions satisfy

\[
d_-h_-=z^2,
\qquad
h_-d_-=z^2.
\]

Thus the odd resonant block supplies the matrix factorization

\[
\boxed{(-6z,-z/6)}
\]

of the doubled-carrier equation.  This is precisely the derived coherence cell
missing from an ordinary cokernel map.

The construction is global across (b=\pm1).  The divisor
(3[1]+4[-1]) belongs to the odd frame
(eta_-=a t^3(b+1)); relative to that frame, both (-6) and (-1/6) are
units.  Hence the matrix factorization has no boundary-supported defect.

This should not be collapsed to ordinary homology over
(mathbb Q[z]/(z^2)).  The resulting two-periodic complex is totally acyclic
as a module complex but represents nontrivial singularity/derived-support data.
That is exactly why ordinary reduced nearby cycles see the anti-invariant line
while the doubled-carrier comparison requires extra coherence.

The even block is different.  Its first-Cartier symbol is zero, and no scalar
map (h_+) can satisfy (0\cdot h_+=z^2).  Therefore the odd derived cell is
complete, but the full homotopy fiber still requires the even carrier map or a
higher term from the complete complex.

The next gate is to construct that even derived cell and assemble both blocks
into the homotopy fiber of carrier reduction.

The executable audit is
research/voevodsky/check_soft_axis_odd_matrix_factorization.py.
