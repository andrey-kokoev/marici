# The first equally spaced rank-four source packet is positive numerically

## Packet

At width

\[
\sigma=0.005,
\]

take four translates centered at

\[
-0.375,
\quad-0.125,
\quad0.125,
\quad0.375.
\]

The source-side kernel values at successive spacing multiples are approximately

\[
0.1496980,
\quad-0.1171689,
\quad0.0922235,
\quad-0.0622867.
\]

They define a real symmetric Toeplitz Gram matrix of rank four.

## Cholesky test

The successive Cholesky pivots are approximately

\[
0.1496980,
\quad0.0579897,
\quad0.0579851,
\quad0.0561568.
\]

Every pivot is positive, so Sylvester's criterion gives numerical positive definiteness. The determinant is approximately

\[
2.83\times10^{-5}.
\]

## Significance

The alternating signs of the kernel values do not obstruct matrix positivity. The fourth translate introduces a genuinely new principal-minor condition beyond the rank-three packet, and it passes with a substantial pivot margin.

No zero-location data enter the calculation. All entries come from the endpoint, gamma, and prime source formula.

## Scope

This is a floating scout. A perturbation certificate requires entrywise error bounds for the additional separation \(d=0.75\). It establishes neither all rank-four packets nor the all-rank Toeplitz theorem.

## Verification

```text
python research/voevodsky/checkers/scout_four_translate_source_gram.py
```

Artifacts:

- `research/voevodsky/checkers/scout_four_translate_source_gram.py`
- `research/voevodsky/results/four_translate_source_gram_scout.json`
