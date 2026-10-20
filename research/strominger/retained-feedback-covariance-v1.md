# Retained feedback satisfies a source-comparison extension square

## Result

For the six-arrow source comparison and the existing outgoing-attachment feedback
adapter, Agda now proves that transporting a COMPLETE retained construction and
then extending agrees with extending and then transporting. This includes the
initial native derivation, all retained edge witnesses, the interpreted native
Resolve history, and the actual canonical Ready output/admission record.

This is a local covariance theorem for the declared comparison and task policy.
It is not yet a functorial action of every source isomorphism with all higher
coherences, nor a derivation of the task policy itself.

## The initial-history problem cannot be bypassed

A Chain starts with an actual inhabitant

    d : Resolve Seeds (pointQ(v)).

Replacing d by a freshly generated root at sigma(v) would erase its provenance.
Nor did this work establish that every such indexed proof is literally the
syntactic seed node. Its index includes type-valued Code; direct seed-pattern
elimination encounters the Cubical no-K boundary. No uniqueness of indexed seed
proofs or general proof irrelevance is assumed.

Instead, the new module constructs a path of COMPLETE endpoint packages using
univalence for the source vertex equivalence:

    pointPath(v) : pointQ(v) = pointQ(sigma(v)).

The retained graph package remains present. The interpreted vertex carrier and
selected value move along the univalent path. Transport in the actual dependent
family Resolve Seeds then supplies

    moveInitial(v,d) = subst (Resolve Seeds) (pointPath(v)) d.

This acts on the actual supplied derivation, including any indexed transport
already present in it. It neither invents a fresh seed lookup nor replaces the
proof by a Boolean existence claim.

## Inverse transport, not an unproved lifted involution

The reverse lift transports along the inverse endpoint path. Standard dependent
transport cancellation proves both inverse laws for the initial derivations.
Recursive edge transport then yields mutually inverse maps move and back on

    Total = Sigma(v:Vertex) Chain(v).

The module constructs an actual equivalence Total~=Total and proves recovery
of the entire retained payload in both directions.

Although sigma squares to identity on the four source vertices, this report does
NOT claim that applying the chosen FORWARD history lift twice is identity. Its
proved inverse is the separately constructed backward lift. Identifying the two
lifts, or furnishing a fully coherent C2 action on every indexed proof, requires
additional comparison/coherence work. No endpoint identity is silently promoted
to identity of retained proof transport.

## The full extension square

For a retained chain c and actual admissible edge e, the theorem is

    move(step(c,e)) = step(move(c),moveOut(e)).

Both sides retain the same transported previous chain and transported edge. The
statement is uniform over all finite chains and arbitrary initial derivations
of the declared endpoint type.

Applying the native interpreter gives equality of the complete native endpoint
AND its Resolve derivation on the two routes. Peeling the selected E premise and
its reflexivity premise recovers exactly the transported previous native
endpoint/history pair.

This is stronger than the earlier statement that source relabelling preserves
path endpoints or path counts. The actual retained proof data occur in the
commuting square.

## The square for actual admitted reified outputs

Ready inputs include a Complete and a code-equality admission certificate.
Their decoding may involve nontrivial type transport. Define

    moveReady(r)=encode(move(decode(r))).

The edge witness must also be transported through the decode/encode normalization
path to inhabit Task(moveReady(r)). The new moveTask performs that dependent
transport; simply copying the old edge would be ill-typed.

Agda proves the equality of Ready records

    moveReady(run(r,e)) = run(moveReady(r),moveTask(r,e)).

Thus the outputs agree including their canonical code-admission evidence, not
only after an endpoint observation. The theorem also applies when r is already
a previous run result. It does not assert literal preservation or proof
irrelevance of every possible INPUT admission-path presentation.

## First composition result

The two-extension task fiber is

    TwoTasks(c)=Sigma(e:Questions(c)) Questions(step(c,e)).

Both witnesses and their dependent seam transport together. The module proves
the corresponding two-extension square for full retained chains. This begins
the proposed dependent-fiber composition synthesis without replacing dependent
fibers by a constant Cartesian product.

At A there are three two-edge possibilities: AB BA, AB BC, AD DB. There are not
four independent choices from a uniform binary alphabet: the second branch
family is determined by the first actual output boundary.

No classification theorem for arbitrary composite fibers or universal higher
fillers is inferred from this example.

## Verification and controls

    python research/strominger/checkers/check_retained_feedback_covariance.py

Fresh headless Agda closure with `--ignore-interfaces` passes under Agda 2.8.0.1 /
Cubical 0.9. The safe Cubical/guardedness module has no postulates or holes and
introduces no unsupported indexed-match warning.

A negative module moves the package from A to B but attempts to reuse the
unmoved AB attachment. The kernel rejects the resulting edge boundary (exit 42).

An independent symbolic finite control checks 556 extension squares and 900
two-extension squares, along with two-sided inverse recovery and native-style
premise recovery. Two opaque initial-evidence tags detect accidental replacement
by fresh seed evidence. These tags are regression parameters; the script does
NOT claim to enumerate or count inhabitants of native indexed derivation fibers.

Artifacts:

- `agda/RetainedFeedbackCovariance.agda`
- `agda/negative/FeedbackBadEdgeTransport.agda`
- `checkers/check_retained_feedback_covariance.py`
- `results/retained-feedback-covariance.json`
- `results/retained-feedback-covariance-positive.log`
- `results/retained-feedback-covariance-negative.log`

Source hashes remain stable across verification. Only Strominger-owned
source/report/checker files were edited; dependency interfaces may be refreshed
by checking. No physical time, execution policy, graph publication, commit or
push is claimed.
