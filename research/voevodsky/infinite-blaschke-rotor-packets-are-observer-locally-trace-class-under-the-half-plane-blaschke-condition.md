# Infinite Blaschke rotor packets are observer-locally trace class under the half-plane Blaschke condition

## Objective

Extend the finite-rank hostile rotor transport to infinitely many symmetry-completed divisor factors.

The unlocalized infinite model-space projection generally has infinite rank and is not trace class. Nevertheless, after Mellin--Schwartz observer localization, the defect is trace class and finite-product truncations converge in trace norm under the standard half-plane Blaschke condition.

## Infinite divisor packet

Let

\[
z_j
=
\gamma_j+ib_j,
\qquad
b_j>0,
\]

be a discrete sequence in the upper half-plane. Associate the elementary factor

\[
b_j(z)
=
\frac{
z-z_j
}
{
z-
\overline{z_j}
}.
\]

Assume the half-plane Blaschke condition

\[
\boxed{
\sum_j
\frac{
b_j
}
{
1+
\gamma_j^2+
b_j^2
}
<
\infty.
}
\]

Then the ordered product

\[
B(z)
=
\prod_j
b_j(z)
\]

defines an inner function up to the standard unimodular normalization.

For centered symmetry completion, include paired zeros

\[
\gamma_j+ib_j,
\qquad
-
\gamma_j+ib_j.
\]

## Model-space defect

Let

\[
K_B
=
H^2_+
\ominus
BH^2_+.
\]

Then

\[
\boxed{
\Pi-
M_B
\Pi
M_B^*
=
P_{K_B}.
}
\]

If the product has infinitely many factors, \(K_B\) is generally infinite dimensional, so

\[
\operatorname{Tr}
P_{K_B}
=
\infty.
\]

Thus no unlocalized global trace-class claim is available.

## Takenaka basis

Let

\[
B_{j-1}
=
\prod_{k<j}
b_k.
\]

The ordered Takenaka vectors

\[
e_j(t)
=
B_{j-1}(t)
\sqrt{
\frac{b_j}{\pi}
}
\frac1{
t-
\gamma_j+i b_j
}
\]

form an orthonormal basis of the divisor-generated part of \(K_B\), with the usual completeness qualification if an additional singular inner factor is present.

Because

\[
|B_{j-1}(t)|=1
\]

for almost every real \(t\),

\[
\boxed{
|e_j(t)|^2dt
=
\frac1\pi
\frac{
b_j
}
{
(t-
\gamma_j)^2+
b_j^2
}
\,dt.
}
\]

Each rotor blade therefore retains its elementary Poisson phase-energy measure even after all preceding factors are inserted.

## Observer localization

Let \(m\) be a Mellin--Schwartz boundary multiplier. Define

\[
T_{B,m}
=
M_m^*
P_{K_B}
M_m.
\]

This is positive. Its formal trace is

\[
\operatorname{Tr}
T_{B,m}
=
\sum_j
\|M_m^*e_j\|_2^2
=
\sum_j
\int
|m(t)|^2
\frac1\pi
\frac{b_j}{(t-
\gamma_j)^2+b_j^2}
\,dt.
\]

Whenever this sum is finite, \(T_{B,m}\) is trace class and the displayed sum is its trace norm.

## Blaschke-condition estimate

For a Schwartz multiplier \(m\), split the Poisson integral into a fixed compact region and its rapidly decaying complement.

On a fixed compact interval \(|t|\le R_0\), factors with large \(|z_j|\) satisfy

\[
\frac{b_j}{(t-
\gamma_j)^2+b_j^2}
\le
C_{R_0}
\frac{b_j}{1+
\gamma_j^2+b_j^2}.
\]

The sum over \(j\) is finite by the Blaschke condition.

Outside the compact interval, Schwartz decay of \(m\) controls factors whose centers lie near \(t\). A shell decomposition gives convergence provided the divisor counting and \(b_j\)-weights have at most polynomial growth, as is the case for the symmetry-completed hostile packets under consideration.

Hence

\[
\boxed{
\operatorname{Tr}
T_{B,m}
<
\infty
}
\]

for every Mellin--Schwartz observer under the Blaschke condition together with polynomial local counting.

## Finite-product convergence

Let

\[
B_N
=
\prod_{j=1}^N
b_j.
\]

The model spaces are nested:

\[
K_{B_N}
\subset
K_{B_{N+1}}
\subset
K_B.
\]

Therefore

\[
P_{K_{B_N}}
\uparrow
P_{K_B}
\]

strongly on the divisor-generated model space.

For localized positive operators,

\[
T_{B_N,m}
=
M_m^*
P_{K_{B_N}}
M_m
\]

and

\[
0
\le
T_{B_N,m}
\le
T_{B,m}.
\]

Moreover,

\[
\|T_{B,m}-
T_{B_N,m}
\|_1
=
\sum_{j>N}
\int
|m(t)|^2
\frac1\pi
\frac{b_j}{(t-
\gamma_j)^2+b_j^2}
\,dt
\longrightarrow
0.
\]

Thus finite rotor packets converge in observer-localized trace norm.

## Symmetry completion and dagger

For paired factors at \(\pm\gamma_j\), order each pair compatibly with centered reflection. The dagger exchanges the corresponding Takenaka blades up to the phases introduced by preceding factors.

At the level of the full model-space projection,

\[
D
P_{K_B}
D^{-1}
=
P_{K_B}
\]

when the infinite product is symmetry invariant.

The localized trace can be grouped into paired contributions

\[
\int
|m(t)|^2
(
P_{b_j,\gamma_j}(t)
+
P_{b_j,-\gamma_j}(t)
)
\,dt.
\]

The grouping is absolutely convergent, so dagger pairing commutes with the infinite sum.

## Crossing limit

Suppose a common deformation sends

\[
b_j(a)
\downarrow
0
\]

at declared crossing parameters while maintaining uniform Blaschke and polynomial-counting bounds on compact deformation sets.

For every fixed finite packet,

\[
P_{b_j(a),\gamma_j}(t)dt
\longrightarrow
\delta_{\gamma_j}.
\]

Under a uniform observer-localized tail bound, one may pass from finite packets to the infinite sum and obtain

\[
\operatorname{Tr}
T_{B(a),m}
\longrightarrow
\sum_j
|m(\gamma_j)|^2
\]

with the reflected terms included separately.

Polynomial divisor counting and Schwartz decay make the limiting atomic sum finite.

This interchange requires uniform control; pointwise convergence of each factor alone is insufficient.

## Semilocal cutoff transport

For each finite product, exact Hardy recentering transports the model-space projection by unitary conjugation:

\[
P_{
\Lambda,
\chi,N
}^{rot}
=
\mathcal U_\chi^*
U_L
M_{
\Gamma_\chi
}
P_{
K_{B_N}
}
M_{
\Gamma_\chi
}^*
U_L^*
\mathcal U_\chi.
\]

Define the infinite transported projection by replacing \(P_{K_{B_N}}\) with \(P_{K_B}\).

Unitary conjugation preserves strong convergence and localized trace norms. Therefore

\[
M_m^*
P_{
\Lambda,
\chi,N
}^{rot}
M_m
\longrightarrow
M_m^*
P_{
\Lambda,
\chi
}^{rot}
M_m
\]

in trace norm for every fixed Mellin--Schwartz observer.

The bound is independent of cutoff after exact recentering.

## Relative current

The infinite projection defect realizes the sum of the local Blaschke logarithmic currents. Observer localization gives an absolutely convergent trace formula

\[
\operatorname{Tr}
\left(
M_{|m|^2}
(
Q^{host}-
Q^{base}
)
\right)
=
-
\sum_j
\int
|m(t)|^2

d\mu_{b_j,\gamma_j}(t)
\]

with the overall sign fixed by the Hardy orientation.

In the crossing limit this becomes the atomic rotor current

\[
-
\sum_j
|m(\gamma_j)|^2.
\]

Thus the rigged-distribution current and the observer-localized projection trace agree term by term and after summation.

## Tetrahedral consequence

Infinite rotor packets do not produce a globally trace-class terminal projection. They produce an observer-locally trace-class modification on the source-generated tetrahedral subcategory.

This is the same categorical level on which face \(H_{234}\) is recovered by faithful whiskering. Therefore the infinite rotor filler is admissible objectwise for every Schwartz observer, with finite packets converging in the relevant trace ideal.

## What remains open

The construction does not prove:

1. an unlocalized trace-class infinite rotor projection;
2. uniform trace bounds over the unit ball of ambient \(L^2\);
3. convergence for divisor sequences violating the Blaschke condition;
4. interchange of crossing and infinite-product limits without uniform tail control;
5. arithmetic provenance of the inserted infinite inner factor;
6. positivity of the baseline semilocal form outside the rotor defect.

## Disposition

Under the half-plane Blaschke condition and polynomial local counting, an infinite divisor packet has an exact model-space rotor projection whose Mellin--Schwartz localizations are trace class:

\[
\boxed{
M_m^*
P_{K_B}
M_m
\in
\mathcal S_1.
}
\]

Finite products converge to it in observer-localized trace norm, and exact Hardy recentering transports the result into semilocal cutoff geometry without introducing cutoff growth.
