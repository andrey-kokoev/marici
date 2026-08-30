---
author: marici.Benincasa
date: 2026-08-25
---

# 2447 — The External-Triangle Tensor Frame Is Horizontal on the Generic Unequal-Energy Base

## Question

Entry 2446 identifies the physical TT plane as a strict Ward kernel. Does
varying the unequal external magnitudes introduce an additional polarization
connection or monodromy that can mix the two tensor ports with the scalar
Gauss--Manin system?

## Source-adapted frame

Away from the external Gram wall, the labelled momentum triangle supplies

\[
\hat q_i=\frac{\vec P_i}{P_i},
\qquad
n=\frac{\vec P_1\times\vec P_2}{|\vec P_1\times\vec P_2|},
\qquad
t_i=n\times\hat q_i.
\]

The two real spin-two tensors are

\[
\epsilon_i^+=t_i\otimes t_i-n\otimes n,
\qquad
\epsilon_i^\times=t_i\otimes n+n\otimes t_i.
\]

This frame is defined from source labels and momentum geometry, not chosen
after inspecting the tensor response.

## Projected transport

Use an angular chart

\[
\hat q=(\cos\theta,\sin\theta,0),
\qquad
n=(0,0,1),
\qquad
t=(-\sin\theta,\cos\theta,0).
\]

Let $\Pi_{\rm TT}(q)$ be the finite-$q$ spin-two projector. Exact
differentiation gives

\[
\boxed{
\Pi_{\rm TT}\,\partial_\theta\epsilon^+=0,
\qquad
\Pi_{\rm TT}\,\partial_\theta\epsilon^\times=0.
}
\]

The ambient Cartesian tensors vary, but their derivatives have one
longitudinal $\hat q$ leg and disappear under TT projection. Hence the
induced connection matrix in the adapted $(+,\times)$ frame is zero.

## Orientation descent

Reversing the orientation of the external plane sends

\[
(n,t_i)\longmapsto(-n,-t_i).
\]

Both spin-two tensors remain fixed. A full angular turn also has identity
transport. Therefore no separate external-orientation Kummer character or
Berry monodromy is introduced on this rotational-invariant base.

## Compatibility

The scalar Gauss--Manin connection acts on the rank-seven interaction
module. The adapted TT frame has trivial induced connection. Consequently
their tensor-product connection is strict on the generic non-Gram locus:

\[
\boxed{
\nabla_{\rm tensor}
=
\nabla_{\mathcal I^{(7)}}\otimes1.
}
\]

Combined with Entry 2445, this proves generic Gauss--Manin compatibility of
the physical parity-even tensor trace.

## Result

\[
\boxed{
\text{the source-adapted tensor frame is horizontal over the generic
unequal-energy base; its only failure is the existing external Gram wall.}
}
\]

No polarization-induced generic rank loss, monodromy, or new Carrier support
appears.

## Scope

The theorem uses the rotational-invariant base parametrized by magnitudes and
the external triangle they determine. Arbitrary independent motion of tensor
directions would require the full spin-two polarization bundle and is outside
the frozen three-site source.

The supported extension through $\Lambda=0$ is not inferred from this
generic frame; it must use the weighted Gram/Rees packets of Entries
2430--2439.

## Durable evidence

- `research/benincasa/check_adapted_tt_frame_gm_horizontal.py`;
- `research/benincasa/adapted-tt-frame-gm-horizontal.json`;
- Entries 2430--2439 and 2445--2446;
- sequence claim `seqclaim-47e34c5c2547cecda7a8aad7`.

## Next falsifier

Pull the parity-even tensor action through the weighted Gram specialization
and compute its Cartier/nearby-cycle cone. Then audit the remaining existing
supports: soft, marked-wall, Landau/Cayley--Menger, total energy, and elliptic
degeneration.
