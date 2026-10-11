# Full-turn witnessing with the actual active exchange action

## The branch action is now explicit

Reuse the actual LR/RL products, then perform the existing six full-seed
continuations corresponding to the retained 2pi rotor turn. The completed
family contains 34 LR and 34 RL words. For each word, keep its initial
2-arrow preparation separate from the six subsequent appended arrows.

The existing exchange's active coordinates are

    delta=r-F^T H y,
    K=I+F^T H F,
    T_i=I-K[:,i] e_i^T.

For each primitive port, exact source binding gives

    delta(S_i z)=T_i delta(z).

Thus the six-arrow suffix acts by its actual ordered product of T_i. This
computes the full-turn action branch by branch, rather than replacing the
family by one summed physical operation.

Results:

- 68 retained full-turn branches.
- 20 return to their individual starting endpoint; the other 48 do not.
- 62 change the reused AB-record excitation after its own retained prefix;
  6 leave that particular preparation unchanged.
- There is NO nonzero active vector fixed by every full-turn branch action.

The completed rotor witness is shared by the family. It does not imply that
every individual spatial path closes or that every attached internal state
returns. This is an explicit attached-state action alongside the cyclic
reading, not a new clock or a claim that all branches executed sequentially.

## Energy: one common form, not 68 separate fitted budgets

Every port and every complete branch preserves

    E_active=delta^T K^-1 delta.

K is positive definite. The corresponding continuous port generator
P_i=(I-T_i)/2 is self-adjoint in this SAME metric, and its phase-pulse
endpoint is the already existing exchange.

The checker also uses the prior decoder-induced branch weights, whose sum
per initial prefix remains 1/2. The weighted whole-family active energy
therefore remains fixed as records branch. These weights are a retained
Hilbert-metric convention, not Born probabilities. Summing unweighted
copies would count multiplicity, not demonstrate energy creation.

The original rotor Hamiltonian and this active energy remain distinct
specified quantities; no equality of their physical units is inferred.

## Joint invariant classification: the real six-port sector is irreducible

Solving the complete 36-variable commutant equations gives

    {X : X T_i=T_i X for all six ports}=R I.

The equation matrix has rank 35. Since the operators preserve a positive
metric, a proper common invariant subspace would have a commuting orthogonal
projector. None exists. The active representation is therefore irreducible
over the reals.

Two consequences are exact:

1. There is no nonzero LINEAR scalar on this active sector conserved by all
   six ports. The stacked invariant-covector constraints have rank six.
2. Every invariant symmetric quadratic form is proportional to K^-1:
   if Q is invariant, K Q commutes with every T_i. Thus the common quadratic
   invariant space does not provide a second independent signed charge.

This does not exclude nonlinear charges, a charge carried in the conserved
anchor, or the separately constructed complex/dual phase sector. It says
precisely why a signed charge cannot simply be named among these real linear
or quadratic active readings. It also forbids a commuting complex structure
on this un-enlarged real six-dimensional space; using the prior complexified
exchange is a substantive representation choice, not a relabelled real axis.

## Recoil: local compatibility does not yet make a global body assignment

At port i, the prior elastic reading starts with carrier amplitude
`a_i=f_i^T H y` and record amplitude `r_i`. Their sum is conserved by that
port's swap. The actual all-port check finds:

- all six local sums are conserved at their own port;
- each is changed by EVERY other port: all 30 ordered cross-port pairs.

Thus those six local elastic-collision readings cannot simply be called one
fixed pair of body momenta through the whole witnessing cycle.

There is a stronger conditional obstruction. Suppose a FIXED linear map
from the full exchange state to two bodies' momenta gives an autonomous
closed reading for every port and preserves their total momentum. Restricted
to the irreducible active six-space, its kernel is invariant, so its rank
must be zero or six. For one-dimensional two-body momenta the target has
dimension two, ruling out rank six. For three-dimensional two-body momenta,
conservation puts active changes in the zero-total-momentum subspace of
dimension three, again ruling out rank six. Hence such a reading must be
blind to active recoil.

This is not an exclusion of mechanical realization. It excludes the stated
fixed, closed, linear two-body identification of ALL six ports. An attached
larger system, nonclosed/subsystem dynamics, nonlinear coordinates or
source-dependent body charts would have different obligations. None is
inserted merely to evade the calculation.

## Critical-path result

The full-turn active action and its conserved energy are now calculated.
The unresolved item is more concrete than 'find a coupling': the original
single-port two-body interpretation does not extend unchanged to this
irreducible six-port whole. Charge and recoil must be interpreted together
at the whole level, rather than independently assigning each port the same
pair of classical bodies. The existing complex-dual charge result is not
discarded, but has not been identified with that collective mechanical
structure by this calculation.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run --with sympy --with 'numpy>=2,<3' python research/nima/checkers/check_full_turn_active_exchange_action.py

249 exact checks pass. The earlier source-operation comparison and original
seed-port exchange checks rerun. The commutant and invariant-space results
use exact rational linear algebra on the full domains, not sampled states.
Receipt: `results/full-turn-active-exchange-action.json`.
