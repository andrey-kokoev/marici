# Constructor-stable endpoint completion

Owner: `marici.Buzzard`

Source locator: `Constructor-stable endpoint completion` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

The source space is the rational finite-packet module `Nat →₀ Rat`. The base
endpoint `L` reads coordinate zero. The authorized constructor is

`A(x) = (sum_j x_j) e₀`.

The first orbit endpoint is the linear functional `L ∘ A`. For the singleton
packet `e₁`, Lean proves

`L(e₁) = 0`, while `(L ∘ A)(e₁) = 1`.

Consequently the kernel of `L` is not contained in the kernel of `L ∘ A`.
Using the previously formalized factorization theorem, Lean concludes that
`L ∘ A` cannot factor through the single endpoint presentation `L`.

Adding the constructor-orbit endpoint detects this exact hostile packet. The
orbit port is therefore forced by descent preservation, not an optional
duplicate of the original endpoint.

## Interpretation boundary

This proves the algebraic gate underlying the topology claim. It does not by
itself construct the weakest locally convex topology, prove continuity of all
constructors, or form the diagonal product completion.

A faithful general upgrade needs:

- a typed source monoid of authorized constructors;
- a representation into continuous linear endomorphisms;
- composition orientation and identity laws;
- bulk and endpoint target seminorms;
- the orbit-indexed topology and its universal property;
- the diagonal evaluation map, product topology, and closure/completion;
- recurrence or observability-rank witnesses for any finite-orbit claim.

The current theorem specializes the single-constructor hostile while reusing
the general kernel/factorization interface. It does not assert that all sector
constructor monoids share one presentation.

Finitely supported rational constructors are marked noncomputable because the
available implementation uses classical decidable equality. This does not
weaken the proved propositions.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/ConstructorStableEndpoint.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without warnings or diagnostics. No site build
or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/ConstructorStableEndpoint.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/constructor-stable-endpoint.md`
