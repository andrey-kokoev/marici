# Corrected barrier parameters are fourth-order degenerate

## Question

Can the fitted values \(\kappa=0.31\) and \(c=-1\) be recovered uniquely from the asymptotic defect?

Let

\[
r_n=1-rac4n+rac{10}{n^2}+rac{r_3}{n^3}+O(n^{-4})
\]

and use

\[
v_n^{(\kappa,c)}
=\frac1{n+\kappa}\left(1+\frac{c}{n^2}ight).
\]

Exact truncated-series algebra gives the induced critical defect

\[
\varepsilon_n^{*,v}
=rac2{n^2}-rac6{n^3}
+rac{-8-r_3+2\kappa-2\kappa^2-2c}{n^4}
+O(n^{-5}).
\]

Thus \(\kappa\), \(c\), and the unsourced Jacobi ratio coefficient \(r_3\) all enter first at fourth order. The finite slack determines only their combination. It cannot identify the two profile parameters separately.

## Disposition

Reject unique source derivation of the fitted decimal profile from current asymptotics. The next leaf is `weibull-fourth-order-barrier-combination`: derive \(r_3\) and the fourth defect coefficient \(e_4\), then characterize the open region

\[
-8-r_3+2\kappa-2\kappa^2-2c>e_4
\]

of eventual barrier candidates. Initialization data must select within that region.

## Claim boundary

The calculation identifies the necessary coefficient combination but supplies no signed remainder beyond fourth order. The refused SymPy preflight was not bypassed; the verified checker uses dependency-free exact truncated-series arithmetic.
