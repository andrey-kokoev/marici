# Partial binding of the geometric request schedule to electron spin transport

## Result

The five electron requests now have a checked action on the existing logical
spin doublet, through both its cell and face encodings. **69 exact checks pass**
for both chiralities and both lift choices.

This is a partial source binding, not a complete proton/electron interaction
schedule. Proton spin requests and relative-position/contact updates remain
unbound; they have not been silently assigned identity actions.

## Existing source construction reused

`research/voevodsky/checkers/check_pentachoron_cycle_transport.py` supplies the
five-cell transport T and exports conditional doublet cell/face encodings.
The new checker reads its existing receipt and verifies all its source hashes.
It does not regenerate or overwrite owner artifacts.

For each exported cell isometry W, derive the logical action rather than choose
one:

    U = W* T W.

Fresh exact arithmetic verifies W*W=I, U*U=I and TW=WU. The analogous covariance
is checked on the entire 40-row face encoding, using the source permutation of
both cell and face labels and its spin action. Thus the same U acts on the
actual embedding used by the existing contact-singlet construction.

All five electron primitive correspondences use the one supplied affine source
generator. The two backends have different vertex names: the pair adapter names
the affine origin A, while the spin backend names it E. The explicit dictionary
is A->E, B->A, C->B, D->C, E->D. It preserves the directed five-cycle. This is
not an identification of similarly named ports without checking conventions.

## Effect on the existing singlet relation

For an electron-only request the pair action is I tensor U. Here I means no
proton operation is requested; it is not a proposed action for proton arrows.
Apply this to the existing normalized singlet s and its projector Pi=|s><s|.
For all four variants:

- one electron step changes Pi;
- five electron steps restore Pi;
- the displayed lift gives U^5=-I;
- the opposite lift gives U^5=+I.

Consequently, if a supplied policy were to require preservation of the fixed
singlet projector at every atomic step, these electron-only steps would fail
that condition. That policy is **not** supplied by merely including Pi in a
Hamiltonian. A Hamiltonian interaction need not keep its input in Pi's image.
No transition has been removed from the geometric graph on this basis.

## What the geometric quotient forgets

One and two complete electron cycles have the same geometric predictive state.
For the displayed spin lift their amplitude actions are -I and +I. Therefore
that vector-level action needs additional cycle-sign information, or a retained
history, beyond the geometric state. Both give the same action on projectors;
a global sign is not itself a different isolated-state observable.

The rung records retain the word and hence its electron-step count. The checker
recovers the count and the five-step spin action through both transport policies.
This is a concrete case where predictive sufficiency depends on which added
carrier and readout are requested.

## Remaining binding obligations

1. Supply the proton spin action for each actual proton source generator. The
   contact model's declared spin extension alone does not assign these actions.
2. Supply the relative-position/contact update and mediator interface. No
   geometric endpoint letter is used as a substitute for separation.
3. Specify initial logical preparation and any physical choice of chirality/lift.
4. Specify whether admission protects a fixed singlet sector, permits its
   evolution, or transports the comparison target.

Only then is a source-bound restricted joint graph or maximal closed domain
well-defined. The present result connects a real portion of the existing
interaction carrier to the schedule without inventing these missing operations.

## Reproduction

    python research/nima/checkers/check_predictive_pair_electron_spin_binding.py

Receipt: `results/predictive-pair-electron-spin-binding.json`.
It records all four induced logical matrices, the label dictionary and hashes.
Verification uses existing exact arithmetic and freshly rebuilds the geometric
bridge. It does not replay the owner's complete embedding producer or contact
energy calculation, and makes no physical time or energy calibration claim.
