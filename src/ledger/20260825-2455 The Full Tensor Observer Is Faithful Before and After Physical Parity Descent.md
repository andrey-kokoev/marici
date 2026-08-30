---
author: marici.Benincasa
date: 2026-08-25
---

# 2455 — The Full Tensor Observer Is Faithful Before and After Physical Parity Descent

## Question

Entry 2444 shows that the reflection-symmetric physical loop cycle kills the
helicity anti-trace.  Is this an unrecoverable observer class, or the kernel
of a canonical physical quotient?

Sequence claim: `seqclaim-e7015761afa9d6c814a16b7a`.

## Full labelled observer

The three-occurrence observer and two-helicity analyzer are

\[
Q=
\begin{pmatrix}
1&2&0\\
1&-1&-1\\
1&-1&1
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

Their tensor product acts on all six labelled helicity ports and satisfies

\[
\boxed{
\det(Q\otimes B)=(-6)^2(-2)^3=-288.
}
\]

Thus the complete coefficient-level polarization family is faithful.
Moreover it intertwines helicity exchange with the even/odd deck grading.

## Physical coinvariant quotient

The source loop cycle is invariant under reflection of the loop momentum
normal to the external triangle.  Therefore the physical coefficient domain
is the reflection coinvariant quotient, not the unreduced six-dimensional
helicity presentation.

For each occurrence, the physical trace is

\[
(h_+,h_-)\longmapsto h_++h_-.
\]

Its kernel is exactly the anti-invariant line ((1,-1)).  The even inclusion
and averaging retraction satisfy

\[
\frac12(1,1)inom11=1.
\]

Hence the quotient is canonically rank one per labelled occurrence.

The induced physical observer is

\[
\boxed{
Q_{\rm phys}=2Q,
\qquad
\det Q_{\rm phys}=-48.
}
\]

It has rank three.  No class survives in the kernel after physical parity
descent.

## Interpretation

The parity-odd Tate channel remains genuine coefficient data before pairing,
but it is not a physical period class of the reflection-symmetric cycle.
Splitting the real loop cycle into oriented half-cycles would add an
unsupported boundary at the reflection plane and is not an admitted repair.

Thus

\[
\boxed{
\text{coefficient helicity rank six}
\longrightarrow
\text{physical coinvariant rank three}
\longrightarrow
\text{faithful occurrence readout rank three}.
}
\]

## Classification

- full polarization observer kernel: zero;
- physical-cycle kernel before quotient: three labelled anti-invariant lines;
- physical coinvariant observer kernel: zero;
- omitted instrument port: none;
- new Carrier support: none.

## Durable evidence

- `research/benincasa/check_tensor_polarization_parity_observer.py`;
- `research/benincasa/tensor-polarization-parity-observer.json`;
- Entries 2289 and 2443--2445.

## Scope and next falsifier

This closes the finite polarization/occurrence diagram.  The remaining broad
goal is physical-period faithfulness of the rank-seven contact-normal source
module: reduce the moving-cycle covariant responses, including their marked
boundary terms, and compute the induced period-covector rank.  Algebraic
score invertibility alone is not enough for that claim.
