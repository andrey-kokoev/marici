# Rzk arithmetic-reconstruction feasibility audit

## Question

Can an Rzk lane reconstruct the compact-source arithmetic kernel without importing analytic semantics as uninterpreted structure?

## Evidence boundary

No Rzk files or project configuration are present in this repository: a repository-wide `**/*rzk*` search returned zero paths. Under explicit operator authorization, the official Windows x64 release archive for Rzk v0.11.3 was downloaded from `rzk-lang/rzk` and installed at `C:/Users/andrey/.local/bin/rzk.exe`. `rzk version` reports `0.11.3`; the installed executable SHA-256 is `ad2d3fade7c9f225f8072b72fb7a4560d88d054e385a8600dd682d2f68bdb026`. A temporary checkout of upstream `rzk-lang/sHoTT` main at commit `52a441cc4aaa03f3fe94ee94f70bb2874e26a6a2` passed `rzk typecheck` with `Everything is ok!` and warnings about meta-prefix arguments. Its checked modules include simplicial type theory, extension types, Segal and Rezk types, covariant families, Yoneda, adjunctions, cocartesian families, and limits/colimits. This establishes that a simplicial categorical shell is executable; it does not establish the arithmetic and constructive-analytic substrate listed below.

## Feasibility matrix

| Target | Disposition | First required typed object | Acceptance test |
|---|---|---|---|
| Generic pasting-complex exactness | Conditionally feasible | A checked Rzk definition of the indexing shape, boundary maps, and zero-composite witnesses | The Rzk checker accepts the generic complex and exactness statement without arithmetic or analytic axioms |
| Free additive kernel syntax | Conditionally feasible | A native inductive/free additive object or a source-derived encoding with its recursion and induction principles | Constructors, additive evaluation, and uniqueness are checked; no quotient equality is postulated |
| Source-natural evaluation maps | Blocked pending the first two rows | A functorial interpretation from free syntax into a declared additive target | Naturality squares and compatibility with differentials are checked internally |
| Abelian groups | Unknown locally | A pinned Rzk library/module supplying groups, homomorphisms, kernels, images, and abelian laws | Minimal import and an internally checked kernel/image example |
| Quotients | Unknown locally and critical | A quotient/HIT or set-quotient with elimination and computation rules adequate for cokernels | Construct a cokernel and check its universal property; propositional truncation alone is insufficient |
| Rationals | Unknown locally | A normalized rational object with field laws, or a proved fraction quotient | Check normalization independence and field identities without assuming the result as an axiom |
| Constructive reals/completion | Blocked | A Cauchy or Dedekind real construction, modulus discipline, equivalence relation, quotient, completeness theorem, and extension principle | Extend a uniformly continuous rational map uniquely and prove independence of representatives |
| Exponential and cosine | Blocked by constructive analysis | Constructive definitions on the real object plus convergence, algebraic identities, and continuity/uniform-continuity theorems | Prove the identities used by the kernel and justify extension from rational approximants |
| Arithmetic/completion derived rather than inserted | Blocked until the preceding substrate exists | A derivation chain from integer/rational syntax through completion to analytic operations | Every evaluation map factors through checked constructors and universal properties; no opaque `Real`, `exp`, or `cos` constants occur |

## Scoped microprogramme

### RZK-G0 — Toolchain and library authority

Pin the Rzk executable, version, project manifest, standard library revision, and checking command. Inventory native support for inductive types, set truncation, quotients/HITs, algebraic structures, rationals, Cauchy/Dedekind reals, series, exponential, and cosine.

Stop if the checker or dependency revision cannot be pinned. This is the current branch state because the executable preflight was refused and no local project is materialized.

### RZK-G1 — Additive syntax, without quotients

If native inductive families are available, encode the finite generator syntax and its structural recursion. Interpret it in an arbitrary explicitly supplied additive target. Prove evaluation naturality by induction.

This stage may establish free syntax and source-natural evaluation only. It must not call the target an abelian-group quotient, completion, or analytic kernel.

### RZK-G2 — Quotient and homological substrate

Construct or import reviewed abelian groups, kernels, images, cokernels, and the quotient eliminator needed for exactness. Reconstruct generic pasting-complex exactness independently of the compact-source constants.

Stop if quotient computation or elimination is only postulated. Do not replace a missing quotient by representatives and then state quotient-level uniqueness.

### RZK-G3 — Rational arithmetic

Derive rationals from integer pairs modulo the proved fraction relation, unless a reviewed native rational implementation already exposes the same universal property. Instantiate the additive syntax and prove normalization independence.

### RZK-G4 — Constructive completion

Choose one completion construction and state its topology/uniform structure and quantifiers. Build the completion map and extension theorem. This stage is undefined until quotient support and rational arithmetic pass their acceptance tests.

### RZK-G5 — Analytic operations

Define exponential and cosine by a source-derived constructive route, prove convergence in the chosen completion, and prove precisely the identities and continuity estimates needed by the compact-source evaluation. Do not import uninterpreted operation symbols as analytic semantics.

### RZK-G6 — Arithmetic-kernel reconstruction

Only after RZK-G0 through RZK-G5 pass, instantiate the source-natural evaluation with the centered half-divisor, gamma, and prime-translation coefficients. Audit each coefficient and completion map against the external classical source contract. The resulting theorem is conditional on those source identifications; internal type checking does not certify them.

## Ownership interface

`marici.Grothendieck` owns RZK-G2 through RZK-G6: additive arithmetic, quotients, rationals, completion, analytic operations, and the audit that arithmetic is derived. `marici.Voevodsky` owns comparison of Rzk shapes with the Cubical Agda lane and the higher-coherence/pasting interface. Neither owner may infer semantic equivalence from parallel type signatures.

## Disposition

The lane is admissible as a staged research microprogramme. The Rzk v0.11.3 executable is now available, so RZK-G0 can begin. Analytic reconstruction remains blocked at the first missing typed object—a pinned project and standard-library inventory—and no surrogate theorem should be opened downstream until that object exists.
