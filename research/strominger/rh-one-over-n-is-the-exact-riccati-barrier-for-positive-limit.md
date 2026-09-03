# One over n is the exact Riccati barrier for a positive limit

## Question

Which coefficient inequality would convert the finite \(nP_n(0)\) evidence into a positive-limit theorem?

For the positive alternating exterior solution, write

\[
u_{n+1}-(1+r_n-\varepsilon_n)u_n+r_nu_{n-1}=0,
\qquad
r_n=\frac{a_n}{a_{n+1}},
\]

and set \(\rho_n=u_n/u_{n-1}\). Then

\[
\rho_{n+1}=1+r_n-\varepsilon_n-rac{r_n}{\rho_n}.
\]

The sequence \(nu_n\) is nondecreasing exactly when

\[
\rho_n\ge\frac{n-1}{n}.
\]

Because the Riccati map is increasing in \(\rho_n\), this barrier propagates if

\[
\varepsilon_n\le
\varepsilon_n^*
:=rac1{n+1}-rac{r_n}{n-1}.
\]

Indeed, substituting the barrier value gives

\[
1+r_n-\varepsilon_n^*-rac{nr_n}{n-1}
=rac{n}{n+1}.
\]

Thus \(u_n=1/n\) is the exact comparison solution for the critical defect \(\varepsilon_n^*\), not merely its indicial approximation.

If the barrier holds from one finite index onward and an independent asymptotic estimate supplies \(u_n=O(n^{-1})\), then \(nu_n\) is positive, nondecreasing, and bounded. It therefore converges to a strictly positive limit.

## Disposition

Resolve the positive-limit problem to two explicit gates: an eventual defect inequality \(\varepsilon_n\le\varepsilon_n^*\) and the upper bound \(u_n=O(n^{-1})\).

The next leaf is `weibull-critical-defect-barrier`: prove the defect inequality from Jacobi coefficient asymptotics with signed remainder.

## Claim boundary

The known expansion \(\varepsilon_n=2n^{-2}-6n^{-3}+O(n^{-4})\) does not determine the sign of \(\varepsilon_n^*-\varepsilon_n\). Unsigned asymptotics are insufficient.
