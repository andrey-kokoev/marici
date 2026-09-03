# Exact rational SDP certificate backend

## Question

How can numerical tomography optimization be converted into independently checkable exact lower bounds and infeasibility certificates?

## Claim boundary

This packet specifies and implements a rational certificate verifier for real-symmetric four-dimensional density-matrix SDPs. It verifies certificates proposed by any external optimizer; it does not discover optimal multipliers or yet support general complex Hermitian input.

## Primal problem

Let \(W,A_i\) be rational symmetric matrices. Consider

\[
\inf_{\rho}\operatorname{Tr}(W\rho)
\]

subject to

\[
\rho\succeq0,
\qquad
\operatorname{Tr}\rho=1,
\qquad
l_i\le\operatorname{Tr}(A_i\rho)\le u_i.
\]

The slabs may come from efficiency-enclosed Born probabilities or Pauli-coordinate bounds.

## Exact dual lower certificate

Choose rational \(y\), \(\alpha_i\ge0\), and \(\beta_i\ge0\). Define

\[
Z=W-yI-\sum_i\alpha_iA_i+
\sum_i\beta_iA_i.
\]

If \(Z\succeq0\), then every feasible \(\rho\) obeys

\[
\operatorname{Tr}(W\rho)
\ge
b:=y+
\sum_i\alpha_il_i-
\sum_i\beta_iu_i.
\]

The verifier checks multiplier signs, constructs \(Z\) using exact fractions, and proves positive semidefiniteness by checking every principal minor. No solver tolerance enters the admitted bound.

A feasible rational primal matrix with objective value \(b\) proves the bound optimal. Otherwise the certificate remains a rigorous lower bound, not an optimum claim.

## Exact infeasibility certificate

Choose \(\alpha_i,\beta_i\ge0\) and set

\[
M=\sum_i\alpha_iA_i-
\sum_i\beta_iA_i.
\]

If

\[
-M\succeq0
\]

and

\[
\sum_i\alpha_il_i-
\sum_i\beta_iu_i>0,
\]

then no feasible density matrix exists: the slab constraints force \(\operatorname{Tr}(M\rho)>0\), while \(M\preceq0\) forces \(\operatorname{Tr}(M\rho)\le0\).

## Bell-fidelity certificate

Take

\[
W=\lvert\Phi^+\rangle\langle\Phi^+\rvert
=rac14(I+XX-YY+ZZ)
\]

with slabs

\[
\langle XX\rangle\ge4/5,
\quad
\langle YY\rangle\le-4/5,
\quad
\langle ZZ\rangle\ge4/5.
\]

Set \(y=1/4\), lower multipliers \(1/4\) for \(XX,ZZ\), and upper multiplier \(1/4\) for \(YY\). The slack matrix is exactly zero and the dual bound is

\[
17/20.
\]

The rational Bell-diagonal state with correlations \((4/5,-4/5,4/5)\) is feasible and attains \(17/20\), proving exact optimality.

## Hostile and infeasible fixtures

The inconsistent slabs

\[
\langle XX\rangle\ge1,
\qquad
\langle XX\rangle\le-1
\]

have an exact infeasibility certificate with equal multipliers: \(M=0\) while the scalar contradiction is two.

A mutated lower-bound certificate with enlarged \(y\) has a slack matrix with a negative principal minor and is rejected. Failure to enclose a numerical candidate rationally therefore cannot silently become a theorem.

## Scope extension

General complex path–polarization tomography requires Gaussian-rational Hermitian matrices or interval enclosures of algebraic entries. Certificate discovery may use a floating-point SDP solver, but admission requires rational reconstruction followed by this exact verifier. Solver success alone carries no evidential force.

## Disposition

Rational dual and infeasibility certificates provide a solver-independent verification boundary for tomography SDPs. The finite backend proves an exact \(17/20\) fidelity optimum, validates a contradictory-slab witness, and rejects a corrupted certificate. Complex Hermitian support remains a separate implementation branch.
