# The naive separation amplitude is not a spectral factor

## Bounded question

Does the positive two-copy separation density immediately provide the
source-derived spectral factor required by packet 126?

## Natural fiber amplitude

In sum--difference coordinates, define

\[
 h_n(S,D)
 =D^n
 \sqrt{
 \Phi\left(\frac{S+D}{2}\right)
 \Phi\left(\frac{S-D}{2}\right)}.
\]

The separation-weighted pushforward density is, up to the fixed Jacobian,

\[
 g_n(S)=\int_{\mathbb R}|h_n(S,D)|^2\,dD.
\]

Thus `g_n(S)` is a pointwise norm in the `D` fiber.

## Fourier mismatch

Fourier transformation in `S` gives

\[
 \widehat g_n(x)
 =\int_{\mathbb R}e^{ixS}
 \|h_n(S,\cdot)\|_{L^2(D)}^2\,dS.
\]

By contrast, the squared norm of the Fourier-transformed amplitude is

\[
 \|\widehat h_n(x,\cdot)\|_{L^2(D)}^2
 =\iint e^{ix(S-S')}
 \langle h_n(S',\cdot),h_n(S,\cdot)\rangle\,dS,dS'.
\]

These are different objects.  The first contains a phase in the absolute
coordinate `S`; the second contains a phase in the displacement `S-S'` and is
automatically nonnegative.

Therefore

\[
 \boxed{
 g_n(S)=\|h_n(S,\cdot)\|^2
 \not\Longrightarrow
 \widehat g_n(x)=\|\widehat h_n(x,\cdot)\|^2.}
\]

The positive source density supplies a direct-integral norm, not an
autocorrelation factor.

## Consequence for the DPC

Packet 126 remains a meaningful conjecture only if modular sewing constructs
an additional comparison map identifying absolute sum-scale with a relative
translation coordinate.  Without that map, writing the positive density as a
fiber norm merely restates source positivity and does not constrain its
Fourier sign.

This is the same categorical distinction encountered throughout Marici:

\[
 \boxed{
 \text{positive fibers}
 \neq
 \text{positive transported comparison kernel}.}
\]

## Scalar versus module-valued factor

The theta source contains infinitely many winding labels and a moving modular
seam. A scalar factor `h_n` would erase those channels before their coherence
is proved. The better target is a Hilbert-module-valued amplitude `H_n` with a
source-derived translation representation `T_S` such that

\[
 g_n(S)=\langle H_n,T_SH_n\rangle.
\]

Then

\[
 \widehat g_n(x)
\]

would be the positive spectral density of the unitary representation. This is
a genuine operator construction rather than a post-hoc square root.

## Next gate and falsifier

The immediate task is to derive `T_S` from adelic dilation and modular seam
transport while retaining winding labels. It must act on a fixed Hilbert
module; a family of unrelated fibers `L2(D)` is insufficient.

The conjecture fails if the moving-centered fibers of packet 118 cannot be
canonically identified under changes of `S`, or if their modular transition is
indefinite. The smallest falsifier is holonomy around one reciprocal
scale-reflection loop that fails to preserve the proposed fiber inner product.
