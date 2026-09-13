# Constructive odd residual fold

## Purpose

`agda/BoundaryPfaffianResidualFold.agda` formalizes recursion in configuration size. An odd metric word is generated from a singleton by adding two gaps at a time.

## Recursive type

```text
singleton : OddMetric
extendRight : OddMetric -> evenGap -> oddGap -> OddMetric
```

A second type, `LocalizedOddMetric`, has the same recursion but requires a `GapUnit` witness for every selected even-indexed gap. Its erasure forgets those witnesses and returns the underlying metric word. Agda proves that its recursively accumulated selected torsion equals the outgoing alternating product after erasure.

`LocalizedEvenMetric` additionally requires a unit witness for the final selected closing gap. It therefore carries exactly the hypotheses needed to contract every prescribed hyperbolic pair, with no inverses required for unselected gaps. Its localized torsion is proved equal to the ordinary even alternating torsion.

The module formalizes both versions of paired refinement:

- over a bare commutative ring, the selected-gap cross relation
  \[
  \rho\tau_{\rm new}=\alpha\beta\tau_{\rm old};
  \]
- given `GapUnit rho`, the localized forward transition
  \[
  \tau_{\rm new}=\alpha\beta\rho^{-1}\tau_{\rm old}.
  \]

The unselected-gap transition remains polynomial. Thus correspondence-before-localization and transport-after-localization are separated in the formal types.

Its residual summary contains two charges. They satisfy

\[
q_{\rm out}(\operatorname{extend}(X,e,o))=q_{\rm out}(X)e,
\]

\[
q_{\rm in}(\operatorname{extend}(X,e,o))=q_{\rm in}(X)o.
\]

Thus repeated extension computes the alternating products of even- and odd-indexed gaps.

## Constructed laws

The module proves:

- exact agreement between recursive metric extension and residual-summary action;
- associativity of adjoining two gap pairs;
- left residual extension changes later sewing only through the outgoing multiplier;
- right residual extension changes sewing only through the incoming multiplier;
- reversal of the complete metric word exchanges incoming and outgoing charges.

For summaries \(X,Y\), sewing is

\[
\operatorname{sew}(X,g,Y)=q_{\rm out}(X)gq_{\rm in}(Y).
\]

Therefore the two-charge summary is a sufficient statistic under arbitrary further pair extension in the finite ordered-chain protocol.

## Arbitrary odd--odd closure

The module also defines recursively presented even metric words and their adjacent torsion. Joining two arbitrary odd words \(X,Y\) across a gap \(g\) gives an even word. Structural induction proves

\[
\tau_{\rm even}(X\star_gY)
=q_{\rm out}(X)gq_{\rm in}(Y).
\]

This generalizes the separate three-plus-three calculation to arbitrary finite odd sizes. The module further proves

\[
\tau_{\rm even}(Y^{\rm op}\star_gX^{\rm op})
=
\tau_{\rm even}(X\star_gY),
\]

by composing metric reversal, summary reversal, contravariant sewing, and odd--odd torsion reconstruction. Thus arbitrary-size even closure is formally reversal invariant at the fold level.

These results prove the arbitrary-size alternating-product sewing theorem; identifying this recursively defined adjacent torsion with the full matrix Pfaffian at every size remains the outstanding general Pfaffian formalization step.

## Constructive reversal

Because the metric word is stored by right extension, reversal is implemented by reversing pair order and swapping the two gaps in each pair. Agda proves

\[
q_{\rm out}(X^{\rm op})=q_{\rm in}(X),
\qquad
q_{\rm in}(X^{\rm op})=q_{\rm out}(X).
\]

The module first proves the structural lemma that reversing a prepended gap pair is the same as appending the swapped pair. Induction then proves the full metric-word identity

\[
(X^{\rm op})^{\rm op}=X.
\]

This is an equality of recursively presented odd configurations, not merely equality of their observed charges.

At summary level, reversal is the literal swap

\[
(q_{\rm out},q_{\rm in})^{\rm op}
=(q_{\rm in},q_{\rm out}).
\]

The module proves that this swap is involutive, that summarization commutes with metric-word reversal, and that summary involution is induced by the constructed metric-word involution. It also proves the contravariant sewing law

\[
\operatorname{sew}(Y^{\rm op},g,X^{\rm op})
=
\operatorname{sew}(X,g,Y).
\]

Thus the pair \((q_{\rm out},q_{\rm in})\) is the canonical reversal-closed, polarized torsion certificate. Selecting only one component is an orientation choice.

## Verification

Checked with Agda 2.8.0.1 and Cubical 0.9:

```text
agda --transliterate \
  -i research/voevodsky/agda \
  -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 \
  research/voevodsky/agda/BoundaryPfaffianResidualFold.agda
```
