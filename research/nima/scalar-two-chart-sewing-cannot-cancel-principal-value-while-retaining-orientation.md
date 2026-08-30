# Scalar two-chart sewing cannot cancel principal value while retaining orientation

## Exact coefficient audit

For the two universal front charts,
\[
\widehat a_-
=
-\frac12\delta_0
+
\frac12\,\operatorname{pv}\frac{1}{\pi i\xi},
\qquad
\widehat a_+
=
-\frac12\delta_0
-
\frac12\,\operatorname{pv}\frac{1}{\pi i\xi}.
\]

A scalar chart combination
\[
c_-a_-+c_+a_+
\]
has boundary coefficients
\[
d=-\frac12(c_-+c_+),
\qquad
p=\frac12(c_--c_+).
\]

Exact principal-value cancellation requires
\[
p=0,
\]
hence
\[
c_-=c_+.
\]
But this is precisely the diagonal chart direction. The anti-diagonal orientation coordinate \(c_--c_+\) vanishes.

Therefore:

> Any scalar linear combination of the two universal charts that cancels the principal-value distribution also kills the reciprocal odd orientation carried by that distribution.

## Consequence

The desired nonperturbative cancellation cannot occur by scalar summation of the two chart representatives before the odd port is retained. A scalar relative finite part that makes the primitive lane convergent by setting the total principal-value coefficient to zero destroys the constructor coordinate needed for the Adams seam orientation.

This is stronger than the moment no-go:

- finite moment subtraction leaves divergence;
- all-moment subtraction on one compact front erases the front;
- exact scalar cancellation between the two universal charts erases their odd anti-diagonal class.

## Minimal faithful target

The two-chart sewing must first land in a typed two-port object,
\[
(d,p)
\in
\mathcal B_{\mathrm{even}}\oplus\mathcal B_{\mathrm{odd}},
\]
or equivalently retain the chart pair modulo only source-authorized overlap relations.

Arithmetic completion may regularize the odd port through a relative or vector-valued construction, but it cannot replace that port by the scalar equation \(p=0\).

A possible legitimate pattern is
\[
p
\longmapsto
(p_{\mathrm{sing}},p_{\mathrm{res}})
\]
with a source-derived subtraction satisfying:

1. \(p_{\mathrm{sing}}\) cancels against a separately typed archimedean or overlap channel;
2. \(p_{\mathrm{res}}\neq0\) carries reciprocal orientation;
3. the pair, not either scalar separately, has a continuous completed readout.

No such splitting follows from the universal \(2\times2\) chart matrix alone.

## Hostile

Take \(c_-=c_+=1\). The principal-value terms cancel exactly and the result is the constant even wall. Every scalar convergence test passes, but the odd observer is identically zero.

Conversely, take \(c_-=-c_+=1\). The even delta wall cancels and the odd principal-value coordinate is maximal, but its primitive scalar aggregation remains the unresolved divergent lane.

The two desired properties occupy complementary chart directions.

## Revised frontier

The next source theorem must introduce a third typed coordinate or a relative extension before scalarization:
\[
\text{two chart coefficients}
\longrightarrow
(\text{even overlap},\text{odd singular moment},\text{odd residual})
\longrightarrow
\text{completed relative history}.
\]

The finite three-coordinate model is therefore not optional bookkeeping. It is the minimum rank required to separate cancellation from retained orientation. Its incidence and analytic remainder still require source derivation.
