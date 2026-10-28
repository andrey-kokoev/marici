---
author: marici.Voevodsky
title: Joins and Cones as a Candidate Source Space
description: An operator-originated insight identifies join and cone generation as a candidate geometry of the source, relates the four-plane tetrahedron to sections of a four-dimensional cone, and separates lifting a space from shrinking a section.
---

# 4329 — Joins and Cones as a Candidate Source Space

## New understanding

The operator proposed that the underlying space of the source may be understood through **join and cone generation**. The tetrahedron would then be a produced member of a dimensional construction, rather than an unexplained primitive or merely a familiar shape drawn around the source.

The important connection is that the existing four-plane viewer already supplies tetrahedral sections of a cone. A family that looks like a changing three-dimensional space can be treated as sections of one higher-dimensional space. This gives a precise candidate meaning to the intuition of a “space of spaces.” It also exposes a distinction the initial visualization missed: **moving through shrinking sections is not the same operation as lifting the whole cone while retaining its base.**

This entry records the operator's insight as important new conceptual understanding and a source-space hypothesis worth preserving. The elementary geometric identities below are established mathematics. Their identification with the actual WG source, its operations and its witnesses remains a research claim, not a result of the visualization.

## Join unifies the two proposed constructions

Use augmented simplicial complexes, with the empty simplex as the join unit. Successive cones give

$$
\Delta^{-1}\longrightarrow\Delta^0\longrightarrow\Delta^1\longrightarrow\Delta^2\longrightarrow\Delta^3.
$$

Each step adds an apex and joins it to the preceding simplex. Rotation is not part of this operation.

The alternative construction from two segments uses the same framework:

$$
\Delta^p*\Delta^q\cong\Delta^{p+q+1},
\qquad
\Delta^1*\Delta^1\cong\Delta^3,
\qquad
C(X)=X*\Delta^0.
$$

The two-segment join has four vertices, six edges, four triangular faces and one tetrahedral cell. A geometric realization requires four affinely independent endpoints; a particular quarter-turn is a geometric choice, not the join law.

The candidate underlying picture is therefore a decorated simplicial construction generated through joins and witnessed attachments. Its tetrahedral stage is an instance of that construction. This is stronger as a research proposal than recognizing a tetrahedral silhouette, but still requires an explicit connection to the declared source.

## The four-plane model as sections of a four-dimensional cone

Let the four unit normals be the normalizations of

$$
(1,1,1),\quad(-1,-1,1),\quad(-1,1,-1),\quad(1,-1,-1),
$$

and let

$$
T_d=\{x\in\mathbb R^3:n_j\cdot x\le d,\ j=1,\ldots,4\},\qquad d>0.
$$

This is the tetrahedron bounded by the viewer's four supporting planes. Its displayed circular patches are finite visualizations of those planes, not additional constraints on the bounded region.

For a supplied positive height L, form

$$
\mathcal C(x,s)=((1-s)x,Ls),
\qquad x\in T_d,\quad 0\le s\le1.
$$

At fourth coordinate w=Ls, its section is exactly

$$
T_{d(1-s)}.
$$

Thus the viewer's coordinated plane-distance contraction can be interpreted as traversal through the sections of C(T_d), a four-simplex. Four lateral tetrahedral facets are traced by the moving face planes; the starting tetrahedron is the fifth facet.

Equivalently, the full cone is specified by the five facet inequalities

$$
w\ge0,
\qquad
n_j\cdot x+\frac dLw\le d\quad(j=1,\ldots,4).
$$

Summing the last four inequalities gives $w\le L$ because the normals sum to zero. The upper section is the single apex. This is an explicit construction of a higher-dimensional carrier, not just a sequence of unrelated pictures.

## Lifting the space is different from selecting its sections

The first cloned visualization emphasized s. With the fourth coordinate hidden, changing s simply displayed smaller tetrahedra. The operator correctly identified that this did not show the intended formation of the new space.

A more appropriate lift family keeps the base fixed:

$$
F_\lambda(x,s)=((1-s)x,\lambda Ls),
\qquad 0\le\lambda,s\le1.
$$

Here lambda controls the lift, while s independently selects a section. In particular,

$$
F_\lambda(x,0)=(x,0),
\qquad
F_\lambda(x,1)=(0,\lambda L).
$$

Every base point stays fixed as lambda changes; the apex moves in the additional direction. For positive lambda the construction is an affine cone over the same base. At zero lift it degenerates into the original base under the centered convex realization.

A fixed display projection, for example P(x,y,z,w)=(x,y,z+w), gives

$$
P F_\lambda(x,s)=((1-s)x_1,(1-s)x_2,(1-s)x_3+\lambda Ls).
$$

Unlike changing a projection angle, this operator does not foreshorten the original base as the lift changes. Camera rotation is a separate display operation.

Two implementation attempts must remain part of the record: a three-scene simplex sequence was rejected as not representing the intended construction, and the later cone clone was also rejected after correction. The clone, its generated assets, gallery entry and implementation tests were removed at the operator's request. Those rejected displays do not refute the geometric identities, but they are not accepted visual evidence for the proposed source interpretation. The original Vue four-plane viewer remains separate and unchanged.

## Comparison with the actual source

The inspected WG research brief specifies the directed arrows

$$
AB,\ BC,\ CA,\ BA,\ AD,\ DB.
$$

Their supports fit two adjacent tetrahedral faces through the cycles A->B->C->A and B->A->D->B. They do not constitute the full tetrahedral edge set: CD is absent, and AB and BA are separately declared directed arrows. A cycle is not automatically a supplied filling witness.

Consequently, a source-identification argument must explain which decorations, directions and incidences are generated and retained, rather than simply identify the ambient join tetrahedron with the full native source. It must account for the two directed cycles, the absent CD edge, the status of reversed arrows, and the source's actual extension/comparison operations.

Every nonempty filled simplex is contractible. Any explanation of nontrivial source structure must therefore retain the relevant boundaries, directed operations, histories and witnesses; the unmarked filled volume alone cannot distinguish them.

This proposal belongs beside Strominger's current representation-independent tower-cut question. Revision 6 of that contract does not require FCC or tetrahedral presentation. The join/cone proposal is a concrete candidate construction to compare with the source, not a reinstatement of a mandatory geometry or a proof of physical-domain coverage. No automatic research task queue is opened by this entry.

## Durable verification and provenance

- **Origin:** operator proposal and explicit request to record this discussion as important new understanding, in the current Pi conversation on 2026-10-20; synthesis by marici.Voevodsky.
- **Allocation:** sequence `marici-ledger-entry`, value 4329, claim `seqclaim-a4b57a3afefc751c46e5ac14`.
- **Exact checker:** `research/voevodsky/checkers/check_join_cone_source_space.py`.
- **Receipt:** `research/voevodsky/results/join-cone-source-space-v1.json`.
- **Checked scope:** finite augmented-simplex joins, exact affine barycentric identities for the tetrahedral cone, fixed-base/common-apex lift coefficients, and the declared six-arrow incidence distinction. These do not verify native WG generation or physical adequacy.
- **Existing mathematical context:** `research/voevodsky/simplicial-recombination-particle-interactions.md` and `research/voevodsky/a-plane-bearing-coherent-nerve-seed.md`. Neither earlier note already establishes this source-space identification.
- **Source and programme context:** `research/chatgpt/20261019/shoshin_wg_research_brief_v3_20261019.md`; `research/strominger/contracts/marici-tower-cut-domain-net.v1.json` (revision 6 inspected); `research/strominger/canonical-berry-refinement-proof-v1.md`.
- **Retained viewer:** `examples/tetrahedral-planes/`; its geometry is context, not proof that WG has this underlying space. The removed clone is not a live dependency.
- **Epistemic graph:** admitted proposal `ep_54f9749b-b9d8-447e-bcac-e63c93ed06fb`, event `ev-000000016264-1be2a63e-a55e-497e-8835-905f62ddf796` (sequence 16264). The entry and open source-space conjecture were registered, with notices to marici.Strominger and marici.Nima. Admission records provenance and scope, not truth certification.
- **Publication validation:** `pnpm run build` passed locally, including VitePress generation and Pagefind indexing. The numbered filename and heading agree, and no second live entry uses 4329. Files are not committed or deployed.

No new proof-assistant theorem, source-identification proof or physical experiment is claimed. The durable contribution is the join/cone source-space hypothesis, its exact geometric connection to the plane family, and the distinction between lifting a space and traversing its sections.
