# A linear scalar zero is one channel short of even Fourier-graph incidence

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact minimal observation-rank obstruction

## Boundary equations versus scalar readout

Let \(F_+\) be the self-adjoint Fourier involution on the smallest
two-dimensional reflection-even boundary space. A doubled boundary state
\((x,y)\) belongs to its Lagrangian graph precisely when

\[
y-F_+x=0.
\]

This is a rank-two vector equation. A scalar zero can supply at most one
linear component of it.

The rank gap is exact:

\[
\operatorname{rank}(y-F_+x)=2,
\qquad
\operatorname{rank}(\ell(y-F_+x))=1.
\]

Therefore one linearly compressed scalar vanishing condition does not imply
Fourier-graph incidence. In the smallest even model, exactly one additional
independent linear comparison channel is required.

This statement does not apply to a genuine determinant section. A determinant
is scalar but nonlinear, and its vanishing can encode failure of
transversality of the complete graph relation. Thus the result separates two
possible typings of the completed theta value rather than proving that an
extra observer is unavoidable.

## Concrete witness

Choose a boundary packet whose Fourier-graph defect has two components
\((0,1)\). Its first scalar readout vanishes, but the packet does not belong
to the graph. This preserves the visible zero while violating the boundary
condition needed by the forbidden-nonreal-incidence theorem.

## Relation to the source currents

The earlier continuous-cocycle result now fits exactly. At a scalar zero, the
primitive and square prime currents may become summable, but summability is
only the first boundary coordinate. Star-compatible extension of the
continuous seam cocycle supplies an additional relation. Without it, an
off-seam hostile zero occupies the unresolved graph-defect channel.

If the theta value is only a linear boundary readout, the extra channel must
not be chosen after seeing the desired graph. It must arise from a named
source operation. Current candidates are:

- the centered moving-seam cocycle;
- a flux observer paired with the value observer; or
- the mixed primitive–archimedean Green current.

The prime-seam samples alone cannot supply it: previous work proved that no
universal prime-power quadrature reconstructs the continuous moving seam.

## New proof contract

A linear zero-to-state bridge sufficient for the Lagrangian argument must
produce a rank-two boundary packet

\[
(\mathcal O_{\mathrm{value}},\mathcal O_{\mathrm{flux}})
\]

whose simultaneous vanishing is equivalent to membership in the normalized
even Fourier graph. Alternatively, a source-derived relative determinant may
encode the two-row rank loss in one nonlinear scalar. The next audit must
decide which type \(\xi\) actually has in the proposed boundary construction.

## Falsifier

At any finite source cutoff, compute the two rows of the Fourier-graph defect.
If the proposed source observers span only one row, the bridge is incomplete.
If they span both rows but the second vanishing was obtained by differentiating
or dividing an already assumed scalar zero without a source identity, the
bridge is circular.

## Scope

The rank gap is exact for linear scalar compression in the smallest
reflection-even Fourier model. It does not obstruct a determinant section.
The typing of the completed theta value as a linear observer or a genuine
relative determinant remains open.

## Verification

The checker computes the exact graph-constraint rank, scalar-readout rank,
and a boundary witness with zero scalar readout but nonzero graph defect.
