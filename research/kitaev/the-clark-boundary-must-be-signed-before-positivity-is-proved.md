# The Clark boundary must be signed before positivity is proved

## Question

Can the theta tail be mapped into the positive Clark model space in order to
derive the Hermite–Biehler property, or does that choice of codomain already
assume the desired theorem?

## Conditional Clark construction

From the fixed theta transform define

\[
X(z)=\xi\left(\frac12+iz\right),
\qquad
E(z)=X(z)+iX'(z),
\]

and

\[
\Theta(z)=\frac{E^*(z)}{E(z)}.
\]

If \(\Theta\) is Schur in the upper half-plane, one may form

\[
\mathcal K_\Theta
=
H^2(\mathbb C_+)\ominus\Theta H^2(\mathbb C_+)
\]

and its Clark operators. In the theta setting, this Schur property is
equivalent to the required Hermite–Biehler inequality and hence to the
zero-confinement statement.

Therefore a trace map whose codomain is declared to be the positive model
space \(\mathcal K_\Theta\) cannot be used to prove that \(\Theta\) is Schur.
Its codomain has already encoded the conclusion.

## Denominator-free signed kernel

Before positivity, the source still defines the Hermitian kernel numerator

\[
\mathcal K_E(z,w)
=
\frac{
E(z)\overline{E(w)}
-E^*(z)\overline{E^*(w)}
}{
2i(\overline w-z)
}.
\]

This kernel is algebraically meaningful wherever the diagonal extension is
taken correctly. Its finite evaluation matrices may be positive, indefinite,
degenerate, or have growing negative index.

The noncircular boundary object is therefore the algebraic span of evaluation
symbols

\[
\mathcal B_E^{\rm alg}
=
\operatorname{span}\{k_z:z\in\mathbb C_+\}
\]

with sesquilinear form

\[
\langle k_w,k_z\rangle_E=\mathcal K_E(z,w),
\]

followed by quotienting only the actual radical. No positive completion is
chosen in advance.

If the form is positive, its completion becomes the desired reproducing
kernel Hilbert space. If it has finitely many negative squares, a Pontryagin
completion may be available. If its negative index grows without bound, the
appropriate target remains a more general Krein or locally convex dual-pair
object.

The sign type is an output of the source theorem.

## Source tail domain

The archimedean tail side is already noncircular. The two reciprocal
half-line graph domains sew through their endpoint traces:

\[
\mathcal D_{\rm sew}
=
\mathcal D_+\times_{\mathbb C}\mathcal D_-.
\]

After coordinate reversal this is the ordinary \(H^1(\mathbb R)\) trace
pullback. Tensoring with the arithmetic test space gives

\[
\mathcal D_{\rm test}
=
\mathcal S_P\widehat\otimes H^1(\mathbb R).
\]

Endpoint evaluation is continuous there. The obstruction appears only after
arithmetic dualization: the completed state and primitive current may both
lie in

\[
\mathcal S_P'\widehat\otimes H^1_{\rm loc},
\]

and there is no canonical dual-times-dual Green pairing.

Thus the source of the trace is defined, but its completed self-pairing is
not.

## Minimal noncircular trace target

The required map is not initially

\[
J:\mathcal D_{\rm test}\longrightarrow\mathcal K_\Theta.
\]

It must instead be

\[
J_{\rm alg}:
\mathcal D_{\rm test}
\longrightarrow
\mathcal B_E^{\rm alg}
\]

or a cross-sector version

\[
J_+\times J_-:
\mathcal D_+\times\mathcal D_-
\longrightarrow
\mathcal B_E^+\times\mathcal B_E^-,
\]

with a source-derived dual pairing between the two targets.

Only after proving that the pullback kernel form is positive and continuous
may the target be completed as a Hilbert or Clark space.

## Explanatory theorem shape

A noncircular theorem would establish an identity of the form

\[
\langle J\phi,J\phi\rangle_E
=
\mathcal E_{\rm scale}(\phi)
+\mathcal E_{\rm seam}(\phi)
+\mathcal E_{\rm arith}(\phi),
\]

where every term on the right is:

- derived before scalar zero testing;
- well-defined in its test/dual direction;
- nonnegative or exactly cancelled by a typed source relation;
- faithful modulo declared gauge.

If the image of \(J\) is dense in the signed kernel module and the right side
is nonnegative, then \(\mathcal K_E\) is positive on all evaluation packets.
That proves Clark admission rather than assuming it.

Density or range completeness is essential. Positivity on a proper source
subspace does not imply positivity of the full kernel.

## Fourier–Tate naturality

The trace must also satisfy the uncompressed naturality square

\[
J\mathcal F
=
\mathcal F_{\rm Tate}J
\]

in the signed boundary object. Equality only after applying the scalar Tate
functional permits a hidden boundary residual.

The residual

\[
\mathfrak R(\phi)
=
J(\mathcal F\phi)-\mathcal F_{\rm Tate}J(\phi)
\]

must vanish as a typed vector or relation, not merely under one scalar
observer.

## Why finite positive samples are insufficient

Every finite collection of evaluation points may produce a positive Gram
matrix while a negative direction appears later or escapes to completion.
The source theorem requires:

1. positivity on every finite evaluation packet;
2. compatibility under inclusion of packets;
3. completion-stable closure of the radical;
4. no normalized negative or null sequence escaping in the limit.

This is the kernel analogue of uniform observability.

## Hostile fixtures

### Positive target by definition

Constructing \(H^2\ominus\Theta H^2\) before proving that multiplication by
\(\Theta\) is contractive assumes the admission condition.

### Proper positive image

A trace may land in a positive subspace while the ambient signed kernel has
an orthogonal negative direction. Source-image positivity alone is
insufficient without density or a quotient theorem.

### Dual-times-dual pairing

Pairing two distributional prime currents through an undeclared Riesz pivot
can manufacture the desired sign and violates source typing.

### Scalar-natural but vector-anomalous trace

A nonzero \(\mathfrak R(\phi)\) can lie in the scalar observer kernel, leaving
the functional equation intact while breaking boundary naturality.

### Finite negative-index escape

Cutoff kernels may each have no detected negative direction while their least
Gram eigenvalue tends to zero and the limit becomes indefinite.

## Revised DPC

The source-native explanation should assert:

> The sewn theta tail admits a Fourier–Tate natural trace into the signed
> Clark kernel module, and the complete typed Green identity makes the kernel
> form positive and faithful before any positive Clark completion is chosen.

Its primary falsifiers are a typed naturality residual, an undefined
dual-times-dual term, a negative evaluation packet, a non-dense trace range,
or a collapsing completion margin.

## Disposition

The infinite Clark carrier remains the right target only after a crucial
correction: it must begin as a signed algebraic kernel module. The positive
model space is the theorem's conclusion.

The next concrete work is to derive the trace on the test-valued tail source,
compute its pullback form, and isolate the first term that fails to extend
when both inputs become distributional.

## Claim boundary

This packet defines the noncircular target and theorem shape. It does not
construct the theta trace, prove density, define the completed dual pairing,
or establish positivity.
