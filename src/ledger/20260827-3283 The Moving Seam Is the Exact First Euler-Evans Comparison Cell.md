# 3283 — The Moving Seam Is the Exact First Euler–Evans Comparison Cell

For the prime-shifted source, with \(s=1/2+z\), \(q_p=p^{-s}\), and

\[
B_p(z)=\int_0^{\log p}\phi(v)e^{zv}\,dv,
\]

the exact endpoint contribution is

\[
F_p(z)=q_p\bigl(F(z)-B_p(z)\bigr).
\]

Hence the bare Euler first variation \(q_pF\) differs from the Evans endpoint
first variation by exactly the source-derived moving-seam current
\(-q_pB_p\). The identity holds for the undivided section, including at its
zeros; the logarithmic quotient is only a chart away from the divisor.

This closes the first scalar cross-tower comparison cell and proves that a
candidate operator lift must retain the moving endpoint as a genuine boundary
port. The remaining gate is the two-addition operator lift whose determinant
shadow reproduces the det3 cocycle and whose endpoint shadow reproduces the
twice-shifted Evans section.

- Research packet: research/grothendieck/the-moving-seam-is-the-exact-first-euler-evans-comparison-cell.md
- Checker: research/grothendieck/checkers/check_moving_seam_first_euler_evans_cell.py
- Sequence claim: seqclaim-34767969335c278b4063a994
- Graph event: 6957
