# Source resolution and replay contract

## What is checked

Validation has two distinct stages: SHACL checks record structure; application code then resolves local source files and replays supported derivations. File I/O and replay are not SHACL inference. A source-stage failure has its own error code and application constraint marker, and cannot be reported as overall conformance.

Concrete records must carry explicit registered types; inherited class membership alone is insufficient. This matters because SHACL class checks recognize subclass relationships even without materializing inference, while application readers enumerate explicit types. The source helper also refuses referenced sources without an explicit Source type. The production checker compares the entire supplied shape graph against the local authoritative bundle before validation; retaining shape names while deleting constraints is rejected.

Every Source reference resolves to a file within the supplied repository root. Absolute paths, traversal, URLs, backslashes and paths resolving outside that root are rejected. Reads are bounded to 4 MiB. Fixture/operator-input references are reported as `reference-resolved-not-derived`; the observed digest is not a pin or proof of their claims.

A derived-input source must declare an InputArtifact (repository-relative path plus SHA-256), operation, record selector, and output structure. Input bytes must match the pin. The source reference must agree with the artifact path. Only an allowlisted operation runs; input data never supplies executable code. Every output triple on the replayed source-owned subjects, including nominal occurrence identities and source/operation metadata, must match replay. A matching digest or matching counts alone is insufficient.

Receipts additionally report evidence per structure root. Only the exact output root of a replay receives `root_evidence: operation-replayed`; a separately attributed wrapper does not inherit it by referencing the same nucleus. Reachable record sources and shared records are disclosed. Sharing is not prohibited, and incoming references from other records are not asserted to be operation outputs. See `SOURCE-SCOPE.md`.

## ReferenceNuclearInventoryV1

Actual inspected input: `research/matter/isotope-reference.resource.json`, the existing tabular reference resource. Select exactly one row by isotope name using schema field names. Project only `isotope`, `protons`, and `neutrons`; require integer counts, positive Z, nonnegative N and agreement of Z+N with the mass label. Allocate deterministic nominal slots for those counts, a nucleus, and an InventoryProfile/NoBindings root. These slot IRIs are not measured identities of physical particles.

Electronic state, shell assignments, arrows, cells and geometric layout are NOT inferred. Other columns remain available in the pinned source artifact but are not represented as computed facts by this operation. A 1,000-constituent allocation limit is a software budget, not a physical law.

The operation is reproducible from the input bytes, selector, operation version and declared output namespace. It does not revalidate the repository's HTML extraction, fetch NIST/IAEA, certify physical data, or generate the native isotope diagram. The source itself expressly disclaims independent upstream revalidation.

## Why this input, and the remaining boundary

The existing neutron real/complex arrow source supplies endpoint geometry but no isotope inventory or color assignment. The isotope-obstruction protocol describes fixed-footprint experiments, not a complete source record for the current Ne-20 drawing. Neither can authorize reconstructing that drawing from counts. The reference inventory is therefore imported only as an inventory, not promoted to a complete diagram.

The structural schema and complete authored fixtures remain separately usable. A complete spatial isotope diagram still needs its own source correspondence; neither operation supplies it.

## NativeReaderIncidenceV1

Iteration 8 adds a second allowlisted operation for the saved Ne-22 D4 finite-reader witness. It requires both the witness artifact and an explicit `dependencyArtifact` pin for the native manifest. A fixed read-only Node checker verifies the declared dependency set and input digest, freshly regenerates/replays the native constructor, and checks occupied contacts and exit reachability. Its returned witness/manifest digests must agree with the bytes observed by the Python verifier.

The projection retains reader IDs, origins, chart/body assignments and directed operation IDs/endpoints/kinds/deltas as typed records. It is PartialStructureProfile with TotalBindings, not a complete spatial structure. Reader states and transitions are separate types from spatial vertices and colored arrows. Source replay compares the exact outgoing projected triples, as for the inventory operation. See `NATIVE-REPLAY.md` for omitted fields, the field mapping, runtime requirements and evidence. Raw saved pass flags, a count match, or successful serialization alone do not qualify.
