# Neutron reverse assembly: occurrence records versus minimal rotational seeds

Date: 2026-10-10

## Answer to the operator's question

The relevant test is a lossless reverse of the actual construction, not just
the smallest polyhedron with its symmetry. That reverse audit now passes.

| What is being counted | Checked count |
|---|---:|
| Distinct undirected geometric segments | 12 |
| Expanded directed, face-tagged boundary occurrences | 18 |
| Minimum seed occurrences with the retained C3 sector rotation | 6 |
| Minimum seed occurrences with all six retained proper source symmetries | 3 |
| Expanded coefficient-transfer arrows of the fixed intrinsic L/G/N protocol | 1836 |

These are different records, not competing answers to one unqualified count.
The rotational minima are relative to explicit replay rules and retained source
data. They do not claim that three bare segments, without a metric, labels,
rotation operations or phase/assembly rules, determine the neutron candidate.

## 1. Reverse the stored assembly, rather than invent a new shape

Read the original six panels and all eighteen ordered centroid triangles from
`results/coupled_six_piece_belt_store.json`, bound to
`results/four_six_center_cones.json`. A primitive reverse-assembly occurrence is

    (incident face vertex set, directed tail, directed head).

Its native small triangle is (face centroid, tail, head). Thus it retains both
its geometric boundary and the orientation used by its coefficient mode. The
face centroid is recalculated from the retained vertex coordinates, not stored
as an unrelated point.

Each of the six panels reverses to three directed boundary occurrences. Joining
those occurrences by their face tags reconstructs exactly the six original
oriented panel cycles. The eighteen reconstructed small triangles reproduce
all 54 ambient complex coefficients under the existing frame and character
rule. No new phase table or energy law is fitted.

The eighteen occurrences identify to twelve undirected segments:

- six rim segments, each with one admitted panel incidence;
- six stitches, each with two admitted panel incidences.

In this source, the two stitch occurrences have opposite directions, so there
are eighteen distinct directed endpoint pairs as well.

## 2. The six-occurrence packet used by the existing C3 sector construction

The first native paired sector contains these two panel boundaries:

    U0 -> L1 -> L2 -> U0,
    L1 -> U0 -> U1 -> L1.

Explicitly its six seed records are:

| Incident panel | Directed occurrence |
|---|---|
| U0 L1 L2 | U0 -> L1 |
| U0 L1 L2 | L1 -> L2 |
| U0 L1 L2 | L2 -> U0 |
| L1 U0 U1 | L1 -> U0 |
| L1 U0 U1 | U0 -> U1 |
| L1 U0 U1 | U1 -> L1 |

The shared stitch appears twice, with different incident panels and opposite
directions. These six records therefore occupy **five distinct undirected
segments**, not six independent spatial edges.

Applying the retained 120-degree rotation zero, one and two times recovers all
18 records. The complete occurrence set splits into six disjoint C3 orbits of
size three. Rotation cannot leave an orbit, so at least one seed per orbit is
necessary. The six listed records attain that lower bound. Removing any one
loses three expanded occurrences.

The six seeds are taken from the existing intrinsic store's first paired sector,
not chosen to force a desired count.

## 3. The stronger existing symmetry library reduces the seed packet to three

`check_belt_operator_inputs.py` had already identified six proper monomial
source-frame symmetries preserving the actual ordered triangles. Reusing that
library, the same eighteen records split into **three orbits of size six**.

One representative packet is the single oriented panel

    L0 -> L1 -> U1 -> L0,

with its incident-face tag L0 L1 U1 on each arrow. These three occurrences
lie in different orbits. Their six symmetry images recover the entire packet.
Removing any one seed loses six expanded occurrences.

The checker exhaustively tests every smaller subset of the eighteen candidates
for both the three-seed and six-seed contracts. The general minimality argument
is orbit coverage: every allowed replay operation stays inside the seed's orbit,
and every target orbit must be reached.

This is not a newly postulated reflection or complex conjugation. The six
operations are the already retained proper source symmetries. The audit also
checks that all six preserve the chosen adjacent-pair partition, intrinsic
metric denominators, selected numerator modes, and all three intrinsic L/G/N
coefficient operators under the corresponding coordinate permutation.

## 4. What the replay grammar permits—and what it does not

Permitted generation: apply the supplied vertex rotation maps to an existing
face-tagged directed occurrence. Join endpoint/face labels afterward, retaining
occurrence provenance. Only vertex actions are stored in the replay rules;
they do not contain a hidden table mapping all target faces or triangles.

Not implicitly permitted:

- invent a reverse arrow from an existing arrow;
- compose a path into a new arrow occurrence;
- fill every directed three-cycle with a face;
- reconstruct a convex hull or apply a facet-admission algorithm;
- infer a phase or native operator grouping from unlabeled geometry.

If one of those operations is admitted, its source data and witnesses must be
counted and the minimality question changes. In particular, the earlier generic
orbit/hull constructor can generate faces from point data without starting with
these arrow occurrences at all. That is a different input grammar, not a
contradiction of the rotational-seed minima.

The retained supplementary data are the vertex geometry/metric, rotation actions,
coefficient frame and character, chosen adjacent-pair grouping, and identification
and occurrence conventions. A source-arrow count is not the bit size or total
operation cost of this entire package. No unrestricted program-minimality claim
is made.

## 5. Loss controls: geometric coincidence is not record equivalence

### Dropping direction loses the native phase

Reversing each of the eighteen ordered local edges changes its complex mode
while preserving its squared norm. All eighteen controls are checked. A norm or
an undirected segment cannot recover that orientation choice by itself.

### A directed triangle cycle is not automatically an admitted face

The eighteen directed endpoint pairs contain eight directed triangular cycles.
Six are the retained panels; the other two run around the upper and lower caps.
The endpoint graph alone does not declare which cycles carry face witnesses.
Adding an inference rule about orientation, supporting facets or active centroid
modes would supply additional construction data; it is not implicit in an arrow.
The extra cap cycles are not claimed to be compatible outward-oriented faces of
the same oriented surface.

This is exactly why the inverse must retain incident-face/admission information.
The two fixed cap-centroid channels from the mode constructor are not silently
deleted or promoted to moving panel records by this reverse audit.

## 6. Do not confuse compression with deleting the coefficient protocol

The intrinsic protocol still has

    L: 432 arrows, G: 108 arrows, N: 1296 arrows; total 1836.

Its existing positive closed-cycle certificate was freshly rerun. Every arrow
is indispensable under that fixed coefficient/stage deletion test. The small
seed packets generate source geometry and modes; they do not replace execution
of the expanded protocol by three or six coefficient transfers.

Changing coordinates, permitting another constructor or changing the operation
library is outside the fixed deletion theorem. No claim of 1836 as an absolute
minimum over all possible algorithms is made.

## 7. Disposition

We can now say precisely:

- **Literal reverse ungluing:** eighteen directed, face-tagged occurrences.
- **The native three-sector rotational replay:** six seed occurrences.
- **The fuller already-retained proper-symmetry replay:** three seed occurrences,
  one oriented triangle, plus the explicit source/replay data.

The neutron comparison with the proton's previously stated six **undirected
edges** must use the same record type and operation library before drawing a
minimality conclusion across species. This packet does not equate those counts,
identify geometric symmetry with electric neutrality, or prove a physical
neutron interpretation.

## Verification

```sh
python research/voevodsky/checkers/check_belt_three_by_twelve.py
python research/voevodsky/checkers/check_neutron_reverse_arrow_minimality.py
```

Both pass. New receipt: `results/neutron_reverse_arrow_minimality.json`. It records
the concrete seed packets and vertex actions, orbit/deletion certificates,
reverse-assembly and coefficient round trips, cap-cycle ambiguity controls,
operator covariance, and current source hashes.
