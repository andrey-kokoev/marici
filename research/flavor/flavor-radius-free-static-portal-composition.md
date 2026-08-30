# The half twist and first KK level remove the radius, not the gauge normalization: WP771

## Question

Can the source-selected half twist, separated-boundary gauge exchange, and
two-port readout be composed into one radius-independent portal prediction?

## Common five-dimensional identification

On an interval of length

\[
\ell=\pi R,
\]

WP753 selects the half twist

\[
\omega=\frac12.
\]

Take the first massive vector KK level (N=1). The soft and vector masses are

\[
m_{\mathrm{soft}}^2=\frac{1}{4R^2},
\qquad
M_V^2=\frac{1}{R^2}.
\]

Their nondecoupling ratio is

\[
\epsilon=\frac15,
\]

and the dimensionless propagation length is

\[
M_V\ell=\pi.
\]

Both quantities are independent of (R). In particular, the static
boundary-to-boundary shape appearing in WP769 is

\[
M_VG_0(0,\ell)=\frac{1}{\sinh\pi}.
\]

The radius is therefore not the surviving dimensionless magnitude fiber in
this composed branch.

## Portal and readout

The ordered nondecoupling contrast remains

\[
\Delta=\frac{g_*^2}{10}.
\]

WP769 protects its static exchange from quadratic gauge-invariant boundary
completion, while WP770 reconstructs the finite quadratic response through
two calibrated momentum ports. These are compatible operations: selection,
threshold transport, and readout are not being identified with one another.

## Exact remaining source fiber

The gauge normalization is still free. The two packets

\[
g_*^2=1
\]

and

\[
g_*^2=2
\]

share the half twist, KK level, radius cancellation, static protection, and
readout architecture, but predict (1/10) and (1/5).

Nor does the present matter packet close this gate. WP754 finds a positive
spectral index for the link-only bulk lift, while putting the portal operands
in the bulk reverses its sign. WP738 exhausts the compulsory-mediator
gauge-Yukawa branches and finds no physical interacting fixed point.

## Classification

The composed architecture is now a conditional sign and ratio selector, a
radius-independent static threshold theorem, and a jointly faithful formal
readout. It is not a completed source explanation. The missing constructor is
sharply joint: one anomaly-complete five-dimensional localization must both
produce the positive spectral measure and yield an isolated interacting gauge
normalization. Choosing the favorable lift and borrowing a fixed point from a
different matter packet would violate source-frame composition.

After that constructor exists, its finite transfer must still be realized in
actual `physical16` channels with the WP770 uncertainty rank.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp771_radius_free_static_portal_composition.py

Generated result:
research/flavor/results/wp771_radius_free_static_portal_composition.json
