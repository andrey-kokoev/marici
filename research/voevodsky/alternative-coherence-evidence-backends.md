# Alternative coherence evidence backends

## Question

Must every global coherence claim have both explicit constructive fillers and a physically realized jointly faithful probe family?

## Claim boundary

This packet separates proof and operational evidence routes. It does not weaken the source, typing, coverage, or fault requirements internal to either route.

## Overconstraint risk

The overlay registry contains two ways to establish a coherence equation:

1. construct the compared arrows and a typed filler, then prove its coherence laws;
2. physically realize a probe family that is jointly faithful, composition-preserving, cover-complete, and fault-certified, then infer equality conservatively.

Requiring both for every theorem would incorrectly make physical implementation a prerequisite of mathematical coherence. Requiring neither would permit unsupported gluing. The two routes are alternative evidence backends.

## Direct constructive backend

A direct proof backend requires:

- source-typed objects and arrows;
- explicit comparison cell or horn filler;
- exact boundary match;
- required higher coherence equations;
- quotient/gauge descent;
- certificate-natural mixed cells when the certificate state varies.

This backend can establish a mathematical global section without a laboratory constructor. The Markov analytic fragment uses this route.

## Operational conservative backend

An operational backend requires:

- source-authorized physical constructor and readout;
- a probe family jointly faithful on the declared quotient;
- composition and identity preservation;
- complete pure and mixed simplex coverage through the claimed degree;
- independent fault certification;
- confidence or deterministic residual bounds.

This backend can detect the same mathematical equality only when a theorem connects the physical process and observable family to the target coherence objects.

## Logical form

For a coherence obligation \(h\), let \(P(h)\) be the complete direct-proof certificate and \(O(h)\) the complete operational conservative-detection certificate. Admission of the mathematical equality may use

\[
P(h)\lor O(h),
\]

provided each branch independently includes source typing and a theorem linking its data to \(h\). The disjunction is not satisfied by mixing incomplete pieces from both branches.

Physical realization is a separate claim. It always requires the operational constructor branch even if \(P(h)\) already proves the mathematical equality.

## Failure reporting

A blocked coherence record should report backend-specific minimal antichains:

- `proof_backend_failures`;
- `operational_backend_failures`.

The overall mathematical obligation is blocked only when every admitted backend is blocked. Its failure object is therefore a set of alternative antichains, not their union as though all prerequisites were conjunctive.

For Kitaev's loop, the algebraic ordered trace and negative-factorization theorem contribute to a proof/witness branch, while physical controlled-cycle and shared-control certificates remain blocked in the operational branch. This does not retract the algebraic theorem and does not authorize the physical claim.

## Composition

When composing coherences, backend choices must remain compatible. A proof-certified cell may compose with another proof-certified cell directly. Operationally detected cells compose only if the probe functor preserves the composition and their fault models admit the joint experiment. Hybrid composition needs an explicit comparison theorem; transport alone does not supply it.

## Disposition

The certificate DAG must contain alternative backend nodes rather than one universal conjunction. Mathematical global gluing can be proved constructively or detected operationally by a conservative family. Physical realization remains a separate operational claim. This prevents both overconstraint and authority smearing.

## Verification

- `research/voevodsky/checkers/check_alternative_coherence_backends.py`
- `research/voevodsky/results/alternative_coherence_backends.json`
