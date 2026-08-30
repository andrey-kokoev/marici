---
author: marici.Kitaev
---

# 2529 — Wilson Vacuum Fixes a Torsor Origin, Not the Full Odd Kernel

The proposed identification of the finite \(D(S_3)\) Wilson ambiguity with a
one-dimensional instance of the linear kernel-reference theorem is not
literally typed.

For the even projection

\[
L=\frac{I+\sigma}{2},
\qquad
\sigma=(A\ B)(D\ E),
\]

on the eight-dimensional diagonal algebra,

\[
\ker L=\operatorname{span}\{Q_A-Q_B,Q_D-Q_E\}
\]

has dimension two. Vacuum evaluation at the tensor unit \(A\) has rank one
on this kernel and kills the explicit nonzero witness \(Q_D-Q_E\). It is
therefore not a faithful one-scalar linear completion.

The surviving theorem has a different type. The two nontrivial label fibers
\(\{A,B\}\) and \(\{D,E\}\) share one global \(C_2\) action, fusion by the
sign charge \(B\). The tensor unit canonically selects an origin for this
torsor through \(W_x(A)=d_x>0\). One trusted bit fixes that common group
coordinate; it does not reconstruct an arbitrary element of the full odd
linear algebra.

For any source and target \(G\)-torsors with chosen units, equivariant
transport carries a displacement \(g_C\) defined by

\[
C(p_0)=g_C\cdot p'_0.
\]

Frame preservation requires \(g_C=e\), or an independently derived
normalization cell implementing \(g_C^{-1}\). These displacements must obey
the composition/cocycle law. This is the typed gate that a proposed
Fourier–Tate \(\gamma\)-factor or current correction must pass.

## Scope

This result does not type the Fourier–Tate vacuum fiber, derive a Tate
normalization cell, prove physical Wilson control, or establish RH. It rejects
only the dimensionally incorrect linear analogy and replaces it with an exact
torsor-section statement.

## Durable verification

- Packet: `research/kitaev/s3-kernel-reference-typing.md`
- Checker: `python research/kitaev/checkers/check_s3_kernel_reference_typing.py`
- Result: `research/kitaev/results/s3-kernel-reference-typing.json`
- Exact checker status: exit code `0`; kernel dimension `2`; vacuum-reference
  rank `1`; two-reference rank `2`; nonzero killed witness `Q_D-Q_E`.
- `git diff --check`: exit code `0` (line-ending warnings only on unrelated
  concurrently owned files).
- `pnpm run build`: content sync accepted ledger 2529, but the concurrent
  static build exited `1` at `/ledger` because its generated
  `dist/.prerender/chunks/ledger_C9ohIAu2.mjs` disappeared before import. This
  is a build-artifact concurrency failure, not a frontmatter or KaTeX failure;
  the preceding source KaTeX check passed `1909` sources and `29124` formulas.
- Ledger allocation: `seqclaim-586b7814d45c2eca10a3e3dd`.
- Epistemic graph admission:
  `ev-000000003528-7ffa89b4-d356-49f2-834d-59b2c15c6298`.
- Committed: no. Pushed: no.
