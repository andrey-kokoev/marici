# Hausdorff uniqueness supplies rational-step semigroup coherence

## Question

After constructing a positive contraction separately at each heat step, must semigroup coherence be proved as another independent infinite family?

## Rational mesh objects

Fix a base heat scale `t>0`. For each positive rational mesh `delta`, define

\[
b_n^{(\delta)}(t)=H(t+n\delta).
\]

Assume this is a Hausdorff moment sequence, with unique measure `mu_(t,delta)` on `[0,1]`:

\[
b_n^{(\delta)}(t)
=
\int_0^1y^n\,d\mu_{t,\delta}(y).
\]

Compact support makes the moment problem determinate.

## Mesh refinement

Let `delta'=delta/m`. Push `mu_(t,delta')` forward by

\[
p_m(y)=y^m.
\]

Its moments are

\[
\int y^n\,d(p_m)_*\mu_{t,\delta'}
=
\int y^{mn}\,d\mu_{t,\delta'}
=
H(t+n\delta).
\]

These are exactly the moments of `mu_(t,delta)`. Hausdorff uniqueness therefore gives

\[
(p_m)_*\mu_{t,\delta'}
=
\mu_{t,\delta}.
\]

In the multiplication models this is the canonical power compatibility

\[
Y_\delta=Y_{\delta'}^m
\]

up to the unique cyclic unitary identification.

## Finite families of rational steps

Any finite set of positive rational steps has a common refinement `delta=1/D`. Writing `h_j=m_j delta`, define

\[
Y_{h_j}=Y_\delta^{m_j}.
\]

Then

\[
Y_{h_i+h_j}=Y_{h_i}Y_{h_j}
\]

holds algebraically. Refining the denominator gives the same cyclic model by the pushforward identity above. Thus all finite rational-step coherence cells are forced by one-dimensional Hausdorff uniqueness; no independently chosen coupling is needed.

## Base-scale transport

Changing the base from `t` to `t+r delta` tilts the same measure by `y^r`:

\[
d\mu_{t+r\delta,\delta}(y)
=
y^r d\mu_{t,\delta}(y)
\]

with total mass `H(t+r delta)`. This follows from equality of all moments and compact determinacy. Hence heat-scale translation is also source-forced.

## Passage to a continuous semigroup

The rational family determines a positive contraction semigroup if continuity at zero is established from the source function:

\[
H(t+h)\longrightarrow H(t).
\]

In the cyclic representation,

\[
\|(Y_h-I)\Omega_t\|^2
=H(t+2h)-2H(t+h)+H(t),
\]

which tends to zero. Polynomial density and contractivity extend this to the cyclic space. The semigroup therefore has a nonnegative self-adjoint generator.

## Disposition

Semigroup coherence is not an additional RH-strength sign conjecture. Once every rational-mesh sequence has a positive Hausdorff measure, compact moment uniqueness forces mesh refinement, rational composition, and base-scale tilting. The only sign gate is positivity of the Hausdorff Hankel/localizing cones; source continuity closes the semigroup limit.