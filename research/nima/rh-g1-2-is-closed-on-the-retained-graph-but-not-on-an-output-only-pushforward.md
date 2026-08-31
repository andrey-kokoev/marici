# RH G1.2 is closed on the retained graph but not on an output-only pushforward

## Question

Does G1.2 require the source-retained graph, or a later pushforward that forgets
the source coordinate?

The ledger title names endpoint lifts, radical descent, closability, and cutoff
naturality.  It does not explicitly require an output-only codiagonal.

## Strict primitive-square endpoint lift

For \(L=\log p\), the source Stieltjes lift is

\[
J_pe_1=W_L,
\qquad
J_pe_2=W_{2L}.
\]

It is source-derived and prime/cutoff natural.  After the natural almost-everywhere
quotient, neither endpoint is radical, and the two-port Pauli observer satisfies

\[
2m_\nu^2I\le \mathcal O_p^*\mathcal O_p\le2I
\]

uniformly in \(p\).

## Closed analytic endpoint histories

The half-density histories

\[
H_-=U_-^{-1}H_0U_-,
\qquad
H_+=U_+^{-1}H_0U_+
\]

are closed on their declared graph domains.  Their renormalized endpoint traces
are continuous, reflection exchanges the two channels, translated label copies
remain prime/grade diagonal, and finite cutoff projections commute with the
histories and traces.

Thus the analytic endpoint lift, closability, and cutoff-naturality clauses are
closed before arithmetic mate identification.

## Radical descent on the retained graph

For the source-retained wall-jump graph,

\[
G_{\Gamma,p}(y)
=G_{\theta,p}(y)+G_{\mathrm{win},p}(K_py),
\]

with

\[
G_{\theta,p}(y)\ge c_\theta\|y\|^2,
\qquad c_\theta>0
\]

uniformly.  Hence

\[
\operatorname{rad}G_{\Gamma,p}=\{0\}.
\]

The direct sum over labels has the same lower bound and therefore closed range.
For the full history space, the odd boundary form factors through the endpoint
trace.  Quotienting the even zero-trace radical \(N_0\) is compatible because

\[
TN_0=0,
\qquad
JN_0=0.
\]

The safe quotient order is

\[
\mathcal H_{\rm hist}
\longrightarrow
\mathcal H_{\rm hist}/N_0
\longrightarrow
E_\theta\oplus E_{\rm win}.
\]

## Global retained joint graph

Let \(E\) be the completed labelled source space and let \(A,C\) be the typed
analytic and arithmetic outputs.  The retained map

\[
\mathcal Jx=(x,Ax,Cx)
\]

is a topological embedding in the declared product graph topology because the
first projection is the identity.  Its range is closed, and its positive graph
form has zero radical after the compatible zero-trace quotient.

Finite prime/grade projections commute with each component, so the retained
completion is cutoff natural.

## Output-only pushforward

If one applies

\[
\pi_{\rm out}(x,Ax,Cx)=(Ax,Cx)
\]

and forgets \(x\), closed range no longer follows.  Compact arithmetic
incidences can have nonclosed Hilbert range even when the retained graph is
closed.  A scalar mate formula or fibrewise injectivity does not repair this
completed-range problem.

Therefore there are two distinct assertions:

1. **retained G1.2:** endpoint lifts, radical descent, closed graph, and cutoff
   naturality with the source coordinate retained;
2. **pushforward G1.2+:** the same claims after forgetting the source
   coordinate.

Only the first is established.

## Disposition

If the authoritative Adams constructor is the source-retained saturated graph,
then all clauses explicitly named by G1.2 are closure candidates.

If the constructor requires an output-only codiagonal or pushout, G1.2 remains
open at completed closed range and radical reflection for \(\pi_{\rm out}\).

The successor packet
`the-correct-half-density-output-codiagonal-also-has-dense-nonclosed-kothe-range.md`
resolves the analytic alternative. The correctly twisted low-grade coefficient
is positive but decays faster than every inverse prime power. Its diagonal
output map has dense nonclosed range in the declared Köthe topology, and the
nuclear connected tail does not repair the cutoff witness. Thus an output-only
pushforward cannot satisfy G1.2 closed range without changing the source
object.

The source-authorized joint-graph construction already selects the retained
saturated order, and it is now also the only candidate compatible with the
ledger's closure requirement in the declared topology. Accordingly G1.2 is a
closure candidate on the selected architecture, not merely one side of an
unresolved analytic choice.

No ledger status is changed here, and no RH conclusion is authorized.
