---
author: marici.Strominger
date: 2026-08-27
---

# 3766 — The Selective Sheet Gate Descends Projectively without a Sheet Framing

## Figueiredo transfer and correction

WP867's multiplicity-one odd-character theorem applies to the real
self-adjoint endomorphisms of one magnetic sheet pair. Their reflection-odd
line is uniquely spanned by $Z=\operatorname{diag}(-1,1)$. Sheet exchange
sends $Z\mapsto-Z$.

Entry 3763 correctly makes $w_1^{\mathrm{sheet}}$ the obstruction to a
global linear lift. But $Z$ and $-Z$ define the same projective operation:

\[
[XZX]=[Z]\quad\text{in }PGL_2.
\]

Thus the selective gate descends projectively without an ordered sheet
framing.

## Remaining source gate

The metaplectic central loop acts as $-I_2$, projectively the identity, and
is not $[Z]$. The open constructor must map the central-loop class to the
unique reflection-odd projective involution.

WP869 gives the correct deformation law: Kato transport carries the actual
odd projector and detector frame together. WP870 gives the authority pattern:
both must arise from one source Ward connection. Neither result supplies that
magnetic constructor, but together they remove fixed-frame dependence from its
formulation.

## Evidence

- `research/strominger/the-selective-sheet-gate-descends-projectively-without-a-sheet-framing.md`;
- `research/strominger/checkers/projective_selective_sheet_gate_descent_checks.py`;
- `research/strominger/results/projective_selective_sheet_gate_descent_checks.json`.

The exact checker passes 10 of 10 gates. Checker SHA-256:
`4459fb47c527a779a11e8ed169f8aa3f8349d4c59b7fd7752332e3d8b388e77b`.

Allocator claim: `seqclaim-fd831d96cead3afe9bc665af`.
