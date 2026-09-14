# Kato determinant-line support bridge gate

```rzk
#lang rzk-1

#define nima-diagonal-finite-CR1-carrier (KatoConnector : U) : U
  := Sigma (_ : KatoConnector),
       Sigma (_ : KatoConnector),
       Sigma (_ : KatoConnector), KatoConnector

#define nima-diagonal-finite-CR1-carrier-witness
  (KatoConnector : U)
  (carrier : KatoConnector)
  : nima-diagonal-finite-CR1-carrier KatoConnector
  := (carrier, (carrier, (carrier, carrier)))

#define nima-kato-determinant-generator
  (KatoLine DeterminantLine : U)
  : U
  := Sigma (physicalPrimitive : KatoLine),
       Sigma (determinantGenerator : DeterminantLine),
       Sigma (physicalToDeterminant : KatoLine -> DeterminantLine),
       physicalToDeterminant physicalPrimitive = determinantGenerator

#define nima-kato-common-line-interpretation
  (KatoLine CommonLine : U)
  : U
  := Sigma (toCommonLine : KatoLine -> CommonLine),
       Sigma (zeroKatoLine : KatoLine),
       Sigma (zeroCommonLine : CommonLine),
       toCommonLine zeroKatoLine = zeroCommonLine

#define nima-identity-determinant-to-common-line
  (Line : U)
  : Line -> Line
  := \ x -> x

#define nima-identity-kato-common-line-interpretation
  (Line : U)
  (zero : Line)
  : nima-kato-common-line-interpretation Line Line
  := ((\ x -> x), (zero, (zero, refl)))

#define nima-kato-theta-comparison
  (Parameters KatoLine CommonLine : U)
  (distinguishedKatoClass : Parameters -> KatoLine)
  (thetaSection : Parameters -> CommonLine)
  (toCommonLine : KatoLine -> CommonLine)
  : U
  := (parameter : Parameters) ->
       thetaSection parameter = toCommonLine (distinguishedKatoClass parameter)

#define nima-kato-CR1-support-package
  (Parameters KatoLine DeterminantLine CommonLine : U)
  (distinguishedKatoClass : Parameters -> KatoLine)
  (thetaSection : Parameters -> CommonLine)
  : U
  := Sigma
       (generator : nima-kato-determinant-generator KatoLine DeterminantLine),
       Sigma
       (interpretation : nima-kato-common-line-interpretation KatoLine CommonLine),
       nima-kato-theta-comparison Parameters KatoLine CommonLine
         distinguishedKatoClass thetaSection (first interpretation)

#data NimaKatoBridgeEstablished
  := nima-global-Kato-connector-type-exists
  | nima-diagonal-finite-carrier-interpretation-exists
  | nima-determinant-generator-interface-exists
  | nima-Kato-support-package-implies-CR1-support-witness

#define nima-highest-established-Kato-bridge-layer : NimaKatoBridgeEstablished
  := nima-determinant-generator-interface-exists

#data NimaDeterminantToCommonDerivationScope
  := nima-identity-map-derivable-when-lines-definitionally-equal
  | nima-framed-line-map-derivable-from-explicit-equivalence
  | nima-abstract-common-line-has-no-canonical-map
  | nima-project-specific-normalization-remains-required

#define nima-current-determinant-map-derivation-scope
  : NimaDeterminantToCommonDerivationScope
  := nima-abstract-common-line-has-no-canonical-map

#data NimaKatoBridgeMissing
  := nima-source-derived-determinant-to-common-line-map
  | nima-distinguished-theta-comparison
  | nima-external-nearby-specialization-eF-to-unit
  | nima-ringed-endpoint-q-counit
  | nima-relative-dualizing-AW-counit

#define nima-first-missing-Kato-bridge-map : NimaKatoBridgeMissing
  := nima-source-derived-determinant-to-common-line-map

#data NimaKatoForbiddenPromotion
  := nima-diagonal-carrier-does-not-create-physical-line-map
  | nima-tautological-finite-BC-is-not-spatial-proper-BC
  | nima-numeric-unit-is-not-common-line-identification
  | nima-ordinary-Q-zero-cannot-be-extraordinary-Q-unit
  | nima-formal-coherence-is-not-geometric-inhabitation

#define nima-current-Kato-forbidden-promotion : NimaKatoForbiddenPromotion
  := nima-diagonal-carrier-does-not-create-physical-line-map

#data NimaEquivalentCR1FrontierPresentation
  := nima-nearby-cycle-spG-eF-equals-unit
  | nima-Kato-toCommonLine-plus-theta-comparison
  | nima-equivalence-between-presentations-not-yet-proved

#define nima-current-CR1-frontier-presentation
  : NimaEquivalentCR1FrontierPresentation
  := nima-equivalence-between-presentations-not-yet-proved

#data NimaAlphaRouteDisposition
  := nima-enlarged-endpoint-carrier-constructed
  | nima-perfect-can-var-and-Tor1-orientation-constructed
  | nima-ringed-q-projection-missing
  | nima-all-active-alpha-paths-blocked

#define nima-current-alpha-route-disposition : NimaAlphaRouteDisposition
  := nima-all-active-alpha-paths-blocked
```
