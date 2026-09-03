# Adelic cutoff index category

## Question

Does the existing adelic-height result supply the missing cutoff index and transition structure?

## Claim boundary

The construction supplies transitions among cutoff label sets. It does not yet lift them to filler chain objects or prove completion.

## Index category

Objects are positive integer bounds \(N\), with a unique arrow \(N\to N'\) when \(N\leq N'\). For a reduced nonzero rational \(r=a/b\), define

\[
H(r)=\max(|a|,|b|).
\]

The fiber at \(N\) is

\[
F_N=\{r\in\mathbb Q^\times:H(r)\leq N\}.
\]

For \(N\leq N'\), the transition is literal inclusion \(F_N\subseteq F_{N'}\). These inclusions satisfy identity and composition strictly.

## Reciprocal synchronization

Since

\[
H(1/r)=H(r),
\]

reciprocal inversion preserves every fiber and commutes with every transition. Restriction to positive integers gives \(H(n)=n\), recovering the Euler cutoff.

The checker exhaustively verifies these properties through bound 8 using exact reduced fractions.

## Remaining lift

Nested label fibers do not themselves define maps between filler chain objects. The next datum must be a functor from this index category to chain objects, with natural boundary maps and affine-simplex fillers. Uniform graph-topology descent remains a later gate.

## Disposition

Cutoff synchronization and its indexing category are constructed. The previous statement that no cutoff transition existed is narrowed: label transitions exist canonically; filler-chain transitions do not.

## Verification

- `research/voevodsky/adelic-cutoff-index-category-v1.json`
- `research/voevodsky/checkers/check_adelic_cutoff_index_category.py`
- `research/voevodsky/results/adelic_cutoff_index_category.json`
