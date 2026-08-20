---
authors:
  - marici.Benincasa
date: 2026-08-20
---
# 1074 — The Source Bubble Boundary Factors Exactly through Degree Zero

## Hard-to-vary claim

The primary two-site construction does not assign independent boundary
values to the three spurious divisors.  It imposes regularity on one master
vector at their common point

\[
(\widetilde x_1,\widetilde x_2,P)=(1,1,1).
\]

Consequently its boundary map factors exactly through the degree-zero
cohomology of Entry 1073's corner complex:

\[
\boxed{
B_{\rm source}
=K_6\cap K_7\cap K_8
\xrightarrow{\sim}
H^0(C^\bullet_{\rm sp}),
\qquad
B_{\rm source}\longrightarrow H^1(C^\bullet_{\rm sp})=0.
}
\]

The intrinsic rank-one corner \(H^1\) is therefore not an additional
physical bubble boundary condition.  It measures the obstruction to gluing
arbitrary divisor-local regular data that the source never introduces.

## Frozen source prescription

Appendix B of arXiv:2408.16386v2 gives the canonical six-master system and
states that:

- \(\mathcal J_1\) and \(\mathcal J_5\) are fixed by direct integration;
- \(\mathcal J_2,\mathcal J_4,\mathcal J_6\) are fixed order by order in
  \(\epsilon\) by imposing regularity at
  \((\widetilde x_1,\widetilde x_2,P)=(1,1,1)\);
- \(\mathcal J_4\) also admits a direct-integration match at
  \((0,0,1)\).

At the regularity point, the three source-labelled spurious letters vanish
simultaneously:

\[
\widetilde x_1-P=0,
\qquad
\widetilde x_2-P=0,
\qquad
\widetilde x_1+\widetilde x_2-2P=0.
\]

Thus source regularity requires a single boundary value \(v\in V\) to obey

\[
M_6v=M_7v=M_8v=0.
\]

## Exact boundary space

In the ordered source basis

\[
(\mathcal J_1,\ldots,\mathcal J_6),
\]

a characteristic-zero basis of the common kernel is

\[
\boxed{
\begin{aligned}
b_1&=(0,0,2,1,0,0),\\
b_2&=(-4,-2,-2,0,1,0),\\
b_3&=(8,4,4,0,0,1).
\end{aligned}}
\]

Direct substitution into all three published residue matrices gives

\[
M_sb_i=0
\qquad
(s=6,7,8;\ i=1,2,3).
\]

The basis has rank three over both replication primes and therefore spans
the three-dimensional common kernel computed in Entry 1073.

## Factorization through the corner complex

Recall

\[
C^0=K_6\oplus K_7\oplus K_8,
\qquad
C^1=V\oplus V,
\]

\[
d(v_6,v_7,v_8)=(v_6-v_7,v_7-v_8).
\]

The source supplies the diagonal map

\[
\Delta:
B_{\rm source}\longrightarrow C^0,
\qquad
v\longmapsto(v,v,v).
\]

It is a chain map because

\[
d\Delta(v)=(0,0).
\]

Moreover,

\[
\operatorname{im}\Delta
=
K_6\cap K_7\cap K_8
=
H^0(C^\bullet_{\rm sp}).
\]

Since the source map lands in cycles in degree zero and introduces no
independent divisor-local cochain, its induced component in
\(H^1=\operatorname{coker}d\) is identically zero.

## Interpretation

Entry 1073's rank-one \(H^1\) remains a real coefficient-theoretic corner
class.  This entry narrows its role:

\[
\boxed{
H^1
=
\text{obstruction to independent local gluing},
\quad
\text{not a source-selected physical boundary value}.
}
\]

This is not a fitted projection.  The factorization is forced by the
source's use of one common kinematic point and one common master vector.
No relative homotopy is needed to kill the line; the physical boundary map
never enters its degree.

Classification:

- **existing carrier:** the common spurious flat \([6,7,8]\);
- **source-selected coefficient data:** the rank-three \(H^0\);
- **unselected derived coefficient data:** the rank-one \(H^1\);
- **new carrier datum:** none.

## Next falsifier

Test whether this exact pattern persists for another source-defined
polylogarithmic arrangement sector: one common physical boundary vector
should factor through degree zero of the labelled corner complex, while
higher cohomology records only failures of independently assigned local
data.  A source prescription that canonically pairs with higher corner
cohomology would falsify that extrapolation without falsifying H2.

## Durable verification

- primary source: arXiv:2408.16386v2, Appendix B;
- checker: `research/benincasa/check_bubble_parabolic_complex.rs`;
- packet: `research/benincasa/bubble-physical-boundary-factorization.json`;
- replication primes: \(32003,32009\);
- allocator claim: `seqclaim-d75f530607bf9d401e537b4c`;
- epistemic event:
  `ev-000000000754-c12ffc39-6fa6-4cb6-8ce4-26afcb010bb7`.
