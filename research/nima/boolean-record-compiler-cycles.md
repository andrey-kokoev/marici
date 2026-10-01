# Consecutive native compiler cycles from Bool x Bool

## Instantiation

`agda/BooleanRecordCycleRegression.agda` directly imports and uses:

- `TableFibrationCycle.agda`: `twice`, `four`, and their row equivalences;
- `NativeNormalizationRouteCompiler.agda`: `retain-compilation`, native
  comparison nodes, canonical-leaf certificates, execution, and `next-Q`.

The initial table has four rows `(false,false)`, `(false,true)`, `(true,false)`,
`(true,true)`. Its `from` column is the first coordinate, its `to` column is the
second, and its label is unit. These are the four rows of a Boolean relation
between two Boolean endpoint spaces. They are not the twelve nonidentity arrows
of the complete directed graph on four vertices.

We explicitly supply the existing table cycle:

1. Group by `from`.
2. Unpack with reversed endpoint wiring (`twice`).
3. Group by the new `from` (the previous `to`).
4. Unpack with reversed endpoint wiring again (`four`).

`twice-correct` supplies each compound row equivalence. The native route therefore
has two comparison slots. The compiler neither selects this route itself nor
adds a complete graph of pairwise relations.

For the first cycle the presentations are:

| Stage | Presentation of row `(a,b)` | Reachable rows / members |
|---|---|---:|
| Input | `(a,b)` | 4 |
| First grouping | outer `a`, fiber retaining `(a,b)` and its boundary witness | 2 fibers of 2 |
| Reversed unpack | endpoints `(b,a)`, original row retained inside | 4 |
| Second grouping | outer `b`, fiber retaining the first grouped row | 2 fibers of 2 |
| Second reversed unpack | endpoints `(a,b)`, both grouping witnesses retained | 4 |
| Native retention | route, input, output, native history, boundary certificates | 4 reachable packages |

`four-correct` recovers every original row exactly. The regression proves this
for the compiler's executed route, not only for a separately defined simulator.

## Feeding the actual retained value forward

The next table's row type is the preceding compiler's `Retained` type. Its
endpoint columns are the original endpoints recovered through the retained
source's faithful coordinates. Lifted endpoint types account for the universe
increase. The row value remains the full retained record; the endpoint decoder
only supplies grouping keys.

Each of the four previous outputs is fed to the next compiler instance. The
regression checks that this value is exactly the payload of the existing
`next-Q` constructor, and that each later run's input is literally the preceding
record. Three successive compiler levels are instantiated.

The full `Retained` type admits other routes and inputs. Counts below refer to
the four explicitly generated trajectories, not a cardinality claim about that
type.

| Completed cycles | Reachable packages | Endpoint configurations | Comparison slots added per input this cycle | Comparison slots along each input ancestry | Retained compilation layers |
|---:|---:|---|---:|---:|---:|
| 0 | 4 | 00,01,10,11 | 0 | 0 | 0 |
| 1 | 4 | 00,01,10,11 | 2 | 2 | 1 |
| 2 | 4 | 00,01,10,11 | 2 | 4 | 2 |
| 3 | 4 | 00,01,10,11 | 2 | 6 | 3 |

There are eight new route comparison slots across the four trajectories per
cycle. Ancestral slot counts follow the retained input chain once; they are not
total syntax-tree sizes or memory-use estimates. Normalization certificates and
repeated references inside boundary packages are not counted as new route slots.

## Checked statements

- `two-comparison-slots`: the supplied route has exactly two native steps.
- `certified`: the existing compiler's canonical-leaf theorem applies.
- `recovery`: the cycle's executed output recovers its original row.
- `decode-run`: the retained input is recoverable.
- `run-injective`: distinct inputs give distinct retained packages.
- `original-retained`: the original Boolean pair is recoverable after three runs.
- `three-cycle-injective`: all four explicit trajectories remain distinct.
- `previous-record-is-input` and `second-record-is-input`: history is actually
  fed forward rather than reset to a fresh Boolean seed.

## Scope of the outcome

The existing fibration cycle preserves the four-row population while increasing
retained provenance depth. This supplies a concrete replacement for the earlier
invented recurrence `4 -> 12 -> 132`. It does not identify the compiler's
four-operation cycle with all nine rungs of the proposed physical tower.

Producing twelve new records requires an additional constructor that forms the
twelve directed nonidentity relationships and promotes them to records. That
constructor is absent from the chosen route. Likewise, no proton/quark identity,
102-entry fiber, mass assignment or spin readout is inferred by this regression.

The inherited compiler also admits canonical boundary seeds; the proof certifies
the route and retained ancestry, not generation of every boundary from a sole
initial physical seed. This is the source restriction already documented in
`native-normalization-route-compiler.md`.

## Fresh verification

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module BooleanRecordCycleRegression -Fresh
```

Passed with `--safe --cubical --guardedness`, rebuilding dependencies with
`--ignore-interfaces`.

- Source: `agda/BooleanRecordCycleRegression.agda`
- Receipt: `results/agda-BooleanRecordCycleRegression.json`
- Log: `results/agda-BooleanRecordCycleRegression.log`
