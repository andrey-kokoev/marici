# The unique reciprocal-balanced prime-delay monomial at the required diagonal shell order is grade four

## Question

If the missing diagonal reciprocal coefficient is compiled from direct and
reciprocal prime-delay atoms, which graded monomial can first have the required
parameter-independent order \(p^{-2}\)?

## Claim boundary

Among monomials in the two reciprocal delay characters, the unique balanced
choice is \(S_+^2S_-^2\). This selects a grade-four comparison target. It does
not prove that the source constructor produces the required coefficient or
sign.

## Reciprocal delay atoms

Let

\[
 S_{p,+}(z)=p^{-1/2}e^{i(\log p)z},
 \qquad
 S_{p,-}(z)=p^{-1/2}e^{-i(\log p)z}.
\]

A monomial with nonnegative integer exponents \((r,s)\) is

\[
 S_{p,+}(z)^rS_{p,-}(z)^s
 =p^{-(r+s)/2}e^{i(r-s)(\log p)z}.
\]

## Parameter independence

The leading required endpoint-relative correction

\[
 -\frac{1}{4\pi p^2}
\]

has no delay character in \(z\). Therefore a single reciprocal monomial must
satisfy

\[
 r-s=0.
\]

Hence \(r=s\).

## Required prime order

Order \(p^{-2}\) requires

\[
 \frac{r+s}{2}=2,
\]

or

\[
 r+s=4.
\]

Together with \(r=s\), this has the unique solution

\[
 r=s=2.
\]

Thus

\[
 S_{p,+}^2S_{p,-}^2=p^{-2}.
\]

## Exclusion of lower grades

- Grade one carries a nontrivial delay character and order \(p^{-1/2}\).
- Grade two is parameter independent only for \(S_{p,+}S_{p,-}=p^{-1}\),
  which is too large.
- Grade three cannot be reciprocal balanced because \(r+s\) is odd.
- Grade four first supplies the required parameter-independent order.

Therefore primitive, square, and connected grade-three data cannot directly be
the final diagonal multiplier unless their lower-order contributions cancel
and a grade-four residue is retained.

## Source support and limitation

The repository's exact finite-translation audit already found a required
fourth Gaussian grade that a three-grade truncation omits. This shows that
retaining grade four is source-compatible. It does not identify that Gaussian
grade with the reciprocal-balanced prime-delay monomial; a comparison map is
still required.

Likewise, the order-three regularized determinant organizes primitive, square,
and connected tails but does not by itself construct a grade-four boundary
response coefficient.

## Exact candidate

A diagonal constitutive response consistent with the late-shell order must
begin schematically as

\[
 M_{p,\rm diag}(z)
 =1+c_4S_{p,+}^2S_{p,-}^2+O(p^{-3}),
\]

with

\[
 c_4=-\frac1{4\pi}
\]

under the current unit shell normalization, if no other source factor changes
the comparison.

The coefficient must be derived from the completion differential, endpoint
metric, or polarized Green current. It cannot be selected from the asymptotic
target alone. The completed-theta target has no order-\(p^{-3}\) term, so any
balanced grade-six contribution must also be shown to vanish or cancel.

## Hostile

A proposed reciprocal compiler fails the diagonal late-shell test if its first
surviving normalized term is:

- unbalanced in \(S_+,S_-\);
- of total grade below four;
- parameter-dependent at order \(p^{-2}\);
- or assigned the target coefficient without a source map.

## Disposition

The diagonal reciprocal frontier is narrowed to a reciprocal-balanced
grade-four source comparison. This is the first delay monomial with the correct
prime order and parameter behavior. Construction of its coefficient and its
map into the G4 response port remains open. No RH conclusion is authorized.
