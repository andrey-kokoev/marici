# Suppressed value form has a degree-independent coercivity budget

## Question

Does the value component of the atomic quadrature error admit a bound independent of polynomial degree?

## Uniform estimate

For the tail beginning at label three, put \(x_0=\log3\). The value component is

\[
R_{\rm val}(p)
=(2+2a\beta)
\int_{x_0}^{\infty}
 e^{-x-2ax^\beta}|p(x)|^2dx.
\]

Since \(x\geq x_0\),

\[
e^{-x}\leq e^{-x_0}=\frac13.
\]

Therefore

\[
R_{\rm val}(p)
\leq
\eta_{\rm val}Q_{\rm cont}(p),
\qquad
\eta_{\rm val}=\frac{2+2a\beta}{3}.
\]

This estimate is independent of polynomial degree and retains quadratic-form order.

## Parameter gate

The value form alone leaves a positive lower-bound budget exactly when

\[
\eta_{\rm val}<1
\quad\Longleftrightarrow\quad
a\beta<\frac12.
\]

For the tested candidate \(a=1\), \(\beta=1/4\),

\[
\eta_{\rm val}=\frac56.
\]

Thus at most \(1/6\) remains for the endpoint and derivative components under this crude decomposition. Their bounds must sum to less than \(1/6\) to certify the atomic lower Gram form.

## Relation to the finite grid

The exact generalized eigenvalue of the value component was approximately \(0.07836\) at degree six, far below \(5/6\). The analytic estimate is intentionally coarse: it supplies degree independence, not a sharp asymptotic constant.

## Disposition

The suppressed value component is uniformly controlled. It cannot by itself obstruct Loewner coercivity when \(a\beta<1/2\). The unresolved theorem is now the combined endpoint-plus-derivative estimate within the remaining budget.

## Claim boundary

The parameters \(a,\beta\) remain candidate completion data rather than source-selected constants. This estimate does not prove the total quadrature error is relatively bounded below one.
