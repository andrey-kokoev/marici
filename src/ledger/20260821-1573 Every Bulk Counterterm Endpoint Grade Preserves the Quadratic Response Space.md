# 1573 — Every Bulk Counterterm Endpoint Grade Preserves the Quadratic Response Space

## Question

Can the dynamical counterterms \(c_1,c_2,c_3\) introduce a boundary response
direction beyond the rank-three \((\operatorname{Re}A_p,\operatorname{Im}A_p,B_p)\)
object, even though the cubic loop itself closes there?

## Frozen source operators

The source bulk counterterms are

\[
\mathcal L_{ct}
=c_1M_{\rm pl}^2a^3\dot\zeta^2
-c_2M_{\rm pl}^2a(\partial\zeta)^2
-c_3a^{-1}(\partial^2\zeta)^2.
\]

In conformal time their quadratic insertion monomials are, up to common real
normalizations,

\[
\begin{aligned}
c_1:&\quad p^4,\\
c_2:&\quad p^2\eta^{-2}-2ip^3\eta^{-1}-p^4,\\
c_3:&\quad p^4-2ip^5\eta-p^6\eta^2.
\end{aligned}
\]

The source-internal correction of Entry 1536 is retained: the third solved
coefficient label is \(c_1\), not the repeated \(c_3\) printed in the paper.

## Endpoint census

The complete nonnegative endpoint grades are

\[
(c_1,0),\quad(c_2,0),\quad(c_3,2),\quad(c_3,1),\quad(c_3,0).
\]

Each was reduced with the same endpoint-primitive recurrence used for Entries
1563--1570. Its observation-time polynomial was reconstructed and checked at
an unused point, then evaluated against the four oscillatory annihilators of
Entry 1528. Counterterm insertions have no zero-frequency column, so the
\(B_p\) annihilator is automatic.

## Result

Every tested grade closes independently. The maximum numerical defect is

\[
5.33\times10^{-15}.
\]

Hence

\[
\boxed{
\mathcal C_{ct}^{(g)}
\in
\operatorname{span}
\{r_{\operatorname{Re}A},r_{\operatorname{Im}A},r_B\}
\qquad
\text{for every nonnegative source endpoint grade}.}
\]

## Consequence

Arbitrary divergent or finite choices of \(c_1,c_2,c_3\) can change the
coordinates of the initial-state matching, but cannot create a new quadratic
boundary coefficient direction. In particular, subtraction-scheme dependence
acts internally on the existing response object.

Combining Entries 1568, 1570, and 1573 gives a complete coefficient-space
closure theorem for the toy one-loop packet. What remains undetermined by the
paper is the source-specific **finite coordinate choice** after momentum
integration, not the type or rank of the target coefficient object.

This does not establish Hadamard preservation: that requires the fully
subtracted momentum-dependent kernels and their ultraviolet asymptotics.

## Artifacts

- `research/benincasa/checkers/finite_time_counterterm_boundary_closure.rs`
- `research/benincasa/results/finite-time-counterterm-boundary-closure.json`

Ledger sequence claim: `seqclaim-b615b3e3798fca0cc7482553`.
