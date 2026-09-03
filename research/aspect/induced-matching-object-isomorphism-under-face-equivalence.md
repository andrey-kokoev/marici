# Induced matching-object isomorphism under face equivalence

## Question

How does a face-category equivalence and natural isomorphism of constraint presheaves induce the matching-object isomorphism required for rewrite soundness?

## Claim boundary

This packet gives the typed categorical construction conditional on chosen matching limits in `Set` and an equivalence of proper-face indexing categories. It proves local matching-map conjugacy and fiber equivalence under those assumptions. It does not prove global rewrite confluence, SCC-wide soundness, physical equivalence, or that an arbitrary category equivalence preserves a separately chosen geometric notion of face.

## Proper-face index

Let \(\mathcal C\) and \(\mathcal D\) be thin skeletal face categories and let \(\sigma\in\mathcal C\). Define the punctured lower category

\[
\partial\sigma=\{\tau\in\mathcal C\mid \tau<\sigma\}.
\]

Let \(E:\mathcal C\simeq\mathcal D\) be an equivalence and choose \(\sigma'=E\sigma\). Because the categories are thin and skeletal, \(E\) preserves and reflects strict face inclusion. It therefore restricts to an equivalence

\[
e_\sigma:\partial\sigma\simeq\partial\sigma'.
\]

For non-skeletal or geometrically decorated categories, this restriction is additional data rather than a consequence of abstract equivalence.

## Boundary diagrams and matching objects

Let

\[
F:\mathcal C^{op}\to\mathbf{Set},
\qquad
G:\mathcal D^{op}\to\mathbf{Set},
\]

and let

\[
\eta:F\mathrel{\cong}G\circ E^{op}
\]

be a natural isomorphism. Restriction to proper faces gives a natural isomorphism between the boundary diagram of \(F\) and the reindexed boundary diagram of \(G\).

Choose limits

\[
M_F(\sigma)=\lim_{\tau<\sigma}F(\tau),
\qquad
M_G(\sigma')=\lim_{\upsilon<\sigma'}G(\upsilon).
\]

Write their projections as \(\pi^F_\tau\) and \(\pi^G_{E\tau}\). The transported cone has legs

\[
\eta_\tau\pi^F_\tau:M_F(\sigma)\to G(E\tau).
\]

The equivalence \(e_\sigma\) makes this a limiting cone for the target boundary diagram. By the universal property, there is a unique isomorphism

\[
\alpha_M:M_F(\sigma)\mathrel{\cong}M_G(\sigma')
\]

such that

\[
\pi^G_{E\tau}\alpha_M=\eta_\tau\pi^F_\tau
\]

for every proper face \(\tau<\sigma\). Its inverse is constructed from \(\eta^{-1}\) and a quasi-inverse of \(e_\sigma\); uniqueness of limit mediating maps proves the two composites are identities.

## Matching-map conjugacy

Let

\[
\mu_F:F(\sigma)\to M_F(\sigma),
\qquad
\mu_G:G(\sigma')\to M_G(\sigma')
\]

be the matching maps induced by restriction. For each proper face \(\tau\),

\[
\begin{aligned}
\pi^G_{E\tau}\alpha_M\mu_F
&=\eta_\tau\pi^F_\tau\mu_F\\
&=\eta_\tau r^F_{\sigma,\tau}\\
&=r^G_{\sigma',E\tau}\eta_\sigma\\
&=\pi^G_{E\tau}\mu_G\eta_\sigma.
\end{aligned}
\]

The target limit projections are jointly monic, hence

\[
\alpha_M\mu_F=\mu_G\eta_\sigma.
\]

No additive structure is used.

## Fiber equivalence

For \(m\in M_F(\sigma)\), map a joint section \(x\) in the fiber of \(\mu_F\) over \(m\) to \(\eta_\sigma(x)\). Conjugacy places it in the fiber of \(\mu_G\) over \(\alpha_M(m)\). The inverse components of \(\eta\) and \(\alpha_M\) give the inverse fiber map. Thus corresponding fibers are equivalent, preserving empty fibers and multiplicities.

## Exact residual

The categorical construction is complete under the declared hypotheses. The remaining formal residual is machine verification in the Buzzard-owned Lean lane, including the restriction of \(E\) to punctured lower categories and the theorem that reindexing a limit diagram along an equivalence preserves its limiting cone. The SCC candidate currently validates explicit finite certificates; it does not construct this limit comparison.

## Disposition

The missing matching-object map is constructed and its defining projection equation yields matching-map conjugacy. The earlier finite witnesses instantiate this theorem; they are no longer substitutes for its typed construction.
