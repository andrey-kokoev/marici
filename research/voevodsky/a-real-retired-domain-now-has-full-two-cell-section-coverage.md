# A real retired domain now has full two-cell section coverage

## Delivered coverage gate

The owning forced-zero-tail migration now has a full-domain section attachment, not merely a declared subdomain. Its retired state has m=3, no surviving audits, and public frames

    -U+128V<=127, U-V<=0.

The original source has V<=U because all atom slopes are at most one, and U>=0. Together these imply U=V and 0<=U<=1. Conversely every (u,u), 0<=u<=1, has the old-compatible source lift (u,0,0). Thus the complete retired public domain is exactly that segment.

The implementation does not trust this prose or a producer coverage flag. It constructs four target halfspaces for the declared segment: the two parameter bounds and both signs of its affine-hull equation. Each must have a nonnegative rational combination of the EXPECTED runtime source/evidence rows with exactly matching normal and a sufficient upper bound. Source rows are reconstructed from the verifier's source model, not supplied as candidate authority.

## Two-cell section

The declared public vertices are (0,0), (1/2,1/2), (1,1), with source lifts (0,0,0), (1/2,0,0), (1,0,0). Each source lift is checked against the same verified migration's fine context. Ordered knots cover the segment without gaps. Adjacent cells share one source-lift array entry, so interpolation agrees at their common endpoint.

Attachment therefore proves both inclusions: runtime domain lies in the segment by Farkas implications; the segment lies in the runtime domain by endpoint admission and convexity. A fresh handle is published only after all checks pass.

## Restriction and reuse

The service locates a requested point in its interval cell and interpolates. After appending U<=3/4 it still covers the ENTIRE current domain by restriction. A lift at (3/4,3/4) succeeds without rechecking source vertices; the now-excluded endpoint (1,1) is refused. Current source/runtime/public inequalities are evaluated before answering. The service does not call a solver to locate the segment cell.

Coverage and vertex proofs are retained as immutable serialized context. Public-only transitions cannot widen the domain or change the fine source, so reuse is justified by session-owned transition authority. Arbitrary domain widening is not supported.

## Checks and limits

The workload passes three source vertex checks, four coverage implications and a two-cell cover. Nine refusals include missing implication, negative weight, altered source lift, mismatched knots, foreign migration, off-line point, excluded endpoint, stale handle and archive escalation. Full attachment replay outside the session uses the same verification kernel; it is not a separately implemented verifier.

This closes the full-domain coverage gap for a REAL RANK-ONE migration. It does not claim a general higher-dimensional triangulation checker. In particular, all cells are ordered intervals in one shared affine line; higher-dimensional overlap, boundary coverage and face incidence remain outside this adapter. The segment helper supports affine coordinates but has only been exercised on this owning two-public-coordinate case.

Section encoding is charged separately in receipts. Encodings are not a complete heap/storage ledger. The service remains a trusted in-process prototype and does not grant archival re-exposure merely because it can return a valid section point.

## Reproduction

    uv run --with sympy python research/voevodsky/checkers/check_full_segment_checkpoint.py

Implementation: `checkers/full_segment_checkpoint.py`.

Artifact: `results/full-segment-checkpoint.json`.
