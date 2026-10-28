# Registered inventory-fibration attempt: candidate insufficient

## Net obligation and prior registration

This executes `pb208-inventory-fibration-attempt`, registered in net revision24
BEFORE the checker was run. The immutable specification is
`contracts/pb208-inventory-fibration-attempt.v1.json`; the pre-execution net is
`contracts/persistent-seam-pe-conjecture-net.snapshot.rev24.json`.
The parent obligation is `pb208-retained-native-construction`.

The criterion was not merely whether a fibration calculation succeeds. It was
whether the existing retained-total source supplies the missing cross-alternative
particle-inventory comparison without dropping a body or fitting a constant count.

## Source inspection

Nima's label/from/to recurrence retains complete rows and membership paths.
`TableFibrationCycle.agda` defines `TableIso` with explicit `preserves-label`,
`preserves-from` and `preserves-to` obligations. Its `restore-correct` and
`marked-recovery` reconstruct the SUPPLIED table. They do not construct a
species-preserving equivalence between two different occupied-body tables.
The Agda declarations were inspected, not freshly compiled here.

## Native finite instance

Rebuild the actual PN-to-NE and PN-to-NN alternatives using unchanged native laws.
For this test, each occupied primitive becomes a row whose label is the existing
species and whose identity endpoints are its canonical cell key. This is an
explicit table-encoding convention, not a new native arrow or inventory law.
The table count agrees with the existing native inspection on both alternatives.

Both alternatives occupy the same three primitive cells. Their supplied species
inventories are nevertheless different:1P/1N/1E versus1P/2N/0E.

Run eight label/from/to retained-total transitions separately on each table.
Every key, original row and inventory is recovered exactly at every stage.
All six possible bijections of the original three rows were then tested. NONE
preserves species; the unique geometry-preserving bijection does not either.
Since total recovery preserves species, a species-preserving equivalence between
the totals would compose with recovery to one between the original rows. The
finite obstruction therefore survives the wrappers.

Inverse coefficient recovery returns the same nonzero root vector from both
alternatives but different inventories remain. Coefficients alone do not determine
this occupied-body inventory. Freezing the seed/PN inventory would fail the
unchanged native composition reader, not solve the problem.

## Disposition against the registered criterion

**Candidate insufficient for the inventory bridge.** The recurrence succeeds at
its own recovery task, while preserving precisely the inventory difference that
needs explanation. It requires the missing cross-alternative carrier/inventory
identification rather than providing it. This is the registered failure branch,
not an implementation failure and not a refutation of the generic theorem.

No new particle inventory, Pb construction or universal no-go conclusion follows.
The result must not be presented as positive completion of the Pb obligation.
The next source to assess is the existing native retained-whole fixture: does its
independent whole/readout data actually bind this pair, or merely provide another
conditional construction once the assembly is supplied? Register that comparison
before executing it; do not infer its answer from the current test.

## Reproduce

```sh
python research/nima/checkers/check_label_from_to_fibration_tower.py
node research/strominger/checkers/check_pb208_inventory_fibration.mjs
```

The first command is the existing source finite regression, not a fresh Agda
proof. The second performs the registered native instance, retained membership
checks, six-bijection test and forbidden forgetting/constant-inventory controls.
Artifacts: `results/pb208-inventory-fibration/attempt.json` and `verification.json`.
