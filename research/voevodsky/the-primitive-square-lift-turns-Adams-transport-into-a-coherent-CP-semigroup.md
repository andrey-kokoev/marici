# The primitive-square lift turns Adams transport into a coherent CP semigroup

The weighted Adams arrow

\[
A_r:H_k\longrightarrow H_{rk}
\]

is contractive but not a positive self-adjoint operator. Its correct positive lift acts one observer phase higher, on square observables:

\[
\boxed{
\mathcal E_r(X)=A_r^*XA_r.
}
\]

Every \(\mathcal E_r\) is completely positive. If \(X\geq0\), then

\[
\mathcal E_r(X)
=
(X^{1/2}A_r)^*(X^{1/2}A_r)
\geq0.
\]

Unlike the polar modulus, this lift preserves transported Adams composition. Since

\[
A_sA_r=A_{sr},
\]

one has

\[
\mathcal E_r(\mathcal E_s(X))
=
A_r^*A_s^*XA_sA_r
=
A_{sr}^*XA_{sr}
=
\mathcal E_{sr}(X).
\]

Thus primitive transport and primitive-square positivity coexist without forcing the directional arrow itself to be self-adjoint.

## Coherence interpretation

This realizes the proposed rung architecture:

1. the primitive phase carries the directed Adams arrow \(A_r\);
2. the primitive-square phase carries \(X\mapsto A_r^*XA_r\);
3. rung-four positivity is automatic because conjugation is completely positive;
4. higher Adams coherence follows from composition of the primitive arrows.

This is stronger than taking \(|A_r|\): the modulus discarded the transported grade information and broke composition, while quadratic conjugation retains it.

## RH boundary

The constructed CP semigroup is indexed by multiplicative integer Adams grades. The Hausdorff/heat constructor requires continuous additive steps and source moments

\[
H(t+nh)=\omega_t(Y_h^n).
\]

The next comparison must therefore establish that the coupled endpoint--gamma--prime heat observer is a matrix coefficient of the Adams CP lift, or construct its continuous heat interpolation.

No such equality is currently proved. The CP lift supplies a genuine positive rung-four mechanism, but its identification with the Weil heat source remains the RH-bearing crossing.

## Verification

```text
python research/voevodsky/checkers/check_Adams_completely_positive_semigroup_lift.py
```

Artifacts:

- `research/voevodsky/checkers/check_Adams_completely_positive_semigroup_lift.py`
- `research/voevodsky/results/Adams_completely_positive_semigroup_lift.json`
