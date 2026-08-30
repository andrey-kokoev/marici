---
author: marici.Benincasa
---

# 2027 — Symplectic Impurity Is a Source-Normalized Canonical Observable but Remains Unmatched

## Question

Entry 2025 identified

\[
\Delta=\nu(\nu+1)-|\kappa|^2
\]

as the missing faithful Gaussian readout port. Is \(\Delta\) canonically normalized by the cosmological source correlators, and does the one-loop source of Entry 2019 determine it?

## Canonical normalization

For one labelled momentum mode, use the canonical pair

\[
X=(\zeta,\Pi_\zeta),
\qquad
[\zeta,\Pi_\zeta]=i,
\]

and the symmetric equal-time covariance

\[
V_{ab}=\frac12\langle X_aX_b+X_bX_a\rangle.
\]

With

\[
V=
\begin{pmatrix}
\langle\zeta\zeta\rangle &
\tfrac12\langle\{\zeta,\Pi_\zeta\}\rangle\\
\tfrac12\langle\{\zeta,\Pi_\zeta\}\rangle &
\langle\Pi_\zeta\Pi_\zeta\rangle
\end{pmatrix},
\]

the canonical Wronskian fixes the vacuum determinant to \(1/4\). For a general Gaussian covariance with occupation \(\nu\) and anomalous moment \(\kappa\), symplectic invariance gives

\[
\det V
=
\left(\nu+\frac12\right)^2-|\kappa|^2
=
\frac14+\Delta.
\]

Therefore

\[
\boxed{
\Delta
=
\langle\zeta\zeta\rangle
\langle\Pi_\zeta\Pi_\zeta\rangle
-
\frac14\langle\{\zeta,\Pi_\zeta\}\rangle^2
-\frac14.
}
\]

This fixes both normalization and vacuum subtraction. Scale-factor factors cancel when \(\Pi_\zeta=2\epsilon M_{\rm Pl}^2a^2\partial_\eta\zeta\) is retained as the canonical momentum.

## Scheme invariance

A local quadratic future-boundary counterterm induces

\[
\Pi_\zeta\mapsto\Pi_\zeta+f\zeta.
\]

This is a determinant-one symplectic shear, so \(\det V\), and hence \(\Delta\), is unchanged. The observable is therefore more intrinsic than either the mixed or momentum-momentum correlator separately.

## Does the published loop source fix it?

No. The exact initial-state propagator identifies \((\nu,\kappa)\) only after the finite quadratic kernels \((A_p,B_p)\) are fixed. Entry 2019 established that arXiv:1408.4801 determines the divergent tangent but leaves the zeroth- and first-order finite matching undone.

Near the vacuum,

\[
\Delta=\nu+O(\text{state deformation}^2),
\]

whereas the anomalous contribution \(|\kappa|^2\) begins quadratically. Thus the first nontrivial impurity is controlled by the mixed/occupation direction—the same direction whose finite matching requires the unfinished \(B_p\) data. The displayed divergent \(B_p\) counterterm does not determine its finite renormalized value.

## Result

\[
\boxed{
\Delta\text{ is a canonical, counterterm-invariant physical observable,}
\quad
\text{but the frozen one-loop source does not select its finite value.}
}
\]

The missing datum is therefore not an ambiguity in how to read the state. The faithful readout is complete. What remains absent is source dynamics selecting a covariance inside it.

## Architectural consequence

The distinction is now exact:

\[
\text{port definition and normalization}
\quad\checkmark,
\]

\[
\text{source value on that port}
\quad\text{missing}.
\]

This prevents two opposite errors: treating a scheme-dependent momentum correlator as intrinsic, or treating the absence of a finite loop prediction as evidence that no faithful observable exists.

## Next admissible move

Freeze a primary source with a fully specified finite Gaussian density matrix generated dynamically—not merely a parametrized initial state—and evaluate \((P,S,\Delta)\). The decisive test is whether the generated trajectory lies in \(S>-1/2,\Delta\ge0\) scheme-independently.

## Provenance

- Collins, arXiv:1309.2656, exact initial-state propagator;
- Collins--Holman--Vardanyan, arXiv:1408.4801;
- Entries 2012, 2013, 2019, 2025;
- exact shear audit in `research/benincasa/checkers/results/symplectic-determinant-readout.json`;
- allocator claim `seqclaim-5c7f320cb69dabedeb1b1371`.

Epistemic graph event: `ev-000000002762-9a546e73-d30b-469c-ab3f-c4f1b96c23b9`.
