# The doubled half-line derivative realizes the full rigged Green--Real boundary ladder

## Question

Can the abstract rigged-boundary contract be realized by a concrete radial differential system in which the transpose, graph adjoint, ambient failure, Green form, reciprocal comparison, and Real wall are all explicit?

## Claim boundary

The model is the doubled first derivative on the half-line with Schwartz-type test functions and \(H^1\) graph domain. It realizes the analytic and boundary constructors exactly. It is a mathematical radial model, not a sourced laboratory Hamiltonian or calibrated physical record system.

## Rigged ladder

Let

\[
\mathcal S_+
=
\{f|_{[0,\infty)}:f\in\mathcal S(\mathbb R)\},
\]

equipped with its quotient Schwartz topology. Set

\[
\Phi=\mathcal S_+\oplus\mathcal S_+,
\qquad
H=L^2(0,\infty)\oplus L^2(0,\infty),
\]

and

\[
\mathcal E=H^1(0,\infty)\oplus H^1(0,\infty).
\]

Then

\[
\Phi\hookrightarrow\mathcal E\hookrightarrow H
\hookrightarrow\mathcal E'\hookrightarrow\Phi'
\]

continuously and densely. Here \(\Phi'\) contains half-line tempered distributions, including the endpoint delta.

## Differential row

Define

\[
D=
\begin{pmatrix}
\partial_r&0\\
0&-\partial_r
\end{pmatrix}
\]

on \(\mathcal E\). The graph norm is equivalent to the standard doubled \(H^1\) norm:

\[
\|f\|_D^2
=
\|f\|_2^2+\|Df\|_2^2.
\]

The opposite derivative signs encode the two radial orientations algebraically; no physical-time interpretation is assigned.

## Boundary trace and Green form

Define

\[
\gamma:\mathcal E\to\mathbb C^2,
\qquad
\gamma(f_+,f_-)=(f_+(0),f_-(0)).
\]

The one-dimensional trace theorem makes \(\gamma\) bounded on \(\mathcal E\). It is also continuous on \(\Phi\).

For \(f,g\in\Phi\), integration by parts gives

\[
\langle Df,g\rangle_H
+
\langle f,Dg\rangle_H
=
\langle J_\partial\gamma f,\gamma g\rangle_{\mathbb C^2},
\]

with

\[
J_\partial=
\operatorname{diag}(-1,1).
\]

Thus the differential operator is formally skew relative to the boundary Green form. The formula extends to the appropriate maximal/minimal domain pairing, but that extension is not needed for the constructor audit.

## Continuous transpose and endpoint delta

On the test rung, the trace transpose is

\[
\gamma':(\mathbb C^2)'
\longrightarrow\Phi'.
\]

Under the standard finite-dimensional pairing,

\[
\gamma'(a,b)
=
(a\delta_0,b\delta_0).
\]

This is a distributional boundary row. The delta lies in \(\Phi'\), but not in the ambient Hilbert space \(H\).

## Explicit graph adjoint

Use the scalar \(H^1\) inner product

\[
\langle f,g\rangle_{H^1}
=
\int_0^\infty f\overline g\,dr
+
\int_0^\infty f'\overline{g'}\,dr.
\]

The Riesz representative of endpoint evaluation is

\[
k_0(r)=e^{-r}.
\]

Indeed, for \(f\in H^1(0,\infty)\),

\[
\int_0^\infty f(r)e^{-r}dr
-
\int_0^\infty f'(r)e^{-r}dr
=f(0).
\]

Therefore the doubled graph adjoint is

\[
\gamma^{*D}(a,b)
=
(ae^{-r},be^{-r}).
\]

Its range is two dimensional, and

\[
\gamma^{*D}\gamma
\]

is finite rank. Its graph Calkin class is zero.

The transpose and graph adjoint are related by the Riesz maps:

\[
\gamma'R_{\mathbb C^2}
=R_{\mathcal E}\gamma^{*D}.
\]

The left side is represented distributionally; the right side is the same functional represented through the graph metric.

## Ambient adjoint obstruction

There is no bounded trace

\[
L^2(0,\infty)\to\mathbb C.
\]

For example, let \(f_n\) be continuous triangular packets with

\[
f_n(0)=1,
\qquad
\operatorname{supp}f_n\subset[0,n^{-1}].
\]

Then

\[
\|f_n\|_{L^2}\to0
\]

while the trace remains one. Hence an ambient adjoint

\[
\gamma_H^*:\mathbb C^2\to H
\]

for a bounded ambient trace does not exist. The endpoint delta cannot be substituted for such an adjoint because \(\delta_0\notin H\).

## Reciprocal comparison

For \(u\in U(1)\), define on \(H\), \(\mathcal E\), and \(\Phi\)

\[
\mathcal W_u(f_+,f_-)
=
(u^{-1}f_-,uf_+).
\]

It is unitary on both the ambient and graph Hilbert rungs, preserves the test space, and satisfies

\[
\mathcal W_u^2=I,
\qquad
D\mathcal W_u=-\mathcal W_uD.
\]

On boundary values it induces

\[
W_u=
\begin{pmatrix}
0&u^{-1}\\
u&0
\end{pmatrix},
\]

with

\[
\gamma\mathcal W_u=W_u\gamma
\]

and

\[
W_u^*J_\partial W_u=-J_\partial.
\]

Thus the differential sign and Green sign agree as degree \((-,-)\).

The induced dual map sends endpoint deltas by the transpose reciprocal action. This is a map on \(\Phi'\), not an ambient operator on delta vectors.

## Fixed-fiber Real structure

Let \(K\) denote scalar complex conjugation and define

\[
\mathcal J_u
=
\operatorname{diag}(1,u^2)K
\]

on each rung. It is continuous on \(\Phi\), antiunitary on \(H\) and \(\mathcal E\), and induces a continuous dual action on \(\Phi'\). It satisfies

\[
\mathcal J_u^2=I,
\qquad
\mathcal J_u\mathcal W_u
=
\mathcal W_u\mathcal J_u,
\qquad
D\mathcal J_u=\mathcal J_uD.
\]

Boundary naturality is exact:

\[
\gamma\mathcal J_u=J_u\gamma.
\]

Dual naturality follows with the induced dual conjugation and the fixed pairing convention.

## Real wall domain

Define the boundary wall

\[
\Lambda_u
=
\{(c,uc):c\in\mathbb C\}.
\]

It is isotropic for \(J_\partial\):

\[
\langle J_\partial(c,uc),(c,uc)\rangle=0.
\]

It is fixed by both comparison structures:

\[
W_u\Lambda_u=\Lambda_u,
\qquad
J_u\Lambda_u=\Lambda_u.
\]

The operator domain

\[
\operatorname{Dom}D_{\Lambda_u}
=
\{f\in\mathcal E:\gamma f\in\Lambda_u\}
\]

is therefore reciprocal and Real invariant. The Green identity shows that the boundary form vanishes on this domain.

This is domain sewing, not an essential-observer theorem.

## Bulk observer separation

The boundary trace is finite rank and cannot control broad half-line packets. Add a bounded scalar or multiplicity-valued bulk multiplier \(M_W\). Then

\[
f\longmapsto(Df,M_Wf)
\]

is graph-bounded below exactly under the uniform local-mass criterion established in the half-line theorem, within its declared upper-regularity class.

The two roles remain separate:

- \(\gamma\) and \(\Lambda_u\): boundary domain and Green/Real coherence;
- \(M_W\): essential bulk observation;
- \(\gamma^{*D}\gamma\): finite-rank graph correction with zero Calkin class;
- \(\gamma'\): distributional boundary constructor.

## Constructor audit

| Object | Rung | Constructor role |
|---|---|---|
| \(\gamma\) | \(\Phi\to\mathbb C^2\), \(\mathcal E\to\mathbb C^2\) | test and graph trace |
| \(\gamma'\) | \((\mathbb C^2)'\to\Phi'\) | continuous transpose |
| \(\gamma^{*D}\) | \(\mathbb C^2\to\mathcal E\) | graph adjoint |
| \(\delta_0\) | element of \(\Phi'\) | boundary distribution |
| \(W_u\) | boundary fiber | Green comparison cell |
| \(\mathcal W_u\) | test, graph, ambient, and dual ladders | reciprocal comparison |
| \(\mathcal J_u\) | test, graph, ambient, and dual ladders | Real comparison |
| \(\Lambda_u\) | subspace of boundary fiber | sewn wall domain datum |
| \(M_W\) | graph to bulk record | essential observer when thickness holds |

## Deliberate failures

1. Replacing \(\gamma'\delta\) by an ambient vector fails because \(\delta_0\notin L^2\).
2. Replacing \(\gamma^{*D}\) by an ambient adjoint fails because the ambient trace is unbounded.
3. The finite-rank graph Gramian does not provide an essential Calkin margin.
4. Formal boundary covariance alone does not prove invariance of an operator domain; the wall condition must be checked.
5. Reciprocal anti-commutation with \(D\) does not imply physical-time reversal.
6. The mathematical graph metric is not a calibrated physical metric.

## Disposition

The doubled half-line derivative realizes every rung and constructor in the rigged-boundary contract. Endpoint delta is the transpose image, \(e^{-r}\) is its graph-Riesz representative, and no bounded ambient trace exists. Reciprocal and Real comparisons act coherently on test, graph, ambient, boundary, and dual rungs; the wall \(\Lambda_u\) is invariant and Green-isotropic. Essential bulk stability still comes only from an independent thick multiplier.
