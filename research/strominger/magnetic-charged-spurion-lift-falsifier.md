# Charged spurions repair typing but do not create the magnetic kernel

At the rational interference point

\[
(g,d)=\left(6,\frac{17}{3}\right),
\]

the three candidate full path columns have intrinsic deck charges

\[
(2,1,1)\pmod 3.
\]

The minimal compensating spurions have charges

\[
(1,2,2)\pmod 3,
\]

so every adapted column is neutral. This is a valid typing repair.

It does not create a kernel. Let \(F\) be the full fractional path matrix and
let \(S=\operatorname{diag}(s_0,s_1,s_2)\). Exact construction of \(F\)
exhibits a nonzero three-by-three minor \(\Delta\). The corresponding minor
after adaptation is

\[
\det(FS)_I=\Delta s_0s_1s_2.
\]

Therefore every fiber with nonzero spurions still has rank three. A zero
spurion can reduce rank only by deleting a source route; that is route loss,
not activation of the rational destructive-interference state.

The local residual packet behaves differently. Its two weighted amplitudes
are equal and opposite, so adapted cancellation imposes one projective ratio
on the spurions. But this local relation does not annihilate the full path
matrix. The integer-tail elimination that produced the residual coordinate
has no fractional-tail lift.

There is also a selector defect. Three nonzero spurion trivializations modulo
common scale form

\[
(\mathbb G_m)^3/\mathbb G_m.
\]

This has two projective ratios. Residual cancellation fixes one and leaves one
free modulus. Thus the Flavor transfer predicts correctly that typing repair
reopens a selection problem, but the magnetic case is more restrictive: no
choice inside the invertible spurion torsor creates the full kernel at all.

The missing constructor must be non-diagonal. It must change the transport
matrix, add a charged target quotient, or supply a charged tail
correspondence. A charged scalar multiplier alone is insufficient.

Replay:

`python research/strominger/checkers/magnetic_charged_spurion_lift_checks.py`
