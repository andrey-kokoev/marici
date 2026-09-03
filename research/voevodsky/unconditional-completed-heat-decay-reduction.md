# Unconditional completed-heat decay reduction

## Question

Does extraction of the endpoint atom require RH, or can the needed moment asymptotic be obtained unconditionally from the general complex-zero heat expansion?

## Claim boundary

The spectral estimate and the exact decay-to-moment-asymptotic identity are derived. Authoritative citations and the exact completed complex-zero expansion still need attachment. Remainder Hankel positivity remains open.

## Complex-zero heat rate

For a nontrivial zero

\[
\rho=\beta+i\gamma,
\]

define

\[
\lambda_\rho
=-\left(\rho-\frac12\right)^2.
\]

Then

\[
\operatorname{Re}\lambda_\rho
=
\gamma^2-
\left(\beta-\frac12\right)^2.
\]

The critical-strip bound \(0<\beta<1\) gives

\[
\operatorname{Re}\lambda_\rho
\geq
\gamma^2-\frac14.
\]

Thus a zero need not lie on the critical line for its heat contribution to decay. It is enough that

\[
|\gamma|>\frac12.
\]

## Normal convergence argument

Assume the classical inputs:

- every nontrivial zero ordinate satisfies \(|\gamma|>1/2\);
- the zero-counting function obeys \(N(T)=O(T\log T)\);
- the exact completed heat expansion sums \(e^{-t\lambda_\rho}\) with the stated multiplicities and no untracked growing term.

For \(t\geq t_0>0\),

\[
\left|e^{-t\lambda_\rho}\right|
\leq
 e^{-t(\gamma^2-1/4)}
\leq
 e^{-t_0(\gamma^2-1/4)}.
\]

The counting bound makes the majorant summable. Every term tends to zero as \(t\) tends to infinity, so dominated convergence gives

\[
H(t)\longrightarrow0.
\]

This argument does not use \(\beta=1/2\).

## Exact endpoint asymptotic

Let

\[
Y=e^{h/4},
\qquad
H_E(s)=e^{s/4},
\qquad
H_R(s)=H(s)-H_E(s).
\]

Define the remainder localizer moments

\[
a_n
=H_R(t+nh)-H_R(t+(n+1)h).
\]

Direct substitution gives

\[
\frac{a_n}{Y^n}
=
e^{t/4}(Y-1)
+
Y^{-n}
\left[
H(t+nh)-H(t+(n+1)h)
\right].
\]

Therefore, if \(H(s)\to0\),

\[
\frac{a_n}{Y^n}
\longrightarrow
c(t,h),
\qquad
c(t,h)=e^{t/4}(Y-1).
\]

This is exactly the endpoint coefficient in the raw localizer.

## Combined reduction

If every remainder Hankel matrix

\[
(a_{i+j})_{0\leq i,j<N}
\]

is positive, the endpoint-atom extraction theorem supplies a positive representing measure containing mass exactly \(c(t,h)\) at \(Y\), with no mass at \(-Y\). Subtracting that atom leaves the full localizer positive.

Hence, after the classical decay inputs are sourced, the RH-strength matrix programme has only one nontrivial positivity gate:

\[
(a_{i+j})\geq0
\quad\text{for every rank, }t>0,h>0.
\]

The endpoint range and Schur conditions are consequences, not separate estimates.

## Remaining source checks

The following cannot be inferred from the finite symbolic fixture:

1. the exact general-complex-zero expansion, including multiplicities and conjugate pairing;
2. absence or cancellation of additional growing completed terms;
3. authoritative zero-free and counting estimates;
4. interchange of the completed sum and the limiting operation.

Once these are attached, the decay branch is unconditional and closes. The remainder Hankel cone then carries all RH-strength content.

## Verification

- `research/voevodsky/unconditional-completed-heat-decay-reduction-v1.json`
- `research/voevodsky/checkers/check_unconditional_completed_heat_decay_reduction.py`
- `research/voevodsky/results/unconditional_completed_heat_decay_reduction.json`
