# Endpoint-free completed-heat cone

## Question

Can the known endpoint atom be removed before attacking the RH-strength positivity inequality?

## Claim boundary

Yes algebraically. This produces a cleaner cone for the completed heat kernel \(H\). Its equivalence to RH uses the already established decay, moment-representation, generic-mesh, and pole-comparison arguments. It does not prove the cone.

## Exact subtraction

The remainder kernel is

\[
H_R(u)=H(u)-e^{u/4}.
\]

For fixed positive \(t,h\), set

\[
Y=e^{h/4},
\qquad
c_E=e^{t/4}(Y-1).
\]

Then

\[
\begin{aligned}
a_n
&=H_R(t+nh)-H_R(t+(n+1)h)\\
&=H(t+nh)-H(t+(n+1)h)+c_EY^n.
\end{aligned}
\]

Define the endpoint-free moments

\[
b_n
=H(t+nh)-H(t+(n+1)h).
\]

Thus

\[
a_n=b_n+c_EY^n.
\]

At matrix level,

\[
A_N=B_N+c_Ev_Yv_Y^*,
\qquad
v_Y=(1,Y,\ldots,Y^{N-1})^T.
\]

The second term is known, positive, and rank one.

## Why this is the sharper frontier

Positivity of \(A_N\) permits the endpoint atom to mask a negative direction of \(B_N\) at finite rank. The asymptotic endpoint-extraction theorem removes that masking only after using all ranks and the source-derived asymptotic.

Working directly with \(B_N\) avoids this detour. Under RH,

\[
b_n
=
\sum_{[\rho]}
m_\rho e^{-t\gamma_\rho^2}
(1-e^{-h\gamma_\rho^2})
e^{-nh\gamma_\rho^2},
\]

so

\[
c^*B_Nc
=
\sum_{[\rho]}
m_\rho e^{-t\gamma_\rho^2}
(1-e^{-h\gamma_\rho^2})
\left|p(e^{-h\gamma_\rho^2})\right|^2
\geq0.
\]

Conversely, if every \(B_N(t,h)\) is positive, Hamburger representation gives a positive measure for \((b_n)\). Since \(H(t+nh)\to0\), telescoping gives

\[
H(t+nh)=\sum_{k=n}^\infty b_k.
\]

The decay of \(b_n\), together with positivity of all shifted matrices obtained by replacing \(t\) by \(t+mh\), confines the representing support to \([0,1)\). The generic-mesh pole comparison then forces every sampled zero base to be real and hence every nontrivial zero onto the critical line.

## First inequalities

The endpoint-free rank-one target is

\[
H(t)-H(t+h)\geq0.
\]

The rank-two target is

\[
[H(t)-H(t+h)]
[H(t+2h)-H(t+3h)]
\geq
[H(t+h)-H(t+2h)]^2.
\]

These are sharper than the corresponding \(H_R\) inequalities because no known positive endpoint term can conceal a residual failure.

## Disposition

The direct frontier should be stated using the completed heat kernel \(H\), not the endpoint-contaminated remainder kernel \(H_R\). The unproved assertion is positivity of every endpoint-free matrix

\[
B_N(t,h)
=
\bigl(H(t+(i+j)h)-H(t+(i+j+1)h)\bigr)_{i,j<N}.
\]

This is still RH-strength; the reduction removes bookkeeping, not difficulty.

## Verification

- `research/voevodsky/checkers/check_endpoint_free_completed_heat_cone.py`
- `research/voevodsky/results/endpoint_free_completed_heat_cone.json`
