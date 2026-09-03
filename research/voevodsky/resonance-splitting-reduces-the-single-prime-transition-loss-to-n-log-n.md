# Resonance splitting reduces the single-prime transition loss to N log N

## Question

Can the nested-set Abel estimate be integrated despite its dual resonances and its nondecaying large-coordinate envelope?

## Claim boundary

Combining the Abel estimate with the independent endpoint-count decay and splitting each dual resonance cell at their crossover yields harmonic rather than quadratic accumulation. The transition contribution scales as \(N(1+\log N)\), up to explicit initial-cell and source constants. This removes the large-coordinate divergence of the Abel bound. A fully frozen numerical constant remains to be assembled.

## Two simultaneous bounds

For the endpoint sum of \(N\) nested translated sections, the direct endpoint estimate gives

\[
|k_\Omega(t)|
\leq
\frac{N}{\pi|t|}.
\]

For \(|t|\geq2/p\), the nested-set Abel estimate gives

\[
|k_\Omega(t)|
\leq
\frac{p}{\pi|\sin(pt/2)|},
\]

up to a fixed harmless enlargement accounting for the terminal amplitude. Neither bound is adequate alone; use their minimum.

## One resonance cell

Let a positive dual-resonance cell have lower coordinate \(T_k\). Write \(\phi\in[0,\pi]\) for phase distance from its resonance. The elementary bound

\[
\sin(\phi/2)
\geq
\frac{\phi}{\pi}
\]

gives

\[
|k_\Omega(t)|
\leq
\min\left(
\frac{N}{\pi T_k},
\frac{p}{\phi}
\right).
\]

When \(T_k\leq N/p\), the crossover occurs at

\[
\phi_k=
\frac{\pi pT_k}{N}.
\]

Direct integration of the squared minimum over both sides of the resonance gives the cell estimate

\[
\int_{\text{cell }k}|k_\Omega(t)|^2dt
\leq
\frac{4N}{\pi T_k}.
\]

## Harmonic accumulation

Resonance cells are spaced by \(2\pi/p\), so \(T_k\) is proportional to \(k/p\). Summing the pre-crossover cells gives

\[
\sum_{k\leq cN}
\frac{N}{T_k}
\leq
C pN
\sum_{k\leq cN}\frac1k
\leq
C pN(1+\log N).
\]

Beyond \(T_k>N/p\), the direct endpoint estimate is smaller throughout each cell. Its squared tail sums as

\[
N^2\sum_{k>cN}\frac1{k^2}
=O(N).
\]

The finite region \(|t|<2/p\) is controlled by the mass bound

\[
|k_\Omega(t)|
\leq
\frac{|\Omega|}{2\pi}.
\]

Multiplication by the crossing weight \(\min(2L,|t|)\) preserves the same asymptotic order.

## Consequence

For the one-prime window,

\[
\operatorname{Tr}(T-T^2)
\leq
C_{L,p,W}\,N(1+\log N)
\]

with an explicit constant obtainable by retaining the cell endpoints and the harmless amplitude factors. This replaces the rejected \(N^2\) component envelope and resolves the large-\(|t|\) divergence.

## Remaining gate

The exact constant must be frozen without dropping the terminal amplitude or the first resonance cells. Then it can be inserted into

\[
M
\geq
\operatorname{Tr}(T)
+
\frac{1}{\eta}
\operatorname{Tr}(T-T^2).
\]

The resulting finite dimension may still be large; this theorem changes the proven scaling, not the RH disposition.

## Verification

- `research/voevodsky/checkers/check_resonance_split_nlogn.py`
- `research/voevodsky/results/resonance_split_nlogn.json`
