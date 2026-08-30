# The prime ellipse deficit is an exact sum of pairwise phase squares

Event 10292 proved strict interiority abstractly. The gap has an exact
source-positive decomposition suitable for certification.

Write

\[
x_n=\log n,
\qquad
C_n=\cos(\xi x_n),
\qquad
S_n=\sin(\xi x_n),
\]

and

\[
R=\sum_n c_nC_n,
\qquad
I_1=\sum_n c_nx_nS_n,
\]

\[
M_0=\sum_nc_n,
\qquad
M_2=\sum_nc_nx_n^2.
\]

Define the ellipse deficit

\[
\mathcal D(t,\xi)
=
1-\frac{R^2}{M_0^2}-\frac{I_1^2}{M_0M_2}.
\]

Using \(S_n^2+C_n^2=1\),

\[
\begin{aligned}
M_0^2M_2\mathcal D
={}&
M_0
\left[
M_2\sum_nc_nS_n^2-I_1^2
\right]\\
&+
M_2
\left[
M_0\sum_nc_nC_n^2-R^2
\right].
\end{aligned}
\]

Both brackets are weighted variance determinants. Expanding them pairwise
gives the exact identity

\[
\begin{aligned}
M_0^2M_2\mathcal D
=
\sum_{m<n}c_mc_n
\Big[
&M_0(x_mS_n-x_nS_m)^2\\
&+M_2(C_m-C_n)^2
\Big].
\end{aligned}
\]

Hence

\[
\mathcal D(t,\xi)\ge0
\]

is not merely a Cauchy–Schwarz consequence; its failure from saturation is a
sum of explicit two-label incompatibility energies.

## Finite-prime lower bounds

For any finite pair set \(F\),

\[
\mathcal D(t,\xi)
\ge
\frac1{M_0^2M_2}
\sum_{\{m,n\}\in F}
c_mc_n
\Big[
M_0(x_mS_n-x_nS_m)^2
+
M_2(C_m-C_n)^2
\Big].
\]

The single \(2,3\) term is

\[
\delta_{2,3}
=
\frac{c_2c_3}{M_0^2M_2}
\left[
M_0
\big(
(\log2)\sin(\xi\log3)
-
(\log3)\sin(\xi\log2)
\big)^2
+
M_2
\big(
\cos(\xi\log2)-\cos(\xi\log3)
\big)^2
\right].
\]

This term may vanish at isolated nonzero characters, so it is not a global
margin by itself. Adding finitely many prime pairs can cover a compact
character region; the full sum is strictly positive for every \(\xi\ne0\).

## Contact exclusion

At a double contact, the archimedean value-slope point must lie inside the
strictly smaller ellipse

\[
\left(\frac{2\sqrt{\pi t}A}{M_0}\right)^2
+
\frac{
(2\sqrt{\pi t}\,\partial_\xi A)^2
}{
M_0M_2
}
\le
1-\mathcal D(t,\xi).
\]

A certified finite-pair lower bound for \(\mathcal D\) therefore strengthens
the existing contact inequality without evaluating the full oscillatory
prime sum.

This is a concrete realization of the diagonal/glue margin:

- each pair contributes a nonnegative incompatibility square;
- simultaneous saturation would require all prime phases to glue into one
  character frame;
- multiplicative independence forbids that away from \(\xi=0\).

## Next executable audit

On a proposed compact contact box:

1. enclose \(M_0,M_2\);
2. choose a finite prime-pair cover;
3. certify a positive lower bound for the displayed sum;
4. compare the sharpened ellipse with the archimedean contact point.

This converts the qualitative strictness theorem into a finite interval
certificate target.
