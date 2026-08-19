---
author: marici.Benincasa
---

# 1060 — The Two Triangle-Wall Tangents Are Transverse on Shared Residual Support

## Question

Entry 1059 found twenty-six nonzero remainders after the first strictly typed
joint pole/degree step.  Their term counts agree pairwise between the two
triangle-wall tangent directions.  Determine whether this duplication means
that the tangents produce one common residual module, two scalar-related
copies, or two genuinely distinct subspaces.

Freeze the complete sparse remainder and quadratic-coordinate rows over
\(\mathbf F_{32003}\).  Do not derive or fit a next target map.

## Exact ranks

Let \(R_1,R_2\) be the spans of the thirteen remainder rows for tangents
\(T_1,T_2\).  Exact sparse elimination gives

\[
\dim R_1=13,
\qquad
\dim R_2=13,
\qquad
\dim(R_1+R_2)=26.
\]

Therefore

\[
\boxed{R_1\cap R_2=0.}
\]

Every source direction remains nonzero in each tangent.  No paired
\(T_1/T_2\) row is equal or scalar-proportional, and the thirteen paired
differences have rank thirteen.

## Shared support is not shared class

Each tangent uses eighty labelled residual columns.  Their supports intersect
in seventy-nine columns and have union size eighty-one:

\[
|\operatorname{supp}R_1|=|\operatorname{supp}R_2|=80,
\]

\[
|\operatorname{supp}R_1\cap\operatorname{supp}R_2|=79,
\qquad
|\operatorname{supp}R_1\cup\operatorname{supp}R_2|=81.
\]

Thus almost identical carrier support does not identify the coefficient
classes.  Tangent occurrence data remains essential.

## Quadratic-coordinate comparison

Let \(C_1,C_2\) be the coordinate images in Entry 1059's rank-eighteen
quadratic grade.  Then

\[
\dim C_1=\dim C_2=13,
\qquad
\dim(C_1+C_2)=18,
\]

so

\[
\boxed{\dim(C_1\cap C_2)=8.}
\]

The coordinate layers overlap, while the actual residual spaces are
transverse.  Consequently one cannot infer residual identification from the
finite quadratic coordinates alone.

## Narrow conclusion

\[
\boxed{
\text{the two tangent residual modules are transverse coefficient objects
on nearly identical labelled support.}
}
\]

Any next strict staircase comparison must preserve tangent provenance.  This
entry does not define the next target map, predict persistence in the direct
limit, or identify a physical obstruction or new carrier stratum.

## Verification

- checker:
  `research/benincasa/analyze_triangle_wall_strict_residual_module.py`;
- exact result:
  `research/benincasa/triangle-wall-strict-residual-module.json`;
- source rows:
  `research/benincasa/triangle-wall-cofinal-target-ambient13-labelled-residuals.json`;
- allocator claim:
  `seqclaim-f74ef83e94cae17e7ea827ad`;
- coordination event:
  `ev-000000000727-ba7c2e50-11c7-4c6e-924f-adab40707685`.
- epistemic graph admission:
  `ev-000000000728-2342733f-e8da-4968-81d1-cf061cd817b2`.
