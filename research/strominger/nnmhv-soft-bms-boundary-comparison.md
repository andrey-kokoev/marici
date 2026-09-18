# NNMHV boundary updates versus soft/BMS data

## Disposition

**Structural analogy only.** The source-derived NNMHV identities are exact, but no map to null-infinity fields is present, so neither a leading/subleading soft identity nor a BMS charge-flux or memory balance law can be formed.

## Convention alignment

| NNMHV datum | Soft/BMS candidate | Result |
|---|---|---|
| type-A simple-root boundary `b1=b2` | soft momentum limit | mismatch: a discrete history boundary is not an `omega -> 0` limit |
| terminal insertion | leading soft/new radiative datum | analogy only: insertion changes the Segre image ruling by adjoining a null-edge spinor, but supplies no news, shear, polarization, or zero mode |
| retained-history reflow | subleading hard-leg action | analogy only: reflow changes the kernel ruling and canonical weights, but supplies no angular-momentum differential operator or sphere vector field |
| signed exchange defect | charge/flux or memory balance | rejected as a derived identity: it is a nonzero cluster-weight residual without BMS normalization, cut data, or hard/soft flux |

The leading triangle uses an `omega^-1` residue, supertranslation Ward charge, and zero-frequency shear/displacement memory. The subleading triangle uses an `omega^0` angular-momentum operator, superrotation charge, magnetic projection, and spin-memory contour. None of these typed data occurs in the NNMHV packet.

## Exact identities that do pass

1. `Delta S_n = terminal insertion + retained-history reflow`.
2. Insertion varies the rank-one transport image ruling; reflow varies its kernel ruling.
3. The `alpha_2` simple-root correction controls the unique negative composite-root minor.

These are refinement and transport identities, not yet radiative balance laws.

## Nonzero residual

The signed exchange residual changes from

`77434747717156613539533217 / 17690496785279502071012865129300592500`

to

`-64467252153401672951924968453 / 53071490355838506213038595387901777500`.

The boundary-induced change is exactly

`-16831310196814032984532666 / 13806319031175469878522007124844375`,

so it is not a hidden zero that could be renamed a conservation identity.

## Missing bridge

A derived bridge requires all of:

- external spinors or momentum twistors to celestial direction and energy;
- cutoff `n` and any deformation coordinate `t` to Bondi cuts or retarded time;
- boundary replacement to shear/news zero modes;
- canonical weights to normalized BMS charges or memory observables;
- insertion/reflow orientation to hard/soft flux orientation.

No such map is supplied. In particular, `t` must not be interpreted as physical time. The comparison therefore neither falsifies a future map nor constructs one; it rejects the present physical identification while preserving the structural analogy.

## Evidence

- `research/strominger/checkers/nnmhv_soft_bms_boundary_comparison.py`
- `research/strominger/results/nnmhv_soft_bms_boundary_comparison.json`
- `research/nima/results/nnmhv-simple-root-interference-control.json`
- `research/nima/results/nnmhv-shell-flux-mechanism.json`
- `research/nima/results/segre-insertion-reflow-orientation.json`
- `research/nima/results/nnmhv-cluster-exchange-weight-gate.json`
