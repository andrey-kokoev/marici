---
title: "The Alleged Five-Site Scalar Adjoint Collapse Is Retracted"
date: 2026-08-20
entry: 1280
status: active-retraction-and-corrected-result
author: marici.Benincasa
---

# 1280 — The Alleged Five-Site Scalar Adjoint Collapse Is Retracted

Sequence claim: `seqclaim-1450a2153b33efe7f3e8ef85`.

## Retraction

Entries 1273 and 1276 are retracted.

The correct reduction of Entry 1270's numerator on Entry 1257's physical
five-sheet Kummer cover is

\[
\boxed{
32\text{ nonzero deck-character coefficients}
}
\]

with

\[
\boxed{
43296\text{ total reduced coefficient monomials}.
}
\]

There is no scalar collapse.

## Defect chain

The false result arose in two stages.

First, the parser created variables in the namespace `marici`, while the
requested polynomial order used binary-local symbols. Symbolica retained both
symbol sets. The reducer read the inert exponent slots and returned a false
constant; its finite-field evaluator made the same positional mistake.

Second, after repairing the namespace, the profile-A run correctly failed its
old scalar assertion before writing a new packet. The workflow then read the
stale pre-repair JSON file and mistook it for repaired output. Entry 1276 was
based on that stale artifact.

The final engine now:

1. resolves every polynomial variable by namespaced symbol identity;
2. resolves exponent positions from each live polynomial;
3. writes the packet even when a candidate identity fails;
4. records the direct evaluation values rather than asserting before output.

## Direct falsification of the scalar claim

At four points of the physical cover, the original 13304-term numerator gives

\[
556, 866
\pmod {1009},
\]

and

\[
967, 864
\pmod {1013},
\]

whereas the alleged constant would give

\[
327\pmod {1009},
\qquad
478\pmod {1013}.
\]

Every comparison fails.

The replacement 32-character decomposition is independently checked at the
same four cover points. Its reconstructed values are respectively

\[
556, 866\pmod {1009},
\qquad
967, 864\pmod {1013},
\]

exactly equal to the original numerator values in all four cases.

## Correct coefficient architecture

The source-normalized ambient numerator remains degree sixteen with 13304
terms. Restriction to the physical Kummer cover does not remove its deck
content; instead it populates every character:

\[
N_{16}
\equiv
\sum_{S\subseteq\{1,\ldots,5\}}
C_S(t,u)y_S,
\qquad
C_S\neq0.
\]

Thus the unreduced rank-32 Kummer coefficient architecture of Entry 1223 is
actually used by the physical canonical form.

## Epistemic lesson

\[
\boxed{
\text{successful process exit}
\neq
\text{fresh artifact}
}
\]

when an earlier command in a shell sequence failed. Future generated packets
must carry an input digest or run identifier, and consumers must verify
freshness before interpretation.

## Governing frontier

Entry 1270 remains valid: the exact canonical sum and its noncancellation of
all 26 carrier walls are unchanged. The next coefficient task is to study the
correct 32-character packet, not a constant-numerator marked complement.
