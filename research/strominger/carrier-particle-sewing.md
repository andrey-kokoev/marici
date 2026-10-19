# Carrier sewing: coupling constrained by a shared boundary

## Question, claim boundary, disposition

How far can the P/N/E paths constrain a coupling, rather than having an arbitrary
four-by-four matrix attached to their ports?

**Disposition:** 96 exact checks pass: 52 baseline controls and 44 sewing
controls, including four evaluated-composite SCC cells and a deliberate cell
corruption. Source-derived C boundaries and explicit faithful boundary spans
construct the predicted restriction and reconstructible residual. This extends
[the initial circuit model](carrier-particle-circuits.md) without changing its
source words, fixture, receipt, or viewer geometry.

The proposed constraint is literal boundary sharing: graph carriers are glued by
a pushout; compatible assignments form a pullback. This is a formal operation,
not a physical bond, evolution, stability law, or unchanged-state claim about
repeated occurrences of C1.

## Frozen source enlargement

The source remains P=C0->M0->C1, N=M0->C1->M1, E=M1->C1->C2.
Under the declared graph-source/sink boundary convention, the H=P+E and D=P+N+E
templates each have one nonisolated C source, C0, and one C sink, C2. These C
ports are now computed from primitive edges rather than selected by a supplied
matrix. The neutron changes an internal return core, not those C boundary ports.

New supplied data, frozen in `inputs/carrier-particle-sewing-v1.json`:

- Interpret the previous binary basis as indicator functions on S={0,1}, so
  V=Q^S. This boundary-function interpretation is a declared representation,
  not inferred from the C/M names.
- A seam identifies one derived C output with another template's derived C input.
- Both endpoints refer to one simultaneous boundary-evaluation context.
- Explicit bijections rho_left,rho_right map their value labels to the common S.
  Equal carrier kind or dimension does not supply these maps.

Graph sharing alone does NOT select those value correspondences. Deleting a map
or the common context must block construction. Noninjective observation maps are
not admitted as identification of the complete retained carrier.

Prospective graph proposal: `ep_a96ff2ae-0a7f-415a-a457-2ec5ac6e927e`, recorded
2026-10-15T20:36:45Z, addresses the existing operator stimulus
`maricioperator_stimulus:8d9165926dce3408c967`. The operator's "do" continues that
objective; it is not new evidence.

## The forced state-matching map

For fixed faithful restrictions, compatible assignments are exactly

    F={(i,j): rho_left(i)=rho_right(j)}.

Each common value s labels exactly one pair in F, making s a faithful coordinate
on this pullback. Define R by restricting a joint boundary function to F, and E
by extension by zero to all four assignments. For identity value maps:

    R = [[1,0,0,0],       E = [[1,0],
         [0,0,0,1]]            [0,0],
                               [0,0],
                               [0,1]]

Then RE=I2 and P=ER=diag(1,0,0,1). The domain compatible with the seam is im(E),
not arbitrary Q^4. Incompatible assignments are not declared physically null.
For arbitrary ambient v, retain the full packet

    (Rv, Nv),  N=I4-ER;   v=E(Rv)+Nv.

This is exact reconstruction; restriction alone would lose the mismatch data.
The compatible extension of the constant joint function is (1,0,0,1), which is
non-product as a two-factor coefficient vector. It describes a compatibility
relation, not a dynamical preparation procedure. Also E(1,1) is NOT the tensor
square (1,1) tensor (1,1): copying an index does not copy an arbitrary vector.

P has rank two, unlike every invertible sign-only box in the previous search.
Consequently the earlier norm-preserving diagonal-sign class does not contain
literal shared-boundary restriction. No sign is fitted to produce this result.

## Component-preserving assembly and static coherence

For two named H templates A and B, the derived directed cross-template seam
candidates are A.C2~B.C0 and B.C2~A.C0. Test all four subsets: none, each single
seam, and both. Keep the original particle instance IDs, ordered occurrence
walks, primitive sharing and complete quotient fibres.

The predicted graph vertex counts are 10,9,9,8. Each single seam connects the
templates without closing a directed cycle. Both create a six-vertex directed
return cycle; gluing identifies vertices and does not add two extra wire edges.
No feedback operator or stability property follows from that graph cycle.

Two independent binary seams restrict Q^16 to a four-dimensional compatible
subspace. Retain its twelve-dimensional mismatch residual. The shared-plus-
residual encoding has 20 displayed coordinates but rank 16; it introduces no
extra independent source degrees of freedom.

The checker verifies graph-gluing order, the two restriction orders, full packet
reconstruction, and simultaneous common-value relabelling. It generates an SCC
categorical diagram from the complete computed maps. Map tokens are hashes of
those evaluated maps, not invented equality labels for distinct primitive words.
SCC's token compiler checks these realized composites; the owner checker supplies
the exact matrix/finite-function equality witnesses. No higher word coherence
or native representation equivalence is promoted.

## Issue-boundary DPC

1. **Problem:** an unconstrained external box did not explain how shared P/N/E
   carriers constrain an interaction.
2. **Bold conjecture:** graph-derived ports plus an explicit faithful common-
   boundary span force a reconstructible compatibility restriction, outside the
   old invertible sign class; independent seam orders cohere exactly.
3. **Named rivals:** C-label equality implies state equality; an arbitrary old
   sign box implements sharing; restriction is lossless on every ambient input;
   graph gluing recovers instance counts without provenance; basis dimension
   equality repairs missing restriction maps.
4. **Risky consequences:** four graph-gluing cases retain four instances;
   canonical equality has rank-two P, RE=I and a nonzero mismatch kernel;
   all four bijective binary spans transport the same law with explicit value
   permutations. Among all 16 unrestricted map pairs, pullback cardinalities
   differ, so faithfulness cannot be silently omitted.
5. **Strongest falsification:** compare identical graph gluing with identity and
   twisted value restrictions. Their masks differ; deletion of either map must
   block. Corrupt one evaluated restriction composite and require SCC to fail
   exactly that cell with rank-one numerical residual. Preserve every ambient
   coordinate via the mismatch packet rather than weakening the admissible
   domain until a readout agrees.
6. **Disposition:** survives the stated tests in
   `structured_command_execution:e_28364_1792096846538103700_213`. All four graph
   cases preserve two P and two E instances; the complete 16-span census has
   pullback cardinalities 0 in two cases, 2 in twelve, and 4 in two. Exactly four
   spans are faithful binary identifications, all with two retained assignments
   and explicit value transports. The corrupted cell has numerical residual
   rank one and fails only the predicted restriction-order cell. The derived
   part is eligible C endpoints and sewing conditional on the declared span.
   P/N/E incidence still does not select a partner, seam, value identification,
   native interior operator, or binding/stability law. Those remain missing
   constructors; no waiting-only successor is opened.

## Reproduce

    python research/aspect/scc/scc.py check carrier-particle-sewing-v1 --verbose
    python research/aspect/scc/scc.py categorical research/strominger/contracts/carrier-particle-sewing-v1.json

The checker is standard-library Python with exact rational arithmetic. It reuses
all 52 original controls in memory without rewriting the original receipt.
New receipt: `results/carrier-particle-sewing/verification.json`. Generated
finite diagram: `contracts/carrier-particle-sewing-v1.json`. Original checker,
fixture, viewer words, SCC compiler and new source files are hash-pinned.

Pre-test optionality: four graph seam subsets, four admissible bijective binary
spans, sixteen general spans as hostile controls; no selected bond. Post-test
snapshot before user-facing synthesis: all four assembly choices retained; only
four of sixteen value spans admitted as faithful identifications; 96/96 checks;
four exact static cells; one deliberate rank-one coherence failure; compatible
source dimensions 4->2 for one seam and 16->4 for two, with residual dimensions
2 and 12 retained rather than discarded. The missing source-selection and native
operator data are unchanged. No composite activation/confidence score is inferred.

The relevant obligation is forward realization followed by exact static route
coherence. The global SCC models inspection returned nonzero; no unrelated owner
model is repaired or used as a truth certificate. The owner-local model passes
independently.
