# Dependency-aware partial-repair compiler

The compiler replaces the free finite-repair permutohedron by the legal path
space of a typed dependency poset. A repair constructor carries its local
defect transition, domain and graph-norm requirements, complete boundary and
support deltas, authority root, prerequisites, residual certificate type, and
capability consumption/production signatures.

For a finite repair poset `(R,<)`, the compiler enumerates precisely its linear
extensions. A listed order may still fail dynamically: every leg is checked
against the actual intermediate defect signature, graph domain, graph norm,
and residual capabilities. An unresolved prefix is retained only as an
`unsafe_repair_in_progress` state with its unresolved defects, next admissible
repairs, and residual capability packet.

## First three exact models

Three independent repairs produce all `3! = 6` paths. Authorized adjacent
swaps connect them into one component and all paths yield one typed endpoint.
This recovers the ordinary permutohedron exactly when the dependency poset is
discrete and all swap gates pass.

Adding `A < B` leaves the three linear extensions

```text
A B C
A C B
C A B
```

Adjacent swaps of incomparable repairs connect these paths. The missing
orders are absent because they are illegal, not because a coherence cell was
forgotten.

The third model has two legal orders and identical scalar endpoint bytes, but
the two composites produce inequivalent graph norms. Its swap gate reports
`repair_swap_domain_failure`; the legal path graph has two components and two
typed endpoints. Scalar equality therefore supplies neither a swap cell nor
endpoint coherence.

The higher comparison boundary is crossed only through a typed
comparison-current channel.

## Braid and anomaly gate

Every nonzero pairwise swap comparison value must carry its own source
authority root and `source_comparison_current` derivation. For a legal triple,
the compiler follows both braid words and subtracts their accumulated
comparison currents. It classifies the first residual as:

- `zero`: strict braid coherence;
- `exact_boundary`: a higher cell only when a source root and comparison cell
  are supplied;
- `central_phase`: a retained determinant/Pfaffian anomaly candidate;
- `domain_mismatch`: one comparison path is not defined;
- `untyped_residual`: rejection, with no fitted killing cell.

The failed-braid model has six legal paths and every pairwise swap cell, but its
two braid composites differ by one unit of comparison current. With no typed
higher witness it is classified `untyped_residual`. A second model has the same
scalar endpoint bytes and the same numerical residual, but a source-rooted
central-phase type; the compiler retains it as an anomaly candidate rather than
calling the paths coherent.

## Residual capability deletion

In the sixth model, both orders are linear extensions of the discrete
dependency poset. `Read;Delete` is dynamically legal. `Delete;Read` is not:
the first constructor consumes `residual_k`, so the second leg fails with
`repair_residual_capability_failure`. This is a domain-of-definition failure,
not a precedence relation inferred after the fact. The missing swap cell is
reported explicitly.

## Theta/Tate declaration barrier

The theta/Tate stages `{S,P,Q,A,L,C,D}` are present as a parameterized packet,
but the compiler assigns them no dependencies. Every stage currently lacks the
source-owned fields

```text
precedes
commutes_with
domain_after
boundary_delta
completion_scope
```

Accordingly the packet status is `source_declarations_required`; path
enumeration, component construction, braid comparison, and endpoint claims are
not performed. In particular, the compiler preserves the questions

```text
P <-> Q?
S <-> P?
L < C?
(P,Q,S,A) < D?
```

as questions. A hostile request to assume the discrete poset or enumerate the
incomplete packet is rejected.

A final refresh of Grothendieck's live notes found a source-native candidate
scale-flow graph norm and an explicit warning that the bulk tail--seam Gram
does not preserve the endpoint trace. This strengthens the need for the
`graph_norm_signature` and boundary-packet swap gates, but it still does not
declare the per-stage precedence, commutation, domain transition, boundary
delta, or completion scope. The seven-stage packet therefore remains correctly
blocked rather than being partially inferred from those analytic results.

## The compiler theorem

Legal staged repairs are dynamically admitted linear extensions of a typed
dependency poset. Adjacent swaps are available only for incomparable repairs
with source-declared commutation and equal complete local packets: boundary,
domain, graph norm, support/fault union, remaining defects, and reconstruction
capabilities. These swaps generate coherence only subject to the typed braid
and anomaly gate. Equal scalar bytes never suffice.

The compiler records two graphs separately. The abstract graph of all linear
extensions is connected under adjacent swaps of incomparable elements, as the
standard poset theorem requires. The dynamically legal, authority-bearing swap
graph is a subgraph: it can split when a domain is absent, a graph norm changes,
a residual capability is destroyed, or source commutation authority is
missing. Only connectivity of the latter establishes coherent construction.

## First theta/Tate repair triangle: `S`, `C`, `L`

The first source instantiation uses seam retention `S`, finite Clark bulk `C`,
and valuation pro-Gram construction `L`. Each carries the ten requested state,
domain, norm, boundary, completion, residual, and authority fields.

The exact cut decomposition authorizes `S` and proves that the seam cannot be
reconstructed from the retained tail:

\[
\|g_p\|\to0,
\qquad
\|h_p\|\to\|\Phi\|_2>0.
\]

The valuation constructor algebra authorizes the finite operational topology
behind `L`, while adjacent analytic atoms collapse and fixed-prime projectors
remain separated. Thus `L` requires both `seam_translation_norm` and
`raw_arithmetic_label`; completing before either is retained is irrecoverable.

The Clark identity authorizes `C` on finite packets:

\[
\|H_a+f\|^2+\|H_{-a}+f\|^2
=2\|G+f\|^2+2a^2\|\partial_zG\|^2.
\]

It does not authorize continuity through completion. Grothendieck's source
correction says the `z` derivative is not the scale-flow endpoint graph norm.
The endpoint is nevertheless controlled—separately—by the native first-order
operator (A_s=-\partial_q+(1-s)):

\[
|G(0)|^2\le {\|G+f\|_2^2\over 1-\Re s}.
\]

This closes ordinary one-sided tail completion escape, but it does not turn
the Clark `z` current into a completion-continuous valuation incidence map.
No fixed finite authorized family `F` uniformly dominating those current
matrices has been supplied, and the valuation/Fock-to-boundary incidence and
completion extension needed by `L` remain absent.

All six formal orders therefore have a typed first failure:

| Order | First rejection |
|---|---|
| `C L S` | `L` lacks the retained seam distinction |
| `C S L` | the common Clark/valuation incidence required by `L` is absent |
| `L C S` | `L` lacks the retained seam distinction |
| `L S C` | `L` lacks the retained seam distinction |
| `S C L` | the common Clark/valuation incidence required by `L` is absent |
| `S L C` | the completion extension required by `L` is not source-authorized |

There are currently zero completed typed paths, zero authorized adjacent swap
cells, and no braid comparison domain. The braid class is
`illegal_factorization`, not a fitted zero or central anomaly.

The compiler emits the principal hostile witness directly:

```json
{
  "code": "distinction_erased_before_required_repair",
  "path": ["complete_tail_quotient", "retain_seam"],
  "lost_capability": "seam_translation_norm",
  "recovery_possible": false
}
```

The resulting precedence law is logical rather than chronological:

\[
\boxed{
\text{completion may precede a repair only when it preserves every
distinction required by that repair's source contract}.}
\]

Supplying `F` would remove the Clark/completion obstruction but would not by
itself authorize the `S`--`C` swap. A source comparison cell for their complete
domain, graph norm, boundary packet, and residual capability would still be
required before the triangle could be called coherent.
