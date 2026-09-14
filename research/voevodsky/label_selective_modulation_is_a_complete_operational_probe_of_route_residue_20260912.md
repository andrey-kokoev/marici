# Label-selective modulation is a complete operational probe of route residue

## Question

What is the weakest explicit measurement interface that would detect every route-residue cycle and generate a positive form from measured responses?

## Claim boundary

If individual source-labelled edge channels can be modulated before common-history synthesis, the resulting differential probes are jointly faithful on the completed cycle sector. Their response Gram form is positive definite there. This is a mathematical interface theorem, not evidence that such label-selective modulation is physically available or that its noise is independent.

## Edge-selective differential probes

For each source edge \(e\), let \(D_e\) be the coordinate selector and let

\[
A_e=B D_e.
\]

For a coefficient packet \(c\),

\[
A_ec=c_e b_e,
\]

where \(b_e\in L^2(\mathbb R_+)\) is the history column of that interval. Every arithmetic interval has positive length. The explicit completed atom is nonzero on the interval support, and for sufficiently large separation its shifted factor has fixed positive sign. Hence \(b_e\) is not the zero function.

If \(z\neq0\) is a cycle, some coefficient \(z_e\neq0\). Then

\[
A_ez=z_eb_e\neq0.
\]

Therefore

\[
\bigcap_e\ker(A_e|_{\mathcal Z})=\{0\}.
\]

The edge-selective family detects all route residue without choosing a forest.

## Bounded completed measurement family

Choose a mathematical damping parameter \(\gamma>0\) and amplitudes

\[
\alpha_e=e^{-\gamma W(e)}.
\]

Define the direct-sum differential readout

\[
\mathcal A_\gamma c=(\alpha_eA_ec)_e
\in\ell^2_e(L^2(\mathbb R_+)).
\]

The column estimate and projective source bounds make \(\mathcal A_\gamma\) continuous. Because every \(\alpha_e\) is nonzero, it remains injective on \(\mathcal Z\).

The damping is an analytic device ensuring a bounded infinite probe family. It is not a physical attenuation law unless independently realized.

## Response and noise forms

The response Gram form is

\[
Q_\gamma(z)
=
\sum_e\alpha_e^2|z_e|^2\|b_e\|_2^2.
\]

It is strictly positive for every nonzero cycle. If experiments provide positive noise variances \(\sigma_e^2\), the corresponding diagonal Fisher form is

\[
Q_{\gamma,\sigma}(z)
=
\sum_e
\frac{\alpha_e^2}{\sigma_e^2}
|z_e|^2\|b_e\|_2^2.
\]

This becomes a physically sourced covariance or information metric only when the modulation amplitudes, readout normalization, and noise law are measured or derived.

## Smallest falsification test

Use the four-edge multiplicative rectangle cycle. Verify that the unmodulated sum has zero common history. Modulate one of its four labelled channels and test the differential history. The interface predicts a nonzero response proportional to that edge's coefficient and history column.

Failure under a verified edge-selective modulation would refute one of the premises: the channel was not actually isolated, the source loading differs from the declared linear model, or the readout does not implement common history. Failure because the apparatus can modulate only the already-codiagonalized history would instead show that the physical interface factors through \(B\) and cannot observe route residue.

## Disposition

The missing physical covariance has been reduced to a concrete laboratory/source question: can one independently modulate and read at least a jointly faithful family of shell/theta-labelled channels before codiagonalization? An affirmative calibrated implementation generates a positive cycle form; absent that implementation, \(Q_\gamma\) remains a mathematical probe metric.
