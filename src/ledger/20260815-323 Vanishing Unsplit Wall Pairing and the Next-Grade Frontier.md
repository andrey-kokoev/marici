---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Vanishing Unsplit Wall Pairing and the Next-Grade Frontier

> Correction: entry 234 replaces the incomplete connecting-form argument
> below with the complete \(K_1/K^{3/2}\) calculation. The vanishing verdict
> survives at the leading grade, and entry 234 also closes the next grade.

## Record

Status: the relative connecting form of the canonical unsplit occurrence
pair has zero pairing with the frozen source exceptional wall. The nonzero
exceptional commutator in the \(q_{\mathcal G_{ij}}\)-only projection does
not survive the literal lower-denominator lift at the leading full
occurrence grade.

No denominator, carrier incidence, support summand, regulator hierarchy,
projector, or normalization is added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the singular primitive of the unsplit occurrence pair produces a
nonzero relative wall class on the source exceptional chain.}
}
\]

The finite falsifier was the source-fixed reflection symmetry of the wall
and an odd connecting form.

## Frozen exceptional wall

Entries 226, 320 derive the source exceptional disk

\[
Q(r,n)
=
\beta(1-r^2)-\alpha n^2>0,
\]

with

\[
\alpha=4x^2y^2,
\qquad
\beta=8xy(x+y).
\]

At the existing lower-divisor collision \(r=0\), the source chain is the
oriented interval

\[
W_{\rm src}
=
\left[
-\sqrt{\frac\beta\alpha},
+\sqrt{\frac\beta\alpha}
\right]_n.
\]

No wall or endpoint is fitted: both endpoints are the intersection of the
frozen Cayley--Menger boundary with \(r=0\).

## Relative connecting form

Entry 322 gives the exact leading two-form

\[
\omega_{-3}
=
-\frac{n}{4xy,r^2},dr\wedge dn
=
d\eta_{-3},
\]

where

\[
\eta_{-3}
=
\frac{n}{4xy,r},dn.
\]

The principal normal coefficient of the primitive defines the relative
connecting form on \(r=0\):

\[
\boxed{
\partial_{r=0}(\eta_{-3})
=
\frac{n}{4xy},dn,
}
\]

up to the already frozen common Leray scalar and orientation. Since the
pairing vanishes, neither affects the verdict.

## Source-chain pairing

Let

\[
N=\sqrt{\frac\beta\alpha}.
\]

Then

\[
\left\langle
\partial_{r=0}(\eta_{-3}),W_{\rm src}
\right\rangle
=
\frac1{4xy}\int_{-N}^{N}n,dn
=
\frac{N^2-N^2}{8xy}
=0.
\]

Equivalently, the wall and its endpoints are invariant under
\(n\mapsto-n\), while the connecting form is odd.

The same calculation holds in all three cyclic Cut sectors:

\[
\boxed{
(P_{12},P_{23},P_{31})=(0,0,0).
}
\]

## Verdict

The nonzero-wall-class conjecture is falsified:

\[
\boxed{
\text{the canonical unsplit lower-occurrence lift kills the leading
exceptional correction on the literal source chain.}
}
\]

This is a genuine ablation of the projected result. Entry 321 established a
nonzero cyclic sewing only after forgetting the lower denominator.
Entries 230--231, 322--323 now show:

\[
\text{project}
\longrightarrow
\text{nonzero factor-two class},
\]

but

\[
\text{retain occurrences}
\longrightarrow
\text{cancel simple residue}
\longrightarrow
\text{exact leading form}
\longrightarrow
\text{zero source-wall pairing}.
\]

Therefore occurrence forgetting is not conservative for this integrated
nearby comparison.

## Scope boundary

The result is only for the leading full occurrence weight \(-3\) of the
restored lower-denominator factor. It does not prove that the complete
physical Cut--nearby commutator vanishes.

Subleading expansions of

\[
q_{\mathfrak g_1}^{-1},
\quad
q_{\mathfrak g_2}^{-1},
\quad
q_{\mathfrak g_3}^{-1},
\quad
q_{\mathfrak g_{23}}^{-1}
+
q_{\mathfrak g_{31}}^{-1},
\]

and of the Cayley--Menger/master factor can break the leading
\(n\mapsto-n\) oddness. The first possible surviving term is the next
weight.

## Classification

- existing carrier: exceptional disk, lower collision wall, and its two
  Cayley--Menger endpoints;
- leading absolute coefficient class: exact;
- leading relative source pairing: zero;
- regulator hierarchy: absent from the unsplit result;
- elliptic Gauss--Manin data: no new image;
- genuinely new carrier datum: none.

## Exact evidence

- `research/benincasa/check_unsplit_relative_wall_pairing.rs`;
- `research/benincasa/unsplit-relative-wall-pairing.json`;
- exact endpoint-square cancellation at 10,201 generic nonsoft pairs;
- cyclic covariance and reflection-oddness assertions;
- warnings-denied optimized Rust compilation and execution.

## Next finite falsifier

Expand the complete source-normalized unsplit integrand one additional power
of \(\tau\), including:

- the three common lower denominators;
- the occurrence-pair numerator and denominator;
- the Cayley--Menger branch;
- the source double-pole master numerator and Jacobian.

Reduce the next coefficient modulo exact forms and evaluate its relative
wall pairing. A nonzero canonical result is the first literal full-source
exceptional correction. Another zero moves the frontier one grade higher.
Any dependence on splitting the occurrence pair is prohibited.

## Outcome contract

~~~json
{
  "claim": "The leading unsplit relative connecting form has nonzero source-wall pairing.",
  "status": "falsified",
  "wall": "r=0, n in [-sqrt(beta/alpha),sqrt(beta/alpha)]",
  "connecting_form": "n/(4*x*y) dn",
  "source_pairing": 0,
  "cyclic_pairings": [0, 0, 0],
  "projected_nonzero_class_survives_full_lift": false,
  "scope": "leading full occurrence weight only",
  "new_carrier_incidence": false,
  "next_experiment": "Compute and reduce the next tau coefficient of the complete unsplit source integrand."
}
~~~
