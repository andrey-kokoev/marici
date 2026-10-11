# Complex-mode lead: derive the neutron's two exclusions from centroid modes

**Scope correction:** `centroid-admission-refinement-counterexample.md` verifies
that this works at the supporting-facet level but not on arbitrary subdivided
cells. Subdividing the excluded caps makes all their children centroid-active.

## Operator proposal and precise tested interpretation

The operator suggested that a movement into and from the complex plane might
explain the two extra pieces obtained when neutron rim protection is removed.
Tested a concrete mode-selection interpretation, not an assumption that changing
coordinates can delete cells.

For any facet F with centroid c_F and supplied affine isometries g, define

    score(F) = sum_g ||g(c_F)-c_F||_G^2.

Admit F iff score(F)>0. Positive definiteness implies that score zero means the
centroid lies in the common fixed affine subspace. Although score magnitudes
depend on the generator presentation, this zero/nonzero distinction depends
only on the generated action. This is one rule for all three sources.

Before constructing the geometry, replace every external-interface seed role
by the ordinary carrier role. Thus no explicit neutron cap exclusions are used.
The separate retained attachment-pole records for proton and electron remain.

## Exact result

| Source | Supporting facets | Positive centroid-mode scores | Zero scores | Recovered cones |
|---|---:|---:|---:|---:|
| Proton | 4 | 4 | 0 | 4 |
| Neutron | 8 | 6 | 2 | 6 |
| Electron | 5 | 5 | 0 | 5 |

All exact marked target comparisons passed: distances, facets, center distances,
attachment interfaces and the stored fine subdivisions. The two zero-score
neutron facets are precisely the former explicitly protected rims. They are
retained as interface records, not lost from construction history.

An exact affine-frame control changes coordinates by nonuniform rational scales
and a translation, transforms the metric and actions accordingly, and recomputes
the selection. Every score and every target comparison is unchanged. This rules
out an accidental dependence on drawing axes or the coordinate origin.

## Why the neutron example is naturally complex

In its stored scaled coordinates let

    u = Z + i*sqrt(3)*X.

The existing 120-degree rim action sends u to conjugate(omega)*u, with
omega=exp(2*pi*i/3), while Y is fixed. The upper rim satisfies u^3=1 and the lower
rim u^3=-1. Exact arithmetic checks every vertex.

The fixed projector is

    (I+R+R^2)/3 = diag(0,1,0),

and its complement is diag(1,0,1), the real carrier of the two conjugate complex
modes. On facet centroids:

- both cap centroids have u=0;
- all six side centroids have |u|^2=4/9;
- their displacement scores are 3|u|^2, hence 0 versus 4/3.

This supplies a source-action reason for the distinction, replacing the previous
hand-declared cap exclusion by a new uniform centroid-mode admission hypothesis.

## Essential negative control

The caps do NOT disappear under projection into the complex plane. Every cap
vertex has |u|=1, and each projected cap remains a nondegenerate triangle, with
edge Gram determinant 27/4. Only its centroid amplitude vanishes.

Therefore the experiment supports **selecting active facet-centroid modes**, not
geometric erasure by complex coordinates or complexification alone. Nor does it
yet specify a time evolution into/out of that plane. Why centroid-mode support
should govern cell admission is the remaining mathematical/modeling question.
The centroid is already used by the established face subdivision, but that does
not by itself prove this new selection law.

No 1836 count, neutron coefficient network or full-pentachoron spinor operator
is inferred from this result.

## Reproduction

    python research/voevodsky/checkers/check_relative_geometry_mode_selection.py

Fresh run passed, including the non-erasure control.

- `results/relative_geometry_mode_selection.json`: comparison and interpretation,
  with source/implementation hashes.
- `results/mode-selected-proton.json`, `mode-selected-neutron.json`,
  `mode-selected-electron.json`: generated cells and exact per-facet scores.

The original explicit-interface constructor is retained unchanged for comparison;
this checker implements the new selection as an independently testable extension.

## Follow-up

`relative-geometric-reversible-mode-motion.md` now supplies the explicit exact
encode/phase-advance/decode procedure, including inverse histories and a neutron
source with no external-interface exclusions. It retains fixed centroid modes
and separately checks that cap corners still move. The choice of centroid-mode
support as cell admission remains a hypothesis.
