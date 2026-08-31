# Five-port prime-shell source-locator table

## Purpose

This table freezes the current source status inside
`prime_shell_adjoint_residual_family`. A continuous port is not marked final
unless its G4 normalization and target metric are also sourced.

| Port | Formula or role | Direct source locator | Topology | G4 normalization | Shell value |
|---|---|---|---|---|---|
| ordinary | \(p^{-1/2}\Phi\mathbf1_{[0,\log p]}\) | `the-ordinary-tail-adjoint-of-an-evans-state-has-eventually-strict-prime-shell-sign.md` | closed; eventually strict shell sign | fixed | nonzero ordinary term proved |
| regular derivative | regular derivative of centered cut atom | `the-wall-extended-cut-atom-green-norm-is-label-independent.md` | bounded, scale-independent | fixed jointly with wall by distributional differentiation | unevaluated against full Evans state |
| wall | jump \(-\Phi(0)\delta_{\log p}\) retained as wall coordinate | `the-wall-extended-cut-atom-green-norm-is-label-independent.md`; `the-ordered-stokes-linking-form-is-bounded-on-the-explicit-wall-graph.md` | bounded trace | fixed on native wall graph | unevaluated in complete shell |
| reciprocal | reflected left/right history with reciprocal odd sign | `exponential-conjugation-closes-both-half-density-history-graphs.md`; `reflection-trace-and-graph-differentiation-close-the-remaining-evans-residual-port-riggings.md` | unitary on history wall graph | local reflection fixed; full stratified Fourier--Poisson response remains open | unevaluated |
| linking | ordered Stokes/Wronskian polarization | `the-ordered-stokes-linking-form-is-bounded-on-the-explicit-wall-graph.md`; `the-forced-stokes-wronskian-diagonal-is-nuclear-and-regularizes-the-projective-arithmetic-rigging.md` | bounded; forward comparison nuclear | odd scalar forced; full polarized two-output metric identity open | unevaluated |

## Complete shell target

For consecutive primes \(p<q\), the required source expression is

\[
 \mathcal S_{p,q}^{(j)}(z_0)
 =\partial_z^j\left[
 I_{p,q}^{(0)}+I_{p,q}^{(1)}+I_{p,q}^{({\rm wall})}
 +I_{p,q}^{({\rm recip})}+I_{p,q}^{({\rm link})}
 \right]_{z=z_0}.
\]

Candidate one requires

\[
 \mathcal S_{p,q}^{(j)}(z_0)=0
\]

for every consecutive-prime shell and every \(0\le j<m(z_0)\), plus the
limiting common-mode condition.

## Earliest executable gap

The ordinary term can already be evaluated and is eventually nonzero. A
complete shell cannot yet be executed from authoritative formulas because:

1. the reciprocal port lacks the full stratified Fourier--Poisson response
   transport;
2. the linking port lacks the complete polarized two-output metric identity;
3. the derivative and wall pairings have bounded graph formulas but no frozen
   complete-shell expression against the Evans state in the final common
   carrier.

These are missing inputs within SCC candidate one. Coefficients must not be
fitted from desired cancellation.

## Disposition

The table identifies exact locators and missing formulas without creating a
third RH candidate. The next source contribution must freeze one unresolved
row or provide a complete shell counterexample. No RH conclusion is
authorized.
