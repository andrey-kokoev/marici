# An exact ideal passive network for the full-state extraction

## Fresh construction

The normalized260-coordinate exchange now has a concrete ideal mode-network factorization. It does not rely merely on the existence of some orthogonal matrix decomposition.

The actual source-derived joint reader D has four rows with disjoint supports of64 bank coordinates each. Every nonzero coefficient is+1/8 or-1/8.

For each support, retain its source sign pattern, then use a normalized64-mode Walsh/Hadamard router. Its first output is exactly that row's readable supermode. Complete routing keeps all252 complement modes.

Swap those four outputs with the four carrier ports, then unroute the complete bank.

## Exact operator identity

Let Q be the full256-mode router, with first four rows equal to D. Let S swap the four readable bank outputs with the carrier. Then

    E=diag(I4,Q^T) S diag(I4,Q).

The checker verifies every one of the260 operator columns equals the previously constructed full-state exchange. The same252-dimensional kernel is retained. It is not initialized to vacuum or discarded after routing.

The ideal real orthogonal matrix also defines a unitary amplitude map on complex modes, but no laboratory device or source-generated physical mode encoding is claimed.

## Primitive network proposal

Each64-mode router uses six stages of32 independent balanced two-mode couplers. Each stage is the normalized H2 transformation. Across six layers its coefficient denominator is exactly8, so the composed router can be verified with rational arithmetic.

The full unoptimized proposal uses:

- four64-mode router blocks;
-768 balanced couplers per router pass;
- two passes (routing and inverse routing):1536 balanced couplers;
- four carrier/readable-bank swaps;
-112 source-sign phases per pass,224 total;
- explicit wiring permutations and all complement outputs retained.

These are implementation counts, not an intrinsic minimum, physical mass, clock period or resource-cost theorem. Phases/wiring may be optimized under another explicitly specified plant.

A negative control omits a required source sign while keeping the selected readout port fixed. It changes the extracted supermode; such signs cannot be erased as a harmless coordinate choice.

## Preparation and response boundaries remain

The router accepts a PREPARED256-coordinate joint bank and four carrier amplitudes. It does not create that bank from two separate inputs, establish their correlations, or normalize their physical resources.

The extracted carrier is the NORMALIZED joint response D t. Recovering the earlier raw comparison response still uses its explicit observation conversion matrix(4*carrier). That conversion is not a conservative amplification of the output state and requires a specified detector/calibration interpretation.

This ideal proposal is not an identification with the prior lossy cavity plant. `research/nima/optical-plant-endpoint-exchange.md` already shows that the frozen lossy plant is not an exchange and that phases alone cannot repair its missing singular value.

Nor does its four-port calibration certificate automatically certify this260-mode network. The complete new routers, swaps, delays, environment and reference phases need their own evidence.

## Apparatus information now needed

The proposal makes the experimental boundary concrete:

1. joint input preparation and common energy/amplitude normalization of all260 ports;
2. independent complex transfer calibration of all router and swap paths, including inactive outputs;
3. required sign phases, storage and event delays, with uncertainty and calibration-validity intervals;
4. detector convention for the raw response conversion;
5. explicit retained environment versus reset/degradation policy.

Ideal balanced couplers and lossless swaps are declared theoretical controls. No source operation or measurement provided here proves that an apparatus realizes them. Hardware data cannot be replaced with self-generated synthetic evidence IDs.

## Verification

    uv run research/strominger/checkers/check_passive_joint_bank_network.py

1306 exact checks pass. They cover source supports/signs, balanced-layer wiring and norm identity, all256 router inverses/readouts, all260 full-state operator columns, complement retention and the missing-sign hostile. The previous full-state extraction and response/reference chains are rerun as dependencies.

No new Agda closure, empirical calibration, apparatus claim or physical-source admission is made.

Artifacts:

- `research/strominger/checkers/passive_joint_bank_network.py`
- `research/strominger/checkers/check_passive_joint_bank_network.py`
- `research/strominger/results/passive-joint-bank-network.json`

The result contains full source routing groups and layer-pair wiring for reproduction.
