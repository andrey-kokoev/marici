# Finite observer shadows require uniformly conditioned source realization

## The comparison problem

Fix a versioned observer theory and a declared cofinal family \(\mathfrak F\) of finite admitted inventories. For \(F\in\mathfrak F\), set
\[
G_F=\bigcap_{W\in F}\ker(W|_N),
\qquad
E_F=N/G_F.
\]
If \(F\subseteq F'\), then \(G_{F'}\subseteq G_F\), giving a canonical surjection
\[
\rho_{F'F}:E_{F'}\twoheadrightarrow E_F.
\]
Thus \((E_F,\rho_{F'F})\) is a cofiltered quotient system.

Let
\[
G_\infty=\bigcap_{F\in\mathfrak F}G_F,
\qquad
E_\infty=N/G_\infty.
\]
The finite shadows define
\[
\Phi:E_\infty\longrightarrow\varprojlim_F E_F,
\qquad
[n]\longmapsto([n]_F)_F.
\]

The completion gate asks separately whether \(\Phi\) is:

1. an algebraic isomorphism;
2. a homeomorphism for the declared topologies;
3. an isometry for the frozen observer aggregation norm.

## Algebraic realization

The map \(\Phi\) is always injective by the definition of \(G_\infty\). Surjectivity is not automatic. It is the source-realization assertion:

> Every compatible family of finite observer shadows is represented by one source residue \(n\in N\), modulo \(G_\infty\).

Failure of surjectivity is **inverse-limit surplus**: the projective limit contains formal compatible shadows not realized by any source state.

A sufficient algebraic condition is stabilization of \(G_F\) along a cofinal finite inventory. In nonstabilizing systems, surjectivity requires an explicit completeness/compactness theorem for the affine fibers
\[
\{n\in N:[n]_F=e_F\}.
\]
Finite consistency alone does not establish a common point.

## Topological realization

Equip every \(E_F\), \(E_\infty\), and the inverse limit with declared quotient and projective-limit topologies. Even if \(\Phi\) is algebraically bijective, its inverse may be unbounded. This is **topology loss**.

Topology loss is the observer analogue of spectral mass escaping through cutoff: each finite shadow is exactly realizable, but reconstruction becomes arbitrarily ill-conditioned.

A topological isomorphism requires continuity of the reconstruction map. In Banach or Hilbert form this follows from a uniform inf-sup estimate for a frozen aggregation of one cofinal observer family.

## Frozen joint frame

Choose aggregation weights \(a_W>0\) and a target topology once at the claim boundary. Define
\[
\mathbf W_{\mathrm{all}}n=(a_WWn)_W
\]
into the declared Hilbert direct sum or locally convex product. In the Hilbert case, on \(G_\infty^\perp\), define
\[
A=\mathbf W_{\mathrm{all}}^*\mathbf W_{\mathrm{all}}.
\]

The following are equivalent in the Hilbert setting:

1. there is \(\delta>0\) such that
   \[
   \|\mathbf W_{\mathrm{all}}n\|
   \ge\delta\|n\|,
   \qquad n\in G_\infty^\perp;
   \]
2. \(\inf\sigma(A)\ge\delta^2>0\);
3. the range of \(\mathbf W_{\mathrm{all}}|_{G_\infty^\perp}\) is closed and reconstruction on its range is bounded;
4. \(\Phi^{-1}\) is uniformly conditioned when the inverse-limit topology is induced by this aggregation.

Uniformity must hold over cutoff and compact \(s\)-sets. Zero in the continuous spectrum of \(A\), even with \(\ker A=0\), is asymptotic invisibility without an actual invisible vector.

An isometry is stronger: the effective source norm must equal the frozen shadow norm,
\[
\operatorname{dist}(n,G_\infty)^2
=
\sum_Wa_W^2\|Wn\|^2.
\]
Equivalently \(A=I\) on \(G_\infty^\perp\). A general positive lower and upper frame bound gives a topological isomorphism but not an isometry.

## Corrected coordinate hostile

Let \(N=\ell^2(\mathbb N)\), and let
\[
R_m=\operatorname{span}(e_1,\ldots,e_m)
\]
be the finite reachable subspace. Define
\[
W_m n=(n_1,\ldots,n_m).
\]
Then
\[
G_m=R_m^\perp,
\qquad
E_m\cong R_m.
\]
The restriction \(W_m|_{R_m}\) is an exact isometry. This is cutoffwise exact observation of the declared finite reachable sector, not finite gauge uniqueness on all of \(N\).

Now use weighted coordinates
\[
V_m n=(n_1,\tfrac12n_2,\ldots,\tfrac1m n_m).
\]
Each \(V_m|_{R_m}\) is bijective and hence exactly reconstructs its finite reachable sector, but its inverse norm is \(m\). In the completed joint frame,
\[
Ae_k=\frac1{k^2}e_k.
\]
Thus \(\ker A=0\) while \(\inf\sigma(A)=0\). Algebraic point separation survives, but topology and uniform reconstruction fail.

## Interaction-net determinant check

The reported Schur reduction supplies a finite control for this distinction. Joining a new block \(E\) to retained block \(A\) through \(B,C\) produces
\[
S=E-CA^{-1}B.
\]
Its first variation contains both incidence residue and retained transport:
\[
S'=E'-C'A^{-1}B
+CA^{-1}A'A^{-1}B
-CA^{-1}B'.
\]
For the reported \(N=1\) prime-chain case, internal and exit jet terms vanish while entry incidence and retained transport remain. Hence the diagonal shadow can vanish although
\[
\operatorname{tr}(S^{-1}S')
\]
is nonzero. This is a finite-dimensional witness that exact terminal shadows do not reconstruct the full first-order source transport.

The Schur complement therefore acts as a local realization test: compatible block shadows require the retained inverse and its derivative, not merely diagonal observation.

## Finite-inventory comparison theorem target

A completion-valid theorem must prove:

1. \(\Phi\) is surjective: no inverse-limit surplus;
2. the frozen joint frame has uniform lower and upper bounds;
3. those bounds are uniform in cutoff and on compact \(s\)-sets;
4. the finite reachable spaces are stated explicitly;
5. the aggregation weights and target topology do not drift;
6. theory extension rechecks newly observable quotient layers.

Only then does every compatible family of finite observer shadows arise from one completed source residue with uniformly bounded condition number.

## RH interface

The frame operator \(A\) and the Birman–Schwinger family exhibit the same escape pattern. In each case the finite systems can be exact while the forbidden boundary is approached only in the limit. The categorical RH tower therefore needs two completion margins:

- an observer-reconstruction margin \(\inf\sigma(A)>0\);
- a spectral collision margin separating the generalized eigenvalue from \(1\).

The first ensures the completed operator packet is actually realized by source data. The second excludes the RH-forbidden collision inside that realized packet.
