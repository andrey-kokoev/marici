# Constructive odd residual fold

## Purpose

`agda/BoundaryPfaffianResidualFold.agda` formalizes recursion in configuration size. An odd metric word is generated from a singleton by adding two gaps at a time.

## Recursive type

```text
singleton : OddMetric
extendRight : OddMetric -> evenGap -> oddGap -> OddMetric
```

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

## Constructive reversal

Because the metric word is stored by right extension, reversal is implemented by reversing pair order and swapping the two gaps in each pair. Agda proves

\[
q_{\rm out}(X^{\rm op})=q_{\rm in}(X),
\qquad
q_{\rm in}(X^{\rm op})=q_{\rm out}(X).
\]

At summary level, reversal is the literal swap

\[
(q_{\rm out},q_{\rm in})^{\rm op}
=(q_{\rm in},q_{\rm out}).
\]

The module proves that this swap is involutive and that summarization commutes with metric-word reversal. It also proves the contravariant sewing law

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
