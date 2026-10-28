# Native observations retain the full parent, frame and history

## Generic actual native construction

`agda/RamseyNativeRetainedObservation.agda` uses the existing native E rule and resolution calculus. The sole seed policy admits a full root with its explicit validity witness. Frame realization and observation are declared functions; no observation result is admitted as a seed.

For a fixed root a, the E index contains

    (history h, state s, s=realize(end h,a),
     observation o, o=observe(end h,s)).

Selecting the computed index gives an actual native resolved package that also retains the full root premise. Kernel proofs recover the root/value certificate, history and native input derivation literally.

Equal history endpoints give equal derived readouts under the declared functions. They do not erase history: equality of the complete selected values implies equality of the retained histories. No theorem identifies different routes merely because a frame recurs.

This is a constructor for derived observation data attached to retained evidence. It is not a new native primitive implementing numerical matrix arithmetic, nor an authority to acquire physical measurements.

## Generic no-compressed-update theorem

The kernel proves the general obstruction used by the preceding runtime audit. Given admitted roots a,b with

    view(h,a)=view(h,b),
    view(k,a)!=view(k,b),

there is no function update on observation values satisfying

    update(view(h,x))=view(k,x)

for every admitted root x. The proof uses congruence and the two correctness equations to contradict the unequal future observations.

This separates recomputation from a retained full parent from an update on its lossy displayed value. The native package supports the former without pretending the latter exists.

## Fresh runtime instances

The current source-sector transport and trace-channel receipts were reread and their direct pins checked. Seven prepared roots are instantiated: zero, five coefficient basis vectors, and the explicit lost-direction vector. Four histories per root are retained, including a full three-frame return, giving28 runtime packages.

Each instance includes root coefficients, the full36-coordinate root field, full framed field, route history, current support, computed observation and source-context pins. Co-rotating observations agree exactly. Histories `[0]` and `[0,1,2,0]` have the same frame/state/readout but distinct retained records. The fixed future observation still separates the previously invisible direction.

These source matrices are checked by exact runtime arithmetic, not interpreted in the Agda kernel. The formal concrete example is a small Boolean instance demonstrating actual admission and rejection of a false observation equation. The generic theorem is available for declared realization/observation functions; no source-matrix equivalence has been kernel-certified here.

## Verification

Passing freeze: `scc-freezes/ramsey-retained-observation-v1.32b7497672508117.json`.
Contract: `contracts/ramsey-retained-observation-attempt.v1.json`.
Checker: `checkers/check_ramsey_retained_observation.py`.
Receipt: `results/ramsey-retained-observation-v1.json`.

Both positive modules pass fresh safe Cubical checks with `--ignore-interfaces`. A false observation module is rejected. Compiler hash and source inventories remain stable during checking. The frozen SCC challenge passes.

## Relation to the active net

This is scoped progress under `face-chart-transition-descent`, not closure of that node. Native retained incidence and retained observation now have generic actual constructors. The finite field/lift comparisons and source-backed runtime observations remain at their separately declared policies.

The unresolved integration is to instantiate these structured native packages on the actual matrix/field carrier with explicit comparison proofs and source-bound geometric incidence restrictions, while retaining off-edge dependencies and central spin lifts. A local field-gluing interpretation cannot be inferred from a package that deliberately retains nonlocal observations.

No graph verdict, net revision or Git checkpoint was changed.
