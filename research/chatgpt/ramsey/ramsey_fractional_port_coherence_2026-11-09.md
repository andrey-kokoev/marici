# Fractional compatibility obstruction for the six-port Ramsey reduction

Date: 2026-11-09. Status: rigorous sufficient criterion; verified finite samples, **not** a universal theorem for all 16-vertex residual graphs.

## 1. Problem

Assume a hypothetical 23-vertex triangle-free graph with independence number at most six. Earlier degree arguments reduce to the 6-regular case. At a vertex `v`, let `S=N(v)` be its six independent ports and let `H=G−({v}∪S)` be the 16-vertex residual. Then `e(H)=33` and `α(H)≤5`; each port `s∈S` has `T_s=N_H(s)` an independent five-set. The row cover equations are `Σ_s 1_{T_s}(w)=6−d_H(w)` for each residual vertex `w`.

The exact Hall condition is `|N_S(I)|≥|I|` for every independent residual set `I⊆H`. In particular, for an independent five-set `I` at most **one** of the six `T_s` may be disjoint from `I`.

## 2. Disjointness hypergraph and fractional certificate

Write `F=I_5(H)` for the collection of independent five-sets, and `D(T)={I∈F:I∩T=∅}`. For each `T∈F`, choose a nonnegative rational weight `y_I` on every `I∈F` such that

    Σ_{I∈D(T)} y_I ≥ 1.

If additionally

    Σ_{I∈F} y_I < 6,

then **no six** port neighborhoods from `F` can satisfy even the fifth-order Hall constraints. Indeed, the six required inequalities demand six units of total incidence-weight, while a fixed `I` can contribute to at most one port because fifth-order Hall permits `I` to be disjoint from at most one selected `T_s`. The resulting upper bound is `Σ_I y_I < 6`, contradiction.

This proof permits repeated `T_s`; no assumption about pairwise distinctness is hidden. It does not use the degree-cover equations, so it is stronger than ruling out degree-balanced six-tuples *when a certificate exists*. Conversely, the nonexistence of a sub-six fractional certificate alone does not imply an admissible six-tuple.

This is the dual of the fractional packing problem:

    maximize   Σ_T x_T
    subject to Σ_{T: I∩T=∅} x_T ≤ 1   for each I∈F,
               x_T ≥ 0.

A dual objective < 6 gives the exact obstruction. The interpretation is fractional total domination in the disjointness graph of independent five-sets.

## 3. Verified cases

The original example `ramsey_port_hall_witness.py` has 76 independent five-sets, a rank-five compatibility graph with clique number four, and fractional packing LP optimum approximately `4.7424242424`. Exact integer weights with denominator 100 give total `495/100=4.95`; the least disjointness coverage of any independent five-set is `103/100`, so the certificate is a strict, exact witness independent of the numerical LP.

A harder 16-vertex graph obtained by deleting a vertex and additional edges from one of the seven `(3,6;17)` graphs has 84 independent five-sets. Its numerical fractional optimum is `5.7692307692`; exact weights with denominator 1000 give total `5775/1000=5.775`, with least disjointness coverage `1001/1000`.

A separate nonexhaustive experiment generated **4,014 candidate 16-vertex graphs** through vertex deletion and constrained edge deletion from the seven known 17-vertex `(3,6)` graphs. They reduced to **27 distinct Weisfeiler–Lehman hashes**; one representative of every hash was given an independent integer-verifiable rational certificate with weight < 6. This is not an enumeration of all 2,576 nonisomorphic 16-vertex `(3,6)` graphs. Nor does a WL hash certify graph isomorphism. The maximum numerical LP optimum in this sample was approximately `5.7692307692`, and the maximum exact rational certificate mass was `5.775`.

A separate 1,200-trial edge-deletion experiment starting from the 16-vertex Clebsch graph yielded 1,117 accepted 33-edge graphs, for which a sampled subset had fractional LP optimum between about `4.6061` and `4.9334`. This is exploratory, not independently enumerated as distinct isomorphism types.

## 4. Current conjecture and falsifiers

**Fractional obstruction conjecture.** Every triangle-free 16-vertex graph `H` with `α(H)≤5`, `e(H)=33`, and `2≤d_H(w)≤5` has `τ*(H)<6`, where `τ*` is the fractional disjointness domination optimum above. This is deliberately stated without requiring a six-port completion, which would make the claim vacuous if no such completion exists.

The implication `τ*(H)<6 ⇒ no six-port completion` is established. The universal inequality itself is **open in this project**, and need not be true for all residual graphs satisfying the weaker degree constraints. The full catalogue test remains unexecuted because the compressed ANU dataset could not be delivered into the available runtime. The catalogue is at https://users.cecs.anu.edu.au/~bdm/data/ramsey.html (`r36_16.g6.gz`, 2,576 graphs).

A single valid `H` with `τ*(H)≥6` would refute the strong fractional conjecture but would **not** automatically produce a six-clique or a valid 23-vertex Ramsey graph. If that happens, the next tests should separately check compatible six-cliques, the degree-cover matrix, and lower-order Hall constraints, in that order.

## 5. Reproduction

- `ramsey_fractional_port_certificate.py` computes rational certificates from an LP, then verifies them with integer arithmetic and independently checks the 16-vertex graph and independence-number prerequisites.
- `ramsey_fractional_port_certificates.json` stores the two exact certificates (original and high-LP example).
- `ramsey_17parent_fast_probe.py` performs the nonexhaustive structural sampling with exact six-set edge-count checks.
- `ramsey_fractional_port_sample_verify.py` reruns the deterministic sampling and issues integer-verifiable rational certificates for all 27 hash representatives.
- `ramsey_fractional_port_sample_certificates.json` stores the sample certificates and their provenance.
- `ramsey_six_port_catalogue_check.py` accepts the complete 2,576-graph `.g6.gz` catalogue if it becomes available.

## 6. Mathematical priority

Test the universal fractional inequality on the full 16-vertex catalogue before attempting a general symbolic proof. If it survives, search for a graph-theoretic reason `τ*<6` follows from `n=16`, `e=33`, `α=5`, and the degree bounds. If it fails, isolate which port-cover/Hall constraints remain necessary and quantify the smallest higher-order witness. Neither outcome requires the `esd7` geometry.
