# Jointly faithful probes for coherence descent

## Question

When can agreement of all measured loop or face observables imply equality of the underlying coherence composites?

## Claim boundary

This packet states a conditional detection principle. It does not assert that the currently proposed physical probes are jointly faithful, source-authorized, or composition-preserving.

## Probe quotient

Let \(H\) be a typed space of candidate boundary composites and let

\[
Q=(q_\lambda)_{\lambda\in\Lambda}:H\to\prod_\lambda O_\lambda
\]

be the family of admitted observables. Two composites are probe-indistinguishable when all \(q_\lambda\) agree. This defines an observable quotient \(H/{\sim_Q}\).

Measured coherence establishes equality in this quotient. It establishes equality in \(H\) only if \(Q\) is monic on the intended quotient of gauge/equivalence classes.

This is the same faithful-coordinate gate used elsewhere in Marici, now applied to coherence cells rather than state fibers.

## Conditional detection principle

Suppose for every relevant hom-object:

1. every probe is typed and source-authorized;
2. the probe family is jointly faithful after the declared gauge quotient;
3. the probes preserve the compositions and identities used in the coherence equation;
4. every required nerve simplex and mixed certificate simplex is covered;
5. fault-independence certificates justify combining the probe results.

Then equality of all probed route composites implies equality of the underlying route composites, so a measured zero residual detects the corresponding coherence cell.

Each hypothesis has a separate role. Joint faithfulness without composition preservation cannot transport an equation through a composite. Composition preservation without faithfulness detects only a quotient. Coverage without fault independence can repeat one hidden common-mode residual.

## Hidden-kernel obstruction

A trace probe has a large kernel. For example, the identity and a nonidentity matrix can have the same trace after a traceless perturbation. A coherence defect lying in that kernel is invisible to every repetition of the trace probe.

Adding more scalar probes helps only if their common kernel on the declared quotient becomes zero. Full matrix-entry probes are jointly faithful in a fixed basis, but that basis may not descend through gauge. Gauge-invariant faithful coordinates require their own proof.

## Kitaev placement

The ordered Bargmann trace is valuable because it preserves cyclic order and complex phase. Its demonstrated strength is one exact scalar loop coordinate. To promote it to a coherence detector requires a theorem that the chosen family of Bargmann observables is jointly faithful on the relevant fusion-channel quotient and that the controlled-cycle implementation preserves the intended composite.

The shared-control obstruction attacks hypothesis 5. Missing physical controlled-permutation authority attacks hypothesis 1. A single loop attacks hypothesis 4. Trace nonfaithfulness attacks hypothesis 2. These failures are independent certificate predicates.

## Schema consequence

Probe records should include:

- `probe_family_id`;
- `typed_domain`;
- `declared_gauge_quotient`;
- `joint_kernel`;
- `joint_faithfulness_certificate`;
- `composition_preservation_certificate`;
- `simplex_coverage`;
- `fault_independence_certificate`;
- `demonstrated_detection_strength`.

## Disposition

The route from loop measurements to pyramid coherence is a conservative-detection problem. Current Kitaev data supply a nontrivial ordered scalar coordinate but not a jointly faithful conservative probe family. Global gluing remains unresolved modulo the observable kernel.

## Verification

- `research/voevodsky/checkers/check_jointly_faithful_coherence_probes.py`
- `research/voevodsky/results/jointly_faithful_coherence_probes.json`
