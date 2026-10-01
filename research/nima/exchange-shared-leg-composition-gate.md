# Iteration 5: addressed exchanges do not factor through shared legs

## Fresh state and contract tested

Iteration4 found that the native additive witness response does not provide
independently writable record amplitudes. Attaching instrument memory addresses
that state issue conditionally, but does not automatically give a representation
of native path composition. This iteration tests that separate obligation.

Suppose each slot exchange H_ij were the composite Y_j X_i of invertible
primitive-leg maps acting on the same joint carrier/record state space. Then
for any rectangle with base indices r,c,

    H_ij^-1 H_rj H_rc^-1 H_ic = I.

This follows by substituting Y_j X_i and cancelling adjacent inverses. A common
invertible output-reference map can be absorbed into Y_j and does not remove
the requirement. This is a consequence of the PROPOSED instrument factorization,
not a claim that the native DG source equates arbitrary event histories.

## Exact hostile on every rooted rectangle

Every exchange is its own inverse. The required identity is therefore the
chronological event word

    (i,c), (r,c), (r,j), (i,j).

Choose i!=r and j!=c, zero carrier amplitude, and unit amplitude at only the
first record port (i,c). The first exchange empties that port and transfers its
amplitude to the carrier. The other three distinct events never write that
record again. Its final amplitude is exactly0, rather than the initial1.
Therefore the rectangle operator is not identity.

The exact rational checker verifies all100 rooted arrow rectangles and9 rooted
state rectangles. It also checks the16 conserved anchors and total budget after
every event. Executing the four events in REVERSE order afterwards returns the
complete state exactly. Reversible temporal dynamics is intact; the failed
property is shared-leg factorization, not reversibility.

## Preparation/readout consequence

The oscillator contract already supplies a conditional physical test. Prepare
one real coherent record amplitude A and zero carrier, then apply the four
addressed pulses with no intermediate reset or measurement. A final signed
quadrature reading at the first port has mean0 under exchange, whereas the
strict shared-leg identity hypothesis predicts sqrt(2)*A. Ideal coherent
variance remains1/2 in either case. This statement imports the previously
declared oscillator assumptions; the present checker verifies the amplitude
identity exactly, not experimental frequencies.

The first-record emptiness also holds for any fixed nonzero initial amplitude.
No equilibrium assumption, normalized1/137 share, fitted gain or energy-only
argument enters the falsifier.

## Honest adapter contract

There are now two different notions of composition:

- Native legs compose to comparison paths, with retained endpoint witnesses.
- Instrument events compose as ordered addressed exchanges on carrier plus
  separately attached memory.

The existing exchange model supports the second. Assigning its137 operators to
the native137 composite labels does not establish the first. In particular a
source square cannot be compiled into a physically empty rectangle merely by
forgetting the independent record addresses.

A viable weaker construction is a labelled-experiment compiler: retain each
source comparison and its witness provenance, use its declared feature to
address an instrument pulse, transport labels and references covariantly, and
retain the chronological event word. This preserves event concatenation but
must not advertise shared primitive-leg factorization or descent through an
unproved source path-equivalence quotient.

The immediate implementation target is that explicitly typed compiler, including
rejection of unauthorized rectangle flattening. It can establish a conditional
source-labelled experiment without pretending that the source uniquely selected
the memory, pulse Hamiltonian, preparation or physical normalization.

The obstruction is limited to invertible leg maps on the same state space.
Larger intermediate spaces, noninvertible/dilated maps or additional higher
witness actions require separate tests and are not excluded here.

## Verification

    python research/nima/checkers/check_exchange_shared_leg_composition.py
    python research/aspect/scc/scc.py check nima-exchange-shared-leg-composition

The prior exact raw-coordinate exchange checker is rerun. All109 rectangle
controls, conserved anchors/budgets and reverse-word recovery use Fraction
arithmetic. Report: `results/exchange-shared-leg-composition.json`.
