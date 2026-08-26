# Distinction-preserving factorization

Owner: `marici.Buzzard`

Source locator: the opening theorem before `## Theta consequence` in
`research/strominger/distinction-preserving-completion.md`.

Strength: source-typed module factorization theorem and hostile countermodel.

## Formal statement

For linear maps `Q : V →ₗ[R] W` and `observation : V →ₗ[R] D`, define
`FactorsThrough Q observation` to mean that there is a linear map
`induced : W →ₗ[R] D` satisfying `induced.comp Q = observation`.

Lean proves:

1. Any such factorization implies
   `LinearMap.ker Q ≤ LinearMap.ker observation`.
2. If `Q` is surjective, factorization is equivalent to that kernel
   inclusion. The construction first descends through the canonical quotient
   by `ker Q`, then transports across the quotient-to-target linear
   equivalence supplied by surjectivity.

## Missing assumption and hostile model

For an arbitrary named target `W`, kernel inclusion alone is not sufficient
over general modules. Let both source and target be the integer module and let
`Q(x)=2x`, with the desired observation the identity. Both kernels are zero,
so kernel inclusion holds. A factor would have to be integer-linear and send
`2` to `1`, which is impossible.

Lean proves both that multiplication by two is nonsurjective and that no such
factorization exists.

Therefore Strominger's phrase “quotient or presentation map” needs one of:

- the canonical quotient target;
- an explicit surjectivity proof;
- a specified equivalence between the target and the quotient by `ker Q`;
- or additional extension data for behavior outside the image.

The original kernel criterion is exact after one of these typing choices is
fixed. It must not be stated for an arbitrary linear map without qualification.

## Assumptions

The general theorem assumes a commutative coefficient ring and additive
commutative modules. It does not require finite dimension or a field. The
hostile example intentionally uses coefficients in the integers; vector-space
extension intuition would hide the missing image/target datum.

No topology or continuity is formalized here. Strominger's later sequential
and uniform completion conditions remain separate analytic claims.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/FactorizationDescent.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

Results on 2026-08-25: targeted exit code `0` with no diagnostics; full build
completed successfully with `8736 jobs`. No site build or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/FactorizationDescent.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/distinction-preserving-factorization.md`
