# An explicit resonance constant makes the first-prime reduction finite

## Question

Can the initial resonance cell, harmonic middle cells, and large-coordinate tail be combined into one explicit transition-trace bound?

## Claim boundary

For the one-prime window and the previously scouted nested bad sections, yes. Retaining the small-coordinate vanishing of each section amplitude yields an explicit bound of order \(N\log N\). At the diagnostic parameters it lowers the sufficient dimension from about \(5.37\) million to about \(474{,}000\). The input interval geometry remains floating rather than certified.

## Zero resonance

The nested-section amplitude satisfies both

\[
|A_{N-1}(t)|
\leq |t|p
\]

and

\[
\operatorname{TV}_jA(t)
\leq |t|p.
\]

Hence near the zero resonance,

\[
|k_\Omega(t)|
\leq
\frac p\pi
\min\left(
N,
\frac1{|\sin(pt/2)|}
\right).
\]

For the first-prime window, the half-cell \(0\leq t\leq\pi/p\) lies inside \(t<2L\), where the crossing weight is \(t\). Splitting at phase \(\phi=\pi/N\) gives the explicit two-sided zero-cell contribution

\[
D_0
\leq
1+2\log N.
\]

## Middle resonances

Let

\[
T_k=
\frac{2\pi}{p}\left(k-\frac12\right).
\]

For cells with \(T_k\leq N/p\), the previous squared-minimum integration and the crossing bound \(2L\) give

\[
D_k
\leq
\frac{16LN}{\pi T_k}.
\]

If

\[
K=
\left\lfloor
\frac{N}{2\pi}+rac12
\right\rfloor,
\]

then

\[
\sum_{k=1}^{K}D_k
\leq
\frac{8LpN}{\pi^2}
\sum_{k=1}^{K}
\frac1{k-1/2}.
\]

## Exterior tail

After the crossover, direct endpoint decay gives

\[
D_{\rm tail}
\leq
\frac{4LpN}{\pi^2}.
\]

Thus

\[
\operatorname{Tr}(T-T^2)
\leq
1+2\log N
+
\frac{8LpN}{\pi^2}
\sum_{k=1}^{K}
\frac1{k-1/2}
+
\frac{4LpN}{\pi^2}.
\]

## Diagnostic evaluation

For

\[
L=7/20,
\qquad
p=2\pi/\log2,
\qquad
N=1229,
\qquad
\delta=0.05,
\]

the components are bounded by

\[
D_0\leq15.23,
\]

\[
D_{\rm middle}\leq22887.63,
\]

\[
D_{\rm tail}\leq1580.29.
\]

Therefore

\[
\operatorname{Tr}(T-T^2)
\leq24483.14.
\]

Using the scouted trace and \(\eta\) gives

\[
M\geq474019
\]

as the first integer above the diagnostic bound.

## Disposition

The resonance constant is explicit and removes both the zero-cell and large-coordinate gaps. The first-prime finite reduction remains large but is now six orders rather than seven. Certification still requires directed enclosures for the bad sections and constants; the finite Schur matrix remains RH-bearing.

## Verification

- `research/voevodsky/checkers/check_explicit_resonance_transition_constant.py`
- `research/voevodsky/results/explicit_resonance_transition_constant.json`
