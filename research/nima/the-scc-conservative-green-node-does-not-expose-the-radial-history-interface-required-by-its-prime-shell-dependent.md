# The SCC conservative-Green node does not expose the radial-history interface required by its prime-shell dependent

## Question

Does the current SCC declaration of `conservative_green_complex` expose enough
interface data to compare it with the newly constructed radial bordered block?

## Claim boundary

No. The node records only dependencies and a common interface label. Repository
search finds no carrier, differential, boundary traces, Wronskian incidence, or
polarized metric attached to its witness. Therefore the constructed radial
block cannot yet be identified with that node, and the node cannot supply the
prime-shell response formula merely by dependency composition.

## Mutable contract readback

The v2 contract digest remains

`44d3fa22c7ad883b04bff130828e7bc852ac93c8edb27ad7caad3ae6fd593ddd`.

The node declares:

- status: `constructed`;
- witness: `corrected_g4_audit`;
- interface: `g4_common`;
- dependencies: `centered_trace_class_seam_return` and
  `three_port_source_separation`.

The prime-shell residual family depends on this node and five-port summability,
but remains explicitly open.

## Missing interface fields

The radial bordered comparison requires at least:

1. history carrier containing the translation-cyclic radial module;
2. first-order differential and its domain;
3. zero-separation trace;
4. two moving shell-endpoint traces;
5. function-valued Wronskian incidence;
6. forward shell synthesis;
7. Hermitian adjoint and analytic-transpose returns as distinct arrows;
8. polarized Green metric;
9. arithmetic loading and codiagonal;
10. Laplace readout compatible with every jet.

None is exposed by the node or compiler dependency table.

## Dependency insufficiency

The current topology admits many inequivalent conservative complexes with the
same two incoming dependencies. For example, one may vary:

- the radial differential domain;
- the boundary trace frame;
- the Wronskian coefficient;
- the adjoint/transpose comparison;
- the endpoint border;
- the arithmetic codiagonal.

All variants satisfy the displayed graph dependencies while producing
different shell sections. Therefore dependency agreement does not determine
the required response.

## Exact interface target

An owner-reviewed witness must compare the canonical G4 object with the finite
radial block

\[
 \mathbb T_X(z)
 =\begin{pmatrix}
 D_t-z & U_X^{\rm rad}\\
 N_X^{\rm rad} & B_X(z)
 \end{pmatrix}
\]

including its retained border, and prove that its diagonal shell readout is

\[
 R(z)+2E(z)
 =\frac{\rho(0)+E(z)-\frac12W(z)}{z}+2E(z).
\]

The comparison must be polarized before scalar Schur elimination.

## Cheapest hostile

Keep the SCC dependencies fixed and change the Wronskian coefficient from
\(-1/2\) to zero. The current node schema cannot distinguish the mutation, but
the radial shell identity rejects it. This proves the interface is
under-specified for candidate one.

A second hostile keeps the Hermitian adjoint fixed and changes the analytic
transpose sign. Norm and dependency checks pass while multiplicity jets change.

## Authority boundary

The SCC contract and compiler are Aspect-owned. This audit records a Nima-side
interface requirement only. It does not authorize mutation of the node,
checker, witness status, or graph records.

## Disposition

The radial bordered block now supplies a concrete conformance target for
`conservative_green_complex`. The authoritative SCC remains insufficient to
perform that conformance check because its witness interface is not
materialized. Candidate one is blocked on owner-reviewed interface exposure,
not on further density algebra. No RH conclusion is authorized.
