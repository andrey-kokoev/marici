# Joint selector correlation and the orbit-product gate

## Problem

Per-node selector audits do not compose automatically. Two reverse lifts may
each expose enough states to cover their own fibers while sharing one hidden
selector variable. Their joint image can then cover only a correlated
diagonal of the product fiber.

Let

\[
U_i:C_i\to E_i
\]

have invisible candidate orbits \(\mathcal O_i\). A joint constructor must
select a point in the admissible joint orbit

\[
\mathcal O_{\rm joint}\subseteq\mathcal O_1\times\cdots\times\mathcal O_k.
\]

The correct information lower bound is

\[
\boxed{
\left\lceil\log_2|\mathcal O_{\rm joint}|\right\rceil,
}
\]

computed after accounting for declared correlations and shared authority
roots.

## Smallest correlation witness

Take two binary fibers:

\[
\mathcal O_A=\{A_0,A_1\},
\qquad
\mathcal O_B=\{B_0,B_1\}.
\]

Audited separately, one shared bit \(s\) appears sufficient:

\[
A(s)=A_s,\qquad B(s)=B_s.
\]

Each marginal image contains both candidates. But the joint image is only

\[
\{(A_0,B_0),(A_1,B_1)\},
\]

not the four-point product orbit. The combinations

\[
(A_0,B_1),\qquad(A_1,B_0)
\]

are unreachable.

If the two choices are supposed to be independent, the compiler must reject
with

\[
\texttt{joint\_selector\_correlation\_deficit}.
\]

Two independent bits cover all four combinations. Alternatively, a
source-authorized coherence law may declare that only the diagonal is
admissible. In that case one shared bit is sufficient, but the reduction in
orbit size comes from the coherence constructor, not from counting the same
bit twice.

## Authority and fault implications

Shared selectors also create common-cause faults. Even when diagonal
correlation is semantically intended, a single selector authority root can
make two nominally separate decisions fail or equivocate together.

The joint audit therefore records:

- selector-state image in the joint fiber;
- independence or declared correlation law;
- selector authority roots;
- fault domains and common-cause sets;
- epoch and replay identity;
- resource consumption of the selector event.

Marginal distinguishability is necessary but not sufficient.

## Cross-sector consequences

- **Strominger.** Two capability lifts driven by one policy/default bit may
  each pass a local import test while lacking independent modality or epoch
  choices. Shared governance also invalidates fault-independence claims.
- **Kitaev.** A shared predicate pointer can correlate several gadget
  selections. Local gate realizability does not prove that all joint gadget
  combinations or fault paths exist; the pointer multiplicity must be typed.
- **Arithmetic/RH.** Separate scalar compressions may share one hidden probe
  or gauge choice. Marginally rich lifts need not span the product carrier;
  a claimed two-copy kernel must verify joint cyclicity rather than two
  one-copy surjectivity checks.
- **Benincasa.** Two period/insertion adapters may share a latent coordinate.
  Marginal rank can be full while the joint response image lies on a
  correlated diagonal.

## Finite compiler gate

Given selector state set \(S\) and joint map

\[
f:S\to\mathcal O_{\rm joint},
\]

compute the exact image \(f(S)\).

1. Verify each marginal image.
2. Verify the required joint orbit.
3. Reject if \(f(S)\) is a proper subset without an authorized correlation
   law.
4. If correlation is authorized, type its constructor and fault roots.
5. Never sum marginal bit lower bounds without checking shared inputs.

## Durable statement

> Selector sufficiency is a property of the joint orbit image, not of its
> marginals. Shared choice variables can make every local lift look complete
> while silently deleting cross-combinations and introducing common-cause
> authority.

