# RH off-seam zero is forbidden by source-derived regular parallelism

## Result

The missing spectral anchor has a precise geometric form. If the endpoint Evans section is a nonzero parallel section of a source-derived regular line connection on either open half-plane, then it has no zero there.

In a local frame, parallelism is

\[
f'(z)=a(z)f(z),
\]

where \(a\) is regular on the domain. A solution that vanishes at one point has zero initial data and is identically zero by uniqueness. Therefore a section nonzero at one anchored point cannot acquire an isolated off-seam zero.

This is the symbolic puncture-impossibility theorem sought earlier. A puncture would force the connection itself to become singular.

## Hostile multiplier

For

\[
h(z)=1-z^2,
\]

the only scalar coefficient making \(h\) parallel away from its zeros is

\[
a(z)=\frac{h'(z)}{h(z)}
=\frac{-2z}{1-z^2}.
\]

This coefficient has poles at both hostile zeros. More directly, at \(z=1\), every regular connection would require

\[
h'(1)=a(1)h(1)=0,
\]

but \(h'(1)=-2\). The one-point derivative residual is a finite falsifier.

## Noncircularity gate

Defining \(a=f'/f\) is forbidden. It divides by the endpoint section, exposes its zeros, and manufactures the desired connection on the zero-free locus.

The connection must instead be derived from the labelled theta/Tate colligation before taking the scalar endpoint readout. The endpoint section must then be proved parallel by an operator or boundary identity.

## Two-direction architecture

Let \(D_{\mathrm{src}}\) denote labelled-addition transport and \(D_{\mathrm{sp}}\) the spectral connection. The complete bridge requires

\[
D_{\mathrm{sp}}F=0,
\qquad
D_{\mathrm{src}}F=0
\]

in the appropriate comparison line, together with the mixed flatness relation

\[
[D_{\mathrm{sp}},D_{\mathrm{src}}]=0.
\]

Arithmetic transport propagates the anchored comparison through source additions. Spectral parallelism prevents a cutoff-independent hostile divisor. Mixed flatness ensures that the two propagations describe one section rather than incompatible normalizations.

## DPC verdict

Candidate: reflection symmetry, anomaly coherence, or labelled-addition jets alone.

Verdict: all are compatible with hostile off-seam multipliers.

Candidate: a source-derived regular spectral connection with a nonzero anchored parallel endpoint section.

Verdict: sufficient for zero exclusion on each connected open half-plane. Construction from the source remains open.

## Immediate source calculation

Derive the spectral generator of the complete boundary-bearing colligation before scalar projection. Apply it to the endpoint evaluation vector and compute

\[
R_X(z)=D_{\mathrm{sp},X}F_X(z).
\]

Any nonzero residual falsifies parallelism. Any pole introduced only after scalar division falsifies source derivation. Exact zero residual with a regular generator would provide the missing vertical bridge; completion must then preserve regularity, flatness, and the nonzero anchor.
