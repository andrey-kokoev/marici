# DPC retirement: typed questions replace the conjecture

Owner: `marici.Kitaev`

## Disposition

DPC should be retired as a conjecture. Successive hostile tests removed every
candidate universal clause: source priority, microscopic uniqueness, named
resource necessity, exact code preservation, and finally the proposed
protection--engineering dichotomy. What remains is useful audit vocabulary,
but no single truth-valued explanatory law.

## Final falsifier

Protection and engineering are not disjoint alternatives. A magic-state
injection protocol reaches a non-Clifford logical channel only from the joint
packet

\[
  \text{protected Clifford substrate}
  + \text{engineered resource state and injection}.
\]

Neither part alone is sufficient. Moving the apparatus cut can redescribe the
same channel as a calibrated gate or as a state plus injection gadget, so the
partition is not canonical.

Protection also does not imply operational accuracy. A logical Pauli commutes
with all stabilizers and therefore has zero syndrome, yet logical \(Z\) sends
\(|+\rangle\) to the orthogonal state \(|-\rangle\). The corresponding unitary
channels have diamond distance 2. Local syndrome is blind to this coherent
logical fault.

## Typed audit matrix

| Question | Required certificate | What does not suffice |
|---|---|---|
| Is the target algebraically reachable? | compiler or controllability theorem | endpoint-algebra membership |
| Which resource class is necessary? | fixed free class plus monotone or no-go | deletion of one named device |
| What microscopic process realizes it? | independently validated Hamiltonian or channel | target spectral logarithm |
| Is it robust? | perturbation or topological stability bound | quantized abstract braid alone |
| Is it fault tolerant? | recovered-channel bound under a declared noise class | trivial syndrome |
| Does it scale? | size-indexed overhead and precision bounds | one finite lattice |
| What does it explain? | an explicit question and comparison class | an untyped predicate “proper explanation” |

These rows are independent theorem obligations. Passing one must not be
promoted into another.

## D(S3) boundary

The endpoint algebra, stabilizer obstruction, and conditional nonlinear
logical realization remain exact finite results. They do not prove executable
physical control, robustness, fault tolerance, or scalability. The physical
programme therefore splits cleanly:

1. classify operations protected by the \(D(S_3)\) phase under an explicitly
   chosen locality and deformation class;
2. construct and certify an engineered non-Clifford extension with a typed
   microscopic source, recovered-channel error, and scaling contract.

This split is a work decomposition, not a metaphysical dichotomy: a successful
architecture may be hybrid.

## Falsifiers and unresolved typing

The retirement would be reversed only by a new, non-vacuous DPC statement that
specifies its question, model class, equivalence, resource theory, accuracy,
noise, and scaling quantifiers and then survives the recorded countermodels.
No such statement is currently present.

Unresolved for \(D(S_3)\): the microscopic constructor set, locality metric on
a size-indexed family, admissible gauge/code deformations, noise class,
recovery map, and precision/overhead scaling.

## Artifacts

- Checker: `checkers/check_dpc_protection_engineering_dichotomy.py`
- Result: `results/dpc-protection-engineering-dichotomy.json`
- Consolidated replay: `checkers/check_s3_dpc_explanation_audit.py`
- Graph admission: `ev-000000003350-ad193dd7-e881-45fc-bddb-0162339fe4f3`
- Ledger: `src/ledger/20260825-2450 DPC Retired as Conjecture, Retained as Typed Audit.md`
