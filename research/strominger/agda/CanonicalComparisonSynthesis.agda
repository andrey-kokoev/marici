{-# OPTIONS --safe --cubical --guardedness #-}
module CanonicalComparisonSynthesis where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma using (_×_)
open import Cubical.Data.Sum using (_⊎_; inl; inr)
open import Cubical.Data.Empty as Empty using (⊥)
open import Cubical.Data.Bool using (Bool; true; false; false≢true)
open import Cubical.Data.Maybe using (Maybe; just; nothing)
open import Cubical.Relation.Nullary using (Dec; yes; no; ¬_)
open import NativeExtensionFamilyAudit using
  (Vertex; Edge; A; B; C; D; AB; BC; CA; BA; AD; DB; Seeds; root; sigmaEquiv)
open import InternalSourceComparisons using
  (Mode; stay; exchange; act; package; nonidentity; derivation)
open import GeneratedReaderClassification
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- Primitive finite decisions follow the ACTUAL indexed Edge constructors.
edge? : (s t : Vertex) → Dec (Edge s t)
edge? A A = no (λ ())
edge? A B = yes AB
edge? A C = no (λ ())
edge? A D = yes AD
edge? B A = yes BA
edge? B B = no (λ ())
edge? B C = yes BC
edge? B D = no (λ ())
edge? C A = yes CA
edge? C B = no (λ ())
edge? C C = no (λ ())
edge? C D = no (λ ())
edge? D A = no (λ ())
edge? D B = yes DB
edge? D C = no (λ ())
edge? D D = no (λ ())

shape-image? : (s : Shape) (w : Vertex) → Dec (ShapeImage s w)
shape-image? whole w = yes (w , refl)
shape-image? (outgoing v) w with edge? v w
... | yes e = yes ((w , e) , refl)
... | no absent = no (λ { ((t , e) , p) → absent (subst (Edge v) p e) })

AgreeAt ApartAt : Mode → Shape → Shape → Vertex → Type
AgreeAt m s t w = (ShapeImage s w → ShapeImage t (act m w))
  × (ShapeImage t (act m w) → ShapeImage s w)
ApartAt m s t w = (ShapeImage s w × (¬ ShapeImage t (act m w)))
  ⊎ ((¬ ShapeImage s w) × ShapeImage t (act m w))
at? : (m : Mode) (s t : Shape) (w : Vertex) → AgreeAt m s t w ⊎ ApartAt m s t w
at? m s t w with shape-image? s w | shape-image? t (act m w)
... | yes left | yes right = inl ((λ _ → right) , (λ _ → left))
... | yes left | no absent = inr (inl (left , absent))
... | no absent | yes right = inr (inr (absent , right))
... | no left | no right = inl ((λ x → Empty.rec (left x)) , (λ y → Empty.rec (right y)))

-- Fixed search order supplies the first explicit separating vertex.
all4 : (P Q : Vertex → Type) → ((w : Vertex) → P w ⊎ Q w)
  → ((w : Vertex) → P w) ⊎ (Σ Vertex Q)
all4 P Q decide with decide A
... | inr q = inr (A , q)
... | inl a with decide B
...   | inr q = inr (B , q)
...   | inl b with decide C
...     | inr q = inr (C , q)
...     | inl c with decide D
...       | inr q = inr (D , q)
...       | inl d = inl (λ { A → a ; B → b ; C → c ; D → d })
shape-decision : (m : Mode) (s t : Shape)
  → ((w : Vertex) → AgreeAt m s t w) ⊎ (Σ Vertex (ApartAt m s t))
shape-decision m s t = all4 (AgreeAt m s t) (ApartAt m s t) (at? m s t)
shape-accepts : Mode → Shape → Shape → Bool
shape-accepts m s t with shape-decision m s t
... | inl _ = true
... | inr _ = false

module Compile (m : Mode) {v : Vertex}
  (a : Fragment v) (b : Fragment (act m v)) where
  module C = Comparisons m a b
  leftShape = Normal.shape (normal a)
  rightShape = Normal.shape (normal b)
  leftImage = image-classification a
  rightImage = image-classification b

  -- These are computations from the normal forms, NOT new input parameters.
  lift-agreement : ((w : Vertex) → AgreeAt m leftShape rightShape w) → C.ImageAgreement
  lift-agreement agrees = forward , backward
    where
    forward : (w : Vertex) → Image (body a) w → Image (body b) (act m w)
    forward w x = invEq (rightImage (act m w)) (fst (agrees w) (equivFun (leftImage w) x))
    backward : (w : Vertex) → Image (body b) (act m w) → Image (body a) w
    backward w y = invEq (leftImage w) (snd (agrees w) (equivFun (rightImage (act m w)) y))

  Refusal : Type
  Refusal = Σ[ w ∈ Vertex ]
    ((Image (body a) w × (¬ Image (body b) (act m w)))
     ⊎ ((¬ Image (body a) w) × Image (body b) (act m w)))
  lift-refusal : Σ Vertex (ApartAt m leftShape rightShape) → Refusal
  lift-refusal (w , inl (left , absent)) = w , inl
    (invEq (leftImage w) left , λ y → absent (equivFun (rightImage (act m w)) y))
  lift-refusal (w , inr (absent , right)) = w , inr
    ((λ x → absent (equivFun (leftImage w) x)) , invEq (rightImage (act m w)) right)
  refutes : Refusal → ¬ C.Filler
  refutes (w , inl (left , absent)) f = absent (fst (C.images-from-filler f) w left)
  refutes (w , inr (absent , right)) f = absent (snd (C.images-from-filler f) w right)

  Result : Type
  Result = C.Filler ⊎ Refusal
  compile : Result
  compile with shape-decision m leftShape rightShape
  ... | inl agrees = inl (C.filler-from-images (lift-agreement agrees))
  ... | inr apart = inr (lift-refusal apart)

  accepted : Result → Bool
  accepted (inl _) = true
  accepted (inr _) = false
  separating-vertex : Result → Maybe Vertex
  separating-vertex (inl _) = nothing
  separating-vertex (inr (w , _)) = just w
  complete : C.Filler → accepted compile ≡ true
  complete f with compile
  ... | inl _ = refl
  ... | inr bad = Empty.rec (refutes bad f)
  decision : Dec C.Filler
  decision with compile
  ... | inl f = yes f
  ... | inr bad = no (refutes bad)

  -- The returned Filler contains derived e/point/port parameters. This adapter
  -- consumes those results and retains the EXACT original Fragment operands.
  next : C.Filler → Fragment (act m v)
  next (e , p , h) = compareF m a b e p h
  admitted : (f : C.Filler) → Resolve Seeds (package (body (next f)))
  admitted f = native (next f)
  agrees-with-existing : (f prior : C.Filler) → f ≡ prior
  agrees-with-existing = C.filler-prop
  native-coherence : (f g : C.Filler) → PathP
    (λ i → Resolve Seeds (package (body (next (C.filler-prop f g i)))))
    (admitted f) (admitted g)
  native-coherence f g i = admitted (C.filler-prop f g i)

  record Success : Type where
    constructor success
    field certificate : C.Filler
    -- Definitions, not independently replaceable fields: no seed reset can
    -- be installed in the output while keeping its comparison certificate.
    term : Fragment (act m v)
    term = next certificate
    admission : Resolve Seeds (package (body term))
    admission = admitted certificate

  -- Public synthesis result: only m, a and b are inputs. Native output is
  -- computed on success; refusal carries actual image witnesses on failure.
  run : Success ⊎ Refusal
  run with compile
  ... | inl f = inl (success f)
  ... | inr bad = inr bad

  require-success : (result : Result) → accepted result ≡ true → C.Filler
  require-success (inl f) _ = f
  require-success (inr _) impossible = Empty.rec (false≢true impossible)

-- Reduction regressions exercise actual compiled operands, not a standalone
-- Boolean lookup table. Initial derivations remain arbitrary in the theorem.
module WholeExchange = Compile exchange (start A (root A)) (start B (root B))
whole-exchange-accepted : WholeExchange.accepted WholeExchange.compile ≡ true
whole-exchange-accepted = refl
whole-filler = WholeExchange.require-success WholeExchange.compile whole-exchange-accepted
whole-next = WholeExchange.next whole-filler
whole-native = WholeExchange.admitted whole-filler

-- Compare AFTER synthesis with the actual old nonidentity comparison.
-- This witness is a regression target, never an argument to the compiler.
whole-prior : WholeExchange.C.Filler
whole-prior = sigmaEquiv , refl , (λ _ → refl)
whole-body-coherence : body whole-next ≡ nonidentity A
whole-body-coherence = cong (λ f → body (WholeExchange.next f))
  (WholeExchange.agrees-with-existing whole-filler whole-prior)
whole-native-coherence : PathP
  (λ i → Resolve Seeds (package (whole-body-coherence i)))
  whole-native (derivation (nonidentity A))
whole-native-coherence = WholeExchange.native-coherence whole-filler whole-prior

module SamePointMismatch = Compile stay allA onlyA
same-point-refused : SamePointMismatch.accepted SamePointMismatch.compile ≡ false
same-point-refused = refl
same-point-separator : SamePointMismatch.separating-vertex SamePointMismatch.compile ≡ just B
same-point-separator = refl

leftOut = attachF (start A (root A)) (B , AB)
rightOut = attachF (start B (root B)) (A , BA)
module OutExchange = Compile exchange leftOut rightOut
out-exchange-accepted : OutExchange.accepted OutExchange.compile ≡ true
out-exchange-accepted = refl
out-filler = OutExchange.require-success OutExchange.compile out-exchange-accepted
out-next = OutExchange.next out-filler
out-native = OutExchange.admitted out-filler

-- A synthesized comparison is again in the fragment and can feed synthesis.
module Reused = Compile stay whole-next whole-next
reused-accepted : Reused.accepted Reused.compile ≡ true
reused-accepted = refl
reused-native = Reused.admitted (Reused.require-success Reused.compile reused-accepted)
