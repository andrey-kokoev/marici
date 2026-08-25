# Dual-matrix constructor certificate: freedom and safety are independent

## Two matrices

A compiled constructor family needs at least two finite representations.

### Selector matrix

\[
y=As+b
\qquad(\mathbb F_2).
\]

Its rank measures reachable joint logical choices. For \(k\) required binary
choices, selector completeness is

\[
\operatorname{rank}A=k.
\]

### Contact-incidence matrix

\[
M_{bc}\in\{0,1\}
\]

records which physical contact \(c\) touches correction block \(b\).
For a one-contact-per-block fault rule, contact safety within one hygiene
layer is

\[
\max_b\sum_cM_{bc}\le1.
\]

These conditions are independent.

## Four finite countermodels

Take two required logical choices.

### Complete and safe

\[
A=I_2,\qquad M=I_2.
\]

Both logical choices vary independently and each contact touches a distinct
block.

### Complete and unsafe

\[
A=I_2,\qquad M=\begin{pmatrix}1&1\end{pmatrix}.
\]

The choices are independent, but both contacts hit one correction block.
Selector rank cannot certify fault safety.

### Deficient and safe

\[
A=\begin{pmatrix}1\\1\end{pmatrix},
\qquad M=I_2.
\]

The contacts are physically separated, but only diagonal logical choices
are reachable. Safe support cannot certify constructor freedom.

### Deficient and unsafe

\[
A=\begin{pmatrix}1\\1\end{pmatrix},
\qquad M=\begin{pmatrix}1&1\end{pmatrix}.
\]

Both failures coexist.

Therefore no implication holds between selector completeness and contact
safety.

## Combined compiler record

A constructor node that includes controllable alternatives and physical
contacts should carry:

\[
\mathsf{Certificate}
=(A,b,M,\mathcal R,\mathcal F,\mathcal E),
\]

where:

- \(A,b\): logical selector map;
- \(M\): contact-to-correction-block incidence;
- \(\mathcal R\): selector and contact authority roots;
- \(\mathcal F\): fault domains and common-cause sets;
- \(\mathcal E\): epoch/replay scopes.

The compiler reports selector circuits from \(\ker A^T\) and overloaded
contact rows from \(M\) independently.

## Composition

When constructor nodes compose:

- selector matrices combine according to substitution and shared selector
  columns;
- contact matrices combine according to physical block identification and
  schedule layers;
- shared roots must remain shared rather than duplicated;
- a coherence cell may restrict the required selector orbit but cannot erase
  physical contact load;
- a recovery boundary may reset contact accumulation but cannot create
  missing selector rank.

Thus logical coherence and physical hygiene are different modalities in the
typed partial multicategory.

## Cross-sector consequences

- **Kitaev.** Declaring split pointer blocks may repair \(M\) while leaving
  shared-predicate selector correlations in \(A\). Conversely, independent
  predicates may repair \(A\) while a monolithic ququart keeps \(M\)
  overloaded.
- **Strominger.** Independent policy choices do not imply independent
  physical authority roots; disjoint physical supports do not imply all
  capability combinations are constructible.
- **Arithmetic/RH.** Probe independence and transport closure are separate
  from positivity or interaction incidence. A full labelled probe rank
  cannot orient the coupled kernel.
- **Benincasa.** Independent external controls and independent geometric
  support/contact classes require separate rank and incidence audits.

## Durable statement

> Joint constructor freedom and physical fault safety are orthogonal finite
> obligations. The selector matrix and contact-incidence matrix must both be
> carried through compilation; neither can be reconstructed from the other.

