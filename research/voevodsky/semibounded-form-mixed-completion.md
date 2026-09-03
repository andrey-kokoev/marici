# Semibounded-form completion of mixed bridges

## Question

Which analytic hypotheses extend finite Schur bridge certificates to unbounded closed forms?

## Claim boundary

This packet gives a sufficient theorem and an exact unbounded diagonal realization. It does not establish that the radial source data satisfy the hypotheses.

## Sufficient theorem

Let \(a\) and \(d\) be densely defined nonnegative closed forms on Hilbert spaces \(K\) and \(X\). Assume:

1. \(a(k)\ge\alpha\lVert k\rVert^2\) for some \(\alpha>0\);
2. a cross form \(b(k,x)\) is continuous from the \(a\)-form space against the \(d\)-form space;
3. its reduced form
   \[
   r(x)=\sup_{k\ne0}\frac{|b(k,x)|^2}{a(k)}
   \]
   satisfies \(r(x)\le\theta d(x)\) with \(0\le\theta<1\);
4. all pasted bridges use the same declared form domains and preserve them.

Then

\[
s(x)=d(x)-r(x)
\]

is nonnegative and closed on \(D(d)\). Indeed, \(r\) is \(d\)-form bounded with relative bound below one, so the KLMN form theorem applies; moreover \(s(x)\ge(1-\theta)d(x)\).

For nested kernel blocks satisfying the same hypotheses, staged and joint reduction agree by the variational identity

\[
\inf_{k_2}\inf_{k_1}G(k_1,k_2,x)
=
\inf_{(k_1,k_2)}G(k_1,k_2,x).
\]

This is the closed-form counterpart of associative Schur elimination. It is defined only when the common-domain and coercivity certificates make each infimum a represented closed form.

## Exact unbounded realization

Take \(K=X=\ell^2(\mathbb N)\) with common form domain

\[
Q=\left\{x:\sum_{n\ge0}(n+1)|x_n|^2<\infty\right\}.
\]

Set

\[
a(k)=\sum_{n\ge0}(n+1)|k_n|^2,
\quad
d(x)=\sum_{n\ge0}(n+1)|x_n|^2,
\]

and

\[
b(k,x)=\frac12\sum_{n\ge0}(n+1)\overline{k_n}x_n.
\]

Then \(r=d/4\), so \(s=3d/4\). The associated operators are unbounded, while the forms are closed on \(Q\); finitely supported sequences are a common core. Finite coordinate restrictions preserve every coefficient and converge monotonically on \(Q\).

## Strongest falsification attempt

At cross coefficient one, \(r=d\) and \(s=0\). Coercivity disappears and the radical becomes all of \(X\). For coefficients above one, the Schur form is negative. Thus the strict relative bound is necessary for the stated positive, radical-free conclusion.

## Source comparison gate

The radial \(R_\zeta\) sector still lacks the source-derived intertwiner, common invariant core, cross-form estimate, relative bound below one, and closure identification. The theorem names acceptance data; it does not supply them.

## Disposition

The candidate heterogeneous equipment now has a genuine unbounded closed-form realization under explicit sufficient hypotheses. What remains is source adequacy, not abstract analytic existence: test whether the radial construction supplies the five named certificates.

## Verification

- `research/voevodsky/checkers/check_semibounded_form_mixed_completion.py`
- `research/voevodsky/results/semibounded_form_mixed_completion.json`
