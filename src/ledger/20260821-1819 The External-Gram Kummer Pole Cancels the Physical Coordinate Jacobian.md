# 1819 — The External-Gram Kummer Pole Cancels the Physical Coordinate Jacobian

## Question

Does Entry 1818's rank-110 physical coefficient object acquire supported
excess at a generic corank-one external-Gram degeneration?

## Rank-drop chart

Use a source-normalized local chart

\[
Q=\operatorname{diag}(1,1,s),
\qquad
H=Q^TQ=\operatorname{diag}(1,1,s^2).
\]

Then

\[
\det(H)=s^2
\]

and the physical coordinates are

\[
u=(\ell_1,\ell_2,s\ell_3).
\]

Their Jacobian is

\[
du_1\wedge du_2\wedge du_3
=
s\,d\ell_1\wedge d\ell_2\wedge d\ell_3.
\]

On the oriented Gram cover, choose

\[
\sqrt{\det(H)}=s.
\]

Therefore the strict-transformed physical current is

\[
\boxed{
\frac{du_1\wedge du_2\wedge du_3}{\sqrt{\det(H)}}
=
d\ell_1\wedge d\ell_2\wedge d\ell_3.
}
\]

## Deck covariance

The deck transformation \(s\mapsto-s\) flips both:

- the coordinate Jacobian;
- the chosen Gram square root.

Their ratio is invariant. Thus the Kummer character belongs to the coordinate
orientation descent, while the complete physical current is regular on the
oriented cover.

## Result

At a generic corank-one Gram point, away from additional marked-wall tangency
and soft support,

\[
\boxed{
\operatorname{rank}(\text{Gram nearby excess})=0.
}
\]

Entry 1818's 110 supported summands extend with the regular physical current.
No new carrier generator or coefficient extension is produced by the generic
Gram degeneration.

## Scope

This does not cover deeper loci where the Gram rank drop coincides with a
loss of wall-normal transversality or edge softness. Those require separate
labelled Rees calculations.

## Architectural consequence

The result is another instance of the resolved-normal/coarse-invariant
distinction:

\[
s\ \text{is the linear oriented normal},
\qquad
\det(H)=s^2\ \text{is the coarse invariant}.
\]

The apparent Kummer pole disappears only when the physical coordinate
Jacobian and coefficient line are retained together.

## Next falsifier

Classify the intersections of \(\det(H)=0\) with loss of transverse wall rank
among the 22 active pair orbits. Test whether those deeper loci are generated
by existing soft and Gram carrier strata or require a new incidence type.

## Evidence

- research/benincasa/checkers/five_site_g5_transverse_external_gram_specialization.py
- research/benincasa/results/five-site-g5-transverse-external-gram-specialization.json
- Entries 1216 and 1818
- allocator claim: seqclaim-804a237c6e09cfc1e34aa029
