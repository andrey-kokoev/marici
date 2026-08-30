# 1726 — Composed Singular Amplitude Maps Have No Excess Hermitian Costalk

## Two-rank-drop falsifier

Compose

\[
f_\varepsilon=\operatorname{diag}(1,\varepsilon),
\qquad
g_\eta=\operatorname{diag}(\eta,1).
\]

Their direct composite is

\[
g_\eta f_\varepsilon=\operatorname{diag}(\eta,\varepsilon).
\]

For \(|u\rangle=(a,b)^T\), direct Hermitian-square specialization gives

\[
\rho_{\eta,\varepsilon}
=
\begin{pmatrix}
\eta^2a^2&\eta\varepsilon ab\\
\eta\varepsilon ab&\varepsilon^2b^2
\end{pmatrix}.
\]

## Iterated comparison

The two singular-map costalks give the pure bidegrees \((2,0)\) and \((0,2)\).
Their labelled overlap gives the mixed bidegree \((1,1)\).  Together they
reconstruct the direct packet exactly:

\[
\boxed{
\operatorname{gr}_{g}\operatorname{gr}_{f}\mathsf H(u)
=
\operatorname{gr}_{(g,f)}\mathsf H(u).
}
\]

The mixed occurrence is required; omitting it would discard relative phase.
After retaining it, no excess Tor or extension class survives.

## Narrow result

The existing multi-Rees/Hermitian-square calculus composes across two
transverse amplitude rank drops.  No additional quantum coherence operation
or Cut carrier stratum is required in this finite model.

## Durable artifacts

- `research/benincasa/checkers/composed_singular_hermitian_costalk.rs`
- `research/benincasa/results/composed-singular-hermitian-costalk.json`
- `research/benincasa/composed-singular-hermitian-costalk.md`

## Next falsifier

Replace transverse diagonal rank drops by nontransverse maps with a shared
kernel.  Test whether derived intersection produces a genuine excess costalk
or remains the ordinary Hermitian square of the common kernel flag.
