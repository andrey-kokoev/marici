# The Global Coherence Constructor Is the Simplicial Braid Object

## From separate ports to one graded object

The pure braid groups assemble into the simplicial group

\[
AP_n=P_{n+1}.
\]

Its face maps delete strands. Its degeneracy maps double strands. Therefore
the arity-indexed deletion systems are not unrelated observation packets;
they are the faces of one graded constructor.

## Cycles, fillings, and residues

The Brunnian subgroup is the simultaneous deletion kernel

\[
\operatorname{Brun}_n(S^2)=\bigcap_i\ker(d_i).
\]

These are cycle-like classes: every face is trivial. But a Brunnian class is
not automatically an irreducible residue. Some such cycles are supplied by
higher fillings and belong to an explicitly generated symmetric-commutator
subgroup.

For \(n>4\), the sphere-braid theorem gives an exact sequence whose terminal
quotient is

\[
\pi_{n-1}(S^2).
\]

Thus the irreducible coherence datum at arity \(n\) is a homotopy class after
fillable Brunnian cycles have been quotiented out.

## Correct hierarchy

```text
all deletion faces trivial
        ↓
Brunnian cycle
        ↓ quotient by authorized fillings
homotopy residue in pi_(n-1)(S2)
```

This corrects the naive conclusion that every raw Brunnian element demands a
new primitive port. A port is required only for the quotient class that cannot
be supplied by the declared filling constructors.

## Prediction

The global constructor is not one scalar ubermonitor. It is the simplicial
braid object together with its realization/filling law. It predicts two
distinct failure types:

1. a cycle defect, where all proper faces agree but a Brunnian class remains;
2. a residue defect, where that class is not the boundary of an authorized
   higher filling.

The second is the genuine next-level obstruction.

Geometric realization supplies classification, not executable observation.
An instrument still requires a separate source-authorized map from the
homotopy residue into an accessible readout.

## Verification

```powershell
uv run python research/strominger/checkers/simplicial_braid_homotopy_residue_contract_checks.py
```

## Sources

F. R. Cohen and J. Wu construct the simplicial pure-braid group with deletion
faces and strand-doubling degeneracies and relate its realization to the loop
space of the two-sphere. Bardakov, Mikhailov, Vershinin, and Wu identify the
spherical Brunnian quotient carrying \(\pi_{n-1}(S^2)\).
