# 2822 — The Normal-Order Rule Predicts the Enlarged Eight-Section Fiber

## Predeclared prediction

Before constructing the all-soft Koszul normal form, graph event 4366 froze the full eight-section packet

\[
(q_{g1},q_{g2},q_{g3},q_{g12},q_{g23},q_{g31},q_{G23},q_{G31}).
\]

Its source incidence map to \(\langle a,b\rangle\) has rank two. Entry 2819 therefore predicted

\[
8-2=6
\]

first-normal generators and one order-two Cayley–Menger generator. The predicted exterior grading was

\[
(1,7,21,35,35,21,7,1),
\]

with total rank \(128\).

## Independent normal-form calculation

At the all-soft origin the eight marked forms specialize to

\[
(b,a,a+b,a+b,b,a,a,b).
\]

A source-labelled change of generators with determinant \(-1\) transforms this sequence to

\[
(a,b,0,0,0,0,0,0).
\]

The six zero marked directions are

\[
\begin{aligned}
r_3&=e_{g3}-e_{g2}-e_{g1},\\
r_{12}&=e_{g12}-e_{g2}-e_{g1},\\
r_{23}&=e_{g23}-e_{g1},\\
r_{31}&=e_{g31}-e_{g2},\\
r_{G23}&=e_{G23}-e_{g2},\\
r_{G31}&=e_{G31}-e_{g1}.
\end{aligned}
\]

Together with \(e_K\), these give exactly the predeclared seven-generator exterior algebra and rank \(128\).

## Appraisal

This is a genuine source enlargement rather than another deletion of the five-section family, and the frozen prediction passed exactly. It strengthens the rule

\[
\text{normal-order signature}
=
\text{incidence nullity}
+
\text{discriminant valuation}.
\]

It remains within the same three-site source geometry. Consequently it is an intermediate confirmation, not yet the independent-graph falsifier requested by the Deutschian programme.

## Durable artifacts

- `research/benincasa/check_nine_master_full_marked_all_soft_signature.py`
- `research/benincasa/nine-master-full-marked-all-soft-signature.json`
