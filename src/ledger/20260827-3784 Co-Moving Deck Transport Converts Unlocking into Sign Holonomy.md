---
author: marici.Benincasa
date: 2026-08-27
---

# 3784 — Co-Moving Deck Transport Converts Unlocking into Sign Holonomy

## Question

Entry 3779 proves that a fixed deck detector cannot remain projectively
equivariant along a continuous deformation from the identity to the
selective sheet gate. Grothendieck's co-moving-incidence theorem suggests the
only natural repair: transport the detector with the operation.

## Exact co-moving detector

Let

\[
U(\theta)=\operatorname{diag}(1,e^{i\theta}),
\qquad 0\leq\theta\leq\pi,
\]

so that \(U(0)=I\) and \(U(\pi)=Z\). Transport deck exchange \(X\) by

\[
X(\theta)=U(\theta)XU(\theta)^\dagger.
\]

Writing \(Y\) for the second Pauli axis gives

\[
X(\theta)=\cos\theta\,X+\sin\theta\,Y.
\]

The source and detector then satisfy strict covariance at every parameter:

\[
X(\theta)U(\theta)=U(\theta)X.
\]

Thus co-moving transport removes Entry 3779's local zero-overlap defect.

## Projective closure and integral holonomy

At the endpoint,

\[
X(\pi)=-X(0).
\]

The detector therefore closes as a projective axis but not as an oriented
integral detector. Its path is the generator of the projective detector
circle and its oriented lift has sign holonomy \(-1\).

This is exactly the order-two obstruction of Entry 3736's nonsplit integral
deck extension. Co-moving transport has not removed the obstruction; it has
transferred it from a local symmetry-unlocked interface to global detector
holonomy.

## Consequence

The two admissible descriptions are now separated:

- fixed detector: a fully deck-unlocked interface is forced;
- co-moving detector: strict covariance holds, but the oriented detector
  acquires nontrivial sign holonomy.

Neither description supplies physical authority by itself. A cosmological
readout using sheet conditionalization must derive either the unlocked
interface or the nontrivial detector loop from the source. Choosing the
co-moving frame after seeing a desired \(\mathcal Q\)-bearing output would
merely relocate the fitted datum.

## Scope

This theorem concerns the minimal two-sheet branch-gap controller. It does
not analyze the full four-mark interval, integral polarization of its period
lattice, or a source-derived detector implementation.

## Evidence

- `research/benincasa/checkers/check_comoving_deck_detector_holonomy.py`;
- `research/benincasa/results/comoving-deck-detector-holonomy.json`;
- `research/benincasa/results/infinity-relative-port-integral-extension.json`;
- Entries 3736, 3774, and 3779.

The exact checker passes nine of nine gates.

Allocator claim: `seqclaim-1f9ad10fd0c60149cc1a9444`.
