# Global Hopf trial: consistent Abelian connection, native binding still open

**Conditional experiment; not admitted wiring.** This follows the [local trial](five-side-oct-local-hopf-trial-v1.md). It changes the connection hypothesis, not the native packet contents or viewer.

## 1. Derive the geometry of the failed comparison

Let `v,w` be adjacent interior vertices and `c` the centre of one of their four shared cells. Since a regular native cell has equally distant vertices, `|c-v|=|c-w|`. In orthogonal coordinates, with `e=(w-v)/|w-v|`, its two direction vectors satisfy

```
n_w = n_v - 2 dot(n_v,e) e.
```

This is a reflection of the direction sphere, not a common-phase change over a fixed base point. The tests verify the identity for all four cells of all 168 shared rings. Thus treating the isolated local connections as differing only by a scalar gauge was too restrictive.

The inspected source notes `geometric-context-and-extended-coherence-v1.md` and `context-composition-fillers-v1.md` supply candidate five-coefficient/frame constructions and scoped retained-history fillers, respectively. Neither supplies a binding of this reflection or the Hopf phase to the operator's signed P/E records. No such binding is claimed here.

## 2. An explicit additional global hypothesis

Instead of an isolated monopole connection at each star, form **one tensor-product line connection** with one equal-sign unit Hopf factor at each of the 44 interior vertices:

```
L(x) = tensor product over v of Hopf((x-v)/|x-v|)
A(x) = sum over v of A_v(x).
```

This lives away from the 44 centres. Interpreting the local direction spheres this way is a new mathematical hypothesis, not an identification of physical charges. The factors are auxiliary line-bundle data; no native payload is copied, summed, or tensored. Implementation retains 44 labelled factor contributions rather than materializing a large tensor-state space.

At every native cell centre, evaluate all factors. Assign the resulting connection phase to every native shared-face adjacency. All stars now restrict the **same global connection** to their shared comparison edges.

This is not a gauge repair of the previous trial. Contributions from the other 43 centres change a star's local curvature. Their total flux around that star is zero, so its own unit charge is preserved, but their individual face fluxes need not vanish.

## 3. Results on the native dual complex

The resulting comparison graph covers **all 245 cells and all 560 native shared interfaces**. Its 360 quadrilateral faces correspond exactly to the native edges not lying in the carrier boundary. There are 44 dual 3-cells, one around each interior native vertex.

- Each dual cell retains total flux `-2 pi`: winding magnitude one.
- The contribution of every other monopole to that cell's total flux is zero.
- All **168 shared dual faces** cancel between opposite boundary orientations, within numerical tolerance.
- Each face's connection holonomy agrees modulo `2 pi` with its independently computed sum of half-solid-angle fluxes.
- The remaining **192 outer dual faces** carry total flux `-88 pi`, or **44 units in magnitude**.

The outer dual boundary is a surface assembled from cell centres. It is **not** the native octahedron's triangular boundary or an authorized five-edge closure law.

The checker also evaluates all three-/four-interface comparison-context moves and graph-cycle bases in all six readings. The declared scalar connection respects context cancellation and closed comparison cycles. This is a bounded Abelian result; it does not establish the native nonabelian comparison or retained-history laws. The previously potential comparison domain has not thereby become source-authorized.

## 4. Triple overlaps and retained winding

The earlier conjugation-everywhere proposal failed because three anti-linear transitions cannot compose to identity. Here charts refer to a single global complex line. Ordinary section gauges have transitions `exp(i(g_b-g_a))`, whose triple cocycles cancel. Tests use the actual 176 native triple overlaps and reject a perturbed transition.

This does not select the native histories. It verifies the mechanism of the new mathematical reference bundle, in contrast to the incompatible isolated connections.

All face fluxes and source labels remain retained. Exponentiating the total boundary flux gives identity and loses all 44 units. The checker therefore never treats a unit complex holonomy alone as a certificate of zero winding.

A consequential open constraint is now explicit: **this equal-sign trial cannot close with zero net boundary flux without further structure**. A compact closed extension would need compensating charge or another justified change of the assumptions. No sink, seam, opposite charge or boundary quotient has been inserted to force closure. The number 44 is an auxiliary Chern-flux sum, not a physical charge or a count of the 80 retained fibres.

## 5. Admission gates

This experiment supplies a globally consistent reference connection, not a completed native realization. Still required:

1. source-defined correspondence between the native packet and the auxiliary line/factors;
2. a justification for equal signs and additive connection composition, or a different source-derived choice;
3. actual comparison maps retaining native operands and histories, not only scalar phase ratios;
4. the operator's boundary/entry/exit law and compatibility with the measured flux;
5. a binding to the 80 retained fibres and valid native routes.

No routing, grouping or rendering was changed.

## Replay

```sh
node --test tests/five-side-oct-global-hopf-trial.test.mjs
node research/strominger/checkers/check_five_side_oct_global_hopf_trial.mjs --record
```

Implementation: `five-side-oct-global-hopf-trial.mjs`.
Receipt: `results/five-side-oct-global-hopf-trial-v1/verification.json`.

The receipt retains per-source flux for each dual cell, every shared/boundary face occurrence, six-reading context checks and source hashes, with `constructionAdmitted: false` and `nativeBindingAdmitted: false`.
