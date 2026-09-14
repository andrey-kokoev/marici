# The Adams modulus is positive but loses Hausdorff semigroup coherence

Given the weighted Adams shift \(A_r\), its polar modulus

\[
Y_r=|A_r|=(A_r^*A_r)^{1/2}
\]

is a positive contraction. This repairs the operator-order defect of \(A_r\).

However, Adams cocycle composition is transported through grade reindexing:

\[
\rho_{sr}(p,k)
=
\rho_r(p,k)\rho_s(p,rk).
\]

The fixed-carrier modulus product instead uses

\[
\rho_r(p,k)\rho_s(p,k),
\]

which is generally different.

For \(p=4,k=1,r=2,s=3\),

\[
\rho_6(4,1)=\frac1{192},
\]

while

\[
\rho_2(4,1)\rho_3(4,1)=\frac1{48}.
\]

The transported cocycle gives the correct \(1/192\), but the moduli on one fixed grade do not.

Thus

\[
Y_{sr}\neq Y_sY_r.
\]

Taking the polar modulus makes every individual Adams edge positive but destroys the source composition law required of the Hausdorff filters:

\[
Y_{h_1+h_2}=Y_{h_1}Y_{h_2}.
\]

This confirms that positivity at each edge and coherence of the original directed shift do not automatically coexist after forgetting the directional part. A valid binary filter must be constructed on a carrier where positivity and semigroup composition hold simultaneously.

## Verification

```text
python research/voevodsky/checkers/check_Adams_modulus_semigroup_failure.py
```

Artifacts:

- `research/voevodsky/checkers/check_Adams_modulus_semigroup_failure.py`
- `research/voevodsky/results/Adams_modulus_semigroup_failure.json`
