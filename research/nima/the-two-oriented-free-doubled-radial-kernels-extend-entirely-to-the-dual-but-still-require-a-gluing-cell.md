# The two oriented free doubled radial kernels extend entirely to the dual but still require a gluing cell

## Question

Does only the rank-one wall crossing continue through the seam, or do the full right- and left-half-plane kernels admit rigged continuations?

## Claim boundary

Each oriented full kernel, including its Volterra pieces and wall crossing, extends weakly entirely from the projective exponential test space to its dual. The two extensions are not thereby identified: equality or coherent gluing across the seam is a separate source comparison. Neither extension generally preserves the test space because a causal solution may acquire an exponential homogeneous tail.

## Triangular kernels

Every diagonal free-resolvent piece has a kernel of the form

\[
K_z(t,s)=\mathbf1_{s<t}e^{\pm z(t-s)}
\]

or its terminal counterpart with \(t<s\). For a compact parameter set \(C\), put

\[
M_C=\sup_{z\in C}|\operatorname{Re}z|.
\]

Then

\[
|K_z(t,s)|\le e^{M_C(t+s)}.
\]

Choose \(a>M_C\). For \(f\in\mathcal S_{\exp}\), Cauchy--Schwarz gives

\[
\int_0^\infty e^{M_Cs}|f(s)|\,ds
\le
\frac{p_a(f)}{\sqrt{2(a-M_C)}}.
\]

Therefore, for test vectors \(f,g\),

\[
\left|
\int_0^\infty\int_0^\infty
\overline{g(t)}K_z(t,s)f(s)\,ds\,dt
\right|
\le
\frac{p_a(f)p_a(g)}{2(a-M_C)}.
\]

The estimate is independent of the triangular support orientation.

## Parameter jets

Differentiating the kernel introduces \((t-s)^j\). Since

\[
|t-s|^j\le(t+s)^j,
\]

one may choose \(b>a>M_C\) and absorb the polynomial into \(e^{(b-a)(t+s)}\). Thus every fixed parameter derivative satisfies a compact-local estimate

\[
|\langle g,\partial_z^jV_zf\rangle|
\le C_{C,j,a,b}\,p_b(f)p_b(g).
\]

Dominated differentiation then proves that

\[
z\longmapsto V_z:
\mathcal S_{\exp}\to\mathcal S_{\exp}'
\]

is weakly entire and compact-locally equicontinuous.

## Adding the wall crossing

The rank-one wall term is already an entire map

\[
C_z:\mathcal S_{\exp}\to\mathcal S_{\exp}'.
\]

Hence each oriented kernel

\[
\mathcal R_{z,+}^{\rm rig}=V_{z,+}+C_{z,+},
\qquad
\mathcal R_{z,-}^{\rm rig}=V_{z,-}+C_{z,-}
\]

is weakly entire as a test-to-dual family. Its restriction in its source half-plane agrees with the corresponding bounded Hilbert resolvent. Analytic continuation alone does not prove

\[
\mathcal R_{z,+}^{\rm rig}=\mathcal R_{z,-}^{\rm rig}.
\]

That comparison must retain reciprocal exchange, triangular support, sewing phase, and any homogeneous-tail correction.

## Why the codomain is the dual

For a causal kernel, compactly supported or superexponentially decaying input can produce a tail proportional to \(e^{zt}\). At parameters where that tail grows, the output does not belong to \(\mathcal S_{\exp}\), although it remains a continuous functional on that space.

Thus

\[
\mathcal S_{\exp}\to\mathcal S_{\exp}'
\]

is the natural global type. Claiming

\[
\mathcal S_{\exp}\to\mathcal S_{\exp}
\]

without moment cancellation would be false. The exact Evans mismatch is one source-specific cancellation that can remove a homogeneous tail; it is not a property of the free kernel on arbitrary inputs.

## Reciprocal orientation

The two parameter half-plane formulas use opposite triangular supports and opposite cross-channel directions. Their rigged continuation belongs to one doubled operator family only when the incoming and outgoing labels are retained. Scalarizing the kernels before continuation loses this orientation even though the resulting scalar pairing may remain entire.

## G4 consequence

The free part of the candidate conservative complex now has a complete typed continuation:

\[
\mathcal S_{\exp}^{\oplus2}
\longrightarrow
(\mathcal S_{\exp}')^{\oplus2}.
\]

The remaining G4 problem is not free seam continuation. It is whether the source-generated radial, endpoint, Wronskian, and arithmetic feature maps compose with this test-to-dual kernel so that:

1. the full response returns to the declared reduced feature carrier;
2. homogeneous tails cancel by source identities rather than fitted subtraction;
3. reciprocal and Real structures intertwine;
4. every Xi jet is preserved.

## Hostiles

A checker must reject:

1. test-space invariance claimed without tail-moment cancellation;
2. a kernel estimate using a weight \(a\le M_C\);
3. zeroth-order continuity promoted to all jets without polynomial absorption;
4. scalar continuation that erases triangular support orientation;
5. free test-to-dual continuation promoted to arithmetic feature continuity;
6. source-specific Evans cancellation treated as a free-kernel identity.

## Disposition

Each oriented free doubled radial kernel is now controlled: zero-free on Hilbert space, explicitly resolvent-bounded in its half-plane, and weakly entire from the exponential test space to its dual. The two entire continuations still require a source gluing cell, and the nonfree response requires G4's canonical feature and arithmetic interfaces. No RH conclusion is authorized.
