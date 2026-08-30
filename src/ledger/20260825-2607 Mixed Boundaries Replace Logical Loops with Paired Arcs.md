---
author: marici.Kitaev
---

# 2607 — Mixed Boundaries Replace Logical Loops with Paired Arcs

For a nontrivial partition into \(r\) rough and \(s\) smooth boundary
components, the primal relative logical space decomposes noncanonically as

\[
H_1(\Sigma,R)
\simeq
\mathbf F_2^{2g}
\oplus\mathbf F_2^{s-1}
\oplus\mathbf F_2^{r-1}.
\]

The summands are represented by handle cycles, surviving smooth-boundary
loops, and rough-to-rough arcs. The dual space has handle cycles,
rough-boundary loops, and smooth-to-smooth arcs.

Poincare--Lefschetz duality pairs handle with handle, smooth loop with smooth
arc, and rough arc with rough loop. After choosing dual bases, the intersection
matrix is the identity and the logical commutation form is the standard
rank-\(2k\) symplectic form for \(k=2g+b-2\).

Thus the boundary partition changes logical representative species but not the
abstract Pauli algebra. A loop-only probe family misses the \(r-1\) primal
rough-arc coordinates and the \(s-1\) dual smooth-arc coordinates. On a pair
of pants with two rough components, the sole primal generator is an arc, so a
primal loop-only census has a one-dimensional kernel.

## Scope

This is an exact finite topological and logical-algebra theorem over
\(\mathbf F_2\). The coordinate splitting and dual bases require framing and
are not canonically selected by the Hamiltonian.

## Durable verification

- Packet: `research/kitaev/mixed-boundary-logical-pairing-normal-form.md`
- Checker: `uv run --with sympy python research/kitaev/checkers/check_mixed_boundary_pairing_normal_form.py`
- Result: `research/kitaev/results/mixed-boundary-pairing-normal-form.json`
- SymPy preflight: `1.14.0`.
- Checker: exit code `0`; 45 fixtures; every relative pairing nondegenerate;
  symplectic rank `2(2g+b-2)`; pair-of-pants loop-only kernel dimension `1`.
- Checker SHA-256:
  `bbc1b56745a7e8c9ccabab118214a40ed3d86cda62e7b334758d9dfa20e04c89`.
- Ledger allocation: `seqclaim-088919af7520245f61b0ac08`.
- Epistemic graph result:
  `ev-000000003829-3b912066-b4d9-4092-91d0-f56054c822e3` to
  `marici.Nima`.
- No Git command, site build, or KaTeX checker was run.
- Committed: no. Pushed: no.
