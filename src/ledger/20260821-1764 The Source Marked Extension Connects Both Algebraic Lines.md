---
title: "The Source Marked Extension Connects Both Algebraic Lines"
entry: 1764
date: 2026-08-21
status: established-generic-support
---

# 1764 — The Source Marked Extension Connects Both Algebraic Lines

## Question

Entry 1763 found that the exact flat marked-extension candidate has complete
support between the three marked quotient generators and the two split
algebraic lines.  Is that support forced by the frozen source reduction, or
could it be an artifact of the uncertified rational reconstruction?

## Frozen projection

Entries 853 and 857 establish that the final coordinates

\[
(e_6,e_7,e_8,e_9)
\]

are fixed across the complete primitive exact-lift nullspace.  Entry 867
splits their algebraic kernel with frame

\[
k_0=(1,0,0,0),
\qquad
k_1=(0,\alpha,\beta,\gamma)
\]

and gauge

\[
h=\frac{u(u+v)(u+v-4)P_6}{4}.
\]

For a fixed source column (b), the two split coordinates are therefore

\[
c_1=\frac{b_1}{\alpha},
\qquad
c_0=b_0-hc_1.
\]

## Falsifier

Run the complete 132-equation reduction at five generic points, for all three
marked generators and both base derivatives.  Reject any specialization whose
rank or fixed-coordinate mask differs from

\[
(117,3847).
\]

Then test both:

1. exact membership in the algebraic plane;
2. nonvanishing of each split coordinate.

Repeat over two independent large primes.

## Result

All sixty accepted columns satisfy

\[
b_2=\beta c_1,
\qquad
b_3=\gamma c_1
\]

exactly.  For each prime, both split coordinates are nonzero in all thirty
labelled columns:

\[
(\#c_0\ne0,\#c_1\ne0)=(30,30).
\]

Hence no one of the twelve source-labelled projection functions vanishes
identically in characteristic zero.  In either derivative direction, the
generic support graph is source-derived:

\[
\boxed{G_{\rm src}=K_{3,2}.}
\]

## Consequence

The no-relative-sign conclusion of Entry 1763 no longer depends on the
uncertified rational candidate.  A diagonal involution preserving all six
source couplings must assign the same sign to both algebraic lines.  Therefore
the relative (Z) required by Entry 1761's antiunitary deletion is absent from
the frozen generic marked source extension.

The surviving statement is narrow:

\[
\boxed{
\text{the pure Legendre block's companion-deletion real structure does not
extend through the generic marked source block.}
}
\]

This does not exclude a support-localized real structure on a proper existing
carrier stratum, nor does it prove any new carrier component.

## Durable artifacts

- checker: `research/benincasa/marici-gm/src/bin/marked_extension_algebraic_line_support.rs`;
- convention packet: `research/benincasa/marked-extension-algebraic-line-support.md`;
- prime-one result: `research/benincasa/results/marked-extension-algebraic-line-support-p1.json`;
- prime-two result: `research/benincasa/results/marked-extension-algebraic-line-support-p2.json`;
- allocator claim: `seqclaim-b4075c9fad8d55050f19a60a`.

