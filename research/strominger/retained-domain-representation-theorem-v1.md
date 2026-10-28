# Common retained-domain representation argument

## Result and exact hypotheses

The three examples instantiate one construction, not three independent geometric mechanisms.

Let D be a declared domain packet, P a retained tower presentation, and let

    S : D -> P,   R : P -> D,   R(S(d)) = d.

The hypothesis is actual full-packet recovery, including the operations, connection/reference data and witnesses that the chosen domain requires. It is not recovery merely of its scalar readout. The finite family promotions used in the examples supply this interface on their labelled record domains; they do not establish it for arbitrary previously unspecified source syntax.

Choose three focus maps on P. `ThreeWitnessRetainedCone.Cone` constructs their retained typed tetrahedron. Each focused view is a dependent record `(p, selected value, selection equality)`, so it retains the whole p. The apex is that same whole, not a new physical degree of freedom.

Extract the face opposite the apex, retaining its first vertex's type certificate. Let E map P to that triangle record and D_T decode it. The existing focus recovery and the face extraction give

    D_T(E(p)) = p.

The type certificate is necessary: a bare unknown vertex type cannot provide a decoder into P. The supplied triangle record is not just its shape or a scalar projection.

## Consequences

The composite representation C=E S has decoder Q=R D_T, and

    Q(C(d)) = d.

Therefore any declared observation o:D->O satisfies

    (o Q)(C(d)) = o(d).

For a declared operation f:D->D define its represented operation by

    f_hat = C f Q.

Then

    f_hat(C(d)) = C(f(d)),
    g_hat(f_hat(c)) = (g f)_hat(c).

The second equality uses Q C=id on the intermediate domain value and holds for every well-typed represented-input record c. The identity law is asserted on encoded records: id_hat(C(d))=C(d). On arbitrary target records id_hat=C Q is normalization, not necessarily identity.

These equations apply to operations and readouts once their actual data belong to the declared domain interface. They do not independently derive a quantum law, anomaly matching, a connection, or the source origin of a supplied operation. The operations above are transported by decode/apply/encode; this is not automatically an independently native or local implementation.

Equality of encoded records reflects equality of original domain values by applying Q. Do not upgrade that statement to a claim that every arbitrary tetrahedral package is an encoded domain, or to an unrestricted higher-categorical full-faithfulness theorem. The target contains other packages and possible witness structure.

The same idea extends to typed operations between different admitted domains by their own encoders/decoders; actual domain and codomain interfaces must agree. No identification follows merely from equal dimensions or tetrahedral shape.

## Geometric representation

A canonical FCC tetrahedral cell supplies a chart for the four typed vertices and their incidences. Carrying all decorations makes this chart reversible. Composition and readout preservation come from retained data, not from the coordinates. A physical metric, lattice dynamics and an infinite FCC tiling are separate claims and are not prerequisites for the representation statement.

## How the examples instantiate it

- Markov oscillator: D retains the four coefficient records and regime; Q restores the bath contribution. Its readout is the sum of route products.
- Relational inflow: D retains the integer level, both orientation fields and matching conditions. Q preserves the mirror pair even when their currents agree.
- CP1 Berry connection: D retains frames, transition and connection functions, curvature and parameter conventions. Q preserves circle holonomy; the annular flat twist defeats a projector-only substitute.

All three use a full retained packet. In each hostile, a proposed smaller readout fails to factor a required observation. The common explanation is therefore retention of domain distinctions, not the number of physical ports or the cardinality of a sampled carrier.

## What remains of the governing conjecture

The representation construction is generic **conditional on a law-domain being admitted with full recovery at a tower stage**. It is already enough to explain the common mechanism in the examples. No more example enumeration is needed to establish these algebraic identities.

The still-open coverage premise is: for each known physical-law domain intended by the conjecture, its required typed structure is carried by an admitted WG-generated packet/tower stage. The constructor takes P and its focus maps as inputs; it does not prove this premise merely by accepting arbitrary supplied types. Nor may the target domain be defined as whatever the constructor happens to encode.

This is one remaining coverage premise, not a new chain of generic specification tasks. An existing source-admission/representation theorem with the required scope could discharge it; otherwise a source invariant excluding a required domain would refute the broad claim. The initial test branches remain completed at their stated scopes.

## Formal artifact and verification boundary

`research/nima/agda/RetainedDomainRepresentation.agda` extracts the opposite-apex face from the existing generic cone and proves full recovery, observation preservation, operation composition and the encoded-unit law, plus the independent tower-recovery interface. The identical original source is retained at `research/strominger/agda/RetainedDomainRepresentation.agda`.

**Fresh safe Cubical compilation passed**, including the imported cone/horn closure, with `--ignore-interfaces`. The operator explicitly directed use of Nima's folder and existing launcher after the direct executable invocation was refused. No launcher modification was needed:

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module RetainedDomainRepresentation -Fresh

Execution: `structured_command_execution:e_42200_1792521740088555100_46`, exit zero. Source/compiler/library inventories and stability checks: `research/nima/results/agda-RetainedDomainRepresentation.json`; log beside it. The net validator checks the receipt, source hash and equality of the two source copies. This verifies the stated generic conditional result, not the remaining physical-domain coverage premise.
