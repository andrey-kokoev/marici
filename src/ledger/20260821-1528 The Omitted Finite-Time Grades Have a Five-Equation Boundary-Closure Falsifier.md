# 1528 — The Omitted Finite-Time Grades Have a Five-Equation Boundary-Closure Falsifier

## Hard-to-vary claim

At first order in the quadratic initial action of arXiv:1408.4801, the real
kernels \(\operatorname{Re}A_p\), \(\operatorname{Im}A_p\), and \(B_p\)
span only a rank-three subspace of the rank-eight late-time trigonometric
coefficient space.  Therefore each omitted \(\eta_0\)-grade must satisfy five
exact linear identities if the published quadratic coefficient object is
sufficient.

## Frozen basis

Let \(\theta=2p(\eta-\eta_0)\), and order coefficients by

\[
(\cos\theta,\eta\cos\theta,\eta^2\cos\theta,
\sin\theta,\eta\sin\theta,\eta^2\sin\theta,1,\eta^2).
\]

Equation (21) gives the three response directions

\[
r_{\operatorname{Re}A}=(0,-2p,0,1,0,-p^2,0,0),
\]

\[
r_{\operatorname{Im}A}=(1,0,-p^2,0,2p,0,0,0),
\]

\[
r_B=(0,0,0,0,0,0,1,p^2).
\]

They have generic rank three.

## Exact annihilators

Writing a candidate loop grade as coefficients \(c_\bullet\), membership in
the response span requires

\[
c_{\eta\cos}+2p c_{\sin}=0,
\qquad
p^2c_{\sin}+c_{\eta^2\sin}=0,
\]

\[
p^2c_{\cos}+c_{\eta^2\cos}=0,
\qquad
-2pc_{\cos}+c_{\eta\sin}=0,
\]

\[
-p^2c_{1}+c_{\eta^2}=0.
\]

The Symbolica checker verifies exactly that all five functionals annihilate
all three source response directions.  As an end-to-end control, it also
projects the printed Eq. (19) vector and obtains

\[
(\operatorname{Re}A,\operatorname{Im}A,B)=(0,L,-J_0),
\]

where

\[
L=J_1-2J_0-4J_2-
\frac{32c_3}{(3\epsilon+2\delta)^2}.
\]

All five obstruction functionals vanish on this control.

## Deutsch--Popperian decision rule

- If both omitted grades satisfy all five identities, the published bilocal
  quadratic kernel remains sufficient at this loop order.
- If one identity fails, the failure is not removable by choosing
  \(A_p\) or \(B_p\).  A further source-derived boundary coefficient operator
  is required.
- No new carrier stratum follows from such a failure: it is initially a
  coefficient-closure obstruction.

## Artifacts

- `research/benincasa/marici-gm/src/bin/finite_time_quadratic_response_span.rs`
- `research/benincasa/results/finite-time-quadratic-response-span.json`

## Verification

```text
cargo run --release --bin finite_time_quadratic_response_span
exit code: 0
response rank: 3
annihilator rank: 5
```

## Next falsifier

Contract Eq. (18), project its \(\eta_0^1\) coefficient onto these five
annihilators before evaluating the loop momentum integrals, and stop at the
first nonzero obstruction.  Only if that grade closes should the
\(\eta_0^0\) grade and subsequent Hadamard audit be computed.
