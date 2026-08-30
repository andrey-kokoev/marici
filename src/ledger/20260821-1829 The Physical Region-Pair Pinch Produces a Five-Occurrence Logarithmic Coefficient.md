# 1829 — The Physical Region-Pair Pinch Produces a Five-Occurrence Logarithmic Coefficient

## Local normal form

At Entry 1828's smooth Morse pinch, choose a common normal coordinate \(s\)
and two tangent coordinates \(z\).  The two active walls have source-oriented
local forms

\[
q_1=s+Q_1(z)+\cdots,
\qquad
q_2=-s+Q_2(z)+\cdots.
\]

The positive Landau Hessian implies that \(Q_1+Q_2\) is positive definite.
Taking the normal residue reduces the physical loop form to

\[
\operatorname{Res}_s
\frac{d^3\ell}{q_1q_2}
=
u\,
\frac{d^2z}{\delta+Q_1(z)+Q_2(z)+\cdots},
\qquad u\ne0.
\]

The two-dimensional Morse integral is logarithmic.  Its local variation is a
rank-one Kummer/vanishing-cycle coefficient with additive monodromy
\(2\pi i\) times Entry 1828's nonzero source-normalized residue coefficient.

## Labelled cyclic assembly

The pair \((g_{123},g_{125})\) has a free five-element labelled orbit under
the source \(C_5\) action.  Retaining occurrences gives

\[
\mathbb Q[C_5],
\qquad
\dim=5,
\qquad
\chi=(5,0,0,0,0).
\]

Collapsing these five occurrences to one scalar equation would discard the
source incidence and is not authorized.

## Classification

\[
\boxed{
\text{existing labelled region-pair carrier incidence}
+
\text{rank-one logarithmic coefficient per occurrence}.
}
\]

No new carrier divisor or cell is required by this local physical pinch.
The new structure is coefficient-theoretic and sector-specific, exactly of
the type allowed by H2.

This is a local Picard--Lefschetz packet.  It does not yet prove activation by
the complete global Bunch--Davies integration chain, nor compatibility with
other orbit sectors under global sewing.

## Next falsifier

Derive the global relative-chain intersection number for one labelled
occurrence from the frozen contour and transport it cyclically.  The packet is
physically active only if that source-defined pairing is nonzero and
occurrence-covariant.  A vanishing pairing would make the local coefficient
physically invisible without altering the carrier classification.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_picard_lefschetz_packet.py`
- `research/benincasa/results/five-site-region-pair-picard-lefschetz-packet.json`
- Entries 1827--1828
- allocator claim: `seqclaim-ca6ed130f67272870ad82f5f`
