# Loop-probe coverage and faithfulness

## Question

When can ordered loop probes support a claim of global coherence rather than one sampled holonomy value?

## Claim boundary

This packet gives necessary audit conditions for a finite nerve. They are not sufficient for higher-categorical descent unless all typed face and higher coherence laws are also supplied.

## Cycle coverage

Let the overlap graph of local representations have \(V\) vertices, \(E\) admitted comparison edges, and \(c\) connected components. Its independent graph-cycle rank is

\[
\beta_1=E-V+c.
\]

After fixing a spanning forest, at least one independent loop datum is required for each nonforest edge to determine graph-level holonomy. Kitaev's four-copy cycle supplies one loop datum. It can cover one cycle-basis element, not an arbitrary overlap graph with \(\beta_1>1\).

This count concerns the 1-skeleton only. Filled triangular and higher simplices impose relations among cycle generators. Those relations require associator and pentagon tests; counting graph cycles does not verify them.

## Observable faithfulness

A loop probe returns an observable \(q(H_\gamma)\) of the holonomy \(H_\gamma\). Global conclusions require the family of observables to be faithful on the intended quotient. One trace value is generally not faithful: distinct operators can have equal trace while differing in spectrum and action.

For rank-one Bargmann loops, the complex ordered trace retains a gauge-invariant scalar phase and magnitude, but it does not automatically reconstruct every underlying comparison cell. Its admissible claim is the measured scalar loop invariant, not uniqueness of the full gluing datum.

Thus a loop record needs:

- the typed loop and orientation;
- its place in a declared cycle basis or relation set;
- the predicted observable and normalization;
- a proof that the observable family is faithful on the claimed quotient, or an explicit unresolved multiplicity;
- independent-control or correlated-fault coverage;
- higher-face relations touching that loop.

## Shared-control correlation

Several loop measurements implemented with one control can share a fault mode. Nominal loop count then overstates independent coverage. Coverage should be indexed by fault-independence classes as well as cycle classes. Reversal, identity-cycle, quadrature, and randomized-control fixtures test different residuals but do not automatically make the main loop observations independent.

## Two independent failure modes

1. **Coverage failure:** every measured loop is exact, but an unmeasured cycle carries nontrivial holonomy.
2. **Faithfulness failure:** all declared scalar loop values match, but distinct holonomy operators lie in the same observable fiber.

Neither failure is repaired by increasing repetition of the same probe.

## Pyramid consequence

The partial-representation projection should not have a Boolean `loop_verified` field. It needs a typed object with:

- `cycle_basis_coverage`;
- `higher_relation_coverage`;
- `observable_coordinate`;
- `coordinate_faithfulness`;
- `unresolved_fiber`;
- `fault_independence_class`;
- `physical_constructor_status`.

Only after cycle coverage, faithful quotient coordinates, higher relations, and fault certificates are complete can loop evidence contribute to global gluing.

## Disposition

Kitaev's four-copy trace is an exact candidate coordinate on one associator loop. It is not yet a faithful or cover-complete coordinate system for the coherence pyramid. The next executable task is to inventory the pyramid nerve's independent cycles and assign each an observable family and fault class.

## Verification

- `research/voevodsky/checkers/check_loop_probe_coverage_and_faithfulness.py`
- `research/voevodsky/results/loop_probe_coverage_and_faithfulness.json`
