# Iteration 7: a fold-preserving, mode-bearing interface

## Repair the rejected assumption, not the source operator

The complete iteration-6 packet was freshly read and reverified. That candidate failed because it imposed a particular coefficient value j(x) from the host point's spatial position, excluding sixteen required fold interiors.

The repair keeps host location and coefficient value as **different typed variables**. The actual source projector, its direction map Gamma, and its image disk Z are unchanged. No new particle operator is introduced.

Definitions:

- T: the selected flagged host triangle (F_ABC,A,B).
- B: the iteration-5 refined direction sphere, retaining all 24 original inward-fold owners.
- I=[0,1]: inward depth.
- Z: the actual L_AB mode-image disk.
- H=T x Z: host location together with a possible mode value.
- C_hat=I x B: resolved potential with retained inward direction.

## 1. Actual maps and pullback

Construct

```text
                  Q
                 / \
                v   v
       H = T x Z     C_hat = I x B
                \   /
                 v v
                I x Z
```

The maps are

```text
mu(x,z) = (h_T(x),z),
nu(t,v) = (t,Gamma(v)).
```

The full pullback is explicitly isomorphic to T x B:

```text
(x,v) -> ((x,Gamma(v)), (h_T(x),v)).
```

Conversely, a compatible pair ((x,z),(t,v)) satisfies t=h_T(x) and z=Gamma(v), so its unique preimage is (x,v).

For arbitrary compatible PL maps from any X, the mediator is the pair of their x and v components. It is PL and unique. This gives the geometric universal property; the finite vertex and cell tests are supporting checks, not a replacement for the argument over arbitrary X.

The retained product triangulations make both incoming interface maps, both pullback projections and the projection to bare host location simplicial. Directions are ordered by their actual mode image on each triangle so that this claim is checked rather than assumed.

## 2. All folds are active again

| Object | f-vector |
| --- | --- |
| Full pullback | (140,1266,3396,3564,1296) |
| Preimage of the bare host center | (20,54,36) |

The center preimage has sphere homology. Every one of the 24 original vertex-edge-face-body fold owners has an active cell interior there. All sixteen interiors excluded by iteration 6 are restored, not merely retained in an unused source record.

The full object has the same underlying PL space T x S2 as the resolved direction-bearing construction, with the refined potential atlas and explicit coefficient observables. Its mod-2 Betti numbers are (1,0,1,0,0). The new triangulation is not asserted to be the identical old inventory or a cellwise refinement of its particular product ordering.

The 1296 here counts four-dimensional simplices. It is not the source network's 1296 feedback arrows or a new particle-cost claim.

## 3. Three levels of information, three different fibers

These must remain distinct:

```text
bare host location:       q
mode-bearing host state:  (q,z)
retained potential state: (q,v), with z=Gamma(v).
```

Over q alone the direction fiber is the complete sphere. Equivalently, it is the preimage of {q} x Z in the actual host interface H.

Over a fixed (q,z), the fiber has two points for an interior mode and one on the mode seam. Equal modes do not merge the two direction witnesses.

Thus the construction realizes one **visible host vertex with retained internal directions**. It does not claim that the entire information space over that vertex is a single point. The radial blowdown to the previous point realization remains explicitly lossy at that center.

## 4. The failed candidate is a restriction of this one

The former rule is the extra section constraint z=j(x). Imposing it on the new pullback recovers exactly the previous eleven vertex pairs, and geometrically recovers the same twelve-triangle disk by the closed-form lift formulas of iteration 6.

This is why the failure was substantive: fixing the mode by position selects a smaller object. It is not merely a change of names or serialization.

The comparison is a PL comparison; the particular triangulations need not make that section simplicial without a common subdivision. We do not infer simplicial equality merely from agreement of vertex sets.

## 5. What is and is not required about the belt

The host's six-panel annulus remains the positive-depth truncation of its six flagged inward sectors. Its preimage in the full object is that annulus times B, not just a two-dimensional belt.

The potential mode seam remains a different locus: in the full object it is T times the seam circle in B. Neither its location nor its dimension identifies it with the host annulus.

Holding v fixed around any host-belt loop holds Gamma(v) fixed as well. The loop closes without a sheet permutation. The image-interior sheet labels from iteration 5 remain global, so coefficient-mode loops likewise do not force the independent odd C2 twist.

Six panels follow from the retained flag convention; annular topology follows from a punctured host neighborhood. Nontrivial transport is not forced by the constructed interface maps. No neutron identity follows from either belt or seam.

## 6. Verification and remaining closure work

All 20 checks passed:

- fresh verification of the entire retained source chain;
- all five typed simplicial maps and their commuting square;
- unique mediators for all 140 compatible vertex pairs;
- mediator/inverse round trips in all 1296 cell interiors;
- active representatives of every original fold over q;
- restored omitted folds and recovery of the restrictive section's vertices;
- separate location, mode and direction typing;
- actual host-loop returns, rehashed mutations and complete packet replay.

```text
python research/voevodsky/checkers/check_open_mode_pullback.py
```

- `research/voevodsky/checkers/check_open_mode_pullback.py`
- `research/voevodsky/results/open_mode_pullback_store.json`
- `research/voevodsky/results/open_mode_pullback.json`

Root: `77bbbe1b7c1d3a0ec3dc9221883f62e33c740c442b05259a7bafb8e28a9cf0cc`.

The static interface now satisfies full fold retention under the declared barycentric grammar. The next closure check is the inward realization itself: construct its family of maps on this mode-bearing square and verify that approaching the center retains directions and fold owners, while the old point realization is obtained only by the explicit blowdown. A cell count alone is not that dynamical-free realization witness.
