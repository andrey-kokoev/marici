# Recursive interface realization: working approach

**Status:** operator-proposed construction, with bounded geometric probes. Not a derived Pb-208 formation process, a recovered five-stage coding, or a completed native esd7 realization.

## Fixed-cell-size correction

The operator rejected the rendered dilation of boundary cells and compression
of coherence bands. **Existing cells must retain their edge lengths and volumes.**
New space appears by moving cells apart, then must be filled with compatible
fixed-size cells. The earlier homothetic collar probes below are historical PL
experiments, not realizations of this requirement.

The viewer now uses actual esd7 cell coordinates and shared-face incidence.
The central P is the existing regular tetrahedron; its four immediate neighbors
are native octahedral wedges, not reflected regular tetrahedra. Each boundary
identity moves to the opposite congruent wedge in its own octahedron. The
existing source ring order supplies two intervening face-connected cells.
Step 5 assigns them P [N N] E, P [P P] P, P [N E] N, P [N P] N as specified
by the operator. The source ring direction is a display convention, not a
uniqueness or typing theorem. All successive cells share full triangular faces;
there are no arbitrary translations, reflections, or tip-to-tip substitutions.
The fourth wedge of each octahedron remains unfilled. The conceptual interface
recurrence remains a proposal; its earlier scaled rendering is withdrawn.

## Core idea

A realization step need not add an exterior shell. It can expose a retained interface as an explicit coherence layer:

\[
A\mid B\quad\longmapsto\quad A\mid\mathrm{Coh}(A,B)\mid B.
\]

The two earlier layers remain identifiable. Their relation becomes intervening structure. New interfaces can undergo the same operation at the next stage. Here `Coh` names the intended role of the inserted layer; the geometry alone does not prove that it supplies a native coherence witness.

This approach treats growth as **recursive interface expansion**, with attachment rules transported through the change of realization.

## 1. Starting interpretation: retained whole and direction

The dot represents an already completed whole, proposed here to be Pb-208 retained from a previous cycle. At the handoff it is described as having an electron role. This is a representation-relative interpretation, not a claim that a literal isolated electron has been identified with a Pb nucleus.

Its immediate choice is a binary realization direction relative to the observer:

- toward the observer: expose the whole as one typed unit tetrahedral cell;
- away from the observer: expose the retained internal construction, proposed as an edge-length-seven tetrahedral complex with typed cells.

The direction choice is not a choice among five presentations. No five-stage assignment is derived from a pentachoron's five vertices. The spatial language uses the A3 root lattice/FCC setting; it must not be confused with the alternating group A3.

## 2. Current stage sketch

| Working stage | Proposed presentation |
|---|---|
| 0 | Dot/handoff presentation of the retained completed whole |
| 1 | One central typed unit cell, necessarily P in this proposal |
| 2 | Central P with a surrounding **P,E,N,N** quartet, understood as its proto-proton witness |
| 3 | Central P and the retained quartet separated by an inserted coherence layer |
| Next | Both interfaces of the three-layer view become layers, giving five radial layers |

**Revision retained:** the earlier conversation used P,N,E,E around the center. The insertion proposal explicitly revised this to **P,E,N,N**. The latter is the boundary used by the insertion and recursive-layer checkers. The earlier probe remains historical; its inputs have not been silently rewritten.

The operator's local hydrogen/helium readings are interpretations made without the previous cycle's constraints. They do not erase the retained whole or establish literal particle counts. No missing-particle correction is part of this approach.

“Vertex,” “typed cell,” and “boundary carrier” are not yet mechanically identified. The geometric prototype represents the quartet as four tetrahedral caps, not four bare points. Binding those caps to the intended esd7 cells/vertices remains open.

## 3. Two-cycle interpretation

### First cycle: expose the object and its witness

\[
\text{dot (E handoff)}\longrightarrow P
\longrightarrow P\text{ with a }(P,E,N,N)\text{ witness}.
\]

The surrounding quartet is proposed as the proton's proof or proto-proton structure. “Proof” requires a specified judgment and checked witnesses; the quartet's labels alone do not establish it.

### Second cycle: build coherence between retained endpoints

Keep both the central P and the surface quartet. Push the boundary outward to make room for a layer, then grow coherence:

- outward from the central structure;
- inward from the displaced boundary.

The operator describes each of the four boundary vertices as growing three incident edge paths. These give twelve directed paths organized into six tetrahedral edge pairs. Their meeting must retain both histories, not privilege whichever arrives first.

The resulting radial picture is

\[
\text{central P}\mid\text{intermediate coherence}\mid(P,E,N,N)_{\rm surface}.
\]

Thus one inserted cell layer is associated with **two edge-building steps**, one from each side. These are proposed construction steps, not two additional radial cell layers. The probes do not yet implement directed native edge transport.

## 4. Repeat: boundaries become layers

If every interface expands simultaneously and all old radial layers remain, then

\[
L_{n+1}=2L_n-1.
\]

Starting from the three-layer construction gives

\[
3\to5\to9\to17\to\cdots.
\]

The initial **1→3** construction is separate: one isolated layer has no internal interface, so the recurrence cannot generate that step. With the three-layer state indexed by n=0, L_n=2^{n+1}+1.

These numbers count **radial presentation layers**. They are not tetrahedral edge lengths, numbers of particles, numbers of native tetrahedra, or an identification with the seven intervals per esd7 edge. In particular, this recurrence does not select a seven-layer stage.

Each inserted layer should retain:

1. the identity of the old interface;
2. its two endpoint layers;
3. incoming paths and ordered interface data from both sides;
4. the compatibility witnesses for their meeting;
5. the new interfaces available for subsequent expansion.

Items 1–2 and geometric incidence are implemented in the recursive probe. Native data and witnesses in items 3–4 remain open.

## 5. Attachment rules are stage-relative

A fixed particle-adjacency table is not assumed to govern all presentations. A cell's represented structure changes as realization proceeds, so the proposed evolution acts on both state and admissibility:

\[
(S_k,R_k)\longrightarrow(S_{k+1},R_{k+1}).
\]

The operator's stage-2 mnemonic is **“Ps and Es together; Ns together.”** This is not yet a precise face/edge contact predicate. The task is to derive how its meaning transports across an inserted layer, not arbitrarily replace the table at each step.

Important distinction exposed by the insertion test:

- direct **central P–boundary E face contact** can disappear and be replaced by a path;
- **boundary P–E and N–N edge contacts** can remain.

Consequently, insertion does not by itself establish that a general P–E pairing rule has disappeared. The relation, its incidence dimension, and its retained witness must be specified.

## 6. What the experiments establish

### Earlier fixed-rule and edge-first probes

- [Fixed occupied-body rule probe](checkers/check_stage3_type_forcing_probe.mjs): under an explicitly unestablished cell-type-to-particle-role adapter, the old rule rejected the earlier P,N,E,E boundary before stage 3. This does not refute the realization proposal.
- [Six-edge C/M probe](stage3-six-edge-typing-probe-v1.md): shared vertex roles propagated, but P/N/E remained ambiguous because each template has two C and two M vertices. Ordered windows and trajectory transport were omitted. Its face-growth shell also had no remainder after the edge-adjacent cells, so it was not the proposed complete edge-then-layer construction.

These results motivated separating stage-relative realization interfaces from a static occupied-particle compatibility table. They do not prove a rule transformation.

### Inserted-layer geometry

[Checker](checkers/check_stage3_inserted_layer.mjs): a fixed central P, a 12-tetrahedron untyped collar, and four retained P,E,N,N caps. All six seams match. The four direct center–cap face contacts become connecting face paths; boundary pair edge contacts survive.

This prototype dilates the caps rather than moving rigid unit cells. It is a piecewise-linear construction, not an esd7 primitive filling.

### Recursive interface geometry

[Report](recursive-interface-layers-v1.md), [checker](checkers/check_recursive_interface_layers.mjs), [receipt](results/recursive-interface-layers-v1.json).

| Radial layers | Coherence bands | Untyped tetrahedra in bands | Total tetrahedra |
|---|---|---|---|
| 3 | 1 | 12 | 17 |
| 5 | 3 | 36 | 41 |
| 9 | 7 | 84 | 89 |
| 17 | 15 | 180 | 185 |

Checks retain layer identities and interface provenance, consistent face seams, four faces across each consecutive-layer interface, no adjacency shortcuts, fixed center and outer caps, and constant collar volume.

**Metric limitation:** to demonstrate insertion without moving the outer boundary again, this probe compresses/reparameterizes old coherence bands within a fixed envelope. Their identities persist, but their embeddings change. Band widths shrink; there is no assertion of one-unit growth. It supplies neither inserted P/N/E types nor native coherence proofs.

## 7. Next constructive gates

1. **Bind the geometry.** Identify central cell, quartet, layer boundaries and edge paths in the intended native lattice. Distinguish whole FCC cells from subdivision tetrahedra. Specify whether old embeddings move or only their presentations change.
2. **Define one interface expansion.** Give its inputs, output cells, retained identity maps and ordered entry/exit windows. Do not infer typing from unordered C/M counts.
3. **Transport admissibility.** State how old attachments become paths and which new local attachments are licensed. Preserve the old relation as witnessed data where appropriate.
4. **Meet from both sides.** Construct the directed paths from center and boundary; check competing arrivals, six-edge compatibility and face fillers without a first-arrival selector.
5. **Test typing rather than prescribe it.** Count compatible P/N/E assignments after the actual transported constraints are applied: none, one or several.
6. **Check the inverse.** A retained interface genealogy suggests collapsing an inserted layer back to its prior interface. Construct the corresponding typed inverse/witness; do not assume geometric collapse establishes native equivalence.
7. **Bind scale and cycles.** Relate radial layer count, unit length, realization stage and the seven-edge envelope explicitly. The current recurrence is not that binding.

## Interactive view

In [the normal-ray viewer](../realization-tower/normal-ray.html), select
**From center cell — interface expansion**. Steps 0–5 show the dot, central P,
P/E/N/N boundary, native wedge relocation, meeting guides, and eight assigned
arrow cells on actual shared-face routes. Cell sizes remain fixed. The previous seed-first and other processes remain
available with independent saved progress.

The viewer uses `../realization-tower/center-interface-process.mjs`; it no longer
uses the scaled PL collars. Guides illustrate four bidirectional face
channels, not an implementation of the proposed twelve directed edge paths.
Viewer coverage: `tests/center-interface-process.test.mjs` and
`scripts/test-center-interface-process.mjs`.

## Reproduction

```sh
node research/strominger/checkers/check_stage3_inserted_layer.mjs
node research/strominger/checkers/check_recursive_interface_layers.mjs
```

The exploratory process is now displayed in the viewer; native production rules and the maintained net are unchanged.
