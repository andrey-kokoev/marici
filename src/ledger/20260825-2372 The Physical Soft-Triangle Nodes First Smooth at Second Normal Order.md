---
author: marici.Benincasa
date: 2026-08-25
---

# 2372 — The Physical Soft-Triangle Nodes First Smooth at Second Normal Order

## Question

Entries 2368--2371 identify the endpoint nodes, their physical incidence,
and their occurrence module. A node class is not activated merely because
it exists. Its source-derived smoothing direction must be computed from the
full kernel before taking nearby cycles.

Sequence claim: seqclaim-89fd4bffee14eb4371953eef.

## Full normal expansion

After the weighted substitution, divide the complete residue kernel by its
common \(x^2\) factor:

\[
\frac{K_0}{x^2}
=K_{\rm exc}+xK_1+x^2K_2+O(x^3).
\]

The first coefficient is

\[
K_1
=2p(\xi+2)
\left(
-a^2\kappa\xi-2a^2
+4\kappa^2p^2+13\kappa\xi p^2
+4\xi^2p^2+6p^2
\right).
\]

Exact evaluation at every one of Entry 2368's eight nodes gives

\[
\boxed{K_1=0.}
\]

Thus the ordinary first jet does not smooth any endpoint node.

## Second normal grade

The second coefficient is nonzero at all eight nodes. On the four physical
nodes of Entry 2369, in the same order, it is

\[
\boxed{
9p^2,\qquad9p^2,\qquad p^2,\qquad81p^2.
}
\]

For generic \(p\ne0\), every physical node therefore has first nonzero
smoothing order two.

## Result

\[
\boxed{
\text{the physical endpoint-node packet is invisible to the first normal
jet and is born in }\operatorname{gr}^{(2)}_{X_1}.
}
\]

This is a direct source computation, not an inference from the earlier
quartic \(\mathcal Q\). It independently reproduces the program's
loop-specific warning:

\[
\text{first jet}\not\Rightarrow
\text{control of integrated loop deformation}.
\]

## Classification

- support: existing site-soft and triangle-endpoint intersections;
- first normal grade: zero;
- second normal grade: four nonzero physical smoothing coefficients;
- coefficient type: local \(A_1\) vanishing-cycle packet;
- new Carrier datum: none.

The result strengthens H2 while proving that a first-jet-only physical
observer is insufficient at this corner.

## Scope

The calculation fixes normal order and source coefficients. It does not yet
fix Picard--Lefschetz orientation signs, integral thimble normalization,
relations among the four cycles, or their physical period amplitudes.

## Durable verification

- research/benincasa/check_soft_triangle_node_smoothing.py;
- research/benincasa/soft-triangle-node-smoothing.json;
- exact \(K_0,K_1,K_2\) evaluations at all eight labelled nodes;
- epistemic event
  ev-000000003250-254185b3-868a-4211-b2f8-149ff7f538ba.

## Next falsifier

Use \(K_2\) to normalize the local Picard--Lefschetz maps. Compute their
signs against the positive-sheet chain orientations from Entry 2370, then
assemble the four physical node lines through the rational occurrence
quotient of Entry 2371. The resulting rank and monodromy decide whether a
second-grade physical coefficient survives.
