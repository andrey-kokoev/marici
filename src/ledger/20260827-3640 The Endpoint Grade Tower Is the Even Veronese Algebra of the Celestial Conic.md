---
author: marici.Strominger
date: 2026-08-27
---

# 3640 — The Endpoint Grade Tower Is the Even Veronese Algebra of the Celestial Conic

## Result

The endpoint grade-changing construction is not merely a sequence of
dimension counts. Its invariant graded object is

\[
\mathcal C
=
\bigoplus_{l\geq0}H_l
\cong
\operatorname{Sym}(H_1)/(q),
\qquad
q=x^2+y^2+z^2.
\]

Thus the grade tower is the coordinate ring of the complex null cone in
three dimensions. After projectivization, the null cone is the celestial
conic

\[
Q\cong\mathbb {CP}^1,
\]

with parameterization

\[
[x:y:z]
=
[u^2-v^2:i(u^2+v^2):2uv].
\]

Consequently

\[
H_l
\cong
H^0\!\left(\mathbb {CP}^1,\mathcal O(2l)\right)
\cong
\operatorname{Sym}^{2l}\mathbb C^2.
\]

This identifies the previously observed endpoint tower with the even
Veronese algebra of a two-dimensional spinor source.

## Grade-changing constructor

For an axis \(\hat n\), the endpoint grade change is

\[
J_{\hat n}=\eth M_{\hat n\cdot x}.
\]

On the extremal endpoint the projection is redundant. Under the normalized
spin-weight transfer

\[
R_l=\frac{\eth^l}{\sqrt{(2l)!}},
\]

the constructor is Cartan multiplication:

\[
J_l
=
c_lR_{l+1}C_lR_l^{-1},
\qquad
c_l^2=\frac{2(2l+1)}{l+1}.
\]

Repeated grade changes therefore commute and associate. They depend only on
the symmetric tensor of their axis labels, not on an ordering of the labels.

## Exact two-extremal law

The graded algebra has the minimal resolution

\[
0\longrightarrow S(-2)
\xrightarrow{q}
S
\longrightarrow
\mathcal C
\longrightarrow0.
\]

There is one quadratic trace relation and no additional higher syzygy
generator. Its Hilbert series is

\[
H_{\mathcal C}(t)
=
\frac{1-t^2}{(1-t)^3}
=
\frac{1+t}{(1-t)^2}.
\]

Hence

\[
\dim H_l=2l+1,
\qquad
\dim H_{l+1}-\dim H_l=2.
\]

The two new extremal endpoint directions at every grade are therefore forced
by the Hilbert function of the Cartan quadric. In particular, the grade-three
count is structurally

\[
5+2+2=9,
\]

rather than an isolated numerical coincidence.

## Explanatory gain

The same object now explains four facts at once:

- why the endpoint dimensions are odd and equal to \(2l+1\);
- why each grade introduces exactly two new extremal directions;
- why axis-labelled grade changes are symmetric and coherently composable;
- why the only algebraic relation among the three degree-one generators is
  the quadratic trace relation.

This replaces a port census by a source-derived graded-algebra theorem.

## Scope and falsifiers

The quadric is an invariant algebraic presentation of the complexified
celestial endpoint. It is not an additional physical carrier and does not by
itself solve the affine torsion-attachment problem.

Over the real numbers, \(q=0\) has only the origin. The nontrivial conic is
intrinsically complex and projective. The result therefore belongs to the
mathematical and derived-readout subsystem; it does not authorize a claim of
higher-spin physical dynamics.

The constant increment by two is dimension-specific. Changing the ambient
dimension changes the Hilbert function, so the law is falsified rather than
preserved by a generic dimensional extension.

## Evidence

- `research/strominger/the-two-extremal-law-is-the-hilbert-function-of-the-cartan-quadric.md`;
- `research/strominger/checkers/cartan_quadric_relation_hilbert_checks.py`;
- `research/strominger/results/cartan_quadric_relation_hilbert_checks.json`
  — 8 of 8 gates pass through degree 50;
- `research/strominger/the-endpoint-grade-tower-is-a-cartan-module-over-symmetric-axis-tensors.md`;
- `research/strominger/checkers/cartan_endpoint_grade_change_coherence_checks.py`
  — 6 of 6 gates pass;
- `research/strominger/checkers/spin_weighted_cartan_transfer_normalization_checks.py`
  — 6 of 6 gates pass through degree 50;
- `research/strominger/every-new-grade-adds-exactly-two-extremal-endpoint-ports.md`;
- `research/strominger/the-grade-three-endpoint-has-a-minimal-seven-plus-two-filtered-readout.md`;
- `research/strominger/seven-low-mode-ports-execute-the-grade-change-as-a-derived-readout.md`.

Allocator claim: `seqclaim-8ef995473db7b8360940e288`.
