# Finite-scheme normalization-port theorem

## Question

What is the smallest operational readout capable of selecting one point in
Ledger 3037's rank-three finite-scheme orbit?

## Evaluation map

After removal of common source factors, the finite response has the form

\[
R(x)=r_0+r_1x+r_2x^2,
\qquad x=p^2\eta^2.
\]

Evaluating it at declared physical ports \(x_0,x_1,x_2\) gives

\[
E_{\boldsymbol x}=
\begin{pmatrix}
1&x_0&x_0^2\\
1&x_1&x_1^2\\
1&x_2&x_2^2
\end{pmatrix}.
\]

Its determinant is the Vandermonde factor

\[
\det E_{\boldsymbol x}
=(x_1-x_0)(x_2-x_0)(x_2-x_1).
\]

Therefore three distinct scalar ports are jointly faithful. One or two scalar
ports cannot be faithful on a three-dimensional linear orbit; two distinct
ports leave a one-dimensional kernel.

## Result

Exactly three independent scalar normalization measurements are minimally
sufficient to select a finite scheme point in the toy response. Their values
define the section; the Carrier, Ward identities, and Hadamard condition do
not.

The primary source does not select three port locations or provide three
measured values. It also states that the finite initial time is arbitrary when
nothing physical occurs there. Hence the theorem constructs a family of
faithful operational interfaces, not a canonical one.

Any alternative collection of observables is equally admissible only after
its combined Jacobian on the scheme orbit is proved rank three. Counting three
reported numbers is not enough.

## Deutschian interpretation

The missing input is now finite and testable. A proposed physical preparation
must predict three independent normalization records and use the same scheme
point for every subsequent observable. Fitting the three values separately to
the two-point function has no explanatory content; predicting them from an
independent preparation mechanism does.

## Scope

The minimality theorem is linear and applies to the rank-three toy response.
It does not claim that point evaluations are experimentally optimal or that
the full inflationary theory has only three renormalized parameters.

## Verification

- `research/benincasa/checkers/finite_scheme_normalization_ports.rs`
- `research/benincasa/results/finite-scheme-normalization-ports.json`
- exact integer verification of the Vandermonde determinant and the two-port
  residual kernel
