# 3320 — The Moving-Wall Leray Interval Has No v-Zero Horizontal Boundary

## Question

Can Entry 304's source-derived moving-wall Leray interval select the primitive
base-soft logarithmic torsor isolated in Entries 3315–3318?

The test must use the actual moving-wall formulas. Agreement of the two
primitive sign vectors is not enough to define a map between the fiber endpoint
pair and the base soft-divisor pair.

## Frozen source family

Entry 304 gives, on the physical total-energy chart,

\[
a=-y-Er,\qquad b=-x+Er,
\]

with fixed endpoint sections

\[
p_-:\ r=-1,\qquad p_+:\ r=1.
\]

The two normalized wall residues have the common coefficient

\[
-\frac{1}{2xy}.
\]

On the homogeneous chart used by the rank-twelve calculation,

\[
u=0,\qquad x=X_1=1,\qquad
y=X_2=\frac{v-2}{2},\qquad X_3=-\frac v2.
\]

Therefore the common Leray coefficient becomes

\[
-\frac{1}{v-2}.
\]

The endpoint sections remain constant in (v):

\[
\partial_v p_-=\partial_v p_+=0.
\]

## Exact support comparison

Order the base soft divisors as

\[
s_3=\{v=0\}=\{X_3=0\},\qquad
s_2=\{v=2\}=\{X_2=0\}.
\]

The residue vector of Entry 304's common normalization is

\[
\left(
\operatorname{Res}_{v=0},
\operatorname{Res}_{v=2}
\right)
\left(-\frac{dv}{v-2}\right)
=(0,-1).
\]

By contrast, the primitive candidate torsor from Entry 3315 is proportional to

\[
d\log\frac{v}{v-2},
\]

whose residue vector is

\[
(1,-1).
\]

Thus the established moving-wall family has no (v=0) horizontal residue. Its
two fiber endpoints carry the correct occurrence orientation, but their fixed
family and common coefficient do not produce the missing (s_3) component.

## Narrow result

Entry 304's two-wall Leray interval cannot be the source-defined selection map
for the candidate primitive base-soft torsor.

This is stronger than saying that a comparison map has not yet been written:
the frozen family has the wrong horizontal support. The match

\[
[p_+]-[p_-]\quad\leftrightarrow\quad[s_3]-[s_2]
\]

cannot be promoted to a specialization map from this family.

## Scope

This result excludes only the already established moving-wall Leray interval.
It does not exclude:

- a separately source-derived relative chain in parameter space;
- another occurrence sector whose normalization contains the (X_3=0) pole;
- a supported comparison defined at a deeper soft intersection.

No new carrier stratum is indicated.

## Next falsifier

Audit the frozen source for an independently defined occurrence-resolved chain
whose boundary meets both (X_2=0) and (X_3=0). If none exists, the candidate
(e_6) logarithmic torsor remains an allowed coefficient class but is not
source-selected by the current physical relative-cycle data.

## Verification

The exact symbolic audit is
`research/benincasa/checkers/audit_moving_wall_leray_base_boundary.py`; its
machine-readable packet is
`research/benincasa/results/moving_wall_leray_base_boundary.json`.
