# Higher witness admission: exact-code obstruction and a faithful native presentation

## Result

The existing signature CAN admit the already constructed repeated-interchange
higher witness without adding rules or seeds, but NOT in its originally chosen
bare atomic path code.

Both claims are proved:

1. The exact earlier package `path-package (atom CompleteFiller) ...` has no
   `Resolve Seeds` derivation under the current source policy and twelve rules.
2. An existing E/reflexivity construction supplies an admissible envelope whose
   interpreted carrier is equivalent to CompleteFiller. The same higher path is
   admitted in that envelope, and projection recovers the original path exactly.

This is not an illicit coercion between Code constructors. Native admission
remains indexed by the actual retained code, even when interpreted types are
equivalent.

## Audit of the literal higher-rule interface

The native higher rule takes

    higher-rule Q x y p q alpha,
    p,q : x=y,
    alpha : p=q.

Its premises are actual derivations of path-package Q x y p and
path-package Q x y q. The earlier native comparison derivations are not those
premises. Moreover, the formed repeated-interchange witness is a path between
complete filler records, encoded using atom CompleteFiller; it is not already a
path-between-paths in that rule's required Code shape.

Thus simply feeding the two comparison derivations to higher-rule would be an
incorrect boundary substitution, not closure of admission.

## Exact obstruction under the unchanged signature

Define a Boolean Code observation:

    atomicSpine(atom A)=true,
    atomicSpine(paths Q x y)=atomicSpine(Q),
    atomicSpine(other constructors)=false.

The current seeds have a retained wrapper, so their atomicSpine is false.
Every native rule preserves this invariant:

- E, Pi, comparison, retained inverse/composition, distribution and congruence
  outputs have a non-atomic outer constructor;
- reflexivity inherits its spine from its actual input package;
- higher-rule inherits it from its actual path premises.

Induction over Resolve proves false atomicSpine for EVERY admitted package.
The original bare atomic path has true atomicSpine, yielding a checked
non-admissibility theorem.

This invariant respects actual Code paths. It does not use unsafe fixed-index
seed elimination, axiom K, or an assumption that all indexed seed proofs are
literal syntax nodes.

## The actual premise bridge already available

A generic checked lemma shows:

    Resolve S (pack Q x)
      -> (p:x=y)
      -> Resolve S (path-package Q x y p).

Its proof uses the existing reflexivity rule at x and ordinary dependent path
induction/transport along the SUPPLIED path p. No new native rule is needed.
This does not discover p; it admits an already constructed witness once its
pointed package is actually derivable.

The missing ingredient was therefore an admitted presentation of the complete
filler, not a new arbitrary higher-filling principle.

## Constructing the native E envelope from actual comparison premises

For each complete filler f between the fixed source and target Bodies, the
previous native compare construction already gives an actual derivation of its
comparison package. Apply native reflexivity to that package:

    branch(f) = path-package(expression(comparison(f)), value(f), value(f), refl).

Here value(f) abbreviates the selected comparison-package value, not the filler
record itself. Each branch retains the full comparison expression and actual
selected value. Its native premise is the actual comparison derivation.

Now apply the EXISTING E rule with index CompleteFiller and this branch family.
For a selected f its interpreted value is (f,refl). All branch premise derivations
are supplied uniformly as a function of f. No atomic filler seed is inserted.
The family can be infinitely branching; the calculus permits this and the proof
does not enumerate all fillers.

In the present diagram each comparison carrier is proved to be a set. Its
reflexive loop fiber is therefore contractible. Consequently the envelope
projection onto CompleteFiller is a proved equivalence, not just an information-
losing observation or an unrelated equally sized carrier.

For a non-set-valued carrier the same envelope pattern could retain additional
loop structure; the equivalence conclusion would need a separate proof. No
global truncation assumption is made here.

## Admitting and recovering the same higher witness

Let alpha be the previously checked complete-filler coherence. Its envelope
path is

    i -> (alpha(i), refl).

The selected envelope endpoints have actual E derivations. The generic
path-admission lemma therefore produces a native derivation of this envelope
path package under the UNCHANGED Seeds policy.

Projection of the admitted path is definitionally alpha:

    cong fst envelopePath = filler-coherence.

Thus the result admits the already constructed higher witness in a faithful
retained presentation; it does not replace it with an unrelated reflexive path.
The original diagram, both endpoint derivations, the new higher derivation and
its recovery theorem are retained together and reified with exact recovery.

## A subsequent actual higher-rule application

As a separate control, the module derives both envelopePath and
(envelopePath composed with refl) as native path packages. The supplied standard
right-unit coherence then feeds the unchanged higher-rule with EXACTLY its two
required path-premise derivations.

This confirms that native higher-rule use becomes valid once the proper path
premises are admitted. The unit-coherence control is not presented as a
substitute for the original interchange witness, which was admitted earlier
through the faithful envelope.

## Consequence for the conjecture

For this source and diagram, the local higher-admission test succeeds without
extending the rule signature. The obstruction concerned the chosen bare atomic
presentation. An admitted, equivalent E presentation provides the bridge.

The result does not prove universal admission of every equivalent Code, automatic
higher-witness discovery, completeness of the twelve-schema calculus, or all-
dimensional interchange coherence. Native admissibility and interpreted
equivalence remain distinct properties.

## Verification

    python research/strominger/checkers/check_higher_witness_admission.py
    python research/strominger/checkers/check_repeated_interchange_coherence.py

Fresh headless closure with ignored interfaces passes under Agda 2.8.0.1 /
Cubical 0.9. The safe Cubical/guardedness module contains no postulates or holes
and introduces no unsupported indexed-match warnings.

Two intended negative controls are rejected (exit 42 each):

- presenting the envelope derivation as a derivation of the bare atomic path;
- substituting a comparison derivation for a higher-rule path premise.

The predecessor higher-coherence regression also passes. Its previously checked
filler-coherence proof was made abstract to avoid expanding a large nested path
normal form in subsequent dependent transport. Its type and proof body are
unchanged and freshly rechecked; no axiom was added.

Artifacts:

- `agda/HigherWitnessAdmission.agda`
- `agda/negative/HigherBadAtomicReinterpretation.agda`
- `agda/negative/HigherBadComparisonPremise.agda`
- `checkers/check_higher_witness_admission.py`
- `results/higher-witness-admission.json`
- `results/higher-witness-admission-positive.log`
- `results/HigherBadAtomicReinterpretation-negative.log`
- `results/HigherBadComparisonPremise-negative.log`

Source hashes remain stable across verification. Temporary diagnostic probes
were removed. Only Strominger-owned files were edited; generated dependency
interfaces may be refreshed. No physical claim, graph publication, commit or
push.
