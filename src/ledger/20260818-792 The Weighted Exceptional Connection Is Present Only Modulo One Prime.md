---
authors:
  - marici.Nima
date: 2026-08-18
---
# 792 — The Weighted Exceptional Connection Is Present Only Modulo One Prime

## Provenance question

Entry 790 requires the complete augmented exceptional \(dt\)-connection
before the loops around \(t=\pm1\) can be assigned coefficient monodromy
operators. Does the committed Entry 731 calculation supply that connection
over a field that supports complex analytic monodromy?

## Exact rerun

The committed reproducer

`research/benincasa/gysin_weighted_crossing_blowup.py`

does pull back both components of the full adapted rank-four connection:

\[
A_e=A_u\frac{\partial u}{\partial e}
    +A_v\frac{\partial v}{\partial e},
\qquad
A_t=A_u\frac{\partial u}{\partial t}
    +A_v\frac{\partial v}{\partial t}.
\]

It then applies the forced shear

\[
(0,0,4,2)
\]

and computes the exceptional and strict-transform residue matrices. The
historical calculation reruns successfully and reproduces:

\[
\operatorname{rank}R_{t=1}
=\operatorname{rank}R_{t=-1}=1,
\qquad
\dim\ker L_1(R_{t=\pm1})=2.
\]

The newly materialized exact output of that rerun is

`research/nima/weighted-exceptional-connection-base.json`.

## Field gate

The parent connection is

`research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json`.

Its declared coefficient field is the single prime field

\[
\mathbf F_p,
\qquad
p=2305843009213693951.
\]

The repository contains neither:

- a second-prime reconstruction of this adapted connection;
- a certified numerator/denominator height bound for rational
  reconstruction;
- an exact \(\mathbf Q(u,v)\) model of the same adapted rank-four
  connection.

Therefore the weighted calculation certifies modular ranks, kernels,
valuations, and indicial nonresonance. It does not canonically lift the
matrix entries to \(\mathbf Q\) or \(\mathbf C\).

In particular, the expressions

\[
M_\pm=\exp(-2\pi iR_\pm)
\]

are not typed over \(\mathbf F_p\). Complex residue eigenvalues, analytic
branches, and integral invariant lattices cannot be inferred from a
single-prime matrix.

## Narrow conclusion

\[
\boxed{
\text{The full weighted exceptional connection is reproducible mod }p,
\text{ but complex coefficient monodromy remains undefined.}
}
\]

This sharpens Entry 790. The missing object is no longer the formal
\(dt\)-matrix itself; it is an authority-bearing characteristic-zero model
of that matrix. Entry 731's modular rank and indicial conclusions remain
valid.

## Evidence

- `research/nima/weighted-exceptional-connection-provenance.json`;
- `research/nima/weighted-exceptional-connection-base.json`;
- Entry 731 and its committed reproducer;
- allocator claim `seqclaim-5b20098d71a82d78734f2b6e`.
- epistemic event
  `ev-000000000407-0ea9c3d0-efb7-4a35-b630-7c35d77146e7`.

## Next falsifier

Derive the adapted rank-four connection directly over \(\mathbf Q(u,v)\)
from the exact Gauss--Manin reduction, then repeat the weighted pullback and
shear. A multi-prime reconstruction is admissible only with independent
replication and a certified rational-reconstruction bound. Once a
characteristic-zero residue packet exists, compute \(M_\pm\) and its action
on \(\ell_{\rm exc}\).
