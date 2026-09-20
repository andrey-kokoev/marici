# Evans-to-joint-response source map and fixed-marginal hostile

## Question

Does an independent source operation construct the finite-cutoff Evans-to-joint-response map without fitting the Haar scalar or assuming a common Schatten operator?

## Source operation and type

Fix the nonzero theta forcing vector `Phi`. On the admitted Evans history carrier define

\[
F_{\rm Ev}(u)=J_\Phi(u)
=\bigl(C_\Phi u,\Phi\otimes u\bigr),
\]

where

\[
(C_\Phi u)(s)=\int\Phi(x)u(x+s)\,dx.
\]

The target is the based joint graph

\[
\Gamma_\Phi\subset
H_{\rm sep}\oplus
(H_{\rm add}\widehat\otimes\overline{H_{\rm mult}}).
\]

This operation is constructed from correlation and tensor insertion. It is not reconstructed from an energy equality, Xi divisor, determinant, or scalar readout. The base `Phi` is retained because both response coordinates depend on it.

## Composition and transport

For source translation `S_a`, use the transported joint action

\[
R_a=
S_a^{\rm sep}\oplus(I\otimes S_a).
\]

Then

\[
F_{\rm Ev}(S_a u)=R_aF_{\rm Ev}(u).
\]

The composition law is the based translation law

\[
R_bR_a=R_{a+b}.
\]

No physical-time interpretation is assigned to the translation parameter.

## Noncollapse at the source stage

The tensor coordinate is injective because `Phi` is nonzero:

\[
\Phi\otimes u=0\Longrightarrow u=0.
\]

Thus `F_Ev` retains source-state dependence even if the correlation coordinate has a kernel. This is a source-stage noncollapse result, not a completed positivity theorem.

## Finite falsifier

The checker uses a two-dimensional rational fixture. It retains the correlation and tensor responses, verifies exact transport intertwining, and tests a hostile that reverses only the tensor leg.

The hostile preserves both marginal ranks. It changes the joint coupling and violates the based graph relation. Therefore marginal observer sufficiency does not authorize the joint map; the shared source state does.

## Claim boundary

This constructs the missing finite-cutoff forward realization `F_Ev` into the density/Haar joint graph. It does not construct:

- the endpoint–Euler–archimedean determinant-line clutching cell;
- determinant monodromy;
- cutoff variance or completion;
- the relative-Haar energy-cycle identity.

The first remaining analytical-form obligation is packet sewing: define the source-derived attachment from this joint graph to the already typed endpoint, Euler, and archimedean lines while preserving both response coordinates.

## Disposition

The finite forward-realization candidate survives the fixed-marginal cross-coupling hostile. Its surviving scope is the based joint response graph before determinant attachment and completion.

Verification:

- `research/nima/checkers/check_evans_joint_response_finite_source_map.py`
- `research/nima/results/evans-joint-response-finite-source-map.json`
