# 2701 — The Canonical Rank-Twenty-Six Source Derivative Is Fixed Coefficientwise

## Frozen source

Write the coefficient of the five-pole source form as

\[
F
=
\frac{N K_{\rm CM}^{5}}
{q_{\mathcal G_1}q_{\mathcal G_2}q_{\mathcal G_3}
 q_{\mathcal G_{23}}q_{\mathcal G_{31}}},
\qquad
N=q_{\mathcal G_{23}}+q_{\mathcal G_{31}}.
\]

The canonical first-order source extension in external direction (j) is obtained without choosing a quotient representative:

\[
\partial_j\log F
=
\frac{\partial_jN}{N}
+5\frac{\partial_jK_{\rm CM}}{K_{\rm CM}}
-\sum_i\frac{\partial_jq_i}{q_i}.
\]

## Exact coefficient audit

The complete unspecialized formulas give:

- in the (x)-direction, (partial_xN=-1), with marked-pole derivatives on (q_{\mathcal G_2}) and (q_{\mathcal G_{23}});
- in the (y)-direction, (partial_yN=-1), with marked-pole derivatives on (q_{\mathcal G_1}) and (q_{\mathcal G_{31}});
- in the (z)-direction, (partial_zN=0), with marked-pole derivatives on (q_{\mathcal G_1},q_{\mathcal G_2},q_{\mathcal G_3}).

Symbolic differentiation verifies that (K_{\rm CM}) has total degree (6), every (q_i) and (N) has degree (1), and their derivatives have degrees (5) and (0), respectively.

The source coefficient has weight

\[
1+30-5=26.
\]

Including (da\wedge db) gives source-form weight (28). Every canonical external derivative has coefficient weight (25), hence form weight (27).

## Result

The dual-number coefficient required by Entry 2697 is now fixed term-by-term by the frozen source. It is not selected by the desired Euler recurrence, by sparsity, or by a quotient section.

This establishes the characteristic-zero source derivative but not yet its equality with the finite de Rham connection implementation.

## Artifacts

- `research/benincasa/check_rank26_canonical_source_derivative.py`
- `research/benincasa/rank26-canonical-source-derivative.json`

Run the checker with:

```text
uv run --with sympy python research/benincasa/check_rank26_canonical_source_derivative.py
```

## Next falsifier

Insert the canonical coefficient derivatives into the complete finite presentation and verify in all three directions that

\[
P_1^2\nabla_jD_0+P_2^2\nabla_jD_1+P_3^2\nabla_jD_2
=27D_j
\]

after quotient reduction. A mismatch would localize the failure in the finite Gauss--Manin adapter rather than in source homogeneity.
