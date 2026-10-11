# Prior-work search: continuous rotor lift versus retained-history execution

## Closest existing continuous intertwiner

`rotor-rung4-action-metric-bridge.md` already constructs a compatible extension
of a specified rotor generator through the fixed-Gram tower. With its actual
embedding E and metric-adjoint projection P, PE=I, it defines

    D12=E D4 P,
    P D12=D4 P,
    D12^T G12+G12 D12=0.

The discarded orthogonal sector is fixed. The exact generator identity gives
continuous intertwining, not merely matching tick endpoints. Its checker
was freshly rerun: 45 exact/symbolic checks pass.

This is an EXISTING method preferable to assuming a new parent/child swap
will have the same intermediate dynamics. But its carrier is the fixed
stabilizer-probe Gram tower, not the growing retained path family or the
137-row response fixture. The actual seed relation there uses the active
sector of its unique four-cycle cover; it does not identify that whole
permutation with a continuous rotor. These qualifications must survive reuse.

## Continuous realization already retains history labels

`retained-rotor-norm-completion.md` completes packets of the form

    (history, signed center, coefficient sequence).

Its Cauchy equivalence requires equality of history and center labels, so
completion does not erase them. It constructs the continuous differentiable
rotor, controlled derivative, group law, signed chart comparisons and finite
returns through explicit coefficient/tail bounds.

This supplies continuous realized dynamics WITH retained labels, not a theorem
that appending an entire branching history is itself that same Hamiltonian
flow. Insisting that every provenance coordinate be a Hamiltonian degree of
freedom is an additional modeling demand, not a consequence of retention.

Rerun attempted:

    python research/nima/checkers/check_retained_rotor_norm_completion.py

It stopped because the prerequisite receipt
`results/agda-FormalRotorCoefficients.json` was absent. No fresh pass is
claimed for this branch. Its written completion proof was inspected.

## Formal retention versus action quotient

`../voevodsky/retained-history-lift-action-and-the-missing-section.md` provides
the chain History -> SignedLift -> AdjointAction, retaining full construction
trees and showing that neither endpoint nor signed lift recovers history.
Its no-multiplicative-section result prevents dropping central signs and
reconstructing them consistently later. This is the declared Clifford-word
prototype, not all histories of the six-arrow successor. The formal suite
was not rerun during this search.

## Autonomous history execution exists, but is programmed

`mass-autonomous-history-execution.md` supplies a time-independent history
Hamiltonian for a supplied reversible programme. Its gates, clock couplings
and initial state are inputs. It neither selects the triangle successor's
physical execution nor proves continuous compatibility with the current
rotor endpoint reader. Its existence should not be rediscovered as a new
source-derived clock.

## Bilateral dilation: relevant mathematics, different source sector

`canonical-bilateral-dilation-of-history-translation.md` realizes half-line
translation in L2(R) by a strongly continuous unitary translation group with
Stone generator -i*d/dq. Its source is the two-history Xi carrier. Even there,
forcing/observation port lifts remain explicit open obligations; point
readers need a rigged domain. No identification with our branching successor
is supplied. This is not a ready-made physical solution to the current gate.

## Correct next use of prior work

For continuous observation compatibility, inspect whether the actual
triangle endpoint/rotor adapter admits the same metric-adjoint embedding /
projection construction already used in the fixed-Gram tower. Do not infer
compatibility from equal dimensions or merely matching one discrete update.

Keep distinct:

1. the existing continuous rotor evolution and clock on the actual cyclic
   endpoint contrast, now integration-tested;
2. retention of all source histories alongside that realized evolution;
3. a stronger autonomous Hamiltonian implementing the creation of those
   growing histories themselves.

Prior work supports the first two in their declared realizations. This search
did not locate an existing proof of the third for the actual six-arrow
successor with the same intermediate observer. The failed swap experiment
is not a general obstruction and is not needed merely to retain provenance.
