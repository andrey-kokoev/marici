# Anomaly descent leaves the flux lattice; an internal gauge flux is unstable: WP778

## Question

Do six-dimensional anomaly cancellation, tadpole balance, and stability make
the WP777 oriented flux \(m=3\) unavoidable?

## Anomaly descent is not a flux selector

Let \(A_6\) denote a coefficient in the local six-dimensional anomaly
polynomial. Integrating one internal field-strength insertion over the torus
gives a four-dimensional coefficient of the form

\[
A_4(m)=mA_6.
\]

Consequently,

\[
A_6=0
\quad\Longrightarrow\quad
A_4(m)=0
\qquad (m\in\mathbb Z).
\]

The anomaly condition can constrain the representation and charge packet, but
after parent cancellation its contextual equivalence class contains the whole
integer flux lattice. In particular, \(m=1\) and \(m=3\) give the same zero
anomaly readout. This is a failure of selection, not evidence for uniqueness.

This calculation is deliberately limited to local anomaly-polynomial descent.
A complete six-dimensional model must additionally check reducible
Green--Schwarz, global, fixed-point, and gravitational anomalies. Those extra
conditions may constrain the allowed source packet, but they cannot be assumed
to select the desired flux before their dependence on \(m\) is derived.

## The minimal tadpole selector relocates the integer unless sourced

The smallest integrated Bianchi or tadpole relation capable of fixing a signed
flux is

\[
c\,m+Q_{\mathrm{loc}}=0.
\]

It gives

\[
m=-\frac{Q_{\mathrm{loc}}}{c}.
\]

Thus \(m=3\) follows only if

\[
Q_{\mathrm{loc}}=-3c.
\]

This is a genuine selector only when the localized charge and coefficient are
independently compulsory consequences of the source theory. Choosing their
ratio to reproduce three merely moves the fitted integer from the flux to the
tadpole. With no localized source, the same equation selects \(m=0\), not
three. The sign of \(Q_{\mathrm{loc}}\) also carries the orientation, so an
orientation-even energy proportional to \(m^2\) cannot replace it.

## Stability defeats internal non-Abelian flux

For a charged vector in a constant magnetic field, the spin-aligned lowest
Landau state has

\[
M^2_{0,-}=|qB|-2|qB|=-|qB|.
\]

Hence a Cartan flux embedded in the non-Abelian \(SU(6)\) gauge field has a
tachyonic charged-vector mode. This agrees with the complete magnetized
\(SU(n)\) spectrum derived by
[Kojima, Okubo, and Takeda](https://arxiv.org/abs/2306.00644). The naive flux
background therefore has no stable RG basin from which to claim threshold
survival.

## Smallest surviving window

A distinct \(U(1)_F\) can carry the magnetic flux while the \(SU(6)\) vector
bosons remain neutral. That removes this particular vector tachyon, but it is
a new source theory, not a reinterpretation of the old one. It must derive:

1. an anomaly-free \(U(1)_F\) charge embedding for the complete matter packet;
2. localized sources whose quantized charges force \(Q_{\mathrm{loc}}=-3c\);
3. a stable scalar and vector spectrum for that sourced background;
4. the gauge normalization and flux-weighted threshold potential;
5. a calibrated map into generation-resolved `physical16` ports.

## Classification

Local anomaly cancellation is neither selector nor presentation rigidifier of
the flux integer. A sourced tadpole can be a selector, but only after its charge
ratio is independently derived. The current internal \(SU(6)\) realization
also fails stability. The next bounded search is therefore not another scan of
integer fluxes: it is the smallest complete external-\(U(1)_F\) source packet
whose charge lattice and tadpole equation uniquely force oriented flux three.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp778_flux_anomaly_tadpole_stability_gate.py

Generated result:
research/flavor/results/wp778_flux_anomaly_tadpole_stability_gate.json
