# Persistent seam addresses do not determine their feedback law

## Result

**37 exact checks pass.** The primitive AB/BA addresses can be retained after
indirect-edge deletion, but their missing coefficient bindings must remain
explicitly unresolved. More importantly, a simple append-only repair cannot
produce joint feedback while preserving the old collective projector exactly.

This is an interface audit and completion obstruction, not a newly selected
source operation.

## Persistent records without invented responses

The checker rebuilds the original constructor for the baseline and each single
indirect-edge deletion. It records both surviving primitive seam addresses with
status `bound` or `unresolved`. A bound address names its actual generated raw
coefficient ports. An unresolved address has no coefficient binding.

`require_seam_bindings` rejects a joint query if either binding is unresolved.
No old slot is reused, no zero response is inserted and no replacement vector
is selected. The receipts retain the generated-manifest hash for each case.
This keeps the primitive input domain without claiming a coefficient operation
that the constructor did not supply.

## Exact obstruction to append-only collective coupling

The existing collective maps are freshly reconstructed from their coefficient
manifests and verified self-adjoint and idempotent. Suppose a proposed enlarged
collective map has block form

    P = [[N, B], [B*, D]],

where N is the unchanged old orthogonal projector. If P is also an orthogonal
projector, its old-block equation gives

    N^2 + B B* = N.

Since N^2=N, B B*=0 and hence **B=0**. Thus no added record can feed back into
the old carrier within this operation class while its entire old compression
remains exactly N. The argument applies to arbitrary added dimension and the
inherited positive metric after an isometric coordinate change.

This is stronger than merely observing that the constructor omitted a port. It
shows why preserving a completed old subsystem and appending an interacting
projector is incompatible with the proposed unchanged-block requirement.

## Controls separate retention, readout and joint regeneration

For the three-mode equal-mean projector N=J_3/3, the checker uses illustrative
completion controls, not adopted source dynamics:

- N direct-sum 0 and N direct-sum 1 both preserve the old projector, but give
  different orphan readings. Existing data do not select one.
- J_4/4 couples the extra mode and is a valid orthogonal projector, but changes
  the old self-response from 1/3 to 1/4. Joint closure changes the old block.
- A one-way receiver can read the old state without changing its block, but
  that enlarged map is not the same kind of self-adjoint collective projector.

The prior compiled three-arrow receiver belongs to the open-readout approach;
it does not claim reciprocal feedback. Its independently established character
mismatch must not be repaired by silently adding phases or feedback arrows.

## What the next construction would need to specify

There are now distinct legitimate branches, not interchangeable fixes:

1. **Retained unresolved interface:** preserve input occurrences, reject queries
   lacking a coefficient binding. Implemented by this audit.
2. **Open receiver:** supply actual extraction/readout maps, with no claim that
   the added record modifies old collective evolution.
3. **Joint regenerated closure:** specify how the primitive source, including
   incomplete paths, generates a new common carrier and collective map. Its old
   block is allowed to change and must be compared rather than assumed equal.
4. **Different operation class:** supply nonprojective dynamics, controls or
   explicit environment coupling rather than call it an old projector extension.

No source rule selecting branches 2–4 was introduced. The exact unresolved
question is how a surviving incomplete path participates in the new shared
response, not how to store its label or pad the old matrix.

## Reproduction

    uv run --with sympy python research/nima/checkers/check_open_seam_completion_boundary.py

Receipt: `results/open-seam-completion-boundary.json`.
It contains persistent primitive records, explicit missing bindings, source
hashes and completion controls. Owner source constructors remain unchanged.
