# Exact source admission and mixed native constructor closure

## Result

A specified source contract now determines its witness family up to an
equivalence preserving its decoder, and that family participates in a mixed
native construction with no new admission predicate between the constructors.

The contract is: retain ALL source-incidence attachments, with exact realization
of their actual witnesses. The two admitted task schemas are source attachment
and the native identity-comparison constructor. Their outputs can serve as
inputs of either schema for arbitrary finite mixed constructions. Whole-history
source transport and native-premise recovery are checked.

This is a restricted instance of the source-determined admission conjecture.
Exactness is an explicit part of the declared contract; bare retention does not
imply it. The two-schema fragment is declared, not a discovered universal menu.

## A precise criterion that distinguishes competing policies

At a boundary v the source request family is

    Out(v)=Sigma(w:Vertex) Edge(v,w).

A candidate representation I must expose its target and its ORIGINAL incidence
witness. These fields define a decoder d:I->Out(v).

The exactness contract says that every parameterized family of source requests
has a contractible fiber of realizations through d:

    for every T, post_d:(T->I)->(T->Out(v)) is an equivalence.

This preserves actual realization evidence; it is stronger than merely saying
that some realization exists. The Agda module derives an inverse of d rather
than assuming it:

1. Use exactness at T=Out(v) to realize the identity request family, obtaining
   an inverse candidate and its right inverse law.
2. Use exactness at T=I to prove the left inverse law.

Therefore d itself is an equivalence. Conversely, an equivalence d satisfies
exactness for all T. The canonical Out(v) representation satisfies the contract
by identity maps.

The result determines the representation RELATIVE TO ITS SOURCE DECODER; it does
not identify arbitrary equally sized carriers or erase boundary provenance.
Different exact representations are equivalent through their source decoder.

The requirements distinguish earlier alternatives:

- Selecting only AB at A misses the AD request: completeness fails.
- Duplicating each outgoing witness with an independent Boolean tag realizes
  every request but has two distinct realizations per request: exactness fails.
- A contractibly redundant presentation is allowed: equivalence, not literal
  serialized identity, is the criterion.

A duplicated-witness system may be a valid DIFFERENT task with extra retained
content. The theorem says it is not an exact representation of this same declared
request family. Likewise, the native E rule still accepts arbitrary supplied
indices; its generic signature does not itself impose this all-attachments
contract.

## Mixed closure through actual native rules

`MixedSourceAdmissionClosure.agda` defines retained assemblies with three forms:

    initial(v,d),
    attach(previous,edge),
    certify(previous).

Here d is an actual native derivation of pointQ(v); edge inhabits Out(v).
Certification uses the existing native identity-comparison rule, not a newly
postulated filler. The interpreted complete outputs are:

- attachment: the existing E package indexed by Out(v), with native reflexive
  branch witnesses of the previous complete package;
- certification: identity-comparison of the previous complete package.

The native compiler supplies actual Resolve derivations recursively. Attachment
uses the prior native derivation through the reflexivity/E premises; certification
uses it as the identity rule's premise. Neither constructor obtains a fresh seed
at the new endpoint.

Both outputs remain typed assemblies. Their task family is

    Task(assembly at v)=Out(v) + Unit.

Consequently either constructor can consume an output of the other without an
additional admission predicate between them. This is an all-finite-mixed-history
Agda theorem, not just two manually prepared examples.

Readers of the actual native premises recover the preceding native endpoint and
derivation: one premise layer for certification, two for attachment. Reification
retains the entire mixed assembly and its current native closure, with exact
recovery. This does not claim a decoder for arbitrary complete syntax outside
this declared interface.

## Source covariance extends to the mixed histories

The existing univalent endpoint-package transport acts on arbitrary initial
native derivations. It is reused without collapsing indexed seed proofs.
Attachment edges move with their actual source-incidence witnesses; certification
is preserved as the identity-comparison constructor.

Forward and separately defined backward transports are proved mutually inverse
on the complete mixed assembly type. For either admitted task:

    move(run(a,t)) = run(move(a),moveTask(a,t)).

Applying the native compiler gives equality of complete native endpoints and
retained derivations across this square. As before, this does not prove that the
chosen forward lift squared is identity on all indexed proof data, or provide
all higher coherences for arbitrary source isomorphisms.

## Closure is not an interchange law

Both of the following are admitted:

    certify(attach(base,AB)),
    attach(certify(base),AB).

Agda proves that their complete packages are NOT literally equal: one has a
comparison code at its outer boundary, the other an E code. They retain different
construction orders. This does not prohibit a separately supplied interpreted
comparison between them, but neither closure nor covariance provides permission
to erase the difference.

The comparison task in this packet is specifically canonical native identity
comparison. Admission of arbitrary nonidentity comparisons, policy-preserving
interchanges, and higher fillers remains outside this mixed fragment.

## Conjecture status

The local structural test is positive:

    exact source request contract
      -> decoder-preserving determination of the witness family
      -> native attachment/comparison closure
      -> retained evidence and source-covariant mixed histories.

No new source policy is needed BETWEEN these two constructors. However, the
exactness requirement, all-attachments task, and two-schema fragment remain part
of the declared source contract. The work does not derive that contract uniquely
from unstructured retention or from the full twelve-schema calculus.

## Verification

    python research/strominger/checkers/check_mixed_source_admission.py

Fresh headless Agda closure with `--ignore-interfaces` passes under Agda 2.8.0.1 /
Cubical 0.9. The new safe Cubical/guardedness modules contain no postulates or
holes and introduce no unsupported indexed-match warning.

The negative control attempts to attach CA at the A boundary AFTER native
certification. It is rejected at Edge(A,D), showing that comparison has not
released the source attachment constraint (exit 42).

Finite controls enumerate 157 candidate decoders and check exactness against
parameterized request sets of sizes zero, one and two. The mixed-history control
checks 1,968 transport/application squares. Assembly counts at depths zero through
five are 4,10,26,68,178,466. These are structural regression counts, not physical
states, execution times, dimensions or rung identifications.

Artifacts:

- `agda/ExactSourceAdmission.agda`
- `agda/MixedSourceAdmissionClosure.agda`
- `agda/negative/MixedBadBoundaryAfterComparison.agda`
- `checkers/check_mixed_source_admission.py`
- `results/mixed-source-admission.json`
- `results/mixed-source-admission-positive.log`
- `results/mixed-source-admission-negative.log`

Source hashes are stable across verification. Only Strominger-owned files were
edited; dependency interfaces may be refreshed by Agda. No physical claim, graph
publication, commit or push.
