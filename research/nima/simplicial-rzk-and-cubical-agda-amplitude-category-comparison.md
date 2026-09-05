# Simplicial Rzk and Cubical Agda for amplitude categories

## Question

How does Grothendieck's simplicial type-theory lane run in parallel to Voevodsky's Cubical Agda lane, and where can it apply to amplitude modelling?

## Claim boundary

The Rzk lane formalizes directed categorical composition and its coherent simplices. The Cubical Agda lane formalizes equality/coherence boundaries and an additive fixture complex. They are complementary backends, not two proofs of one structure. No checked interpretation functor currently connects them or assigns physical amplitude semantics to either.

## Rzk increment

The first Rzk module constructs canonical composition in a Segal type, retains its two-simplex witness, and derives associativity of three arrows from a three-dimensional filling theorem. The Rezk entry point adds the relevant completeness condition.

The interpretation module maps arrows and two-simplex witnesses pointwise and uses target Segal uniqueness to prove preservation of canonical composition. Later functoriality modules prove identity and composition laws for those maps on arrows and retained fillers. The arithmetic bridge correctly distinguishes `is-discrete` from sethood and makes the discreteness premise explicit.

This is categorical composition, not additive exactness. The `ExtExt` assumptions and every supplied Segal, Rezk, or discreteness witness remain premises rather than derived amplitude facts.

## Relation to Cubical Agda

Voevodsky's native cubical skeleton checks that edges, squares, and cubes have compatible boundaries. Its pasting complex checks an oriented additive chain complex and uniqueness modulo vertex adjustments over integer coefficients.

Grothendieck's simplicial shell instead answers which directed arrows compose, which two-simplex witnesses exhibit the composite, and why triple composition is associative. A comparison requires a typed functor from the Rzk Segal/Rezk object to an additive target whose images agree with the Agda boundary maps. Similar triangle notation is not such a functor.

## Amplitude dictionary

For a source-audited amplitude graph:

- objects may be branch-labelled kinematic regions or labelled divisor strata;
- directed arrows may be residue, restriction, cut-gluing, sewing, or admissible continuation maps;
- a two-simplex records a source-authorized composite factorization rather than erasing it to an equality;
- the three-dimensional filler compares triple compositions;
- an interpretation map sends the abstract arrows and simplices to analytic kernels, rational functions, distributions, or state-space maps while preserving composition.

This makes Rzk a closer fit than the integer cubical complex for the directed category of factorization operations. Cubical Agda remains the closer fit for additive incidence, obstruction classes, gauge adjustments, and explicit equality boundaries.

## Applicability gates

1. Segal uniqueness is admissible only when the labelled source data determine a contractible space of composites. Multiple analytic branches, contour choices, subtraction schemes, or monodromy invalidate an unlabelled Segal presentation; they must be promoted into object or arrow labels, or the structure must remain lax/non-Segal.
2. Rezk completeness does not authorize treating physical gauge equivalence, crossing equivalence, or field redefinition as identity. The source theory must specify the equivalences and prove that the interpretation descends.
3. A directed simplex is not physical time, propagation, or causal order. It records typed composition order unless a separate map to physical time is supplied.
4. Pointwise functoriality does not supply analyticity, unitarity, positivity, normalization, or a cut prescription.
5. The current Rzk arithmetic lane does not make factorization arithmetic or adelic. That requires an independently derived interpretation.

## Conditional comparison target

Do not mix the proof assistants by default. Choose Rzk when the target theorem is directed Segal/Rezk composition; choose Cubical Agda when it is cubical boundary typing or additive exactness. Maintain one source-level amplitude specification independent of either backend.

A cross-backend comparison is justified only if a named amplitude theorem simultaneously needs both structures and neither backend can express it alone. Then use one smallest connected source graph, define separate interpretations into each backend, and prove a commuting comparison at the mathematical specification level. Do not import generated terms from one proof assistant into the other or treat one checker result as an assumption in the other.

## Verification status

The Rzk README records the checked core and its pinned dependency boundary. A later Grothendieck report states that 124 modules were verified while 17 successors remain unverified because the admitted structured-command surface suppresses the pinned Rzk child executable. The entire locus is untracked and has no commit baseline. Therefore the unverified successors cannot be used as checked premises.

## Disposition

The default is parallel, noncomposed backends with a shared source specification. A comparison functor is not the next target unless a concrete amplitude claim requires both directed composition and additive obstruction data. Without that consumer theorem, building the bridge adds toolchain, translation, and coherence obligations without increasing scientific evidence.
