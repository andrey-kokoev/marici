# Hardy orientation produces a causal one-sided impedance and locates the global gate in reciprocal feedback

## Oriented Hardy branch

Let

\[
H(z)
=
F(-iz)
=
\int_0^\infty
\Phi(u)e^{izu}
\,du.
\]

For \(\operatorname{Im}z>0\), this is the positive-support Paley--Wiener branch. Its reflected boundary branch is

\[
H^*(z)
=
F(iz).
\]

On the real boundary, since \(\Phi\) is real,

\[
H^*(x)=
\overline{H(x)}.
\]

The two functions must not be treated as independent states in one parity graph. \(H\) is the causal branch and \(H^*\) is recovered adjointly.

## One-sided Clark observations

The positive-support pieces of the Clark observations are

\[
E_+(z)
=
\frac12
\int_0^\infty
(1-u)
\Phi(u)e^{izu}
\,du,
\]

\[
E_+^*(z)
=
\frac12
\int_0^\infty
(1+u)
\Phi(u)e^{izu}
\,du.
\]

With \(s=-iz\), these are

\[
E_+
=
\frac12
\left(F(s)+F'(s)
\right),
\]

\[
E_+^*
=
\frac12
\left(F(s)-F'(s)
\right).
\]

Define the causal impedance

\[
m(s)
=
-
\frac{F'(s)}{F(s)}.
\]

Then

\[
E_+
=
\frac12F(s)(1-m(s)),
\]

\[
E_+^*
=
\frac12F(s)(1+m(s)).
\]

The naturally oriented Cayley transfer is therefore

\[
\theta_+(s)
=
\frac{E_+}{E_+^*}
=
\frac{1-m(s)}{1+m(s)}.
\]

## Positive-real criterion

The Cayley transform satisfies

\[
|\theta_+(s)|
\le1
\]

exactly when

\[
\operatorname{Re}m(s)
\ge0.
\]

For positive real \(s\),

\[
m(s)
=
\frac{
\int_0^\infty
u\Phi(u)e^{-su}
\,du
}{
\int_0^\infty
\Phi(u)e^{-su}
\,du
}
>0.
\]

Thus the causal one-sided transfer is contractive on the positive real axis. Extending the positive-real property to the full right half-plane is a separate analytic question; positivity of the density alone does not make it automatic because the complex Laplace transform can have zeros.

## Recovery of the completed Clark pair

The completed outputs are reciprocal feedback sums:

\[
E(z)
=
E_+(z)
+
\left(E_+^*
\right)^*(z),
\]

\[
E^*(z)
=
E_+^*(z)
+
E_+^*(z)^*_{
\text{with the opposite moment orientation}},
\]

or, explicitly,

\[
E(z)
=
\frac12
\left[
F(s)+F(-s)+F'(s)-F'(-s)
\right],
\]

\[
E^*(z)
=
\frac12
\left[
F(s)+F(-s)-F'(s)+F'(-s)
\right].
\]

Hence the global Clark transfer is not the one-sided Cayley transform \(\theta_+\). It is the reciprocal feedback closure of the causal branch and its adjoint branch.

## Control interpretation

The one-sided system is a causal impedance realization. Its state is the stopped positive-support history. Reflection supplies the anticausal adjoint system.

The global Xi system is a two-sided feedback interconnection. The difficult sign occurs in closing that feedback loop, not in defining the causal branch.

This separates two questions:

1. Is the one-sided impedance \(m\) positive real?
2. Does reciprocal feedback preserve passivity and produce the completed Clark ratio?

The second is strictly stronger and contains the zero-confinement obstruction.

## Next executable test

The source-derived one-sided kernel is

\[
K_m(s,t)
=
\frac{
m(s)+
\overline{m(t)}
}{
s+
\overline t
}.
\]

Finite positivity tests for this kernel determine whether the causal impedance is positive real on sampled right-half-plane packets. If it fails, the proposed Hardy orientation is already invalid before reciprocal sewing. If it succeeds, the remaining defect is isolated to the reciprocal feedback closure.

## Disposition

Hardy orientation yields a well-typed causal constructor and preserves the odd moment channel. The completed Xi transfer remains a reciprocal feedback system; its positivity is not inherited formally from the one-sided branch.
