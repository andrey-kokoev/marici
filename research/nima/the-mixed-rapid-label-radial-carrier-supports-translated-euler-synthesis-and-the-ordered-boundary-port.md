# The mixed rapid label--radial carrier supports translated Euler synthesis and the ordered boundary port

## Mixed test carrier

Let

\[
\mathcal E
=
\mathcal S_{\mathrm{lab}}\widehat\otimes_\pi
\mathcal S_{\exp}(\mathbb R),
\]

where

\[
\mathcal S_{\mathrm{lab}}=\bigcap_{a>0}\ell^2(\mathbb N,n^{2a})
\]

and `S_exp(R)` consists of functions whose two-sided exponential weighted
`L2` seminorms are finite for every positive weight. The projective tensor
product retains label and radial variables before scalar aggregation.

## Translation estimate

For radial translation `tau_L f(t)=f(t-L)`,

\[
p_a(\tau_Lf)\le e^{a|L|}p_a(f).
\]

At an arithmetic displacement `L=log n`, this becomes

\[
p_a(\tau_{\log n}f)\le n^a p_a(f).
\]

Therefore logarithmic translation costs only polynomial label growth. The
rapid-label seminorms absorb that cost.

More generally, if `b_n` has polynomial-logarithmic growth, then on elementary
vectors the synthesis

\[
\Sigma_b(c\otimes f)
=
\sum_{n\ge1}b_nc_n\tau_{\log n}f
\]

converges in every weaker exponential radial seminorm after choosing a
stronger label seminorm. It consequently extends continuously from the
projective mixed carrier to the radial test space. The same argument applies
to primitive, prime-power, von Mangoldt, and full logarithmic interval rows.

## Ordered boundary carrier

The order operator does not preserve the rapidly decaying radial space: its
outputs retain endpoint constants. Introduce instead

\[
\mathcal B_{\mathrm{ord}}
=
\{h:h'\in\mathcal S_{\exp}(\mathbb R),\ h(-\infty),h(+\infty)
\text{ exist}\},
\]

with the derivative seminorms together with the two endpoint traces. For
`g` in `S_exp(R)`,

\[
(Sg)'=-2g,
\qquad
(Sg)(-\infty)=\int_{\mathbb R}g,
\qquad
(Sg)(+\infty)=-\int_{\mathbb R}g.
\]

Exponential Cauchy--Schwarz bounds the integral by any positive weighted
seminorm. Hence

\[
S:\mathcal S_{\exp}(\mathbb R)\longrightarrow\mathcal B_{\mathrm{ord}}
\]

is continuous. Its two endpoint traces are opposite, so the constant-mode
packet is retained with the required reciprocal oddness rather than silently
discarded.

Fourier transformation sends the derivative coordinate to the regular
frequency channel and the endpoint jump to the principal-value/zero-mode
boundary pair. Thus the Hardy port descends on `B_ord`, whereas value sampling
alone would not.

## Constructed mixed arrow

Combining translated Euler synthesis with the continuous ordered map gives a
typed continuous arrow

\[
\mathcal E
\xrightarrow{\Sigma_b}
\mathcal S_{\exp}(\mathbb R)
\xrightarrow{S}
\mathcal B_{\mathrm{ord}}.
\]

This constructs a common carrier for labelled arithmetic synthesis,
logarithmic translation, the ordered inverse derivative, and its endpoint
packet.

It does not prove that every authorized cutoff or reciprocal route induces
the same polarized Green-current row. That equality is now the remaining
comparison-cell condition rather than a continuity or carrier-existence
problem.
