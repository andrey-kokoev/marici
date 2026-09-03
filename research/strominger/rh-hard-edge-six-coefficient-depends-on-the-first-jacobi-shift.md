# The hard-edge coefficient six depends on the first Jacobi shift

## Question

Is the fitted coefficient six forced solely by the \(n^4\) recurrence scale and the \(p=-1\) branch?

Write

\[
a_n=A n^4\left(1+\frac{a_1}{n}+O(n^{-2})\right).
\]

Then

\[
r_n=\frac{a_n}{a_{n+1}}
=1-\frac4n+\frac{10+a_1}{n^2}+O(n^{-3}).
\]

If the alternating recurrence has the exact leading branch \(u_n\sim n^{-1}\), its required defect is obtained directly from

\[
\varepsilon_n
=1+r_n-rac{u_{n+1}}{u_n}
-r_n\frac{u_{n-1}}{u_n}.
\]

Expansion gives

\[
\varepsilon_n
=\frac2{n^2}-\frac{6+a_1}{n^3}+O(n^{-4}),
\]

hence

\[
n^2\varepsilon_n
=2-\frac{6+a_1}{n}+O(n^{-2}).
\]

The coefficient six follows only if the chosen degree coordinate has \(a_1=0\). A shift \(n\mapsto n+\kappa\) changes this first correction, so the coefficient is coordinate-sensitive until the canonical Jacobi indexing and two-term asymptotic are fixed.

## Disposition

Reject an unconditional derivation of six from \(n^4\) scaling alone. The next leaf is `jacobi-first-shift`: determine \(a_1\) in the repository's canonical degree indexing and test whether it vanishes or is absorbed by a source-authorized index shift.

## Claim boundary

The calculation is conditional on the \(p=-1\) branch. It identifies the missing coefficient rather than proving branch selection or the full recurrence expansion.
