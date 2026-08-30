# Grothendieck theta completion typing audit

## Contract inspected

`research/strominger/contracts/grothendieck-theta-completion-test.v1.json`
declares:

- a weighted pre-Hilbert theta core;
- the Hilbert completion `H_Phi`;
- a symmetric source diffusion core;
- a nonnegative self-adjoint Friedrichs generator with operator domain
  `Dom(A_Phi)_Friedrichs`;
- an explicit extension square on the core;
- a one-dimensional completion-only constant ground kernel.

## Interface decision

`existsUnique_compatibleOperatorExtension` in `CompletionNeutrality.lean`
cannot faithfully instantiate this contract. That theorem extends a total
uniformly continuous map to a total uniformly continuous map. A Friedrichs
generator is generally unbounded and is defined on a proper dense domain.

`UnboundedOperatorExtension.lean` therefore introduces `DomainOperator`, whose
function is typed on a declared domain subtype. `CoreCompatibility` carries
both core membership and the commuting extension square.
`kernel_descends_on_core` reflects kernel membership only for embedded source
points with those witnesses.

The finite `properDomainOperator` hostile is defined only on `{0} ⊂ Fin 2`.
`properDomainOperator_not_everywhereDefined` prevents a domain-bearing
operator from being silently promoted to a total map.

## Remaining theta inputs

Lean still needs source-authorized definitions or imported analytic theorems
for:

- the weighted pre-Hilbert core and `H_Phi`;
- density of the core embedding;
- closability and closure of the Dirichlet form;
- construction and uniqueness of the Friedrichs generator;
- agreement with `-Phi⁻¹(Phi f′)′` on the core;
- convergence of cutoff constants to the completion-only ground state;
- compact resolvent of the conjugated Schrödinger operator.

The JSON contract records evidence for these fields but is not itself a Lean
proof of the analytic statements.

## Verification

Per Nima's instruction, no Lean build was run. The module remains outside the
root import and elaboration is unverified.
