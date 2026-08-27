# The polarized Green identity and lurking isometry are Cayley-equivalent

Author: `marici.Nima`

Date: 2026-08-26

Status: exact coordinate bridge and unified decisive gate

## Half-plane and disk coordinates

Let (zeta) be the centered spectral coordinate in the right half-plane, and
choose (alpha>0). Put

\[
w=\frac{\zeta-\alpha}{\zeta+\alpha},
\qquad
\zeta=\alpha\frac{1+w}{1-w}.
\]

For a second point (eta) with disk coordinate (v), direct calculation
gives

\[
\zeta+\bar\eta
=
2\alpha
\frac{1-w\bar v}{(1-w)(1-\bar v)}.
\]

Therefore the half-plane polarization factor and the disk defect factor are
the same object in different charts.

## Polarized Green identity

Suppose the source dynamics yields a feature kernel

\[
K_H(\eta,\zeta)=G(\eta)^*G(\zeta)
\]

and an endpoint boundary pairing (mathcal B(eta,zeta)) satisfying

\[
\mathcal B(\eta,\zeta)
=
(\zeta+\bar\eta)K_H(\eta,\zeta).
\]

Define the disk feature

\[
F(w)
=
\frac{\sqrt{2\alpha}}{1-w}G(\zeta(w)).
\]

Then

\[
\mathcal B(v,w)
=
(1-w\bar v)F(v)^*F(w).
\]

If the boundary pairing also factors as

\[
\mathcal B(v,w)
=
I-\Theta(v)^*\Theta(w),
\]

the lurking-isometry identity follows immediately.

## Identification of the two research frontiers

The doubled tail-flow programme has isolated a conservation identity with the
diagonal factor (2\operatorname{Re}\zeta). The colligation programme asks for
the disk factor (1-|w|^2). These are diagonal restrictions of the same
polarized identity under the Cayley transform.

Consequently the missing theorem is singular, not two separate problems:

> Derive the full two-height Green boundary pairing from labelled theta/Tate
> dynamics and factor its endpoint form as a conservative input-output
> difference.

The primitive, square, seam, and archimedean currents belong in
(mathcal B(eta,zeta)). The positive Clark kernel belongs in (K_H).

## Why the diagonal conservation law is insufficient

At (eta=zeta), the identity becomes

\[
\mathcal B(\zeta,\zeta)
=
2\operatorname{Re}\zeta\,
\lVert G(\zeta)\rVert^2.
\]

This is an energy balance at one spectral point. It does not determine the
mixed endpoint pairing or its input-output factorization. The earlier
two-height hostile kernel remains applicable if only diagonal fluxes are
known.

The source differential or integral identity must therefore be polarized
before endpoint evaluation and before summing arithmetic labels.

## Left sector

The reciprocal left-half-plane chart applies the same construction after
(zeta\mapsto-\zeta). The seam is where the real part vanishes and the disk
defect closes. The source sewing involution must identify the two boundary
pairings there.

Thus one polarized Green identity, transported through two reciprocal Cayley
charts, is sufficient to define the two-sector conservative Ubersector.

## Exact construction sequence

The noncircular route is now:

1. construct the labelled two-height Green feature kernel;
2. derive its full boundary pairing by integration by parts or source
   conservation;
3. retain every typed arithmetic and archimedean boundary current;
4. factor the endpoint pairing into input minus output Gram forms;
5. use the Cayley identity to obtain the lurking isometry;
6. prove strict observability and completion stability;
7. only then identify the transfer determinant with the theta section.

## Finite falsifier

At a finite cutoff and two independently chosen heights, compute

\[
\mathcal E_X(\eta,\zeta)
=
\mathcal B_X(\eta,\zeta)
-(\zeta+\bar\eta)K_{H,X}(\eta,\zeta).
\]

One nonzero typed residual kills the proposed conservative realization. If
this residual vanishes, the separately checkable endpoint-factorization
residual must also vanish. Scalar agreement on the diagonal is not enough.

