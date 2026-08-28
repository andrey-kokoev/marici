# Moving-seam growth forces state-valued boundary incidence

## Correction of type

For every fixed length \(L\), integration over the seam is a continuous
scalar functional. Its norm grows like \(\sqrt L\), so those scalar
functionals do not form a uniformly bounded moving-seam family.

That does not mean seam completion fails. It means the moving seam was given
the wrong codomain.

## The source-derived seam is a state

For \(f\in H^1(0,\infty)\), define

\[
C_Lf=(T_Lf,R_Lf)
     =\bigl(f(L+\cdot),f|_{[0,L]}\bigr).
\]

The codomain depends on the cut:

\[
C_L:H^1(0,\infty)
\longrightarrow
H^1(0,\infty)\oplus H^1(0,L).
\]

Splitting the two integrals at \(L\) gives the exact identity

\[
\lVert C_Lf\rVert^2
=\lVert T_Lf\rVert_{H^1}^2
 +\lVert R_Lf\rVert_{H^1(0,L)}^2
=\lVert f\rVert_{H^1}^2.
\]

The image is constrained by the interface trace

\[
(R_Lf)(L)=(T_Lf)(0).
\]

Thus the complete cut has norm one for every \(L\). Completion stability is
carried by a state-valued correspondence, not by a uniformly bounded family
of scalar seam integrals.

## Directed seam system

If \(0<L<M\), the interval state on \([0,M]\) is obtained from the state on
\([0,L]\) by adjoining the shell \([L,M]\). The shell inclusions are
isometries with orthogonal increments. Consequently the expanding seam spaces
form a directed system whose completion is \(H^1(0,\infty)\).

This distinguishes three operations:

1. restriction produces the seam state;
2. refinement adjoins a new interval shell;
3. a readout subsequently pairs the seam state with a dual vector.

Only the third operation is scalar. A readout family must separately prove
uniform dual control. Scalarization cannot be moved before seam completion.

## Categorical form

The moving-seam constructor is not a natural transformation into one scalar
object. It is a section of a varying boundary-state fibration over the cutoff
poset. Refinement maps carry the section forward, and the tail component
supplies the complementary state needed for exact conservation.

Forgetting the boundary fiber and retaining only its integral is a quotient.
The growing scalar norm measures the information lost by trying to make that
quotient commute with the directed limit.

## Consequence for arithmetic incidence

Smooth prime synthesis may be followed by \(C_L\) without a completion
loss. Prime-labelled cuts then select objects in the directed seam system.
This resolves the topology of the moving seam itself.

It does not yet construct:

- a uniformly controlled scalar readout on the completed seam;
- primitive or prime-square incidence;
- the archimedean comparison row;
- the zero-state-to-boundary-flux bridge.

Those are downstream constructors and must not be inferred from the seam
isometry.

## DPC verdict

The scalar moving-seam family fails uniform descent.

The state-valued tail–seam cut passes uniformly and exactly.

The smallest hostile is a constant unit vector on a growing interval: its
state norm remains one while its unnormalized scalar integral grows like
\(\sqrt L\).

## Verification

The checker `check_state_valued_moving_seam_incidence.py` verifies exact
tail–seam energy splitting, refinement by orthogonal shells, and divergence
of the scalarized moving-seam readout.
