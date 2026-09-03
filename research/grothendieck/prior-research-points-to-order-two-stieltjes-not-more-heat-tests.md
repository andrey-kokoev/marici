# Prior research points to order-two Stieltjes, not more heat tests

## Search question

Which existing Marici branch supplies a nonredundant attack on the complete-monotonicity gate?

## Strongest surviving branch

The packet `xi-complete-bernstein-equivalence.md` identifies the centered squared-coordinate determinant logarithm

\[
B(x)=\log\frac{\xi(1/2+\sqrt x)}{\xi(1/2)}
\]

and its derivative

\[
B'(x)=
\frac{\xi'/\xi(1/2+\sqrt x)}{2\sqrt x}.
\]

The sharper outer-current packet derives an order-two Stieltjes target

\[
H'(x)=
\int_{1/4}^\infty
\frac{d\nu(a)}{(x-1/4+a)^2},
\qquad d\nu(a)\ge0.
\]

This is more rigid than raw heat complete monotonicity: it fixes the support edge, meromorphic pole order, and spectral multiplicity weight. Its inverse Laplace density has the forced form

\[
m(t)=t\int e^{-at}\,d\nu(a).
\]

The prior packet `the-angular-bernstein-measure-is-the-differentiated-xi-heat-trace.md` proves that this is not a separate measure: it is the shifted Xi heat trace followed by one directed heat derivative.

## Why this may unlock the meta-observer gate

The factorial moments

\[
q_k(x)=
\frac{(-1)^kH^{(k+1)}(x)}{(k+1)!}
\]

must satisfy three Hausdorff matrix families:

\[
(q_{i+j})\succeq0,
\qquad
(q_{i+j+1})\succeq0,
\qquad
\left(\frac{q_{i+j}}x-q_{i+j+1}\right)\succeq0.
\]

These are all restrictions of one divided-difference kernel because

\[
\sum_{k\ge0}q_k(x)t^k
=
\frac{H(x)-H(x-t)}t.
\]

Thus the infinite positivity family can be attacked as one source kernel or one continued-fraction/Jacobi operator, rather than derivative by derivative.

Existing source reconstructions already recover stable low rates and positive weights from theta jets, and their finite Jacobi feature map predicts out-of-sample values. This is stronger structural evidence than the Gaussian heat scans.

## Rejected prior shortcuts

The search also found exact no-go results:

- the free operator `1/4-partial_u^2` has continuous spectral type and cannot produce the required discrete rates;
- the scalar theta ground-state Schrödinger transform has the wrong eigenvalues;
- fixed-sum Wigner slices cannot all be positive by Hudson rigidity;
- a four-state positive canonical-system repair changes the theta source, while the unrepaired triangular system admits no suitable positive Green form;
- the finite Hurwitz transfer is a P-matrix but not totally positive or an M-matrix;
- tested one-statistic cancellation groupings fail, and Dodgson induction leaves lower-oriented and interval-avoiding cases.

These should not be retried as if open.

## Exact next attack

Seek a source factorization of the two-point kernel

\[
L(x,y)=\frac{H(x)-H(y)}{x-y}
\]

on the outer ray, with the order-two support localizer retained. Equivalently, derive a Stieltjes J-fraction whose coefficients are positive source expressions and whose convergents are the already observed Jacobi approximants.

The acceptance test is not numerical fit. The continued-fraction coefficients must be obtained from the completed theta/prime source and prove all three Hausdorff families simultaneously. A negative coefficient or failure of base-point transport kills this route.

## Disposition

Prior research does not contain a hidden RH proof. It does identify one nonredundant candidate unlock: replace raw heat-jet positivity by source factorization of the order-two Stieltjes divided-difference kernel, using its compact Hausdorff moment problem and Jacobi/J-fraction realization. This keeps the same RH-strength gate but gives it a structured induction target.