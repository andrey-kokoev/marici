# 1055 — The Triangle-Wall Thirteen-Plane Is Stable from Ambient Degree Ten to Eleven

## Falsifier

Entry 1053 showed that a fixed ambient-degree-ten window is not closed under
the external connection.  Before constructing a joint pole/degree staircase,
test whether the depth-three thirteen-plane itself is merely a degree-ten
boundary artifact.

Freeze Cayley--Menger pole depth three, marked pole depth two, pole-extension
stage two, the triangle-wall point \((2,3,5)\), and characteristic 32003.
Compare ambient relation degrees ten and eleven through the honest labelled
column inclusion.

## Labelled inclusion

Numeric column positions change with the ambient cutoff.  The thirteen
degree-ten basis rows were therefore transported by their full labels

\[
(k;q_1,q_2,q_3,q_{23},q_{31};a^ib^j)
\]

and normal-jet block, not by numeric-index prefixing.

## Result

The exact-valuation-two ranks are

\[
\dim E_2^{(10)}=13,
\qquad
\dim E_2^{(11)}=13.
\]

All thirteen transported degree-ten representatives reduce with zero
remainder in degree eleven.  Their coordinate matrix has rank thirteen:

\[
\boxed{
E_2^{(10)}\xrightarrow{\sim}E_2^{(11)}.
}
\]

Hence the depth-three one-plus-five pole grade survives the first honest
ambient-degree enlargement.  It is not an artifact confined to the outer
degree-ten boundary.

## Scope

This proves one transition, not stabilization of the ambient direct system.
It also does not repair the same-window connection failure of Entry 1053:
connection images can require a larger degree jump than one.  The next test
must derive a cofinal staircase from the actual degree of \(T(K)\), then check
transport into that enlarged target.

## Durable verification

- labelled basis remapper:
  `research/benincasa/remap_triangle_wall_basis_by_labels.py`;
- degree-eleven reduction packet:
  `research/benincasa/triangle-wall-ambient10-to11-reduction.json`;
- allocator claim: `seqclaim-ed66e7a5d50319639828c786`.
- epistemic graph event:
  `ev-000000000697-5843e143-8235-433e-94ec-1b0f5a30dcaa`.
