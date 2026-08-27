# Separated-boundary exchange removes the contact term but leaves a completion fiber: WP768

## Question

Can source locality repair WP767 by forbidding the additive Kähler boundary
while retaining a calculable asymmetric portal?

## Local source grammar

Place the two flavor sectors on disjoint endpoints of a local interval of
length (ell). Let a single bulk field of mass (m>0) couple to their endpoint
currents with strengths (h_0) and (h_L). A local ultraviolet counterterm
cannot contain fields supported only at both disjoint endpoints. The direct
cross-boundary Kähler contact is therefore absent by source locality, rather
than set to zero after matching.

The complete local grammar still permits endpoint self-operators. Encode the
quadratic boundary completion by Robin data

\[
u'(0)=a u(0),
\qquad
u'(\ell)=-b u(\ell),
\qquad
a,b\geq0.
\]

## Exact nonlocal exchange

For the bulk operator (-\partial_y^2+m^2), the endpoint Green function is

\[
G(0,\ell)
=\frac{1}{
\left(m+ab/m\right)\sinh(m\ell)
+(a+b)\cosh(m\ell)}.
\]

The induced portal is

\[
\lambda_{0L}=-h_0h_LG(0,\ell).
\]

For passive boundary completion the denominator is positive. Once the
relative source coupling orientation is fixed, every admitted completion
therefore preserves the exchange sign. This is a genuine improvement over
WP767: the additive cross-boundary contact is not an allowed local operation.

## Hostile completion pair

Locality does not choose the endpoint self-action. At (m=\ell=1) and (b=0),

\[
a=0\;\Longrightarrow\;G(0,1)=\frac{1}{\sinh 1},
\]

while

\[
a=1\;\Longrightarrow\;G(0,1)=e^{-1}.
\]

Both completions have the same separated sectors, bulk equation, unique
mediator, and portal sign. Their magnitudes differ because a legal local
endpoint operator changes the nonlocal propagator.

## Classification

Separated-boundary locality converts the arbitrary additive threshold of
WP767 into a narrower boundary-condition matching fiber. It protects the sign
against passive local completion but does not fix the magnitude, compactification
clock, endpoint couplings, RG basin, or instrument.

The next source principle must derive the boundary conditions rather than
choose them. Gauge symmetry or a unique variational boundary action is a
candidate only if its complete boundary operator ring leaves no response-changing
coefficient. It must then fix (m\ell) and the physical normalization and
compose with a calibrated `physical16` response.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp768_separated_boundary_exchange_completion_fiber.py

Generated result:
research/flavor/results/wp768_separated_boundary_exchange_completion_fiber.json
