# 1098 — The Exceptional Rank-Four Object Glues Across Both Rees Charts

## Record

Entry 1097 reconstructed the complete rank-four quotient connection on the
\(p\neq0\) chart of the joint Rees center

\[
(p,q)=(u,v-2).
\]

The complementary \(q\neq0\) chart has now been constructed and reduced
independently from the frozen rank-twelve source equations.

Sequence claim: `seqclaim-c0cbc11d430e145e5b58dc08`.

## Independent chart census

Write

\[
s=\frac qp,
\qquad
r=\frac pq,
\qquad
r=s^{-1}
\]

on the overlap.  In each of two independent 61-bit fields, the \(q\)-chart
reduction gives

\[
\operatorname{rank}(d_{\rm exact})=107,
\qquad
\operatorname{rank}(d_{\rm all})=111,
\]

and hence the same rank-four quotient

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_4).
\]

All reconstructed entries agree between the two fields and pass nine unused
verification points per field.

## Rees transition

The labelled Rees orders in the source \(e_5\) frame are

\[
(-2,-1,-1,0).
\]

Therefore the overlap transition is forced to be

\[
\boxed{
G(r)=\operatorname{diag}(r^{-2},r^{-1},r^{-1},1).
}
\]

The independently reconstructed source-frame transition on the \(q\)-chart is

\[
e_5
=
-\frac{24r^2}{(1+3r)(1+3r^2)}e_4.
\]

It agrees with the \(p\)-chart transition after applying \(r=s^{-1}\) and the
labelled Rees scaling of \(e_4\).

## Connection cocycle

Using the row convention in which row \(i\) expresses the derivative of basis
element \(i\), the required overlap identity is

\[
A_q(r)
=
\frac{ds}{dr}
G^{-1}A_p(s)G\big|_{s=1/r}
-
G^{-1}\frac{dG}{dr}.
\]

Exact Symbolica reduction gives

\[
\boxed{
A_q-
\left(
\frac{ds}{dr}G^{-1}A_pG-G^{-1}dG/dr
\right)
=0
}
\]

entry by entry.  The checker reports zero defects.

## Deutsch--Popperian verdict

The conjecture that Entry 1097's rank-four exceptional connection might fail
to descend across the second Rees chart is falsified.  The independently
constructed charts glue by the source-labelled Rees transition, and the
overlap introduces no new pole divisor.

Thus the first exceptional center closes, at the tested associated-grade and
modular-connection level, as

\[
\boxed{
\text{existing joint carrier}
+
\text{globally glued rank-four coefficient object}.
}
\]

No new cosmological carrier datum is indicated.

## Epistemic status

- both chart reductions: replicated over two independent 61-bit fields;
- chartwise rational reconstruction: nine unused verification points per
  field;
- transition and cocycle: exact characteristic-zero rational algebra;
- characteristic-zero primitive witness for the chartwise source reduction:
  pending;
- new overlap support: none.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`;
- `research/benincasa/marici-gm/src/bin/rank12_u0v2_chart_cocycle.rs`;
- `research/benincasa/rank12-u0-v2-exceptional-line.json`.

Epistemic graph admission:
`ev-000000000797-f432ede8-bb91-4c99-bda3-857573e22876`.

## Next falsifier

Apply the same two-chart, source-labelled test to the next proper existing-
carrier intersection from Entry 863.  Compare its exceptional coefficient
object with this first center without identifying their coefficient systems
in advance.  A failure of chart descent would be coefficient descent failure;
only an independently required incidence divisor would count as carrier
failure.
