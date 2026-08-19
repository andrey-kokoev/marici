# The Exact-Valuation Seven-Plane Is Flat Along Both Coordinate Wall Tangents

## Independent tangent

Entry 1003 established first-order flatness of

\[
E_2(C)=
\frac{\ker\Lambda\cap\operatorname{im}\Lambda}
     {\ker\Lambda\cap\operatorname{im}\Lambda^2}
\]

along the wall tangent

\[
(X_1,X_2,X_3)=(2+\tau,3,5+\tau+\Lambda).
\]

The independent coordinate tangent is

\[
(X_1,X_2,X_3)=(2,3+\tau,5+\tau+\Lambda).
\]

It preserves the triangle wall \(X_3=X_1+X_2\) while varying \(X_2\)
rather than \(X_1\).

## Exact replicated ranks

Over

\[
B=\mathbf F_{32003}[\tau]/(\tau^2),
\]

the complete mixed relation ranks are

\[
\begin{array}{c|c|c|c}
k&\operatorname{rank}R_{k,\tau}
&2\operatorname{rank}R_k&\text{excess}\\
\hline
1&12610&12610&0\\
2&25230&25230&0\\
3&37864&37864&0.
\end{array}
\]

These are identical to the independently generated \(X_1\)-tangent ranks.
With 11520 columns per normal grade, the mixed cokernel dimensions are again

\[
(10430,20850,31256).
\]

Consequently

\[
\dim\operatorname{im}\Lambda=31256-10430=20826,
\]

\[
\dim\operatorname{im}\Lambda^2=31256-20850=10406,
\]

and

\[
\dim E_{2,\tau}=20826-2(10406)=14=2\cdot7.
\]

The same freeness and saturation argument as Entry 1003 therefore gives

\[
\boxed{E_{2,\tau}\simeq B^7}
\]

along the \(X_2\) tangent.

## Meaning and boundary

The exact-valuation seven-plane is first-order flat along both coordinate
generators of the triangle wall tangent space at the tested generic point.
This removes a coordinate-direction accident from Entry 1003.

It does **not** yet provide a canonical Gauss--Manin connection.  Separate
free dual-number lifts can be trivialized noncanonically, and the two results
do not test curvature or mixed-tangent integrability.  The next typed object
is the connection class induced directly by the source relation complex,
followed by its occurrence-covariance and curvature tests.

## Durable artifacts

- `research/nima/export_triangle_wall_dual_rows.py`;
- `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- `research/nima/triangle-wall-dual-relation-rank.json`.

## Sequence

- allocator claim: `seqclaim-822561677bc619e0d10ea2e3`.
