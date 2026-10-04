# Layer 1: typed witness-producing generators

## Status and foundation

This is the first Marici interface over the adopted dependent type-theoretic foundation. It records the generator formulation developed with the operator. The subsequent `agda/TypedGeneratorLayers.agda` formalizes the Layer 1 record, retained Layer 2 histories, naturality, and generated path coherence through a tetrahedron. See [Layer 2](typed-generator-layer-2.md) for the checked scope and receipts.

The foundation supplies universes, dependent pairs, dependent functions, paths, transport, and their computation and coherence rules. Function extensionality is used when comparing generator functions. Univalence is an additional assumption where equivalences are represented by paths between types.

Active SCC obligations: forward realization and route/coherencer compatibility. The path specialization uses the adopted path machinery. Each other witness relation carries its own composition and coherence obligations.

## State

Let S be a declared type of complete states. A state may contain typed data, source syntax, labels, boundaries, histories, and earlier witnesses. Dependencies between fields are retained in the definition of S. An ordered dependent context is one possible representation.

The state type specifies which data are present. A witness relation specifies what a permitted transition means.

## General generator

Supply a family

\[
R:S\to S\to\mathsf{Type}.
\]

For states s and t, the type R(s,t) expresses the required relationship between them. A generator has type

\[
G_R:\prod_{s:S}\sum_{t:S}R(s,t).
\]

For each input it returns a successor state together with a witness of the specified relationship.

This signature requires a result for every admitted input. An operation with restricted applicability must expose its admissibility evidence in the input type. Formation of the result type alone supplies no generator term.

## Family formation versus witnessed execution

The bare WG type specifies a total witnessed transition, but does not make its application a derivation in a particular rule system. For a domain presentation $D$ with admitted inputs $I_D$ and dependent result types $B_D(i)$, a family presentation may retain

\[
P_D=\prod_{i:I_D}B_D(i)
\]

and the full component packages. A *derivation* of this Pi family by the existing native `P-kind` rule requires derivations of **every** component, not only a package containing the whole family. Selection of a stored value, recovery of a certified component premise, and computation of a new certified result from an opaque function plus input are different operations.

For domain-specific constructor generation the execution principle must be explicit: from a derivation of a function package $f:\prod_i B_D(i)$ and a derivation of an admitted input $i:I_D$, derive a result package carrying $f(i):B_D(i)$, both operands, and its beta/coherence witness. The tested implementation is the *separately added* `NativeApplicationExtension.Application` rule; the original twelve-rule closure is not asserted to derive this endpoint. Encoding a WG as a native P-family (even with all values retained) does not confer derivations of its components. See [native specialization audit](meta-witness-native-bridge.md), [old-rule obstruction](adapters/native-application/README.md), and [application extension](adapters/application-extension/README.md).

This is an execution and provenance layer **in addition to** $G_R$; it does not change the meaning of Witness Generator or assert that every domain law is discovered from types alone.

## Path-producing specialization

Choose paths within S as the witness family. The generator then has type

\[
G:\prod_{s:S}\sum_{t:S}\mathsf{Path}_S(s,t).
\]

Its two components have types

\[
g:S\to S,
\qquad
h:\prod_{s:S}\mathsf{Path}_S(s,g(s)).
\]

Thus h is a homotopy from the identity function to g. The successor remains in the input's path component.

Iterating g constructs successive states. Applying h to those states constructs the transition paths. Path composition supplies edges between nonadjacent states.

This specialization describes path-connected transitions. An update that changes a discrete history length, for example, requires an appropriate general relation unless the declared state type already provides a path between those states.

## Generated triangle and tetrahedron

Take four successive state occurrences A, B, C and D, with generated paths p, q and r.

| Boundary item | Construction |
|---|---|
| A to B, B to C, C to D | The three generated paths |
| A to C | Compose p and q |
| B to D | Compose q and r |
| A to D | Compose the A-to-C path with r |
| Faces ABC, BCD and ACD | Compare the corresponding composites with the constructed edges |
| Face ABD | Use the associativity comparison between the two groupings |
| Tetrahedral filler | Compare the two compatible face pastings |

These choices admit a coherent construction by path induction. The tetrahedral witness relates face pastings along their shared boundary. Its existence does not require D to be the initial state.

Arbitrary independently chosen face witnesses introduce another filler problem. The assertion here concerns the faces generated by the coherent construction just specified.

## Comparisons pass through the generator

Given a path from a to b, applying g gives a path from g(a) to g(b). Together with h at a and b, these form a square.

One route first follows the supplied path and then the generated transition. The other first follows the generated transition and then the image path. Naturality of the dependent witness h compares these routes.

Applying the path operations at higher levels gives coherent comparisons of these comparisons. Their source is the adopted type theory and the typed generator term.

## Certification

For a fixed input, the result type is

\[
\sum_{t:S}R(s,t).
\]

A further certificate may establish its contractibility. The general generator signature requires an inhabitant; contractibility is a stronger, separately stated property.

For the path specialization, this unrestricted endpoint-and-path type is contractible. Path induction supplies a center at the input with its reflexive path and a contraction to each endpoint-and-path pair. Consequently the complete path-generator type is also contractible under function extensionality.

The endpoint varies in this statement. With both endpoints fixed, the path type can retain nontrivial loops and higher comparisons. Fixing an entire successor function likewise gives a different witness type from allowing the successor function to vary.

For any certified result type T, a witness of its contractibility supplies a witness that its contractibility-witness type is contractible. This is the higher certification form discussed with the operator. It adds no independent condition after the first certificate.

## Connection to the transport experiment

`agda/DependentTransportMachine.agda` checks a companion fragment with explicit route syntax and actual transport in the supplied circle double cover.

Its execution record retains the source program, output, and semantic correctness witness. The output-and-correctness type is contractible for each fixed program. The source syntax remains retained separately.

In the geometric interpretation, the circle point and fiber value together form a dependent pair. One turn connects different Boolean values over the same base point through a path of those total states. A Boolean fiber considered alone has no path from true to false.

The execution record itself certifies semantic correctness through a general witness relation. Its construction is not asserted to be a path between raw program records.

## Open content

To instantiate this interface for a Marici operation, specify S, R, the generator term, and any required composition or certification structure. The interface does not select a NAND expression, a geometric model, or physical dynamics.

Retained finite histories and generated tetrahedral completion are now checked in [Layer 2](typed-generator-layer-2.md). Integration of the transport fragment with dependent contexts and an explicit all-dimensional simplicial interface remain open.

## Related sources

- `dependent-transport-machine.md`
- `two-sided-transport-foundation.md`
- `universal-substitution.md`
- `research/voevodsky/resolution-net-v1/dependent-machine.md`
- `research/voevodsky/resolution-net-v1/dependent-interface-foundation.md`
