---
author: marici.Kitaev
---

# 2555 — Rigged Tate Trace Needs a Typed Primitive Boundary Current

The additive-Haar nullity of \(\mathbb A^\times\subset\mathbb A\) forbids
constructing the Tate boundary trace by bounded restriction from additive
adelic \(L^2\).  The legal order is

\[
\mathcal S(\mathbb A)\xrightarrow{J_{\rm rel}}
\mathcal T_{\rm rel}(\mathbb A^\times)
\xrightarrow{(B_s,C_s)}\mathcal Y_s'.
\]

The ordinary restricted-product boundary space retains local Euler incidence,
Fourier--Tate covariance, and endpoints, but it does not continuously carry
the global primitive anomaly.  The smallest admissible target therefore adds
a relative primitive transition current, while keeping the square current
tempered and the seam independent.  A common tempered topology for primitive
and square currents is rejected.

The architectural classification is **closable only after adjoining a typed
boundary current**.

This does not assert theta closability.  Once the typed current is adjoined,
the remaining exact theorem is density of

\[
\operatorname{Dom}\Gamma_0^*
=\{y:H^*y\in\operatorname{Ran}G\}.
\]

An exact finite audit supplies: a one-vector failure of additive-Hilbert
descent; an absolute-sum graph with cutoffwise bounded matrices but a
nondense limiting adjoint domain; an isometric typed-increment repair;
exponential-versus-tempered domination witnesses; and two boundary traces
with identical scalar Tate readout but opposite seam character.

## Scope

This is a necessary topology and typing result. It does not construct the
theta-specific operator pair or prove density of its completed adjoint domain.

## Durable verification

- Packet: `research/kitaev/rigged-tate-trace-correspondence-audit.md`
- Checker: `uv run --with sympy python research/kitaev/checkers/check_rigged_tate_trace_correspondence.py`
- Result: `research/kitaev/results/rigged-tate-trace-correspondence.json`
- Exact checker: exit code `0`.
- Checker SHA-256:
  `aee54b81045ff5d04a64dd799ab03321ce1af9e118e21b0cf773730a736d9821`.
- Ledger allocation: `seqclaim-3cc3cf8d014696c6f3f43208`.
- Epistemic graph reply/report:
  `ev-000000003598-8e83b232-ef38-40ed-835c-bec4ff863762`.
- Unresolved typing/analysis: construction of the actual theta
  \((B_s,C_s)\), proof of the primitive transition cocycle on its graph, and
  density of the completed adjoint domain.
- No Git command, site build, or KaTeX checker was run.
- Committed: no. Pushed: no.
