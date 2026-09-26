{-# OPTIONS --safe --cubical --guardedness #-}
module ObservationRespectingBoundary where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Unit.Base using (Unit; tt)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import BoundaryGeneratedQuestions as B
import IndexedConstructorTables as Tables
import NativeTableRules as Native
import RetainedLocalTidalOverlap as L
import NewtonianTidalKernel as K
module O = Whole.Universe ℓ-zero
module R = Resolution.Generators ℓ-zero
module G = Tables.Core ℓ-zero
module N = Native.Native ℓ-zero

-- These maps are supplied observations in aligned output units, not an
-- algorithm for inferring physical semantics from a bare carrier.
Preserves : {A C V : Type} → (A → V) → (C → V) → A ≃ C → Type
Preserves r s e = (x : _) → s (equivFun e x) ≡ r x
preserves-id : {A V : Type} (r : A → V) → Preserves r r (idEquiv A)
preserves-id r x = refl
preserves-compose : {A C D V : Type} {r : A → V} {s : C → V} {t : D → V}
  (e : A ≃ C) (f : C ≃ D) → Preserves r s e → Preserves s t f → Preserves r t (compEquiv e f)
preserves-compose e f p q x = q (equivFun e x) ∙ p x
preserves-inverse : {A C V : Type} {r : A → V} {s : C → V}
  (e : A ≃ C) → Preserves r s e → Preserves s r (invEquiv e)
preserves-inverse {s = s} e p y = sym (p (invEq e y)) ∙ cong s (secEq e y)

Ty : O.Complete → Type
Ty a = O.El (O.retained a)
Observed : {V : Type} (a b : O.Complete) → (Ty a → V) → (Ty b → V) → Type
Observed a b r s = Σ (B.Filler a b) (λ f → Preserves r s (fst f))
identity : {V : Type} (a : O.Complete) (r : Ty a → V) → Observed a a r r
identity a r = B.identity a , preserves-id r
compose : {V : Type} {a b c : O.Complete}
  {r : Ty a → V} {s : Ty b → V} {t : Ty c → V}
  → Observed a b r s → Observed b c s t → Observed a c r t
compose {a = a} {b} {c} {r} {s} {t} (f , p) (g , q) =
  B.compose {a = a} {b} {c} f g , preserves-compose {r = r} {s} {t} (fst f) (fst g) p q
inverse : {V : Type} {a b : O.Complete} {r : Ty a → V} {s : Ty b → V}
  → Observed a b r s → Observed b a s r
inverse {a = a} {b} (f , p) = B.inverse {a = a} {b} f , preserves-inverse (fst f) p

-- Refinement restricts compatible fillers. No converse is asserted.
forget-left : {A C V W : Type} {r : A → V} {s : C → V}
  {u : A → W} {v : C → W} {e : A ≃ C}
  → Preserves (λ x → r x , u x) (λ y → s y , v y) e → Preserves r s e
forget-left p x = cong fst (p x)
forget-right : {A C V W : Type} {r : A → V} {s : C → V}
  {u : A → W} {v : C → W} {e : A ≃ C}
  → Preserves (λ x → r x , u x) (λ y → s y , v y) e → Preserves u v e
forget-right p x = cong snd (p x)
join : {A C V W : Type} {r : A → V} {s : C → V}
  {u : A → W} {v : C → W} {e : A ≃ C}
  → Preserves r s e → Preserves u v e
  → Preserves (λ x → r x , u x) (λ y → s y , v y) e
join p q x i = p x i , q x i
joint-evidence-iso : {A C V W : Type} {r : A → V} {s : C → V}
  {u : A → W} {v : C → W} {e : A ≃ C}
  → Iso (Preserves (λ x → r x , u x) (λ y → s y , v y) e)
      (Preserves r s e × Preserves u v e)
Iso.fun joint-evidence-iso p = (λ x → cong fst (p x)) , (λ x → cong snd (p x))
Iso.inv joint-evidence-iso (p , q) x i = p x i , q x i
Iso.rightInv joint-evidence-iso (p , q) = refl
Iso.leftInv joint-evidence-iso p = refl
preservation-is-prop : {A C V : Type} → isSet V
  → (r : A → V) (s : C → V) (e : A ≃ C) → isProp (Preserves r s e)
preservation-is-prop setV r s e p q = funExt λ x → setV (s (equivFun e x)) (r x) (p x) (q x)

-- Preserve compatibility evidence as data, not just the unannotated rule.
rule : {V : Type} {a b : O.Complete} {r : Ty a → V} {s : Ty b → V}
  → Observed a b r s → R.Rule
rule {a = a} {b} ((e , p) , h) = R.compare-rule a b e p
retained-certificate : {V : Type} {a b : O.Complete} {r : Ty a → V} {s : Ty b → V}
  → Observed a b r s → O.Complete
retained-certificate {a = a} {b} {r} {s} f =
  O.remember (R.output (rule {a = a} {b} {r} {s} f)) (O.pack (O.atom (Observed a b r s)) f)
certificate-recovered : {V : Type} {a b : O.Complete} {r : Ty a → V} {s : Ty b → V}
  (f : Observed a b r s) → O.value (retained-certificate {a = a} {b} {r} {s} f) ≡ f
certificate-recovered {a = a} {b} {r} {s} f = refl

NativeFiller : (a b : G.Package) → Type
NativeFiller a b = Σ (N.Ty a ≃ N.Ty b) (λ e → equivFun e (N.value a) ≡ N.value b)
NativeObserved : {V : Type} (a b : G.Package) → (N.Ty a → V) → (N.Ty b → V) → Type
NativeObserved a b r s = Σ (NativeFiller a b) (λ f → Preserves r s (fst f))
native-identity : {V : Type} (a : G.Package) (r : N.Ty a → V) → NativeObserved a a r r
native-identity a r = (idEquiv _ , refl) , preserves-id r
native-compose : {V : Type} {a b c : G.Package}
  {r : N.Ty a → V} {s : N.Ty b → V} {t : N.Ty c → V}
  → NativeObserved a b r s → NativeObserved b c s t → NativeObserved a c r t
native-compose {r = r} {s} {t} ((e , p) , h) ((f , q) , k) =
  (compEquiv e f , cong (equivFun f) p ∙ q) , preserves-compose {r = r} {s} {t} e f h k
native-inverse : {V : Type} {a b : G.Package} {r : N.Ty a → V} {s : N.Ty b → V}
  → NativeObserved a b r s → NativeObserved b a s r
native-inverse {a = a} ((e , p) , h) =
  (invEquiv e , cong (invEq e) (sym p) ∙ retEq e (N.value a)) , preserves-inverse e h
native-rule : {V : Type} {a b : G.Package} {r : N.Ty a → V} {s : N.Ty b → V}
  → NativeObserved a b r s → N.Rule
native-rule {a = a} {b} ((e , p) , h) = N.compare-kind , a , b , e , p
native-retained-certificate : {V : Type} {a b : G.Package} {r : N.Ty a → V} {s : N.Ty b → V}
  → NativeObserved a b r s → G.Package
native-retained-certificate {a = a} {b} {r} {s} f =
  N.remember (N.output (native-rule {a = a} {b} {r} {s} f))
    (N.pack (G.atom-node (NativeObserved a b r s)) f)
native-certificate-recovered : {V : Type} {a b : G.Package} {r : N.Ty a → V} {s : N.Ty b → V}
  (f : NativeObserved a b r s) → snd (native-retained-certificate {a = a} {b} {r} {s} f) ≡ f
native-certificate-recovered f = refl

-- Explicit independently supplied native observations and their comparison.
-- Same payload types under this carrier's encoding; no decoded readout needed.
to-native : {V : Type} {a b : O.Complete}
  {r : Ty a → V} {s : Ty b → V}
  (nr : N.Ty (G.encode-package a) → V) (ns : N.Ty (G.encode-package b) → V)
  → ((x : Ty a) → r x ≡ nr x) → ((y : Ty b) → s y ≡ ns y)
  → Observed a b r s → NativeObserved (G.encode-package a) (G.encode-package b) nr ns
to-native nr ns ar as ((e , p) , h) = (e , p) ,
  (λ x → sym (as (equivFun e x)) ∙ h x ∙ ar x)

-- Concrete actual source pair from the preceding retained construction.
tidal : Observed (L.Cited.old-package L.newtonian) (L.Cited.old-package L.rosen)
  (λ x → x) (λ x → x)
tidal = L.Cited.coarse-filler , (λ x → refl)
native-tidal : NativeObserved (L.Cited.native-package L.newtonian) (L.Cited.native-package L.rosen)
  (λ x → x) (λ x → x)
native-tidal = (idEquiv K.Tensor , L.Cited.native-agreement) , (λ x → refl)

-- Electric-only VIEW of the fine payload: not authorization for its full profile.
electric-only : Observed (L.Cited.fine-package L.newtonian) (L.Cited.fine-package L.rosen) fst fst
electric-only = L.Cited.unrestricted-fine-filler , L.loose-keeps-electric
no-joint : Observed (L.Cited.fine-package L.newtonian) (L.Cited.fine-package L.rosen)
  (λ x → x) (λ x → x) → ⊥
no-joint ((e , p) , h) = L.no-respectful-refinement record
  { equivalence = e
  ; preserves-electric = λ v → cong fst (h v)
  ; preserves-gradient = λ v → cong snd (h v)
  ; marked = p }
no-automatic-upgrade :
  (Observed (L.Cited.fine-package L.newtonian) (L.Cited.fine-package L.rosen) fst fst
   → Observed (L.Cited.fine-package L.newtonian) (L.Cited.fine-package L.rosen) (λ x → x) (λ x → x)) → ⊥
no-automatic-upgrade upgrade = no-joint (upgrade electric-only)

-- Remaining authorization boundary: callers must not replace an attached
-- physical profile by an arbitrary constant map and claim full compatibility.
constant-admits : {a b : O.Complete} → B.Filler a b
  → Observed a b (λ _ → tt) (λ _ → tt)
constant-admits f = f , (λ x → refl)
constant-view-of-hostile : Observed (L.Cited.fine-package L.newtonian) (L.Cited.fine-package L.rosen)
  (λ _ → tt) (λ _ → tt)
constant-view-of-hostile = constant-admits
  {a = L.Cited.fine-package L.newtonian} {b = L.Cited.fine-package L.rosen}
  L.Cited.unrestricted-fine-filler
