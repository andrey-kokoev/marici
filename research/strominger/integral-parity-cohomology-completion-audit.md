# Completion audit: integral parity-cohomology classification

Date: 2026-08-24 (America/Chicago)

This audit maps every requested move to current authoritative evidence.  A
green result means the named packet contains the theorem boundary and the
named checker was rerun from source with exit code zero during closeout.

## Requirement matrix

| move | requirement | authoritative packet | fresh evidence | status |
|---:|---|---|---|---|
| 1 | typed lattices and maps | `integral-parity-cohomology-types.md` | `integral_parity_cohomology_types_checks.py`, 5/5 | proved |
| 2 | commuting parity-de Rham diagram | `integral-parity-cohomology-diagram.md` | `integral_parity_cohomology_diagram_checks.py`, 6/6 | proved |
| 3 | symbolic logarithmic normal form | `magnetic-tower-logarithmic-normal-form-proof.md` | `magnetic_tower_logarithmic_normal_form_checks.py`, 4/4 | proved |
| 4 | rational-exact combinations | `magnetic-rational-exact-classification.md` | `magnetic_rational_exact_classification_checks.py`, 4/4 | proved |
| 5 | global residue augmentation | `magnetic-residue-augmentation.md` | augmentation checker, rank/circuit/basis gates | proved |
| 6 | Smith form and torsion boundary | `magnetic-residue-augmentation.md` | augmentation checker, 9/9 total | proved |
| 7 | prime-local fixed divisor | `even-depth-fixed-divisor-proof.md` | `even_depth_fixed_divisor_checks.py`, 4/4 | proved |
| 8 | exact stabilization cutoffs | `stabilization-cutoffs-theorem.md` | `stabilization_cutoffs_checks.py`, 4/4 | proved |
| 9 | naturality | `parity-cohomology-naturality.md` | `parity_cohomology_naturality_checks.py`, 4/4 | proved |
| 10 | constructor extensions | `constructor-extension-classification.md` | `constructor_extension_classification_checks.py`, 6/6 | classified at declared authority boundary |
| 11 | hostile falsifiers | `hostile-falsifier-suite.md` | `hostile_parity_cohomology_falsifiers.py`, 8/8 | reproduced |
| 12 | corrected master theorem | `integral-parity-cohomology-master-theorem.md` | master manifest, 4/4 over 115 underlying gates | complete |

## Fresh closeout commands

Every theorem-bearing checker in the manifest was rerun in three bounded
batches using

```text
uv run --with sympy python -u <checker>
```

All three batches returned `PASS`.  The regenerated master command

```text
uv run --with sympy python -u research/strominger/checkers/integral_parity_cohomology_master_checks.py
```

returned 4/4 with 115 underlying passed gates.

Additional closeout gates:

- `git diff --check -- research/strominger`: no whitespace error;
- non-ASCII scan of every new checker: empty;
- stale-claim scan for the superseded two-dimensional ordinary residue
  quotient: empty;
- corrected legacy tower checker: 42/42.

## Defects found and repaired during the objective

1. The old inference “one ordinary residue line per positive depth” was false.
   Cross-depth residues cancel.  The ordinary quotient has rank one whenever
   any positive tower is visible.
2. Pairwise primitive residue circuits need not generate the saturated
   integral kernel.  Sequential unimodular Bezout reduction replaces that
   claim; the old approach has an explicit index-five falsifier.
3. A literal null-vector orientation check was replaced by an orientation-free
   span/primitivity test.
4. The Boolean Mobius test had source and observation subset orientation
   reversed; the incidence direction was repaired.
5. The cross-sector synthesis initially promoted endpoint-algebra generation
   to observer faithfulness.  It now distinguishes algebraic control from a
   physical reconstruction certificate.
6. The all-integer constructor was shown nonconservative by two explicit new
   mixed-parity circuits.

The stale `magnetic-kernel-tower.md` interpretation and its result verdict were
repaired, and the checker now includes the missing cross-depth exactness gate.

## Scope that remains deliberately unclaimed

- No physical source-to-engine constructor is derived.
- No physical target is proved equal to the theorem's full Laurent target.
- Target truncation is excluded and has an explicit rank-drop falsifier.
- Odd-only constructors have bounded evidence but no unbounded theorem.
- The all-integer constructor requires a new mixed-component classification.
- Fractional/cyclic-cover states require equivariant pullback and descent data.
- A parity circuit is not called a homology class without an independently
  derived preceding repair map.
- No Hall or Plucker certificate selects a physical coefficient or lens point.

These are theorem boundaries, not incomplete clauses of the stated even-lane
full-target objective.

## Durability state

The correction milestone was admitted to the epistemic graph at event 3144;
the final completion report replying to the physical-target caution was
admitted at event 3169.
All filesystem changes are confined to `research/strominger`.  No commit or
push was made because the operator has not authorized either action.
