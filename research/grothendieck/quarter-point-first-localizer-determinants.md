# The first full quarter-point Hausdorff localizers

Let

\[
 S(x)=\frac{\Xi'}{\Xi}\!\left(\frac12+\sqrt{x}\right),
 \qquad
 A_k=\frac{(-1)^k}{k!}S^{(k)}(1/4).
\]

The compact Hausdorff formulation of the scalar RH gate requires positivity
of the ordinary moment matrix and both endpoint localizers for measures on
`[0,4]`.  The previously computed `A_0,A_1,A_2` test the first ordinary
matrix.  Computing `A_3` closes the first nontrivial lower and upper
localizer matrices.

## Fourth source jet

Write `epsilon=s-1`, `h=x-1/4=epsilon+epsilon^2`, and

\[
 L(1+\epsilon)=S(1/4+h)=l_0+l_1\epsilon+l_2\epsilon^2+l_3\epsilon^3+O(\epsilon^4).
\]

With the Stieltjes convention

\[
 \zeta(1+\epsilon)=\epsilon^{-1}+\gamma_0-\gamma_1\epsilon
 +\frac{\gamma_2}{2}\epsilon^2-\frac{\gamma_3}{6}\epsilon^3+O(\epsilon^4),
\]

direct logarithmic differentiation of the completed zeta factors gives

\[
 l_3=-1-\frac23\gamma_3-2\gamma_0\gamma_2-2\gamma_1^2
 -4\gamma_0^2\gamma_1-\gamma_0^4+\frac{\pi^4}{96}.
\]

Series inversion `epsilon=h-h^2+2h^3+O(h^4)` then yields

\[
 \boxed{A_3=-l_3+4l_2-10l_1+20l_0}.
\]

No zero ordinate is used in this source-side formula.

## First complete endpoint-localizer test

The lower-support and upper-support matrices are

\[
 H_u^{(1)}=\begin{pmatrix}A_1&A_2\\A_2&A_3\end{pmatrix},\qquad
 H_{4-u}^{(1)}=
 \begin{pmatrix}
 4A_0-A_1&4A_1-A_2\\
 4A_1-A_2&4A_2-A_3
 \end{pmatrix}.
\]

The dependency-free numerical regression gives

\[
 A_3\approx6.59828\,10^{-10},\qquad
 \det H_u^{(1)}\approx3.83671\,10^{-15},
\]

and

\[
 \det H_{4-u}^{(1)}\approx3.10305\,10^{-8}.
\]

Both signs are positive in ordinary binary arithmetic.  The lower determinant
is exceptionally close to the boundary and is therefore the sharper early
falsifier.  Its sign is **not interval-certified** here; cancellation at this
scale makes interval or exact-real certification the immediate next task.
More precisely, its positive and negative products are approximately
`2.44800e-14` and `2.06433e-14`.  Their subtraction condition number is only
about `11.76`: the small absolute scale comes mainly from the tiny moments,
not from catastrophic cancellation.  A modest directed-rounding enclosure
of the Stieltjes constants should therefore decide this sign.

An exact-rational interval propagation makes that statement quantitative.
If each of `l_0,l_1,l_2,l_3` lies independently within `10^-12` of the
printed center, then

\[
 \det H_u^{(1)}\in[2.5353,5.1381]10^{-15}
\]

and the upper determinant remains above `3.1023e-8`.  Thus the localizer
arithmetic itself is now certified *conditional on four modest input boxes*.
What remains is analytic certification that the completed-zeta coefficients
occupy those boxes; treating printed constants as certified would be circular.

Conditionally on the Hausdorff representation, these determinants are
weighted variance numerators, respectively biased toward the lower and upper
ends of `[0,4]`.  Their positivity is therefore structurally expected under
RH, but checking one finite corner proves neither the representation nor RH.

## Scope

This is an analytic source-jet identity and a binary-float regression.  It is
not a proof of RH, not an interval proof of either decimal sign, and not a
physical relative-chain or readout construction.

## Durable verification

- Checker: `checkers/quarter_point_first_localizer_determinants.py`
- Result: `results/quarter-point-first-localizer-determinants.json`
- Robustness checker: `checkers/quarter_point_localizer_interval_robustness.py`
- Robustness result: `results/quarter-point-localizer-interval-robustness.json`
