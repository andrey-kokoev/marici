# Coherent returns with protected history and explicit update cost

## Declared policy

Retain original unit witnesses and any previous triangle as immutable parents.
A successor version must satisfy

    delta(u_new)=r*d-1_A,
    delta(v_new)=d*r-1_B,
    delta(W_new)=d*u_new-v_new*d.

By default, both unit histories are locked. Changing them requires explicit
permission. Selected linear readouts can also be protected as equality
constraints. An inconsistent request rejects without replacing the old records.

Given a declared positive metric, select the feasible version minimizing

    a*||u_new-u_old||^2 + b*||v_new-v_old||^2
      + c*||W_new-W_old||^2.

An absent previous triangle uses W_old=0. The finite checker uses coefficient
norms; a change of basis would require transporting that metric. These weights
are policy inputs, not inferred physical constants.

Accepted versions retain parents, both closed unit-history edits, the triangle,
changed coordinates and total update cost. A complete coherent version is a
zero-cost no-op when submitted unchanged.

## Exact results

The singular-reference example with surviving homology admits a triangle while
both unit histories remain fixed. The solver returns the exact least-cost
triangle under the declared metric. Its positive cost belongs to creating the
filler; both unit-history edits are zero.

The zero-differential counterexample has unit coefficients u_old=1 and v_old=0.
Triangle coherence requires u_new=v_new, since there are no nonzero boundaries
available to fill their difference.

| Permission/readout policy | Result |
|---|---|
| Both unit histories fixed | Rejected |
| Only v editable, weight b=3 | u=v=1, cost3 |
| Both editable, weights a=2,b=3 | u=v=2/5, cost6/5 |
| Both editable, equal weights | u=v=1/2, cost1/2 |
| Both individual coordinate readouts protected | Rejected |
| Only 2u+3v protected, weights2:3 | u=v=2/5; protected value remains2 |

The weighted solution follows from minimizing a(z-1)^2+b*z^2:

    z=a/(a+b), cost=a*b/(a+b).

Thus a common protected readout can coexist with coherent history adjustment,
while protecting both individual values can obstruct it. Parent retention alone
does not imply permission to change an observable's current value.

## Return to the recursive constructor

Accepted versions feed the same fixed-reference recursion, now with e=d*u_new.
Because unit-history edits are closed,

    delta(e)=d*r*d-d

is unchanged. Choosing a cheaper history cannot erase reference drift. The
checker applies two recursive constructor rounds for the accepted fixed and
editable policies and rechecks the degree-two associator equation.

This provides a concrete admission and selection mechanism for the earlier weak
return construction: preserve the declared observations, pay the recorded update
cost, or reject. A physical application still needs to specify which readouts
are protected and where the metric/resource budget comes from. Recorded positive
update cost is not itself a conservation law or a mass/coupling prediction.

## Verification

    python research/nima/checkers/check_coherent_return_history_policy.py

Rational row reduction detects inconsistent constraints. Independent constraints
and their positive weighted Gram matrix give the least-change solution. Exact
feasibility and stationarity certify its unique minimum. Tests cover immutable
parents, unchanged-version zero cost, locked-history rejection, permitted edits,
protected readouts, closed edits, reference drift and recursive composition.
