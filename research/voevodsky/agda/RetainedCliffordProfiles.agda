{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedCliffordProfiles where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true; _⊕_; _and_)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import NativeRetainedProfiles as Profiles
import BoundaryGeneratedQuestions as OwnerBoundary

-- Boolean sign is negative iff true. Grade labels the adjoint action; the
-- exact matrix/source-sector identification is independently audited in Python.
Grade = Bool × Bool
Signed = Bool × Grade
multiply : Signed → Signed → Signed
multiply (e , a , b) (d , c , f) = ((e ⊕ d) ⊕ (b and c)) , (a ⊕ c) , (b ⊕ f)
reverse-lift : Signed → Signed
reverse-lift (e , a , b) = e ⊕ (a and b) , a , b
compose-action : Grade → Grade → Grade
compose-action (a , b) (c , d) = a ⊕ c , b ⊕ d
forget-sign : Signed → Grade
forget-sign = snd
action-composition : (g h : Signed)
  → forget-sign (multiply g h) ≡ compose-action (forget-sign g) (forget-sign h)
action-composition (e , a , b) (d , c , f) = refl

-- Full syntax is retained. In particular a reversal node is not silently
-- canceled, nor is a multiplication tree replaced by its flattened word.
data History : Type where
  unit : History
  e1 e2 : History
  times : History → History → History
  reversal : History → History
lift-reading : History → Signed
lift-reading unit = false , false , false
lift-reading e1 = false , true , false
lift-reading e2 = false , false , true
lift-reading (times h k) = multiply (lift-reading h) (lift-reading k)
lift-reading (reversal h) = reverse-lift (lift-reading h)
action-reading : History → Grade
action-reading h = forget-sign (lift-reading h)
previous : History → History
previous (reversal h) = h
previous h = h
reversal-history-recovered : (h : History) → previous (reversal h) ≡ h
reversal-history-recovered h = refl
left-history : History → History
left-history (times h k) = h
left-history h = h
composition-history-recovered : (h k : History) → left-history (times h k) ≡ h
composition-history-recovered h k = refl

module N = Profiles.Native ℓ-zero
module G = N.G
-- Keep the actual owner source comparison and declared representation scope
-- attached. This does not turn the active word model into the full source.
data Scope : Type where active-word-sector-cl20-not-full-source : Scope
source-packet : G.Package
source-packet = G.encode-package (OwnerBoundary.retain-filler
  OwnerBoundary.fourQ OwnerBoundary.fourQ OwnerBoundary.swap-filler)
source-node : G.Node History
source-node = G.retain-node (N.N.expression source-packet) (N.N.value source-packet)
  (G.retain-node (G.atom-node Scope) active-word-sector-cl20-not-full-source (G.atom-node History))
module Readings = N.Two source-node unit lift-reading action-reading
module Grouped = N.Coarsen source-node unit lift-reading forget-sign
LR RL : History
LR = times e1 e2
RL = times e2 e1
same-action : action-reading LR ≡ action-reading RL
same-action = refl
different-lifts : lift-reading LR ≡ lift-reading RL → ⊥
different-lifts p = false≢true (cong fst p)
different-histories : LR ≡ RL → ⊥
different-histories p = different-lifts (cong lift-reading p)
retained-lift : (h : History)
  → Grouped.original-index (equivFun Grouped.source-to-groups h) ≡ lift-reading h
retained-lift h = refl
retained-history : (h : History)
  → invEq Grouped.source-to-groups (equivFun Grouped.source-to-groups h) ≡ h
retained-history = Grouped.recovered
is-unit : History → Bool
is-unit unit = true
is-unit _ = false
same-lift-distinct-history : unit ≡ times e1 e1 → ⊥
same-lift-distinct-history p = false≢true (sym (cong is-unit p))
same-lift : lift-reading unit ≡ lift-reading (times e1 e1)
same-lift = refl

-- A new obstruction: no multiplicative section can choose lifts from actions.
-- Every choice of signs for the two generator lifts still anticommutes.
Anticommute : Type
Anticommute = (e d : Bool) → multiply (e , true , false) (d , false , true)
  ≡ multiply (d , false , true) (e , true , false) → ⊥
anticommute : Anticommute
anticommute false false p = false≢true (cong fst p)
anticommute false true p = false≢true (sym (cong fst p))
anticommute true false p = false≢true (sym (cong fst p))
anticommute true true p = false≢true (cong fst p)
no-multiplicative-section : (choose : Grade → Signed)
  → ((g : Grade) → forget-sign (choose g) ≡ g)
  → ((g h : Grade) → choose (compose-action g h) ≡ multiply (choose g) (choose h)) → ⊥
no-multiplicative-section choose section law = anticommute
  (fst (choose (true , false))) (fst (choose (false , true)))
  (sym (cong₂ multiply shape1 shape2)
    ∙ sym (law (true , false) (false , true))
    ∙ law (false , true) (true , false)
    ∙ cong₂ multiply shape2 shape1)
  where
  shape1 : choose (true , false) ≡ (fst (choose (true , false)) , true , false)
  shape1 = cong (λ g → fst (choose (true , false)) , g) (section (true , false))
  shape2 : choose (false , true) ≡ (fst (choose (false , true)) , false , true)
  shape2 = cong (λ g → fst (choose (false , true)) , g) (section (false , true))
