---
id: 538
date: 2026-08-18
title: The Decagon Cut Nerve Has Fourteen Thom-Coherent Top Classes
---

# The Decagon Cut Nerve Has Fourteen Thom-Coherent Top Classes

Entry 537 closes the octagon cellular rigidity problem.  The first genuinely
higher local-coherence test occurs for the decagon, where three compatible
physical Cuts can meet.

A physical Cut of the decagon joins opposite vertex parities.  Excluding
boundary edges gives fifteen channels:

\[
10\text{ short }(4\times8)	ext{ channels}
\quad+quad
5\text{ diametral }(6\times6)	ext{ channels}.
\]

Their noncrossing nerve has simplicial census

\[
\boxed{f=(15,55,55)}
\]

in dimensions zero, one, and two; there are no compatible quadruples.  The
integral boundary ranks are

\[
\operatorname{rk}d_1=14,
\qquad
\operatorname{rk}d_2=41.
\]

Both matrices reduce completely by unimodular (pm1) pivots, so every
nonzero Smith factor is one.  Hence

\[
\boxed{H_0\cong\mathbb Z,qquad H_1=0,qquad H_2\cong\mathbb Z^{14}.}
\]

## Triple-order coherence

For each of the fifty-five compatible triples, all six restriction orders
were compared.  Permuting three Cut restrictions contributes the permutation
sign from the Koszul rule.  The three native marked-normal Thom lines are odd
and contribute the same sign.  Their product is trivial:

\[
\operatorname{sgn}(sigma)_{m Koszul},
\operatorname{sgn}(sigma)_{m Thom}=+1.
\]

All (55\cdot6=330) order checks therefore agree.  The native Thom package
cancels not only octagon loop holonomy but the full local (S_3) character at
the first triple intersections.

This proves local sign coherence, not global decagon descent.  The fourteen
free top classes are the possible integral obstruction coordinates for
extending the locally compatible Cut data across the entire nerve.  The next
test must evaluate the actual transformed physical comparison on this
(mathbb Z^{14}), or construct the full loaded decagon Čech totalization and
show that its carrier differential kills the coordinates.  Vanishing cannot
be inferred from the sign cancellation alone.

The executable audit is
`research/voevodsky/check_n10_physical_cut_nerve.py`.
