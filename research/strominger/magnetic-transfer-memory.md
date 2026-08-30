# Magnetic Hall transfer has memory floor(q/2)

Companion to checkers/magnetic_transfer_memory_checks.py (8/8, exit 0) and
results/magnetic_transfer_memory.json.

For each full-Hall component, compare the selected row set at cutoff \(k\)
with that at \(k-1\). The row sets are nested throughout

\[
2\le g\le15,\qquad1\le q\le30,\qquad0\le k\le20.
\]

For the two newly admitted rows, record the oldest preceding pole-depth pair
whose columns have nonzero support there. Its distance from the new pair is
the backward memory.

Across 8,362 admitted extensions,

\[
\boxed{w(q)=\left\lfloor\frac q2\right\rfloor.}
\]

No interaction reaches farther back. For every tested \(g\ge3,q\), some
extension attains the bound, so one less unit of memory is insufficient in
this ordering. The first tight witness is \((g,q)=(3,2)\).

Beyond the finite initial window \(k\le\lfloor q/2\rfloor+1\), the two rows
added at cutoff \(k\) obey

\[
r_-=-2k-g,\qquad
r_+=-2k-g+2\left\lfloor\frac q2\right\rfloor+1.
\]

An old pole pair \(d\) steps behind begins at \(r_-+2d\). It can meet the
second boundary row only if

\[
2d\le2\left\lfloor\frac q2\right\rfloor+1,
\]

which for integral \(d\) is equivalent to
\(d\le\lfloor q/2\rfloor\). This gives a symbolic support explanation of the
observed width once the stable Hall-row formula is established.

At \(q=1\), \(w=0\), recovering the scalar block-triangular theorem. For
\(q>1\), only the last \(\lfloor q/2\rfloor\) pole pairs can affect the new
boundary equations. Thus the global determinant problem admits a cutoff-
independent finite state whose size grows with reflection distance, not with
the Laurent cutoff.

The Hall-row formula and nesting remain finite-range results; their support
implication is symbolic. The explicit transfer matrix and its singular locus
remain open. Hall-deficient grade-two blocks are skipped at the deficient step
rather than treated as ordinary transfers.
