{-# OPTIONS --safe --cubical --guardedness #-}
module Su32RecordReaderClassification where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using
  (isSetRetract; isSetΣ; isSetΠ; isSet×; isPropΠ; isProp×)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sigma.Properties using (ΣPathP; Σ≡Prop)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (isSetBool; false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import Su32JoinGeometry as Geometry
open import Cubical.Functions.Embedding using (isEmbedding; injEmbedding)
open import NativeSharedReaderJoin
import Su32CoherentReferenceCarrier as Coherent

record-set : (r : Reference) → isSet (RecordAt r)
record-set r = isSetRetract RecordAt.payload record-at (λ _ → refl) isSetBool

-- A general lemma about the EXISTING retained join, not proof irrelevance
-- of Resolve. Only current value loops at set-valued operands are props.
module JoinSets (Admit : G.Package → Type₁) (E : Type) (a b : G.Package)
  (rA : N.Ty a → E) (rB : N.Ty b → E)
  (p : rA (N.value a) ≡ rB (N.value b))
  (setA : isSet (N.Ty a)) (setB : isSet (N.Ty b)) (setE : isSet E) where
  module D = Derived Admit
  module J = D.Join E a b rA rB p
  loop-prop : (i : Bool) → isProp (N.Ty (J.loop i))
  loop-prop false = setA (N.value a) (N.value a)
  loop-prop true = setB (N.value b) (N.value b)
  provenance-prop : isProp (N.Ty J.provenance)
  provenance-prop = isPropΠ loop-prop
  carrier-set : isSet (N.Ty J.result)
  carrier-set = isSetΣ
    (isSetΣ setA (λ x → isSetΣ setB (λ y → isProp→isSet (setE (rA x) (rB y)))))
    (λ _ → isProp→isSet provenance-prop)
  ext : (z w : N.Ty J.result) → J.left z ≡ J.left w → J.right z ≡ J.right w → z ≡ w
  ext z w x y = Σ≡Prop (λ _ → provenance-prop)
    (ΣPathP (x , ΣPathP (y , isProp→PathP (λ i → setE (rA (x i)) (rB (y i))) (J.shared z) (J.shared w))))

module Classified (registry : Reference → Bool) where
  module K = Coherent.Context registry
  module P = K.P
  module R = K.R
  module C = K.C
  module D = K.D
  module U = K.Consumer
  module F = K.Full

  channel-set : (side : Bool) → isSet (N.Ty (P.channel side))
  channel-set side = isSetΠ (λ i → record-set (P.reference side i))
  minus-set : isSet (N.Ty K.minusChannel)
  minus-set = isSetΠ (λ i → record-set (K.minusRef i))
  records-set : isSet K.Records
  records-set = isSetΠ record-set

  module CS = JoinSets P.Seeds (RecordAt E+) (P.channel false) (P.channel true)
    (P.readShared false) (P.readShared true) refl
    (channel-set false) (channel-set true) (record-set E+)
  module DS = JoinSets P.Seeds (RecordAt P+) (P.channel false) K.minusChannel
    (λ x → x false) (λ x → x false) refl
    (channel-set false) minus-set (record-set P+)
  module US = JoinSets P.Seeds K.Common C.result D.result K.commonC K.commonD refl
    CS.carrier-set DS.carrier-set (isSet× (record-set P+) (record-set E+))
  module FS = JoinSets P.Seeds K.Records P.preparation U.result (λ x → x) K.records K.selected-records
    records-set US.carrier-set records-set

  -- The four-record reader determines every channel value. Shared-reader
  -- paths determine duplicate fields; sethood determines remaining loops.
  consumer-injective : (z w : N.Ty U.result) → K.records z ≡ K.records w → z ≡ w
  consumer-injective z w h = US.ext z w c-eq d-eq
    where
    cz = U.left z
    cw = U.left w
    dz = U.right z
    dw = U.right w
    eq : (r : Reference) → K.records z r ≡ K.records w r
    eq r = cong (λ f → f r) h
    c-left : C.left cz ≡ C.left cw
    c-left = funExt λ { false → eq P+ ; true → eq E+ }
    c-right : C.right cz ≡ C.right cw
    c-right = funExt λ { false → eq P- ; true → sym (C.shared cz) ∙ eq E+ ∙ C.shared cw }
    c-eq : cz ≡ cw
    c-eq = CS.ext cz cw c-left c-right
    dp : D.left dz false ≡ D.left dw false
    dp = sym (cong fst (U.shared z)) ∙ eq P+ ∙ cong fst (U.shared w)
    de : D.left dz true ≡ D.left dw true
    de = sym (cong snd (U.shared z)) ∙ eq E+ ∙ cong snd (U.shared w)
    d-left : D.left dz ≡ D.left dw
    d-left = funExt λ { false → dp ; true → de }
    d-right : D.right dz ≡ D.right dw
    d-right = funExt λ { false → sym (D.shared dz) ∙ dp ∙ D.shared dw ; true → eq E- }
    d-eq : dz ≡ dw
    d-eq = DS.ext dz dw d-left d-right

  full-injective : (z w : N.Ty F.result) → F.left z ≡ F.left w → z ≡ w
  full-injective z w h = FS.ext z w h
    (consumer-injective (F.right z) (F.right w) (sym (F.shared z) ∙ h ∙ F.shared w))
  reader-embedding : isEmbedding F.left
  reader-embedding = injEmbedding records-set (full-injective _ _)

  -- Construct every compatible current value from its four records. These
  -- are values of a FIXED package, not newly seeded producer histories.
  plusE : (s : Bool) → K.Records → N.Ty (P.channel s)
  plusE false r false = r P+
  plusE false r true = r E+
  plusE true r false = r P-
  plusE true r true = r E+
  minusE : K.Records → N.Ty K.minusChannel
  minusE r false = r P+
  minusE r true = r E-
  makeC : K.Records → N.Ty C.result
  makeC r = (plusE false r , plusE true r , refl) , N.value C.provenance
  makeD : K.Records → N.Ty D.result
  makeD r = (plusE false r , minusE r , refl) , N.value D.provenance
  makeConsumer : K.Records → N.Ty U.result
  makeConsumer r = (makeC r , makeD r , refl) , N.value U.provenance
  records-compute : (r : K.Records) → r ≡ K.records (makeConsumer r)
  records-compute r = funExt λ { P+ → refl ; P- → refl ; E+ → refl ; E- → refl }
  restore : K.Records → N.Ty F.result
  restore r = (r , makeConsumer r , records-compute r) , N.value F.provenance

  normal : Iso (N.Ty F.result) K.Records
  Iso.fun normal = F.left
  Iso.inv normal = restore
  Iso.rightInv normal r = refl
  Iso.leftInv normal z = full-injective (restore (F.left z)) z refl

  -- A complete native filler, selected by the full-record reader. The
  -- comparison retains both operand derivations; it does not equate them.
  Filler : Type
  Filler = Σ (N.Ty F.result ≃ K.Records) (λ e →
    (equivFun e (N.value F.result) ≡ N.value P.preparation) ×
    ((z : N.Ty F.result) → equivFun e z ≡ F.left z))
  filler : Filler
  filler = isoToEquiv normal , refl , (λ _ → refl)
  filler-prop : isProp Filler
  filler-prop (e , p , h) (f , q , k) = Σ≡Prop
    (λ e → isProp× (records-set _ _) (isPropΠ (λ z → records-set _ _)))
    (equivEq (funExt (λ z → h z ∙ sym (k z))))
  filler-contractible : isContr Filler
  filler-contractible = filler , filler-prop filler
  rule : N.Rule
  rule = N.compare-kind , F.result , P.preparation , fst filler , fst (snd filler)
  admitted : R.Resolve (N.output rule)
  admitted = R.apply rule (λ { (lift true) → K.dFull ; (lift false) → P.preparation-derivation })

  -- Two context presentations in the same geometric frame. This swaps
  -- preparation/consumer ordering, NOT either original incidence path.
  module Reordered where
    module X = K.Native.Exchange K.Records P.preparation U.result (λ x → x) K.records K.selected-records
    module T = X.T
    target-set : isSet (N.Ty T.result)
    target-set = isSetRetract (Iso.inv X.law) (Iso.fun X.law) (Iso.rightInv X.law) FS.carrier-set
    target-injective : (z w : N.Ty T.result) → T.right z ≡ T.right w → z ≡ w
    target-injective z w h = sym (Iso.rightInv X.law z)
      ∙ cong (Iso.fun X.law) (full-injective (Iso.inv X.law z) (Iso.inv X.law w) h)
      ∙ Iso.rightInv X.law w
    Comparison : Type
    Comparison = Σ (N.Ty F.result ≃ N.Ty T.result) (λ e →
      (equivFun e (N.value F.result) ≡ N.value T.result) ×
      ((z : N.Ty F.result) → T.right (equivFun e z) ≡ F.left z))
    computed : Comparison
    computed = isoToEquiv X.law , X.selected-law , (λ _ → refl)
    comparison-prop : isProp Comparison
    comparison-prop (e , p , h) (f , q , k) = Σ≡Prop
      (λ e → isProp× (target-set _ _) (isPropΠ (λ z → records-set _ _)))
      (equivEq (funExt (λ z → target-injective _ _ (h z ∙ sym (k z)))))
    comparison-contractible : isContr Comparison
    comparison-contractible = computed , comparison-prop computed
    native : R.Resolve (N.output X.rule)
    native = X.derive P.preparation-derivation K.dConsumer

  physical-reader-injective : (z w : N.Ty F.result)
    → K.physicalRecords z ≡ K.physicalRecords w → z ≡ w
  physical-reader-injective z w h = full-injective z w
    (funExt (λ r → cong record-at (cong (λ f → snd (f r)) h)))

module PortOnlyCounterexample where
  module Z = Classified (λ _ → false)
  changed : Z.K.Records
  changed P+ = record-at false
  changed P- = record-at true
  changed E+ = record-at false
  changed E- = record-at false
  z0 z1 : N.Ty Z.F.result
  z0 = Z.restore (N.value Z.P.preparation)
  z1 = Z.restore changed
  ports : N.Ty Z.F.result → Geometry.Port × Geometry.Port
  ports _ = Geometry.fromPort (Geometry.Frame.cOut Geometry.frame) , Geometry.fromPort (Geometry.Frame.dOut Geometry.frame)
  same-ports : ports z0 ≡ ports z1
  same-ports = refl
  distinct-values : z0 ≡ z1 → ⊥
  distinct-values p = false≢true (cong (λ z → RecordAt.payload (Z.F.left z P-)) p)
