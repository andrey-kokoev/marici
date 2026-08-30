# Boundary-kinetic RG selector gate: WP937

## Question

Can renormalization of WP936's exchange-even boundary coefficient supply the
missing completion-stable selector?

## Declared authority boundary

The admitted `SU(4)` gauge-Higgs packet specifies the bulk group, orbifold
parity, link realization, and allowed boundary operator ring.  It does not
yet specify a beta function for the common boundary kinetic coefficient
`tau`.  The following flows are therefore exact typing alternatives, not
assertions about physical evolution of the current source.

The parameter `t` is an RG scale coordinate.  No physical-time or causal
interpretation is used.

## Additive running

For

\[
\frac{d\tau}{dt}=b,
\]

the solution is

\[
\tau(t)=\tau(0)+bt.
\]

Two initial packets remain separated by the same difference at every finite
scale.  This is transport, not selection.

## Homogeneous running

For

\[
\frac{d\tau}{dt}=a\tau,
\]

the solution is `tau(t) = tau(0) exp(a t)`.  Zero is a fixed point, but it is
attractive only after the direction of the RG limit and the sign of `a` are
independently fixed.  Every finite-scale map is invertible and retains the
initial coefficient.

## Affine attraction

For

\[
\frac{d\tau}{dt}=a\tau+b,
\qquad a\ne0,
\]

the fixed point is

\[
\tau_*=-\frac{b}{a}.
\]

This is genuine selector architecture when the admitted limit is attractive.
It does not predict a number until the complete source derives `a` and `b`.
The equally attractive hostile systems

\[
\frac{d\tau}{dt}=-\tau+1,
\qquad
\frac{d\tau}{dt}=-\tau+2
\]

select `tau = 1` and `tau = 2`.  Stability alone therefore has no numerical
authority.

## Completion gate

WP935 shows that the admitted matter completion changes the full spectral
index.  The same completion must be included when deriving the boundary beta
coefficients.  A fixed point calculated in the pure-vector stratum cannot be
promoted unless `-b/a`, its attractive domain, and threshold matching are
unchanged or transform by a separately derived common-frame map throughout
every admitted completion.

## Classification

The current source-authorized RG probe family contains no specified
boundary-beta operation, so it induces the indiscrete contextual partition
on candidate beta systems.  Additive and finite homogeneous flows are
transporters.  An affine attractive flow would be a conditional selector,
not a rigidifier, but its selected value and completion stability are
undeclared.

The smallest exact falsifier of selection-by-attractiveness is the pair of
flows with fixed points one and two.  The remaining physical-instrument gate
is unchanged: WP770's two momentum ports require production and decay
channels with a nonsingular uncertainty-completed response and can identify,
but cannot authorize, the selected coefficient.

## Result

RG dynamics is a viable form for the missing arrow, but no such arrow is
presently source-authorized.  The flavor frontier becomes the derivation of a
completion-stable boundary beta system in the same source frame as the
`physical16` instrument.

Reproduce with:

    uv run python research/flavor/checkers/wp937_boundary_kinetic_rg_selector_gate.py

Generated result:
`research/flavor/results/wp937_boundary_kinetic_rg_selector_gate.json`.
