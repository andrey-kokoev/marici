# Exact free-tail cancellation requires negative radial support and cannot come from a second positive-half-line copy

> **Correction.** The successor packet
> `folding-the-whole-line-source-identifies-the-gluing-coordinate-with-its-bilateral-laplace-transform.md`
> computes the canonical whole-line fold. Negative-support reflection constructs
> the reciprocal source geometry but does not make the free gluing coordinate
> vanish: after folding that coordinate is the bilateral Laplace transform of
> the complete source and vanishes entirely only for the zero source.

## Question

Can a parameter-independent reciprocal source on a second copy of \(\mathbb R_+\) satisfy the entire gluing-cancellation identity?

## Claim boundary

Not for a nonzero ordinary source function. The required identity is the bilateral Laplace reflection law, whose inverse transform places the reciprocal source on the negative radial half-line. Two channels both parametrized by positive radial distance cannot realize it by a parameter-independent local copy or phase. Cancellation therefore requires a whole-line reflected source coordinate, a parameter-dependent nonlocal incidence, or retention of the defect as a G4 boundary feature.

## Cancellation identity

For source functions \(f_+,f_-\in\mathcal S_{\exp}(\mathbb R_+)\), free-tail cancellation requires

\[
\ell_{-z}(f_-)=-u\,\ell_z(f_+)
\]

for every \(z\in\mathbb C\), where

\[
\ell_{-z}(f_-)=\int_0^\infty e^{zt}f_-(t)\,dt,
\qquad
\ell_z(f_+)=\int_0^\infty e^{-zt}f_+(t)\,dt.
\]

All moments exist because the sources decay faster than every exponential.

## Moment reflection

Differentiation at \(z=0\) gives, for every \(j\ge0\),

\[
\int_0^\infty t^j f_-(t)\,dt
=-u(-1)^j
\int_0^\infty t^j f_+(t)\,dt.
\]

These are exactly the moments of the reflected distribution

\[
f_-^{\rm req}(t)=-u f_+(-t),
\]

which is supported on \(( -\infty,0]\), not on the second positive half-line.

## Support obstruction

Extend both positive-half-line sources by zero to \(\mathbb R\). The cancellation identity states that their bilateral Laplace transforms agree after reflection. Injectivity of the Fourier transform on the seam \(z=i\xi\) implies

\[
f_-^{\rm ext}(t)=-u f_+^{\rm ext}(-t)
\]

as tempered distributions. The left side is supported in \([0,\infty)\), while the right side is supported in \(( -\infty,0]\). Their equality is therefore supported only at \(t=0\).

Ordinary functions in \(\mathcal S_{\exp}\) have no point-supported component. Hence

\[
f_+=f_-=0.
\]

A nonzero completed-theta radial forcing cannot satisfy exact cancellation inside two independently positive half-line source channels.

## Architectural consequence

The reciprocal carrier \(\partial_t\oplus(-\partial_t)\) remains correct for conservative wall sewing, but its source coordinates cannot both be interpreted as the same positive radial history. The second source must instead arise from one of three typed constructions:

1. a whole-line radial source with the reciprocal component supported at negative separation;
2. a nonlocal, parameter-dependent incidence implementing reflected Laplace transport;
3. a boundary-feature map carrying the uncancelled entire section
   \[
   zR(z)-\rho(0)=E(z)-\frac12W(z).
   \]

The first is the minimal reciprocal source realization, but the successor folding calculation proves that it does not produce universal cancellation. It preserves the distinction between radial separation sign and reciprocal channel label while exposing the full bilateral transform as boundary data. The second risks circularly building the desired spectral response into the incidence and needs independent source authority. The third matches the existing endpoint-minus-Wronskian decomposition and is now the productive route, but requires G4 to expose the full feature carrier.

## Ordered-pair implication

The completed-theta ordered-pair kernel is naturally defined for real separation before one-sided Laplace readout. Its swap reverses the ratio coordinate and changes the translated shell. Therefore a whole-line reflected source is compatible with the known pair architecture, but only if the shell and ordered-pair transport are retained. A scalar same-shell phase is not compatible with that swap law.

## Disposition

Direction 1 narrows from “find a second positive-half-line source” to “construct the whole-line reflected ordered-pair source and its restriction to the doubled conservative carrier.” The positive-half-line local-copy variant is eliminated. The next depth-first test is whether the existing real-separation pair kernel and shell-transport law define this whole-line source without losing endpoint localization. No RH conclusion is authorized.
