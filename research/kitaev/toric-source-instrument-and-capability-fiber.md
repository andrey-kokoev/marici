# Toric source instrument and its capability fiber

Status: exact finite theorem on the two-logical-qubit code representation and
periodic lattices `2 <= L <= 6`.

## Source-derived dilation

The controlled-string protocol supplies the complete instrument datum:

- system: the four-dimensional toric ground space;
- apparatus: one pointer qubit prepared in `|0>`;
- interaction: coherently XOR the logical `Z1` eigenlabel into the pointer,
  realized microscopically by the marked controlled string;
- pointer: exclusive computational outcomes `b=0,1`;
- conditioning: pointer projection followed by apparatus trace.

The induced Kraus maps are derived, not selected:

\[
K_0=\Pi_+,
\qquad K_1=\Pi_-,
\qquad \Pi_\pm=(I\pm Z_1)/2.
\]

Thus the coherent Wilson constructor is a source-derived QND Lüders
instrument in this frozen control model.  This is stronger than merely
declaring a formal completion of an effect algebra.

## Capability fiber over the same effects

Let `X1` be the conjugate logical operator.  The alternative maps

\[
\widetilde K_b=X_1\Pi_b

\]

have the identical effects `K_b^dagger K_b=Pi_b` and hence the same one-use
record law.  Their successors differ: on a `Z1=+1` state, the QND instrument
repeats the `+` result with probability one, while the flip instrument repeats
it with probability zero.  Sequential records therefore recover a capability
coordinate forgotten by the effect projection.

The controlled-string source selects the QND point; it does not select every
mathematically compatible point in the fiber.

## Protected-ground-space witness

The prior ambient trace-distance example was not yet code-space evidence.
Here the distinction is tested directly on any toric ground state with the
chosen Wilson eigenvalue.  The global Wilson projector commutes with every
star and preserves all `A_v=+1` expectations.  Measuring every constituent
`Z_e` and then forgetting all but parity kills the expectation of each star
touching the loop—exactly `L` stars on the checked lattice—and therefore
leaves the ground stabilizer face.

So the direct and refined instruments differ even on the protected input
domain.  Equal Wilson effects do not imply equal code-space backaction.

## Cross-sector placement

| sector | strongest instrument status |
|---|---|
| toric controlled string | source-derived QND instrument |
| double-slit controlled pointer | bounded source-derived QND instrument |
| one-mode UDW | bounded source-derived absorptive instrument |
| scattering/flavor Lüders maps | formal completions only |
| radiative memory | paired effect without apparatus dilation |
| cosmology | scalar period without outcome algebra |

This is a type census, not a cross-sector morphism.  The readout algebras are
heterogeneous and no source constructor currently transports one instrument
surface into another.

## Falsifiers and limits

The result fails if pointer dilation does not yield `Pi_+/-`, if QND and flip
effects differ, if their sequential signatures agree, or if fine constituent
measurement preserves every star expectation.  The exact source claim is
conditional on the admitted controlled-string gates and marked support.

Fault propagation, verified cat preparation, generic perturbative dressing,
and a constructor between sectors remain open.

