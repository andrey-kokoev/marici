# The quarter pivot-curvature grid selects two over n

## Question

Do local LU-pivot curvatures support

\[
c_m=1+rac2m+O(m^{-2})?
\]

Reconstructing \(R_m\) from exact four-staircase determinants and taking \(c_m=R_m/R_{m-1}\) gives \(c_m>1\). For \(m=10,\ldots,17\),

\[
m(c_m-1)
=1.8090,
1.8278,
1.8433,
1.8562,
1.8672,
1.8767,
1.8849,
1.8921.
\]

The sequence moves monotonically toward two. The next scaled residual is

\[
m^2\left(c_m-1-rac2m\right)
=-1.9103,\ldots,-1.8349,
\]

suggesting a finite second-coefficient candidate near \(-7/4\).

## Disposition

Complete the finite local-curvature discrimination in favor of coefficient two. The next leaf is `quarter-pivot-curvature-second-coefficient`: determine whether

\[
c_m=1+rac2m-rac{7}{4m^2}+O(m^{-3})
\]

and derive the expansion from the pivot recurrence.

## Claim boundary

The reconstructed grid is exact at each degree but does not prove convergence. It is algebraically downstream of the same staircase determinants used for the global cross-limit fit and is not independent evidence for the amplitude \(104/1575\).
