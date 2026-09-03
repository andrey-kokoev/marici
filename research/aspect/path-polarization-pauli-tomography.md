# Path–polarization Pauli tomography with explicit loss

## Question

Which realizable interferometric and polarimetric settings are jointly monic on arbitrary path–polarization density matrices, and which settings are necessary within that analyzer architecture?

## Claim boundary

This packet treats a four-dimensional one-photon sector with two path modes and two polarization modes. It proves informational completeness and setting minimality within local Pauli analyzers. It does not cover variable photon number, unresolved frequency, detector dark counts, nonlinear response, or arbitrary generalized measurements.

## State object

Let

\[
H=\mathbb C^2_{\rm path}\otimes\mathbb C^2_{\rm pol}.
\]

The physical state object for this model is the convex set of trace-one positive operators \(\rho\) on \(H\). Its affine real dimension is fifteen.

Let \(X,Y,Z\) denote Pauli operators. The sixteen tensor products

\[
\sigma_a\otimes\sigma_b,
\qquad a,b\in\{I,X,Y,Z\},
\]

form an orthogonal basis of operators. Trace fixes the \(I\otimes I\) coefficient, so the other fifteen expectation values determine \(\rho\) uniquely.

## Realizable analyzer settings

Path analyzers implement:

- \(Z\): direct which-path detection;
- \(X\): balanced path interference with zero relative phase;
- \(Y\): balanced path interference with a quarter-turn phase shift.

Polarization analyzers implement:

- \(Z\): horizontal/vertical analysis;
- \(X\): diagonal/antidiagonal analysis;
- \(Y\): right/left circular analysis.

A joint setting \((a,b)\in\{X,Y,Z\}^2\) has four outcomes labelled \((s,t)\in\{+1,-1\}^2\). Its outcome statistics determine

\[
\langle\sigma_a\otimes I\rangle,
\qquad
\langle I\otimes\sigma_b\rangle,
\qquad
\langle\sigma_a\otimes\sigma_b\rangle.
\]

The nine joint settings recover all six local coordinates and all nine correlation coordinates, hence all fifteen nonidentity Pauli coefficients.

## Joint monicity

Define the tomography map

\[
T(\rho)=
\bigl(
\operatorname{Tr}(\rho\,\sigma_a\otimes\sigma_b)
\bigr)_{(a,b)\ne(I,I)}.
\]

Since the Pauli tensor products form a basis, \(T\) is injective on trace-one Hermitian operators and therefore monic on the density-state object.

The reconstruction formula is

\[
\rho=\frac14
\sum_{a,b\in\{I,X,Y,Z\}}
\langle\sigma_a\otimes\sigma_b\rangle
\,\sigma_a\otimes\sigma_b,
\]

with the identity expectation equal to one.

## Minimality within the nine-setting architecture

Remove one joint setting \((a,b)\). Every remaining setting is orthogonal to the correlation direction \(\sigma_a\otimes\sigma_b\). The two states

\[
\rho_\pm=rac14
\left(I\otimes I
\pm\frac12\sigma_a\otimes\sigma_b\right)
\]

are positive: their eigenvalues are \(3/8\) and \(1/8\). They agree on all remaining settings and differ on the omitted correlation. Thus every one of the nine joint settings is necessary within this fixed local-Pauli architecture.

This does not prove that nine is minimal among arbitrary POVMs or detectors with larger record alphabets.

## Explicit loss channel

Let propagation and detection have a setting-independent scalar efficiency \(\eta\in[0,1]\). Pulling back the four ideal outcome effects gives detected total

\[
\eta I_H.
\]

The declared no-click effect is

\[
E_\varnothing=(1-\eta)I_H.
\]

The five effects then sum to \(I_H\). Conditional renormalization of the four clicks recovers ideal setting probabilities only under the explicit assumption that loss is state- and outcome-independent. If efficiency depends on path, polarization, setting, or outcome, no-click statistics must remain in the tomography model.

## Compatibility with attachment transport

Each analyzer setting is an instrument attachment to the same typed path–polarization port. Propagation pulls its effects back by operator conjugation. Geometric branch ambiguity remains correspondence-valued; tomography compares the resulting state effects only after a particular lawful lift is specified or all lifts are retained.

## Exact diagnostic

A symbolic Pauli-label checker verifies that the nine settings cover precisely fifteen nonidentity coordinates, that every deleted setting leaves one unique correlation absent, and that the corresponding \(\rho_\pm\) pair is positive and indistinguishable on the retained coordinates. With \(\eta=3/4\), four click effects total \(3I/4\) and the no-click effect \(I/4\) restores normalization.

## Disposition

Nine local Pauli analyzer settings are jointly monic on the four-dimensional path–polarization density-state object and deletion-minimal within that architecture. Explicit no-click effects preserve normalization under uniform loss. The next unresolved gate is robustness and calibration under state-, mode-, and outcome-dependent loss.
