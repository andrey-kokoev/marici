# Independent recursive constructor tables: E/P stage

## Status

Full follow-up: [native-table-equivalence.md](native-table-equivalence.md)
now establishes the typed recursive table equivalence for all eight code forms,
all twelve independently implemented native rules, and actual retained closures
for arbitrary original seed families. This report records the earlier E/P stage.

This advances the representation work beyond the annotated interpretation in
`fibration-constructor-equivalence.md`. The new stored datatypes do not contain
an opaque original Code, Complete, Rule or Resolve field. Their operations are
defined independently, before the legacy decoder.

The checked coverage is precise:

- an independent codec and value interpreter for the original atom/E/P code
  fragment;
- an independent retained E/P runtime, equivalent to the actual original
  Resolve closure restricted to supplied seeds and E/P applications;
- an independently constructed NAND table, with constructor and operation
  compatibility proved by `refl`.

This E/P-stage module alone is not the full eight-constructor/twelve-rule
equivalence. Its five general code forms and ten other rule implementations
are supplied by the full follow-up. Reconstructing retain wrappers for E/P
inputs in this earlier module does not implement the general retain constructor.

Active SCC obligations: forward realization, attachment transport,
route/coherencer compatibility, and readout descent.
Model: `nima-recursive-constructor-tables`.

## What the three columns contain

Each canonical node table has a declaration row and indexed child rows:

| label | from | to |
|---|---|---|
| constructor kind and its supplied type/index domain | root | declaration port |
| recursive child table | root | child port i |

There is a declaration row even when there are no child ports. Atom declarations
carry the supplied atomic type; E/P declarations carry their active index domain.
The format therefore distinguishes a product with no indices from a product
with an existing index whose fiber is empty.

`RecursiveConstructorTables.agda` defines this intrinsic, well-typed, canonical
recursive table format. It is a well-founded construction with potentially
infinite supplied index types, matching the original constructor scope. Atomic
types and values remain supplied parameters, as in the original signature.
It is not a finite string serialization of arbitrary types or functions.

The three-column field view is an actual `TableFibrationCycle.Table` instance.
The existing kernel was generalized uniformly over universe levels to admit
these large typed labels. Its row, label and endpoint operations are unchanged.
Endpoint uniqueness and four-step table-data recovery are proved for the new
instances. This data recovery does not identify retained derivations.

The generic kernel contains more tables than this typed schema. No equivalence
of every unrestricted raw table with an old constructor expression is claimed.
The finite executable parser checks the schema; the Agda implementation uses
intrinsically typed canonical nodes.

## Syntax and values

A recursively defined `Supported` predicate selects exactly atom, E and Pi from
the unchanged `WholePackageSigmaPi.Code`. The predicate is proved propositional.
The codec establishes

\[
\sum_{c:\operatorname{Code}}\operatorname{Supported}(c)
\simeq
\operatorname{Graph}.
\]

Both syntax roundtrips are proved. The graph value interpreter reads the new
constructor declaration and child tables directly: E gives total values, and P
gives sections. It does not call the old decoder or interpreter.

A separate theorem identifies its value type with the original interpretation
of the decoded code. Together with the syntax equivalence, this gives the
corresponding equivalence of value packages for that fragment.

The fragment boundary is enforced in the formalization: a maps code is not
accepted by `Supported`, even if an atom of function type has the same values.

## Retained operations, not just output values

`RecursiveTableRuntime.agda` supplies independently defined literal, E-assembly
and P-assembly tables. A literal carries its native type table, selected value,
and an actual witness from the supplied family `Admit`.

An assembly retains every recursive input table. An E declaration additionally
retains its selected index. The native result is computed directly from those
inputs. The P result is the section selecting each input's value.

This distinction matters: two E computations can have the same output type and
selected value while differing in an unselected input. Their retained tables
and decoded old results remain different. Reading only the output package
would lose that information.

The legacy decoder reconstructs the actual old retain wrappers from input
tables and selected values. It does not retrieve a previously stored old Code.
The complete old E/P package boundary equations close by `refl`, including their
constructor metadata. The independent native value interpretation is also
proved equivalent to the decoded old value type, with selected-value
compatibility.

## Equivalence with the actual retained derivation type

The central runtime theorem is

\[
\sum_{q:\operatorname{Complete}}
\sum_{d:\operatorname{Resolve}(\operatorname{Seeds},q)}
\operatorname{OnlyEP}(d)
\simeq
\operatorname{Run}_{\operatorname{Admit}}.
\]

`Resolve` here is imported from the original `WholePackageResolution` module.
`OnlyEP` recursively restricts its applications to the two E/P schemas and is
proved propositional. Both inverse laws are checked. An intermediate restricted
syntax is explicitly related to the actual imported datatype; the theorem is
not only about a newly declared source copy.

`Seeds` carries the supplied native literal package and its actual `Admit`
witness. The theorem is parameterized over arbitrary such admission families,
not a hard-coded policy accepting all values. Admission witnesses need not be
propositions: two distinct supplied certificates for the same literal remain
distinct, although the output package is identical.

A regression also sets the admission family to empty. No literal seed can then
exist, while zero-arity P still constructs its result by the original Pi rule.
No target seed is introduced for that construction.

This is an equivalence of retained E/P derivations, not an assertion that
retained executions are determined by their output Complete package.

## Boolean construction

`RecursiveTableRegression.agda` builds pair and NAND tables using only the new
constructors and the independent native interpreter. It proves by `refl` that

- decoding the new NAND table gives the existing `nandCode`;
- its native operation is the existing NAND operation.

The full Wolfram word therefore satisfies the previously checked double-negation
theorem. It specializes to C under the same stable-proposition assumptions.
The unrestricted claim for arbitrary nonpropositional C remains excluded.

## Verification

Fresh safe/cubical closure compilation and three intended rejection controls
pass through `checkers/check_recursive_constructor_tables.ps1`.

The rejected claims are:

1. that maps codes already belong to the independent grammar;
2. that equal output packages identify different source certificates;
3. that the output type graph alone retains the old E input metadata.

The finite independent checker exercises unordered rows, 1,745 code roundtrips,
3,593 value instances, 227 retained runtime roundtrips, and 64 NAND/double-negation
cases. It rejects missing declarations, missing declared ports, duplicate
endpoints and absent literal certificates.

The existing table-fibration and annotated full-code bridge checks were also
rerun after the universe generalization; both pass.

Receipts:

- `results/agda-RecursiveTableRegression.json`
- `results/recursive-constructor-formal-audit.json`
- `results/recursive-constructor-tables.json`

## Remaining whole-system gate

The remaining codecs are paths, maps, equivalences, general retain, and
comparison. Their typed value and compatibility-witness attachments must be
represented explicitly and proved coherent. The ten remaining resolution
schemas also need independent table implementations and commuting diagrams.

The earlier full-code annotated equivalence remains available as a semantic
reference. It is not used to mark these missing independent implementations as
finished. No new physical realization or independently defined physical readout
compatibility is established here.
