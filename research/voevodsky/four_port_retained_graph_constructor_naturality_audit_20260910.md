# Four-port retained-graph constructor naturality audit

## Question

Which admitted constructor operations are already proved to preserve the completed odd retained graph, and where does the first unproved naturality square occur?

## Claim boundary

This audit classifies existing source results against one exact graph-preservation criterion. It does not infer a global coalgebra from separate commuting squares or pursue an RH conclusion.

## Universal criterion

Let

\[
K_p:E_{p,\theta}^{\rm odd}\to E_{p,\rm win}^{\rm odd}
\]

be the completed odd compression and

\[
\Gamma(K_p)=\{(y,K_py):y\in E_{p,\theta}^{\rm odd}\}.
\]

A source constructor \(T\) on the theta coordinate and a corresponding constructor \(U\) on the window coordinate preserve the graph precisely when

\[
UK_p=K_pT.
\]

Then

\[
(y,K_py)\longmapsto(Ty,UK_py)=(Ty,K_pTy)
\]

is a well-defined graph endomorphism. For constructors changing prime or grade, replace \(K_p\) by the corresponding target block and require

\[
U_{p,k\to q,\ell}K_{p,k}=K_{q,\ell}T_{p,k\to q,\ell}.
\]

This equation, not scalar covariance, is the coalgebra/naturality gate.

## Reciprocal reflection: closed

The map \(K_p\) was uniquely characterized by:

1. odd reciprocal character on source and target;
2. annihilation of the even wall line;
3. \(K_pj_\theta=d_p\).

Therefore

\[
R_{\rm win}K_p=K_pR_\theta.
\]

Reciprocal reflection preserves the graph strictly.

## Prime cutoff: closed

Every \(K_p\) is prime-labelled and

\[
\sum_p\|K_p\|_{\mathfrak S_1}<\infty.
\]

For prime projection \(P_X\),

\[
P_X^{\rm win}K=KP_X^\theta.
\]

Thus finite prime cutoffs are restrictions of the completed trace-class direct sum, and the odd graph is cutoff-natural.

## Analytic causal-history realization: closed

The coefficient-level map was fixed before the analytic comparison. Later causal evaluation proves

\[
\operatorname{Tr}_{\rm win}\mathfrak S_{1,p}
=
K_p\operatorname{Tr}_\theta
\]

on the declared history core, with the forced normalization

\[
d_p=-2j_\theta b_p.
\]

Hence the local causal/Stokes constructor realizes the same graph map; it does not introduce a second fitted odd comparison.

## Fixed/comoving odd frame change: closed

For source-derived scales \(a_k\), the comparison

\[
\Theta_k=\mathcal D_{a_k}
\]

is unitary and satisfies

\[
A_{r;k}^{\rm mov}\Theta_k
=
\Theta_{rk}A_{r;k}^{\rm fix}.
\]

It preserves the Weyl phase exactly. Therefore fixed versus comoving description is a natural unitary change of presentation, provided every observation map, including \(K\), is conjugated by \(\Theta\). It adds no independent holonomy.

This theorem compares two odd phase frames. It does not itself prove that Adams transport preserves the complete theta-to-window graph.

## Quadratic graph form: closed in the constructed direction

The form

\[
G_\Gamma(y)=G_\theta(y)+G_{\rm win}(Ky)
\]

retains the nondegenerate theta coordinate and adds a trace-class positive shadow. Since the theta odd radical is zero, radical compatibility is automatic on the one-dimensional odd source line. The direct-sum trace-class perturbation does not destroy graph closedness or the theta lower bound.

No completed inverse or output-metric isometry is present or required.

## Adams grade transport: first unproved full square

Adams transport is source-derived on grade labels and the odd phase fibers admit naturally equivalent fixed/comoving presentations. What is not supplied by the reviewed packets is the complete square

\[
U_{r;k}^{\rm win}K_{p,k}
=
K_{p,rk}T_{r;k}^{\theta}
\]

on the full primitive, square, connected, wall, and odd boundary packet with their respective graph domains.

The local phase cocycle and unitary frame comparison are necessary but insufficient: \(K_{p,k}\) includes the normalized theta endpoint covector and the Stieltjes disagreement generator, both of which must transform with the declared Adams grade law.

## Other constructor words

A global coalgebra requires closure under composites, not only generators. Once every generating square is proved, composite naturality follows algebraically. Without the Adams square, no statement about arbitrary constructor words is authorized.

Scalar Tate invisibility, Fourier character, and endpoint equality cannot substitute for this missing graph square because they may agree after forgetting the retained theta coordinate or the stratum topology.

## Acceptance test for the Adams square

For every admitted grade arrow \(k\to rk\):

1. define \(T_{r;k}^{\theta}\) on the theta odd graph domain;
2. define \(U_{r;k}^{\rm win}\) on the window disagreement graph domain;
3. verify both preserve prime labels and the three completion strata;
4. prove equality of the two composites on the source core;
5. prove graph-norm continuity with constants compatible under composition;
6. verify reciprocal reflection and prime cutoff squares commute with this comparison.

## Disposition

The four-port odd retained graph is already natural for reciprocal reflection, prime cutoff, analytic causal realization, and fixed/comoving frame equivalence. The first unproved generator-level coalgebra law is Adams preservation of the complete theta-to-window graph. Until its two actions are explicitly typed, another finite scalar check would be nonresponsive.
