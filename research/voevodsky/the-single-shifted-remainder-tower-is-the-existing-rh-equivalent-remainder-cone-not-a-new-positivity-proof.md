# The single shifted remainder tower is the existing RH-equivalent remainder cone, not a new positivity proof

## Deduplication result

The recently derived one-time tower

\[
H_r^{R,+}(t_0)
=
(
(-1)^{i+j+1}
R^{(i+j+1)}(t_0)
)_{0\le i,j\le r}
\]

is the differential/Stieltjes presentation of the remainder cone already isolated in prior Grothendieck research.

The sampled presentation uses

\[
a_n
=
R(t+nh)
-
R(t+(n+1)h)
\]

and requires

\[
(
a_{i+j}
)_{0\le i,j\le r}
\succeq0
\]

for every rank, mesh, and base point.

As \(h\downarrow0\), the first localizer divided by \(h\) converges to

\[
-
R'(t),
\]

and higher polynomial polarizations recover the derivative Hankel tower. Conversely, heat-semigroup analyticity and finite-difference integration recover sampled localizers from the derivative hierarchy.

Thus the two formulations carry the same unresolved positivity content after the declared analytic conformance hypotheses.

## Existing endpoint extraction

Prior work already proves the abstract implication

\[
\text{remainder Hankel positivity}
+
	ext{completed heat decay}
\Longrightarrow
	ext{exact endpoint atom}.
\]

The Christoffel leverage formulation is a useful operator interpretation of this implication, but it does not weaken the remainder positivity hypothesis.

In sampled coordinates, the endpoint atom lies at

\[
y_E
=

e^{h/4}.
\]

In differential moment coordinates, it lies at

\[
x_E
=
-
\frac14.
\]

These are related by

\[
y_E
=

e^{-hx_E}.
\]

The two endpoint extraction theorems are therefore the same spectral atom in exponential and infinitesimal coordinates.

## Existing equivalence boundary

Prior research establishes that the all-rank remainder cone, together with the completed source bridge, is RH-equivalent. It is not an auxiliary inequality expected to follow from already known gamma or prime estimates.

In particular, the following do not prove it:

1. positivity of selected diagonal Laguerre directions;
2. broad-smoothing order-zero positivity;
3. finite-rank numerical scans;
4. sectorwise gamma and prime estimates;
5. endpoint asymptotics alone;
6. formal moment reconstruction from the target matrices.

Any unconditional proof of

\[
H_r^{R,+}(t_0)
\succeq0
\quad
\text{for every }r
\]

would already prove the spectral statement.

## Narrowest equivalent source target

The prior Loewner reduction supplies a more compressed equivalent target. Define

\[
t
=
(
s-1/2
)^2
\]

and

\[
F(t)
=
\frac{
4s(s-1)
}
{
2s-1
}
\frac{
\Xi'(s)
}
{
\Xi(s)
}.
\]

After exact endpoint cancellation, the remaining Pick target is

\[
\boxed{
\operatorname{Im}
\left\{
\frac{
4s(s-1)
}
{
2s-1
}
\left[
-
\frac12
\log\pi
+
\frac12
\psi(s/2)
+
\frac{
\zeta'(s)
}
{
\zeta(s)
}
\right]
\right\}
\ge0
}
\]

on the image of the upper \(t\)-half-plane.

This is the endpoint-reduced gamma--prime form of the same positivity gate.

## Rotor interpretation of the Pick target

A hostile Blaschke rotor contributes a nonreal or forbidden pole to the Loewner/Pick function. In the divided-difference kernel, that pole contributes the same finite-rank negative model-space direction previously identified as \(K_B\).

Hence the following are presentations of one obstruction:

1. negative shifted remainder Hankel minor;
2. failure of the Loewner kernel to be positive;
3. failure of the Pick imaginary-part inequality;
4. nonzero Krein--Langer model space;
5. hostile rotor in the terminal tetrahedral slab.

Changing presentations does not remove the RH-strength sign problem.

## Viable next actions from prior research

Repository search leaves three legitimate actions.

### Direct coupled Pick attack

Seek an integral representation coupling

\[
\frac12
\psi(s/2)
+
\frac{
\zeta'(s)
}
{
\zeta(s)
}
\]

before taking imaginary parts. Separate sign estimates are known to fail.

### Certified falsifier search

Use rigorous complex interval arithmetic on compact subsets of the mapped upper half-plane. A strict negative enclosure would falsify the proposed Pick route. Positive finite grids remain diagnostic only.

### New source-derived Gram factor

Construct a feature map for the Loewner divided-difference kernel from independent arithmetic operations. Defining the feature by polarizing the target kernel is circular.

No fourth route is currently supported by prior research.

## Disposition

The single shifted gamma--prime tower is a clean final formulation, but it is not new positive capacity:

\[
\boxed{
	ext{shifted remainder tower}
=
	ext{sampled remainder cone}
=
	ext{Loewner/Pick gate}
=
	ext{hostile-rotor exclusion}.
}
\]

Further algebraic compression of this tower should stop unless it produces an independently positive source factor, a rigorous falsifier, or a genuinely new coupled Pick estimate.
