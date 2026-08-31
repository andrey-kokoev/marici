# The three-port Evans vector is in the conservative block domain before the arithmetic adjoint equation is solved

## Question

After placing the exact Evans history in \(H^1(\mathbb R)\), is a further
limiting-absorption theorem needed merely to put the corresponding three-port
vector in the conservative block-operator domain?

## Claim boundary

No, for the currently declared centered three-port block. Domain membership is
already available from the whole-line Evans theorem, bounded theta incidence,
and Hilbert--Schmidt arithmetic incidence. The unresolved condition is the
arithmetic adjoint equation, not existence of the operator-domain vector.
This does not construct the full Fourier--Poisson response trace or prove that
the vector is a conservative kernel state.

## Frozen three-port operator

Use

\[
\mathcal H_{\rm tot}=H\oplus\mathbb C_\theta\oplus U_{\rm ar},
\]

where

- \(H=L^2(\mathbb R)\) is the centered history carrier;
- the differential history block \(A\) has domain \(H^1(\mathbb R)\);
- \(V:\mathbb C_\theta\to H\) is bounded and \(V1=\Phi\);
- \(B_\Sigma:U_{\rm ar}\to H\) is Hilbert--Schmidt, hence bounded;
- \(D_U(z)\) is a closed arithmetic pencil with dense domain
  \(D(D_U)\subset U_{\rm ar}\);
- \(D_\theta=0\) and there is no primitive theta--arithmetic dynamic arrow.

The block domain is

\[
\mathcal D
 =H^1(\mathbb R)\oplus\mathbb C_\theta\oplus D(D_U).
\]

Bounded off-diagonal maps do not alter this domain. In particular,
\(B_\Sigma^\dagger:H\to U_{\rm ar}\) is defined on every history Hilbert
vector.

## Evans vector

At a zero \(z_0\) of \(\tau\), let \(u_{z_0}\) be the exact global Evans
history. The preceding source estimate proves

\[
 u_{z_0}\in H^1(\mathbb R).
\]

Since every linear subspace contains zero,

\[
 0\in D(D_U).
\]

Therefore

\[
 \Psi_{z_0}=(u_{z_0},1,0)\in\mathcal D.
\]

No boundary value of a resolvent and no limit from either parameter half-plane
is used.

## Block residual

Choose the already frozen signs so that the triangular Evans equation is the
history row. On the Xi divisor, the history and theta rows vanish by the exact
Evans construction and the declared theta compression. The remaining block
residual is

\[
 \mathcal G(z_0)\Psi_{z_0}
 =\bigl(0,0,B_\Sigma^\dagger u_{z_0}\bigr),
\]

up to the fixed row ordering.

This vector belongs to \(U_{\rm ar}\) automatically because
\(B_\Sigma^\dagger\) is bounded. Thus failure of

\[
 B_\Sigma^\dagger u_{z_0}=0
\]

is a nonzero equation residual in a valid target space. It is not a domain
failure and cannot be repaired by changing from exact range to closure of
range.

## Closed-operator consequence

Let \(\mathcal G(z)\) be the closed diagonal operator
\(A\oplus0\oplus D_U(z)\) plus the bounded theta and centered-incidence
couplings. Then \(\mathcal G(z)\) is closed on \(\mathcal D\). Consequently,
the exact Evans vector can be tested directly against the conservative pencil.
No limiting-absorption regularization is required for this test.

This does not imply that \(D_U(z)\) is invertible, passive, or the final
source-derived arithmetic law. Those are separate complement gates.

## Maximal-isotropic scope

The history component lies in the continuity extension
\(H^1(\mathbb R)\), which is maximal isotropic for the punctured-line
first-order seam form. Bounded theta and arithmetic incidence add no new
history derivative boundary term.

This proves maximal-isotropic membership for the centered history seam. It does
not prove that every primitive, square, connected, wall, reciprocal, and
archimedean response trace lies in the global Fourier--Poisson sewing relation.
That stronger response statement remains a separate source-intertwining
problem.

## Parameter-root chain

If \(z_0\) has Xi multiplicity \(m\), then for \(0\le j<m\),

\[
 \Psi_j=(\partial_z^ju(\cdot;z_0),0,0)\in\mathcal D
\]

apart from the undifferentiated augmented source coordinate at \(j=0\).
Applying the conservative pencil produces arithmetic root-chain residuals
built from

\[
 B_\Sigma^\dagger\partial_z^j u(\cdot;z_0),
 \qquad 0\le j<m,
\]

and derivatives of any parameter-dependent source-authorized coupling.
Therefore pointwise cancellation at \(j=0\) would not by itself prove local
module-length preservation. The full derivative family is the multiplicity
gate.

## SCC refinement

The corrected dependency graph should distinguish:

1. `evans_history_H1_domain`, constructed;
2. `three_port_block_domain_membership`, constructed;
3. `global_FP_response_relation_membership`, open;
4. `arithmetic_adjoint_residual_vanishing`, open;
5. `conservative_green_kernel_state`, dependent on 3 and 4;
6. `conservative_parameter_root_chain`, additionally dependent on every
   derivative residual through the local Xi multiplicity.

A single `seam_limiting_absorption_domain` node conflates these statements.

## Disposition

The candidate Evans vector is already a legitimate vector in the closed
three-port conservative block domain. The remaining RH-bearing obstruction is
an equation and response-intertwining problem, not a rigging-existence problem.
No RH conclusion is authorized.
