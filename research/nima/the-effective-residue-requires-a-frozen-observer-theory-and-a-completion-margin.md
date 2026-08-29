# The effective residue requires a frozen observer theory and a completion margin

## Claim-boundary correction

The phrase “every authorized downstream wiring” cannot quantify over unspecified future constructors. Gauge is relative to a versioned continuation theory fixed at the claim boundary.

For each \(s\), the instrument specification must declare
\[
\mathcal W^{\mathrm{adm}}_s(v)
\]
for a theory version \(v\). Define
\[
G_s(v)=\bigcap_{W\in\mathcal W^{\mathrm{adm}}_s(v)}
\ker(W|_{N_s}),
\qquad
E_s(v)=N_s/G_s(v).
\]

Every assertion of gauge uniqueness, horizontal realizability, or spectral completion must cite the exact observer-theory version. Transport admission and observer admission are therefore part of one frozen instrument packet.

## Monotonicity under theory extension

If
\[
\mathcal W^{\mathrm{adm}}_s(v)
\subseteq
\mathcal W^{\mathrm{adm}}_s(v'),
\]
then
\[
G_s(v')\subseteq G_s(v).
\]
Thus theory extension can only shrink harmless gauge and refine effective residue. There is a canonical map
\[
E_s(v')=N_s/G_s(v')
\longrightarrow
E_s(v)=N_s/G_s(v).
\]

The direction matters: the richer theory retains more distinctions and maps onto the coarser quotient. Equivalently, the coarser effective residue acquires a filtration whose new layer is
\[
G_s(v)/G_s(v').
\]
A prior proof remains valid under extension only if this newly observable layer has zero obstruction and zero effective torsor, with a preserved quantitative margin.

No claim may infer extension stability merely from validity at one version.

## Joint observer

For an infinite admitted family, choose a declared product or direct-sum target
\[
\mathcal Y_s(v)
\]
and define the joint observer
\[
\mathbf W_s(v):N_s\longrightarrow\mathcal Y_s(v),
\qquad
n\longmapsto(Wn)_{W\in\mathcal W^{\mathrm{adm}}_s(v)}.
\]
Then
\[
G_s(v)=\ker\mathbf W_s(v).
\]

The target topology is part of the constructor. An unrestricted algebraic product, Hilbert direct sum, weighted \(\ell^2\) sum, and projective locally convex product need not yield the same completion or uniform estimates.

## Hausdorff and completion gates

For \(E_s(v)\) to be a Hausdorff Hilbert or locally convex quotient, \(G_s(v)\) must be closed. If it is not closed, the algebraic quotient is non-Hausdorff and cannot serve as the coefficient object of an analytic Fredholm argument.

There are two admissible repairs:

1. prove \(G_s(v)\) closed in the declared topology;
2. replace it by the separated quotient
   \[
   E_s^{\mathrm{sep}}(v)=N_s/\overline{G_s(v)}
   \]
   and explicitly record which algebraic residues disappear under completion.

Separation alone is insufficient. The joint observer must retain a quantitative margin. On the effective complement, seek
\[
\|\mathbf W_s(v)n\|_{\mathcal Y_s(v)}
\ge
\delta_C\,
\operatorname{dist}(n,G_s(v))
\]
uniformly for \(s\) in each compact \(C\), and uniformly in the cutoff when a completed limit is claimed.

This is equivalent to bounded-below observation on \(E_s(v)\), hence to closed range of the induced joint observer in the Hilbert setting. It prevents nonzero effective residue from becoming asymptotically invisible.

## Finite inventories and the inverse-limit trap

Let \(\mathcal F\) range over finite subfamilies and set
\[
G_{s,\mathcal F}
=
\bigcap_{W\in\mathcal F}\ker(W|_{N_s}).
\]
Then
\[
G_s(v)=\bigcap_{\mathcal F}G_{s,\mathcal F}.
\]
Each finite quotient can appear gauge-unique relative to its own inventory while the directed family loses every uniform separation constant. Algebraic point separation in the limit does not imply stable observation after completion.

The required finite-to-complete theorem is therefore not merely
\[
\bigcap_{\mathcal F}G_{s,\mathcal F}=G_s(v),
\]
but a uniform frame-type estimate for a declared cofinal family of finite observers.

## Hostile model

Take \(N=\ell^2(\mathbb N)\) and finite inventories
\[
\mathbf W_m(n)=(n_1,\ldots,n_m).
\]
Then
\[
G_m=\{n:n_1=\cdots=n_m=0\},
\qquad
\bigcap_mG_m=\{0\}.
\]
The completed family separates points algebraically.

Now weight the observers by
\[
\mathbf V_m(n)=
(n_1,\tfrac12n_2,\ldots,\tfrac1m n_m).
\]
Every coordinate is eventually observed, yet the unit vectors \(e_m\) satisfy
\[
\|\mathbf V_m e_m\|=\frac1m\to0.
\]
There is no uniform joint separation margin. Completion produces asymptotically invisible effective residue despite trivial limiting gauge.

This is the observer analogue of finite-cutoff eigenvalues approaching the forbidden value \(1\).

## Revised categorical gate

A completion-valid horizontal lift requires:

1. a frozen, versioned \(\mathcal W^{\mathrm{adm}}(v)\);
2. transport preservation of \(N(v)\) and \(G(v)\);
3. closed harmless gauge, or an explicit separated quotient;
4. vanishing obstruction in the effective coefficient system;
5. trivial effective homogeneous torsor;
6. a uniform joint-observer separation margin;
7. an extension theorem for every later observer-theory refinement used by the RH claim.

Only after these conditions may \(E(v)\) be treated as the legitimate coefficient object for the naturality complex and the compact Birman–Schwinger completion.

## Next calculation

Construct the observer matrix at finite cutoff, including seam, endpoint, archimedean, reciprocal, and mixed clutching channels. Compute its least nonzero singular value on \(N/G\). The needed invariant is the lower envelope over cutoff and compact \(s\)-sets.

If that envelope vanishes, completion creates invisible residue even though every finite observer inventory is algebraically separating. If it stays positive, effective gauge uniqueness survives completion.
