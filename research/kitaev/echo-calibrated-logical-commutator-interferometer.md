# Echo-calibrated logical commutator interferometer

## Question

Can the loop-order interferometer cancel ordinary implementation phases while retaining the primal-dual intersection sign?

Let \(Z\) and \(X\) be reversible logical loops and define their group commutator

\[
C(Z,X)=ZXZ^{-1}X^{-1}.
\]

For toric logical loops,

\[
C(Z,X)=(-1)^{I(Z,X)}I,
\]

where \(I(Z,X)\in\mathbf F_2\) is intersection parity.

## Claim boundary

Prepare one control qubit in \(|+\rangle\) and an arbitrary target state \(\rho\). Apply

\[
U_C=
|0\rangle\!\langle0|\otimes I+
|1\rangle\!\langle1|\otimes C(Z,X).
\]

The reduced control coherence is

\[
\langle X_{\mathrm c}\rangle+i\langle Y_{\mathrm c}\rangle
=
\operatorname{Tr}(\rho\,C(Z,X)).
\]

In the ideal toric algebra this gives

\[
\langle X_{\mathrm c}\rangle=(-1)^{I(Z,X)},
\qquad
\langle Y_{\mathrm c}\rangle=0
\]

for every \(\rho\). Odd and even intersection are therefore separated without preparing a particular logical target state.

Suppose implementations carry consistent operation phases,

\[
\widetilde Z=e^{i\alpha}Z,
\qquad
\widetilde X=e^{i\beta}X,
\]

with inverses implemented as the actual inverses. Then

\[
\widetilde Z\widetilde X\widetilde Z^{-1}\widetilde X^{-1}
=
ZXZ^{-1}X^{-1}.
\]

The phases cancel exactly. This removes the ordinary phase-convention ambiguity of comparing controlled \(ZX\) and \(XZ\) as separately compiled branches.

The echo does not cancel:

1. an inverse implementation that is not the inverse of the forward operation;
2. order-dependent coherent errors;
3. a phase attached to the controlled branch as a whole;
4. leakage from the logical subspace;
5. nonunitary noise.

These defects are visible algebraically when the effective commutator is not a scalar phase. Dependence of \(\operatorname{Tr}(\rho C)\) on \(\rho\), a nonzero \(Y\)-record, or magnitude below one rejects the ideal central-commutator model.

An even-intersection pair supplies a differential control only if it is implemented through the same calibrated constructor family. Comparing unrelated physical paths does not cancel their independent phases.

The protocol remains conditional on controlled execution of a logical group commutator. The Wilson algebra proves the conditional record but does not construct the control interface.

## Disposition

The commutator echo is stronger than the two-word interferometer against phase-gauge criticism. Its stable record is the central extension class evaluated on a loop pair.

The first falsifier is one of:

1. \(C(Z,X)\) is not central on the admitted logical subspace;
2. exact inverse pairing is unavailable;
3. the control record depends on the target state;
4. odd/even intersection does not flip the calibrated \(X\)-record;
5. the comparison uses physically unrelated constructor paths;
6. a scalar model reproduces the test only by adding the same commutator cocycle.

The remaining physical question is whether controlled inverse loop transport can be executed fault-tolerantly with a common control phase. That question belongs to the interface and fault model, not to homology alone.
