# Bounded prior-work search: repair the reader, not the energy

## Search question

Can existing research repair the positive-form counterexample by retaining
energy-carrying directions, or does it supply an independently derived form
whose radical already contains those lost directions?

The search covered retained Hamiltonian observers, reversible Haar/native
realizations, prior retained-memory constructions, radical descent criteria,
and signed native Weil attachments. The following are the directly relevant
hits; this is not a claim of exhaustive repository coverage.

## Found: a source-derived energy observer with the right kernel

`research/strominger/retained-hamiltonian-observer.md` and its constructor
`checkers/retained_hamiltonian_observer.py` construct a row-basis reader of a
real skew source generator D. Its hidden space is ker D, which is also the
radical of the energy ||Dx||^2/4. It retains those hidden coordinates for full
state reconstruction. This is different from the four-mode cycle-cover reader,
whose kernel includes nonzero-energy directions.

Apply that EXISTING constructor to our same twelve-arrow D12. The source
Gram is G12=10I+J and J D12=0. Consequently its actual Hessian is exactly ten
times the generic observer's Euclidean Hessian. Multiplying the observer's
inherited energy by ten therefore preserves the original energy convention;
it is not a fit to a desired arithmetic value.

The resulting reader has six coordinates. Its six-dimensional kernel has
zero Hamiltonian and stationary dynamics. The full source clock descends
through this reader as well. The state from the previous counterexample is
now seen and its energy 980 is recovered exactly; the visible Riemann-collapse
counterexample is also seen, with energy 20. All twelve source basis vectors
reconstruct from active and retained-kernel coordinates.

The six-coordinate count is minimal for a linear amplitude reader reproducing
the complete energy: rank K12=6, and a factorization K12=P^T QP implies
rank P>=6. Thus no four-coordinate linear reader can carry this full Hamiltonian,
regardless of its analytic labels. The positive source NORM has rank twelve
and does not descend even to the six-coordinate energy quotient. Norm and
energy must remain distinct.

This repairs the coefficient information loss without replacing the source
Hamiltonian. It does not construct a map from those six coordinates to Weil
tests or identify their positive energy with the Weil functional.

## Found: faithful analytic retention, but no new arithmetic energy law

`research/nima/1836-to-haar-reversible-realization-retains-the-energy-defect.md`
already builds the isometric map h -> v tensor h using a source-derived native
rank-one mode and the complete relative-Haar history space. Prime action and
recovery intertwine exactly. No history is lost.

The same result proves that the prime energy defect survives unchanged. This
is a useful available architecture for retaining an analytic history; it does
not turn a failed arithmetic equality into a true one. Its domain is the
relative-Haar source and its internal carrier has 36 coordinates, not our
12-coordinate source; those interfaces cannot be silently identified.

## Found: signed Weil attachment, not positive-form identification

`research/voevodsky/rh-seed-signed-attachment-v1.md` realizes a supplied
Hermitian packet G as B_G^* K B_G=G in a native signed form. The map depends
explicitly on G and preserves negative controls. It does not derive G from a
positive source metric. It therefore cannot repair the conjecture by supplying
the positive equality independently.

## No matching radical repair in the inspected packets

`research/nima/many-many-radical-descent-source-criterion.md` requires a
source commutator identity before a different bulk form descends. That packet
records the identity as unproved; its radical is not our finite cycle-cover
kernel.

`research/nima/the-residue-positive-block-and-the-retained-pair-energy-are-distinct-strata-and-cannot-be-identified.md`
already rejects a closely related substitution: the residue vanishes where a
retained pair has positive energy. Changing the residue metric cannot identify
the two. It supports keeping the present counterexample rather than renaming
its vanished analytic state.

`research/voevodsky/prior-retained-energy-mechanism-recovery.md` recovers exact
reversible memory laws and emphasizes existential construction rather than
uniqueness. Those laws retain energy in a register; they do not identify that
register energy with an arithmetic scalar functional. No uniqueness demand
is needed for the six-coordinate repair above.

## Decision

Keep the confirmed operation bridges and the failed four-port positive-form
claim. Reuse the six-coordinate source-energy observer if pursuing the energy
branch. A subsequent arithmetic claim must specify a map from that retained
active state to actual Weil tests and test its form equality; attaching a
positive norm or copying the target form is not that test.

No inspected packet already proves the required source-energy/Weil identity.
The new exact computation establishes the narrower constructive repair:
energy information can be retained using an existing source-derived reader.

## Verification

Run `uv run research/voevodsky/checkers/check_recovered_source_energy_observer.py`.
It checks the previous counterexample's source hashes, imports the existing
observer constructor without running source-owner writers, derives its scale
from G12 D12=10D12, verifies exact Hessian factorization, reconstructs all
basis states, and recovers both previous witness energies. Results:
`results/recovered-source-energy-observer-v1.json`.

The other cited packets were freshly read, not freshly executed. No shared
source was edited and no commit or push was performed.
