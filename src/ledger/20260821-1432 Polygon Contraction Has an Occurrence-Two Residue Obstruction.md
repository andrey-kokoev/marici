---
author: marici.Benincasa
---

# 1432 — Polygon Contraction Has an Occurrence-Two Residue Obstruction

## Status

Exact local Poincaré-residue theorem on the contracted-edge divisor.

## Local model

Entry 1431 gives, on \(y_{\{n,1\}}=0\),

\[
q_{\{1\}}+q_{\{n\}}=q_{\{n,1\}}.
\]

Set

\[
q=q_{\{n,1\}},
\qquad
s=q_{\{1\}},
\qquad
t=q_{\{n\}}=q-s.
\]

The two source singleton poles have the local logarithmic form

\[
\Omega=\frac{ds\wedge dq}{s(q-s)}.
\]

## Endpoint residues

At the first occurrence \(s=0\),

\[
\operatorname{Res}_{s=0}\Omega=\frac{dq}{q}.
\]

At the second occurrence \(t=0\), use \(ds=dq-dt\), so

\[
ds\wedge dq=-dt\wedge dq.
\]

Therefore

\[
\operatorname{Res}_{t=0}\Omega=-\frac{dq}{q}.
\]

Consequently,

\[
\boxed{
\operatorname{Res}_{s=0}\Omega
+
\operatorname{Res}_{t=0}\Omega=0,
}
\]

while the occurrence-oriented difference is

\[
\boxed{
\operatorname{Res}_{s=0}\Omega
-
\operatorname{Res}_{t=0}\Omega
=2\frac{dq}{q}.
}
\]

## Consequence

A one-sided occurrence residue gives the target merged-wall form with unit coefficient. It breaks exchange symmetry between the two endpoint occurrences.

The exchange-resolved oriented construction is canonical over the labelled
occurrence complex, but produces a factor \(2\). Hence there is no
simultaneously

\[
\text{integral}
+
\text{exchange-symmetric}
+
\text{unit-normalized}
\]

contraction map in this local model without additional data.

The permitted repairs are sharply typed:

1. a physical current selects one occurrence;
2. an independently normalized trace/counit supplies the factor \(1/2\);
3. the target retains the occurrence-two coefficient.

None is inferred merely from graph contraction.

## Relation to cosmological partial energies

This is the same structural factor \(2\) already seen when two resolved
interface occurrences are identified on the physical diagonal. It is
therefore not evidence for a new cosmological coupling or carrier cell. It is
an occurrence-identification coefficient.

## Scope

The calculation is local and logarithmic. It does not construct the global physical contraction current, establish a period recursion, or authorize division by two.

## Next finite falsifier

Inspect the frozen five-cycle Betti chamber under \(C_5\to C_4\). Determine
whether its oriented boundary selects one endpoint occurrence or the
exchange-resolved difference. This decides between unit normalization and the
occurrence-two coefficient without fitting the answer to \(C_4\).

## Durable verification

- Checker: `research/benincasa/marici-gm/src/bin/polygon_contraction_local_residue.rs`
- Result: `research/benincasa/results/polygon-contraction-local-residue.json`
- Allocator claim: `seqclaim-678641e806f7073ceb4b7b6f`
- Epistemic graph event: `ev-000000001508-a3088fc5-4949-4bfc-9e35-ba7a5d02ef67`
