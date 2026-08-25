# The toric QND instrument is not yet a source-closed constructor

Owner: `marici.Nima`

Status: exact audit of the prediction frozen in
`toric-constructor-sufficiency-prediction.md` against the withheld Kitaev
packets.

## Result

Four parts of the predicted measurement diagram are present:

- the marked controlled-string gate word derives the parity interaction;
- the pointer has two exclusive classical records;
- conditioning gives the Lüders successors `Pi_s rho Pi_s`;
- `Pi_s Pi_t = delta_st Pi_s`, so ideal branch repetition is exact, and
  summing the two branches gives the nonselective Lüders channel.

The fifth part is absent.  The apparatus qubit **is assumed prepared** in
`|0>`, but no admitted source map returns the measured apparatus to `|0>` or
derives an unlimited fresh supply.  The source packet itself leaves verified
cat preparation and fault propagation open.  Fresh replacement is therefore
an imported resource, not a proved return arrow.

Consequently

```text
source-derived repeatable QND instrument       yes
source-closed reusable measurement constructor no
fault-tolerant recovery constructor             no
```

This falsifies the frozen positive prediction at one of its declared
falsifiers: `missing_reset_authority`.  It does not weaken the QND instrument
theorem.

## Why the distinction matters

Idempotence of the data update is not reusability of the apparatus.  The
first says that a selected eigenstate remains selected.  The second requires
a physical successor for the record-bearing ancilla.  Treating preparation
as automatically renewable would silently turn an input boundary condition
into a constructor.

The corrected sufficiency criterion is therefore not merely a commuting
five-face diagram.  Every face must be source-generated, including the
resource-return face.  A repeatable instrument becomes a constructor only
after its apparatus return/replacement is included in the same authority
closure.

## Fault-tolerance boundary

The existing single-fault audit is deliberately narrower: it excludes
preparation faults, two-qubit gate faults, general measurement faults,
multiple faults, and verified cat preparation.  It proves useful bounded
propagation facts, but cannot fill the missing return face or derive a
recovery policy.  A recovery constructor additionally needs a source noise
model, decoder/cost functional, conditional correction, and a reusable
apparatus theorem.

## Falsifier for the corrected claim

The negative constructor verdict is overturned by an admitted circuit that:

1. prepares or resets the pointer from declared source resources;
2. composes that return with extraction without changing the Lüders task;
3. bounds degradation under the declared fault model; and
4. repeats for an unbounded number of task cycles without importing fresh
   low-entropy apparatus states.

The exact checker records the algebraic faces and the missing authority in
`results/toric_source_closed_constructor.json`.
