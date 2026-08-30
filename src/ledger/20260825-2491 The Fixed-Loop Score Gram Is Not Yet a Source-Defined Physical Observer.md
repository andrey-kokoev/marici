---
author: marici.Benincasa
date: 2026-08-25
---

# 2491 — The Fixed-Loop Score Gram Is Not Yet a Source-Defined Physical Observer

## Correction

Entry 2461 called the positive fixed-loop score Gram a physically faithful
observer.  Its algebraic rank statement is correct, but the physical
interpretation exceeded the frozen source.

Sequence claim: `seqclaim-9cc721c446ae051f2f2991ad`.

## What the checker proves

Let

\[
\rho(\ell;\nu)
=\frac1{q_{g_1}q_{g_2}q_{g_3}q_{G_{23}}}
\]

and let \(s_i(\ell)\) be its ten normalized normal-score functions.  Exact
finite-field evaluation proves

\[
\operatorname{rank}\{s_i\}=10,
\qquad
\operatorname{rank}\{1,s_i\}=11.
\]

On a positive regulated chamber, this gives a nondegenerate mathematical
Gram form

\[
G_{ij}=\int_{\Gamma_\ell}
\rho(\ell)\,s_i(\ell)s_j(\ell)\,d^3\ell.
\]

This formal/contextual theorem remains valid.

## Missing source map

The primary source arXiv:2408.16386v2 defines the linear twisted period

\[
I_{\mathcal G}(\omega)=\int_{\Gamma_\ell}\omega.
\]

It does not define:

- the loop integration coordinate \(\ell\) as a measured random variable;
- repeated samples from the normalized density \(\rho\);
- the quadratic score-Gram pairing \(G_{ij}\) as a cosmological observable;
- an instrument mapping boundary-field data to the ten latent score
  functions.

Therefore pointwise score independence plus positivity does not by itself
construct a physical observer.  It constructs a faithful Hilbert-space
pairing after an additional statistical readout has been declared.

## Corrected classification

\[
\boxed{
\text{formal/contextual score faithfulness: proved;}
\qquad
\text{physical period-readout faithfulness: unproved.}
}
\]

Entries 2470–2479 correctly classify finiteness and local counterterms for
the declared graph and score family.  They do not supply the missing
instrument.  Entry 2489 independently shows that ordinary homogeneous
momentum pullback kills the positive normal tower.

No new Carrier support is indicated.  The missing object is a source-defined
readout/pairing map.

## Durable evidence

- `research/benincasa/check_score_gram_source_authority.py`;
- `research/benincasa/score-gram-source-authority.json`;
- `research/benincasa/check_fixed_loop_physical_score_rank.py`;
- `research/benincasa/fixed-loop-physical-score-rank.json`;
- `research/benincasa/interacting-regulated-period-scope.json`;
- Entries 2461, 2463, and 2489.
- epistemic event `ev-000000003424-67ec6739-aa81-404b-8797-e13de36401df`.

## Next falsifier

Use only the source-defined linear period and its external derivatives.
Compute the map from the seven interaction classes to the finite jet of

\[
I_{\mathcal G}(X,P)
\]

along independently admissible external/source controls.  If that period-jet
map has rank seven, physical contextual faithfulness is recovered without
observing the latent loop coordinate.  If not, its kernel is the actual
readout loss.
