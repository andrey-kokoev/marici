# Cube coherence must be Koszul-normalized

## Correction to the raw-sign criterion

The Cartan operators `d` and `Q` are odd. In a graded category, exchanging two
odd arrows produces the canonical Koszul sign

\[
(-1)^{|d||Q|}=-1.
\]

Therefore a raw central `-I` comparison is not automatically an anomaly. It
may be the required super-interchange cell.

## Correct residual

Let `A_raw` be the operator comparison obtained from the two cube routes. Let
`chi` be the product of Koszul signs contributed by every interchange of
homogeneous constructors:

\[
\chi
=
(-1)^{\sum |f_i||g_i|}.
\]

The genuine anomaly is the normalized residual

\[
\mathfrak A_{\mathrm{true}}
=
\chi^{-1}\mathfrak A_{\mathrm{raw}}.
\]

The cube is graded-coherent when this normalized residual is the identity on
the complete typed domain.

## Exact parity fork

Reuse the Pauli fixture with raw residual `-I`.

If both crossed comparison cells are odd, then

\[
\chi=-1,
\]

and the normalized residual is `I`. The cube passes.

If one cell is odd and the other even, then

\[
\chi=1,
\]

and the same raw residual remains `-I`. The cube fails.

Identical matrices therefore have opposite coherence verdicts under different
source parity assignments. Parity is operative authority, not presentation
metadata.

## Source requirements

Every constructor in the two tower-four systems needs a source-derived degree:

- differential: odd;
- contraction: odd;
- number operator: even;
- boundary incidence: degree determined by the complex shift;
- reciprocal functor: normally even, unless it carries an explicit parity
  reversal;
- source refinement: normally even;
- determinant or Berezinian readout: graded by its declared line.

The degree must survive cutoff transport and completion. A constructor cannot
be regraded merely to cancel an observed residual.

## RH relevance

The desired Cartan law is itself a supercommutator:

\[
[d,Q]_{\mathrm{super}}=dQ+Qd.
\]

Forgetting parity turns the defining anticommutator into an apparent failure of
ordinary commutativity. Conversely, accepting every central sign as Koszul can
hide a genuine source anomaly. The sign is licensed only when the exact pair
of crossed arrows are both source-odd.

The reciprocal contraction sign is a separate datum. It reverses sector
orientation and must not be conflated with a Koszul sign from exchanging odd
operators. The cube compiler must account for both independently.

## DPC

Before classifying a cube residual:

1. freeze the degree of every edge and comparison cell;
2. enumerate the actual ordered crossings on both routes;
3. calculate the canonical Koszul factor;
4. calculate the reciprocal-orientation factor separately;
5. divide the raw residual by both declared factors;
6. inspect the remaining operator, boundary, and domain residual;
7. reject any post hoc parity assignment.

Finite falsifiers:

- the same `-I` raw residual under odd–odd and odd–even typings;
- a double-counted reciprocal minus sign;
- a boundary incidence whose degree changes after cone formation;
- finite parity coherence with a completion-induced grading collapse.

## Verdict

The fifth tower should be modeled as a graded double category or super
two-category. Its cube law is not strict commutativity but Koszul-normalized
interchange. This correction removes a false anomaly while making source
parity an additional irreducible constructor type.

