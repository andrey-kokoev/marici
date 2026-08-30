# The ordered inverse-derivative port converts a zero-mean source into an exact localized residual

## Correction of scope

The recent moment no-go applies to scalar Hilbert-tail evaluation after principal-value pushforward. It does not apply unchanged to the already source-derived ordered operator
\[
(Sh)(q)=\int_{\mathbb R}\operatorname{sgn}(v-q)h(v)\,dv,
\qquad
S=-2D^{-1},
\]
because this operator performs an exact antiderivative before arithmetic scalarization.

For \(h\in C_c^\infty(\mathbb R)\),
\[
(Sh)(q)
=
\int_q^\infty h(v)\,dv-\int_{-\infty}^q h(v)\,dv.
\]
If
\[
\int_{\mathbb R}h(v)\,dv=0,
\]
then
\[
(Sh)(q)=2\int_q^\infty h(v)\,dv=-2\int_{-\infty}^q h(v)\,dv.
\]
Hence \(Sh\) is itself compactly supported. One source moment cancellation removes the entire exterior tail, not merely its leading asymptotic coefficient.

## Exact derivative factorization

The strongest form occurs when
\[
h=D\varphi
\]
for \(\varphi\in C_c^\infty(\mathbb R)\). The two-sided inverse identity gives
\[
S D\varphi=-2\varphi.
\]

Thus
\[
\text{compact potential }\varphi
\xrightarrow{D}
\text{zero-mean ordered source }h
\xrightarrow{S}
-2\varphi
\]
is an exact localized return.

No infinite moment subtraction is required. The cancellation is nonperturbative because the source incidence factors through the derivative.

## Reconciliation with the no-go packets

Three statements remain valid:

1. Direct scalar Hilbert-transform tails with only finitely many cancelled moments remain algebraic.
2. A compact scalar front with all ordinary moments zero is zero.
3. Scalar cancellation of the universal two-chart principal-value coefficient kills its odd coordinate.

The ordered-port mechanism evades none of these by contradiction. It changes the order of operations:
\[
\text{source derivative incidence}
\longrightarrow
\text{inverse-derivative ordered port}
\longrightarrow
\text{localized residual}
\longrightarrow
\text{arithmetic aggregation}.
\]

The forbidden route was
\[
\text{principal-value scalar tail}
\longrightarrow
\text{finite asymptotic subtraction}
\longrightarrow
\text{aggregation}.
\]

## Canonical splitting candidate

The derivative exact sequence supplies a source-native singular/residual split. The singular coordinate is the constant-mode obstruction
\[
m_0(h)=\int h,
\]
while the residual lies in
\[
\operatorname{ran}D.
\]

On the compactly supported smooth core,
\[
\ker m_0=\operatorname{ran}D.
\]
Indeed, every compactly supported zero-mean \(h\) has the compactly supported primitive
\[
\varphi(q)=\int_{-\infty}^q h(v)\,dv.
\]

Therefore the earlier one-parameter splitting gauge is fixed if the source proves that the odd arithmetic incidence lands in \(\operatorname{ran}D\) and that the constant mode is routed separately to the wall/archimedean channel.

## Remaining theorem

For each prime label, construct
\[
I_{\mathrm{odd},p}
=
D J_p
\]
on one common rigged source domain, with:

- \(J_p\) source-derived rather than fitted;
- reciprocal and dilation covariance;
- the correct primitive first-cumulant coefficient;
- prime and cutoff naturality;
- continuity of \(S I_{\mathrm{odd},p}=-2J_p\);
- summability of the localized \(J_p\) after Euler half-density loading;
- separate typing of the constant-mode obstruction.

If this factorization holds, the primitive principal-value obstruction is not an infinite-moment problem. It is a derivative-incidence theorem.

## Hostile

A zero-mean condition verified only after scalar summation over primes is insufficient. Each labelled incidence must factor through \(D\) before aggregation. Otherwise cross-prime cancellation can hide a nonlocal tail.

## Frontier

The earliest positive target is now precise:
\[
\text{labelled two-chart odd incidence}
\longrightarrow
\operatorname{ran}D
\xrightarrow{S=-2D^{-1}}
\text{localized odd residual}.
\]

This is the first existing source-native mechanism capable of cancelling the full principal-value tail while retaining a nonzero odd state.
