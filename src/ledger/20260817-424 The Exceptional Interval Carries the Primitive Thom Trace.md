---
id: 424
date: 2026-08-17
title: The Exceptional Interval Carries the Primitive Thom Trace
---

# The Exceptional Interval Carries the Primitive Thom Trace

Entry 423 constructed the marked normalized blowdown as a ringed finite-space
morphism. Its relative dualizing datum is now explicit. Over a singleton fiber
the trace is the degree-zero identity. Over the unique nontrivial fiber, remove
the two marked endpoints from the V-tree and orient both edges away from the
central vertex. The relative cellular complex is
\[
C_1=\mathbb Z\langle e_D,e_1\rangle
 \xrightarrow{(-1\;-1)}
C_0=\mathbb Z\langle h\rangle .
\]
Consequently
\[
H_1(C_*(V,\partial V))=\mathbb Z\langle [I]\rangle,
\qquad H_0(C_*(V,\partial V))=0,
\qquad [I]=e_1-e_D.
\]
The coefficients of \([I]\) are coprime, so this is an integral primitive
orientation class. This degree-one class is precisely the Tor-one suspension
isolated in Entry 399; it is not higher homology of the absolute fiber, which
remains contractible.

Define the exceptional relative dualizing object by
\[
\omega_\pi|_V=\operatorname{Hom}_{\mathbb Z}
  (C_*(V,\partial V),\mathbb Z)[1]
\]
and use the orientation pairing
\[
\operatorname{tr}_V([I])=+1.
\]
A collar chooses an integral chain representative of this derived map. The two
collar choices differ by relative chain homotopy, so the derived trace is
canonical after fixing the endpoint ordering \(D03<x_1\). Reflection exchanges
the endpoints and sends \([I]\mapsto-[I]\); the orientation line also changes
sign. Their product is invariant, agreeing with the odd counit convention.

Because Entry 423 gives the source the pulled-back structure sheaf, every stalk
ring map is the identity on a localization \(A\). Tensoring the displayed
relative complex with \(A\) therefore preserves its unit boundary and gives
\[
\operatorname{tr}_V(a[I])=a.
\]
Thus the trace obeys the projection formula on every marked stalk. On singleton
fibers it glues to the identity trace, while the endpoint matrix fixes the
exceptional overlap. Rotation supplies the other two road centers, and the
Čech compatibility already proved in Entry 419 makes the three local traces a
single global derived trace
\[
R\pi_!\omega_\pi\longrightarrow\mathcal O_{\rm PC}.
\]

Hence the finite ringed PC/Čech connector now has its projection, relative
dualizing object, and primitive Thom trace. The remaining boundary is no longer
finite six-operation data: it is the comparison between this pulled-back
finite-space sheaf and the raw algebraic log-DNC structure sheaf.

The executable audit is
`research/voevodsky/check_relative_dualizing_thom_trace.py`.
