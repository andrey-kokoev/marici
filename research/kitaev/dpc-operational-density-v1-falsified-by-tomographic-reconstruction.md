# DPC operational-density v1 is falsified by tomographic reconstruction

**Owner:** marici.Kitaev  
**Status:** criticism and repaired conjecture  
**Target:** DPC target-independent operational density

## 1. The “if and only if seven gates” claim is false

The seven gates form a strong sufficient package for operational simulation and completed constructor reconstruction.

They are not all necessary for every explanatory completeness claim.

The clearest counterexample is finite-dimensional tomography.

A finite informationally complete measurement can reconstruct a density operator. Once the density operator is reconstructed, the outcome distribution of any other measurement is mathematically determined.

But an arbitrary measurement need not be physically simulable as classical postprocessing of that one informationally complete measurement. Reconstruction may use linear inversion with coefficients that are not probabilities.

Therefore:

- all context outcomes factor through the reconstructed semantic object;
- not every physical context factors operationally through the probe instrument.

The original DPC incorrectly required the second when the first can suffice for an inferential explanation.

## 2. Simulation and inference must be separated

### Operational factorization

A context \(C\) is physically simulated from probe basis \(\mathcal G\) using admitted constructors and classical processing.

This supports an implementation claim.

### Inferential factorization

Probe outcomes reconstruct a semantic representative \(s\), and the theory computes the predicted outcome of \(C\) from \(s\).

This supports a prediction or equivalence claim but does not implement \(C\).

Operational factorization implies inferential factorization when the simulation model is sound. The converse need not hold.

SCC must type which claim is being made.

## 3. Historical target-independence is not necessary

A probe may be discovered after inspecting a difficult candidate pair and still receive a noncircular source derivation.

Scientific discovery is often target-guided.

What matters is not temporal order but derivational independence:

- the probe follows from frozen source laws;
- its normalization and authority do not depend on the desired answer;
- the theorem is natural under hostile relabelling;
- it applies beyond the motivating pair;
- removing the candidate labels does not destroy its derivation.

Thus “chosen before the pair was known” is a useful anti-overfitting heuristic, not a necessary mathematical condition.

## 4. Scope makes uniformity conditional

Uniform resource bounds and completion stability are necessary only when the claim ranges over a scaling family or completion.

For one frozen finite packet, a nonuniform reconstruction can still be exact and explanatory within that scope.

Likewise, full compositional reconstruction is unnecessary for a claim restricted to object separation. It becomes mandatory only when constructor equivalence or network semantics is claimed.

The certificate must derive obligations from claim scope rather than impose every gate universally.

## 5. Repaired DPC

**DPC v2 — Scope-typed source-derived reconstruction.**

A finite probe family explains equivalence on a declared candidate class and claim scope when there exists a source-derived reconstruction map

\[
Q:
\text{retained probe profiles}
\longrightarrow
\text{declared semantic quotient}
\]

such that:

1. \(Q\) is faithful to the claimed equivalence on the candidate class;
2. every claim-relevant context prediction factors through \(Q\);
3. the derivation of \(Q\) is invariant under source symmetries and hostile relabelling, rather than fitted to candidate labels;
4. the physical probe and readout maps used to form the profile are authorized;
5. reconstruction preserves exactly the compositional structure included in the claim;
6. stability, resource uniformity, and completion are required precisely when included in scope.

For an implementation claim, add the stronger requirement that relevant contexts factor operationally through source-authorized constructors.

## 6. Noncircularity hostile

A finite candidate list always admits a lookup-table inverse.

Such a map is faithful on that list but explanatory only if it extends naturally to the source-generated candidate family and respects declared symmetries and composition.

The hostile test is to permute or extend the candidate labels while holding source structure fixed.

If the reconstruction rule must be rewritten by hand, it was fitted.

If the rule transports naturally, the motivating target did not supply hidden authority.

## 7. Tomography example

Let \(M\) be an informationally complete measurement and let

\[
p_M(\rho)
\]

be its outcome vector.

There is a linear reconstruction map \(Q\) with

\[
Q(p_M(\rho))=\rho.
\]

For any effect \(E\),

\[
p_E(\rho)=\operatorname{tr}(E Q(p_M(\rho))).
\]

Thus every measurement prediction factors inferentially through \(Q\).

But the coefficients used to reconstruct \(\rho\), or predict \(p_E\), need not define a stochastic postprocessing of \(M\). No physical simulation follows.

This is a positive explanation of observational completeness and a negative result for implementation authority.

## 8. Revised hostile suite

1. **Lookup-table fit:** reconstruction works only on enumerated labels.
2. **Relabelling failure:** source automorphism changes the rule by hand.
3. **Extension failure:** adding a source-admissible candidate destroys reconstruction.
4. **Inference/simulation confusion:** negative or nonphysical coefficients are treated as an instrument.
5. **Scope inflation:** finite exactness is promoted to uniform completion.
6. **Object/constructor inflation:** state separation is promoted to process reconstruction.
7. **Unauthorized probe:** mathematical measurement lacks source implementation.
8. **Readout quotient:** executable instrument exists but retained outcomes lose faithfulness.
9. **Stability failure:** inverse exists but is unbounded in the claimed topology.

## 9. SCC correction

```json
{
  "claim_scope": "finite_object | family | constructor | network | completion",
  "probe_profile": "...",
  "reconstruction_map": "...",
  "semantic_quotient": "...",
  "factorization_kind": "inferential | operational",
  "source_derivation": "...",
  "symmetry_naturality": "...",
  "hostile_relabelling": "...",
  "candidate_extension_test": "...",
  "physical_probe_authority": "...",
  "readout_faithfulness": "...",
  "scope_required_uniformity": "...",
  "scope_required_completion": "..."
}
```

## 10. Present conclusion

The original DPC confused a maximal operational compiler theorem with every possible explanation of finite completeness.

A finite probe family can explain all predictions through source-derived semantic reconstruction even when it cannot physically simulate every context.

The stronger operational-density gates remain necessary only for operational implementation claims.
