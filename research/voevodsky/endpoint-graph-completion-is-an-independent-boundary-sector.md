# Endpoint graph completion is an independent boundary sector

## Question

What is the minimal completion that retains the order topology while making the source-required endpoint evaluation continuous?

## Claim boundary

Completing the Gaussian span in the graph norm of endpoint evaluation produces an order bulk plus an independent one-dimensional endpoint sector. The endpoint rank-one form is bounded there. This constructs the minimal endpoint-controlling carrier, not a common gamma-plus-prime or Weil form domain.

## Graph norm

On the algebraic Gaussian span \(D_G\), define

\[
\lVert f\rVert_E^2
=
\lVert f\rVert_{\rm ord}^2
+|L_E(f)|^2.
\]

The graph embedding is

\[
\Gamma_E:
D_G
\longrightarrow
\mathcal H_{\rm ord}\oplus\mathbb C,
\qquad
f
\longmapsto
(f,L_E(f)).
\]

Its graph-norm completion is the closure of this image.

## Vertical boundary vector

For

\[
f_a=e^{-a/4}g_a,
\]

one has

\[
f_a\longrightarrow0
\]

in \(\mathcal H_{\rm ord}\), while

\[
L_E(f_a)=1.
\]

Therefore

\[
\Gamma_E(f_a)
\longrightarrow
(0,1).
\]

The completion contains a nonzero pure endpoint vector independent of the order bulk.

Because scaled copies of this sequence realize every vertical scalar and the Gaussian span is dense in the horizontal order space, the completed carrier is

\[
\mathcal H_E
\cong
\mathcal H_{\rm ord}
\oplus
\mathbb C_E.
\]

The second summand is not a value of a continuous functional on the first. It is a newly completed boundary coordinate.

## Endpoint form

The source-required endpoint contribution becomes

\[
q_E(f,z)
=
(e^{h/4}-1)|z|^2.
\]

It is bounded and positive on \(\mathcal H_E\):

\[
0
\leq
q_E(f,z)
\leq
(e^{h/4}-1)
\lVert(f,z)\rVert_E^2.
\]

Thus the nonclosability residual is repaired by extending the carrier rather than deleting the source endpoint term.

## Coherence interpretation

The endpoint residual has revealed a new realization sector. The higher coherencer is the graph-completion map

\[
D_G
\longrightarrow
\mathcal H_{\rm ord}
\oplus
\mathbb C_E,
\]

not a scalar counterterm on \(\mathcal H_{\rm ord}\).

The endpoint observer and order observer become coordinate projections of one enlarged realization. Neither projection alone reconstructs the other.

## Remaining gates

This completion proves only:

- continuity of endpoint evaluation;
- boundedness of the endpoint rank-one form;
- density of the original Gaussian span in the augmented norm by construction.

It does not prove that the corrected gamma-plus-prime remainder form is closable or semibounded on \(\mathcal H_E\). It also does not identify \(\mathcal H_E\) with a Weil domain.

## Disposition

`endpoint_controlling_domain` is inhabited by \(\mathcal H_E\). The first remaining gate is a closable semibounded gamma-plus-prime form on this augmented carrier. No RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_endpoint_graph_completion.py`
- `research/voevodsky/results/endpoint_graph_completion.json`
