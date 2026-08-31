# Projective signed late diagonal loading remains faithful under the radial codiagonal

## Question

Does the finite signed-shell independence extend to an infinite projective loading?

## Claim boundary

Yes for a projectively summable family of distinct sufficiently late shell endpoints. Every nonzero coefficient family has a least active endpoint. The explicit double-exponential tail supplies a summable majorant after division by that shell, so dominated convergence extracts its coefficient. Repeating the argument proves all coefficients vanish.

## Ordered projective packet

Let

\[
a_1<a_2<\cdots,
\qquad a_j\longrightarrow\infty,
\]

be late shell endpoints, and let \(\rho_j\) be their diagonal autocorrelations. Assume the coefficient packet satisfies every exponential moment,

\[
\sum_j |c_j|e^{\delta a_j}<\infty
\]

for all \(\delta>0\). The loaded radial state is

\[
\rho_c(t)=\sum_{j\ge1}c_j\rho_j(t),
\]

with convergence in every declared rapid radial seminorm.

Kernel membership forces

\[
\rho_c(t)=0
\]

because the loaded derivative source vanishes and rapid decay removes the constant.

## Least active endpoint

If \(c\ne0\), the active index set

\[
A=\{j:c_j\ne0\}
\]

is a nonempty subset of the positive integers and therefore has a least element \(j_0\). No assumption about a largest active shell is needed.

Divide by the slowest-decaying active autocorrelation:

\[
0=
\frac{\rho_c(t)}{\rho_{j_0}(t)}
=c_{j_0}
+
\sum_{j>j_0}c_j
\frac{\rho_j(t)}{\rho_{j_0}(t)}.
\]

## Uniform tail majorant

The explicit completed-theta endpoint bounds give, for sufficiently large \(t\),

\[
\left|
\frac{\rho_j(t)}{\rho_{j_0}(t)}
\right|
\le
C_{j_0}e^{M a_j}
\exp\left[
-c\left(e^{2a_j}-e^{2a_{j_0}}ight)e^{2t}
\right]
\]

with fixed \(c>0\) and finite \(M\). Polynomial label and endpoint factors are absorbed into \(e^{Ma_j}\); higher completed-theta labels carry an additional superexponential penalty.

Fix one sufficiently large \(T\). For \(t\ge T\), the right side is bounded by

\[
C_{j_0}e^{Ma_j}
\exp\left[-c_T e^{2a_j}ight]
\]

after changing the constant for the finitely many nearest endpoints. This is summable against \(|c_j|\); indeed the double exponential dominates every projective exponential weight.

For each fixed \(j>j_0\), the ratio tends to zero as \(t\to+\infty\). Dominated convergence therefore gives

\[
\lim_{t\to+\infty}
\sum_{j>j_0}c_j
\frac{\rho_j(t)}{\rho_{j_0}(t)}
=0.
\]

Hence

\[
c_{j_0}=0,
\]

contradicting the definition of \(j_0\). Thus no nonzero projective packet can lie in the codiagonal kernel.

## Result

For distinct sufficiently late diagonal shells,

\[
\ker(DJ_{\rm or})
\cap
\mathcal A_{\exp}^{\rm diag,late}
=\{0\}.
\]

The radial codiagonal is therefore faithful on the full projective signed late-diagonal source, not only on finite cutoffs or positive coefficients.

## Strength boundary

This argument still excludes:

- repeated endpoints carrying different internal theta labels;
- finitely many early or transition shells, which can be handled separately only after a finite independence audit;
- ordered off-diagonal pair histories;
- a G4 metric that couples the source after codiagonalization.

The result concerns the source codiagonal, not an undeclared G4 return.

## Direction rescore

- Infinite projective signed late-diagonal loading: completed.
- Finite early-shell attachment: 8/10; needs finite determinant or asymptotic independence.
- Repeated-endpoint internal labels: 7/10.
- Ordered off-diagonal packets: 7/10.
- G4 radical comparison: interface-blocked.

## Disposition

Projective completion introduces no new signed diagonal null packet on the late-shell sector. Any G4 radical removing such a source must arise after the source codiagonal, through a separately declared metric, gauge relation, or compression. No RH conclusion is authorized.
