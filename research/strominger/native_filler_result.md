# A native filler instance: image matching, uniqueness, and failure of cancellation

Date: 2026-10-28.

## Result and evidence

The requested filler-selection mechanism is already implemented for a restricted native Marici fragment. It is not yet bound to the supplied Su-32 window construction.

At repository revision `cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c`, the inspected files `GeneratedReaderClassification.agda`, `CanonicalComparisonSynthesis.agda`, and `SourceCertifiedPrograms.agda` respectively prove classification/uniqueness, compute a filler or a refusal, and certify generation without an arbitrary function/equivalence input constructor. This is recovered existing work, not a new claim of inventing that theorem.

The new calculation instantiates those rules on two attachment histories from the same actual seed. It finds a refused comparison before a common extension and a uniquely admitted comparison after that extension. This gives an explicit native example showing that comparison admission cannot in general be cancelled through a common attachment.

Executed here: a finite set-valued semantic replay, parsing the actual six edge constructors and source action from an upstream excerpt; exhaustive bijection checks on the tested carriers; all six vertex-simple attachment paths from A; the two competing same-endpoint pairs; the source's 50 mode/normal-form cases; continuation and noninjective-reader controls.

Not executed here: Agda, the original repository Node checkers, or any Su-32 port/release records. The new `NativeFirstFiller.agda` is an instantiation candidate, not a fresh typechecking receipt. Its general premises are supported by the inspected source. The repository report records an earlier Agda check; that report was read, not independently rerun. The accessible repository revision dates to October 20 and is not presumed to contain unpublished October 28 Su-32 code.

## 1. The actual local source and operations

The graph has vertices A,B,C,D and exactly these directed edge constructors:

    AB, BC, CA, BA, AD, DB.

Its two declared source modes are `stay` and `exchange`; exchange is `(A B)(C D)`. The present concrete example uses stay only. All four graph-retaining pointed seed packages are explicitly part of this source's seed policy. This policy is not being derived from an unpointed graph.

For an admitted package with active vertex v, the attachment request is

    Out(v) = Sigma(w : Vertex) Edge(v,w).

A selected outgoing edge determines the new selected value. The full interpreted attachment carrier is `Out(v)` together with a loop witness at the preceding package's selected value. The preceding package, its code, and its actual derivation remain in the retained structure.

In the classified generated fragment, induction proves that the current carriers are sets. Their based loop types are contractible. Thus the attachment carrier normalizes to `Out(v)`, not to a list of all past vertices and not to an arbitrary history-bearing state space. The reader returns the target vertex of the outgoing edge.

The source therefore has the following possible reader images:

    whole       {A,B,C,D}
    outgoing A  {B,D}
    outgoing B  {A,C}
    outgoing C  {A}
    outgoing D  {B}.

These are alternatives in the current value carrier, not a record of which vertices a history visited. There are no parallel edge constructors with the same source and target, so the outgoing reader is injective. `GeneratedReaderClassification` proves reader injectivity for every generated Fragment, including comparison nodes, rather than assuming it anew at every step.

## 2. Native filler theorem

Let u and v be actual generated operands, with interpreted carriers X_u and X_v, selected values x_u and x_v, and readers r_u and r_v. Fix the allowed mode m and require the selected active vertices to have the source/target typing prescribed by m.

The source's `Filler` is a pointed equivalence e:X_u ≃ X_v together with its whole-carrier reader law:

    e(x_u)=x_v,
    r_v(e(x))=m(r_u(x)) for every x.

Write S_u and S_v for the images of the readers. The source proves:

    Filler exists exactly when m(S_u)=S_v.
    If it exists, Filler is contractible.

Proof at set level: equality of images gives, for each x, an element y with reader m(r_u(x)). Reader injectivity makes that y unique, so define e(x)=y. The reverse image agreement constructs the inverse. The aligned selected values imply pointedness. Any second candidate must map each x to the same y and therefore has the same underlying equivalence. Because the involved carriers and port type are sets, the extra equality witnesses are proposition-valued. The existing Cubical proof gives `filler-prop` and then `filler-contractible`.

The compiler computes the normal forms, decides image membership using the actual Edge constructors at A,B,C,D, and either derives this equivalence or returns a separating vertex with an inhabited fiber on one side and an empty fiber on the other. No equivalence or image-agreement function is supplied to the compiler as an extra input.

On success, the existing `compareF` and native `compare-rule` consume the actual two operand derivations. `SourceCertifiedPrograms.compareP` permits only a guard for the computed success, not an arbitrary filler parameter. The instantiated operands below are generated from `seedP` and `attachP` alone, so there are no pre-imported equivalence parameters in their histories.

This theorem concerns a complete pointed, reader-preserving comparison between fixed operands. It does not make arbitrary `Resolve` proofs, source histories, or producer programs equal. It also does not assert a spatial CW disk or an identification with the dual-indexed 2-packet.

## 3. A refusal followed by a uniquely generated comparison

Begin with one seed program at A. Construct:

    a = A -> B,
    b = A -> D -> B.

Both select B. Their current reader images are respectively `{B,D}` and `{B}`. The compiler refuses their comparison in stay mode, with D as its separating vertex. This is not a missing search result: an equivalence respecting the complete reader law is impossible for these two operands.

Append the same admitted edge BC to both actual operands:

    u = A -> B -> C,
    v = A -> D -> B -> C.

Now both carriers normalize to `Out(B)` and both select the BC branch. Their reader images are `{A,C}`. The compiler therefore admits a unique complete filler. In the normalized carriers its map is

    BA branch -> BA branch,
    BC branch -> BC branch.

On the actual dependent carriers, this map is transported through their source-proved normalizing equivalences. It is not an assertion that the underlying raw types or histories are definitionally identical.

The comparison constructor keeps u and v as its two actual premises. A subsequent CA attachment is admitted at the resulting active C boundary. An attempted AB attachment at that boundary is rejected. The continuation is applied to the actual comparison package, not to a newly introduced seed at C.

The finite replay enumerates all six vertex-simple attachment paths beginning at A:

    empty, AB, ABC, AD, ADB, ADBC.

There are exactly two pairs of distinct paths with the same selected endpoint. The B pair is refused, and the C pair is accepted. This census is only for vertex-simple attachment paths from A in this graph and stay mode. It is not a global minimality theorem over arbitrary native programs.

The supplied Agda module instantiates the existing compiler on exactly these operands. It includes a refusal proof, a proposed reduction-based acceptance guard, `isContr` obtained from the existing theorem, the certified comparison, further CA continuation, and the existing scoped coherence/normalization producers. No new return rules rho2/rho3/Gamma are introduced.

## 4. Why the positive result must not be read as a spatial filling

For these actual objects,

    Fill(a,b) is empty,
    Fill(attach(a,BC),attach(b,BC)) is contractible.

Thus an accepted comparison after a common attachment does not imply an accepted comparison before it. This is a consequence of the actual all-outgoing attachment semantics: the current value carrier is determined by the active source vertex of the new attachment. The older packages remain retained in syntax, but the new current values do not range over all possible previous current values.

It would be invalid to interpret BC here as invertible right-whiskering on complete history paths and then cancel it from the newly generated comparison. Such cancellation would contradict the source's proven refusal at D. Record recovery and invertibility of a path transformation are different claims.

This example exhibits generated comparison admissibility under a native extension. It does not prove that the original graph triangle A-B-D bounds an admitted geometric disk, or that the native constructor is a fibration/homotopy-preserving extension of the whole prior state carrier.

## 5. Why uniqueness holds, and where it stops

Within this fragment the reader distinguishes every current value. Consequently there is no hidden current value that a port-preserving equivalence can permute without being detected.

This is substantive, not a consequence of endpoint equality. The unrestricted `prepared` Body constructor permits the same four-value Vertex carrier with constant reader A and selected value A. That exact kind of input is excluded from the classified Fragment. On this carrier there are six pointed, port-preserving automorphisms: any permutation of B,C,D fixes the selected value and the constant reader. The finite replay enumerates all six.

Therefore the general native comparison schema does not by itself imply uniqueness. The theorem applies because the specified source-generated fragment proves the stronger reader condition. Dropping that restriction invalidates a blanket uniqueness conclusion. Conversely, failure of injectivity does not by itself imply that every individual pointed comparison problem has multiple fillers; the example establishes the necessity of controlling reader fibers in a general theorem.

The example also explains why the earlier free rho2/rho3 presentation needed a further higher relation whereas this comparison fiber does not. They are different models. The present source already proves its relevant carriers set-valued and its readers injective. Those facts make this fixed filler type a proposition. They cannot be transferred to richer history/fiber spaces without proof.

## 6. Exact remaining Su-32 obligation

The supplied `su32-native-window-operation-v1.md` establishes integer-lifted ports and complete labelled-wire regrouping, and explicitly states that its operation introduces no comparison-packet constructor. It does not identify the Su-32 packet carriers with the generated-reader fragment above.

The reusable result is now an existing native compiler and a tested instance, not another request to invent a generic comparison rule. Applying it to Su-32 requires actual packet operands with their producer origins and a source-defined reader, followed by a proof that this reader carries the required information. Exact port identity `(p,a)` alone does not guarantee injectivity on payload or history-bearing values.

If Su-32's readers have nontrivial fibers, equality of their support sets is insufficient to apply this theorem: the full fiber comparison data must be retained and analyzed. No such analysis can be replaced by relabeling the six-arrow vertices A,B,C,D as P/N/E or by identifying the four period generators with these edge constructors.

No native Su-32 filler, geometric 2-packet, n-Segal structure, circle action, or Hopf fibration is certified by this instance.

## Reproduction

The finite replay needs Python 3.10 or later and the standard library:

    python check_native_fragment.py --output results.json

The Agda instantiation is currently uncompiled. To attempt a fresh check against the inspected checkout and its Cubical 0.9 dependency:

    python verify_agda.py --repo /path/to/marici --cubical /path/to/cubical-0.9

The runner checks the repository revision unless explicitly overridden, uses the four include roots from the source checker, disables implicit libraries, requests a fresh safe Cubical/guarded check, and records the command, exit, log, and source hashes. It performs no network access or installation. Agda may refresh its interface caches; no source file is intentionally modified.

## Source map

`source-map.json` records the exact inspected source files and full upstream blob hashes. Only a labelled graph excerpt is copied into this bundle; a full upstream blob hash must not be confused with a hash of that excerpt.

The decisive existing declarations are:

- `GeneratedReaderClassification.normal`, `reader-embedding`, `Comparisons.classification`, `filler-prop`, `filler-contractible`, `admitted`, and `native-coherence`.
- `CanonicalComparisonSynthesis.Compile.compile`, `refutes`, `decision`, `next`, `admitted`, and `run`.
- `SourceCertifiedPrograms.Program`, `Pair.build`, `Higher`, and `derive`.
- `InternalSourceComparisons.package`, `reader`, and `derivation`.

The relevant general Cubical-library lemma is `injective→hasPropFibers` in `Cubical.Functions.Embedding`: injection into a set gives proposition-valued fibers. This library fact was also checked against the published library source. The native theorem remains scoped to its pinned implementation and assumptions.
