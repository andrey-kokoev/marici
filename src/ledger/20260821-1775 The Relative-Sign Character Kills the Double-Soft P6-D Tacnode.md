# 1775 — The Relative-Sign Character Kills the Double-Soft \(P_6\)-\(D\) Tacnode

## Question

Entry 1772 identifies the repeated \((u-1)^2\) resultant component with the
existing double-site-soft carrier corner

\[
X_2=X_3=0.
\]

Does the relative-sign Hom line acquire supported cohomology from the
nontransverse \(P_6\)-\(D\) collision there?

## Local singularity

At \((u,v)=(1,1)\), both branches are smooth, with initial forms

\[
\operatorname{in}(4P_6)=8x,
\qquad
\operatorname{in}(D)=-4x,
\qquad x=u-1.
\]

The exact resultant is

\[
16u^4(u-1)^2(1-8u+12u^2-4u^3).
\]

The last factor is one at \(u=1\). Hence the local intersection
multiplicity is exactly two. The union of the two smooth branches is formally
an \(A_3\) tacnode:

\[
Y^2-X^4=0.
\]

Its ordinary Milnor number is three.

## Character test

The relative Hom line has character

\[
(-1,-1)
\]

on the ordered \((P_6,D)\) meridians. It is therefore the pullback of the
total-link character \(t=-1\). The \(A_3\) Alexander polynomial is

\[
\Delta_{A_3}(t)=(t-1)(t^2+1).
\]

At the source character,

\[
\Delta_{A_3}(-1)=-4\neq0.
\]

Consequently the characteristic-zero twisted local link complex is acyclic:

\[
\boxed{
H^\bullet(\operatorname{Link}_{A_3};\mathcal L_{(-1,-1)})=0.
}
\]

## Consequence

The ordinary rank-three tacnode Milnor space produces no supported
relative-sign extension class. Together with Entries 1770 and 1774, this
closes the relative-sign \(P_6\)-wall route on every component of the exact
resultants, including both nontransverse soft corners.

This conclusion is sector-specific: it does not remove untwisted or differently
twisted coefficient systems at the same carrier strata.

## Durable evidence

- `research/benincasa/checkers/p6_d_tacnode_kummer.py`
- `research/benincasa/results/p6-d-tacnode-kummer.json`
- `research/benincasa/p6-d-tacnode-kummer.md`
- allocator claim: `seqclaim-7a019bfaf5def0b6e7bcf0cf`

