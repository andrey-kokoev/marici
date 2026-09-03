# Applicability of `agda/cubical` to SCC

## Question

Can the public `agda/cubical` library strengthen SCC's executable treatment of displayed lifting towers, selectors, identity, quotients, and higher coherence?

## Claim boundary

This is a repository-interface assessment from the public README, module tree, metadata, and current Marici sources. No Agda toolchain was installed, no library source was vendored, and no SCC theorem was checked by Agda. Applicability means that the library exposes matching formal objects; it does not imply theorem portability from UniMath or physical adequacy.

## Observed interface

The repository describes itself as the standard library for Cubical Agda and current `master` targets Agda `v2.8.0`. Public metadata observed on 2026-09-03 reports recent activity, default branch `master`, and an experimental-library description. Its root license is MIT with file-specific exceptions, including BSD-3-Clause cases.

The public tree contains 32 paths under `Cubical/Categories/Displayed`, including bases, functors, natural transformations, sections, total categories, reindexing, and structure-over instances. It also contains `Cubical/Foundations/SIP.agda`, foundational and dependent univalence modules, and a large higher-inductive-type library.

## Applicable SCC obligations

The strongest fit is a second formal backend for the structural layer, not a replacement for the current UniMath backend.

1. **Displayed lifting IR.** `Categories/Displayed/Section` and `Instances/TotalCategory` match SCC's fibers, global selectors, forgetful projections, and iterated totals directly.
2. **Selector invariance.** Cubical paths and dependent transport can state that a selector commutes with base paths, reindexing, and declared symmetries. This addresses SCC's current gate that selector existence alone is insufficient.
3. **Non-canonicity.** Multiple fillers together with a symmetry path/action can be used to prove that no invariant selector exists, rather than merely recording two elements.
4. **Identity modalities.** SIP and univalence can separate literal/path identity, structured equivalence, displayed isomorphism, and identity induced by univalence. This matches SCC's identity witness gate.
5. **Quotients and coherence.** Higher-inductive types are relevant to gauge quotients, truncations, homotopy fibers, and explicit higher coherencers where set-level quotienting discards required route structure.

## Non-applicable or unproved promotions

- Existing Rocq/UniMath proofs do not transfer automatically to Cubical Agda.
- The library does not supply Marici's source-derived physical maps, detector semantics, RH positivity, Flavor selectors, or readout authority.
- A displayed category does not by itself provide a bicategory or the sector-specific coherence laws SCC needs.
- No Agda project or Agda dependency was found in the current research tree, so integration would add a distinct toolchain and reproducibility contract.
- `master` should not be used as an unpinned dependency; a commit and Agda version must be frozen.

## Recommended bounded pilot

Use an isolated `research/aspect/scc/agda/` backend with a pinned library commit and Agda 2.8.0. Formalize only:

1. a two-layer displayed tower and total category;
2. empty fiber implies no global section;
3. two fillers plus a fixed-point-free involution imply no invariant selector;
4. selector transport along base paths;
5. one univalent identity conversion;
6. one HIT quotient retaining the stated path constructor.

Adopt the backend only if these six obligations typecheck and the generated SCC certificate records the Agda version, library commit, source digests, checked modules, and assumptions. Keep UniMath as the comparison backend; disagreement between the two formalizations is a typed residual, not a reason to weaken either test.

## Disposition

Applicable with high expected value for selector invariance, symmetry-based non-canonicity, quotient paths, and higher coherencers. Not yet integrated. The next admissible action is the bounded pinned pilot, not migration of existing UniMath proofs.
