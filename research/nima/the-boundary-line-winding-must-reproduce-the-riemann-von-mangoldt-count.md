# The boundary-line winding must reproduce the Riemann--von Mangoldt count

The projective-line Evans model has a strong asymptotic falsifier before exact determinant identification.

Let
\[
\mathcal L_{\mathrm{dark}}(t)
\]
and
\[
\mathcal L_{\mathrm{react}}(t)
\]
be the radiation-dark and reactive lines in the two-dimensional boundary space. Choose local projective angles
\[
\phi_{\mathrm{dark}}(t),
\qquad
\phi_{\mathrm{react}}(t),
\]
and define the relative angle
\[
\Delta(t)
=
\phi_{\mathrm{react}}(t)
-
\phi_{\mathrm{dark}}(t).
\]

A seam zero occurs when
\[
\Delta(t)\in\pi\mathbb Z,
\]
because lines are unoriented. For transverse crossings, the signed crossing count on an interval is the winding of \(\Delta/\pi\), with endpoint and orientation conventions fixed by one calibrated crossing.

If the Evans section equals \(\xi\) up to a zero-free factor, this crossing count must reproduce the Riemann--von Mangoldt asymptotic:
\[
N(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-
\frac{T}{2\pi}
+
\frac78
+
S(T)
+
O(T^{-1}),
\]
with the usual convention for the fluctuating argument term.

This predicts a source decomposition of projective winding:

- archimedean endpoint transport supplies
  \[
  \frac{T}{2\pi}\log\frac{T}{2\pi}
  -
  \frac{T}{2\pi}
  +
  \frac78;
  \]
- prime-delay return supplies the fluctuating term;
- wall normalization fixes the constant frame;
- reciprocal sewing fixes the crossing orientation.

The main \(T\log T\) growth cannot come from a fixed finite-dimensional constant boundary matrix. It must enter through the gamma/archimedean transport or an equivalent unbounded phase delay.

This creates an immediate model-selection test. Compute the high-frequency asymptotic of the source-derived reactive row
\[
r(t)
\]
and radiation row
\[
y(t).
\]
If their relative projective winding is only \(O(T)\), the model cannot carry the zeta counting law regardless of local positivity.

Likewise, a finite sum of fixed prime delays has only finite exponential type and cannot produce the completed asymptotic after cutoff removal unless the cutoff family has the correct controlled phase limit.

The test must be applied before fitting any scalar normalization. Multiplying the Evans determinant by a zero-free factor
\[
e^{h(z)}
\]
does not change its zeros, but it can arbitrarily alter its scalar argument on contours. Therefore the crossing count must be extracted from the two boundary lines themselves, not from an untyped scalar phase of a chosen trivialization.

A robust formulation uses the Maslov index of the pair
\[
\left(
\mathcal L_{\mathrm{dark}}(t),
\mathcal L_{\mathrm{react}}(t)
\right).
\]
For rank-one Lagrangian lines, the Maslov crossing form at \(t_0\) reduces to the derivative of the relative angle. Its sign and nullity control local multiplicity.

The next source theorem should establish:

1. continuity or analyticity of both line families;
2. discrete Fredholm intersections;
3. a well-defined relative Maslov index;
4. its high-frequency asymptotic from archimedean Stirling data;
5. convergence of the prime-cutoff fluctuation;
6. equality of the resulting counting function with the argument-principle count of the Evans section.

The smallest hostile has the correct first several crossing ordinates but asymptotic line winding \(O(T)\). It cannot reproduce the zero density.

A second hostile multiplies a deficient Evans section by a zero-free scalar with the correct Riemann--Siegel theta phase and then claims the boundary geometry has the right count. The zero set and projective crossings are unchanged, so the repair is purely cosmetic.

A third hostile derives the main archimedean phase but lets the prime fluctuation grow without cutoff control, destroying a stable Maslov count.

Thus the projective boundary model now has a quantitative global signature:

> Its source-derived relative Maslov index must equal the Riemann--von Mangoldt counting function.

This is a much cheaper falsifier than full pointwise determinant identification and directly tests whether the constructor has enough spectral density.
