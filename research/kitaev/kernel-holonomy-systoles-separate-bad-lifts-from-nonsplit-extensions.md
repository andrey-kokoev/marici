# Kernel-holonomy systoles separate bad lifts from nonsplit extensions

Owner: \`marici.Kitaev\`

## Question

Can “first failed relation” distinguish a defective lift frame from a
structural obstruction to every strict compiler?

## Claim boundary

This is a finite presentation theorem for a frozen extension, authorized lift
family, and word-cost filtration. It grants no physical port authority.

## Residual map

Choose a finite alphabet \(\Sigma\), a surjection

\[
\pi:F(\Sigma)\to G,
\]

and physical lifts of its letters. They induce

\[
\widetilde\pi:F(\Sigma)\to E,
\qquad
q\widetilde\pi=\pi.
\]

For the relator subgroup \(N=\ker\pi\), restriction gives

\[
h_{\widetilde\pi}:N\to K,
\qquad
h_{\widetilde\pi}(r)=\widetilde\pi(r).
\]

This kernel-holonomy map records every composition residual of the chosen
implementation.

## Implementation systole

For weighted word cost \(c\), define

\[
\operatorname{sys}(\widetilde\pi)
=
\inf\{c(r):r\in N,\ h_{\widetilde\pi}(r)\ne1\}.
\]

Its value is infinity when every target relation closes physically. It is the
cost of the cheapest closed target loop carrying nontrivial kernel holonomy.

A split extension can still have finite implementation systole if poor letter
lifts are chosen. Therefore one finite systole does not prove nonsplitting.
The extension splits exactly when some lift frame induced by a homomorphic
section has infinite systole.

## Authorized min–max diagnostic

Let \(\mathcal L_{\rm auth}\) be the physically authorized lift frames and set

\[
\operatorname{Sys}_{\rm auth}
=
\sup_{\widetilde\pi\in\mathcal L_{\rm auth}}
\operatorname{sys}(\widetilde\pi).
\]

The exact conclusions are:

- an authorized strict compiler exists exactly when some authorized frame has
  infinite implementation systole;
- finite \(\operatorname{Sys}_{\rm auth}\) gives a uniform upper bound on the
  cost at which every authorized frame fails;
- infinite \(\operatorname{Sys}_{\rm auth}\) implies a strict compiler only
  when the supremum is attained, for example for a finite authorized family;
- without attainment, failures may merely be deferred to arbitrarily large
  finite cost.

That last case is the same logical shape as finite-stage coherence with inverse
norms escaping during completion.

## Finite hostile budget

For a finite presentation with defining relators \(R\), if every lifted
defining relator is trivial, the letter map factors through \(G\). Therefore a
nonsplit extension forces at least one defining relator to fail for every lift
choice, and

\[
\operatorname{Sys}_{\rm all}
\le
\max_{r\in R}c(r).
\]

Finite presentation thus supplies a uniform relation-test budget for
nonsplitting.

## Central case

When \(K\) is central, changing lifts changes the cocycle representative by a
coboundary. The implementation systole measures the first nontrivial
presentation loop for one representative. The cohomology class decides whether
all residuals can be removed simultaneously.

## Three separate costs

A first-failure report needs:

1. relation cost to execute the closed target word;
2. detection cost to distinguish its kernel residual;
3. correction cost to change the lift frame or cancel the residual.

A short word with an undetectable residual is not a short experiment. An
abstract coboundary without an authorized correcting constructor is not a
repair.

## SCC implication

A finite hostile for source-constructor coherence should publish the target
presentation, authorized lifts, least failed relation, typed kernel residual,
detector, admitted corrections, and whether every authorized frame still
fails. Minimality is relative to that frozen packet.

## Deutschian explanation

The explanation is the kernel-holonomy law on all closed target loops plus the
proof that no authorized frame trivializes it. The systole identifies the
cheapest loop on which this law must become visible. Moving the witness changes
diagnostic economy; eliminating the law requires a genuine splitting or a new
correction interface.

## Falsifiers

- One finite implementation systole is called a nonsplitting proof.
- Infinite supremum is treated as an attained strict compiler without an
  attainment theorem.
- A cheap relation has no admitted residual detector.
- A coboundary is called executable without a correcting constructor.
- Presentation cost changes silently.
- Finite-cutoff systoles are promoted to uniform closure.

## Disposition

The useful packet is the extension class together with the authorized
implementation-systole profile. The first answers structural possibility. The
second measures how cheaply every admitted realization exposes its defect.

No checker, build, or Git operation was run for this research-only packet.
