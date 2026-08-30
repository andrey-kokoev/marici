# 4104 — The Integral Barcode Complex Is Filtered by the Labelled Pole Poset

## Question

Entry 4100 found that the undirected relation graph of the primitive integral
barcode presentation is connected. Does the source nevertheless provide a
finer filtration that permits exact saturation by blocks?

## Frozen filtration

For a labelled coordinate

\[
(k;\ell_1,\ell_2,\ell_3,\ell_{23},\ell_{31};a,b),
\]

retain the block label

\[
\bigl(k;\ell_1,\ell_2,\ell_3,\ell_{23},\ell_{31}\bigr).
\]

At depth three, \(k\in\{0,1,2,3\}\), while each denominator level belongs to
\(\{1,2\}\). The block poset is therefore

\[
C_4\times B_5,
\]

with the five Boolean coordinates occurrence-labelled.

The domain block of every relation is fixed by its source integration-by-parts
or multiplication generator before inspecting its nonzero coefficients.

## Result

The primitive integral presentation occupies all \(128\) coordinate blocks.
Its \(40656\) relation generators occupy \(127\) domain blocks and induce
\(543\) block incidences.

For every nonzero matrix entry, the target block is greater than or equal to
the declared source block in the product order:

\[
k_{\rm target}\ge k_{\rm source},
\qquad
\ell_{i,\rm target}\ge\ell_{i,\rm source}
\quad\text{for every labelled denominator }i.
\]

The audit found zero violations.

Thus the complete integral relation matrix is upper filtered by a
source-derived labelled pole poset, even though its undirected relation graph
has one component.

## Interpretation

Undirected connectedness does not force one monolithic Smith computation.
Forgetting relation variance collapses a directed filtered complex into a
single graph component and loses the structure needed for saturation.

The admissible exact strategy is now:

1. compute saturated associated-grade kernels and images on each labelled
   pole block;
2. extend them along the \(543\) source incidences;
3. retain extension and torsion data at every block attachment;
4. compare the resulting filtered integral object with all good-prime barcode
   filtrations.

This is not componentwise decomposition. The blocks remain coupled by
upper-poset extension maps.

## SCC status

The SCC host model passes, but the barcode lift remains unpromoted. This result
supplies the missing source-derived filtration, not the saturation
certificates themselves.

## Next finite falsifier

Compute the associated-grade relation matrices for all \(128\) blocks. Test
whether each image is saturated and whether successive block attachment
recovers the modular dimensions

\[
20,\qquad6,\qquad27
\]

and depth-four emergence rank \(1353\).

Any nontrivial determinantal divisor must be retained as integral torsion. It
must not be divided away to force agreement with the finite-field barcode.

## Artifacts

- research/benincasa/checkers/check_interaction_net_integral_source_presentation.py
- research/benincasa/results/interaction-net-integral-source-presentation.json
