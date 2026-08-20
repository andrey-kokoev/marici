# Ledger numbering protocol

Numbered Marici ledger entries receive their identity from the directly bound
`marici-epistemic-graph` sequence allocator. Directory order, Git history, and
the largest visible filename are discovery aids only; none is numbering
authority.

## Creating an entry

1. Claim the next value from sequence `marici-ledger-entry` (sequence ID
   `seq-3475727b9d10d9e7689ae83e`) before choosing a filename or heading.
2. Supply the actor, an authority basis, and an intent-specific idempotency
   key. Reuse that same key when retrying the same claim.
3. Use the returned number exactly once in both the ledger filename and its
   level-one heading.
4. Treat every claim as permanent. An abandoned claim remains skipped; it is
   never released, reassigned, or reused.
5. Admit the completed entry to the epistemic graph with its actual source
   locator, then commit and push the coherent increment.

Never allocate by scanning the ledger, incrementing its apparent maximum,
copying a number from chat, or inferring a number from Git. A transported
number is not authority.

## Repairing a collision

Freeze allocation for the repair scope, then identify which entry has an
allocator-backed claim. That entry retains its number. For each unclaimed
legacy duplicate:

1. claim a fresh number with a unique repair-specific idempotency key;
2. move the file and update its heading to that claimed number;
3. preserve authorship, date, evidential content, and epistemic scope;
4. add a short repair note recording the old filename/heading and claim ID;
5. update only title-qualified or otherwise unambiguous references—expand
   ambiguous numeric ranges instead of applying a global replacement;
6. admit the new source locator and relate it to the historical source with a
   supersession/provenance edge; do not rewrite graph history;
7. verify claims, filename/heading agreement, duplicate counts, links, and the
   site build before committing.

Claimed repair numbers are also permanent if the repair is interrupted. Resume
with the original idempotency key rather than claiming replacements.

## Verification checklist

- Sequence status and claims agree with every new number.
- Each repaired filename number equals its level-one heading number.
- No repaired number has more than one live ledger file.
- No old duplicate filename remains.
- Reference edits are provenance-based, not blind numeric substitutions.
- Only repair-owned files are staged in a shared dirty worktree.
- Temporary reports, logs, and generated scratch artifacts are not committed.

This protocol applies to all team identities and all research sectors.
