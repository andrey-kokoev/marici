---
author: marici.Benincasa
---

# 2012 — The Mixed Canonical Correlator Reads the Third-Grade Initial-State Direction

## Question

Entry 2011 established a horizontal third-grade coordinate

\[
\operatorname{Re}C,
\qquad
C=A(1-ik\eta_0)^2e^{2ik\eta_0},
\]

but only as a formal normal derivative of the equal-time field correlator. Does a source-defined canonical observable read it?

## Canonical momentum

The quadratic inflationary action in Collins--Holman--Vardanyan, arXiv:1408.4801v1, Eq. (3.1), gives

\[
\Pi_\zeta
=
\frac{\dot\phi^2}{\dot\rho^2}a^3\dot\zeta
=
2\epsilon M_{\rm pl}^2a^2\partial_\eta\zeta
\]

at leading slow-roll order. Hence the symmetrized equal-time mixed correlator is obtained by applying \(2\epsilon M_{\rm pl}^2a^2\partial_\eta\) to the equal-time field covariance.

## Frozen field covariance

Use the horizontal coordinates

\[
C=P+iQ,
\qquad
N=B|r(k\eta_0)|^2.
\]

Entry 2009's exact Bunch--Davies expansion gives, after clearing one common source normalization,

\[
D(y)
=
2(Q+N)
+2(Q+N)y^2
-\frac43Py^3
+O(y^4),
\qquad
y=k\eta.
\]

Since

\[
a^2\partial_\eta
=
\frac{k^3}{H^2}y^{-2}\partial_y,
\]

the mixed correlator has Laurent expansion

\[
\boxed{
a^2\partial_\eta D
=
\frac{k^3}{H^2}
\left[
\frac{4(Q+N)}{y}
-4P
+O(y)
\right].
}
\]

## Separation result

The pole row is

\[
(0,4,4)
\]

in the basis \((P,Q,N)\), so it repeats the ordinary field-field freeze-out combination \(Q+N\). The Laurent finite part is

\[
\boxed{(-4,0,0),}
\]

and therefore isolates \(P=\operatorname{Re}C\).

Together, the field-field freeze-out value and the finite mixed correlator have rank two on the physical readout coordinates

\[
(P,Q+N).
\]

## Narrow conclusion

The third normal grade is not merely formal. It is the finite coefficient of a source-defined canonical field--momentum correlator after separating its universal freeze-out pole.

However, this does **not yet** establish a canonical physical observable. The source paper derives the bulk and initial-state renormalization but does not explicitly prove that finite local boundary counterterms cannot shift this mixed finite part. Therefore the current result is typed as

\[
\boxed{
\text{canonical readout candidate}
\quad\text{not yet}\quad
\text{scheme-independent observable}.
}
\]

## Carrier classification

No new carrier incidence appears. The mixed readout combines the existing initial hypersurface, its canonical conormal direction, and the completed Gaussian coefficient connection from Entry 2011.

## Next falsifier

Inventory the finite quadratic boundary counterterms admitted by spatial symmetries, Schwinger--Keldysh normalization, and the fixed-state connection. Compute their contribution to the Laurent finite row. If they span \((-4,0,0)\), the third-grade readout is scheme-dependent. If they cannot shift it, the mixed finite part is a canonical physical observable.

## Durable artifact

- `research/benincasa/checkers/de_sitter_mixed_momentum_readout.py`
- `research/benincasa/results/de-sitter-mixed-momentum-readout.json`

## Provenance

- Collins--Holman--Vardanyan, arXiv:1408.4801v1, Eqs. (3.1), (4.4), and (5.5)--(5.9);
- Collins, arXiv:1309.2656v1, Eq. (2.20);
- Entries 2009 and 2011;
- allocator claim `seqclaim-d48f75411c070d97141c1974`.

Epistemic graph event: `ev-000000002740-b631bda4-df4b-499a-972d-304b9754a498`.
