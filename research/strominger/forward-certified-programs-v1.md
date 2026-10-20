# Closed forward producers and exact diagram certificates

## Successor grammar, not a retroactive reinterpretation

`agda/ForwardCertifiedPrograms.agda` adds a versioned initial-producer grammar with only two constructors: an original root and the **existing chosen forward transport** of a previously generated initial proof. It has no arbitrary Resolve import.

The successor program grammar admits those initial producers, the old closed Program syntax, attachment, and canonical comparison with a checked success guard. Old programs retain judgmentally identical native semantics. The comparison guard is proposition-valued; no supplied full filler is stored as a free producer parameter.

Vertex, finite initial word, mode, outgoing request and program shape remain declared controls. This is not a source-selected unique program.

## Origin obligations and native matching

`InitialCertificate v d` exhibits an initial producer and an equality from its evaluation to the **actual** d. There is no function constructing this for arbitrary native proofs.

`Origins` recursively requires such evidence at every initial proof in a generated Fragment. The theorem `certify` constructs a program and an explicit Fragment equality to the supplied fragment. `native-closure-match` lifts that equality to the entire dependent pair of Complete package and actual Resolve derivation.

For a supplied compatible comparison, the two certified operands are transported explicitly to their producer outputs. Compiler completeness supplies a success guard; justified full-filler propositionality matches the computed comparison back to the actual supplied cell. This is source-relative **producibility**, not a claim of unique historical origin.

Conversely, `producer-origins` checks every successor producer, including legacy programs, and `origins-of-certificate` recovers the origin obligations from a certificate. These are two implication constructions, not inverse laws or a claim that native proof/certificate spaces are propositions.

## Exact common forward witnesses

`Diagram d c0` instantiates the unchanged `ForwardForwardBodyBinding.Diagram d` in an explicit certified initial context. Forward certification yields witnesses for its exact d1 and d2. Neither is replaced by a root proof.

`certified-diagram : AllCertified D.diagram` indexes the **original sixteen-entry list**. It gives producer/native-closure matching for:

- d, d1, d2 and the two comparison outputs;
- all four original interchange-cell outputs;
- the original row and outer endpoints;
- both actual sequential/direct final route terms.

`GeneratedDiagram p` provides a closed instance for every finite initial producer word at A. The construction is not restricted to one root regression.

## Remaining common-witness obligations

The overall objective stays open. The three policy presentations still need binding to this same certified context, with actual native package/derivation matching. The mixed compiled-child history interface also needs producer certification for its actual retained raw root outputs. Higher-envelope outputs are not among the sixteen Fragment entries certified here; their producer binding remains part of the common-context work.

Those raw roots are not silently reclassified as generated Fragments. Their carrier equivalences and history certificates from the preceding packet are not origin certificates, and their provably distinct packages cannot be substituted for compiled outputs by reflexivity.

No old source file, seed policy, native rule or predecessor packet was changed. No global Body action, unrestricted native source-generation theorem, topology-changing coverage or physical conclusion follows.

## Verification

    python research/strominger/checkers/check_forward_certified_programs.py

Fresh safe Cubical/guarded closure passed with ignored interfaces, disabled implicit libraries, stable inputs and a conservative 2,358-file source manifest. Three UnequalTerms controls reject importing a raw Resolve proof as an initial producer, resetting an arbitrary actual proof to a seed, and bypassing a computed comparison refusal.

No repository-source warnings; Cubical dependency warnings are retained in the receipt.

Contract: `contracts/forward-certified-programs.v1.json`.
Receipt and dependency manifest: `results/forward-certified-programs/`.
