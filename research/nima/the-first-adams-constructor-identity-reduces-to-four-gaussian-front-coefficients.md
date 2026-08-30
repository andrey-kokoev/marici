# The first Adams constructor identity reduces to four Gaussian-front coefficients

## Differentiate before comparing

The Stieltjes disagreement is

\[
d_p=W_{2L}-W_L,
\qquad
L=\log p.
\]

Its derivative is the explicit wall-killed packet

\[
b_p
=
U_{-2L}f_0-U_{2L}f_0-U_{-L}f_0+U_Lf_0.
\]

The ordered port satisfies

\[
DS_{\mathrm{ord}}=-2I
\]

on the zero-mass rapid core, and

\[
d_p=-\frac12S_{\mathrm{ord}}b_p.
\]

Let \(d_p^{\mathrm{src}}\) be the completed-history output of the source
constructor, and define its differentiated boundary packet

\[
b_p^{\mathrm{src}}=Dd_p^{\mathrm{src}}.
\]

If the source chain uses the same wall quotient and ordered inverse, then

\[
d_p^{\mathrm{src}}=d_p
\]

is equivalent to

\[
b_p^{\mathrm{src}}=b_p.
\]

The differentiation removes every integration-constant ambiguity.

## Linear independence of the four fronts

Suppose

\[
\sum_{a\in\{-2L,-L,L,2L\}}
c_aU_af_0=0.
\]

Fourier transformation gives

\[
\widehat f_0(\xi)
\sum_a c_ae^{ia\xi}=0.
\]

The Gaussian transform never vanishes, so the exponential polynomial is zero
for every \(\xi\). Distinct exponentials are linearly independent; hence

\[
c_a=0
\]

for every \(a\).

Therefore equality with \(b_p\) is equivalent to the four coefficient
identities

\[
(c_{-2L},c_{-L},c_L,c_{2L})
=
(1,-1,1,-1).
\]

The order shown corresponds to the frozen translation convention.

## Source-side extraction

The exact finite Duhamel defect is

\[
\mathcal R_p
=
U_L
\left[
-2L(A+1)D+L^2D^2
\right].
\]

Its reciprocal pair contains:

- an odd first-order curvature channel;
- an even second-order correction;
- four Gaussian polynomial grades on the seed;
- the common moving-cut boundary.

After two-ray sewing, half-density transport, theta summation, completion
differentiation, and Wronskian/tail resolution, the resulting boundary must
be projected onto the four-front basis.

The first Adams theorem is exactly the statement that this projection has the
coefficient vector above and no residual component orthogonal to the
four-front span.

## Two separate tests

A coefficient match alone is insufficient unless the source output is already
known to lie in the four-front span. Thus the finite audit has two parts:

1. span closure:
   \[
   b_p^{\mathrm{src}}
   \in
   \operatorname{span}
   \{
   U_{-2L}f_0,U_{-L}f_0,U_Lf_0,U_{2L}f_0
   \};
   \]
2. coefficient identity:
   \[
   (1,-1,1,-1).
   \]

A hidden theta-tail remainder can pass all four coefficient probes while
remaining nonzero outside the span.

## Four Fourier samples are not enough

Although the target span has dimension four, evaluating the Fourier transform
at four frequencies proves the coefficients only after span closure.
Without that theorem, finitely many samples leave an infinite-dimensional
kernel.

A robust proof may instead establish the exact symbolic Fourier identity

\[
\widehat b_p^{\mathrm{src}}(\xi)
=
2i[
\sin(L\xi)-\sin(2L\xi)
]
\widehat f_0(\xi).
\]

This identity simultaneously proves span closure and coefficients.

## Prime uniformity

The coefficient pattern is independent of \(p\); only \(L=\log p\)
changes. Therefore a naturality theorem for translation length can prove all
primes at once.

If the completed chain is a translation-covariant cocycle, it is enough to
establish the symbolic identity for arbitrary \(L>0\), rather than checking
primes individually.

## Consequence of success

Once the four-front identity is proved:

- \(J_{\mathrm{src}}=J_{\mathrm{top}}\);
- Pauli linking functoriality follows from the common lift;
- reciprocal rank-one incidence follows from character selection;
- the primewise Schur-loading margin is already analytically positive;
- the odd return is trace class;
- the first enlarged Adams edge is source-authorized.

Thus no further local coercivity estimate remains.

## Minimal hostiles

1. Omit the even \(L^2D^2\) correction and obtain wrong outer-front
   coefficients.
2. Match all four coefficients but retain a nonzero theta-tail remainder.
3. Compare primitives without fixing the constant wall.
4. Reverse the translation convention and swap the reciprocal signs.
5. Verify only \(p=2\) without proving length naturality.

## Verdict

The earliest unresolved Adams constructor is now a finite symbolic boundary
identity. After differentiation, the target is the linearly independent
four-front packet

\[
U_{-2L}f_0-U_{2L}f_0-U_{-L}f_0+U_Lf_0.
\]

The next source calculation should compute the Fourier multiplier of the
completed bivariate constructor and compare it with
\(2i[\sin(L\xi)-\sin(2L\xi)]\widehat f_0(\xi)\).
