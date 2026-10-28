# Executable retained contrast/context packet

**Implemented over the existing native five-slot grammar. No new signed-P/E binding or global wiring admission.** This makes the preceding exact dual-line/context adapter into a replayable packet model.

## Packet contents

Each packet retains:

- the anchored original complex five-vector and native geometric source;
- two current contrast coordinates and three complementary coordinates (active mean plus both outside coefficients);
- the unnormalized paired frame `[z,Jz]` when contrast is nonzero;
- an explicit absent-frame marker when contrast is zero, without discarding nonzero context;
- current geometric aliases, primitive vertices, absolute realization origin and role/index/vertex occurrences;
- the actual native operation history, including shared faces and phase-advance witnesses;
- a co-moving coefficient frame recovering the anchored original five-vector;
- a history commitment checked against replay.

The complement is part of the packet, not a hidden external reservoir. The algebraic decomposition is the existing orthonormal contrast/mean decomposition. The paired column remains derived from the contrast; it is not an additional independent payload or a quantum spin-flip operation.

## Use native execution, not a replacement rule table

`createRetainedContextMachine` uses `GenerativeAssemblyRules` directly. Its choices are exactly the currently admitted outgoing operations. Every step reuses the native face and occurrence validator. No arbitrary phase correction, new inverse NE, or geometry-only path is added.

History descriptors contain geometric and occurrence data rather than relying on transient numeric packet IDs. A serialized packet can therefore be replayed in a fresh rules instance. Restore reconstructs its coefficients and derived fields from the anchored source and actual operation history, then compares the complete record.

Both current and co-moving views remain available. The co-moving coordinates recover the source, but they do not replace the current active reader or assert that context never enters the contrast.

## Concrete tests

- An actual PN followed by N reader advance moves the retained outside-slot input into contrast of norm squared `2/3`, without changing the full norm.
- Two phase advances return the coefficient permutation but retain the different absolute origin and history.
- Even PN followed by its admitted inverse, returning the same native chart and coefficients, retains a different history commitment from the empty path.
- Serialization restores against freshly generated geometry.
- Missing context, edited contrast, wrong origin, changed shared face, corrupted reference-context witness, altered moving frame and inconsistent history erasure are rejected.
- Electron packets admit no inverse-NE or invented phase-correction operation.

The commitment is an integrity/consistency field, not a digital signature. A party constructing an entirely new self-consistent history and commitment has supplied another record; this module does not authenticate that execution or grant authority.

## Verification scope

The checker enumerates all native path words through depth six from one seed marking for seven coefficient seeds: a general complex vector, the five basis vectors and zero. It checks native replay, serialization, full-vector recovery, exact permutation norm preservation and the co-moving source anchor. It does not identify paths just because they have equal endpoint coordinates.

The coefficient permutations retain the supplied numeric coefficients exactly. Contrast/reconstruction uses floating square roots, with a `1e-10` recovery bound; its algebraic all-input identities are checked separately by `check_native_dual_line_context_adapter.py`. Signed numeric zeros are canonicalized for lossless JSON round trips. Nonfinite values and unrepresentable contrast norms are rejected rather than silently serialized as null.

This is not enumeration of all source markings or all five-side oct boundary presentations. Native operation validity on each path is not a theorem that unions of paths form valid simultaneous assemblies. No physical inventory reader is changed.

## Remaining binding

The working packet is **two contrast coordinates plus three context coordinates and retained history**. Identifying that object with the operator's revised signed P/E pair still requires a source map. The window-to-sector/electron interpretation remains conditional; the proton contrast is not automatically a derived physical spinor. Neither a global boundary law nor admissible routes follows from this packet implementation.

## Replay

```sh
node --test tests/retained-context-spinor-packet.test.mjs
node research/strominger/checkers/check_retained_context_spinor_packet.mjs --record
python research/strominger/checkers/check_native_dual_line_context_adapter.py --record
```

Implementation: `retained-context-spinor-packet.mjs`.
Receipt: `results/retained-context-spinor-packet-v1/verification.json`.

Existing native sources and viewer remain unchanged. Both construction and signed-pair admission flags remain false.
