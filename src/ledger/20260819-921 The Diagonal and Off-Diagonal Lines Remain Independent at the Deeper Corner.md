# 921 — The Diagonal and Off-Diagonal Lines Remain Independent at the Deeper Corner

## Comparison problem

The diagonal flag

\[
(a,x,q)=(s_{14},s_{23},s_{235})=0
\]

has a rank-one first conormal grade from Entry 912. The off-diagonal flag

\[
(a,y,q)=(s_{14},s_{35},s_{235})=0
\]

has the Cartier-twisted Rees line of Entries 918–920.

Their ranks agree, but this does not type a comparison. The first admissible test is to restrict both source-derived representatives to their actual common deeper corner in the same transition target.

## Forced fourth normal

Use multiplicative channel coordinates

\[
Q=XYZ.
\]

The simultaneous conditions

\[
X=Y=Q=1
\]

force

\[
Z=1.
\]

Therefore setting only (X=1) after the off-diagonal Rees restriction does not reach the common corner. The (Z)-normal is mandatory.

## Inherited lattice regularizations

The off-diagonal exceptional line carries the factor (1/U), so its regular generator is obtained by multiplying by (U).

The diagonal first-conormal line develops a simple pole at (Z=1). Its inherited regular generator is therefore obtained by multiplying by (Z-1) before specialization.

Both operations use existing source equations. No fitted scalar is introduced.

## Exact common-corner comparison

After these two regularizations, the diagonal generator has twelve nonzero matrix entries and target direction

\[
v_x=(1,-1),
\]

whereas the off-diagonal generator has six nonzero entries and target direction

\[
v_y=(0,1).
\]

The exact (2\times2) minor in the first source column is

\[
\frac{
4(A_2B_{24}-1)^2(A_3B_{34}-1)^2
\cdot(A_2B_{24}+1)^2(A_3B_{34}+1)^2
}{A_2^2B_{24}^2A_3^2B_{34}^2},
\]

which is generically nonzero. Hence

\[
\boxed{\operatorname{rank}\langle v_x,v_y\rangle=2.}
\]

The identity comparison in the common transition target does not identify the two lines.

## Narrow conclusion

The diagonal conormal line and the off-diagonal Rees line are distinct filtered coefficient directions even at their shared deeper corner:

\[
\boxed{
\mathcal L_x^{(1)}|_{\rm deep}
\not\simeq_{m identity}
\mathcal L_y^{\rm Rees}|_{\rm deep}.
}
\]

This rules out assembling them by rank matching or by treating the off-diagonal line as another chart of the diagonal line. It does not rule out a nontrivial differential between them.

No such differential is supplied by the frozen basis-transition matrix: it provides the two sections but no map changing filtration type. A comparison remains untyped until derived from a marked-incidence differential, a localization triangle, or a Rees specialization morphism.

## Next falsifier

Search the frozen six-point marked-incidence complex for a boundary operator whose source and target are exactly these two filtered lines. If one exists, compute its common-corner scalar and symmetry character. If none exists, retain the rank-two direct sum and record that the proposed mixed differential is absent at this level.
