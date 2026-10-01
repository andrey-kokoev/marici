# Clarified rung transports and the fixed rung-4 reference

## Operator-confirmed diagram

The middle triple carries the aligned transports

    12 --9--> 6
     |       |
    11 --8--> 5
     |       |
    10 --7--> 4.

Within each outer triple, vertical maps change the retained presentation from
individual labelled records to source-indexed and then target-indexed records.
The physical reference is located at rung4. Rungs9,8,7 are therefore transport
roles in this diagram, rather than independent local-reference choices.

Write L1,L2 for the left vertical maps, R1,R2 for the right ones. The required
coherence equations are

    T8 L1 = R1 T9,
    T7 L2 = R2 T8.

They imply equality of the two complete routes to rung4:

    R2 R1 T9 = T7 L2 L1.

For a specified rung4 observation J4, the corresponding source observation is
J4 composed with either route. This uses forward transport to the reference
locus; no inverse of a possibly many-to-one transport is assumed.

## Executable presentation-level realization

The checker builds the actual137 slot values from the shared-leg matrix model.
Vertical changes index the full retained records and reconstruct them exactly.
A declared horizontal candidate performs two incoming-family promotions,
retaining intermediate families as transport provenance.

For a chosen T9, its source/target presentations are defined by transport through
the retained reindexing maps. Both squares and both complete routes commute
exactly. All137 leaves and their original masses reconstruct at the target.
An altered middle transport is detected by the square and by its rung4 readout.

This is a presentation-level realization of the clarified interface. It does not
yet identify a physically selected horizontal generator. In particular, T8 and
T7 here are transported presentations of T9, rather than independently derived
dynamical laws whose agreement would establish additional physics.

## The reference is fixed; local offsets must travel

The prototype places a fixed matrix reference d4 at the specified rung4 locus.
Its test value2I is supplied, not derived from the rung designation. With C the
transported weighted response, a local comparison standard d_local satisfies

    C-d4 = (C-d_local) + (d_local-d4).

Choosing d_local=C makes the local residual zero, while its retained offset to
d4 remains C-d4. The checker verifies this for both complete diagram routes.
Thus the earlier reanchoring result does not permit replacing or removing the
physical rung4 reference.

The next physical task is to realize the rung4 reference value and observation
metric and transport their meaning through this diagram. Their location is
specified; their numerical normalization is not supplied by the location alone.

## What the squares do and do not determine

Two explicit endpoint policies satisfy every presentation/reconstruction check:

    inherited-key promotion: 137 ->32 ->32,
    common-target promotion: 137 ->32 ->1.

Their target record types differ, while their transported weighted mean gives the
same rung4-relative matrix residual. Coherence under retained presentation
changes therefore does not choose between these horizontal generators.

Replacing member-mass weights by equal weights on fresh labels changes the
readout in the tested inherited-key model. The negative control detects that
change. Counts, retained data and observation measures must stay distinct.

The remaining generator problem is now situated correctly: construct the actual
T9 transport from rung12 to rung6, with T8 and T7 its coherent presentations and
a specified observation at rung4. Any mixed-defect or higher-witness construction
must be connected to these maps, rather than substituted for the diagram.

## Verification

    python research/nima/checkers/check_rung_transport_diagram.py

Exact rational tests of both squares, both full routes, retained reconstruction,
member masses, fixed-reference offsets, wrong-weight and corrupted-transport
controls, and two different coherent horizontal candidate policies.
