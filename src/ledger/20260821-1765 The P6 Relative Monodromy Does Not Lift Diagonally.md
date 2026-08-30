---
title: "The P6 Relative Monodromy Does Not Lift Diagonally"
entry: 1765
date: 2026-08-21
status: established
---

# 1765 — The (P_6) Relative Monodromy Does Not Lift Diagonally

## Question

Entry 1764 excludes the companion-deletion relative sign as a generic
diagonal symmetry of the marked extension.  Can the same sign nevertheless
arise canonically as monodromy on an existing carrier divisor?

## Source-derived boundary sign

Entry 867 gives the exact algebraic splitting

\[
\mathcal A_{--}
\simeq
\mathcal L_{P_6^{-1/2}}\oplus\mathcal L_{D_1}.
\]

At a generic point of (P_6=0), with (D_1\ne0), its residue vector is

\[
\left(-\frac12,0\right).
\]

Hence the local algebraic monodromy is

\[
\boxed{
M_{P_6}^{\rm alg}=\operatorname{diag}(-1,+1).
}
\]

The relative (Z) sign is therefore not invented: it is already present as
an intrinsic boundary monodromy of the algebraic coefficient submodule.

## Lift test

Entry 1764 proves that the generic marked source support graph is

\[
K_{3,2}.
\]

For a diagonal lift, each of the three marked generators would need a sign
equal to the sign on both incident algebraic lines.  Since those signs are
opposite, no assignment exists.  Exhausting all eight source-sign assignments
gives

\[
\boxed{\#\text{ diagonal lifts}=0.}
\]

## Narrow result

The companion-deletion sign has a canonical home on the existing (P_6)
boundary coefficient system, but it does not extend diagonally through the
generic marked rank-twelve extension.

This distinguishes two claims:

\[
\text{relative boundary monodromy exists}
\]

is established, while

\[
\text{relative monodromy is a symmetry of the complete marked object}
\]

is false for diagonal lifts.

The full marked local monodromy may instead be triangular and nonsplit.  Its
off-diagonal nearby-cycle extension is the next typed object; no new carrier
stratum is warranted.

## Durable artifacts

- checker: `research/benincasa/checkers/p6_relative_monodromy_lift.rs`;
- result: `research/benincasa/results/p6-relative-monodromy-lift.json`;
- convention note: `research/benincasa/p6-relative-monodromy-lift.md`;
- allocator claim: `seqclaim-eed8f3049d9a3a8c2032cdbf`.

