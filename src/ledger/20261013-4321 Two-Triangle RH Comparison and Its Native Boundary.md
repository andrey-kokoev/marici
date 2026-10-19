---
author: marici.Voevodsky
description: The added arithmetic and divisor triangles compare the same signed Weil form beside both native carriers; covariance and quotient analysis preserve the RH question without establishing native processing equivalence or positivity.
---

# 4321 — Two-Triangle RH Comparison and Its Native Boundary

## What each triangle computes

The bare triangles act on coefficient amplitudes. Arithmetic enters through an explicit added analytic decoration on a fixed test/antidual register, not through the native arrows alone.

Let \(\mathcal T\) consist of smooth functions with finite seminorms

\[
p_{k,m}(f)=\max_{j\le m}\sup_x e^{k|x|}|f^{(j)}(x)|
\]

for all integers \(k\ge1,m\ge0\). Write \(Ff(u)=\int f(x)e^{-iux}\,dx\). A Hermitian source form \(b\), conjugate-linear in its first argument, defines the continuous weak operator \((W_b g)(f)=b(f,g)\) into the continuous antidual. Its edge operation is the reversible shear

\[
U_b(f,\ell)=(f,\ell+W_bf).
\]

Starting from \((f,0)\), the arithmetic triangle follows \(AB,BC,CA\), with edge labels endpoint \(E\), gamma \(\Gamma\), and signed prime-power term \(P\). It produces \((f,W_Af)\), where \(A=E+\Gamma+P\). The scalar readout is

\[
\begin{aligned}
b_A(f,f)={}&\operatorname{Re}\left(\overline{A_-(f)}A_+(f)\right)\\
&+\frac1{4\pi}\int_{\mathbb R}
\left(\operatorname{Re}\psi(1/4+iu/2)-\log\pi\right)|Ff(u)|^2\,du\\
&-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle f,T_{\log n}f\rangle,
\end{aligned}
\]

where \(A_\pm(f)=\int f(x)e^{\pm x/2}\,dx\) and \(T_rf(x)=f(x+r)\).

The spectral triangle follows \(BA,AD,DB\), with labels \(-E,Z,E\). It subtracts and restores the endpoint register around the full divisor evaluation, producing \((f,W_Zf)\), with

\[
b_Z(f,f)=\frac12\sum_\rho m(\rho)
\overline{Ff(\overline{u_\rho})}Ff(u_\rho),
\qquad u_\rho=\frac{\rho-1/2}{i}.
\]

The sum retains complex nodes and holomorphic multiplicities. It is not replaced by an absolute square at a complex node.

## What the common edge identifies

The shared edge identifies one test frame and the chosen endpoint operator, with inverse operations on \(AB\) and \(BA\). The shared analytic interface fixes Fourier conventions and the half-divisor normalization. This endpoint assignment is noncanonical: compensating changes to other edge labels preserve both face outputs.

The classical explicit formula, not the shared edge, supplies \(b_A=b_Z\). Following both faces forward computes their sum. Comparing them requires the inverse second face; the composable path \(AB,BC,CA,AB,BD,DA\) computes \(U_{A-Z}\), the identity at the exact source level. Independently computed finite midpoints retain a bounded nonzero discrepancy rather than being silently equated.

## What survives in both structures

The protonlike and neutron carriers admit the same added analytic register through metric-correct normalized native tags. Exact restrictions of dimensions three and fifteen were checked, together with negative and complex-Hermitian controls. The neutron metric is retained.

This does not identify the complete native processors. The inherited forms have only fourteen positive directions, excluding a fixed linear encoding of the certified positive fifteen-test family without enlargement. In the selected one-plane enlargement, the three-stage \(G-N\) ranks remain six and thirty-three. Moreover the native clock satisfies \(W^5=W^2\), whereas a nonzero source shear \(U=I+N\), \(N^2=0\), satisfies \(U^5-U^2=3N\ne0\). These obstruct the corresponding full-stage equivalence and injective clock intertwining; they do not exclude every alternative enlargement.

## Covariance, quotient, and the RH condition

Every source form is invariant under simultaneous real translation of its two tests. On the antidual, \(D_r\ell(f)=\ell(T_{-r}f)\) gives \(W_bT_r=D_rW_b\). Signed covariance is unconditional: synthetic off-axis controls preserve the signed pairing while failing positive unitarity.

On the distinct divisor nodes, introduce the auxiliary space

\[
K=\ell^2(\{u_\rho\},m/2),\qquad
(\mathcal Ef)(u)=Ff(u),\qquad (Cv)(u)=v(\overline u).
\]

Then \(b_Z(f,g)=\langle C\mathcal Ef,\mathcal Eg\rangle_K\), where \(C\) is a linear self-adjoint permutation involution. Gaussian-polynomial localization gives density of \(\mathcal E(\mathcal T)\) in \(K\), and hence \(\operatorname{Rad}b_Z=\ker\mathcal E\). The isotropic cone cannot replace the radical without positivity.

If a nonreal node exists, its conjugate pair supplies a negative signed direction, approximable by test evaluations. If all nodes are real, \(C=I\). Thus positivity on every test is equivalent to RH; this establishes the comparison's logical content, not positivity itself. Under RH the positive radical quotient completes to \(K\), with the self-adjoint multiplication generator and compact resolvent described in the companion note.

Multiplicity remains a scalar weight in this model. A node of multiplicity \(m\) does not acquire an \(m\)-dimensional eigenspace: repeated scalar evaluations occupy only the diagonal of \(m\) copies. A multiplicity-resolved determinant requires additional justification.

## Scope

The same signed analytic RH comparison survives beside both native structures. No all-test positivity, RH proof, native arithmetic execution, full native processing equivalence, or zeta determinant identity is asserted. Infinite-dimensional statements are analytic arguments, not machine-formalized theorems; the exact finite controls do not certify them by extrapolation.

## Durable verification

- Analytic construction: `research/voevodsky/rh-analytic-dual-carrier-v1.md`.
- Covariance and quotient argument: `research/voevodsky/rh-covariance-quotient-v1.md`.
- Checkers: `research/voevodsky/checkers/check_rh_analytic_dual_carrier.py` and `research/voevodsky/checkers/check_rh_covariance_quotient.py`.
- Results: `research/voevodsky/results/rh-analytic-dual-carrier-v1.json`, `research/voevodsky/results/rh-covariance-quotient-v1.json`, and `research/voevodsky/results/rh-native-test-capacity-v1.json`.
- The covariance checker was freshly rerun successfully for this entry, including verification of the preceding receipt's source hashes. The earlier analytic-carrier checker passed its recorded SCC challenge.
- Number allocation: sequence `marici-ledger-entry`, claim `seqclaim-74a47a171f321bad9047cd26`, permanently allocated value 4321.
- Epistemic graph admission: proposal `ep_acdf09de-d87a-4545-9044-4fc873cb8c8a`, admitted event/head `ba49959314f135a406db09d6a8a558a738debd7daa48563f41b631e9d152164b`. Admission records provenance and scope, not mathematical truth.
- Site validation: `pnpm run build` passed. This entry and its graph admission remain uncommitted; no commit or push was authorized.
