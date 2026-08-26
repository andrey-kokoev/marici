# Sequential Data Needs Separating Depth

## Bounded question

Does adding ordered observations to a commutative context atlas automatically
recover the orientation of upstream composition?

## Result

No. “Sequential” is not itself a sufficiency condition. The readout must be
jointly separating at a depth where the rival realizations diverge.

Use normalized matrix trace as the readout and compare ordinary composition
with opposite composition. At word depth two, reversal cannot be detected:
`Tr(ab) = Tr(ba)`. This is true even though the input labels are ordered. For
the Pauli basis, every one- and two-letter trace agrees with its reversed word.

At depth three the cyclic symmetry no longer identifies reversal. The exact
fixture gives `Tr(XYZ) = 2i` and `Tr(ZYX) = -2i`. Thus depth three is the first
separating depth for this readout and generator family.

## Control-theory interpretation

An input sequence is not automatically an informative experiment. An ordered
transition system can remain unobservable through a symmetric output map.
Orientation belongs to the minimal realization only when some authorized
continuation produces a different record. The relevant condition is therefore
not “has sequential probes,” but “has a continuation-closed probe family that
separates the candidate oriented realizations.”

This yields three distinct layers:

1. The transition syntax records that interventions are ordered.
2. The physical readout maps ordered histories to records.
3. Behavioral minimization retains only order distinctions separated by the
   authorized future probe closure.

Layer one without layer two is unobservable bookkeeping. Layer two without
closure may establish only a finite-cutoff distinction. Layer three supplies
the stabilized behavioral state.

## Marici consequence

Orientation should not be installed as an unconditional primitive of every
Marici object. Instead, source-authorized sequential contexts generate a
behavioral equivalence. Orientation survives precisely when word reversal
fails that equivalence. If all authorized records remain reversal-invariant,
ordinary and opposite realizations are the same Marici object at that task
resolution, even if a richer external algebra distinguishes them.

Conversely, when an authorized continuation separates reversal, quotienting
it away destroys a source-defined counterfactual capability. The oriented
transition law must then be retained.

## General finite reconstruction criterion

Let candidate products `m` and `n` act on the same source-typed carrier. A
probe family reconstructs their distinction on an admitted generator closure
only if equality of every authorized continuation value forces `m = n` on
that closure. If this implication fails, reconstruction is set-valued. A
source-authorized selector is still required to implement one compatible lift.

## Claim boundary

The checker proves a finite exact depth separation for two-by-two matrices. It
does not establish a universal depth-three theorem. Other readouts may separate
at depth two, require greater depth, or never separate reversal. Unbounded
reconstruction requires stabilized generator closure, not extrapolation from
this finite fixture.

## Verification

Run:

```text
python research/sontag/checkers/sequential_depth_orientation.py
```

The dependency-free checker verifies seven exact claims and writes
`research/sontag/results/sequential_depth_orientation.json`.
