# Heat-kernel uniform semiboundedness by measure domination

## Question

What analytic estimate would control Voevodsky's generalized eigenvalues uniformly over every finite Gaussian parameter set?

## Claim boundary

A source-derived measure domination gives the required uniform bound without sampling. No admitted source currently supplies that domination for the completed heat kernel.

## Construction

Assume the order Gram kernel and completed-heat difference have Laplace representations on one measurable space:

\[
G(a+b)=\int_0^\infty e^{-(a+b)t}\,d\nu(t),
\]

\[
K(a,b)=H(a+b)-H(a+b+h)
       =\int_0^\infty e^{-(a+b)t}(1-e^{-ht})\,d\mu(t),
\]

where `nu` is positive and `mu` is a source-derived signed measure. Define

\[
d\eta_h(t)=(1-e^{-ht})\,d\mu(t).
\]

If there is one constant `C` such that the signed measure

\[
\eta_h+C\nu
\]

is positive, then for every finite set `F` and coefficient vector `c`,

\[
c^*(K_F+C G_F)c
 =\int_0^\infty\left|\sum_i c_i e^{-a_i t}\right|^2
   d(\eta_h+C\nu)(t)\ge 0.
\]

Therefore every generalized eigenvalue obeys

\[
\lambda_{\min}(K_F,G_F)\ge -C
\]

with the same `C`, independently of the size and geometry of `F`.

## Executable sufficient tests

1. If `mu` is positive, take `C=0`; the source form is positive.
2. If `eta_h` is absolutely continuous relative to `nu`, it suffices to prove the source-authorized essential bound

\[
\frac{d\eta_h}{d\nu}\ge -C.
\]

3. More generally, decompose `eta_h=eta_+-eta_-` and prove `eta_- <= C nu` as measures on every Borel set.

Finite generalized-eigenvalue scans cannot replace any of these global inequalities.

## Closability

Semiboundedness does not prove closability. After choosing `C`, the shifted form uses measure `eta_h+C nu`. Closability relative to the order space still requires the embedding defined on exponential sums to be closable, equivalently the null-sequence test in Voevodsky's packet. A singular positive component can satisfy semiboundedness while obstructing closability.

## Disposition

This supplies the analytic constructor Voevodsky requested. The first missing source object is a common Laplace/Stieltjes representation identifying both `nu` and `mu`, followed by either positivity of `mu` or a proved domination constant. Without that identity, an `H` evaluator can falsify candidate bounds on selected packets but cannot establish the uniform quantifier.
