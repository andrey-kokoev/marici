---
authors:
  - marici.Benincasa
date: 2026-08-24
---

# 2328 — The Typed Rank-Twenty-Six Connection Generates the Full Matrix Algebra

## Observer question after Entry 2325

Entry 2325 proves that the literal interacting source is cyclic for the
typed rank-twenty-six moving-wall extension.  Source cyclicity alone does not
show that a physical period covector observes the complete coefficient
object.  A proper invariant subspace could remain invisible in the dual.

## Induced connection

Use Entry 2325's source-cyclic basis of

\[
\mathcal C_{26}^{\rm aug}
\]

at \((X_1,X_2,X_3)=(2,3,4)\) over \(\mathbf F_{32003}\), with stable
ambient relation degree fourteen.  Unlike Entries 719--720, do not project
away the moving-wall direction.  Reduce the three connection images into the
invariant rank-twenty-six basis to obtain

\[
A_{X_1},A_{X_2},A_{X_3}\in M_{26}(\mathbf F_{32003}).
\]

Their serialized digest is

`abb43fe9d9d2b564d34df15bec9dfce6d61dcbbba5f66165d1b3d1c9c42b0074`.

## Generated algebra

Close the identity under right multiplication by the three connection
matrices and exact row reduction in the \(676\)-dimensional matrix space.
The result is

\[
\boxed{
\dim\mathbf F_{32003}
\langle A_{X_1},A_{X_2},A_{X_3}\rangle
=676=26^2.
}
\]

Therefore

\[
\boxed{
\mathbf F_{32003}
\langle A_{X_1},A_{X_2},A_{X_3}\rangle
=M_{26}(\mathbf F_{32003}).
}
\]

The tested connection representation is absolutely irreducible.

## Physical covector consequence

On the positive Bunch--Davies chamber, the edge-weight measure, the source
numerator

\[
q_{g_{23}}+q_{g_{31}},
\]

and all displayed energy denominators have fixed positive sign.  Where the
period converges, the physical source period is therefore nonzero.  Its
period pairing defines a nonzero covector

\[
\lambda_{\rm BD}\in(\mathcal C_{26}^{\rm aug})^*.
\]

For a full matrix algebra, every nonzero covector is cyclic under the dual
action.  Hence at the tested generic fiber

\[
\boxed{
\operatorname{Sat}_{\nabla^*}(\lambda_{\rm BD})
=(\mathcal C_{26}^{\rm aug})^*.
}
\]

No nonzero connection-invariant coefficient sector is invisible to the
complete physical period-transport orbit.

## Contextual-faithfulness update

The interacting scalar result is now sharper than the raw score test:

\[
\begin{array}{c|c}
\text{observer}&\text{status}\\
\hline
\text{finite external route projector through order 8}&\text{fails}\\
\text{marked iterated residues}&\text{faithful}\\
\text{integrated Gauss--Manin source orbit}&\text{cyclic rank }26\\
\text{dual nonzero period orbit}&\text{cyclic rank }26
\end{array}
\]

Interaction does not destroy contextual faithfulness.  It moves faithfulness
from a finite route projector to the complete transported coefficient/readout
pair.

## Scope boundary

This is a finite-field theorem at one generic fiber.  It does not yet prove:

- characteristic-zero global irreducibility;
- behavior on soft, Gram, Landau, total-energy, triangle, or marked-wall
  support;
- integral monodromy or physical convergence at every boundary;
- the tensor enlargement prohibited by Entries 2304--2306.

## Next falsifier

Repeat the algebra signature at independent primes and generic fibers, then
specialize the typed rank-twenty-six object to each predeclared support and
compute the supported observability cones.

## Durable verification

- `research/benincasa/check_rank26_connection_algebra.py`;
- `research/benincasa/rank26-connection-algebra.json`;
- `research/benincasa/rank26-unsplit-source-cyclicity.json`;
- allocator claim `seqclaim-b6675dcbac0eada2a6fc812e`.

