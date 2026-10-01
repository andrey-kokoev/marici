# A registered retained-successor interface

## Implemented contract

`checkers/retained_path_successor.py` implements `RetainedSuccessorLedger`, combining the previously separate path, decoding and spectral-summary checks. It is a finite rational coefficient interface, not an execution scheduler or a new higher-cell promotion rule.

It reuses endpoint composition and indexed-family recovery from `check_indexed_path_synthesis.py`. Registration follows the object-identity-bound pattern of `SpectralLedger`: equal-looking copies are not registered records. The existing three-packet triangle constructor and its depth limit are unchanged. Its triangle `ModeIdentity` objects are not silently repurposed as path stages.

## Operations

| Operation | Contract |
|---|---|
|`ledger.root`|Retains the ordered primitive registry.|
|`successor(parent)`|Constructs all admitted one-arrow extensions with full words, parent slots, lift, decoder and final-occurrence summary.|
|`deconstruct(stage)`|Returns the original registry at the root, or the registered parent plus each child's exact prefix/final-edge decomposition.|
|`family(stage, direction)`|Registers a source- or target-indexed family retaining every member.|
|`deconstruct_family(family)`|Recovers words in their original stage order, not arbitrary flattened group order.|
|`transition(ancestor, descendant)`|Returns the composed lift and decoder along that registered ancestor chain.|
|`encode(...)`, `decode(...)`|Copies coefficients forward and decodes only when the input lies in that transition's image.|
|`compose_primitive_payloads(stage, left, right)`|Evaluates the already-declared bilinear coefficient product on a registered direct successor of the primitive root.|
|`split_payload(stage, values)`|Resolves arbitrary non-root path coefficients into decoded parent means and zero-mean sibling detail.|
|`reassemble_payload(stage, parent_values, remainder)`|Reconstructs the path payload, rejecting a remainder outside the sibling-detail kernel.|
|`summarize(stage, values)`|Aggregates by final primitive occurrence for arbitrary stage coefficients.|
|`inherit(stage, name)`|Binds an existing origin spectral descriptor to a registered stage and ordered primitive history window.|
|`read_mode(mode, values)`|Reads an inherited spectral component only for payloads in the origin-lift image.|
|`inherited_projector(mode)`|Returns the explicit factored image-supported projector, with its scope documented.|

Coefficient inputs are exact rationals. Spectral descriptors and outputs use pairs of rational matrices/vectors in their declared quadratic fields. This implementation does not claim an arbitrary complex-payload API, despite the earlier independent complex linear reconstruction tests.

## Three domains remain distinct

For stage n, write L_n for its composite origin lift, D_n for its decoder, A_n for final-occurrence aggregation, and E_lambda for an original occurrence eigenprojector.

The inherited projector is

    E_lambda,n = L_n E_lambda D_n.

Its complete family includes the original rank-two zero sector. Exact tests show

    sum_lambda E_lambda,n = L_n D_n,
    sum_lambda lambda E_lambda,n = L_n K D_n.

Beyond the root, L_n D_n is an IMAGE projector, not the identity on the ambient path space. The second equation represents the origin K action transported onto that image, not a new physical evolution law on all path coefficients.

For one-step extension J_n,

    E_lambda,n+1 J_n = J_n E_lambda,n,
    A_n L_n = K^(n-1).

Inherited spectral labels therefore remain compatible with retained extension and the coarse summary. No independent phase advancement is inserted during extension.

An arbitrary ten-path preparation need not come from the six primitive coefficients. It CAN be extended to later stages and decoded back to the ten-path preparation. It CANNOT be passed off as a six-input inherited spectral payload. The API rejects that operation before returning a mode reading.

## Provenance and hostile controls

The integration checker verifies:

- Registered stages at word lengths 1, 2, 3 and 4, with 6, 10, 16 and 26 words.
- Source/target family recovery in the original ordered carrier.
- Exact parent-prefix/final-edge reconstruction.
- Composition of both lifts and decoders for every tested ancestor triple.
- Spectral image completeness, extension intertwining and coarse reconstruction.
- Survival of the zero-sector contrast in path records even when its summary vanishes.
- Rejection of substituted stage/family/mode records, foreign-ledger records and false ancestor chains.
- Rejection of missing spectral sectors, incorrect eigenvalues, unknown mode/index requests, wrong coefficient dimensions, float payloads and off-origin spectral requests.
- Rejection of duplicate primitive IDs and extensions that would silently drop a parent at a sink.
- Lossless treatment of distinct parallel primitive occurrences sharing endpoints, because full IDs and words remain retained.

These checks concern the registered in-process interface, not security against arbitrary mutation of Python internals or external graph authority.

## Verification

    python research/nima/checkers/check_retained_path_successor.py

The fresh integration run also invokes the preceding whole-seed checker, which reruns the vertex spectrum, six-occurrence bridge, observation audit and retained-extension squares through word length six. All pass.

Report: `results/retained-path-successor-interface.json`.

## Branch-comparison extension

`retained-branch-comparison-synthesis.md` audits the complement to the unchanged-copy image. The first successor has four sibling-detail directions, coarse rank two, and a two-dimensional hidden detail kernel distinct from the original K-zero sector. The new split/reassemble operations retain arbitrary supplied detail instead of treating a lossy projection as decoding.

Through word length six, independently transported origin/detail bases give full-rank ancestry reconstruction with dimensions 68=6+4+6+10+16+26. Unchanged copying introduces zero new detail. These are comparison coordinates relative to the existing averaging decoder, not independently generated amplitudes or a new ambient spectrum.

Fresh verification: `python research/nima/checkers/check_retained_branch_comparisons.py`, followed by the integration checker above.

## Bilinear input preparation scope

`bilinear-branch-preparation-synthesis.md` now characterizes the existing B(x,y) coefficient rule through the interface. It reaches any four pure sibling-detail coordinates with one supplied signed input pair, whereas a complete single-product ten-word output satisfies two rank-one block conditions (generic dimension eight; linear span ten). Parent means and detail are therefore not jointly arbitrary in one product.

Final-occurrence aggregation obeys A B(x,y)=diag(y)Kx, so a left K-zero input stays coarse-invisible for every right input even when its retained branch detail is nonzero. The preparation claim is algebraic reachability for supplied rational inputs, not physical input authority.

Fresh checker: `python research/nima/checkers/check_bilinear_branch_preparation.py`.

## Arbitrary retained-family composition

`retained-path-family-composition-synthesis.md` adds registered `WeightedPathFamily` records distinct from unchanged-copy stages. The ledger now registers arbitrary supplied homogeneous path payloads, composes endpoint-compatible families, deconstructs exact operand bindings, exposes assembly trees and audits single-product constraints at a specified cut. The primitive coefficient API delegates to this general composition rule.

Both bracketings of a three-family product have equal weighted words but retain different recoverable assembly records. Checks cover all 216 primitive basis triples, mixed lengths through six, and all five four-input bracketings. Composition with an all-ones primitive right family recovers the copy successor exactly. Empty composition differs from nonempty zero-valued words; parallel IDs and rank-two intermediate preparations remain explicit.

These weighted records do not acquire origin-image spectral authority or copy-stage injectivity merely by being registered. Parent recovery uses stored operands rather than inversion of bilinear multiplication.

Fresh checker: `python research/nima/checkers/check_retained_path_family_composition.py`.

## Structural result

The model now exposes one coherent contract for **retained construction, inherited spectral representation and coarse observation**, without identifying them. It remains a finite mathematical interface. Neither physical execution, measurement authority, an ambient spectral successor nor a realized higher-cell constructor follows from registration alone.
