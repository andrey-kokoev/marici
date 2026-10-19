# Seed-prefix completeness — net iteration9

## Theorem

Let U be a finite packet universe containing root r. Let C be a hereditary compatibility predicate: C(S) implies C(T) whenever T⊆S. Each directed interface e=(s,t) has selected-set eligibility E(e,S), requires s,t∈S, and satisfies **endpoint-preserving downward closure**:

> E(e,S) and {s,t}⊆T⊆S imply E(e,T).

Then every compatible selection S containing r, whose active interface graph is rooted at r, admits an ordering r,p₁,…,pₖ of its packets such that every prefix is compatible and rooted. Each new packet is added by an interface active in the enlarged prefix.

### Proof

Take a directed spanning tree of the final active graph of S, rooted at r. List vertices with parents before children. Every prefix is a subset of S and hence compatible. For each nonroot prefix vertex, its tree edge has both endpoints in that prefix and was active in S. Endpoint-preserving downward closure keeps the edge active in the prefix. Those tree edges connect the entire prefix to r. The edge to the newly listed vertex is therefore an admissible addition. This constructs S in |S|−1 additions. ∎

### Generator corollary

An exhaustive additive generator that starts from r, tries every interface target from a selected source, and retains exactly compatible rooted selections enumerates every such S. Soundness follows from the acceptance check; completeness follows from the ordering above. Deduplicating by selected set is safe when eligibility is a function of that set. A resource-limited run is not necessarily complete.

Final exit and native-face-witness obligations can be applied afterward without losing a valid final certificate. They are **not** required at every intermediate prefix. Arbitrary-start extension completeness is a different question.

## Instantiation for the current P/N/E grammar

`generative-phase-assembly.mjs::describe` enforces occupied-cell species, global C/M roles, allowed face-contact species and shared-face C/M counts. These are hereditary: each occupied body has its vertices marked by its own chart; a retained pair preserves those marks and its contact classification. Deleting other packets cannot introduce a new occupied pair or inconsistent mark. This is why the pair-conflict compiler is appropriate here. The executable check also verifies body-vertex coverage for all compiled charts through D4.

Native transfer eligibility requires only its source and target packets. Its transport, geometry, occurrence and map checks are fixed properties of the interface, not positive selected-third-packet conditions.

A terminal-PE edge additionally requires:

1. no selected packet occupying its reference neutron **body**;
2. no selected target of any native outgoing operation from that particular P reader.

For a fixed universe, these compile into a forbidden-packet set F(e). Eligibility is precisely `{s,t}⊆S` and `S∩F(e)=∅`. Removing packets while retaining endpoints cannot disable such an edge. The neutron reference remains in the validated factor metadata; it is not a positive occupancy requirement.

The theorem therefore applies to finite universes of both native and experimental-terminal-PE interfaces, provided enumeration is complete and the stated source rules are retained. It explains complete seed generation, not physical validity beyond the source model, not exhaustive search under resource stops, and not arbitrary-start repair.

## Executable evidence

The checker enumerates all3-packet directed interface systems in which each of the6 nonself edges is absent, unconditional, or forbidden by the third packet:3⁶=729 systems. It combines each with all8 pair-conflict masks, yielding5,832 models and23,328 root-containing selection checks. For each selection, direct compatible-rooted acceptance is compared against additive generation; every accepted selection also gets a replayed spanning-tree prefix construction.

Source checks cover D0–D4 in both modes, deterministic sampled selections, and the nontrivial D4 repaired-core witness. They compare compiled negative guards against the source auditor, verify deletion preserves compatibility and active endpoint-retaining edges, and replay rooted constructions. These finite checks supplement the proof and source-rule analysis; they are not its generality argument.

Two controls demonstrate necessary hypotheses:

- **Positive third support:** r→a requires b, while r→b requires a. The final set is rooted, but neither first addition is available.
- **Nonhereditary compatibility:** only {r} and {r,a,b} are compatible along a chain r→a→b. The final rooted selection cannot be reached through compatible prefixes.

This is a written mathematical proof with executable checks, not a proof-assistant formalization.

## Next frontier

Determine what changes when construction must retain a pre-existing rooted selection A. A final spanning-tree ordering need not put all of A first. Investigate whether negative guards can make all single-packet extensions of A fail despite a compatible rooted superset, and characterize a sufficient scheduling condition or atomic batch repair. Distinguish generic guard counterexamples from actual P/N/E realizations.

```sh
node research/nima/checkers/check_prefix_completeness.mjs
```

[Checker](checkers/check_prefix_completeness.mjs) · [Receipt](results/prefix-completeness/verification.json)
