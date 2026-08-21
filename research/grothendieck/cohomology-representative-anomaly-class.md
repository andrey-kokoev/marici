# The class of alpha Omega is the cohomology-representative anomaly

Epistemic-graph event: 1342.

## Exact descent theorem

Let `S:C(G)->C(H)` be a graded map with boundary defect `Omega`.  Its dual
assignments define a genuine map

`H^n(H)->H^n(G)`

if and only if both conditions hold:

1. every target `n`-cocycle annihilates `Omega_(n+1)`;
2. for every target `(n-1)`-cochain `alpha`, the source cocycle
   `alpha Omega_n` is exact.

Under the first condition, `alpha Omega_n` is indeed a cocycle.  This follows
from the defect Bianchi identity

`D_H Omega+Omega D_G=0`,

because

`d_G(alpha Omega_n)=-(d_H alpha)Omega_(n+1)=0`.

For a change of target representative by the coboundary `d_H alpha`, direct
calculation gives

`S^*(d_H alpha)=d_G(S^*alpha)+alpha Omega_n`.

Hence the anomaly class

`tau_n(alpha)=[alpha Omega_n] in H^n(G)`

is exactly the obstruction to representative independence.  Vanishing of
all `tau_n(alpha)`, together with cocycle preservation, is necessary and
sufficient for cohomological pullback.

## Hostile control

In Ledger 1324's example, the target exact cocycle `[1 0]=d_H(1)` pulls back
to the nonzero source class `1`.  Here `tau_1(1)=1`, so the anomaly detects
the failure exactly.

## Hierarchy and physical scope

One selected cocycle requires only its own defect contraction to vanish.
A map on all cohomology classes additionally requires every anomaly class
`tau_n(alpha)` to vanish.  A strict chain map forces both automatically but
is stronger.

For five-site cosmology, changing a form by an exact term is harmless only
after this anomaly test passes in the frozen relative normalization.  Until
the physical boundary matrices exist, neither `Omega` nor `tau` is
source-evaluable.
