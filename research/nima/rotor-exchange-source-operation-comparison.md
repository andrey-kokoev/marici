# Executed comparison: the rotor reading and the existing seed-port exchange

## Actual source operations, not matched dimensions

Reuse the two original LR/RL path families and their full-seed continuation.
For each retained word w, evaluate its arrows in order by the EXISTING
22-coordinate seed-port exchange operators S_e. Then sum those operator
values at the ACTUAL final endpoints, with LR minus RL signs:

    D_(n,v)=sum_(LR words ending v) S_w - sum_(RL words ending v) S_w.

These operator-valued sums compare the same retained endpoint aggregation
used by the rotor. They do NOT assert that adding branch operators is itself
one physical pulse or a new quantum-superposition rule. Both underlying
path families and their role labels remain available.

The checker independently verifies direct word evaluation against

    D_(n+1,b)=sum_(e:a->b) S_e D_(n,a).

All six ports and all endpoint joins are the original bound source ports.
No new initial excitation or coupling law is chosen.

## Exact result on the full internal state domain

The original cyclic count contrast is d0=(1,-1,-1,1) with d_n=M^n d0.
The exchange's conserved anchor is

    a=y+F r.

For every initial internal state z and every tested phase, exactly

    anchor D_(n,v) z = d_(n,v) anchor z.

Thus the existing exchange DOES retain the same cyclic endpoint reading
through its conserved anchor. The shared source/clock comparison is real.
It is not a comparison of two unrelated matrices selected by dimension.

But the full endpoint-resolved INTERNAL response is richer. Stack the four
D_(n,v) into an 88-by-22 matrix D_n. Exact ranks are

    rank(D0+D1+D2)=6,
    rank(D3-D0)=6,
    rank(D6-D0)=6.

Every kernel is EXACTLY the 16-dimensional common matched sector

    r=F^T H y,

which every individual exchange fixes. The checker proves this by kernel
inclusion and complementary rank, not by sampling input states.

Therefore full internal response has the rotor's three-return AND the
six-update full-turn return only on that inactive exchange sector. The six
active mismatch directions produce nonzero response differences. The old
AB-record preparation, reused without tuning, witnesses the full-turn
residual; one exact nonzero entry is -12500454308901/34522712143931.

## The intermediate Hamiltonian check

The existing continuous pulse at port e uses

    P_e=(I-S_e)/2,
    U_e(theta)=I+(exp(-i theta)-1)P_e.

P_e is a metric-self-adjoint projector; at pi the pulse is exactly S_e.
For EVERY angle the conserved anchor and the common matched sector are
fixed, since anchor P_e=0 and P_e applied to that sector is zero. These
identities are verified for all six ports.

So the cyclic motion seen in endpoint aggregation of that anchor is not
motion caused by an exchange force on the anchor itself. It is the source
continuation acting on the endpoint distribution of retained words. The
exchange's actual back-action occupies the additional mismatch sector.
The failure at the full-turn endpoint already excludes identifying these
complete endpoint-resolved internal responses with the current pure rotor
orbit through an all-angle equality of that same reading.

## What this says about 'the same process'

Positive: both constructions can describe compatible aspects of the SAME
source-labelled path family, and the conserved-anchor reading carries the
established rotor recurrence on every internal input.

Not established: that the pure rotor Hamiltonian alone IS the existing
mechanical exchange Hamiltonian. The active exchange contribution is not
captured by that cyclic reading. The comparison now locates the difference
in an exact six-dimensional sector rather than leaving it as a generic
'missing bridge'.

This is not a universal no-go for a coupled realization. A completed base
witness can coexist with change in an attached state; the earlier actual
Tick-history action was designed for precisely that distinction. Nor is the
operator-valued aggregate residual itself a single physical recoil or
holonomy of a closed path: the full retained family contains different
endpoint paths. Those claims would need their actual event/fiber attachment.

The result rules out the specific shortcut of treating cyclic endpoint
agreement as equality of the whole interaction. It does not diminish the
Hamiltonian/witnessing construction or require a new external observer.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run --with sympy --with 'numpy>=2,<3' python research/nima/checkers/check_rotor_exchange_source_operation_comparison.py

77 exact comparison checks pass, rerunning the prior 267-check port binding
and actual component-composition suite. Full word evaluation is checked
through six continuations; the residual-kernel classifications are exact
linear algebra on the complete 22-dimensional input domain.
Receipt: `results/rotor-exchange-source-operation-comparison.json`.
