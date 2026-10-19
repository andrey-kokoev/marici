# Prior-research search: clues for native and physical coupling

## Main finding

There are already explicit source-addressed coupling constructors, retained-energy
mechanisms and charge/phase candidates in the prior research. The correct next
step is to transport and test them on the current five-cell/pair records, not to
say that a coupling must be invented from scratch.

However, none of the packets read establishes the physical multi-object channel
identification or fixes the present annihilation/branching rates. Several contain
important failed quantitative tests which must not be erased.

This was a targeted repository search and document review, not a claim to have
exhaustively audited every prior research file.

## 1. Strongest constructive clue: finite signed record gates

`finite-record-mediator-constructor.md` explicitly constructs

    R_plus =(I-P) tensor I + P tensor X,
    R_minus=-(I-P) tensor I + P tensor X.

Both are reversible self-adjoint involutions. With the prior uniform generator
rule Q_R=(I-R)/2,

    Q_plus+Q_minus=I-P tensor X.

This supplies a neutral flip/displacement vertex with a common scalar diagonal,
not an omitted species-dependent contact shift. A normalized pool of M neutral
records gives an oscillator ladder in the fixed-occupation limit:

    <n+1|sum X_j/sqrt(M)|n>=sqrt((n+1)(1-n/M)).

The rule uses a common elementary gap, g=1/2, explicit pool preparation and a
common empty reference. It is a uniform constructor, not a coefficient fitted
from the desired mass.

**Use now:** transport P and its controlled signed extensions through the current
native pair encodings; retain both signs, record metric and empty-reference
subtraction. Check whether it supplies a useful dressing or conversion operation.
Do not call it conversion merely because neutral record occupation can change:
the prior field model conserves matter species number.

**Preserved failure:** identifying the elementary clock unit directly with the
electron rest energy gave about 71.36 keV versus the held-out 1293.33 keV splitting.
The constructor exists; that calibration failed.

## 2. Source-addressed full-spin contact already exists

`interacting-elementary-reference.md` reconstructs the actual four-face electron
contact and finds the full rank-two spinor return, not one selected spin:

    sum_i P_i=2I, J^dagger J=I, P_contact=J J^dagger.

Under the same neutral field law the coherent spin doublet has energy 3/4 in the
chosen occupation-gap unit. The earlier source contact is therefore a concrete
candidate for spin-independent dressing, rather than an arbitrary scalar label.

**Use now:** transport the contact construction to all five native cells/faces
and compare its operation with the present encodings. The old eight-coordinate
four-face carrier cannot simply be identified with the current ten-coordinate
five-cell extension.

**Preserved failure:** normalizing by the dressed elementary state changed the
held-out splitting to about 95.15 keV, still far below 1293.33 keV. Changing dark
spinor defect weights cannot repair that particular rest-gap comparison.

## 3. Opposite-phase pairing: retained common phase matters

`electron-pairing-coupling.md` finds the primitive retained attachment

    D_a(v)=v_a/conjugate(v_a),
    D(zv)=(z/conjugate(z))D(v).

The state-dependent version carries phase weight two and supports opposite
variable phase weights. Freezing or root-normalizing it erases that distinction.
Both versions satisfy the retained relative arrow constraints, so those
constraints alone do not select the physical contract.

The same packet constructs the neutral bilinear singlet

    B(p,e)=p_0 e_1-p_1 e_0.

A supplied neutral output imposes q_p+q_e=0, but does not fix absolute charge.
The pair effect is valid; the associated antiunitary single-spinor relation is
not a deterministic completely positive spin-flip gate.

**Use now:** preserve common phase in the native pair adapter and distinguish a
conjugate representation partner from a physical operation creating that partner.
An explicit neutral binary vertex is a promising selection input, not something
already implied by the 100x4 pair isometry.

## 4. Prior energy/occupation machinery should be reused

`prior-retained-energy-mechanism-recovery.md` already records reversible mismatch
memory, retained-history locking, autonomous programme execution and occupied
interface dressing. `geometric-phase-energy-bridge.md` maps full geometric records
to actual native phase/alignment operators and all 21 belt seam controls.

`persistent-seam-occupation-energy.md` gives

    S_e=c-P_e,
    h_e=epsilon n_e+J(n_e-S_e)^2-gX_e,

with a positive common-vacuum-subtracted energy and stability bound. Coupling to
P_e instead makes satisfied interfaces inactive: a bond resource is not an error
syndrome bit.

**Use now:** choose explicitly which resource is being transported—mismatch,
satisfied-interface occupation, or neutral field. Counts of records do not by
themselves determine their Hamiltonian or channel coupling.

## 5. Important correction: existence is not uniqueness

`research/nima/uniform-local-core-proof.md` explicitly adopts existential source
derivation within declared complex mathematics. The uniform rule

    H_f=pi (I-P_f)/2

constructs a generator from a native involution and reaches P_f at the unit
endpoint. Alternative rules do not refute that existence theorem.

Our present adapter/coupling can therefore legitimately be a uniform constructor
without proving unique physical selection. The stronger claims—physical energy
normalization, laboratory realization, observed branching rates—still need their
own evidence. Uniqueness should not become a prerequisite for construction.

## 6. Two useful hostile controls

`research/nima/mass-rotor-action-and-external-charge.md` supplies explicit actions,
but phase locking gives energy ratio 1/1836 with unit external charge, while
charge locking gives energy ratio 1836 and external charge 1836. Gauge symmetry
also permits altered inertias. Energy count alone cannot select charge or scale.

`research/nima/hminus-radiative-channel.md` supplies a conditional E1 radiative
matrix element. It vanishes at its exact threshold trial, requires the appropriate
singlet/parity component, and distinguishes transverse photon polarizations.
It is not derived WG electromagnetism or an annihilation calculation, but is a
useful template for what a physical channel test must retain beyond energy
conservation and a nonzero formal map.

## Recommended next test

1. Transport the finite signed-record constructor to the checked native spinor
   encodings, retaining the full complement and common ready reference.
2. Add the source-anchored common-phase or explicitly neutral binary pairing
   contract, rather than inferring opposite physical charge from conjugate notation.
3. Test the complete coupling against native transport and actual orbital/output
   symmetries; distinguish dressing from pair conversion.
4. Fix any clock/vertex convention before a held-out comparison. Preserve the
   earlier failed rest-energy identifications; do not fit them back into the law.

This is a more concrete continuation than a generic parameter sweep, while not
promoting a promising prior mechanism to a physical theorem.

## Fresh verification versus read-only recovery

Freshly executed successfully during this search:

    python research/voevodsky/checkers/check_electron_pairing_coupling.py
    python research/nima/checkers/check_uniform_local_core.py

The other cited packets were read, not freshly reverified in this turn. Their
reported results above are prior results, not new execution claims.
