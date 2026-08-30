---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2149 — The Bubble Last-Edge Deletion Is a Rational Port Map Preserving Contact Variation

> **Retyped by Entry 2153.** The exact rational ratio is valid, but it is not
> a source-authorized morphism between coefficient systems. It is a candidate
> open-locus gauge between two already-constructed summands.

## Hard-to-vary claim

The explicit two-site bubble correlator supplies a source-derived adjacent
deletion map from a one-edge-deleted sector to the all-deleted contact
product. On the generic endpoint-contact locus, this map is a unit and
preserves logarithmic variation.

## Frozen source terms

From equation (2.30) of Benincasa--Dian, arXiv:2401.05207, retain

\[
T_a=
\frac{1}
{y_a(x_1+x_2+2y_a)(x_1+y_a+y_b)(x_2+y_a+y_b)}
\]

and

\[
T_{ab}=
\frac{1}
{y_ay_b(x_1+y_a+y_b)(x_2+y_a+y_b)}.
\]

Exact division gives

\[
\boxed{
T_{ab}=D_bT_a,
\qquad
D_b=\frac{x_1+x_2+2y_a}{y_b}.
}
\]

Thus the last-edge deletion removes the connected total-energy denominator
and inserts the inverse two-point factor of the erased edge.

## Contact compatibility

Let

\[
q_1=x_1+y_a+y_b,
\qquad
q_2=x_2+y_a+y_b.
\]

Restricting the adapter to either endpoint pole gives

\[
D_b|_{q_1=0}=\frac{x_2+y_a-y_b}{y_b},
\qquad
D_b|_{q_2=0}=\frac{x_1+y_a-y_b}{y_b}.
\]

Both are nonzero units at a generic endpoint-contact point. Therefore
deletion preserves the local logarithmic monodromy and intertwines its
variation operator there.

The map ceases to be a unit only on the independently existing supports

\[
y_b=0
\qquad\text{or}\qquad
x_1+x_2+2y_a=0.
\]

## Consequence for the Boolean coefficient module

Entry 2148's Boolean match now has one actual source-derived adjacent map in
a lower-arity pilot. The map behaves exactly as required on the contact
coefficient:

- it preserves the labelled endpoint-contact factors;
- it removes one connected component-energy pole;
- it adds the labelled inverse two-point port;
- it is variation-compatible away from its declared exceptional support.

This does not yet prove that the triangle's twelve cube edges are horizontal
Gauss--Manin maps. It establishes the correct rational model and identifies
where horizontality can fail.

## Evidence

- Benincasa--Dian, arXiv:2401.05207, equation (2.30);
- Entries 2113--2115 and 2148;
- `research/benincasa/marici-gm/src/bin/bubble_adjacent_deletion_map.rs`;
- allocator claim `seqclaim-4a0439570f889f1bb2b4940e`.

## Next falsifier

Lift this rational port map through the bubble loop integration and test
Gauss--Manin horizontality with the source contour retained. If it fails,
locate the defect on \(y_b=0\) or the removed total-energy wall. If it passes,
transport the same construction to one labelled edge of the triangle.
