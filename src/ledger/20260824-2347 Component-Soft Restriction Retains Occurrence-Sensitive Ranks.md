# 2347 — Component-Soft Restriction Retains Occurrence-Sensitive Ranks

## Frozen test

Compute the tangent Gauss--Manin closure of the literal rank-twenty-six
interacting source inside each specialized component-soft quotient

\[
X_1=0,\qquad X_2=0,\qquad X_3=0.
\]

Retain the source numerator \(q_{g_{23}}+q_{g_{31}}\), all five marked
occurrences, and the moving-wall extension.  Do not identify the three soft
occurrences by an unlabelled cyclic quotient.

## Replicated ranks

At three nonintersecting exact fibers on each divisor over
\(\mathbf F_{32003}\), tangent closure gives

\[
\boxed{
\operatorname{rank}_{X_1=0}=20,
\qquad
\operatorname{rank}_{X_2=0}=20,
\qquad
\operatorname{rank}_{X_3=0}=24.
}
\]

The relation ranks are respectively

\[
11515,\qquad11515,\qquad11520.
\]

The literal source support remains three and its first covariant jet remains
rank three in every test.  At the transverse generic control \((1,3,5)\), the
horizontal closure returns to rank twenty-six.

## Meaning

The component-soft degeneration is real but occurrence-sensitive.  The
\(X_3\)-soft chart loses two directions, while the \(X_1\)- and \(X_2\)-soft
charts lose six.  This is permitted because the frozen occurrence-labelled
source \(q_{g_{23}}+q_{g_{31}}\) singles out a chart; cyclic equivalence would
require an independently derived occurrence transport.

All rank loss lies on predeclared soft Carrier support.  No new divisor is
indicated.  As in Entry 2339, specialized tangent closure is not a complete
derived pullback or nearby cycles and does not classify the missing
directions.  An independent all-ambient-axis census gives the same ranks.

## Next falsifier

Construct the three labelled soft Rees modules and the source-derived cyclic
transition among occurrence charts.  Determine whether their nearby-cycle
objects become isomorphic after transport or retain genuinely distinct
coefficient multiplicities.  Only then test recovery by the marked residue
and physical score ports.

## Artifacts

- `research/benincasa/check_rank26_labelled_component_soft_specialization.py`
- `research/benincasa/rank26-labelled-component-soft-specialization.json`
- `research/benincasa/check_rank26_tangent_support_closure.py`
- `research/benincasa/rank26-tangent-support-closure.json`

Sequence claim: `seqclaim-6d6747ef4eaed273cf32b307`.
