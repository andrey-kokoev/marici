# Forty-point Ramsey and Steiner extension: exact incidence-matrix comparison

Date: 2026-11-08. Exact, reproducible calculations. No resolution of the open value \(R(3,10)\) is claimed.

**Source design.** Kiermaier, Krčadinac, and Wassermann, *Steiner 3-designs as extensions*, 2026, Theorem 2.3, DOI 10.1007/s10623-026-01888-w. The source publishes two permutations and seven seed blocks generating an \(S(3,6,42)\). The companion `steiner_ramsey_matrix_test.py` reconstructs that object using only those generators, with no downloaded design files.

## 1. Published Steiner construction checked from its generators

- The two generators generate a group of order **432** (identified in the paper as \(\mathrm{AGL}(2,3)\)).
- Its orbits on the seven specified six-element blocks have sizes **12, 144, 108, 54, 216, 4, 36**, totaling **574** distinct blocks.
- All **11,480** triples on 42 points appear in exactly one six-block: \(S(3,6,42)\) verified.
- The 42 points form two orbits of sizes **18 and 24**. Stabilizers of points in these orbits have respective orders **24 and 18**.
- Deriving at either point produces an \(S(2,5,41)\), with **82** five-blocks. All **820** point pairs occur once.

Let \(Z\) be the 42×574 point–block incidence matrix. Since each point belongs to 82 blocks and every pair of distinct points belongs to 10 blocks,

\[
ZZ^{\mathsf T}=72I_{42}+10J_{42}.
\]

## 2. Two distinguished points leave ten four-point sectors

Choose two distinct points \(p,q\) in the 42-point design. Of the 574 blocks:

| Condition on the parent 6-block | Number | Size after deleting \(p,q\) | Covered triples of the remaining 40 points |
|---|---:|---:|---:|
| Contains both \(p,q\) | 10 | 4 | 40 |
| Contains \(p\), excludes \(q\) | 72 | 5 | 720 |
| Contains \(q\), excludes \(p\) | 72 | 5 | 720 |
| Contains neither | 420 | 6 | 8,400 |
| **Total** | **574** | | **9,880** |

Each three-element subset of the remaining 40 points lies in **exactly one** of these 574 derived blocks. This partitions the entire \(\binom{40}{3}=9,880\) triangle carrier; it was checked triple by triple.

The ten four-blocks are disjoint and partition the 40 points into **10 groups of 4**. Either 72-block family of fives contains one point from each of five distinct four-groups, and covers each pair belonging to *different* groups exactly once. Hence it is a **5-group-divisible design of type \(4^{10}\)**.

## 3. Full Gram identities, verified exactly

Let \(K\) be the 40×10 incidence matrix of the ten four-groups; let \(P,Q\) be the 40×72 matrices of the two five-block families; and let \(R\) be the 40×420 matrix for the six-block family. Write \(G=KK^{\mathsf T}\), so \(G_{xy}=1\) precisely when \(x,y\) belong to the same four-group (including \(x=y\)).

\[
\begin{aligned}
PP^{\mathsf T}&=9I+J-G,\\
QQ^{\mathsf T}&=9I+J-G,\\
RR^{\mathsf T}&=54I+8J+G,\\
KK^{\mathsf T}+PP^{\mathsf T}+QQ^{\mathsf T}+RR^{\mathsf T}&=72I+10J.
\end{aligned}
\]

The identities were checked pointwise for all 40×40 matrix entries, for pairs of deleted points from both automorphism orbits and for a pair with a surviving 24-element stabilizer.

The spectrum of \(PP^{\mathsf T}\) is **45 (multiplicity 1), 5 (multiplicity 9), 9 (multiplicity 30)**. Thus the original 40-dimensional incidence space has a natural **1+9+30** orthogonal decomposition associated with the ten four-groups. These are linear representation dimensions, not proved Ramsey coherence dimensions.

Let \(T_4,T_{5p},T_{5q},T_6\) be triple–block incidence matrices, each with 9,880 rows indexed by the triples of the 40-point set and with 10, 72, 72, 420 columns. Then

\[
T_4\mathbf 1+T_{5p}\mathbf 1+T_{5q}\mathbf 1+T_6\mathbf 1=\mathbf 1_{9880}.
\]

This is the exact Steiner triple-completion law, including all the formerly nonlocal triples.

## 4. The Ramsey problem as a different matrix system on the same 40 points

Let \(x\in\{0,1\}^{780}\) encode the red edges among the forty points (a coordinate for each unordered pair). A triangle-free graph with independence number at most 9 satisfies exactly:

\[
\sum_{e\subset\tau}x_e\le2\qquad
(\tau\in\binom{[40]}3),
\]

\[
\sum_{e\subset U}x_e\ge1\qquad
(U\in\binom{[40]}{10}).
\]

There are **9,880** red-triangle inequalities and **847,660,528** independent-ten-set inequalities, before symmetry reduction or separation.

A graph satisfying them would prove \(R(3,10)=41\), given the 2025 established upper bound \(R(3,10)\le41\). Their satisfiability remains an open problem. (Angeltveit, *R(3,10) ≤ 41*, Electronic Journal of Combinatorics 32(4), 2025.)

The ten four-blocks and one 72-member five-block family **partition all 780 pairs**: \(10\binom42+72\binom52=60+720=780\). Consequently the Steiner incidence data furnish a lossless coordinate permutation of all 780 edge variables, rather than an automatic reduction in their number.

If every pair within a given four- or five-block is forced to share one color, any red block creates a red clique of order 4 or 5. Therefore *whole-block red/blue labels* yield no nonempty triangle-free red graph, and cannot solve the Ramsey problem. The red-edge decisions must distinguish **positions inside blocks**, while remaining consistent across triples assembled from different blocks.

Only **760** of the 9,880 triples are internal to one of these 82 four-/five-blocks. The other **9,120** triple constraints connect pairs belonging to different blocks. Higher-order compatibility is therefore genuinely needed in any block-local parametrization.

## 5. Symmetry-preserving experiment

Choose \(p=1,q=10\), both fixed by the 24-element point stabilizer of \(p\) in the published Steiner group. After deleting \(p,q\), this stabilizer acts on 40 points in orbits of sizes **8,8,24** and partitions the 780 unordered pairs into **36 pair orbits**. All triangle-free restrictions on invariant red-edge selections reduce to **398 distinct orbitwise inequality patterns**; six pair orbits are individually forbidden because each contains a triangle.

`steiner_40_symmetry_search.py` solves the resulting finite binary optimization model with a degree-at-most-nine condition and adds independent-ten-set cuts as needed. Initial maximum-edge solutions are 9-regular with 180 edges, but have independence number **16**, and successive trial solutions in this restricted test still have independence number **13**. These are exploratory feasible triangle-free graphs, **not** a certificate that no invariant 40-vertex Ramsey graph exists. A complete infeasibility proof would require exhausting the 36-orbit binary decision system and all necessary independent-ten-set cuts.

## 6. Research result

The Steiner and Ramsey extension laws share a *triple-indexed incidence carrier*:

- Steiner requires **exactly one** containing block for every triple; its higher-strength extension supplies the missing triples.
- Ramsey requires **no all-red triangle** plus **no all-blue 10-set**; this couples multiple Steiner blocks and the 780 edge choices.

The verified 40-point partition is a structurally meaningful coordinate system for the unresolved Ramsey boundary. It does not itself choose the 780 binary edge values. The missing generative primitive is a block-internal edge rule compatible across the four types of triple-completion blocks.

## Reproduce

```bash
python steiner_ramsey_matrix_test.py
python steiner_40_symmetry_search.py 10 12
```

The first script uses only Python's standard library and proves all enumerated incidence identities by exact checks. The optional second script requires NumPy, SciPy, and NetworkX for finite symmetry-restricted optimization.

External sources:

- Kiermaier, Krčadinac & Wassermann (2026): https://link.springer.com/article/10.1007/s10623-026-01888-w
- Angeltveit (2025): https://www.combinatorics.org/ojs/index.php/eljc/article/view/v32i4p30
