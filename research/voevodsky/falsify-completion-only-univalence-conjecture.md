# Falsification of the completion-only univalence conjecture

## Problem

The proposed bold conjecture said that displayed univalence can hold only after an explicit higher or Rezk completion, never from gauge fixing alone.

## Bold conjecture under test

Every gauge quotient presentation requires a higher completion or additional kernel framing before equality can classify vertical isomorphisms.

## Named rivals

1. A rigid canonical-presentation subcategory may already be set-level univalent.
2. Gauge fixing may suffice when the kernel has no nonidentity automorphisms.
3. The completion requirement may be specific to the real gauge sector rather than categorical in general.

## Strongest falsification attempt

Work over \(\mathbb F_2\). Fix a one-dimensional kernel \(G=\mathbb F_2\), a quotient \(X=\mathbb F_2^2\), and admit only the canonical split presentation

\[
E=G\oplus X,
\qquad q(g,x)=x,
\qquad s(x)=(0,x).
\]

A vertical automorphism preserving \(q\) has form

\[
h(g,x)=(Ag+Lx,x).
\]

Preserving the gauge section forces \(L=0\). Since

\[
\operatorname{Aut}_{\mathbb F_2}(G)=\mathbb F_2^{\times}=\{1\},
\]

we also have \(A=1\). Therefore the only vertical automorphism is the identity.

The displayed fiber of canonical split presentations over the fixed pair \((G,X)\) is a singleton, and its structured automorphism type is also a singleton. The equality-to-isomorphism map is consequently a bijection without Rezk completion, higher quotient, or separately added kernel framing.

## Risky consequence and exact test

An exhaustive finite-field census must find:

- four quotient-preserving automorphisms before section preservation;
- one section-preserving automorphism;
- no nonidentity section-preserving kernel scaling.

The checker finds exactly those counts.

## Residual

The falsifier uses two restrictions absent from the completed radiative gauge sector:

- characteristic two makes the one-dimensional kernel automorphism group trivial;
- only the canonical split presentation is admitted.

Thus it refutes the universal “only after completion” claim but does not establish displayed univalence for Strominger’s real distributional quotient.

## Disposition

The bold conjecture is rejected as stated. The surviving claim is narrower:

For the unrigidified real gauge quotient, the exact sequence alone does not prove displayed univalence; its vertical group contains gauge shears and kernel automorphisms. A higher completion is one repair, not the only possible repair. A source-authorized rigid subcategory can also suffice when its equality-to-isomorphism map is proved bijective.

## Verification

- `research/voevodsky/checkers/check_completion_only_univalence_falsifier.py`
- `research/voevodsky/results/completion_only_univalence_falsifier.json`
- `research/voevodsky/gauge-rigidification-stabilizer-audit.md`
