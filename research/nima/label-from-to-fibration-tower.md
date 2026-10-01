# Label/from/to fibration as a tower generator

## Operator rule

Each rung takes the previous rung's record type and fibers it over the next
field: label -> from-label -> to-label -> repeat.

The existing kernel is `agda/TableFibrationCycle.agda`, documented in
[table-fibration.md](table-fibration.md). It supplies homotopy fibers, dependent
totals, selected-column provenance, and field-preserving reconstruction. Its
previous four-step endpoint-transposition cycle is a different schedule.

## Explicit retained-total realization

Let a table have row type E, maps ell:E->L, s:E->A, t:E->B, and selector k.
Write p_k for the selected map and X_k for its target. Define

\[
F_k(E)(x)=\sum_{e:E}(p_k(e)=x),\qquad
T_k(E)=\sum_{x:X_k}F_k(E)(x).
\]

A successor row retains the outer key, the previous row, and its membership
path. For the next step, the three field maps are pulled back along the
projection to the previous row. The selected field may equivalently be read
from its outer key, with equality supplied by that path. Retain the selector
in the construction history.

This is one explicit interpretation of 'the previous record type': the next
input is the total type of the preceding family. It reuses the proved kernel
without introducing a new endpoint-promotion operation.

Set E12=E and k_n=(label,from,to)_(n mod 3). Then

\[
E_{11-n}=T_{k_n}(E_{12-n}),\qquad 0\le n\le7.
\]

## Nine presentations

The gauge names are the operator's proposed correspondence. The type column
is the mechanically expanded retained-total recurrence above.

| Rung | Gauge assignment | Current record type | Field used to reach it |
|---:|---|---|---|
| 12 | U(1) | E12=E | initial presentation |
| 11 | SU(2) | E11=T_label(E12) | label |
| 10 | SU(3) | E10=T_from(E11) | from |
| 9 | U(1)^2 | E9=T_to(E10) | to |
| 8 | SU(2)^2 | E8=T_label(E9) | label |
| 7 | SU(3)^2 | E7=T_from(E8) | from |
| 6 | U(1)^4 | E6=T_to(E7) | to |
| 5 | SU(2)^4 | E5=T_label(E6) | label |
| 4 | SU(3)^4 | E4=T_from(E5) | from |

Expanded, the first two successors are

\[
E_{11}=\sum_{l:L}\sum_{e:E}(\ell(e)=l),
\]

\[
E_{10}=\sum_{a:A}\sum_{u:E_{11}}(s(\operatorname{row}(u))=a).
\]

The next is

\[
E_9=\sum_{b:B}\sum_{v:E_{10}}(t(\operatorname{row}^2(v))=b).
\]

These formulas preserve all previous records. The same substitution generates
all lower entries. Nine presentations contain eight transitions; a ninth
transition would complete the third label/from/to cycle and produce E3. To
regard rungs12..4 themselves as nine operations requires a separate input
presentation before rung12. The phase convention must be explicit.

## What the kernel establishes

For every selected field, T_k(E) is equivalent to E, preserving the table
fields. Therefore the three-step composite also reconstructs the original
table data, while retaining a longer construction history. This is a consequence
of the existing generic recovery theorem; no new Agda theorem was compiled in
this experiment.

Finite set checks cover all 147 endpoint-unique tables with field carrier sizes
zero through two and all eight transitions: 1176 steps. Empty fibers, row labels,
selected keys, and complete nested rows are retained. Every step reconstructs
its input and the original table.

## Dependent products and endpoint promotion

A section type exists for each family:

\[
S_k(E)=\prod_{x:X_k}F_k(E)(x).
\]

The fibration-constructor dictionary identifies this with a dependent product
of an equivalent original family. It does not identify S_k(E) with E or T_k(E).
A two-row table can have an empty source fiber and hence no sections.

The intended endpoint schematic

    L_a -> L_b
    L_a -> Pi_ba
    Pi_ab -> Pi_ba

must therefore specify how these section types become endpoint fields of the
next table. The current retained-total realization produces dependent families
and a reversible history, but does not on its own implement that endpoint
promotion. Its row cardinality remains unchanged; the 1,2,4 multiplicity is
not a derived row-count result. Multiplicity might concern nested endpoint
structure instead, requiring that structure to be defined and counted.

## Scope relative to earlier tower work

This is a presentation/fibration tower. The earlier Gram restriction tower
removes state directions. Relating these constructions requires a map explaining
which presentation data become live state and which become records. No rank
loss, gauge group, physical clock, or energy normalization follows from the
field-fibration recurrence alone.

## Verification

    python research/nima/checkers/check_label_from_to_fibration_tower.py

The new checker is a finite regression against the existing generic kernel.
It does not substitute for its HoTT proofs or claim a gauge identification.
