# Candidate central-N reference completion

## Constructed, not recovered

Implemented a concrete proposed information-level operation that selects the E+ or E- reference for the P+/P- comparison **at the central N**. This uses the complete-core pattern found in prior research. It does not add a physical signal transition, a DG witness, a native comparison-compiler adapter, or a simplicial filler.

Implementation: `su32-central-reference-completion.mjs`.

The original native geometry and `su32-layer4-comparison.mjs` are unchanged.

## Domain and state

Preparation requires both actual candidate reconciliation trees `byE` and `byP`, at the same occurrence and binding. Both must validate, use the appropriate shared-reference roles, and contain the same complete record entries, including their original reference cells and payloads.

The retained core contains:

- the central N and complete occurrence anchor;
- all four independent labelled record entries;
- both supplied reconciliation derivations, unchanged.

The selected view contains:

- the active P+/P- pair;
- the chosen E record and its original reference cell;
- the other E record as retained complement;
- the actual previously supplied comparison tree for that E context;
- the current central-N location.

These are not claims that both derivations were physically executed. They are the supplied construction records required by this candidate interface. The core is sufficient, not proved storage-minimal.

**Three locations remain distinct:** current central N, the original layer-4 comparison cell, and the layer-2 reference cell. Selecting E- does not teleport the current packet to either of the latter cells.

## Operation and laws

Given a valid packet and a requested reference E+ or E-, the operation:

1. validates the complete packet and its retained ancestry;
2. snapshots the prior packet as an immutable parent;
3. retains exactly the same complete core;
4. derives the requested contextual view from that core;
5. records the selection, from/to reference labels and unchanged central location.

No external registry, new payload or independently supplied target view is accepted.

Write `V_r(C)` for the deterministic view of complete core C at reference r. Ignoring no information, but distinguishing current state from retained selection history, the update is

```
(C, r, V_r(C)) -> (C, s, V_s(C)).
```

Consequently direct and staged selections ending at t have the same current state. Returning to r restores the original current state. The entire packets are NOT equated: direct, staged, identity-request and round-trip histories remain different immutable records. Every step retains its exact predecessor, recoverable by parent projection.

The P+/P- reader is unchanged by selection. The E-context reader changes as requested. Requiring equality of the entire contextual view would incorrectly forbid the intended operation.

This is a deterministic choice of active reference, not Nima's DG reanchoring formula: Su-32 still lacks the latter's differential and reference-change witnesses. Those structures are not silently inferred from record labels.

## Attachment contract checked, not a continuation invented

The current boundary reader remains the same central-N occurrence under every selection. Its four outgoing geometric shared-face interfaces, obtained from the actual fixed-reading comparison domain, also remain unchanged.

That proves location/menu preservation for this candidate. It does **not** supply a payload map along any interface, permit attachment from the old reference cell, or prove compatibility with a future physical operation. The original outer branches and the missing middle/outgoing law are not replaced by this central packet.

## Refusal and falsification controls

The operation rejects an isolated layer-4 ternary comparison instead of manufacturing its missing E record.

This precondition is information-theoretically necessary for the declared task: two complete preparations can have identical full E+-referenced comparison trees while differing only in E-. Their required E--referenced views differ. No function of that isolated E+ tree can produce both required answers. A richer retained context is needed; the complete core is one explicit sufficient choice.

Other controls reject missing complement data, altered readers or derivations, changed occurrence binding, a wrong current location, wrong route typing, false transition metadata, a parent with a different core, cyclic ancestry, and an unsupported P-reference selection.

The API snapshots mutable caller data before retaining it; it neither freezes the caller's object nor lets later mutations alter the retained parent.

## Verification

Fresh headless replay passed:

- **68 preparations:** four sign bindings × sixteen Boolean registries plus one tagged registry;
- **544 direct/staged composition checks**;
- **272 current-state round trips**;
- **272 attachment-boundary checks**;
- **4 consistent P/E sign-relabelling controls** preserving actual reference cells and payloads;
- **12 rejected malformed/unsupported cases**;
- the identical-source-view/different-required-target counterexample;
- immutable input and parent-snapshot checks.

The general identity/composition argument follows from deriving every view from the unchanged core; the finite cases exercise its implementation. They do not exhaust arbitrary JSON payloads or all possible process continuations.

The existing layer-4 comparison checker also passed its 2,304-case regression.

```
node research/strominger/checkers/check_su32_central_reference_completion.mjs
node research/strominger/checkers/check_su32_layer4_comparison.mjs
```

Receipt: `results/su32-central-reference-completion-v1/verification.json`, including complete initial/changed packets, actual outgoing geometric sites and source hashes.

## What this teaches

There is a consistent conservative completion: changing the active comparison reference need not transform the four records or erase their derivations. Its essential availability condition is explicit and falsifiable.

The reference-selection policy is supplied by the caller. No native dynamics chooses when to select E+ or E-. No nontrivial loop action on the current complete core is produced; round trips retain history but restore current data.

This advances from a missing-operation audit to an executable candidate. It does not prove that Su-32 implements the candidate, close the native higher-filler conjecture, determine the forty middle pair assignments, or establish K(Z,2) structure.
