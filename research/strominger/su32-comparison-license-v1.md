# Which comparison does the source geometry actually support?

## Question and correction

For the two concrete five-cell presentations below, what distinguishes an actual comparison action from a record that merely stores both histories?

A generic native comparison constructor **already exists**. The unresolved item is its Su-32 operand, reader and source-mode binding—not the absence of a comparison schema. `InternalSourceComparisons.agda` applies `compare-rule` to actual retained operand derivations. The generic rule requires a carrier equivalence and selected-value agreement; the source-aware `Body` interface additionally requires a whole-carrier reader law. It explicitly chooses target-side continuation and transports outgoing edges under the selected mode.

That implementation and the canonical synthesis theorem use a particular four-vertex source graph and typed fragment. They cannot be instantiated with Su-32 merely because a local diagram also has four occurrences. Their sources were inspected, not recompiled or modified here.

## One actual pair

The fixed reading is `reading:0:-1`. The two paths are

```
N:0,0,2,1 -> E:-1,0,1,0 -> N:0,1,1,1 -> P:0,1,1,0 -> N:1,1,1,0
N:0,0,2,1 -> E:-1,0,1,0 -> N:0,1,2,0 -> P:0,1,1,0 -> N:1,1,1,0
```

These are actual four-interface incidence presentations. They differ at the middle N occurrence. The complete source domain explicitly leaves their comparison map and filling witness unbound. They are not already native signal trajectories.

## A derived geometric candidate

Search all 24 coordinate permutations about the retained carrier centre. Exactly one maps the first entire path to the second:

\[
S(q_0,q_1,q_2,q_3)=(q_0,q_1,q_3+1,q_2-1).
\]

It fixes the four common cells, preserves P/N/E roles, is involutive, and transports all 104 oriented native interfaces of this reading. This uniqueness is within the searched coordinate-permutation class, not among all possible comparison operations.

The source-derived reference action exchanges P+ and P- and fixes E+ and E-. No payload is altered or discarded: whole input records, including their original identities and provenance, are carried to the exchanged slots.

## Selected-record test: symmetry is not fixed-preparation reconciliation

Let `r` be the original registry of four independently tagged records and `S*r` its slot-transported registry. The actual candidate channel constructors satisfy

\[
S\bigl(\operatorname{channel}_A(r)\bigr)
=\operatorname{channel}_B(S_*r),
\]

but the left side is **not** `channel_B(r)`.

The retained P+ input identity appears in the transported P- slot, whereas the right witness at the original preparation contains the original P- input identity. The E reference and geometric endpoint agree in both cases. This is an explicit record-reader separation, not a failure inferred from counts.

Alternatively, transporting the sign binding from `[0,0]` to `[1,0]` preserves the record labels while moving their reference occurrences. That result is again different from the target specified with both the original registry and original binding.

Therefore this geometry-induced equivalence cannot simply be used as a pointed comparison between the two selected channel witnesses at the original frozen preparation. Any full-history comparison extending this particular channel action would inherit the mismatch. This does not exclude another contextual comparison, nor identify slot transport with a physical change of state.

## Continuation test: a fixed terminal cell is insufficient

There are four outgoing incidence edges at the common terminal N. Two are fixed by S and two are exchanged. For every one, the checker verifies

\[
S(A;e)=B;S(e).
\]

For an exchanged edge, `B;e` is a different retained path from `B;S(e)`. Thus leaving the outgoing edge unchanged is not the correct continuation of this geometric source mode, despite its fixed terminal cell.

These are exact incidence-continuation tests. The result does not silently promote those incidences to executed payload operations.

## What is now distinguished

Two prospective claims must not be conflated:

- **Transported-preparation symmetry:** carry geometry, reference slots and continuations together. The derived S passes the stated geometric and record-transport tests.
- **Same-preparation reconciliation:** compare the two histories at the same original registry and binding. S alone does not provide that comparison.

Merely pairing the histories supplies neither action. A candidate comparison must specify which claim it makes, its map on complete records, its source-reader action and its continuation transport. Those data must then be bound to the existing native comparison rule using actual operand derivations.

The remaining source choice is therefore concrete: which complete Su-32 reader and preparation relation define the intended comparison? No new physical reader or policy is installed by this audit. The existing candidate common-record regrouping is not refuted; its native binding remains separate from this geometric symmetry.

## Verification

```sh
node research/strominger/checkers/check_su32_comparison_license.mjs
python research/aspect/scc/scc.py check strominger-su32-comparison-license-v1
```

Receipt: `results/su32-comparison-license-v1/verification.json`. It retains both paths, the original and transported registries, complete channel witnesses, all four suffix tests and the counterexample to unchanged-edge continuation. `nativeSu32ComparisonCompiled` is false. No Agda run, native source mutation or physical comparison admission is claimed.
