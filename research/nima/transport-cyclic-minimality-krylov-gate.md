# Transport-cyclic minimality: the Krylov gate

## Correction to static minimality

A carrier direction orthogonal to the initial source image need not be
unauthorized. It is source-generated when admitted transport reaches it.
Therefore the correct minimality notion for a dynamical constructor
\((J,\mathcal T,H)\) is not

\[
\operatorname{span}J(V)=H,
\]

but transport cyclicity:

\[
H_{\rm cyc}
=\operatorname{span}\{T_wJv:
v\in V,\;w\text{ a word in the admitted generators }\mathcal T\}.
\]

The intrinsic carrier is \(H_{\rm cyc}\). Directions in
\(H\ominus H_{\rm cyc}\) remain genuinely dark.

## Finite-dimensional closure algorithm

Set

\[
S_0=\operatorname{im}J,\qquad
S_{n+1}=S_n+\sum_{T\in\mathcal T}T S_n.
\]

Then \(S_n\) stabilizes in at most \(\dim H-\dim S_0\) strict-growth steps.
At stabilization \(S_n=H_{\rm cyc}\). For the orthogonal projector \(P_n\)
onto \(S_n\), closure is equivalent to

\[
(I-P_n)TP_n=0\qquad\text{for every }T\in\mathcal T.
\]

This yields three typed outcomes:

1. \(S_1=S_0\): the initial essential image is transport closed;
2. \(S_0\subsetneq H_{\rm cyc}\subsetneq H\): a forced extension plus a
   remaining unauthorized ambient complement;
3. \(H_{\rm cyc}=H\): the whole ambient carrier is dynamically
   source-generated.

## Smallest full-growth witness

Let \(V=\mathbb R\), \(H=\mathbb R^3\), and \(J(1)=e_1\). Define

\[
T e_1=e_2,\qquad T e_2=e_3,\qquad T e_3=0.
\]

The static source image has rank one, but

\[
S_0=\langle e_1\rangle,\quad
S_1=\langle e_1,e_2\rangle,\quad
S_2=\mathbb R^3.
\]

Thus the two initially dark directions are authorized by two finite transport
steps. Replacing \(T\) by zero leaves the same scalar seed form
\(J^*J=[1]\) but gives \(H_{\rm cyc}=\langle e_1\rangle\). The scalar form
cannot distinguish these sources; the transport orbit can.

## What data determine the cyclic realization?

The single Gram form \(Q=J^*J\) is insufficient. The relevant
noncommutative moment kernel is

\[
K(u,v)=J^*T_u^*T_vJ
\]

for transport words \(u,v\). A cyclic realization of the full kernel is
unique up to a unitary intertwining both the source map and every admitted
transport generator. This is the dynamical analogue of minimal
Gram/Kolmogorov uniqueness.

The qualification is essential: manufacturing \(K\) from a desired positive
answer is circular. Its words, inner product, and relations require
independent source authority.

## Cross-sector consequences

- **Arithmetic/RH.** Prime transport already forces an infinite labelled
  cyclic closure. This theorem explains why static finite Gram blocks leak,
  while also confirming the no-go result: if the full word kernel merely
  reconstructs the Weil/Pick form, cyclic completion adds provenance but no
  independent orientation for \(C_Y\).
- **Kitaev.** The relevant resource carrier is the orbit of encoded states
  under the admitted gate-and-injection algebra. A controlled-\(S\)
  decomposition into three \(T/T^\dagger\) injections establishes
  reachability conditional on a verified \(T\)-factory; it does not generate
  that factory.
- **Strominger.** Authority is the closure of proof roots under operations
  admitted by the explicit fault model. A capability outside that orbit is
  not authorized merely because it exists in the ambient replica system.
- **Benincasa.** The source-defined integrated period jet under admissible
  external controls is an observability/Krylov construction. Its stabilized
  rank, not formal independence on a latent coordinate, measures the
  physically generated response carrier.

## Finite falsifier

For each proposed generator \(T\), compute

\[
F_T=(I-P)TP.
\]

- \(F_T\ne0\) falsifies closure of the current carrier.
- Iterating the exposed directions computes the smallest forced extension.
- After stabilization, any nonzero ambient complement falsifies the claim
  that the entire declared carrier is source-generated.

The first word length at which the rank grows is a finite leakage witness.
If no rank growth occurs and the closure is still proper, the ambient excess
must be removed or separately authorized.

## Durable formulation

> A source constructor is minimal relative to its admitted transport algebra
> exactly when its source image is cyclic. Static darkness is harmless when
> finite source transport reaches it; only the orthogonal complement of the
> stabilized transport orbit is genuinely unauthorized.

