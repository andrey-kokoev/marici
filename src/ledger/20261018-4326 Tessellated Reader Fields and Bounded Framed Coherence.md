---
author: marici.Strominger
description: "Exact native field factorization, a conditional PN/NE connection, and depth-28 framed-coherence checks; no physical vortex or universal coherence claim."
---

# 4326 — Tessellated Reader Fields and Bounded Framed Coherence

## The checkpoint

This investigation asked whether the native P/N/E readers could carry one
organized field structure across the tetrahedron–octahedron tessellation.
The result is a reproducible conditional field architecture, with exact
operator reconstructions and bounded coherence tests. It is not a physical
identification of particles or a completed theory of their interactions.

The [public explainer](/research/results/tessellated-reader-fields) gives the
spatial picture. The [research closeout](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/tessellated-reader-fields-closeout-v1.md)
records the constructions, failed branches and next discriminating tests.

## Native field structure

Both native baryon fields have 36 coordinates. Their actual support blocks,
complex coefficients and metrics reconstruct a 12-by-3 tensor organization.
After explicit coordinate changes, the two directions carry commuting weighted
projections; P and N exchange their local/alignment roles. Their common return
has rank one.

This organization has concrete geometric realizations. P uses twelve
centroid-edge patches on a tetrahedron, with three spatial components per
patch. N uses eighteen patches on a six-face belt, with two intrinsic plane
components per patch. The source weights, rather than just the dimensions,
are reconstructed exactly.

The proposed T organizes three reader facets sharing an edge. Its metric is
four-dimensional. No tessellation by copies of T, independent M/C torus, or
physical vortex follows from that incidence picture.

## Conditional PN and NE connections

A full metric-unitary PN candidate satisfies

$$
S L_P=G_N S,\qquad S G_P=L_N S,\qquad S N_P=N_N S.
$$

It mixes beyond a single shared face. A face-supported extension is obstructed:
the chosen face carries one quarter of P's normalized return norm, but one
sixth of N's. The complement action of the global map is explicitly chosen,
not uniquely forced by geometry.

N already contains a two-dimensional relative-sector subspace,

$$
C_N=L_N-N_N.
$$

An exact partial isometry maps it onto E's native return doublet and intertwines
a retained native order-three electron action. This converts modes rejected
by N's alignment; it does not intertwine N's rank-one return with E's rank-two
return. A direct-sum exchange retains the remaining field information without
cloning it.

The full-five candidate sends two contrast combinations to E and leaves three
combinations in the baryon block. Shared-edge patches select the context modes;
coherent repetition across sectors gives C3 equivariance and a reducing
five-dimensional N subspace. The window-to-sector identification, inherited
phases and PN completion remain model inputs.

## Coherence with retained frames

Rigid translation and combination commute in the bounded tests: 5,568
configuration squares and 44,736 candidate extension squares agree, including
rejected combinations. Different native paths may nevertheless reach the same
marked window and origin with different coefficient frames. One relative
comparison has order five; equal endpoints do not erase history.

The refined connection was tested on 24 seed markings through depth 28:

| Recorded quantity | Count |
|---|---:|
| Packet/frame states, summed across seeds | 250,040 |
| Checked transitions | 458,912 |
| Conflicting candidate field parities at repeated marked charts | 0 |

This result concerns the declared field-transport rules in the explored graph.
It is not a universal-depth theorem or a certificate for every simultaneous
assembly and incidental field contact.

## Retained exclusions and accounting

The two-step geometric recurrence does not make seven blocks of four or
fourteen blocks of two into new symmetries. Two frame-related histories also
do not automatically supply two independent physical modes.

The candidate contrast-to-E exchange does not conserve the original defect
operator. The augmented quantity

$$
Q=H_N\oplus(H_E+N_E)
$$

is conserved by the constructed exchange, but the added electron-return term
is explicit dimensionless bookkeeping. Its physical energy interpretation,
normalization and dynamics are not derived.

**Scope.** These are exact algebraic constructions and bounded executable
checks. No independent scientific review, universal coherence theorem, mass,
charge, isotope stability, physical time or particle-creation law is claimed.
The experimental terminal P-to-E support permission is separate and unchanged.
Production generation and viewer rules are unchanged.

## Durable verification

```sh
python research/strominger/checkers/check_reader_field_closeout.py
```

Seven central checkers were freshly rerun. The closeout manifest verifies ten
selected receipt hashes and retains content-addressed copies of the receipts.

- [Fresh verification manifest](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/results/reader-field-closeout/verification.json)
- [Closeout runner](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/checkers/check_reader_field_closeout.py)
- [Global PN construction](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/checkers/construct_global_PN_transport.py)
- [Native contrast-to-E construction](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/checkers/check_neutron_contrast_electron_transport.py)
- [Full-five candidate](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/checkers/check_full_five_channel_candidate.py)
- [Extended frame test](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/checkers/check_extended_field_frames.mjs)

Number allocation: `seqclaim-a12bf5f15281f9a09483fc83` on
`marici-ledger-entry`. Research report admission:
`ev-000000016183-00d9231f-dce3-4554-b610-d1d70bea1f1f`.
Graph admission records policy-valid provenance, not truth certification.

The next tests are source selection of the coupling conventions, field sewing
at incidental contacts of complete assemblies, and dynamics with independently
justified units. The bounded checkpoint is closed; those obligations remain open.
