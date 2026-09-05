# Rational natural-ceiling construction blocker

## Question

What is the first unchecked arithmetic object required to inhabit `RawRationalNaturalCeiling` for Cubical Agda's preferred rational carrier?

## Claim boundary

The preferred carrier represents a rational by an integer numerator `a` and a positive denominator `b`. Its order reduces a representative inequality

\[
[a/b] \le [c/d]
\]

to an integer cross-product inequality. A raw natural ceiling therefore requires, for every `a` and `b`, a natural `n` and a proof

\[
a \le \operatorname{pos}(n)\,b,
\]

together with the checked identification between the recursively defined `natℚ n` and the preferred rational class `[pos n / 1]`.

The numerator cases separate constructively:

- For `a = negsuc k`, choose `n = 0`; the remaining integer fact is `negsuc k ≤ 0`.
- For `a = pos k`, choose `n = k`; the remaining integer fact is `pos k ≤ pos k · b`, using positivity of `b`.

Inspection of Cubical Agda 0.9 found the relevant integer ingredients in `Cubical.Data.Int.Order`: `negsuc<-zero`, `<-weaken`, `zero-≤pos`, `suc-≤-suc`, and multiplication monotonicity `≤-·o`. The rational order's representative reduction is visible in `Cubical.Data.Rationals.Order`: `[a/b] ≤ [c/d]` uses `a·d ≤ c·b`.

This packet does not claim that the Agda terms elaborating those two cases have been constructed. It also does not claim that `natℚ n ≡ [pos n / 1]` is definitional; that comparison must be proved or located in the library.

## Disposition

The first missing typed object is a checked lemma

```agda
natℚ-representative : (n : ℕ) → natℚ n ≡ Q.[ pos n / 1 ]
```

or an existing library theorem with that type. After it is available, acceptance requires a background-safe Agda check of a `RawRationalNaturalCeiling` inhabitant with both integer constructor cases and no postulate.

Candidate terms for `natℚ-representative`, both integer numerator cases, and `preferredCompletionMultiplication` are now authored. They remain unverified. Until a background-safe Agda check succeeds, `preferredCompletionMultiplication` may not be presented as constructed unconditional multiplication.
