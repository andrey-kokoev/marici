# Adelic cutoff labelled-chain functor

## Question

Can the adelic cutoff index category be lifted to algebraic filler chain objects before analytic Mellin evaluation?

## Claim boundary

The construction is algebraic and finitely supported. It supplies no analytic norm, graph topology, or completed operator.

## Functor

For each cutoff \(N\), let

\[
C_N=\mathbb Q[F_N]\otimes C_{\mathrm{aff}}(D_w).
\]

A transition \(N\leq N'\) acts by zero-extension on the label module and identity on affine chains. Boundary acts only on the affine-chain factor.

A finite coefficient packet paired with an affine filler maps to

\[
\sum_{r\in F_N}c_r([r]\otimes\sigma).
\]

## Naturality

Exact sparse-chain fixtures at bounds 2, 4, and 6 verify:

- identity and composition of transitions;
- boundary naturality;
- reciprocal naturality of transitions;
- reciprocal naturality of boundary;
- reciprocal involution.

Reciprocal action simultaneously sends \(r\mapsto1/r\) and reflects the spectral simplex.

## Remaining analytic map

This functor organizes labelled source chains but does not evaluate them. The next datum is a natural Mellin-evaluation transformation into the declared analytic graph-topology target. Uniform completion can be tested only after that target and its transition maps are typed.

## Disposition

The missing cutoff functor has been constructed at the algebraic labelled-chain level. The completion blocker is narrowed to analytic evaluation and topology rather than cutoff indexing or chain transitions.

## Verification

- `research/voevodsky/adelic-cutoff-labelled-chain-functor-v1.json`
- `research/voevodsky/checkers/check_adelic_cutoff_labelled_chain_functor.py`
- `research/voevodsky/results/adelic_cutoff_labelled_chain_functor.json`
