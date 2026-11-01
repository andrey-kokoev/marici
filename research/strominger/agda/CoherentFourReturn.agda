{-# OPTIONS --safe --cubical --guardedness #-}
module CoherentFourReturn where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.GroupoidLaws using (cong-∙)
open import Cubical.Foundations.Transport using (transportComposite)
open import Cubical.Foundations.SIP
open import Cubical.Data.Bool.Base
open import Cubical.Data.Bool.Properties using (isSetBool)
open import Cubical.Data.Sigma.Properties
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; ∣_∣₁; squash₁)
import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Structures.Pointed
open import Cubical.Structures.Function
import DependentFourReturn as Return

-- The indexing object is a set; the state type below need not be a set.
Four : Type
Four = Σ Bool (λ _ → Bool)
pattern q0 = false , false
pattern q1 = false , true
pattern q2 = true , false
pattern q3 = true , true

four-elim : ∀ {ℓ} {P : Four → Type ℓ}
  → P q0 → P q1 → P q2 → P q3 → (x : Four) → P x
four-elim a b c d q0 = a
four-elim a b c d q1 = b
four-elim a b c d q2 = c
four-elim a b c d q3 = d

next : Four → Four
next q0 = q1
next q1 = q2
next q2 = q3
next q3 = q0

four-next : (x : Four) → next (next (next (next x))) ≡ x
four-next = four-elim refl refl refl refl

previous : Four → Four
previous x = next (next (next x))

nextEquiv : Four ≃ Four
nextEquiv = isoToEquiv (iso next previous four-next four-next)

rotate : Four → Four → Four
rotate k q0 = k
rotate k q1 = next k
rotate k q2 = next (next k)
rotate k q3 = previous k

neg : Four → Four
neg q0 = q0
neg q1 = q3
neg q2 = q2
neg q3 = q1

rotate-right : (k x : Four) → rotate k (rotate (neg k) x) ≡ x
rotate-right q0 = four-elim refl refl refl refl
rotate-right q1 = four-elim refl refl refl refl
rotate-right q2 = four-elim refl refl refl refl
rotate-right q3 = four-elim refl refl refl refl

rotate-left : (k x : Four) → rotate (neg k) (rotate k x) ≡ x
rotate-left q0 = four-elim refl refl refl refl
rotate-left q1 = four-elim refl refl refl refl
rotate-left q2 = four-elim refl refl refl refl
rotate-left q3 = four-elim refl refl refl refl

rotateEquiv : Four → Four ≃ Four
rotateEquiv k = isoToEquiv (iso (rotate k) (rotate (neg k)) (rotate-right k) (rotate-left k))

rotate-commutes : (k x : Four) → rotate k (next x) ≡ next (rotate k x)
rotate-commutes k q0 = refl
rotate-commutes k q1 = refl
rotate-commutes k q2 = refl
rotate-commutes k q3 = sym (four-next k)

Index : Type₁
Index = Σ Type (λ T → T → T)

base : Index
base = Four , next

-- Univalent moduli of oriented four-cycles: the connected component of base.
FourTorsor : Type₁
FourTorsor = Σ Index (λ X → ∥ base ≡ X ∥₁)

point : FourTorsor
point = base , ∣ refl ∣₁

Centralizer : Type
Centralizer = Σ (Four ≃ Four) (λ e → (x : Four) → e .fst (next x) ≡ next (e .fst x))

classify : (c : Centralizer) (x : Four) → c .fst .fst x ≡ rotate (c .fst .fst q0) x
classify (e , h) q0 = refl
classify (e , h) q1 = h q0
classify (e , h) q2 = h q1 ∙ cong next (h q0)
classify (e , h) q3 = h q2 ∙ cong next (h q1 ∙ cong next (h q0))

isSetFour : isSet Four
isSetFour = isSetΣ isSetBool (λ _ → isSetBool)

centralizerIso : Iso Centralizer Four
centralizerIso .Iso.fun c = c .fst .fst q0
centralizerIso .Iso.inv k = rotateEquiv k , rotate-commutes k
centralizerIso .Iso.rightInv k = refl
centralizerIso .Iso.leftInv c =
  Σ≡Prop (λ e → isPropΠ (λ x → isSetFour _ _))
    (equivEq (funExt (λ x → sym (classify c x))))

-- This identifies ALL loops, not just four exhibited permutations.
indexLoops : (base ≡ base) ≃ Centralizer
indexLoops = invEquiv (SIP
  (functionUnivalentStr+ pointedEquivAction pointedTransportStr
    PointedEquivStr pointedUnivalentStr) base base)

torsorLoops : (point ≡ point) ≃ Four
torsorLoops = compEquiv (invEquiv (Σ≡PropEquiv (λ _ → squash₁)))
  (compEquiv indexLoops (isoToEquiv centralizerIso))

connected : (x : FourTorsor) → ∥ point ≡ x ∥₁
connected x = PT.rec squash₁
  (λ p → ∣ Σ≡Prop (λ _ → squash₁) p ∣₁) (x .snd)

pointLoopsSet : isSet (point ≡ point)
pointLoopsSet = isOfHLevelRespectEquiv 2 (invEquiv torsorLoops) isSetFour

torsorGroupoid : isGroupoid FourTorsor
torsorGroupoid x y = PT.rec2 isPropIsSet
  (λ p q → transport (λ i → isSet (p i ≡ q i)) pointLoopsSet)
  (connected x) (connected y)

carrier : FourTorsor → Type
carrier x = x .fst .fst

label : (point ≡ point) → Four
label = torsorLoops .fst

label-transport : (p : point ≡ point) → label p ≡ transport (cong carrier p) q0
label-transport p = refl

label-compose : (p q : point ≡ point)
  → label (p ∙ q) ≡ rotate (label q) (label p)
label-compose p q =
  cong (λ r → transport r q0) (cong-∙ carrier p q)
  ∙ transportComposite (cong carrier p) (cong carrier q) q0
  ∙ classify (indexLoops .fst (cong fst q)) (label p)

-- The classified automorphisms compose by cyclic addition, not Klein-four.
rotate-compose : (k l x : Four)
  → rotate k (rotate l x) ≡ rotate (rotate k l) x
rotate-compose k l = classify
  (compEquiv (rotateEquiv l) (rotateEquiv k) ,
   λ x → cong (rotate k) (rotate-commutes l x) ∙ rotate-commutes k (rotate l x))

-- An explicit univalent successor-preserving index loop. Its reverse is the
-- generator whose transport rotates the cycle forward (sections are contravariant).
indexLoop : base ≡ base
indexLoop i .fst = ua nextEquiv i
indexLoop i .snd x = ua-glue nextEquiv i
  (λ { (i = i0) → next x })
  (inS (next (ua-unglue nextEquiv i x)))

generator : point ≡ point
generator i = indexLoop (~ i) ,
  isProp→PathP {B = λ j → ∥ base ≡ indexLoop (~ j) ∥₁}
    (λ j → squash₁) ∣ refl ∣₁ ∣ refl ∣₁ i

generator-label : label generator ≡ q3
generator-label = ~uaβ nextEquiv q0

-- A homotopy-coherent action is a family over the classifying space,
-- together with identification of its fibre. Transport supplies higher laws.
record CoherentC4Action {ℓ : Level} (X : Type ℓ) : Type (ℓ-suc ℓ) where
  field
    Fibres : FourTorsor → Type ℓ
    atPoint : Fibres point ≃ X

module Action {ℓ : Level} {S : Type ℓ} (G : S → S) where
  open Return.General G using (Per4; shift)

  Diagram : Index → Type ℓ
  Diagram (T , successor) = Σ (T → S) (λ v → (t : T) → G (v t) ≡ v (successor t))

  -- A family over the torsor space carries transport along all its paths and
  -- all higher paths. No truncation/proof irrelevance is applied to S.
  family : FourTorsor → Type ℓ
  family X = Diagram (X .fst)

  Cycle : Type ℓ
  Cycle = family point

  rotateCycle : Cycle → Cycle
  rotateCycle (v , e) = (λ x → v (next x)) , (λ x → e (next x))

  rotation-over-generator : (c : Cycle)
    → PathP (λ i → family (generator i)) c (rotateCycle c)
  rotation-over-generator (v , e) i =
    (λ x → v (ua-unglue nextEquiv (~ i) x)) ,
    (λ x → e (ua-unglue nextEquiv (~ i) x))

  generator-computes : (c : Cycle)
    → subst family generator c ≡ rotateCycle c
  generator-computes c = fromPathP (rotation-over-generator c)

  Chain : Type ℓ
  Chain = Σ S (λ a →
    Σ (singl (G a)) (λ b →
    Σ (singl (G (b .fst))) (λ c →
    Σ (singl (G (c .fst))) (λ d → G (d .fst) ≡ a))))

  cycleChain : Iso Cycle Chain
  cycleChain .Iso.fun (v , e) = v q0 , (v q1 , e q0) , (v q2 , e q1) , (v q3 , e q2) , e q3
  cycleChain .Iso.inv (a , (b , p) , (c , q) , (d , r) , s) =
    four-elim a b c d , four-elim p q r s
  cycleChain .Iso.rightInv x = refl
  cycleChain .Iso.leftInv (v , e) i .fst q0 = v q0
  cycleChain .Iso.leftInv (v , e) i .fst q1 = v q1
  cycleChain .Iso.leftInv (v , e) i .fst q2 = v q2
  cycleChain .Iso.leftInv (v , e) i .fst q3 = v q3
  cycleChain .Iso.leftInv (v , e) i .snd q0 = e q0
  cycleChain .Iso.leftInv (v , e) i .snd q1 = e q1
  cycleChain .Iso.leftInv (v , e) i .snd q2 = e q2
  cycleChain .Iso.leftInv (v , e) i .snd q3 = e q3

  chainPer4 : Iso Chain Per4
  chainPer4 = Σ-cong-iso-snd (λ a →
    compIso (Σ-contractFstIso (isContrSingl (G a)))
      (compIso (Σ-contractFstIso (isContrSingl (G (G a))))
        (Σ-contractFstIso (isContrSingl (G (G (G a)))))))

  cyclePer4 : Iso Cycle Per4
  cyclePer4 = compIso cycleChain chainPer4

  fibreEquiv : family point ≃ Per4
  fibreEquiv = isoToEquiv cyclePer4

  normal : Per4 → Cycle
  normal = cyclePer4 .Iso.inv

  -- Generator compatibility with the ORIGINAL canonical shift. This is not
  -- obtained by declaring an unrelated action on an equivalent type.
  normal-shift : (x : Per4) → normal (shift x) ≡ rotateCycle (normal x)
  normal-shift (a , p) i .fst q0 = G a
  normal-shift (a , p) i .fst q1 = G (G a)
  normal-shift (a , p) i .fst q2 = G (G (G a))
  normal-shift (a , p) i .fst q3 = p i
  normal-shift (a , p) i .snd q0 = refl
  normal-shift (a , p) i .snd q1 = refl
  normal-shift (a , p) i .snd q2 j = p (i ∧ j)
  normal-shift (a , p) i .snd q3 j = G (p (i ∨ j))

  generatorOnPer4 : Per4 → Per4
  generatorOnPer4 x = cyclePer4 .Iso.fun (subst family generator (normal x))

  generator-is-shift : (x : Per4) → generatorOnPer4 x ≡ shift x
  generator-is-shift x =
    cong (cyclePer4 .Iso.fun)
      (generator-computes (normal x) ∙ sym (normal-shift x))
    ∙ cyclePer4 .Iso.rightInv (shift x)

  coherentAction : CoherentC4Action Per4
  coherentAction .CoherentC4Action.Fibres = family
  coherentAction .CoherentC4Action.atPoint = fibreEquiv
