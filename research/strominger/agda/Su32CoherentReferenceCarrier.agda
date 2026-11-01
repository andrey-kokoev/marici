{-# OPTIONS --safe --cubical --guardedness #-}
module Su32CoherentReferenceCarrier where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import NativeSharedReaderJoin
import Su32JoinGeometry as Geometry

-- Checked geometric dictionary, not a charged-cell signal-transfer rule.
physicalReference : Reference → Geometry.Cell
physicalReference P+ = Geometry.pRef false
physicalReference P- = Geometry.pRef true
physicalReference E+ = Geometry.eRef false
physicalReference E- = Geometry.eRef true
other-comparison-shares-P+ : Geometry.otherP ≡ false
other-comparison-shares-P+ = refl

module Context (registry : Reference → Bool) where
  module P = Prepared registry
  module R = P.R
  module C = P.J
  module Native = P.D

  -- The second actual comparison uses the shared P+ reference, not a
  -- fresh external payload. It has its own two native channel premises.
  minusRef : Bool → Reference
  minusRef false = P+
  minusRef true = E-
  minusChannel : G.Package
  minusChannel = N.Pi-package Bool (λ i → P.input (minusRef i))
  minus-derivation : R.Resolve minusChannel
  minus-derivation = R.apply (N.P-kind , Bool , (λ i → P.input (minusRef i)))
    (λ { (lift i) → snd (R.premise (P.preparation , P.preparation-derivation) (lift (minusRef i))) })
  module D = Native.Join (RecordAt P+) (P.channel false) minusChannel
    (λ x → x false) (λ x → x false) refl
  dD : R.Resolve D.result
  dD = D.derive (P.channel-derivation false) minus-derivation

  Common : Type
  Common = RecordAt P+ × RecordAt E+
  commonC : N.Ty C.result → Common
  commonC z = C.left z false , C.left z true
  commonD : N.Ty D.result → Common
  commonD z = D.left z false , D.left z true

  -- Raw Pi allows both packets to vary INDEPENDENTLY on its whole carrier.
  rawFamily : Bool → G.Package
  rawFamily false = C.result
  rawFamily true = D.result
  rawConsumer : G.Package
  rawConsumer = N.Pi-package Bool rawFamily
  raw-derivation : R.Resolve rawConsumer
  raw-derivation = R.apply (N.P-kind , Bool , rawFamily)
    (λ { (lift false) → P.admitted-join ; (lift true) → dD })

  -- Simultaneous common-record constraint, not agreement at one point only.
  module Consumer = Native.Join Common C.result D.result commonC commonD refl
  dConsumer : R.Resolve Consumer.result
  dConsumer = Consumer.derive P.admitted-join dD
  whole-carrier-compatible : (z : N.Ty Consumer.result)
    → commonC (Consumer.left z) ≡ commonD (Consumer.right z)
  whole-carrier-compatible = Consumer.shared

  Records : Type
  Records = N.Ty P.preparation
  records : N.Ty Consumer.result → Records
  records z P+ = C.left (Consumer.left z) false
  records z P- = C.right (Consumer.left z) false
  records z E+ = C.left (Consumer.left z) true
  records z E- = D.right (Consumer.right z) true
  selected-records : N.value P.preparation ≡ records (N.value Consumer.result)
  selected-records = funExt λ { P+ → refl ; P- → refl ; E+ → refl ; E- → refl }

  -- Likewise, do not use a raw Pi to identify a preparation's values with
  -- those of its consumer. Retain their equality as part of the carrier.
  module Full = Native.Join Records P.preparation Consumer.result (λ x → x) records selected-records
  dFull : R.Resolve Full.result
  dFull = Full.derive P.preparation-derivation dConsumer
  whole-preparation-compatible : (z : N.Ty Full.result)
    → Full.left z ≡ records (Full.right z)
  whole-preparation-compatible = Full.shared

  -- All four physically named records are read, not just the output port.
  physicalRecords : N.Ty Full.result → Reference → Geometry.Cell × Bool
  physicalRecords z r = physicalReference r , RecordAt.payload (Full.left z r)

module Counterexample where
  module Z = Context (λ _ → false)
  changedLeft : N.Ty (Z.P.channel false)
  changedLeft false = record-at true
  changedLeft true = record-at false
  changedRight : N.Ty Z.minusChannel
  changedRight false = record-at true
  changedRight true = record-at false
  changedD : N.Ty Z.D.result
  changedD = (changedLeft , changedRight , refl) , N.value Z.D.provenance
  inconsistent : N.Ty Z.rawConsumer
  inconsistent false = N.value Z.C.result
  inconsistent true = changedD
  raw-pi-does-not-imply-agreement :
    Z.commonC (inconsistent false) ≡ Z.commonD (inconsistent true) → ⊥
  raw-pi-does-not-imply-agreement p = false≢true (cong (λ q → RecordAt.payload (fst q)) p)
