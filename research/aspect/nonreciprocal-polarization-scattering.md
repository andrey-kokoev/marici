# Nonreciprocal polarization transport and scattering

Owner: `marici.Aspect`

## Bounded question

How can losslessness, reciprocity, reverse propagation, polarization analysis,
and environment completion be tested independently for a two-port Jones
apparatus? The source and both spatial ports use the same declared laboratory
Jones basis `(H,V)` and a common energy normalization.

## Forward and reverse transport

Use the exact rotation

`R=[[3/5,-4/5],[4/5,3/5]]`.

It is orthogonal, hence preserves Jones norm. A reciprocal comparator has
forward transport `U=R` and reverse transport `V=R^T`; its round trip is the
identity. A Faraday-type nonreciprocal element has `U=R` and `V=R` in the same
laboratory basis. Its round trip is `R^2`, not the identity.

This statement depends on basis authority. If a reverse port is displayed in
a different handed frame, its coordinate transport must be applied before
testing reciprocity. Merely observing different matrices in two unrelated
frames proves nothing.

## Full scattering map

Let incoming amplitudes be `(a_left,a_right)` with each entry in `C^2`, and
outgoing amplitudes be `(b_left,b_right)`. With no reflection,

`b_left=V a_right`, `b_right=U a_left`,

so the four-dimensional scattering matrix is the block matrix

`S=[[0,V],[U,0]]`.

If `U` and `V` are orthogonal, `S` is orthogonal: total scattering is
lossless. In the declared common real port basis, reciprocity requires
`S=S^T`, equivalently `V=U^T`. The reciprocal comparator satisfies this; the
Faraday choice `V=U` does not. Thus total unitarity does not imply
reciprocity.

## Polarization-dependent loss and environment

A retained Jones map `A=diag(3/5,1)` attenuates only `H`. It is not unitary on
the retained polarization port. With environment coupling
`L=diag(4/5,0)`, the block dilation

`[[A,L],[-L,A]]`

is orthogonal on retained plus environment Jones spaces. The missing `16/25`
probability for an `H` input is environmental output, not destroyed state and
not recoverable by a downstream analyzer that cannot access the environment.

## Detector family and scalar-preserving hostile

One analyzer row `h=(1,0)` sends the distinct Jones vectors `(1,1)` and
`(1,-1)` to the same scalar amplitude. Rotating that row rotates its kernel;
it does not make it faithful. Two independent rows, fixed before observing
data and expressed in the same calibration frame, are minimally faithful on
the declared Jones `C^2` class. They remain blind to spatial, temporal, and
environment factors traced out before the class was declared.

## Constructor order

Polarization rotation and anisotropic attenuation generally do not commute.
The exact checker records the nonzero commutator of `R` and `A`. Reordering
them silently changes which laboratory polarization is attenuated. Likewise,
assuming that every reverse traversal applies the inverse rotation silently
replaces the nonreciprocal apparatus by the reciprocal comparator.

## Hostile falsifiers and boundary

- infer reciprocity from total scattering unitarity;
- compare forward and reverse matrices before transporting them to one port
  basis;
- assume reverse traversal cancels a Faraday rotation;
- identify a Jones state from one analyzer scalar;
- discard the loss environment while asserting retained unitarity;
- commute rotation and polarization-dependent loss.

All six are rejected by exact residuals. This finite real Jones model omits
dispersion, magneto-optic microscopic response, continuum modes, quantum
noise, and causal Kramers-Kronig completion.

Run `python research/aspect/checkers/nonreciprocal_polarization_scattering.py`.
The result is
`research/aspect/results/nonreciprocal_polarization_scattering.json`.
