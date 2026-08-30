# The dual-energy seam divergence is logarithmic and has no pole residue

## Asymptotic calculation

Set

\[
\sigma=\frac12+\varepsilon,
\qquad
\varepsilon>0.
\]

The squared dual-energy norm of the nonvacuum Mellin observer is

\[
N(\varepsilon)
=
\frac12
\sum_{n\ge2}
\frac{n^{-1-2\varepsilon}}{\log n}.
\]

The integral comparison

\[
\int_2^\infty
\frac{x^{-1-2\varepsilon}}{\log x}\,dx
=
\int_{\log2}^{\infty}
\frac{e^{-2\varepsilon u}}{u}\,du
\]

gives

\[
N(\varepsilon)
=
\frac12\log\frac1{\varepsilon}
+
O(1)
\]

as \(\varepsilon\downarrow0\), subject to the standard sum-integral finite constant.

Thus the seam singularity is logarithmic, not a simple pole.

## No rank-one Abelian residue

In particular,

\[
\lim_{\varepsilon\downarrow0}
2\varepsilon N(\varepsilon)=0.
\]

So the residue test appropriate to the primitive history Gram,

\[
2\varepsilon\,\mathcal H_\varepsilon^{*}\mathcal H_\varepsilon,
\]

does not extract a nonzero wall residue from this dual-energy observer norm.

The two singularities must not be conflated:

- primitive history self-Gram may have a pole-type constant-wall residue;
- Mellin observer dual norm has logarithmic scale accumulation.

A pole subtraction or identity residue that is correct for the first object is not automatically correct for the second.

## Distributed scale escape

The logarithm comes from the interval

\[
1\lesssim\log n\lesssim\varepsilon^{-1}.
\]

As \(\varepsilon\) decreases, the mass of the normalized Riesz representative spreads across progressively larger logarithmic scales. It need not converge to one fixed coefficient direction.

Therefore the observer seam loss may be an escape-to-infinity phenomenon rather than a finite-rank wall mode.

This matches the source typing: the external five-cell controller records boundary capabilities, while the observer itself reaches the seam through a rigged scale limit.

## Correct renormalization question

If the completed Green identity requires a finite part, the candidate subtraction is logarithmic:

\[
N(\varepsilon)
-
\frac12\log\frac1{\varepsilon}.
\]

But even this scalar finite part does not define an operator subtraction. Source authority requires identifying the corresponding distributional scale functional and proving that it lands in the declared boundary port.

A scalar asymptotic cannot decide whether the escaping mass is routed into:

- the constant wall;
- the delta wall;
- an archimedean endpoint jet;
- or no finite boundary direction at all.

## Completion hostile

Choose normalized Riesz vectors

\[
\widehat r_\varepsilon
=
\frac{r_\varepsilon}{\|r_\varepsilon\|_{\mathcal E}}.
\]

They have unit energy norm, while each fixed finite-label projection tends to zero as \(\varepsilon\downarrow0\). Thus they can converge weakly to zero while their norm remains one.

Any completion argument using only finite coordinate tests will miss this seam escape.

## Revised gate

The mixed Green theorem must prove tightness in logarithmic scale, or explicitly compactify the escaping end by a source boundary object. A finite-rank residue theorem is insufficient for the Mellin observer.

The next analytic object is therefore a scale-end defect measure for \(\widehat r_\varepsilon\), together with a proof that the external controller observes it faithfully.
