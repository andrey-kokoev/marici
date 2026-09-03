# Anchored zero-sum lift and its residual

## Question

Once a heat polynomial supplies prime amplitudes, how can a packet with nonzero total mass enter the zero-sum order completion, and what coherence residue does that choice create?

## Claim boundary

Any finite or suitably summable amplitude packet has an anchored zero-sum lift. Changing the anchor produces an exact dipole residual whose order norm is determined by total mass and anchor separation. The construction does not choose a source-valid anchor or construct the prime-amplitude map.

## Lift

Let arithmetic amplitudes \(a_i\) sit at ordered positive labels \(\lambda_i\), and set

\[
A=\sum_i a_i.
\]

For an auxiliary anchor label \(\lambda_*\), define

\[
\iota_{\lambda_*}(a)
=
-Ae_*+
\sum_i a_ie_i.
\]

Then

\[
\sum_j
\bigl(\iota_{\lambda_*}(a)\bigr)_j
=0,
\]

so the lifted packet belongs to the algebraic domain of the order norm.

Its cumulative-sum image is the tail of the original amplitude packet between the anchor and its labels. Thus it belongs to the completed order space exactly when that tail is square-integrable in the gap measure.

## Anchor-change residual

For two anchors \(\lambda_*\) and \(\lambda_*'\),

\[
\iota_{\lambda_*'}(a)
-
\iota_{\lambda_*}(a)
=
A(e_*-e_*').
\]

This is a single dipole. The order norm gives

\[
\left\lVert
\iota_{\lambda_*'}(a)
-
\iota_{\lambda_*}(a)
\right\rVert_{\rm ord}^2
=
2|A|^2
|\lambda_*'-\lambda_*|.
\]

Therefore anchor dependence vanishes precisely when the source amplitudes have zero total mass. Otherwise it is a controlled, nonzero coherence residual.

## Interpretation

The zero-sum condition is not administrative. It is the quotient that removes the constant mode from the conditionally positive order kernel. A source packet with nonzero mass cannot enter that quotient without pairing its mass against another sector.

The completed explicit formula already contains a candidate source of that balancing datum: the archimedean gamma and endpoint terms. But identifying either with a chosen point anchor would be an additional claim. The actual completion may require a distributed archimedean counterpacket rather than a single dipole.

Thus the source map should factor as

\[
p
\longmapsto
(a_i(t,h,p))_i
\longmapsto
\bigl(a_{\Gamma}(t,h,p),(a_i(t,h,p))_i\bigr)
\longmapsto
\mathcal H_{\rm ord},
\]

where the middle object has total mass zero by a proved completed-form identity.

## Higher-coherence test

If different decompositions assign different balancing packets, their difference is a zero-mass arithmetic--archimedean cycle. That cycle is the next residual. A higher coherencer must either identify it as exact or show that its completed-form contribution vanishes. Merely selecting an anchor hides rather than resolves this residual.

## Disposition

The second arrow into the order domain is constructed once an anchor or balancing packet is supplied. The first missing source object is sharpened to a completed prime-plus-archimedean amplitude packet with proved zero total mass. Until that identity is derived, the heat-polynomial source map remains undefined rather than merely unbounded.

## Verification

- `research/voevodsky/checkers/check_anchored_zero_sum_lift.py`
- `research/voevodsky/results/anchored_zero_sum_lift.json`
