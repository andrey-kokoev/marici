# Composable scoped edits across changing membership

## Chosen rule

A structural transition from live ID set I to J records a partial injection
p:D->J, D subset I, identifying surviving members. For each target ID outside
p(D), it supplies an inserted value b_j. Endpoint changes that preserve leaf
identity act as identity on this scalar content transport; endpoint fields and
family grouping are still reconstructed separately by the record store.

This policy does not cover merge, split, averaging of identities or continuous
value evolution of survivors. Those need additional declared transport data.
It covers insertion, deletion, renaming and stable-ID endpoint moves.

The affine content map T and linear edit map P are

    T(x)_j = x_i if j=p(i), otherwise b_j,
    P(delta)_j = delta_i if j=p(i), otherwise 0.

Thus a new member is not silently included in an old edit. A deleted member's
live edit is dropped. Retained historical edits could be restored by a separate
explicit policy; this live-scope policy does not do so automatically.

## Laws and proofs

For successive transitions T1(x)=P1*x+b1 and T2(y)=P2*y+b2:

    T2(T1(x)) = P2*P1*x + P2*b1+b2,
    P_(T2 after T1) = P2*P1.

Survival in the composite means survival through both steps. Earlier inserted
members that survive are inserted members relative to the original domain.
Partial-injection composition and the displayed affine formula give identity
and associativity, including inserted-value provenance.

State/edit compatibility is exact:

    T(x+delta) = T(x)+P(delta).

It follows by distributing the linear part; inserted constants do not change.
This is the scoped naturality law that the unqualified enlarged-family mean
return failed. Edit transport is not authorization to execute the transported
edit against any later versioned state.

The Euclidean cost obeys

    ||P(delta)||^2 = ||delta||^2 - sum_(i not in D) delta_i^2.

Surviving components are neither duplicated nor merged. Insertion and renaming
preserve edit cost; deletion removes exactly the cost of deleted components.
Deletion is not an invertible or metric-preserving presentation change.

## Why richer edit records are required

A uniform shift delta on an old family becomes delta on its surviving original
members and zero on newly inserted members. It is generally nonuniform in the
new family. One new mean scalar cannot encode this edit. Its mean increment
must be accompanied by the residual edit, or represented directly by a retained
member-indexed vector. This gives a concrete compositional reason to keep
residuals in the return interface, not just in stored content.

## History is operationally relevant

Delete the only member and then restore its ID and original value. The final
content equals the original content, but the composite survivor relation is
empty. The old live edit transports to zero, unlike identity transport.

Inferring transport merely from equal initial/final ID sets would incorrectly
resurrect the edit. Retained transition provenance therefore affects future edit
meaning, not only auditing. This is still noninvertible deletion/restoration,
not evidence of holonomy of an invertible connection.

## Verification and scope

    python research/nima/checkers/check_scoped_edit_transport.py

Exact Fraction checks cover3087 triple-composition/vector cases over all seven
partial injections on a two-ID set (with a fixed inserted-value fixture), plus
identity, affine naturality, deleted-cost equality, changing cardinalities,
nonuniform promoted edits, restoration, and invalid-boundary/provenance controls.
General formulas have the algebraic proofs above; the finite enumeration is
regression evidence, not a dependent-type machine proof.

The pure transport checker is now connected to the Store's member-vector
interface for stable-ID insertion/deletion and endpoint movement; see
[versioned scoped vector return](versioned-scoped-vector-return.md). Explicit
rebase approval issues fresh versions, commits validate the full vector before
mutation, and accepted transport provenance is retained. General ID renaming
remains pure-layer only. The integration does not silently revive stale family
requests or treat arbitrary vectors as fresh whole-family mean requests.
