# A typed retained-package feedback loop closes its own admission boundary

## Result

A restricted whole-package feedback adapter now consumes its own admitted
reified output, derives the next outgoing-edge question from the decoded
retained endpoint, and uses the retained native derivation as the next rule
premise. It does not obtain fresh vertex-seed derivations on each application.
Its result carries the admission certificate required to apply the same adapter
again.

Fresh Agda checking proves preservation of the decoded prior payload and of the
actual previous native endpoint-and-derivation pair. This is a constructive local
instance of recursive admission closure, not a universal theorem about arbitrary
Complete values or all possible source/task signatures.

## Why this differs from the preceding construction

`SourceIndexedExtensionFamilies.agda` derives incidence-indexed families at each
specified depth, but its native branch derivations are compiled from the original
endpoint seeds. Merely reifying those derivations did not make one result the
input of the next construction.

The new `RetainedPackageFeedback.agda` instead has an indexed retained chain:

    initial(v,d), where d derives pointQ(v);
    extend(previous, edge), where edge : Out(current endpoint).

The actual initial derivation d is supplied once and retained. Every extension
contains the complete previous chain and the new incidence witness. Its native
interpretation is built from the previous chain's retained derivation, not a
call to root at its current endpoint.

## The native application and explicit premise recovery

Let q,d be the complete native package and derivation represented by the prior
chain, with current boundary v. The next construction uses the existing rules:

1. Reflexivity applied to q, with d as its premise.
2. E indexed by Out(v), with that reflexivity derivation at every branch and
   the supplied actual outgoing witness as the selected index.

The E code retains the full branch family, and each branch path code retains q's
expression and actual selected value. The chain additionally retains its entire
predecessor, including all earlier incidence witnesses and the initial actual
native derivation.

A checked `peel` reader takes the selected premise from the actual native E
derivation, then takes the sole premise from its reflexivity derivation. The
result is EXACTLY the preceding complete package and derivation. This is a theorem
about stored native premises, not just a separately copied endpoint field.

The AB and AD selections from the A-boundary have provably different interpreted
E values. The construction is not solely a repeated certificate with no branch
distinction. On the other hand, an endpoint return such as AB followed by BA
still retains both attachments; it does not erase the chain.

## Typed whole-package input and admission closure

The reified payload type is

    Total = Sigma(v:Vertex) Chain(v).

A Ready input contains a next-universe Complete plus an equality certifying that
its code is atom(Total). Decoding uses its ACTUAL resolved value and that code
certificate. There is no assumed decoder for arbitrary type-valued syntax.

The API is:

    Task(r) = Out(boundary(decode(r))),
    run(r,edge) = encode(extend(decode(r),edge)).

The returned Complete has code atom(Total), with reflexive admission evidence.
The type therefore supports

    run(run(r,e),f)

when f inhabits the task family determined by the first returned package. The
first proof does not manufacture f: formation of a well-typed next question and
construction of its answer remain distinct.

Agda proves:

- decoding an encoded payload recovers that payload;
- the decoded run result contains the entire previous decoded payload;
- peeling its native premises recovers the previous native endpoint/history;
- the run result is Ready and can serve as the next run input.

Recovery here concerns the decoded full construction payload and native history.
It does NOT assert literal retention of every possible admission-path witness or
serialized presentation of an arbitrary Ready argument. The adapter's canonical
outputs have reflexive admission proofs. No broader proof-irrelevance claim is
used.

## Universes and fixed policy

The native chains contain small Complete values and their Type1 derivations.
Their retained payload is Type1, and reifying it uses Complete at the next
universe. Ready additionally contains its code-equality admission evidence.
No universe contains itself, and no arbitrary complete package can be cast into
this payload without the required code witness.

Finite chain extension occurs inside this fixed typed adapter. It is not an
unrestricted tower that internalizes its own universe, all possible admission
policies, and all higher fillers at one level.

The source graph and the outgoing-attachment policy remain FIXED in the adapter.
The changing boundary is obtained from the actual retained output. Thus this
establishes boundary/admission closure for that policy, not derivation of the
policy itself. Native E/reflexivity rules remain unchanged; the adapter is not
claimed to be an automatically discovered primitive rule of the generic calculus.

## Transport scope and remaining synthesis

The preceding module proves source-symmetry transport of path indices and
native selected E packages. The new feedback module does not yet prove transport
of arbitrary INITIAL native derivations inside the richer retained-chain type.
Replacing those derivations by fresh symmetric seed proofs would erase precisely
the provenance this test preserves, so that shortcut is not used.

The full recursive-closure conjecture is therefore only partially established:

- actual retained output feeds the next boundary: checked;
- an actual native extension consumes its retained derivation: checked;
- output admission supports repeated use of the same adapter: checked;
- uniform source-compatible transport of arbitrary feedback histories: open;
- source derivation of every admissible task policy: open;
- automatic selection of an outgoing witness: not claimed.

No physical time, execution event, uniquely preferred path, universal higher
filler or intended T9 interpretation is introduced.

## Verification

    python research/strominger/checkers/check_retained_package_feedback.py

Fresh headless Agda closure with `--ignore-interfaces` passes under Agda 2.8.0.1 /
Cubical 0.9. The safe Cubical/guardedness module has no holes, postulates or new
unsupported indexed-match warnings. A negative attachment using CA at the A->D
boundary is rejected by the kernel (exit 42).

The independent finite control exhausts retained configurations through depth six:
4,6,10,16,26,42,68. Initial seed construction occurs four times only. Every later
model application retains the previous evidence object; selecting and peeling
its native-style premises recovers that same evidence. This model is a regression
control, not a replacement for the general Agda proofs.

Artifacts:

- `agda/RetainedPackageFeedback.agda`
- `agda/negative/FeedbackBadAttachment.agda`
- `checkers/check_retained_package_feedback.py`
- `results/retained-package-feedback.json`
- `results/retained-package-feedback-positive.log`
- `results/retained-package-feedback-negative.log`

Source hashes are stable across the verification run. Only Strominger-owned
source/report/checker files were edited; dependency interfaces may be refreshed
by fresh Agda checking. No graph publication, commit or push.
