# Formalization sprint 3 — partial report

Status: generic layer complete; exact Ising-matrix certification blocked on the
referenced Kitaev source artifact.

## Compiled generic results

Source: `marici_formal/MariciFormal/Sprint3.lean`.

- `FiniteFusionSystem` records finite labels, fusion multiplicities, a finite
  fusion space, associator, braidings, and separate pentagon/hexagon
  propositions. `FiniteFusionSystem.Coherent` requires proofs of those
  propositions; coherence is not inferred from ranks or matrices.
- `fusionProbe_descends_iff` and `fusionFamily_descends_iff` reuse canonical
  quotient descent: every probe must kill the declared quotient submodule.
- `fusion_disappearance_mechanisms_distinct` combines explicit access-denial,
  readout-loss, and constitutive-collapse witnesses without identifying them.
- `AccessInterface` keeps point separation and operator generation as separate
  conditions. `point_separation_does_not_imply_operator_generation` combines
  jointly faithful coordinate probes with the proved non-generation of the
  off-diagonal coordinate swap.
- `CondensationSuccessor` names nested repair submodules and their canonical
  successor map. `representative_dies_iff` gives the death criterion;
  `map_comp` states that composition needs the two nesting witnesses and uses
  no complement or splitting.

## Assumption classes

| Layer | Explicit assumptions | Status |
|---|---|---|
| fusion | commutative coefficient ring, finite labels, multiplicities, fixed finite fusion space, linear equivalences | algebraically typed |
| coherence | separate pentagon and hexagon propositions plus proof fields | parameterized; not source-certified |
| descent | module quotient and kernel inclusion | fully algebraic |
| access | probe family and constructor endomorphism set | fully algebraic; physical accessibility absent |
| condensation | nested source-approved repair submodules | fully algebraic conditional on the nesting datum |
| Ising | exact coefficient field, basis order, gauge convention, `F` and `R` matrices, identities to certify | blocked: source artifact absent |

## Missing frozen data

No file currently under `research/kitaev/` contains Ising fusion rules or
explicit Ising `F`/`R` matrices. The available source files are toric-code
artifacts; `toric-code-braiding-boundaries-perturbation.md` explicitly says
that non-Abelian braiding is outside its scope.

Exact ingestion requires the Kitaev-owned path and, within it:

1. coefficient field or exact algebraic extension;
2. ordered bases for each multiplicity/fusion space;
3. associator matrix convention and direction;
4. braid orientation and `R`-phase convention;
5. exact finite identities intended for certification.

Standard Ising matrices were not supplied from memory because gauge and phase
conventions materially change the formal statement.

## Current verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

Current result: `Build completed successfully (8710 jobs)` with no Lean
diagnostics. This verifies the generic layer only, not the missing Ising
matrix identities.
