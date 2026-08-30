# Mellin radial compression forgets the norm-one idele-class fiber

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact full-source typing obstruction

## Idele-class extension

Let

\[
C_{\mathbb Q}=\mathbb A_{\mathbb Q}^{\times}/\mathbb Q^{\times}
\]

be the idele-class group. The global norm gives an exact sequence

\[
1\longrightarrow C_{\mathbb Q}^{1}
\longrightarrow C_{\mathbb Q}
\xrightarrow{|\cdot|}\mathbb R_{>0}
\longrightarrow1,
\]

where (C_{\mathbb Q}^{1}) is the norm-one idele-class fiber.

The Mellin character is

\[
x\longmapsto |x|^s.
\]

It factors through (mathbb R_{>0}) and is constant on
(C_{\mathbb Q}^{1}). Hence scalar Tate/Mellin readout first integrates or
compresses the norm-one fiber and only then performs one-dimensional
logarithmic character transport.

## Kernel theorem

Let (R) be the radial pushforward from a source module on
(C_{\mathbb Q}) to its norm coordinate. Every source packet (v) with

\[
Rv=0
\]

is invisible to every scalar Mellin parameter (s), although (v) may remain
nonzero and may carry rational-boundary or Fourier–Poisson incidence.

Therefore a Green form constructed solely from the radial Mellin tail factors
through (R). Its Gram form has kernel containing (ker R), so it cannot be
faithful on the undecomposed adelic source whenever that fiber kernel is
nontrivial.

The two-point hostile fiber already suffices. Radial summation sends

\[
(a,b)\longmapsto a+b,
\]

and annihilates the angular mode ((1,-1)). Any post-radial positive form is
blind to that mode.

## Consequence for the doubled Green programme

The source-tail system derived from a one-dimensional logarithmic coordinate
is canonical after radial compression, but it is not yet the full-source
operator lift requested by ledger 3071. Its positive Clark bulk controls only
the norm channel.

The missing additional comparison channel is now identified structurally:
retain the (C_{\mathbb Q}^{1})-valued fiber before Mellin compression,
together with the action of the rational diagonal and Fourier–Poisson sewing
on that fiber.

This may explain why repeated scalar and finite-matrix enlargements remained
flat. They all lived after the norm-one fiber had been integrated out.

## The correct next object

Construct a fiber-valued radial state

\[
\Psi(r)\in\mathcal H(C_{\mathbb Q}^{1}),
\qquad r=\log|x|,
\]

and a source-derived boundary distribution (Delta_{\mathbb Q}(r)) acting on
the same fiber. The doubled Green form must be computed for (Psi) before
pairing with the fiber vacuum.

Only after that calculation may one apply the scalar compression

\[
\Psi(r)\longmapsto
\langle\Delta_{\mathbb Q}(r),\Psi(r)\rangle.
\]

The decisive gate is whether Fourier–Poisson sewing supplies a nontrivial
fiber boundary form or whether the standard vacuum occupies only the trivial
fiber representation. In the latter case, the extra channel again collapses
and provides no RH force.

## Scope

This theorem identifies information lost by Mellin radialization. It does not
prove that the distinguished theta state has a nonzero component in every
fiber mode, nor that retaining the fiber confines zeros.

## Verification

The checker uses the minimal two-point fiber to verify that radial compression
and its Gram form annihilate a nonzero angular mode.
