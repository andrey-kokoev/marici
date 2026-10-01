# Iteration 9: preparation, reset and control resource ledger

## Fresh input and energy convention

The end-to-end checker and its eight supporting checks are freshly rerun. Use
its actual native trace-seeded coherent preparation, not a new amplitude fixture.
For X means x, independent vacuum P quadratures and zero P means, the excess
oscillator occupation is

    N = ||x||^2/2.

For equal independently calibrated mode frequency omega, the free excess energy
is E=hbar*omega*N. This is a supplied physical oscillator identification, not a
source-derived energy unit. For unequal frequencies or pumped mode conversion,
excitation conservation alone is not laboratory-energy conservation.

The prepared occupation is exactly88061/7200, approximately12.2306944444.
The compiled rectangle preserves it. Afterwards the carrier contains approximately
.836588541667 and the records11.3941059028 excitations.

## Reset is not the reverse exchange history

A record-only reset can be realized ideally by swapping each record with a fresh
vacuum environmental mode. The carrier remains excited. Preparing the original
record displacements again therefore produces occupation13.0672829861, not the
original12.2306944444, and changes the anchor packet. This is not a fresh repeat
of the declared zero-carrier preparation.

Resetting ALL carrier and record modes by swaps with vacuum ancillas does give
zero device means, but transfers the complete previous means to the environment.
System-plus-environment occupation remains conserved. The state has not been
erased from that enlarged description. Reusing or disposing of those ancillas
is another physical operation requiring its own resource account.

In contrast, applying the actual four-event history in reverse order recovers
the original entire preparation exactly in this ideal model. The eight-event
history remains retained. This recovery is checked BEFORE destructive detector
readout; it is not a recovery protocol after information or energy has been
lost to an unobserved detector/environment.

No universal Landauer cost is inferred from a count of137 records. The present
states are declared coherent preparations; entropy, available side information,
work recovery and bath conditions must be specified before an erasure-cost claim.

## Ideal pulse-control work

For a selected difference mode b and H_control(t)=hbar*kappa(t)*b^dagger b,
its occupation is constant during an isolated ideal pulse. Ramping the coefficient
from zero to kappa and back gives work

    W_on = +hbar*kappa*<b^dagger b>,
    W_off = -hbar*kappa*<b^dagger b>.

Their sum vanishes in the ideal reversible switching model. The checker verifies
the same difference-mode occupation before and after each compiled pulse.
This cancellation is not evidence that a laboratory pulse generator, timing
system or phase reference has zero cost. No such controller model is included.
Pulse area must still be pi; kappa and duration remain separately unspecified
physical control parameters.

## Detector loss and uncosted apparatus

A vacuum loss-port dilation sends a measured coherent X mean m to sqrt(eta)*m
in the observed mode and sqrt(1-eta)*m in an environment. Their excess occupations
sum to m^2/2. Missing detected excitation is not destroyed by assigning an
efficiency to the readout.

The current ledger does NOT quantify:

- preparation inefficiency;
- supply and recycling of vacuum ancillas;
- environment disposal versus recoverable work;
- controller losses and timing resources;
- the local oscillator and phase monitor;
- electronics and detector resetting.

A complete apparatus energy balance must include these. The checked conclusion
is narrower: the declared exchange and ideal dilations have consistent budgets,
and the tempting record-only reset protocol fails the preparation contract.

## Verification and disposition

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_exchange_resource_accounting.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-exchange-resource-accounting

The initial occupation is evaluated exactly from rational native responses.
Propagation, reset and switching-work checks use tolerance1e-10. Report:
`results/exchange-resource-accounting.json`.

The remaining work is to consolidate these bounds with the state, composition,
measurement and normalization gates. Conditional end-to-end execution is now
checked, but native instrument selection and absolute current/field coupling
remain unproved. Ideal reversibility must not be used to conceal those gaps.
