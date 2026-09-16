# Fourier response graph and Evans membership gate

```rzk
#lang rzk-1

#define nima-operator-graph
  (Response : U)
  (turn : Response -> Response)
  : U
  := Sigma (incoming : Response), Response

#define nima-in-operator-graph
  (Response : U)
  (turn : Response -> Response)
  (boundary : nima-operator-graph Response turn)
  : U
  := second boundary = turn (first boundary)

#define nima-source-response-membership
  (Source Response : U)
  (response : Source -> Response)
  (fourier : Source -> Source)
  (turn : Response -> Response)
  (intertwining : (g : Source) -> response (fourier g) = turn (response g))
  (g : Source)
  : nima-in-operator-graph Response turn
      (response g, response (fourier g))
  := intertwining g

#define nima-Evans-membership
  (Response : U)
  (turn : Response -> Response)
  (evansIncoming evansOutgoing : Response)
  : U
  := evansOutgoing = turn evansIncoming

#define nima-four-independent-matrix-unit-tests
  (Equality : U)
  : U
  := Sigma (_11 : Equality),
       Sigma (_12 : Equality),
       Sigma (_21 : Equality), Equality

#define nima-all-four-tests
  (Equality : U)
  (e11 e12 e21 e22 : Equality)
  : nima-four-independent-matrix-unit-tests Equality
  := (e11, (e12, (e21, e22)))

#data NimaFourierSewingEstablished
  := nima-oriented-radial-sewing-derived
  | nima-semilocal-Tate-sewing-unitary-order-four
  | nima-place-cutoff-naturality
  | nima-logarithmic-connection-self-adjoint
  | nima-logarithmic-connection-commutes-with-sewing
  | nima-all-seam-response-chart-invertible-on-image
  | nima-response-graph-maximal-isotropic

#define nima-current-Fourier-sewing-status : NimaFourierSewingEstablished
  := nima-response-graph-maximal-isotropic

#data NimaPrimeCellNormalizationStatus
  := nima-even-wall-column-fixed
  | nima-odd-Stokes-column-fixed
  | nima-linear-prime-comparison-fixed
  | nima-no-free-alpha-parameter
  | nima-quadratic-representation-equality-missing

#define nima-current-prime-cell-normalization-status
  : NimaPrimeCellNormalizationStatus
  := nima-quadratic-representation-equality-missing

#data NimaEvansMembershipBoundary
  := nima-source-response-vectors-lie-in-graph
  | nima-Evans-incoming-projection-does-not-prove-outgoing-equation
  | nima-maximal-isotropy-does-not-imply-Evans-membership
  | nima-determinant-equality-does-not-imply-four-matrix-unit-equality
  | nima-pullback-defining-source-metric-would-be-circular

#define nima-current-Evans-membership-boundary
  : NimaEvansMembershipBoundary
  := nima-maximal-isotropy-does-not-imply-Evans-membership

#data NimaCurrentRHLocalGate
  := nima-diagonal-endpoint-energy-tests
  | nima-off-diagonal-real-cross-correlation-test
  | nima-off-diagonal-oriented-linking-test
  | nima-parameter-free-four-matrix-unit-Green-equality
  | nima-uniform-prime-shell-closure

#define nima-first-current-RH-local-gate : NimaCurrentRHLocalGate
  := nima-parameter-free-four-matrix-unit-Green-equality
```
