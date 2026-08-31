# Reflection, trace, and graph differentiation close the remaining Evans residual port riggings

## Question

After the ordinary and ordered-linking mixed blocks are controlled, can the
regular derivative, wall, and reciprocal components of the centered Evans
adjoint residual fail to lie in the arithmetic source space?

## Claim boundary

No, for the already declared first-order wall graph and reciprocal reflection.
All three ports are bounded graph maps with constants independent of the prime
cut scale. After the centered arithmetic half-density and source adjoint are
inserted, each produces a vector in \(U_{\rm ar}\), locally uniformly on compact
parameter sets. Their values and cancellation remain open.

## Common Evans graph

At every Xi zero, the exact history satisfies

\[
 u_z\in H^1(\mathbb R).
\]

Use the norm

\[
 \|u\|_{G,\rm wall}^2
 =\|u\|_2^2+\|u'\|_2^2+|u(0)|^2,
\]

or the boundedly equivalent resolved-plus-wall norm already selected by the
source construction.

For compact \(K\subset\mathbb C\), superexponential theta decay gives

\[
 \sup_{z\in K\cap Z(\tau)}\|u_z\|_{G,\rm wall}<\infty.
\]

## Regular derivative port

The map

\[
 D:H^1(\mathbb R)\to L^2(\mathbb R),
 \qquad Du=u',
\]

has norm at most one relative to the graph norm. The regular derivative part
of every cut atom has scale-independent \(L^2\) norm \(\|\Phi'\|_2\).
Therefore

\[
 |\langle D_{\rm reg}c_a,Du_z\rangle|
 \le \|\Phi'\|_2\|u_z'\|_2
\]

uniformly in the cut scale \(a\).

## Wall port

The one-dimensional Sobolev trace theorem gives

\[
 |u(0)|\le C_{\rm tr}\|u\|_{H^1}.
\]

The cut-atom jump is the fixed scalar \(-\Phi(0)\), independent of \(a\).
Hence

\[
 |\Phi(0)u_z(0)|
 \le |\Phi(0)|C_{\rm tr}\|u_z\|_{H^1}
\]

uniformly in \(a\).

Retaining this scalar as a separate wall coordinate avoids treating a delta
distribution as an \(L^2\) vector.

## Reciprocal port

Define reflection by

\[
 (Ru)(q)=u(-q).
\]

Then

\[
 \|Ru\|_2=\|u\|_2,
 \qquad
 \|(Ru)'\|_2=\|u'\|_2,
 \qquad
 (Ru)(0)=u(0).
\]

Thus \(R\) is unitary on the whole-line wall graph. Reciprocal exchange of the
left and right half-density histories is therefore bounded with no cut-scale
loss. Its odd sign changes orientation but not norm.

Any source-declared unit-modulus Fourier--Poisson multiplier composed with
this reflection remains bounded. A multiplier not proved unitary on the
retained graph is not covered by this statement.

## Arithmetic summability

Let \(P_p^{(j)}(u_z)\) denote any of the regular derivative, wall, or reciprocal
pairings above. Each obeys

\[
 \sup_p|P_p^{(j)}(u_z)|
 \le C_j\|u_z\|_{G,\rm wall}.
\]

The corresponding centered arithmetic coordinate has the form

\[
 r_{p}^{(j)}(z)
 =\frac{p^{-1/2}P_p^{(j)}(u_z)}{\log p}.
\]

Therefore

\[
 \|r^{(j)}(z)\|_U^2
 \le C_j^2\|u_z\|_{G,\rm wall}^2
 \sum_p\frac1{p\log p}<\infty.
\]

The estimate is locally uniform on compact subsets of the Xi divisor.

## Parameter-root vectors

For a zero of multiplicity \(m\), every root vector
\(\partial_z^ku(\cdot;z_0)\), \(0\le k<m\), lies in \(H^1\). The derivative,
wall, and reciprocal estimates apply without change. Thus every corresponding
multiplicity residual is a defined vector in \(U\).

## Rigging status

For the centered Evans residual, the following components are now typed and
arithmetically summable:

- ordinary history overlap;
- regular derivative overlap;
- wall response;
- reciprocal history;
- ordered linking polarization.

This removes limiting absorption and distributional domain failure as possible
explanations for the missing chain map on the current explicit Evans vector.

## Remaining obstruction

The complete residual

\[
 B_\Sigma^\dagger u_z
\]

is now a well-defined sum of source-typed \(U\)-valued components. Its
vanishing still requires the exact prime-shell identities

\[
 I_n^{(0)}+I_n^{(1)}+I_n^{({\rm wall})}
 +I_n^{({\rm recip})}+I_n^{({\rm link})}=0.
\]

Uniform boundedness and reciprocal unitarity do not supply these equalities.
The ordinary term remains eventually sign-definite.

## Disposition

The current Evans-to-Green obstruction is no longer a seam-rigging problem.
It is a source-normalized vector cancellation problem, together with the
stronger global Fourier--Poisson response-intertwining requirement. No RH
conclusion is authorized.
