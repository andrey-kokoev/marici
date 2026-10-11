# Native composition successor and its actual rung-reader boundary

## Native derivation constructed

`agda/NativeTriangleCompositionSuccessor.agda` uses the actual Vertex and
Out types from `SeedAttachedObserver`. A joined word contains both actual
edges and a proof that the first target equals the second source. The
constructor enumerates only those typed joins and retains both operands.

The exact two component lists produce:

    LR targets = [A,D],
    RL targets = [B,C].

These are freshly checked definitional equalities, not a table seeded as
the desired result. The native application EXTENSION executes the supplied
composition function and endpoint reader. Its only admission inputs are
the operand pair, operation and reader; the composed object and promoted
derivation are produced by rule application and remain recoverable.

This does not claim the frozen native calculus or physical source selects
those functions. It makes their admission and application explicit.

## Reuse the actual rung machinery

The exact checker imports the existing `check_rung_transport_diagram.py`,
rerunning its original 137-row assertions. For this new input, each role's
indicator is displayed on the same ten-word source comparison frame, as
count times the old 2x2 identity matrix with unit row mass. This adapter is
explicit and is NOT an identification with the old shared-leg 137-row input.

The zero entries are unused coordinates of a declared full comparison frame,
not executed zero events or assigned responses to unavailable experiments.

Both inherited-key and common-target two-stage promotions are reused, as
are both indexed paths through the confirmed diagram. They retain all leaf
words and operand-role labels. The old reference is left at `d4=2I`.

## Information survives, but the unchanged aggregate does not see it

Each cross product has two unit coefficients in the ten-word frame. Thus
both have mean I/5, and the unchanged fixed-reference reader gives

    J4(LR)=J4(RL)=I/5-2I=-9I/5.

It is blind to the role contrast. We do not alter normalization or move the
reference to manufacture a difference.

A declared leaf-target reader DOES recover, under BOTH policies,

    LR: (1,0,0,1),
    RL: (0,1,1,0).

The source contrast remains available in the retained rung-4 object even
when one policy exposes only a single outer family. Retaining information
and having an authorized physical observer of it are distinct obligations.

## What is now closed

- An actual typed, source-retaining composition successor under the declared
  native application extension.
- Exact source-target readings for both component orders.
- A conditional row adapter into the existing rung transport implementation.
- Both route equalities and lossless recovery with the original reference.
- An explicit observation result: endpoint detail survives; the existing
  aggregate cannot distinguish the two channels.

The Python row transport is independently checked; it is not extracted from
the Agda successor theorem or claimed as a formal native equivalence with
the 137-row fixture.

## Remaining physical gate

Determine whether the intended rung-4 physical observer reads the retained
endpoint/role profile or only the existing aggregate response. Under the
current adapter the latter gives no contrast. Adding the finer profile is
a defensible mathematical observer, but calling it position, momentum or
charge requires a separately justified physical readout, not another
retention theorem.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NativeTriangleCompositionSuccessor -Fresh
    python research/nima/checkers/check_triangle_successor_rung_reader.py

Fresh safe Cubical checking passes with ignored interfaces and stable inputs.
26 new exact rung-reader checks pass; the previous actual-component and
original rung/DG checks rerun. Receipts:
`results/agda-NativeTriangleCompositionSuccessor.json` and
`results/triangle-successor-rung-reader.json`.
