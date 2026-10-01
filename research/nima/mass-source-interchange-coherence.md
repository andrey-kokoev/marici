# Source interchange cells preserve genuine traversal cycles

## Typed obligation

Route/coherence compatibility before a particle-energy readout. The prior path
checker is freshly rerun. This test fills only squares justified by operations
on independent registers, and includes the corresponding product cubes. It does
not declare every loop with equal active endpoints to be an identity history.

The allowed cells are:

- an outer path operation interchanged with an inner path/readout operation;
- left and right inner path appends interchanged;
- cubes expressing interchange among outer, left and right operations.

These commute on per-role retained histories. A readout must retain its parent
record; outer interchange does not manufacture an inverse readout. If a global
chronological tape is used, the independent records are compared by the explicit
record permutation, not erased. No claim about commuting physical Hamiltonians
with unspecified interactions follows from this typed construction.

## First reproduce the active-port projection

The previous finite graph merged opposite operations into one undirected edge.
Its outer graph L has12 vertices and30 edges, with first Betti number19. The
inner complex D begins with L x L, then adds nine state vertices and162 endpoint
readout edges. Its Betti numbers are (1,191,361).

The full product L x D has:

| Dimension | Cell count |
|---|---:|
|0|1836|
|1|15174|
|2|37260|
|3|27000|

The square-boundary rank over F2 is13129, checked by exact bit elimination.
The first Betti number falls from13339 to210. Integral product homology is free,
with Betti numbers (1,210,3990,6859). The higher numbers use the cellular product
and Kunneth formula; the checker does not claim a full integer Smith reduction
of the cubic boundary matrix.

A cochain supported on one outer edge, copied across every inner label, vanishes
on all square boundaries but pairs to1 with a particular outer triangle. This
is an integer witness that this cycle remains, not just a mod-two rank artifact.

## Repair the loss of returning-operation identity

For retained histories, the append from active arrow(0,1) to(1,0) and the append
back to(0,1) are DIFFERENT operations. They both consume positive traversal
resource. The second is not the inverse of the first: an actual inverse would
undo the retained append rather than append another edge.

Consequently the operation-resolved graph must keep two distinct1-cells here.
Its outer graph has36 edges, not30. Resolving those operations throughout gives:

| Dimension | Operation-resolved cell count |
|---|---:|
|0|1836|
|1|17820|
|2|52488|
|3|46656|

All52488 square boundaries close exactly. Their F2 rank is15757. Integral
product Betti numbers are now

    (1,228,5700,15625).

For this calculation b1(L)=25; b1(D)=2*25+162-9=203 and b2(D)=25^2=625.
These yield the displayed product homology and Euler identity. The distinction
between a generator and its formal inverse is preserved in these1-cells.
This still is a finite presentation of operations, not an enumeration of the
infinite state space containing every complete history record.

The two-step returning append loop pairs to2 with the cochain assigning one
unit to every forward outer append. That cochain vanishes on all admitted
interchange faces. Thus an additive traversal-resource pairing survives these
coherences. It does not single out1836: short genuine loops already carry
nonzero resource, and the physical conversion from traversal resource to a
particle rest-energy bound remains absent.

## What is not filled

Within one retained path, reassociating a word does not delete its letters.
Returning to the same active-arrow label is not a supplied null-homotopy.
Similarly, a source/target readout is not a reversible identification of an
arrow with its endpoint. Filling cycles using either assertion would add new
laws or lose history, not apply known coherence.

Higher cells cannot change H1 unless additional2-cell boundaries are admitted.
The228 residual first-homology directions are therefore a concrete gate for
any proposed additional reference-return or readout law. Their existence alone
is not an error: real retained histories can have nontrivial loops.

The full graded complex has many even and odd zero modes, not the auxiliary
index+1 spectrum used in the earlier energy-protection trial. No particular
central-charge functional or sector-dependent particle index has been selected.

## Verification and frontier

    python research/nima/checkers/check_mass_source_interchange_cells.py
    python research/aspect/scc/scc.py check nima-mass-source-interchange-cells

Exact checks cover both square-boundary ranks, signed boundary closure, retained
append interchange, surviving integer cocycles and product Euler identities.
Report: `results/mass-source-interchange-cells.json`.

Progress: source-typed higher cells are now explicit, and the active-port graph's
merging of returning operations has been corrected in the stronger model.
Remaining: a source-authorized law involving actual reference returns/readouts,
and an independently defined physical energy pairing. Arbitrary loop fillings
or weights chosen to recover1836 would not constitute that law.
