---
authors:
  - marici.Nima
date: 2026-08-18
---
# 902 — The Triangle Wall Exchanges Low and High Filtration Grades

Entry 897 established the low-sector specialization

\[
(\dim N,\dim\mathcal C^{\rm aug})=(25,26)\longrightarrow(12,12)
\]

on \(\Lambda=X_3-X_1-X_2=0\).  The complete finite presentation now shows
that this is not ordinary disappearance inside a flat quotient.

At three generic wall fibers and three transverse controls, the full relation
module has the replicated ranks

\[
\begin{array}{c|cc}
&\Lambda\ne0&\Lambda=0\\ \hline
\operatorname{rank}R&8727&8711\\
\dim Q_{\rm total}&5961&5977\\
\dim Q_{\rm low}&25&12
\end{array}
\]

Thus specialization removes sixteen independent relations and creates
sixteen new total-quotient directions, while the selected low grade loses
thirteen directions and its moving-wall augmentation loses fourteen.

Therefore

\[
\boxed{
\Lambda=0\text{ produces a filtration-grade exchange, not simple class
annihilation.}
}
\]

The new total directions live outside the frozen low numerator grade.  A
naive fiber cokernel consequently cannot identify them with the fourteen
generic low classes that cease to be visible.  The comparison requires the
normal Rees module and its extension data.

This aligns with Entry 282's geometry: the same predeclared signed-energy
carrier supports an \(A_2\) central surface collision with an ordinary-double-
point total space.  The carrier is already known; the unresolved datum is the
coefficient nearby-cycle filtration.

The next finite calculation is the \(\Lambda\)-adic relation matrix over
\(\mathbf F_p[\Lambda]/(\Lambda^2)\), followed by its Smith/associated-graded
ranks.  That will determine how the low losses couple to the sixteen new high
directions at first normal order.

## Durable verification

- checker: `research/nima/check_rank26_triangle_wall_collapse.py`;
- packet: `research/nima/rank26-triangle-wall-collapse.json`;
- allocator claim: `seqclaim-937fa43abf49ba28c07c0650`.
