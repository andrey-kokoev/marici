# Fibrate a table along a coordinate

## Checked kernel

`agda/TableFibrationCycle.agda` implements the proposed operator for a table
with row labels, from-labels and to-labels. The generic operation is

\[
\operatorname{fibrate}(p:E\to B)(b)
=\sum_{e:E}(p(e)=b).
\]

Taking the dependent sum of those fibers recovers the row type:

\[
\sum_{b:B}\operatorname{fibrate}(p)(b)\simeq E.
\]

The equivalence forgets the outer key and membership witness; its inverse sends
an original row e to its selected coordinate p(e), the row itself, and reflexivity.
Both inverse laws are checked. The construction retains the full homotopy fiber,
not merely a Boolean assertion of membership.

Active SCC obligations: forward realization, route/coherencer compatibility,
and readout descent. Model: `nima-table-fibration`.

## Three coordinates, with a recoverable selector

A table consists of a row type E and three maps

\[
\ell:E\to L,\qquad s:E\to S,\qquad t:E\to T.
\]

The column selector has three constructors: label, from and to. Fibration at
any selected column gives its family of groups; each group retains the other
two fields. The implementation proves a row equivalence preserving all three
fields for each of the three reconstruction procedures.

The robust API retains the selector:

\[
\operatorname{markedFibrate}(Q,k)
=(k,\operatorname{fibrateTable}(Q,k)).
\]

Univalence and the field-preserving row equivalence give

\[
\operatorname{restore}(\operatorname{markedFibrate}(Q,k))=Q.
\]

The formal family includes empty fibers. A finite display may omit empty groups
if omission denotes the empty fiber; the proof does not require a procedure
that decides inhabitation for arbitrary types.

## Why the selector, or equivalent provenance, matters

Let Q have the single row

\[
(0,0,1).
\]

Grouping Q by from-label gives the same nested data as grouping its transpose,
whose row is

\[
(0,1,0),
\]

by to-label. Both give outer key 0 and enclosed pair (0,1).

The module proves definitional equality of these grouped records and proves
that their source tables are not equivalent with endpoints preserved. It follows
that no function of the unmarked grouped data alone can recover both originals.
This obstruction holds even with the required uniqueness of endpoint pairs.

Retaining the column marker solves that ambiguity. Knowing the selector through
the calling context or retaining equivalent source information also suffices;
there is no claim that a separate marker is needed when this information is
already available.

## The four-step cycle

Two unpacking conventions use the same dependent sum of fibers:

- ordinary unpacking puts the outer key back in the from position;
- reversed unpacking puts the enclosed endpoint in the from position and the
  outer key in the to position.

Define two steps as grouping by from, then reversed unpacking. The computed
row representation is equivalent to endpoint transposition, with labels and
endpoints tracked explicitly. Repeating those two steps returns the data:

\[
[L,S,T]
\longrightarrow[S[L,T]]
\longrightarrow[L,T,S]
\longrightarrow[T[L,S]]
\longrightarrow[L,S,T].
\]

The checked `four-correct` theorem constructs the field-preserving row
isomorphism. `four-path` uses univalence to prove

\[
\operatorname{four}(Q)=Q.
\]

This is equality of table data. It does not equate a complete retained
four-operation derivation with its starting construction, nor claim a minimal
period of four for every table.

## What was derived, and what remains specified

The construction uses the dependent sum and identity types already present in
the definition of a homotopy fiber. Canonical unpacking is proved using their
eliminators; no independent invertibility axiom is added.

Endpoint transposition need not be an additional primitive in the executable
two-step construction: it is realized by assigning the two recovered endpoints
to the opposite fields. That wiring convention remains a choice. Ordinary
unpacking also satisfies the fiber recovery law and returns the table after
two steps. An explicit asymmetric table distinguishes the two conventions.

Thus the result is a reversible fibration/total construction in HoTT, with
coordinate and wiring information retained or known. It is not a theorem that
fibration alone selects the wiring convention, supplies HoTT's type formers,
or generates every original Q rule.

These two endpoint groupings are fiberings of the same labelled span. They are
not automatically identified with the earlier dependent-sum and dependent-product
constructor rules.

## Endpoint uniqueness and verification

The row equivalences preserve the condition that two rows with equal from and
to endpoints are equal. This is the user's endpoint-pair uniqueness requirement
for ordinary set-valued tables. The generic row recovery theorem itself does
not require that restriction. Row labels are not assumed unique.

Fresh safe/cubical compilation passed through the shell runner
`checkers/check_table_fibration.ps1`. Two intended failures are checked:
claiming endpoint exchange preserves an asymmetric table, and assigning an
arbitrary Boolean row to the false fiber without a membership path.

`checkers/check_table_fibration.py` enumerates all 147 endpoint-unique unordered
tables whose three label carriers have cardinalities zero through two. It checks
441 marked coordinate roundtrips and the two/four-step equations. Further controls
reject loss of the column selector, erased row labels, incorrect membership,
and deduplication by a row label that need not be unique.

Receipts:

- `results/agda-TableFibrationCycle.json`
- `results/table-fibration-formal-audit.json`
- `results/table-fibration.json`

The four-step path and the unmarked-recovery obstruction are quantified formal
proofs. Finite controls do not substitute for those proofs. The model has no
row-order structure; ordered tables require their ordering information to be
retained separately.
