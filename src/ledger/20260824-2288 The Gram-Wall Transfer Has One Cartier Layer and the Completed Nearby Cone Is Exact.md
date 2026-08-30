# 2288 — The Gram-Wall Transfer Has One Cartier Layer and the Completed Nearby Cone Is Exact

## Local normal form

Let

\[
c=q\cdot\widehat n
\]

be the resolved normal to the existing Gram wall.  Entries 2276 and 2281 show
that the finite-\(q\) tensor determinant is

\[
\det T=c\,U,
\qquad
U|_{c=0}\ne0,
\]

throughout the generic positive-energy wall.  Entry 2283 shows that
\(T|_{c=0}\) has rank exactly two, so a \(2\times2\) minor is a local unit.

Over the local DVR \(\mathbb Q[[c]]\), these two facts force Smith form

\[
\boxed{
T\sim\operatorname{diag}(1,1,c).
}
\]

Thus the tensor-only comparison cone has exactly one Cartier-supported
coefficient:

\[
H^0\operatorname{Cone}(T)
\simeq
\mathbb Q[[c]]/(c).
\]

There is no higher Cartier length, hidden first-normal extension, or extra
nearby rank at this wall.

## Completion by the direct score port

The direct scalar-plus-quadrupole Gaussian score matrix has determinant
\(-6\), a unit in \(\mathbb Q[[c]]\).  Entry 2283 computes its nonzero
restriction to the tensor kernel.  Therefore adjoining this port contracts
the unique Cartier costalk:

\[
\boxed{
H^\bullet\operatorname{Cone}(T\oplus Q)=0
}
\]

over the entire local Gram neighborhood, including \(c=0\).

## Nearby-cycle interpretation

The tensor channel alone has one ordinary linear-normal supported class.  It
is not a new nearby coefficient object: it is the cokernel of a transport map
whose determinant crosses the existing Gram wall simply.  The complete
admitted score-plus-tensor observer complex is locally exact, so no residual
nearby-cycle class survives.

Classification:

\[
\boxed{
\text{existing Gram Cartier layer}
+\text{recoverable transport projection}
\Longrightarrow
\text{no completed-observer obstruction}.
}
\]

## Verification

`research/benincasa/checkers/gram_wall_smith_nearby_cone.rs` verifies a local
representative with determinant \(2c\), a unit two-minor, the resulting Smith
invariants, and the unit direct-score completion.
