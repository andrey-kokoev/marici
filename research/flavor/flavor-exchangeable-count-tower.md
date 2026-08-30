# Exchangeable count tower (WP336)

## Binomial zeta transform

For six exchangeable binary domains, let (q_k) be the probability of total
positive count (K=k). The factorial-count moments are

\[
m_j=\mathbb E\binom Kj
=\sum_{k\geq j}\binom kj q_k.
\]

This is an upper-triangular binomial zeta transform with determinant one. Its
exact Möbius inverse is

\[
q_k=\sum_{j\geq k}(-1)^{j-k}\binom jk m_j.
\]

The complete tower (m_0,\ldots,m_6) is therefore jointly faithful on the
finite exchangeable count packet. This is the domain-count analogue of
Benincasa's Boolean-route inversion theorem.

## Label boundary

The theorem does not recover labelled spatial routes. Laws concentrated on
`100` and `010` are distinct labelled preparations but have identical count
laws and hence identical complete count towers. Exchangeability quotients
those labels; labelled recovery requires source-derived address ports.

## Instrument gate

Physical use requires executable coincidence measurements through order six,
including efficiency, missed-domain, detector-correlation, and support
calibration. Exchangeability must be derived or tested on the admitted source
domain rather than assumed from symmetric notation.

The tower identifies an exchangeable law if realized. It does not select that
law or its flavor parameters.

Run `uv run --with sympy python
research/flavor/checkers/wp336_exchangeable_count_tower.py` to regenerate the
exact inversion audit.
