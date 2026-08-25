# Formalization sprint 1 report

Owner: `marici.Buzzard`

Source packet: `research/nima/buzzard-formalization-sprint-1.md`

Strength: abstract algebraic and finite countermodel theorems. A passing build
does not supply any physical/source-derived selector, frame, transport, probe,
or readout.

## Project contract

The operator authorized one project root at
`research/buzzard/marici_formal/`. Its `lean-toolchain` pins
`leanprover/lean4:v4.33.1`; `lakefile.toml` pins Mathlib `v4.33.1`; the resolved
commit graph is recorded by `lake-manifest.json`.

Primary source: `marici_formal/MariciFormal/Sprint1.lean`.

## Dependency diagram

```text
AddCommGroup A
  -> delta : A × A ->+ A
  -> diagonal : AddSubgroup (A × A)
  -> delta_ker_eq_diagonal                         [2125]

CommRing R + Module R V/W/Q
  -> LinearMap kernels -> iInf jointKernel
  -> JointlyFaithful <-> jointKernel = bottom      [2116]
  -> readout equality <-> difference in ker        [2111, 2114]
  -> K.mkQ + K.liftQ
  -> probe descends <-> K <= ker probe             [2111, 2114]

finite types/functions
  -> Selector / Rigidifier / FaithfulReadout
  -> three explicit non-implication countermodels  [2109, 2114]

Group G + endpoint gauges + FramePair
  -> gaugeOpen changes under nontrivial endpoint gauge
  -> framedValue invariant under compatible frames [2120, 2125]
  -> CommGroup closed conjugation invariant

linear response + declared subset
  -> nonzero response detects nonzero input
  -> one-probe non-injectivity counterexample       [2122]
  -> jointly faithful family reconstructs equality [2116, 2122]
```

## Formal theorems and assumptions

| Milestone | Formal object/theorem | Assumptions | Class |
|---|---|---|---|
| A | `delta`, `diagonal`, `delta_ker_eq_diagonal` | `AddCommGroup A` | algebraic |
| A | `PeriodicPhaseLayer` | declared period subgroup and quotient hom equal to canonical quotient map | quotient; no topology |
| B | `jointKernel`, `JointlyFaithful`, two equivalences | `CommRing R`; additive commutative modules `V,W` | algebraic |
| B | `erases_iff_sub_mem_ker` | linear readout `r : V ->ₗ[R] Q` | algebraic/readout |
| B | `descendsThrough_iff`, family form | canonical module quotient `V ⧸ K`; same module assumptions | quotient/algebraic |
| C | three non-implications | finite/empty types and ordinary functions | logical countermodels |
| D | `open_transport_not_invariant` | group and a specified nonidentity gauge | algebraic/framing |
| D | `framedValue_gauge_invariant` | group plus compatible endpoint frame transformation | framing |
| D | `closed_holonomy_invariant` | commutative group | algebraic |
| E | detection, non-reconstruction, reconstruction | commutative-ring modules and linear maps; explicit `Fin 2 -> ℚ` counterexample | algebraic |

The probe index type is arbitrary in the reusable theorem, hence includes
every finite family. No finite-dimensional assumption is needed for the
kernel equivalence; the explicit counterexample is two-dimensional.

## Frozen-entry audit

- Entry 2109: fully formalized only as logical independence of the minimal
  generic structures. The sector-specific meaning of automorphism reduction
  is untyped.
- Entry 2111: conditionally formalized as linear quotient descent and kernel
  loss. A source-derived transverse/diagonal map is not supplied.
- Entry 2114: conditionally formalized by the readout loss criterion and an
  explicit selector/unfaithful-readout countermodel. No physical selection
  datum is supplied.
- Entry 2116: fully formalized at the algebraic level: joint faithfulness is
  trivial infimum of kernels and reconstructs equality. Probe legality remains
  source/physical data.
- Entry 2120: conditionally formalized in the weakest group-valued endpoint
  gauge model. Berry connection, topology, smoothness, and physical framing
  remain untyped.
- Entry 2122: fully formalized as the abstract detection/reconstruction
  separation with an explicit two-dimensional rational counterexample.
  Identification with interference quadratures/holonomy remains untyped.
- Entry 2125: fully formalized for the additive `AddCommGroup` layer and for
  abstract group framing. The circle-valued physical character remains
  separately typed and unresolved.

## Exact blockers and missing source data

1. A real-to-circle statement needs a specified homomorphism, a declared
   period subgroup (for example a precisely normalized copy of `2πℤ`), and a
   proof of its kernel. Topological/continuous character claims additionally
   need topological group structures and continuity. Equality of real
   representatives cannot replace equality in the quotient.
2. Physical `dqᵢ` require a source-defined domain/codomain, scalar ring,
   differentiability, and proof that the derivative is the stated linear map.
3. Quotient descent is canonical only after the killed submodule `K` is named
   and proved contained in every probe kernel. No splitting or choice was used.
4. Berry transport requires a connection/path/parallel-transport construction
   and a physical endpoint-frame law. The file proves only the group action
   identity conditional on compatible frames.
5. Selector, rigidifier, and readout countermodels prove logical separation,
   not realization by any cosmological or physical sector.

## Verification

Run from `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

Toolchain: Lean `4.33.1`, Lake `5.0.0`, Mathlib `v4.33.1`.

Final result on 2026-08-24: exit code `0`; `Build completed successfully
(8708 jobs).` No Lean diagnostics were emitted. A bounded source scan found no
`sorry` or `axiom` declarations in `MariciFormal/` or `MariciFormal.lean`.
