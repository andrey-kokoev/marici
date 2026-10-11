# Existing target fibers give a nontrivial arrival effect, not an interaction law

## Candidate tested

Use the actual retained table, `ActualSeedEndpointTable.seed`, and the existing `TableFibrationCycle.group-to` operation. Its fiber at v is

    Arrival(v) = (e : Occurrence, target(e) = v).

This gives an actual common comparison type for each direct/indirect pair. The chosen observation update is `arrive e previous = (e,refl)`: read the supplied traversal as the currently arriving row. This is an explicit, simple observer of source records, not a claim that the table itself supplies physical dynamics or an invertible payload transport. No scalar weights or desired gravitational values enter it.

`agda/SeedArrivalEffects.agda` instantiates the preceding `Effects` interpreter with these existing fibers and this reader. No new seed or arbitrary matrix payload was introduced.

## Computed active discrepancy

| Route | Common target fiber | Active arriving occurrence |
|---|---|---|
| AB | Arrival(B) | AB |
| AD DB | Arrival(B) | DB |
| BA | Arrival(A) | BA |
| BC CA | Arrival(A) | CA |

Both parallel pairs have provably different active values. The proofs discriminate the existing occurrence constructors; they are not numerical comparisons or just different endpoints.

On all four complete first returns the reader computes:

    ABA   -> BA
    ABCA  -> CA
    ADBA  -> BA
    ADBCA -> CA.

Thus it remembers the returning choice but forgets the outward choice at the active-value level. The full trace separately retains the initial arrival and the entire route; recovery of both is proved. The unchanged six-row source table remains available, including all off-route complement records. The earlier pairwise history-separation proofs still apply even where active values agree.

## Existing regrouping and recovery do not remove this discrepancy

For any selected column (label, source or target), embed an occurrence into the existing grouped/restored presentation and recover it with the supplied `TableIso`. Its round-trip is proved equal to the original occurrence for every e and every column.

Consequently AB cannot become DB, and BA cannot become CA, merely by these recoveries, even if different grouping columns are used on the two sides. The existing four-step grouping/reversal recovery also preserves every occurrence. These are uses of the actual table isomorphisms, not assumed path-dependent payload maps.

This does not forbid a separately supplied equivalence swapping two active rows. Such an equivalence would change the named occurrence observation and needs its own interpretation; it is not furnished by field-preserving presentation recovery.

## What this adds and where it stops

The previous conditional effect interface now has a concrete nontrivial instance drawn from existing target fibers. Its output is a retained discrepancy, not a missing equality that should be filled by fiat. The direct/indirect equality witnesses required by the previous conditional square do not exist for this reader.

This reader alone cannot represent a mixed interaction: the complete-return active output depends only on the returning choice. It is therefore a useful source-derived observable but not a complement back-reaction mechanism. The next substantive requirement would be an actual state-changing operation responsive to the retained outgoing information and this incoming discrepancy, with its source authorization and recovery data. No such operation, energy, physical time, gravitational gain or G has been constructed here.

## Verification

Fresh check:

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedArrivalEffects -Fresh

Passed with safe Cubical/guardedness flags, ignored interfaces, stable inputs and exit code zero. Receipt: `results/agda-SeedArrivalEffects.json`. Finished 2026-10-05T20:09:29.9735801Z; source SHA-256 `fa17557aabf4b8d4a6ef118cd9330060d37882a7e86266ad4f077396bdf4bb0d`.

An initial import-selection error was corrected by qualifying the existing `Effects` module; the subsequent full fresh check passed. No postulates or unresolved holes were added. No ledger entry, commit or publication is claimed.
