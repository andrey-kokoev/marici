# Standard PNT remainders cannot control the fixed-width Gram tail

## Required scale

For fixed `sigma`, the endpoint and prime-window main terms near separation `d` both have scale

\[
e^{d/2+\sigma/2}.
\]

Rank-two positive definiteness instead requires the completed difference kernel to satisfy

\[
|K_\sigma(d)|\le K_\sigma(0),
\]

so the residual after endpoint--gamma--prime cancellation must remain bounded independently of `d`.

## Unconditional PNT comparison

A classical zero-free-region remainder has the schematic form

\[
\psi(x)-x
=O\!\left(xe^{-c\sqrt{\log x}}\right).
\]

At the moving center `x=e^d`, weighting by `x^{-1/2}` leaves the scale

\[
e^{d/2-c\sqrt d},
\]

up to fixed Gaussian-window and polynomial factors. This still diverges as `d` tends to infinity and cannot yield the required bounded Gram residual.

## RH-size comparison

The standard RH-conditional estimate

\[
\psi(x)-x=O(x^{1/2}\log^2x)
\]

becomes at best polynomial in `d` after the same `x^{-1/2}` weighting. It also does not directly prove a uniform constant bound. The fixed-width Gram inequality needs cancellation organized by the complete explicit formula, not an absolute estimate of the prime-counting remainder alone.

This does not mean the Gram bound is stronger than RH: under RH it follows from the positive spectral representation. It means that passing through a coarse absolute PNT remainder destroys the oscillatory endpoint--gamma--zero cancellation that makes the bounded Fourier kernel possible.

## Consequence

The proposed far-separation strategy

\[
\text{endpoint main term}
-
\text{PNT prime main term}
+
\text{absolute remainder bound}

aims at the wrong norm. Neither the unconditional nor customary RH-level prime-counting remainder reaches the bounded residual after the logarithmic Gaussian window is weighted.

A viable arithmetic proof must retain signed transform information, for example through the complete Weil explicit formula, a relative quadratic-form estimate, or a source-derived positive spectral measure. Termwise absolute values and ordinary PNT error bounds are too lossy.

## Disposition

Close the coarse PNT-remainder branch. The moving saddle explains where cancellation occurs but does not provide a proof norm. Do not request progressively sharper absolute prime-counting estimates from this formulation; return to the coupled transform or Gram form.
