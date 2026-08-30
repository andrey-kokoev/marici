# Reciprocal sewing uniquely centers the Todd germ by a half-density

## The two boundary charts

Let

\[
\tau(t)=\frac{t}{e^t-1}.
\]

Reflection of the formal boundary coordinate gives the exact transition

\[
\tau(-t)=e^t\tau(t).
\]

Thus the two reciprocal charts do not agree literally. Their discrepancy is
the invertible exponential character \(e^t\).

## The forced half-density

Consider a character-renormalized germ

\[
\tau_a(t)=e^{at}\tau(t).
\]

Reflection invariance requires

\[
\tau_a(-t)=\tau_a(t).
\]

Using the transition above, this condition becomes

\[
e^{(1-a)t}=e^{at}.
\]

Hence

\[
a=\frac12
\]

is unique. The centered germ is

\[
\widetilde\tau(t)
=
e^{t/2}\tau(t)
=
\frac{t}{2\sinh(t/2)},
\]

and it is even:

\[
\widetilde\tau(-t)=\widetilde\tau(t).
\]

The half-density shift is therefore forced by reciprocal chart agreement;
it is not selected from the zero set.

## Logarithmic tangent

For

\[
L(t)=\frac{d}{dt}\log\tau(t),
\]

the centered logarithmic tangent is

\[
\widetilde L(t)
=
\frac{d}{dt}\log\widetilde\tau(t)
=
L(t)+\frac12.
\]

Because \(\widetilde\tau\) is even, \(\widetilde L\) is odd. The constant
boundary anomaly

\[
L(0)=\zeta(0)=-\frac12
\]

is cancelled exactly. What remains is the odd Bernoulli tower:

\[
\widetilde L(t)
=
-\frac1{12}t
+\frac1{720}t^3
-\frac1{30240}t^5
+\cdots.
\]

Equivalently, the trivial values \(\zeta(-2m)=0\) are the jet-level shadow
of reciprocal evenness after the unique half-density normalization.

## Meaning of the additional pullback

The signed exterior kernel had several negative directions because it was
viewed after logarithmic differentiation. Pulling it back to the
multiplicative germ reveals two reciprocal charts and their transition unit.
Pulling back once more to the centered germ trivializes that unit by splitting
it equally between the charts.

The resulting structure is not positive by itself, but it is rigid:

- reciprocal reflection determines the transition \(e^t\);
- equal chart normalization uniquely determines the exponent \(1/2\);
- the centered germ is even;
- its tangent is odd;
- the zero-order signed anomaly disappears.

## Relation to the critical offset

This is a source-local prototype of the half-density shift that centers the
functional equation at \(s=1/2\). It does not yet identify the formal
Euler–Maclaurin coordinate \(t\) with the global spectral displacement
\(s-1/2\). That comparison must be derived through Mellin transport and the
completed theta source.

The next commutative square should compare the map from \(\tau(t)\) to
\(\widetilde\tau(t)\) with the map from the sectoral Mellin boundary to the
completed spectral half-density.

The falsifier is a nonunit or residual character in this square. If the
vertical maps leave an additional exponential factor, the local half-density
does not yet explain the global critical offset.

## Result

Reciprocal sewing of the Todd boundary germ has transition \(e^t\), and the
unique reflection-invariant normalization is the half-density
\(e^{t/2}\tau(t)=t/(2\sinh(t/2))\). It cancels the \(\zeta(0)\) boundary
anomaly and organizes the remaining exterior jets into an odd tower. The
next gate is the Mellin naturality square connecting this local centering to
the global spectral coordinate.
