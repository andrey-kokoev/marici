# Rzk versus Lean for the coefficient and coherence machinery

## Question

Does the current formal state justify replacing Rzk with Lean simplicial modules, or does Rzk remain an appropriate backend for the zeta-construction programme?

## Claim boundary

The mutable Rzk state through `research/nima/rzk-coefficient-interface-v40.md` refutes the narrow claim that Rzk can express only abstract higher-categorical interfaces here. It now checks concrete finite polynomial and stalk-sensitive coefficient complexes, legal inversions, square-zero laws, chain maps, endpoint quotients, supported residue classification, explicit fibres, Q contractions at reduced scale, filling rigidity, nonflat support distinctions, and several primitive nonboundary detectors.

This does not establish the intended derived category or physical comparison. Three boundaries remain:

1. evaluation-setoid complexes have not been realized by a completion/localization functor into an identity-based derived category;
2. large sparse contractions are partly exact external checker evidence rather than native Rzk terms;
3. neither backend currently contains the missing source-derived spatial supported-dual or conductor–Morse comparison.

Lean's mature module, chain-complex, localization, and homological-algebra libraries make it the stronger candidate for proving the semantic realization and K-projective/RHom statements. Lean cannot repair the third boundary by itself: formalizing an arbitrary map would reproduce the same nonphysical-interface defect.

The first Lean experiment must not use the ordinary comparison `K(Xt) -> K(X,t)` as a candidate preservation theorem. The exhaustive column `t(1-h)e_X + Xh e_t` maps to zero on first Tor at `X=t=0` for every `h`. Likewise, normalization of the normal total chart has zero cofiber, while normalization formed after specialization has the nonzero conductor quotient. The experiment must therefore represent either the actual derived centre or the logarithmic/excess object and state its base-change defect; otherwise it will formalize a known no-go model.

## Decision

Retain Rzk for the existing concrete setoid complexes and higher framed/coherent statements. Use Lean for a bounded comparison experiment: encode one finite free source, its localized target, and prove the raw Hom complex computes the intended derived Hom under explicit projectivity hypotheses. The experiment must record the coefficient category: an ambient `R`-linear contraction is not an `A`-linear strict equivalence. It should admit a derived equivalence through an `A`-linear acyclic kernel or cone without demanding a strict splitting on the displayed representatives. Filtered, supported, and equivariant promotion each require their own equivalence criterion. Do not port all 215 states before that experiment demonstrates a usable semantic bridge.

The bounded Lean experiment is an independent semantic benchmark over the same source specification, not a proposed Rzk-to-Lean interpretation functor. Build a cross-backend bridge only when a named consumer theorem requires both the Rzk coherent structure and Lean homological algebra. Any such claim requires an explicit dictionary preserving coefficient ring, support stage, grading, variance, signs, and admissible localization. It must also distinguish an ambient map, factorization through a principal ideal, filtered connecting symbol, and framed conormal evaluation. For example, `tx*rho` can be null after ordinary Cartier restriction while its first conormal symbol evaluates to one; these are different arrows, not conflicting values of one map. Equal matrices or homology ranks do not provide the dictionary.

## Operational constraint

The measured Rzk loop is dominated by included-library typechecking: approximately 30–38 seconds even when dependency preparation is cached and only one Marici module is staged. This is an engineering cost, not evidence against the formalism. Interactive work may use a verified incremental/LSP lane, but durable claims still require a fresh headless closure until equivalence of those lanes is tested. Backend comparison should include proof-edit latency and certificate size alongside theorem coverage.

## Disposition

The backend choice is hybrid, not a replacement decision. Rzk's synthetic nature is not the source of nonphysical computations; unconstrained assumptions are. The present Rzk work has reduced those assumptions substantially, while the physical comparison remains an external geometric construction problem.
