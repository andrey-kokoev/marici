# CR1 support and analytic-readout independent assembly

```rzk
#lang rzk-1

#define nima-CR1-support-witness
  (Carrier CommonLine Parameters : U)
  (thetaSection : Parameters -> CommonLine)
  : U
  := Sigma (distinguishedCarrier : Parameters -> Carrier),
       Sigma (openPhysical : Carrier -> CommonLine),
       Sigma (closedPhysical : Carrier -> CommonLine),
       Sigma (_ : (x : Carrier) -> openPhysical x = closedPhysical x),
       ((s : Parameters) -> thetaSection s = openPhysical (distinguishedCarrier s))

#define nima-CR1-analytic-readout-witness
  (CommonLine Scalars : U)
  : U
  := Sigma (boundaryReadout : CommonLine -> Scalars),
       Sigma (zeroLine : CommonLine),
       Sigma (zeroScalar : Scalars),
       boundaryReadout zeroLine = zeroScalar

#define nima-CR1-work-mate
  (Parameters Work Scalars : U)
  : U
  := Parameters -> Work -> Scalars

#data NimaCR1PhysicalSourcePackageLayer
  := nima-support-geometry-layer
  | nima-independent-analytic-readout-layer
  | nima-zero-line-agreement-layer
  | nima-work-mate-layer
  | nima-assembled-physical-source-package

#define nima-CR1-independent-package
  (Support Readout ZeroAgreement WorkMate : U)
  : U
  := Sigma (_ : Support),
       Sigma (_ : Readout),
       Sigma (_ : ZeroAgreement), WorkMate

#define nima-assemble-CR1-independent-package
  (Support Readout ZeroAgreement WorkMate : U)
  (support : Support)
  (readout : Readout)
  (zeroAgreement : ZeroAgreement)
  (workMate : WorkMate)
  : nima-CR1-independent-package Support Readout ZeroAgreement WorkMate
  := (support, (readout, (zeroAgreement, workMate)))

#data NimaCR1SupportStatus
  := nima-diagonal-Kato-finite-carrier-constructed
  | nima-intrinsic-reflection-odd-unit-Gysin-constructed
  | nima-external-extraordinary-specialization-missing
  | nima-determinant-to-common-line-map-missing
  | nima-loaded-face-six-functor-BC-maps-missing

#define nima-current-CR1-support-status : NimaCR1SupportStatus
  := nima-external-extraordinary-specialization-missing

#data NimaCR1ReadoutStatus
  := nima-three-stratum-Weyl-interface-typed
  | nima-prime-shell-residual-interface-typed
  | nima-source-normalized-residual-totalization-missing
  | nima-Green-work-identification-missing

#define nima-current-CR1-readout-status : NimaCR1ReadoutStatus
  := nima-source-normalized-residual-totalization-missing

#data NimaCR1IndependentGate
  := nima-support-does-not-manufacture-readout
  | nima-readout-does-not-manufacture-support
  | nima-zero-line-agreement-is-separate
  | nima-formal-assembly-does-not-inhabit-source-package
  | nima-intrinsic-unit-does-not-supply-literal-face-BC

#define nima-current-CR1-independent-gate : NimaCR1IndependentGate
  := nima-formal-assembly-does-not-inhabit-source-package

#data NimaCR1FormalizationClosure
  := nima-safe-cubical-chain-closed
  | nima-no-holes-or-postulates
  | nima-seventeen-modules-typecheck
  | nima-physical-source-package-still-uninhabited

#define nima-current-CR1-formalization-closure : NimaCR1FormalizationClosure
  := nima-physical-source-package-still-uninhabited
```
