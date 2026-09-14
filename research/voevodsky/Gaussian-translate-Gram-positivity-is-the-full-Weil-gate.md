# Gaussian translate Gram positivity is the full Weil gate

## Density theorem

Fix one positive width and let \(g\) be the corresponding Gaussian. Translation finite differences converge in every Schwartz seminorm to derivatives of \(g\). The derivatives are Hermite polynomials multiplied by \(g\), and finite Hermite expansions are dense in Schwartz space.

Therefore

\[
\overline{\operatorname{span}\{T_ag:a\in\mathbb R\}}^{\mathcal S}
=
\mathcal S(\mathbb R).
\]

Allowing multiple widths is unnecessary for density, although it remains useful for the heat-semigroup organization.

## Positivity theorem

Let \(Q_W\) be the continuous Hermitian Weil form on Schwartz space. Let

\[
K(a,b)=Q_W(T_ag,T_bg).
\]

Then the following are equivalent:

1. every finite matrix \((K(a_j,a_k))\) is positive semidefinite;
2. \(Q_W\) is nonnegative on the linear span of Gaussian translates;
3. \(Q_W\) is nonnegative on all of Schwartz space.

The first two statements are the definition of Gram positivity. The third follows from Schwartz density and continuity; its restriction gives the reverse implication.

After attaching the standard Weil criterion and verifying the exact source normalization, these conditions are equivalent to RH.

## Consequence for the current program

The explicit polarized Gaussian kernel and its Fourier-restriction map are not merely preliminary finite probes. Proving all of their Gram matrices positive would prove the full Weil criterion.

Thus no abstraction should claim that Gaussian Gram positivity is an easier compactness lemma. It is the RH-bearing cell itself.

Closability on the order completion remains mathematically meaningful, but it cannot manufacture positivity. Even a successful closed-form realization would leave the sign of the Gaussian Gram matrices as the decisive theorem.

## Verification

```text
python research/voevodsky/checkers/check_gaussian_translate_schwartz_core.py
```

The checker verifies the finite-difference moment identities through derivative order eight. The Schwartz convergence and Hermite density steps are analytic theorems stated explicitly in the result artifact.

Artifacts:

- `research/voevodsky/checkers/check_gaussian_translate_schwartz_core.py`
- `research/voevodsky/results/gaussian_translate_schwartz_core.json`
