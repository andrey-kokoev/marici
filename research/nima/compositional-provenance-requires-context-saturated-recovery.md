# Compositional provenance requires context-saturated recovery

## Question

When does observational process equivalence on a recovery domain remain valid
after the processes are inserted into admitted constructor contexts?

## Claim boundary

Let (D\subseteq S) be a probe domain and define

\[
U\sim_DV
\quad\Longleftrightarrow\quad
U|_D=V|_D.
\]

This equivalence is always preserved by postcomposition: if (U) and (V)
agree on (D), then (L\circ U) and (L\circ V) agree on (D).

It is not generally preserved by precomposition. For an admitted context (C),

\[
(U\circ C)|_D
\]

depends on the action of (U) on (C(D)), which may lie outside (D).

Therefore (sim_D) is stable under every admitted precomposition context only
if the retained provenance separates process action on the context saturation

\[
D_{\mathcal M}=
\bigcup_{C\in\mathcal M}C(D),
\]

where (mathcal M) is the admitted context monoid.

This is an extensional condition. Typed partial composition additionally
requires equivalent representatives to have the same definedness in every
context and equivalent outputs whenever both composites exist.

## Exact finite hostile

On three states, let (U) be identity and let (V) exchange states one and two
while fixing zero. They agree on (D=\{0\}).

Let (C) exchange zero and one. Then (C(0)=1), so

\[
U(C(0))=1,
\qquad
V(C(0))=2.
\]

The processes become distinguishable after precomposition. Endpoint agreement
on the original probe is not a compositional process quotient.

## Context saturation

For the full permutation context monoid on three states, the orbit of any
nonempty probe is the complete state set. Hence any observational equivalence
that must survive arbitrary permutation contexts collapses to equality of the
full process action.

For the restricted context monoid fixing zero, the singleton domain
(D=\{0\}) is invariant. Equality on that domain is then stable under admitted
precomposition.

Thus provenance requirements depend not only on the requested recovery domain,
but also on the constructor contexts into which the process may later be
substituted.

## Revised interface

The recovery interface must carry both

\[
(D,\mathcal M).
\]

The information-theoretic provenance quotient is computed on the saturated
domain (D_{\mathcal M}), not on (D) alone. A later enlargement of admitted
contexts may refine the required provenance even when the nominal recovery
domain is unchanged.

The complete quotient gate requires:

1. source authority for every context in (mathcal M);
2. context saturation of the probe domain;
3. equality of definedness for typed partial constructors;
4. output equivalence where composition is defined;
5. preservation under authorized process equations;
6. fault and completion stability.

## Cross-sector consequence

- A flavor analyzer calibrated for one production channel need not remain
  faithful after a different upstream preparation changes its input domain.
- A control realization equivalent for one experiment family may separate
  after feedback closes the loop.
- A charge instrument agreeing on one logical sector may separate after an
  admitted braid or fusion context.
- An optical transfer equivalence may fail inside a cavity or interferometric
  feedback route.
- A repair-history quotient may fail when one representative is admissible in
  a downstream constructor and another is not.

## Disposition

The finite compositional obstruction is closed. Recovery-scope provenance must
be indexed by an admitted context monoid and saturated under its action. The
earlier Galois connection remains valid observationally but is not by itself a
compiler-safe congruence.

Verification is provided by
`research/nima/checkers/check_context_saturated_provenance_congruence.py` and
`research/nima/results/context-saturated-provenance-congruence.json`.
