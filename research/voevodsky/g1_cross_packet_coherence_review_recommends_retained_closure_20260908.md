# G1 cross-packet coherence review recommends retained closure

Date: 2026-09-08

## Review scope

This review checks constructor order, common domains, source idempotents,
radicals, and the terminal-evaluator boundary across the current G1.1--G1.4
closure candidates.  It does not mutate the publication ledger.

## Coherent constructor order

The packets agree on one order:

1. retain prime and grade source idempotents;
2. construct causal-history, window, cut, wall, and Wronskian outputs as typed
   graph coordinates;
3. form the direct-sum polarized Green form while the source coordinate is
   still present;
4. aggregate grades only within one fixed prime Wronskian fibre;
5. apply any scalar sum over primes only as a terminal post-G1 evaluator.

No reviewed closure claim requires the output-only codiagonal.  Its dense
nonclosed range is therefore not a contradiction; it excludes that stronger
architecture.

## Gate review

### G1.1

The retained history graph supplies the source-derived causal block.  Its
reciprocal quarter-turn outputs obey the uniform `I/8` Gram bound.  The exact
source compression has

\[
\tau=-\|\Phi\|_2^2<0.
\]

This is compatible with labelwise transport and does not perform arithmetic
endpoint aggregation.

### G1.2

Endpoint lifts, closed half-density histories, trace continuity, reciprocal
exchange, cutoff naturality, and compatible radical descent are established on
the retained graph.  The source identity coordinate gives closed range and
zero radical.  No output-only closed-range assertion is imported.

### G1.3

The strict source `E_{p,12}` retains its orientation
`S_12=diag(-1,+1)`.  The connected grades have their separate nuclear return.
Only after forming `Gamma_12 direct-sum Gamma_>=3` is the within-prime
Wronskian codiagonal applied.  The stated margin remains greater than `0.244`.

### G1.4

Every retained component commutes with prime projections, so

\[
P_qGP_p=0\quad(p\ne q).
\]

This is consistent with within-prime grade overlap.  Cross-prime products may
appear only after the terminal scalar evaluator and are not G1 blocks.

## Frame compatibility

The real Hadamard sum/difference frame used to expose wall-tail polarization
and the complex reciprocal quarter-turn frame used in G1.1 are distinct
faithful readouts.  Neither changes the retained constructor order, and their
use does not authorize summing outputs before polarization.

## Verdict

The four gates are internally coherent as closure candidates on the selected
source-retained saturated architecture.  This review recommends retained G1
closure to the owning ledger authority, subject to independent confirmation of
the cited formulas.  It does not itself have ledger-mutation authority.

G2--G4 and RH remain open regardless of G1 disposition.
