# RH is rung-four positive observation coherence on the forward plane

## Forward system

Let \(X_k\) be the finite Gaussian-translate packet space at stage \(k\), with forward extension

\[
u_k:X_k\longrightarrow X_{k+1},
\qquad
u_k(c_1,\ldots,c_k)=(c_1,\ldots,c_k,0).
\]

Let \(G_k\) be the source-derived Weil Gram matrix and define the rung-three observation

\[
O_k(c)=c^*G_kc.
\]

This is the observation point attached to stage \(k\).

## Rung-four cell

Because \(G_k\) is the principal restriction of \(G_{k+1}\),

\[
O_{k+1}(\nu_kc)=O_k(c).
\]

This equality is the successor coherence cell joining the observation at \(k\) to the same observation at \(k+1\).

The RH-bearing version is cone-valued:

\[
O_k(c)\in\mathbb R_{\geq0}
\]

for every \(k\) and every \(c\), while every successor cell commutes.

Thus the proposed placement is:

1. the forward packet system supplies the coherence plane;
2. \(O_k\) is the rung-three observation point;
3. compatibility of \(O_k\) and \(O_{k+1}\) is rung-four coherence;
4. RH is the assertion that this complete rung-four system lands in the positive cone and survives faithful completion.

## Why ordinary coherence is insufficient

Principal restrictions commute for every fixed Hermitian kernel, including indefinite kernels. The checker retains an exact hostile with off-diagonal entry \(-3/5\):

- rank one is positive;
- every rank-two principal packet is positive;
- the successor restriction cells commute exactly;
- at rank three, the all-ones vector has value \(-3/5\).

Therefore an RH failure appears as a first **cone-admission failure**, not necessarily as failure of the signed successor equation.

## Why positivity alone is insufficient

The observations

\[
O_k(c)=|c_1|^2
\]

are positive and successor-coherent at every stage but ignore every later coordinate. Hence a nonzero invisible completed sector remains.

The complete RH contract requires all four conditions:

1. **source identity:** \(O_k\) is exactly the endpoint–gamma–prime Gaussian Weil form;
2. **cone admission:** \(O_k\geq0\) at every finite stage;
3. **rung-four coherence:** \(O_{k+1}\nu_k=O_k\);
4. **faithful completion:** the Gaussian translate union is dense and the continuous completed observer has no unintended invisible sector.

Under the standard Weil criterion, these conditions are equivalent to RH.

## Interpretation

The concise architectural statement is:

> RH is the cone-valued rung-four coherence of the rung-three Weil observation along the completed forward coherence plane.

This is a placement theorem, not yet a proof of cone admission. It identifies exactly where an off-critical zero must manifest: at a least finite stage where the otherwise coherent observation exits the positive cone.

## Verification

```text
python research/voevodsky/checkers/check_rung4_positive_observation_coherence.py
```

Artifacts:

- `research/voevodsky/checkers/check_rung4_positive_observation_coherence.py`
- `research/voevodsky/results/rung4_positive_observation_coherence.json`
