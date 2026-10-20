{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardSourceLiftComposition where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua; ua-gluePath; uaInvEquiv)
open import Cubical.Foundations.HLevels using (isOfHLevelPathP')
open import Cubical.Relation.Nullary.Base using (¬_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open import NativeExtensionFamilyAudit using
  (Vertex; A; B; C; D; graphQ; pointQ; Seeds; root; sigma; sigma²; sigmaEquiv;
   sigma-not-pointed-self)
open import SourceIndexedExtensionFamilies using (vertex-is-set; moveOut)
open import RetainedPackageFeedback
import RetainedFeedbackCovariance as R
open import InternalSourceComparisons using (Mode; stay; exchange)
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- First compare the ACTUAL chosen univalent type paths. This is stronger
-- than observing sigma squared at vertices. Inverse equivalence equality
-- uses its underlying function, with equivalence evidence retained by equivEq.
sigma-inverse : sigmaEquiv ≡ invEquiv sigmaEquiv
sigma-inverse = equivEq refl
ua-inverse : ua sigmaEquiv ≡ sym (ua sigmaEquiv)
ua-inverse = cong ua sigma-inverse ∙ uaInvEquiv sigmaEquiv

-- Compare the dependent selected-value paths over that type-path square.
-- Their uniqueness uses the proved sethood of Vertex, NOT sethood of Code,
-- Complete, Seeds, Resolve, or retained history.
pointedPath : (x y : Vertex) → sigma x ≡ y → pointQ x ≡ pointQ y
pointedPath x y p i = remember graphQ
  (pack (atom (ua sigmaEquiv i)) (ua-gluePath sigmaEquiv p i))
pointed-inverse : (x y : Vertex) (p : sigma x ≡ y) (q : sigma y ≡ x)
  → pointedPath x y p ≡ sym (pointedPath y x q)
pointed-inverse x y p q j i = remember graphQ
  (pack (atom (ua-inverse j i)) (square j i))
  where
  square : PathP (λ j → PathP (λ i → ua-inverse j i) x y)
    (ua-gluePath sigmaEquiv p) (λ i → ua-gluePath sigmaEquiv q (~ i))
  square = isProp→PathP
    (λ j → isOfHLevelPathP' {A = λ i → ua-inverse j i} 1 vertex-is-set x y)
    (ua-gluePath sigmaEquiv p) (λ i → ua-gluePath sigmaEquiv q (~ i))

-- These match the original forward pointPath and case-defined backward lift
-- definitionally. No new pointPath choice replaces the implemented one.
forward-back-initial : (v : Vertex) (d : Resolve Seeds (pointQ v))
  → R.moveInitial v d ≡ R.backInitial v d
forward-back-initial A d = cong (λ p → subst (Resolve Seeds) p d)
  (pointed-inverse A B refl refl)
forward-back-initial B d = cong (λ p → subst (Resolve Seeds) p d)
  (pointed-inverse B A refl refl)
forward-back-initial C d = cong (λ p → subst (Resolve Seeds) p d)
  (pointed-inverse C D refl refl)
forward-back-initial D d = cong (λ p → subst (Resolve Seeds) p d)
  (pointed-inverse D C refl refl)

forward-square-initial : (v : Vertex) (d : Resolve Seeds (pointQ v))
  → PathP (λ i → Resolve Seeds (pointQ (sigma² v i)))
      (R.moveInitial (sigma v) (R.moveInitial v d)) d
forward-square-initial A d = forward-back-initial B (R.moveInitial A d) ∙ R.back-moveInitial A d
forward-square-initial B d = forward-back-initial A (R.moveInitial B d) ∙ R.back-moveInitial B d
forward-square-initial C d = forward-back-initial D (R.moveInitial C d) ∙ R.back-moveInitial C d
forward-square-initial D d = forward-back-initial C (R.moveInitial D d) ∙ R.back-moveInitial D d

-- Structural recursion retains every edge and the arbitrary initial proof.
forward-back-chain : {v : Vertex} (c : Chain v) → R.moveChain c ≡ R.backChain c
forward-back-chain (initial v d) i = initial (sigma v) (forward-back-initial v d i)
forward-back-chain (extend c e) i = extend (forward-back-chain c i) (moveOut e)
forward-back : (c : Total) → R.move c ≡ R.back c
forward-back (v , c) i = sigma v , forward-back-chain c i
forward-square : (c : Total) → R.move (R.move c) ≡ c
forward-square c = forward-back (R.move c) ∙ R.back-move c
forward-as-inverse : (c : Total) → R.move c ≡ invEq R.wholeEquiv c
forward-as-inverse = forward-back
involutiveEquiv : Total ≃ Total
involutiveEquiv = isoToEquiv (iso R.move R.move forward-square forward-square)
same-forward-equivalence : involutiveEquiv ≡ R.wholeEquiv
same-forward-equivalence = equivEq refl

-- All four binary mode combinations, with explicit composition orientation.
product : Mode → Mode → Mode
product stay n = n
product exchange stay = exchange
product exchange exchange = stay
action : Mode → Total → Total
action stay c = c
action exchange c = R.move c
unit-law : (c : Total) → action stay c ≡ c
unit-law c = refl
composition-law : (m n : Mode) (c : Total)
  → action m (action n c) ≡ action (product m n) c
composition-law stay n c = refl
composition-law exchange stay c = refl
composition-law exchange exchange c = forward-square c
native-composition-law : (m n : Mode) (c : Total)
  → closure (action m (action n c)) ≡ closure (action (product m n) c)
native-composition-law m n c = cong closure (composition-law m n c)

-- The same law includes two actual dependent attachments and their native
-- derivations; this is a Chain/closure theorem, not yet a Body re-binding.
two-attachment-forward-square : (c : Total) (e : Questions c) (f : Questions (step c e))
  → R.move (R.move (step (step c e) f)) ≡ step (step c e) f
two-attachment-forward-square c e f = forward-square (step (step c e) f)
two-attachment-native-square : (c : Total) (e : Questions c) (f : Questions (step c e))
  → closure (R.move (R.move (step (step c e) f))) ≡ closure (step (step c e) f)
two-attachment-native-square c e f = cong closure (two-attachment-forward-square c e f)

-- Ready contains an arbitrary admission path. Cancellation recovers the
-- canonical encoding of its decoded history, not equality of all such paths.
ready-forward-square : (r : Ready)
  → R.moveReady (R.moveReady r) ≡ encode (decode r)
ready-forward-square r = cong encode
  (cong R.move (decode-encode (R.move (decode r))) ∙ forward-square (decode r))

-- A single exchange is still nonidentity. Nor do the new paths claim
-- judgmental cancellation or erasure/replacement of the actual initial proof.
exchange-not-identity : ¬ ((c : Total) → R.move c ≡ c)
exchange-not-identity h = sigma-not-pointed-self
  (cong fst (h (A , initial A (root A))))

-- A precise remaining higher overlap for these CHOSEN binary witnesses.
-- Declaring the boundary does not supply a filler or a coherent C2 action.
TripleExchangeOverlap : Type₁
TripleExchangeOverlap = (c : Total)
  → forward-square (R.move c) ≡ cong R.move (forward-square c)
