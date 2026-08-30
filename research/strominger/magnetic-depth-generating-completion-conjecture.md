# Depth-generating completion conjecture for the Hall quotient

The raw Hall projection has growing support and is not controlled by the
unweighted coefficient norm. A first weighted audit reveals a more structured
possibility.

Assign depth weight

\[
w_\rho(a)=\rho^a,\qquad \rho>1.
\]

For an omitted plus column at depth \(a\), with preferred-basis relation

\[
e_{a,+}=\sum_{(d,\sigma)\in B}c_{a;d,\sigma}e_{d,\sigma},
\]

measure the weighted column ratio

\[
\Gamma_\rho(a)=
\sum_{(d,\sigma)\in B}
|c_{a;d,\sigma}|\rho^{d-a}.
\]

Exact rational relations through depth \(42\) give the following numerical
evaluations.

| \((g,q)\) | \(a\) | \(\Gamma_{1.1}\) | \(\Gamma_{1.25}\) | \(\Gamma_{1.5}\) | \(\Gamma_2\) |
|---|---:|---:|---:|---:|---:|
| \((6,3)\) | 18 | 52.9 | 12.2 | 2.00 | 0.239 |
| \((6,3)\) | 30 | 165 | 8.35 | 0.517 | 0.0907 |
| \((6,3)\) | 42 | 257 | 3.26 | 0.298 | 0.0646 |
| \((6,8)\) | 18 | 6160 | 922 | 69.3 | 1.65 |
| \((6,8)\) | 30 | 501 | 17.4 | 0.326 | 0.00959 |
| \((6,8)\) | 42 | 782 | 6.11 | 0.0959 | 0.00453 |

Thus growing relation support does not by itself obstruct a weighted
completion. Moderate exponential depth weights eventually suppress the long
backward tail. Small exponential weights can exhibit a large finite transient,
so boundedness cannot be inferred from asymptotics alone.

The weight has a natural source candidate. Introduce a depth-generating
variable \(y\). The norm \(\sum_a |v_a|\rho^a\) is the coefficient norm on a
disk strictly larger than the unit depth disk, and the exact source law

\[
F_{a+1}(t,x)=\frac{1-xt}{1+t}F_a(t,x)
\]

becomes multiplication by a fixed rational transfer before grade truncation.
The completion question is therefore whether the descended plus-to-Hall
relation operator is analytic and bounded on some source-authorized annulus in
\(y\).

This leads to the conjecture:

> For every fixed admissible \((g,q)\), there is a source-determined critical
> radius \(\rho_c(g,q)\ge1\) such that the Hall quotient projection is bounded
> on the depth-weighted coefficient space for every
> \(\rho>\rho_c(g,q)\), and fails for every \(1\le\rho<\rho_c(g,q)\).

The conjecture is deliberately stronger than the bounded audit. Its principal
falsifiers are:

1. superexponential relation coefficients, which no fixed \(\rho\) controls;
2. a near-diagonal coefficient growing without bound, which exponential
   weighting cannot suppress;
3. a source singularity whose location depends on the cutoff;
4. bounded columns but unbounded row sums, defeating full operator
   boundedness.

The next exact step is to derive the bivariate generating kernel of the
relation matrix and identify \(\rho_c\) from its singular variety. Until that
is done, \(\rho\) is a tested candidate parameter, not source authority.

## Support-gap refinement

A second exact audit through depth \(70\) inspected the coefficients nearest
the moving depth. For \(g=6,q=3\), the coefficients of minus depths
\(a,a-1,\ldots,a-4\) vanish in every sampled deep relation; the first nonzero
minus coefficient occurs at \(a-5\), where \(5=q+2=Q\). For \(q=8\) and
\(q=13\), the first six offsets all vanish, consistent with the predicted
gaps \(Q=10\) and \(Q=15\).

This is not generic triangular fill. It is the combinatorial shadow of the
explicit factor \(x^Q\) in the right Euler boundary operator. The deep-plus
projection begins only after a fixed source-derived displacement \(Q\).
Consequently an exponential depth norm gains the fixed contraction
\(\rho^{-Q}\) before encountering the moving minus tail.

The sharpened proof target is a delayed convolution theorem: after removing
the finite plus cap, the quotient projection should be a lower-triangular
kernel supported on offsets at least \(Q\). If its coefficients have at most
polynomial growth in depth and offset, every \(\rho>1\) yields a bounded
weighted operator. The remaining issue is whether the source selects a
particular admissible radius rather than merely permitting one.

## Two-sided Schur audit and the radius-one boundary

Column estimates alone do not prove operator boundedness. The conjugated
relation matrix was therefore tested by both maximum weighted column sum and
maximum weighted row sum through cutoff \(80\).

For \((g,q)=(6,3)\), the pairs stabilize as follows:

| \(\rho\) | max column sum | max row sum |
|---:|---:|---:|
| \(1.25\) | \(33.7\) | approximately \(94.5\) |
| \(1.5\) | \(11.2\) | approximately \(10.2\) |
| \(2\) | \(3.24\) | approximately \(1.70\) |

The larger-\(q\) cases have severe but cutoff-stable finite transients. At
\((6,8,\rho=2)\), the pair stabilizes at approximately \((158,215)\); at
\((6,13,\rho=2)\), at approximately \((192,114)\).

A boundary audit through cutoff \(120\) at \((g,q)=(6,3)\) sharply separates
\(\rho=1\). The unweighted column maximum grows from \(267.7\) at cutoff \(20\)
to \(1.384\times10^6\) at cutoff \(120\), while the row maximum grows from
\(535.8\) to \(1.196\times10^7\). At \(\rho=1.1\), the column maximum has
stabilized near \(276.4\), although the row sum is still approaching its much
larger finite limit. At \(\rho=1.05\), convergence is slower still.

The bounded evidence therefore supports the sharper universal prediction

\[
\rho_c(g,q)=1.
\]

This is not yet a theorem: it requires a uniform polynomial bound on the
delayed convolution coefficients and a two-sided summability proof. But the
unit depth circle is now the unique observed failure boundary, rather than a
fitted case-dependent radius.
