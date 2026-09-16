# A four-function response sheaf compresses all moving-seam Fourier saturations

## Question

Must the fourth presentation carry a separate ten-dimensional packet for every nonzero seam?

## Claim boundary

No. The ten scalars are evaluations at \(a\), \(-a\), and zero of four source-derived response functions. Retaining those four functions gives one seam-uniform order-four representation. This is a function-valued compression, not a four-scalar compression.

## Response functions

For \(g\in\mathcal S(\mathbb R)\), define functions of the seam parameter \(a\):

$$
B_g(a)=g(a),
$$

$$
Q_g(a)=\widehat g(a)
=\int_{\mathbb R}e^{-2\pi iax}g(x)\,dx,
$$

$$
A_g(a)=\int_{-\infty}^a g(x)\,dx,
$$

$$
C_g(a)=\operatorname{pv}\int_{\mathbb R}
\frac{e^{-2\pi iax}g(x)}x\,dx.
$$

Set

$$
\mathscr R(g)=(B_g,Q_g,A_g,C_g).
$$

## Fourier action

The moving-seam formulas become identities of functions:

$$
B_{\widehat g}(a)=Q_g(a),
$$

$$
Q_{\widehat g}(a)=B_g(-a),
$$

$$
A_{\widehat g}(a)
=\frac12B_g(0)-\frac1{2\pi i}C_g(a),
$$

$$
C_{\widehat g}(a)
=2\pi iA_g(-a)-\pi iQ_g(0).
$$

Thus define \(\mathbb T\) by

$$
\mathbb T(B,Q,A,C)(a)
=
\left(
Q(a),
B(-a),
\frac12B(0)-\frac1{2\pi i}C(a),
2\pi iA(-a)-\pi iQ(0)
\right).
$$

Then

$$
\mathscr R(\widehat g)=\mathbb T\mathscr R(g).
$$

## Order-four law

Applying the formulas twice yields source reflection:

$$
\mathbb T^2\mathscr R(g)=\mathscr R(g(-\cdot)).
$$

Consequently

$$
\mathbb T^4=I
$$

on the response image.

## Recovery of scalar packets

At a fixed nonzero seam, the ten scalar channels are obtained by evaluating

$$
B,Q,A,C
$$

at \(a\), \(-a\), and zero, omitting repetitions. At \(a=0\), they collapse to the four-channel fixed-seam packet.

Thus the rank jump occurs only when one insists on scalar evaluation before Fourier saturation. The complete function-valued response has a uniform four-component type for all seams.

## Analytic type

On Schwartz space, \(B_g\) and \(Q_g\) are Schwartz, \(A_g\) is a smooth history with finite endpoint limits, and \(C_g\) is the Hilbert-transform response with its standard distributional interpretation. The construction extends by transposition to the corresponding test/strong-dual rigging.

## Disposition

The correct seam-uniform fourth presentation is the four-function response sheaf \((B,Q,A,C)\). It carries exact order-four Fourier transport and specializes to every fixed-seam saturated packet. This provides the natural candidate for the complete function-valued \(V_4\), replacing the nonclosed old four-scalar trace record.