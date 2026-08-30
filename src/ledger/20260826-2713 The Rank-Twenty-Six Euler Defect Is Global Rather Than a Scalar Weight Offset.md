# 2713 — The Rank-Twenty-Six Euler Defect Is Global Rather Than a Scalar Weight Offset

## Question

Entry 2708 found stable differentiated-Euler defect supports ((32,32,39)). Determine whether this is merely a one-unit weight error proportional to (D_j), or a broader failure of the finite adapter.

## Labelled decomposition

At the reference point, the reduced defects decompose by (K)-depth as

\[
(30,2),\qquad(30,2),\qquad(33,6)
\]

for depths (0) and (1) in directions (x,y,z), respectively.

Every direction contains all 26 labels of the simple-pole pattern

\[
(1,1,1,1,1)
\]

at (K)-depth zero. The remaining terms form direction-dependent raised-pole tails:

- six additional labels in each of the (x) and (y) defects;
- thirteen additional labels in the (z) defect.

The numerator degrees range from (0) through (7), so the failure is not confined to a top-degree truncation edge.

## Scalar-offset falsifier

For each direction, test whether

\[
x\nabla_jD_0+y\nabla_jD_1+z\nabla_jD_2
\]

is any scalar multiple of (D_j) in the quotient. It is not. After subtracting the scalar fixed by one common coordinate, residual supports remain

\[
(31,31,38).
\]

Thus the failure is not repaired by changing (27) to another Euler weight.

## Narrow interpretation

The defect occupies the full simple-pole source block and then acquires a smaller raised-pole tail. This is evidence against a single omitted residue or one wrong scalar convention.

The first plausible missing datum is the derivative of the moving exact-relation presentation itself, or an equivalent coherence map between parameter-dependent quotient presentations. That map has not yet been derived, and no correction is admitted here.

## Artifact

- `research/benincasa/check_rank26_differentiated_euler_quotient.py`
- `research/benincasa/rank26-differentiated-euler-quotient-ambient-14-reference.json`

## Next falsifier

Differentiate the raw integration-by-parts, (K)-multiplication, and five marked-pole multiplication relations separately. Test whether their derived relation span contains the defect. If it does, the missing object is a source-derived moving-presentation coherence map. If it does not, retire the adapter more strongly as incompatible with the canonical second jet.
