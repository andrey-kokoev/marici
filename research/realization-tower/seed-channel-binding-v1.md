# Four-channel source binding: paths, retained returns, and the missing face

## The question tested

Bind the proposed inner/outer four-channel construction to an actual source,
not a prefilled honeycomb or already assigned isotope. The source here is
`research/nima/agda/ActualSeedEndpointTable.agda`. This is an explicit candidate
binding, not an assumption that its four vertices already are four physical
transport ports.

The executable reads the source's Vertex, Occurrence, source and target clauses.
It does not replace primitive occurrences by the edges of a complete tetrahedron.

| Occurrence | Source | Target |
| --- | --- | --- |
| AB | A | B |
| BC | B | C |
| CA | C | A |
| AD | A | D |
| DB | D | B |
| BA | B | A |

AB and BA are distinct supplied occurrences. Reversing the presentation of AB
retains its label; it does not turn it into the primitive BA.

## 1. What four channels can mean here

The raw source and target fibres over A,B,C,D have sizes 2,2,1,1. There is no
vertex with four primitive outgoing arrows. With the selected root A, grouping
its direct arrows by the four possible targets gives sizes 0,1,0,1.

Thus **four vertices do not give four primitive outgoing ports** in this table.
This rejects that particular binding, not the general four-channel hypothesis.

An explicit alternative is the free-path completion. Include an identity path
and all composable occurrence words, retaining every occurrence and its order.
Define

    F_A(v) = directed paths from A to v.

Now the four target-indexed families are all inhabited: identity at A, AB at B,
AB;BC at C, and AD at D. This follows from the source graph, after declaring the
path/identity constructor. It is not ordinary regrouping of the original six
rows, nor proof that these are the four geometric transport channels.

The bounded executable lists every directed word of length <=3. Fibre sizes
are 4,3,2,2. The bound is only an inspection window; walks and return histories
are unbounded. No shortest-path representative is selected.

The original table is endpoint-pair unique. The path table is not: AB and AD;DB
already give different A-to-B records. The generic homotopy-fibre construction
allows that multiplicity, but an interface demanding endpoint-pair uniqueness
cannot consume this table unchanged. It must either retain a richer endpoint/
port address or explicitly accept multiple histories. Silently deduplicating
by endpoints would erase exactly the comparison we are investigating.

## 2. The first nontrivial comparison boundary

Use actual parallel paths

    p = AD ; DB : A -> B
    q = AB      : A -> B.

The existing source question asks for the face p=q. Instead of inserting that
face, form and retain the based return

    h = p ; q^-1 : A -> A.

Here q^-1 is formal path reversal in the free graph realization, NOT the
independent native occurrence BA and NOT a newly admitted reverse execution.
The signed word AD,DB,AB^-1 is freely reduced and nonempty. Exchanging p and q
inverts h exactly. This constructs a comparison boundary and its reversal;
it does not contract that boundary or provide a 2-cell filling it.

This is a sharper reading of the proposed round trip: **a return can encode a
nonzero discrepancy between two routes**, not only a path followed by its own
inverse. The latter cancels and cannot supply this distinction on its own.
No physical neutral-particle identification is made here.

## 3. Existing formal obstruction, with a source-bound executable probe

`SeedFaceObstruction.agda` already constructs a Boolean family over the actual
free realization: AB flips the fibre, all other primitive occurrences preserve
it. Its theorem `no-forward-face` rejects p=q; `no-abc-face` rejects AB;BC=CA^-1.
Those are proofs about the fixed free interpretation, not a prohibition on
all possible richer interpretations.

The new executable reproduces the diagnostic transport values:

    q(false) = true
    p(false) = false
    h(false) = true.

All 64 assignments of preserve/flip to the six occurrences are allowed by bare
incidence. Exactly 32 satisfy the forward-face transport equation, 32 satisfy
the ABC equation, and 16 satisfy both. Thus imposing both flatness equations
removes otherwise allowed probe interpretations. These are finite model counts,
not probabilities, particle counts or a uniqueness theorem for richer fillings.

The same probe separates formal inverse AB from primitive BA: inverse AB flips,
BA preserves. Naming a reversed edge by the opposite endpoint pair is unsound.

## 4. An important distinction about the existing Filler constructor

`BoundaryGeneratedQuestions.Filler a b` retains an equivalence of the underlying
carriers and a witness that it maps the selected value of a to that of b.
It is NOT the same type as equality of the two paths in the free realization.

For the Boolean diagnostic, a flip corrects the mismatch between p(false) and
q(false). Such a pointed equivalence is available at this small coefficient
level. It does not construct the missing geometric face: the formal no-face
result still applies. Likewise a computed correction S_q S_p^-1 between two
invertible transport matrices closes their coefficient comparison by algebra;
without independent restrictions on admissible comparison operations, this
cannot select an assembly law.

Therefore there are three distinct retained objects:

1. a pair of parallel histories and their return word;
2. a representation-level comparison of their effects;
3. an actual source-level face or higher comparison witnessing an admitted
   reconciliation.

The first is constructed here. The diagnostic second is computed. The third
is not silently supplied. Promotion requiring a completed comparison cannot
be invoked merely because its endpoints match or a correction matrix exists.

## Disposition: the specific hard boundary

The source permits a four-endpoint path-family interpretation and generates
nontrivial return boundaries. It does not force the flat faces needed by the
previous filled-tetrahedron fixture. Nor does regrouping generate new rows.

This leaves a sharply stated choice for the proposed assembly law:

- enrich the source by a justified face/comparison constructor; or
- retain nontrivial return discrepancies as data and give a source-derived
  rule for their composition and realization.

An arbitrary correction fitted to each observed mismatch is not that rule.
Neither is declaring the entire honeycomb filled in advance. Any proposed
constructor must state which extra comparisons it admits, preserve occurrence
identity and channel addressing, and explain how those comparisons change the
next construction. The existing comparison-promotion machinery can then be
used on actual admitted inputs rather than unrelated filled fixtures.

No viewer/filling rule, particle assignment, Agda source, source admission or
research graph outcome has been changed.

## Reproduction and scope

    node --test tests/seed-channel-binding.test.mjs
    node research/realization-tower/check_seed_channel_binding.mjs

Three test groups pass: actual table/path binding, occurrence-preserving
reversal, and parallel-route/Boolean obstruction controls. Receipt:
`results/seed-channel-binding-v1.json`. It retains source hash, both endpoint
groupings, all bounded path records, comparison words and probe results.
The existing Agda definitions/proofs were inspected and hashed, not freshly
compiled. This executable is not a replacement for their formal proofs.
