# The forced Stokes–Wronskian diagonal is nuclear and regularizes the projective arithmetic rigging

## Question

Does the superexponential decay of the forced Stokes-to-Wronskian coefficient
prevent completion of the forward comparison on the source arithmetic rigging?

## Claim boundary

No. It prevents a bounded inverse in an unweighted Hilbert topology, but makes
the forward diagonal nuclear and strongly regularizing. The linear completed
comparison and its transpose action are therefore available on the declared
projective exponential source scale. This does not prove quadratic Green-form
intertwining or authorize an inverse comparison.

## Forced coefficient

For each prime, the faithful one-dimensional comparison has coefficient

\[
 \lambda_p=\frac{-\kappa_p}{2s_p}>0.
\]

The source estimates give, for every \(N>0\), a constant \(C_N\) such that

\[
 0<\lambda_p\le C_Np^{-N}.
\]

The sharper established majorant is superexponential in \(p^2\), but decay
faster than every power is sufficient below.

## Hilbert completion

Define the diagonal map on finitely supported prime packets by

\[
 Te_p=\lambda_pe_p.
\]

Choose \(N>1\). Then

\[
 \sum_p|\lambda_p|
 \le C_N\sum_p p^{-N}<\infty.
\]

Hence \(T\) is trace class, therefore nuclear, on unweighted \(\ell^2\). It is
compact and injective, but not bounded below because \(\lambda_p\to0\).
Consequently its range is not closed unless the source coordinate is retained.

## Projective exponential source

On the prime-labelled primitive rung, use seminorms

\[
 q_\delta(x)=\sum_p p^\delta|x_p|,
 \qquad \delta>0.
\]

For every \(\delta\),

\[
 q_\delta(Tx)
 =\sum_pp^\delta\lambda_p|x_p|
 \le \left(\sup_pp^\delta\lambda_p\right)q_0(x).
\]

More generally, for any source rung \(q_\varepsilon\),

\[
 q_\delta(Tx)
 \le\left(\sup_pp^{\delta-\varepsilon}\lambda_p\right)
 q_\varepsilon(x).
\]

The supremum is finite for every pair \(\delta,\varepsilon\). Thus

\[
 T:\mathcal A_{\exp}\to\mathcal A_{\exp}
\]

is continuous and improves every polynomial or finite exponential-in-log
weight.

## Strong-dual regularization

A coefficient row of finite exponential order obeys

\[
 |x_p|\le Cp^a
\]

for some \(a\). For every \(\delta>0\), choose \(N>a+\delta+2\). Then

\[
 \sum_pp^\delta|\lambda_px_p|
 \le CC_N\sum_pp^{a+\delta-N}<\infty.
\]

Therefore multiplication by \(\lambda\) maps every finite-order strong-dual
row into the projective test space:

\[
 T:\mathcal A_{\exp}'^{\,\mathrm{fin}}\longrightarrow\mathcal A_{\exp}.
\]

This is stronger than mere continuity on the Hilbert middle rung.

## Cutoff naturality and labels

For the prime cutoff \(P_X\), diagonality gives

\[
 TP_X=P_XT.
\]

Thus finite packets converge in every declared target seminorm and the forward
comparison preserves prime labels. Primitive, square, and connected grades may
carry separate coefficient sequences; the argument applies gradewise whenever
the corresponding forced coefficient has the same superpolynomial decay.
No grade codiagonalization is implied.

## Adjoint direction

On \(\ell^2\), \(T^*=T\) because \(\lambda_p\) is real positive. On the rigged
pairing, the transpose is defined by

\[
 \langle Tx,y\rangle=\langle x,T^\times y\rangle.
\]

The same diagonal formula defines \(T^\times\), with domain and codomain read in
the opposite test/dual direction. Nuclear forward regularization does not make
\(T^{-1}\) continuous.

## G4 consequence

The linear Stokes-to-Wronskian port can be completed forward with its forced
normalization; superexponential smallness is not a domain obstruction. The
remaining comparison theorem is quadratic:

- identify the exact G4 source and target port metrics;
- prove the completed polarized Green form is transported by this forward map;
- retain the source coordinate so compactness does not become false closed
  range;
- combine it with the stratified reciprocal response action.

Only after those steps is the final joint-column adjoint frozen.

## Disposition

The forward Stokes--Wronskian diagonal is a canonical nuclear regularizer on the
projective arithmetic rigging. Its lack of a bounded inverse is an expected
feature, not a failure of linear completion. Quadratic functoriality and the
Xi-divisibility identity remain open. No RH conclusion is authorized.
