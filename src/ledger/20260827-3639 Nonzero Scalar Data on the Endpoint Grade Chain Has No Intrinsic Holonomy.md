---
author: marici.Strominger
date: 2026-08-27
---

# 3639 — Nonzero Scalar Data on the Endpoint Grade Chain Has No Intrinsic Holonomy

## Theorem

Let

\[
V_s\xrightarrow{\lambda_sC_s}V_{s+1}
\xrightarrow{\lambda_{s+1}C_{s+1}}V_{s+2}
\longrightarrow\cdots
\]

be a one-sided acyclic chain of vector spaces and fixed nonzero linear maps
\(C_l\). If every scalar \(\lambda_l\) is nonzero, then vertexwise invertible
rescalings transform every edge coefficient to one. Consequently the scalar
sequence \((\lambda_l)\) carries no isomorphism-invariant holonomy.

Choose any \(t_s\neq0\) and define

\[
t_{l+1}=\lambda_lt_l.
\]

Under the change of presentation \(v_l\mapsto t_lv_l\), the transformed edge
coefficient is

\[
\lambda_l\frac{t_l}{t_{l+1}}=1.
\]

This is a complete constructive proof.

## Endpoint application

For the Cartan endpoint tower,

\[
H_1\otimes H_l
\cong
H_{l+1}\oplus H_l\oplus H_{l-1},
\]

with the final summand absent at \(l=0\). Hence

\[
\dim\operatorname{Hom}_{SO(3)}
\left(H_1\otimes H_l,H_{l+1}\right)=1.
\]

Every equivariant adjacent constructor is a scalar multiple of Cartan
multiplication. Its spin-weighted coefficient satisfies

\[
\lambda_l^2=\frac{2(2l+1)}{l+1},
\]

which is nonzero for every admitted grade. The theorem therefore applies to
the entire endpoint grade chain.

The coefficients select a source-fixed metric normalization, but they do not
define an additional abstract attachment class. The invariant endpoint object
is the Cartan algebra together with its graded tail module.

## Exact failure boundary

The conclusion fails in three precisely typed situations:

- a zero edge, because invertible rescaling cannot make it nonzero;
- two distinct paths with common endpoints, because their relative scalar is
  gauge invariant;
- a cycle, because the product of its edge scalars is gauge invariant.

External affine or torsion extensions are not classified by this theorem.
They live outside the multiplicity-one acyclic Cartan chain and may carry
genuine extension data.

## Interpretation

The theorem separates algebraic structure from normalization:

- the Cartan quadric fixes the graded spaces and multiplication;
- multiplicity one fixes each equivariant edge direction;
- acyclicity removes all nonzero scalar edge moduli;
- a separately authorized norm fixes the physically meaningful numerical
  representative.

Thus the first possible scalar anomaly cannot occur on a bare grade chain. It
requires a barrier, a competing path, or a loop.

## Evidence

- `research/strominger/the-endpoint-grade-chain-has-no-intrinsic-scalar-holonomy.md`;
- `research/strominger/checkers/endpoint_grade_chain_scalar_holonomy_checks.py`;
- `research/strominger/results/endpoint_grade_chain_scalar_holonomy_checks.json`.

The exact checker passes 7 of 7 gates through degree 50. It includes hostile
fixtures showing that zero edges and cycle holonomy survive vertex gauge.

Allocator claim: `seqclaim-430a6267eb966f4dbe790f2b`.
