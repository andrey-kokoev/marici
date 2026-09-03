# Normal-bundle monodromy audit

## Question

How do transition functions act on `Gamma`, `Xi_log`, and the tame decoration?

## Claim boundary

Write local transitions as `l_i'=a_i l_{pi(i)}`. A permutation changes the star and flag orientations by `sign(pi)`. If the three walls are globally labeled, this monodromy is absent; otherwise the primitive class lies in the corresponding sign local system.

For fixed labels,

`u'=(a1/a3)u`, `v'=(a2/a3)v`.

With `alpha=dlog(a1/a3)` and `beta=dlog(a2/a3)`,

`Xi_log'-Xi_log=dlog(u) wedge beta + alpha wedge dlog(v) + alpha wedge beta`.

These mixed and horizontal terms vanish in relative de Rham forms along the normal fibers. Thus the vertical class and geometric `HomotopyLift` descend for a labeled transverse triple. An absolute form requires these terms to vanish or be canceled by a connection and Cech homotopy.

The tame units acquire factors `a3/a2`, `a1/a3`, and `a2/a1`. Their product is one and their vertical valuations vanish, so relative integral residues descend; horizontal regulator terms remain.

## Disposition

Monodromy does not obstruct the relative vertical horn with global wall labels. Absolute carrier promotion remains conditional. The next leaf determines whether the p-normal scientific target is intrinsically relative or requires an absolute logarithmic form.

## Verification

- `research/voevodsky/check_cosmology_normal_bundle_monodromy_audit.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
