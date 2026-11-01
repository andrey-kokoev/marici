{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedPairComparisonAdapter where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels using (isSetΣ; isPropΣ)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import ActualSeedEndpointTable as S
import SeedSeamPathComparisonBoundary as H
import NativeExtensionFamilyAudit as N
import SourceIndexedExtensionFamilies as O
import InternalSourceComparisons as C
import RepeatedInterchangeCoherence as R
import WholePackageSigmaPi as W
open W.Universe ℓ-zero

vertex : S.Vertex → N.Vertex
vertex S.A = N.A
vertex S.B = N.B
vertex S.C = N.C
vertex S.D = N.D

edge : (e : S.Occurrence) → N.Edge (vertex (S.source e)) (vertex (S.target e))
edge S.AB = N.AB
edge S.BC = N.BC
edge S.CA = N.CA
edge S.AD = N.AD
edge S.DB = N.DB
edge S.BA = N.BA

run : {s t : S.Vertex} → H.Path s t → C.Body (vertex s) → C.Body (vertex t)
run H.stop b = b
run (H.step e rest) b = run rest (C.attach b (vertex (S.target e) , edge e))

-- Original words remain stored separately from their interpreted packages.
record Retained (s t : S.Vertex) : Type₁ where
  field
    history : H.Path s t
    body : C.Body (vertex t)
    realizes : body ≡ run history (C.seedBody (vertex s))

adapt : {s t : S.Vertex} (h : H.Path s t) → Retained s t
Retained.history (adapt h) = h
Retained.body (adapt {s} h) = run h (C.seedBody (vertex s))
Retained.realizes (adapt h) = refl

history-recovery : {s t : S.Vertex} (h : H.Path s t)
  → Retained.history (adapt h) ≡ h
history-recovery h = refl

direct indirect : C.Body N.B
direct = Retained.body (adapt H.x0)
indirect = Retained.body (adapt H.x1)

DirectCarrier IndirectCarrier : Type
DirectCarrier = El (expression (C.package direct))
IndirectCarrier = El (expression (C.package indirect))

out-D-prop : isProp (O.Out N.D)
out-D-prop (_ , N.DB) (_ , N.DB) = refl

first-is-set : isSet (El (expression
  (C.package (C.attach (C.seedBody N.A) (N.D , N.AD)))))
first-is-set = isSetΣ (R.out-is-set N.A)
  (λ _ → isProp→isSet (O.vertex-is-set N.A N.A))

indirect-is-prop : isProp IndirectCarrier
indirect-is-prop = isPropΣ out-D-prop (λ _ → first-is-set _ _)

u v : DirectCarrier
u = (N.B , N.AB) , refl
v = (N.D , N.AD) , refl

is-B : N.Vertex → Bool
is-B N.A = false
is-B N.B = true
is-B N.C = false
is-B N.D = false

direct-distinct : u ≡ v → ⊥
direct-distinct p = true≢false (cong (λ x → is-B (fst (fst x))) p)

no-carrier-equivalence : DirectCarrier ≃ IndirectCarrier → ⊥
no-carrier-equivalence e = direct-distinct
  (sym (retEq e u) ∙ cong (invEq e)
    (indirect-is-prop (equivFun e u) (equivFun e v)) ∙ retEq e v)

-- Even the first field of the complete-comparison contract is impossible.
ComparisonAttempt : Type
ComparisonAttempt = Σ (DirectCarrier ≃ IndirectCarrier) (λ e →
  Σ (equivFun e (value (C.package direct)) ≡ value (C.package indirect)) (λ _ →
    (x : DirectCarrier) → C.reader direct x ≡ C.reader indirect (equivFun e x)))

no-complete-comparison : ComparisonAttempt → ⊥
no-complete-comparison attempt = no-carrier-equivalence (fst attempt)
