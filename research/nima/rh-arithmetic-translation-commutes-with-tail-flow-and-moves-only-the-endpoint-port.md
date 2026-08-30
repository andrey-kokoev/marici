# Arithmetic translation commutes with tail flow and moves only the endpoint port

Author: `marici.Nima`

Date: 2026-08-26

Status: exact passive-node intertwiner and boundary natural transformation

## Interior commutation

Let

\[
L_\zeta=\partial_q+\zeta
\]

be the tail-flow operator, and let forward scale translation be

\[
(S_pG)(q)=G(q+p).
\]

Differentiation commutes with translation, so

\[
L_\zeta S_p=S_pL_\zeta.
\]

Consequently, if

\[
L_\zeta G=-f,
\]

then

\[
L_\zeta(S_pG)=-S_pf.
\]

The translated tail remains an exact solution with translated forcing. The
sum-and-difference quadrature ports translate naturally as well.

## Endpoint noncommutation

Let $E_0$ evaluate a state at the endpoint. Then

\[
E_0S_pG=G(p)=E_pG.
\]

Thus the passive node intertwines arithmetic translation only if its endpoint
observer moves with the cut. Keeping the observer fixed at zero produces the
exact boundary defect

\[
(E_p-E_0)G
=
G(p)-G(0).
\]

Using the tail equation,

\[
G(p)-G(0)
=
-\int_0^p
\left(
\zeta G(q)+f(q)
\right)dq.
\]

This is the endpoint incidence map carried by the removed interval.

## Polarized interval identity

For two parameters and their tail states, integration over the removed
interval gives

\[
(\zeta+\bar\eta)
\int_0^pG_\eta(q)^*G_\zeta(q)\,dq
=
G_\eta(0)^*G_\zeta(0)
-G_\eta(p)^*G_\zeta(p)
-\int_0^p
\left(
f_\eta^*G_\zeta
+G_\eta^*f_\zeta
\right)dq.
\]

This is precisely the supply carried by the seam interval. The bulk
differential operator contributes no commutator residual.

## Categorical square

There are two valid presentations:

```text
translate source by p
  -> solve the same tail-flow equation
  -> observe at the new endpoint 0

solve the original tail-flow equation
  -> move the endpoint observer from 0 to p
  -> emit the intervening seam incidence
```

The comparison cell consists of the moving endpoint together with the
oriented interval carrier. Deleting either makes the square fail.

## Prime-power specialization

For $p=k\log\ell$, this gives the exact arithmetic action on the passive tail
node. Prime transport does not alter the differential law. It changes the
boundary presentation by moving the endpoint through a labelled scale
interval.

Therefore the primitive and square currents must enter through the weighted
sum of endpoint-incidence intervals, not through a modification of the tail
generator.

## Consequence

Two possible locations for an arithmetic supply anomaly are now closed:

- the tail--seam cut is functorial under staged translation;
- the interior tail-flow operator commutes with translation.

The remaining arithmetic gate is completion of the weighted endpoint
incidences and their compatibility with reciprocal modular sewing.

## Finite falsifiers

The intertwiner fails if:

- $L_\zeta S_pG\ne S_pL_\zeta G$;
- the endpoint is kept fixed without the interval incidence;
- the incidence has the wrong orientation;
- the polarized interval Green identity fails;
- prime-power weights are applied after erasing the interval labels.

The checker verifies the operator commutation, endpoint defect, and polarized
interval identity exactly on rational polynomial sources.

