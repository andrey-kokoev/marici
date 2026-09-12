# Pfaffian reversal descends exactly to the residual Clifford swap

## Geometric reversal

For an odd ordered block with multiplicative coordinates

\[
y_0,\ldots,y_{2m},
\]

define reversed reciprocal coordinates

\[
y_i'=y_{2m-i}^{-1}.
\]

This combines order reversal with inversion of displacement weight. The resulting chain matrix is

\[
M'=-P^TMP,
\]

where \(P\) reverses the basis order.

## Cofactor state

For an odd skew matrix, the canonical residual is

\[
u_i=(-1)^i\operatorname{Pf}(M_{\widehat i}).
\]

Under congruence and scalar negation,

\[
\operatorname{cof}(-P^TMP)
=(-1)^m\det(P)P^T\operatorname{cof}(M).
\]

For a reversal of \(2m+1\) entries,

\[
\det(P)=(-1)^m.
\]

The two signs cancel. Therefore

\[
\boxed{
u'=P^Tu.}
\]

There is no residual phase.

## Charge intertwining

The effective charges satisfy

\[
q_{\rm out}(u)=\sum_i\frac{u_i}{y_i},
\qquad
q_{\rm in}(u)=\sum_i u_i y_i.
\]

Using \(u_i'=u_{2m-i}\) and \(y_i'=y_{2m-i}^{-1}\) gives

\[
q_{\rm out}(u')=q_{\rm in}(u),
\qquad
q_{\rm in}(u')=q_{\rm out}(u).
\]

Hence retyping commutes strictly with reversal:

\[
\boxed{
\operatorname{Retype}(\operatorname{Rev}_{\rm Pf}X)
=
R_{\rm Cl}\operatorname{Retype}(X).
}
\]

The primitive-level Pfaffian reversal and residual-level Clifford swap are the same symmetry seen before and after minimalization.

## Consequence

The two fermionic structures are not merely analogous:

- exterior/Pfaffian orientation acts on the microscopic primitive block;
- Clifford reversal acts on the effective incoming/outgoing double;
- the cofactor-and-charge retyping map intertwines them exactly.

Thus no extra sign, metaplectic lift, or fitted comparison is required for finite odd blocks under this geometric reversal convention.

## Verification

The checker verifies exact cofactor reversal and charge exchange in 100 rational cases of odd sizes one through nine:

```text
python research/coherence/check_pfaffian_residual_clifford_intertwiner.py
```

Artifacts:

- `check_pfaffian_residual_clifford_intertwiner.py`
- `pfaffian-residual-clifford-intertwiner.v1.json`
