# Versioned commits for transported member edits

## Integrated interface

The recursive Store now supports immutable member-vector requests in addition
to family-mean requests. A vector request records store identity, event cursor,
and (member ID, expected version, rational increment) entries. Omitted members
are outside its read/write scope. Thus a newly inserted member is not implicitly
edited, and insertion outside the explicit scope need not invalidate the request.
This differs intentionally from a snapshot of the entire current family mean.

A vector commit checks local store identity, cursor bounds, distinct member IDs,
all live versions and numeric conversion before changing any member. Accepted
vectors enter the same old/new event history and recursive rebuild path as mean
edits. The accepted immutable request is retained by event index, including its
transport provenance. LIFO compensation restores payloads with fresh versions
without erasing that request or its event.

## Explicit rebase

Rebase requires an explicit approved=True argument. This is a trusted local
policy switch, NOT authentication, a capability, or a claim of external authority.
The prototype accepts programmatically constructed requests from trusted callers;
it is not an adversarial network boundary.

Rebase scans actual retained events since the request cursor. Deleting a scoped
member removes that member from the transported vector. Later restoration does
not resurrect it. Surviving members retain their increments; inserted members
receive no entry (equivalently zero increment). Endpoint moves preserve stable
member scope. The request then receives fresh leaf versions and a new cursor.
Its parent request and intervening event indices are retained.

A freshly approved rebase is not a reservation: any subsequent conflicting leaf
write makes the new request stale again. Approval to rebase is kept separate
from both semantic transport and the atomic validation at commit.

## Composition and reconstruction

Sequential approved rebases and a direct approved rebase produce the same
surviving entries and current versions for the tested event path. Their parent
chains differ, correctly preserving the different approval histories. Transport
through actual insertion events agrees with the pure partial-injection checker.

The integrated path is now:

    original scoped vector -> event-derived transport -> explicit fresh snapshot
    -> validate -> leaf batch -> recursive means/endpoints/versions -> audit event.

Nonuniform transported vectors therefore no longer have to be misrepresented
as fresh whole-family mean shifts. The mean/residual representation can be
recovered from the changed leaf values without dropping edit scope.

## Verification

    python research/nima/checkers/check_versioned_scoped_vector_return.py
    python research/nima/checkers/check_recursive_history_coherence.py
    python research/nima/checkers/check_dependent_mean_return_laws.py

Checks cover preserved inserted values, equality to pure insertion transport,
full-store nonmutation on unapproved rebases and stale/foreign commits, an
intervening write after approval, vector compensation, deletion/restoration,
composed rebases and retained provenance. Existing100-operation recursive,
16-event history replay,1701 content-law and81 insertion regressions also pass.
The imported pure transport checker reruns3087 composition cases.

## Limits and next structural question

Execution is serialized and trusted. There is no authentication, concurrent
locking, crash-safe persistence, or durable serialization of vector provenance.
The empty vector is accepted as an audit event with no leaf writes, consistent
with the existing zero-edit audit policy. The Store does not implement identity
renaming: its integrated survivor relation is stable-ID inclusion. General
partial-injection renaming is tested only in the pure semantic layer.

The next structural question is whether this richer edit interface remains
coherent under alternative promotion endpoint policies. The current footprint
policy is one chosen construction, not a derivation of the nine-rung tower.
