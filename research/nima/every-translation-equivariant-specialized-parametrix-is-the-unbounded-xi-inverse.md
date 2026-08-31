# Every translation-equivariant specialized parametrix is the unbounded Xi inverse

## Question

Can a specialized-range parametrix recover the codiagonalized source while avoiding global division by the completed-theta multiplier?

## Claim boundary

Not if the parametrix respects the real translation action that generates the source labels. Any continuous translation-equivariant left inverse to completed-theta convolution is forced in Fourier coordinates to multiply by \(1/\Xi\) wherever \(\Xi\ne0\). It therefore inherits the same exponential horizontal growth. Avoiding that multiplier requires a non-equivariant arithmetic observer, which is additional label structure rather than a history-only parametrix.

## Convolution and translation

Let

\[
C_\Phi\mu=\Phi*\mu
\]

on a translation-stable test or distribution carrier containing the finite signed prime-power measures. Write real translation as

\[
(\tau_a f)(t)=f(t-a).
\]

The source synthesis is generated from translated point masses, and

\[
C_\Phi\tau_a=\tau_aC_\Phi.
\]

Suppose a proposed parametrix \(P\) satisfies

\[
PC_\Phi\mu=\mu
\]

on the source-generated range and is translation-equivariant there:

\[
P\tau_a=	au_aP.
\]

## Multiplier rigidity

A continuous operator commuting with all real translations is a Fourier multiplier on the relevant translation-stable carrier. Thus there is a symbol \(m(z)\) with

\[
\widehat{Pf}(z)=m(z)\widehat f(z).
\]

Applying the left-inverse identity to a translated point mass gives

\[
m(z)\widehat\Phi(z)e^{-iaz}=e^{-iaz}
\]

for every admitted translation \(a\). Hence, wherever \(\widehat\Phi(z)\ne0\),

\[
m(z)=\frac1{\widehat\Phi(z)}.
\]

In the completed normalization this is, up to the fixed nonzero convention factor,

\[
m(z)=\frac1{\Xi(z)}.
\]

The symbol is therefore not a freely fitted regularizer.

## Consequence on the recovery lines

On the two horizontal lines needed for projective Bohr recovery, Xi is zero-free but

\[
|\Xi(x\pm iR)|^{-1}
\gtrsim
 e^{\pi|x|/4}(1+|x|)^{-N_R}
\]

along large frequencies, modulo the standard fixed-line polynomial factors. Therefore the forced multiplier is not continuous in the unweighted raw two-line supremum topology or in a history topology that supplies only vertical Fourier extension.

A cutoff multiplier cannot repair this while remaining an exact left inverse: suppressing high real frequencies changes the translated point-mass packet and destroys coefficient recovery.

## What a non-equivariant extractor would mean

An operator can evade multiplier rigidity only by using structure not invariant under arbitrary real translation, such as:

- the distinguished displacement set \(\{\pm k\log p\}\);
- prime and grade projections;
- arithmetic sampling functionals;
- a chosen origin and label-dependent localization cells.

Such an extractor may be mathematically valid, but it is an arithmetic label observer. It must be sourced and exposed as part of G4; it cannot be described as a canonical history-only convolution parametrix.

## Direction rescore

- Translation-equivariant specialized parametrix: reduced to Xi division and rejected in the current topology, 0/10.
- High-frequency cutoff parametrix with exact recovery: 0/10.
- Non-equivariant arithmetic localization: 6/10; possible but requires an explicit observer and conditioning estimate.
- Existing labelled fibre recovery: completed.
- G4 observer/interface exposure: 10/10 and ownership-blocked.

## Disposition

The specialized-parametrix branch does not bypass the deconvolution obstruction while preserving source translation covariance. The remaining post-codiagonal option is an explicit arithmetic localization observer, which reintroduces the label lattice in observer form. Without G4 exposure of that observer, the mathematically supported architecture is to retain labels through recovery and codiagonalize only afterward. No RH or closed-range conclusion is authorized.
