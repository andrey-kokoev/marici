---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2203 — The Signed Deletion Augmentation Has a Canonical Jordan Dilation

## Total-variation factorization

Let

\[
\mu(S)=(-2)^{|S|}.
\]

Its Jordan masses are

\[
\mu^+(\Omega)=13,
\qquad
\mu^-(\Omega)=14,
\]

and its total variation is

\[
\|\mu\|_{\rm TV}=27=(1+2)^3.
\]

Normalize the absolute weights:

\[
q(S)=\frac{2^{|S|}}{27}
=\prod_{e}\left(\frac23\right)^{1_S(e)}
\left(\frac13\right)^{1-1_S(e)}.
\]

Thus \(q\) is the law of three independent deletion bits with probability
\(2/3\). With parity character

\[
\chi(S)=(-1)^{|S|},
\]

one has the exact factorization

\[
\boxed{
\sum_S(-2)^{|S|}T_S
=27\,\mathbb E_q[\chi(S)T_S].
}
\]

## Status

This is the canonical Jordan or total-variation dilation of the finite signed
measure. It introduces no fitted coefficient and uniquely separates positive
sampling weight from signed readout.

It is nevertheless a mathematical dilation, not yet a frozen cosmological
apparatus. The source declares the left side, but not three Bernoulli ancillas
or a parity measurement realizing the right side.

## Evidence

- Entry 2202
- `research/benincasa/checkers/deletion_jordan_dilation.rs`
