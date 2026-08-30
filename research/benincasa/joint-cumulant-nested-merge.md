# Complete joint cumulants make correlated non-Gaussian merge associative

At cumulant order (r), merging blocks (A,B) requires every labelled mixed
slot sector, not only the pure cumulants of (A) and (B). The (2^r) slot
patterns form a disjoint partition:

\[
(|A|+|B|)^r
=
\sum_{\epsilon\in\{A,B\}^r}
|A|^{\#A(\epsilon)}|B|^{\#B(\epsilon)}.
\]

Retaining the complete joint cumulant tensor therefore makes nested block
merger a repeated regrouping of the same labelled ordered tuples. Omitting the
mixed sectors produces a strict deficit for every (r>1).

The exact checker audits 23,713 ordered binary trees, 1,590,673 internal
node/order pairs, and 115,437,412 labelled mixed-slot sectors through eleven
occurrences and cumulant order eight.

