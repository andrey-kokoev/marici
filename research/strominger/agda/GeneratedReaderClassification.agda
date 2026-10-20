{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedReaderClassification where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using (isSetRetract; isProp×; isPropΠ)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Functions.Embedding using
  (isEmbedding; injEmbedding; injective→hasPropFibers)
open import Cubical.Relation.Nullary.Base using (¬_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open import NativeExtensionFamilyAudit using
  (Vertex; A; B; C; D; CA; pointQ; Seeds; root; sigma²; isB)
open import SourceIndexedExtensionFamilies using (Out; vertex-is-set)
open import InternalSourceComparisons
open import InternalComparisonInterchange using (graphEquiv)
import RepeatedInterchangeCoherence as Prior
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

Carrier : {v : Vertex} → Body v → Type
Carrier b = El (expression (package b))
point : {v : Vertex} (b : Body v) → Carrier b
point b = value (package b)

-- A specified sublanguage of the EXISTING Body operations. No arbitrary
-- prepared reader/carrier, unrestricted native E family, or new native rule.
-- Initial proofs are arbitrary actual Resolve inputs, not fresh seed resets.
mutual
  data Fragment : Vertex → Type₁ where
    start : (v : Vertex) → Resolve Seeds (pointQ v) → Fragment v
    attachF : {v : Vertex} (a : Fragment v) (o : Out v) → Fragment (fst o)
    compareF : (m : Mode) {v : Vertex} (a : Fragment v) (b : Fragment (act m v))
      (e : Carrier (body a) ≃ Carrier (body b))
      → equivFun e (point (body a)) ≡ point (body b)
      → ((x : Carrier (body a)) → act m (reader (body a) x) ≡ reader (body b) (equivFun e x))
      → Fragment (act m v)

  body : {v : Vertex} → Fragment v → Body v
  body (start v d) = prepared v (pointQ v) d (λ x → x) refl
  body (attachF a o) = attach (body a) o
  body (compareF m a b e p h) = compare m (body a) (body b) e p h

native : {v : Vertex} (a : Fragment v) → Resolve Seeds (package (body a))
native a = derivation (body a)

-- Five explicit normal forms: all vertices, or the outgoing witnesses of
-- one of the four vertices. These classify values, NOT native histories.
data Shape : Type where
  whole : Shape
  outgoing : Vertex → Shape
Values : Shape → Type
Values whole = Vertex
Values (outgoing v) = Out v
port : (s : Shape) → Values s → Vertex
port whole x = x
port (outgoing v) x = fst x
values-set : (s : Shape) → isSet (Values s)
values-set whole = vertex-is-set
values-set (outgoing v) = Prior.out-is-set v
port-injective : (s : Shape) (x y : Values s) → port s x ≡ port s y → x ≡ y
port-injective whole x y p = p
port-injective (outgoing v) x y p = sym (Prior.restore-target v x)
  ∙ cong (Prior.restoreOut v) p ∙ Prior.restore-target v y

record Normal {v : Vertex} (b : Body v) : Type where
  field
    shape : Shape
    equivalence : Carrier b ≃ Values shape
    ports : (x : Carrier b) → reader b x ≡ port shape (equivFun equivalence x)
open Normal

abstract
  set-through-equiv : {X Y : Type} → X ≃ Y → isSet Y → isSet X
  set-through-equiv e = isSetRetract (equivFun e) (invEq e) (retEq e)
carrier-set : {v : Vertex} {b : Body v} → Normal b → isSet (Carrier b)
carrier-set n = set-through-equiv (equivalence n) (values-set (shape n))

attachmentIso : {v : Vertex} (a : Body v) (o : Out v) → isSet (Carrier a)
  → Iso (Carrier (attach a o)) (Out v)
Iso.fun (attachmentIso a o s) = fst
Iso.inv (attachmentIso a o s) x = x , refl
Iso.rightInv (attachmentIso a o s) x = refl
Iso.leftInv (attachmentIso a o s) (x , l) i = x , s (point a) (point a) refl l i

normal : {v : Vertex} (a : Fragment v) → Normal (body a)
shape (normal (start v d)) = whole
equivalence (normal (start v d)) = idEquiv Vertex
ports (normal (start v d)) x = refl
shape (normal (attachF {v} a o)) = outgoing v
equivalence (normal (attachF a o)) = isoToEquiv (attachmentIso (body a) o (carrier-set (normal a)))
ports (normal (attachF a o)) x = refl
shape (normal (compareF m a b e p h)) = shape (normal b)
equivalence (normal (compareF m a b e p h)) =
  compEquiv (graphEquiv e) (compEquiv e (equivalence (normal b)))
ports (normal (compareF m a b e p h)) (x , y , w) =
  sym (cong (reader (body b)) w) ∙ ports (normal b) (equivFun e x)

reader-injective : {v : Vertex} {b : Body v} (n : Normal b)
  (x y : Carrier b) → reader b x ≡ reader b y → x ≡ y
reader-injective n x y p = sym (retEq (equivalence n) x)
  ∙ cong (invEq (equivalence n))
      (port-injective (shape n) _ _ (sym (ports n x) ∙ p ∙ ports n y))
  ∙ retEq (equivalence n) y
reader-embedding : {v : Vertex} (a : Fragment v) → isEmbedding (reader (body a))
reader-embedding a = injEmbedding vertex-is-set (reader-injective (normal a) _ _)
Image : {v : Vertex} (b : Body v) → Vertex → Type
Image b w = Σ (Carrier b) (λ x → reader b x ≡ w)
image-prop : {v : Vertex} (a : Fragment v) (w : Vertex) → isProp (Image (body a) w)
image-prop a = injective→hasPropFibers vertex-is-set (reader-injective (normal a) _ _)
ShapeImage : Shape → Vertex → Type
ShapeImage s w = Σ (Values s) (λ x → port s x ≡ w)
shape-image-prop : (s : Shape) (w : Vertex) → isProp (ShapeImage s w)
shape-image-prop s = injective→hasPropFibers vertex-is-set (port-injective s _ _)

-- No truncation or classical finite-subset choice is needed. The normal
-- form is computed from syntax and gives the exact proposition-valued image.
image-classification : {v : Vertex} (a : Fragment v) (w : Vertex)
  → Image (body a) w ≃ ShapeImage (shape (normal a)) w
image-classification a w = isoToEquiv (iso to from
  (λ z → shape-image-prop _ w _ z) (λ z → image-prop a w _ z))
  where
  n : Normal (body a)
  n = normal a
  to : Image (body a) w → ShapeImage (shape n) w
  to (x , p) = equivFun (equivalence n) x , sym (ports n x) ∙ p
  from : ShapeImage (shape n) w → Image (body a) w
  from (x , p) = invEq (equivalence n) x , ports n (invEq (equivalence n) x)
    ∙ cong (port (shape n)) (secEq (equivalence n) x) ∙ p

mode-square : (m : Mode) (v : Vertex) → act m (act m v) ≡ v
mode-square stay v = refl
mode-square exchange v = sigma² v

module Comparisons (m : Mode) {v : Vertex}
  (a : Fragment v) (b : Fragment (act m v)) where
  left : Body v
  left = body a
  right : Body (act m v)
  right = body b
  Filler : Type
  Filler = Σ (Carrier left ≃ Carrier right)
    (λ e → (equivFun e (point left) ≡ point right)
      × ((x : Carrier left) → act m (reader left x) ≡ reader right (equivFun e x)))

  abstract
    filler-prop : isProp Filler
    filler-prop (e , p , h) (e' , p' , h') = Σ≡Prop
      (λ e → isProp× (carrier-set (normal b) _ _) (isPropΠ (λ x → vertex-is-set _ _)))
      (equivEq (funExt (λ x → reader-injective (normal b) _ _ (sym (h x) ∙ h' x))))
  filler-contractible : Filler → isContr Filler
  filler-contractible f = f , filler-prop f

  -- Equality of the actual reader images under the fixed source action.
  -- Both directions are explicit; selected-point agreement alone is weaker.
  ImageAgreement : Type
  ImageAgreement = ((w : Vertex) → Image left w → Image right (act m w))
    × ((w : Vertex) → Image right (act m w) → Image left w)
  agreement-prop : isProp ImageAgreement
  agreement-prop = isProp× (isPropΠ (λ w → isPropΠ (λ _ → image-prop b _)))
    (isPropΠ (λ w → isPropΠ (λ _ → image-prop a w)))

  images-from-filler : Filler → ImageAgreement
  images-from-filler (e , p , h) = to , from
    where
    to : (w : Vertex) → Image left w → Image right (act m w)
    to w (x , q) = equivFun e x , sym (h x) ∙ cong (act m) q
    from : (w : Vertex) → Image right (act m w) → Image left w
    from w (y , q) = invEq e y , sym (mode-square m (reader left (invEq e y)))
      ∙ cong (act m) (h (invEq e y) ∙ cong (reader right) (secEq e y) ∙ q)
      ∙ mode-square m w

  filler-from-images : ImageAgreement → Filler
  filler-from-images agree = isoToEquiv mapping , selected , ports-law
    where
    forwardFiber : (x : Carrier left) → Image right (act m (reader left x))
    forwardFiber x = fst agree (reader left x) (x , refl)
    backwardFiber : (y : Carrier right) → Image left (act m (reader right y))
    backwardFiber y = snd agree (act m (reader right y)) (y , sym (mode-square m (reader right y)))
    f : Carrier left → Carrier right
    f x = fst (forwardFiber x)
    g : Carrier right → Carrier left
    g y = fst (backwardFiber y)
    mapping : Iso (Carrier left) (Carrier right)
    Iso.fun mapping = f
    Iso.inv mapping = g
    Iso.rightInv mapping y = reader-injective (normal b) _ _
      (snd (forwardFiber (g y)) ∙ cong (act m) (snd (backwardFiber y)) ∙ mode-square m (reader right y))
    Iso.leftInv mapping x = reader-injective (normal a) _ _
      (snd (backwardFiber (f x)) ∙ cong (act m) (snd (forwardFiber x)) ∙ mode-square m (reader left x))
    selected : f (point left) ≡ point right
    selected = reader-injective (normal b) _ _
      (snd (forwardFiber (point left)) ∙ cong (act m) (aligned left) ∙ sym (aligned right))
    ports-law : (x : Carrier left) → act m (reader left x) ≡ reader right (f x)
    ports-law x = sym (snd (forwardFiber x))

  classification : Filler ≃ ImageAgreement
  classification = isoToEquiv (iso images-from-filler filler-from-images
    (λ q → agreement-prop _ q) (λ f → filler-prop _ f))

  -- An actual comparison uses unchanged native rules and the actual operand
  -- derivations. Uniqueness is for this fiber, NOT for all Resolve witnesses.
  asBody : Filler → Body (act m v)
  asBody (e , p , h) = compare m left right e p h
  admitted : (f : Filler) → Resolve Seeds (package (asBody f))
  admitted f = derivation (asBody f)
  comparisons-cohere : (f g : Filler) → asBody f ≡ asBody g
  comparisons-cohere f g = cong asBody (filler-prop f g)
  native-coherence : (f g : Filler) → PathP
    (λ i → Resolve Seeds (package (asBody (filler-prop f g i))))
    (admitted f) (admitted g)
  native-coherence f g i = admitted (filler-prop f g i)

-- Same selected point does not imply existence. The seed sees all vertices;
-- an attachment out of C sees only A. Both selected values are A.
allA : Fragment A
allA = start A (root A)
onlyA : Fragment A
onlyA = attachF (start C (root C)) (A , CA)
module Mismatch = Comparisons stay allA onlyA
same-point-no-filler : ¬ Mismatch.Filler
same-point-no-filler (e , p , h) = false≢true (sym (cong isB
  (h B ∙ sym (cong fst (Prior.restore-target C (fst (equivFun e B)))))))

-- The restriction is essential even without new native seeds: arbitrary
-- prepared can replace the identity reader by a constant one.
hidden : Body A
hidden = prepared A (pointQ A) (root A) (λ _ → A) refl
hidden-not-injective : ¬ ((x y : Carrier hidden) → reader hidden x ≡ reader hidden y → x ≡ y)
hidden-not-injective inj = false≢true (cong isB (inj A B refl))
