# Coherent optical analogue of the neutral record block

Contract: `research/conjecture_net/contracts/optical-neutral-record-block.v1.json`.
Checker: `research/voevodsky/checkers/check_optical_neutral_record_block.py`.
Receipt: `research/voevodsky/results/optical-neutral-record-block-v1.json`.
Run: `uv run research/voevodsky/checkers/check_optical_neutral_record_block.py`.

## Source and encoding

Declare two orthogonal optical modes with standard bosonic mechanics and a prepared single total excitation. Encode logical neutral |0> as |10>, |1> as |01>. Keep optical vacuum as a THIRD outcome, not logical |0>. This is a supplied quantum framework and preparation, not a geometric derivation or a claim that the neutral record physically is a photon.

Reuse the prior difference-mode/exchange construction's explicit diagonal and coupling discipline. In a chosen rotating frame supply

    H/(hbar Omega)=b†b-(a†b+b†a)/2, Omega>0.

Its exact single-excitation block is [[0,-1/2],[-1/2,1]], matching the primary model on its prepared active scalar sector. With coupling disabled the block is diag(0,1), matching the inactive record sector. Both conserve total excitation number. Define t_model=Omega*t_physical; no physical Omega or apparatus has been calibrated.

The matrix has a negative rotating-frame eigenvalue (1-sqrt(2))/2. A common optical frequency term nu N_total, nu>=Omega*(sqrt(2)-1)/2, makes the two-mode one-particle coefficient positive semidefinite. It is an actual free-resource term, not a fabricated zero-energy vacuum. On fixed N_total=1 it contributes only a common dynamical phase and does not change record populations; relative to optical vacuum or number-superposition states it is not a global scalar and must remain in the energy ledger.

## Exact action and query squares

Let V embed C^2 into the basis (vac,10,01). Then V†V=I, HV=Vh and V†(V A V†)V=A for all Pauli queries and n=(I-Z)/2. Include the vacuum flag along with the two encoded projective outcomes of each analyzer. The effects sum to identity on the three-state space.

For q=h-I/2, q²=I/2. Therefore

    U(t)=exp(-it/2)[cos(t/sqrt(2)) I-i sqrt(2) sin(t/sqrt(2)) q].

The initial |0> has occupation sin²(t/sqrt(2))/2, exactly (1-cos(sqrt(2)t))/4. This reproduces the coherent law that failed the unchanged classical detector-readiness bridge, rather than suppressing it with a reset or classical recovery fit.

The Pauli queries here are mathematical effects. Aspect's Stokes analyzer packet supplies physical-theory readout requirements for a polarization encoding. A path-to-polarization conversion or phase-calibrated dual-rail interferometer is still needed before using those hardware settings for these two modes. Y phase conventions, both outcomes and loss calibration cannot be omitted.

## Loss, postselection and resources

Equal-mode pure loss with transmissivity eta maps a logical encoded density rho to

    eta V rho V†+(1-eta)|vac><vac|.

A complete Kraus implementation includes the no-loss branch and separate lost-mode environment labels. The checker verifies completeness and the erasure identity at eta=0,1/2,1. Vacuum is orthogonal to both logical basis states. Calling loss a reset to |0> would change occupation, resource and preparation semantics.

Unequal mode losses generally distort the surviving qubit; the common-erasure formula is not asserted for them. Conditional survival may reproduce the logical state under equal losses, but success probabilities and environment branches must remain retained. This note is not a detector instrument calibration or a full controller/reservoir energy account.

## Missing controlled source binding

The full conditional reaggregation rules require -g Pi tensor X and -g(c-Pi) tensor X on a native 100-state pair, plus separate matter vacuum. This record-block implementation has no such physical matter encoder or conditional optical control. Selecting the known active scalar input allows the record block to be simulated, but does not construct either full operator on arbitrary matter states. Optical and matter vacuum are distinct typed factors.

Constructed at finite ideal scope: record encoding, generator restriction, Pauli-query map and retained loss flag. Unmatched: full carrier encoding, controlled coupling, named apparatus, calibrated time/coupling/phase/readout, and external preparation/reset resource accounts. The reaggregation physical-admission gate remains open and the classical-memory obstruction remains valid.

Next source obligation: specify a realizable matter-control interface for the two complementary projectors, or explicitly review this as a record-only simulator rather than a physical realization of the whole rule. Do not silently upgrade the block witness into the full 202-state comparison.
