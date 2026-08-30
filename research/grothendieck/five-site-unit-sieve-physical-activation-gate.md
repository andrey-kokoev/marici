# Five-site unit-sieve physical activation gate

## Joint gate

For a branch quotient `q_B:(C2)^5 -> (C2)^5/(C2)^B`, an index `n` can enter
the frozen paired physical readout only if two logically separate conditions
hold:

1. the power operation is algebraically Mackey-compatible with `q_B`;
2. the frozen coefficient selector `delta_0` descends through `q_B`,
   equivalently it is constant on kernel fibers.

Ledger 1282 gives the first condition exactly for odd `n`.  The second fails
for every nonempty `B`: the identity fiber contains `0`, where `delta_0=1`,
and a nonzero kernel point, where `delta_0=0`.

Therefore no power index, including every odd unit-sieve survivor, activates
a nontrivial five-site branch quotient as the frozen physical readout.

## Exact census

Across all 31 nontrivial branch kernels and indices `1..24`:

- 372 branch/index pairs are algebraically compatible (all odd indices);
- zero nontrivial branches admit selector descent;
- zero pairs pass the joint physical gate.

The identity quotient is the control: its selector descends and all 24
indices pass the quotient gate.

## Scope

This does not invalidate the algebraic unit sieve, norm, Loewy, or
conjugation-exponent theorems.  It shows that algebraic power compatibility is
not a constructor for the missing physical relative-chain pushforward and
does not repair the frozen cosmological selection variance.  An orbit trace
may descend, but it changes the observable.

