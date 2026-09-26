{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedContinuationContexts where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import UniversalSubstitution as Universal
import ResolutionMapIntroductionGap as Gap

-- Explicit new source fragment: typed cartesian-closed programs.
-- There is NO constructor importing an arbitrary function or equivalence.
data Ty : Type₁ where
  one : Ty
  ground : Type → Ty
  _⊗_ _⇒_ : Ty → Ty → Ty
infixr 20 _⇒_
infixr 25 _⊗_
module Q = Whole.Universe ℓ-zero
code : Ty → Q.Code
code one = Q.Pi ⊥ (λ ())
code (ground A) = Q.atom A
code (A ⊗ B) = Q.E (Q.El (code A)) (λ _ → code B)
code (A ⇒ B) = Q.maps (code A) (code B)
Val : Ty → Type
Val A = Q.El (code A)

data Program : Ty → Ty → Type₁ where
  terminal : {A : Ty} → Program A one
  identity : {A : Ty} → Program A A
  _then_ : {A B C : Ty} → Program A B → Program B C → Program A C
  first : {A B : Ty} → Program (A ⊗ B) A
  second : {A B : Ty} → Program (A ⊗ B) B
  pair : {A B C : Ty} → Program A B → Program A C → Program A (B ⊗ C)
  apply-function : {A B : Ty} → Program ((A ⇒ B) ⊗ A) B
  lambda : {A B C : Ty} → Program (A ⊗ B) C → Program A (B ⇒ C)
infixl 15 _then_

run : {A B : Ty} → Program A B → Val A → Val B
run terminal a = λ ()
run identity a = a
run (f then g) a = run g (run f a)
run first p = fst p
run second p = snd p
run (pair f g) a = run f a , run g a
run apply-function (f , a) = f a
run (lambda body) a b = run body (a , b)

-- A generated open-context program: the continuation is a formal input.
preprogram : {A B : Ty} → Program A B → (X : Ty) → Program (B ⇒ X) (A ⇒ X)
preprogram f X = lambda (pair first (second then f) then apply-function)
preprogram-computes : {A B : Ty} (f : Program A B) (X : Ty)
  (h : Val B → Val X) (a : Val A)
  → run (preprogram f X) h a ≡ h (run f a)
preprogram-computes f X h a = refl

record Inverse {A B : Ty} (f : Program A B) (g : Program B A) : Type where
  field
    left : (a : Val A) → run g (run f a) ≡ a
    right : (b : Val B) → run f (run g b) ≡ b

-- Universal witnesses are constructed from the generated forward/backward
-- context programs and their evaluation paths, not imported as test seeds.
continuation-iso : {A B : Ty} (f : Program A B) (g : Program B A)
  → Inverse f g → (X : Ty) → Iso (Val (B ⇒ X)) (Val (A ⇒ X))
Iso.fun (continuation-iso f g laws X) = run (preprogram f X)
Iso.inv (continuation-iso f g laws X) = run (preprogram g X)
Iso.rightInv (continuation-iso f g laws X) h = funExt λ a → cong h (Inverse.left laws a)
Iso.leftInv (continuation-iso f g laws X) h = funExt λ b → cong h (Inverse.right laws b)

all-continuation-tests : {A B : Ty} (f : Program A B) (g : Program B A)
  → Inverse f g → Universal.Substitution.Universal (Val A) (Val B) (run f)
all-continuation-tests f g laws X = isoToIsEquiv (continuation-iso f g laws (ground X))
selected-equivalence : {A B : Ty} (f : Program A B) (g : Program B A)
  → Inverse f g → isEquiv (run f)
selected-equivalence f g laws = Universal.Substitution.universal-to-equiv _ _ _
  (all-continuation-tests f g laws)

-- Two structural examples: the inverse paths compute by beta/eta laws.
swap : (A B : Ty) → Program (A ⊗ B) (B ⊗ A)
swap A B = pair second first
swap-inverse : (A B : Ty) → Inverse (swap A B) (swap B A)
Inverse.left (swap-inverse A B) (a , b) = refl
Inverse.right (swap-inverse A B) (b , a) = refl
swap-tests : (A B : Ty) → Universal.Substitution.Universal
  (Val (A ⊗ B)) (Val (B ⊗ A)) (run (swap A B))
swap-tests A B = all-continuation-tests (swap A B) (swap B A) (swap-inverse A B)

curry-program : (A B C : Ty) → Program ((A ⊗ B) ⇒ C) (A ⇒ (B ⇒ C))
curry-program A B C = lambda (lambda
  (pair (first then first) (pair (first then second) second) then apply-function))
uncurry-program : (A B C : Ty) → Program (A ⇒ (B ⇒ C)) ((A ⊗ B) ⇒ C)
uncurry-program A B C = lambda
  (pair (pair first (second then first) then apply-function) (second then second)
    then apply-function)
curry-inverse : (A B C : Ty) → Inverse (curry-program A B C) (uncurry-program A B C)
Inverse.left (curry-inverse A B C) h = refl
Inverse.right (curry-inverse A B C) h = refl
curry-tests : (A B C : Ty) → Universal.Substitution.Universal
  (Val ((A ⊗ B) ⇒ C)) (Val (A ⇒ (B ⇒ C))) (run (curry-program A B C))
curry-tests A B C = all-continuation-tests (curry-program A B C) (uncurry-program A B C)
  (curry-inverse A B C)

-- Explicit extension of resolution. This does not alter the old Rule datatype.
record Source : Type₁ where
  constructor source
  field
    domain codomain : Ty
    program : Program domain codomain
open Source
output : Source → Q.Complete
output s = Q.map-package (code (domain s)) (code (codomain s)) (run (program s))
module Old = Resolution.Generators ℓ-zero

data Extended (S : Q.Complete → Type₁) : Q.Complete → Type₁ where
  seed⁺ : {q : Q.Complete} → S q → Extended S q
  old-rule : (r : Old.Rule) → ((i : Old.Arity r) → Extended S (Old.input r i))
    → Extended S (Old.output r)
  generated-map : (s : Source) → Extended S (output s)

embed-old : {S : Q.Complete → Type₁} {q : Q.Complete} → Old.Resolve S q → Extended S q
embed-old (Old.seed s) = seed⁺ s
embed-old (Old.apply r ds) = old-rule r (λ i → embed-old (ds i))
EmptySeeds : Q.Complete → Type₁
EmptySeeds q = Lift ⊥
source-generated : (s : Source) → Extended EmptySeeds (output s)
source-generated = generated-map

-- The entire source program and its derivation become a next-level Q.
nextQ : Source → Whole.Universe.Complete (ℓ-suc ℓ-zero)
nextQ s = Whole.Universe.pack
  (Whole.Universe.atom (Σ Source (λ t → Extended EmptySeeds (output t))))
  (s , source-generated s)
source-recovered : (s : Source) → fst (Whole.Universe.value (nextQ s)) ≡ s
source-recovered s = refl

-- Neither the programs nor their continuation transports came from old seeds.
not-old-generated : (s : Source) → Old.Resolve EmptySeeds (output s) → ⊥
not-old-generated s = Gap.Gap.no-unseeded-map-package ℓ-zero
  (code (domain s)) (code (codomain s)) (run (program s))

-- A retained certificate includes both generated programs and their inverse
-- paths; the universal test family is then constructed from that source.
record Certificate : Type₁ where
  constructor certificate
  field
    from-type to-type : Ty
    forward : Program from-type to-type
    backward : Program to-type from-type
    inverse-laws : Inverse forward backward

certificate-tests : (c : Certificate) → Universal.Substitution.Universal
  (Val (Certificate.from-type c)) (Val (Certificate.to-type c)) (run (Certificate.forward c))
certificate-tests c = all-continuation-tests (Certificate.forward c) (Certificate.backward c)
  (Certificate.inverse-laws c)
forward-context : Certificate → Type → Source
forward-context c X = source (Certificate.to-type c ⇒ ground X)
  (Certificate.from-type c ⇒ ground X) (preprogram (Certificate.forward c) (ground X))
backward-context : Certificate → Type → Source
backward-context c X = source (Certificate.from-type c ⇒ ground X)
  (Certificate.to-type c ⇒ ground X) (preprogram (Certificate.backward c) (ground X))
forward-context-generated : (c : Certificate) (X : Type)
  → Extended EmptySeeds (output (forward-context c X))
forward-context-generated c X = generated-map (forward-context c X)
backward-context-generated : (c : Certificate) (X : Type)
  → Extended EmptySeeds (output (backward-context c X))
backward-context-generated c X = generated-map (backward-context c X)

CertificatePayload : Type₁
CertificatePayload = Σ Certificate (λ c → Universal.Substitution.Universal
  (Val (Certificate.from-type c)) (Val (Certificate.to-type c)) (run (Certificate.forward c)))
retain-certificate : Certificate → Whole.Universe.Complete (ℓ-suc ℓ-zero)
retain-certificate c = Whole.Universe.pack (Whole.Universe.atom CertificatePayload)
  (c , certificate-tests c)
certificate-recovered : (c : Certificate)
  → fst (Whole.Universe.value (retain-certificate c)) ≡ c
certificate-recovered c = refl
swap-certificate : (A B : Ty) → Certificate
swap-certificate A B = certificate (A ⊗ B) (B ⊗ A) (swap A B) (swap B A) (swap-inverse A B)
curry-certificate : (A B C : Ty) → Certificate
curry-certificate A B C = certificate ((A ⊗ B) ⇒ C) (A ⇒ (B ⇒ C))
  (curry-program A B C) (uncurry-program A B C) (curry-inverse A B C)

-- Keep raw programs distinct even when beta/eta give equal interpreted maps.
is-identity : {A B : Ty} → Program A B → Bool
is-identity identity = true
is-identity _ = false
raw-programs-distinct : (A : Ty) → identity {A} ≡ (identity then identity) → ⊥
raw-programs-distinct A p = true≢false (cong is-identity p)

no-source-recovery-from-value : (A : Ty)
  (recover : (Val A → Val A) → Program A A)
  → ((p : Program A A) → recover (run p) ≡ p) → ⊥
no-source-recovery-from-value A recover law = raw-programs-distinct A
  (sym (law identity) ∙ law (identity then identity))

-- Adding the certified fragment does not silently police old parameters.
module SuppliedStillAllowed (A B : Type) (f : A → B) where
  module Original = Gap.SuppliedFunction A B f
  still-admitted : Extended Original.Seeds Original.encoded
  still-admitted = embed-old Original.encoded-derived
