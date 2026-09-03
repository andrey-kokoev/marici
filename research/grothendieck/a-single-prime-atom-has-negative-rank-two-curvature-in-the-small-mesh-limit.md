# A single prime atom has negative rank-two curvature in the small-mesh limit

## Question

Can the favorable odd Laguerre signs be promoted to positive semidefiniteness of the prime sector in the Bernstein basis?

## Claim boundary

No. For one prime log-Gaussian atom, the first and third directed differences can both have the favorable completed-prime sign while the rank-two determinant is negative for sufficiently small mesh. Gamma–prime coupling is therefore essential even inside the near-null sign window.

## One atom

Let

\[
\phi_c(t)=t^{-1/2}e^{-c/t},
\qquad x=c/t,
\]

and let the completed prime atom be `K(t)=-A*phi_c(t)` with `A>0`. The transformed rank-two block is

\[
\begin{pmatrix}
\Delta_hK(t)&\Delta_h^2K(t)\\
\Delta_h^2K(t)&\Delta_h^3K(t)
\end{pmatrix}.
\]

As `h` tends to zero,

\[
\Delta_hK=hA\phi_c'+O(h^2),
\quad
\Delta_h^2K=-h^2A\phi_c''+O(h^3),
\quad
\Delta_h^3K=h^3A\phi_c'''+O(h^4).
\]

Hence its determinant is

\[
A^2h^4
\left(\phi_c'\phi_c'''-(\phi_c'')^2\right)
+O(h^5).
\]

## Exact curvature sign

For `x>1/2`, `phi_c'(t)>0`. Put `g(t)=phi_c'(t)`. Direct differentiation gives

\[
(\log g)''
=\frac1{t^2}
\left[
-2x+\frac32+rac{x}{x-1/2}
-\frac{x}{2(x-1/2)^2}
\right].
\]

For `x>=2`, the bracket is strictly negative: `x/(x-1/2)<=4/3`, while the last term is nonpositive, so the bracket is at most `-4+3/2+4/3<0`. Therefore

\[
\phi_c'\phi_c'''-(\phi_c'')^2
=g(t)^2(\log g)''<0.
\]

It follows that, for every fixed `t` with `c/t>=2`, the prime atom's transformed rank-two determinant is negative for all sufficiently small positive `h`.

## Compatibility with favorable diagonal signs

When `c/(t+3h)` lies beyond the largest zero of `L_3^(-1/2)`, the completed prime first and third differences are nonnegative. The determinant calculation shows that their geometric mean is nevertheless smaller than the magnitude of the second-difference coupling. Thus diagonal Laguerre positivity and sectorwise matrix positivity are incompatible here.

## Beta-filter interpretation

The exact beta coherencer for the radial weight localizes each difference order at a different mean and width. This does not repair the determinant: in the confluent limit the three filters merge into the local derivatives above, whose logarithmic curvature is already negative.

## Disposition

Reject prime-sector positive semidefiniteness as a route, including within the small-heat favorable-sign window. The next rank-two target must retain the gamma and prime entries before taking the determinant; bounding or signing the sectors separately loses the required cross-sector compensation.