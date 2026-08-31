# Common-source cell-support provenance: WP1052

## Question

Can detector and monitor cell supports be derived from one typed `physical16`
source cell rather than declared as separate instrument coordinates?

## Minimal source-support cell

Use six atoms with exact branch weight \(1/4\):

\[
F_{\rm det},F_{\rm null},R_{\rm det},R_{\rm null},X_{\rm det},X_{\rm null}.
\]

The \(F\) atoms carry detector provenance, the \(R\) atoms carry monitor
provenance, and the \(X\) atoms carry both. Every atom also carries a detected
or null label. Detector and monitor supports are derived from the same atom
set:

\[
\alpha=\sum_{a\ni{\rm detector}}w_a=1,
\qquad
\beta=\sum_{a\ni{\rm monitor}}w_a=1.
\]

The shared cross weight is

\[
w_X=w_{X_{\rm det}}+w_{X_{\rm null}}=\frac12,
\]

so

\[
c=\frac{w_X}{\sqrt{\alpha\beta}}=\frac12.
\]

The monitor detected weight is \(1/2\), hence

\[
\eta=\frac12.
\]

Detector, monitor, and cross branches are separately null-complete. The
derived WP1051 rows for \((B,\mathcal L,g,\nu,d)=(0,4,1,1,1)\) are therefore

\[
S=4,
\qquad
D=8,
\qquad
M=\eta c\beta=\frac14,
\qquad
N=\eta\beta=\frac12,
\]

with \(\sigma=1\).

## Declared-overlap falsifier

A split-cell proxy can declare

\[
\alpha=1,
\qquad
\beta=1,
\qquad
\eta=\frac12,
\qquad
c=\frac12,
\qquad
\sigma=1.
\]

It then mimics

\[
M=\frac14,
\qquad
N=\frac12,
\qquad
D=8.
\]

But if no atom carries both detector and monitor provenance, atom derivation
gives

\[
w_X=0,
\qquad
c=0,
\qquad
\sigma=0,
\qquad
D=0.
\]

Null completeness alone does not repair this: the proxy can retain all of its
null branches while still lacking cross-cell provenance.

## Classification

This is a conditional common-source support constructor. Finite atom
provenance derives detector support, monitor support, overlap, efficiency,
same-cell certification, and null completeness from one typed cell. A scalar
overlap declaration without cross-atom provenance is rejected.

## Disposition

Productive. WP1051's typed supports now have a minimal common-source
provenance realization. The next gate is physical: derive the atom weights and
Flavor/reference/cross/null labels from `physical16` source dynamics rather
than posit the finite support cell.

Checker: `research/flavor/checkers/wp1052_common_source_cell_support_provenance.py`

Result: `results/wp1052_common_source_cell_support_provenance.json`
