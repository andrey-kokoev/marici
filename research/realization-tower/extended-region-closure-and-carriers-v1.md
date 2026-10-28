# Extended region: cellular closure and actual P–N–E constructor audit

## Geometric completion

The four-step region recovered by compare-first search was assembled from all
8 contained regular tetrahedra and 6 contained octahedra. Exact oriented cellular
boundary matrices give:

| Quantity | Result |
|---|---|
| Vertices / edges / faces / volumes | 19 / 60 / 56 / 14 |
| Boundary vertices / edges / faces | 18 / 48 / 32 |
| Boundary-map ranks | 18 / 42 / 14 |
| Rational Betti numbers | (1,0,0,0) |
| Boundary rational Betti numbers | (1,0,1) |

Both successive boundary-map products vanish exactly. Every internal face
occurs twice with opposite orientation. No face has more than two incident
volume cells. These establish the recorded cellular compatibility; the region
is the explicit convex octahedral interval. Betti numbers alone are not being
used to characterize arbitrary spaces as balls.

## Actual carrier construction, not roles assigned by count

The owning `createWindowConstruction` was run unchanged on each of the eight
regular tetrahedral seeds, for all 24 bijective C0/M0/C1/M1 seed markings:

- **192** marked trials;
- **192** complete native P→N→E chains;
- **128** trials entirely inside the region;
- **64** distinct contained geometric P→N→E chains;
- **0** contained chains whose proton contains the entry pole and whose electron
  contains the opposite exit pole.

The tested pole-incidence criterion is explicit and weaker/different than the
owner's centre-entry/centre-exit protocol. No identification of pole probes
with those centres is claimed.

The octahedral subdivision, primitive admission and phase update were the
owner's existing inputs, not selected to produce an isotope. In particular,
subdivision tetrahedra are retained where the owner requires them; this is not
an assertion that every particle body is a regular elementary honeycomb cell.

## Surviving result

The larger region is a consistent geometric complex and supports many existing
local marked carrier chains. A **single** existing three-carrier chain does
not span the selected poles within the tested complete seed/marking class.
A longer multi-chain realization needs its own typed continuation and coherence
witnesses. An ordinary E→P continuation is not supplied by this count or
invented to bridge the gap.

The geometric boundary equations do not establish all phase, metric, marked
reader or higher WG conditions. No isotope is assigned to the fourteen volume
cells, and no earlier proof outcome or task frontier is promoted.

## Fresh verification

```sh
python research/realization-tower/check_extended_cell_closure.py
node research/realization-tower/check_extended_carriers.mjs
```

Both pass. The Python checker uses exact integer/Fraction elimination, with no
external algebra dependency. The JavaScript checker imports the existing owner
constructors and retains the bodies, markings, events and endpoint decisions
for every trial.

Receipts:
- [Cellular closure](results/extended-cell-closure-v1.json)
- [All 192 marked carrier trials](results/extended-carrier-search-v1.json)
