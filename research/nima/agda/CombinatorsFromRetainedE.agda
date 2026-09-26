{-# OPTIONS --safe --cubical --guardedness #-}
module CombinatorsFromRetainedE where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import GeneratedContinuationContexts as G
open G using (Ty; one; ground; _⊗_; _⇒_; Val)

-- Explicit structural interpretation of nondependent E. Pairing, projections,
-- sharing, composition and an empty product are admitted. Function objects may
-- occur as inputs, but there is NO evaluation or abstraction constructor.
data EProgram : Ty → Ty → Type₁ where
  identity : {A : Ty} → EProgram A A
  terminal : {A : Ty} → EProgram A one
  _then_ : {A B C : Ty} → EProgram A B → EProgram B C → EProgram A C
  first : {A B : Ty} → EProgram (A ⊗ B) A
  second : {A B : Ty} → EProgram (A ⊗ B) B
  pair : {A B C : Ty} → EProgram A B → EProgram A C → EProgram A (B ⊗ C)
infixl 15 _then_

compile : {A B : Ty} → EProgram A B → G.Program A B
compile identity = G.identity
compile terminal = G.terminal
compile (f then g) = compile f G.then compile g
compile first = G.first
compile second = G.second
compile (pair f g) = G.pair (compile f) (compile g)
run : {A B : Ty} → EProgram A B → Val A → Val B
run p = G.run (compile p)

-- Uncurried K and input duplication are structural E programs.
K-body : (A B : Ty) → EProgram (A ⊗ B) A
K-body A B = first
duplicate : (A : Ty) → EProgram A (A ⊗ A)
duplicate A = pair identity identity
K-computes : (A B : Ty) (a : Val A) (b : Val B) → run (K-body A B) (a , b) ≡ a
K-computes A B a b = refl
duplicate-computes : (A : Ty) (a : Val A) → run (duplicate A) a ≡ (a , a)
duplicate-computes A a = refl

-- Logical relation: ground values must agree; function-typed inputs can vary
-- freely. Every structural E program preserves this relation.
Rel : (A : Ty) → Val A → Val A → Type
Rel one x y = Unit
Rel (ground A) x y = x ≡ y
Rel (A ⊗ B) x y = Σ (Rel A (fst x) (fst y)) (λ _ → Rel B (snd x) (snd y))
Rel (A ⇒ B) x y = Unit
preserves : {A B : Ty} (p : EProgram A B) {x y : Val A} → Rel A x y → Rel B (run p x) (run p y)
preserves identity r = r
preserves terminal r = tt
preserves (f then g) r = preserves g (preserves f r)
preserves first r = fst r
preserves second r = snd r
preserves (pair f g) r = preserves f r , preserves g r

Bit : Ty
Bit = ground Bool
-- This excludes EVERY structural E program, not only a search to finite depth.
no-E-application : (p : EProgram ((Bit ⇒ Bit) ⊗ Bit) Bit)
  → ((h : Bool → Bool) (b : Bool) → run p (h , b) ≡ h b) → ⊥
no-E-application p computes = false≢true
  (sym (computes (λ b → b) false)
    ∙ preserves p {x = (λ b → b) , false} {y = (λ _ → true) , false} (tt , refl)
    ∙ computes (λ _ → true) false)

-- S's uncurried body is generated once application is EXPLICITLY added.
-- This definition uses no lambda constructor, but it DOES use evaluation.
S-body : (A B C : Ty)
  → G.Program (((A ⇒ (B ⇒ C)) ⊗ (A ⇒ B)) ⊗ A) C
S-body A B C = G.pair
  (G.pair (G.first G.then G.first) G.second G.then G.apply-function)
  (G.pair (G.first G.then G.second) G.second G.then G.apply-function)
  G.then G.apply-function
S-computes : (A B C : Ty) (f : Val A → Val B → Val C)
  (g : Val A → Val B) (a : Val A)
  → G.run (S-body A B C) ((f , g) , a) ≡ f a (g a)
S-computes A B C f g a = refl

-- The corresponding structural-only S specification is impossible as well.
no-E-S : (p : EProgram (((Bit ⇒ (Bit ⇒ Bit)) ⊗ (Bit ⇒ Bit)) ⊗ Bit) Bit)
  → ((f : Bool → Bool → Bool) (g : Bool → Bool) (a : Bool)
     → run p ((f , g) , a) ≡ f a (g a)) → ⊥
no-E-S p computes = false≢true
  (sym (computes (λ _ _ → false) (λ b → b) false)
    ∙ preserves p
      {x = ((λ _ _ → false) , (λ b → b)) , false}
      {y = ((λ _ _ → true) , (λ b → b)) , false} ((tt , tt) , refl)
    ∙ computes (λ _ _ → true) (λ b → b) false)

-- Curried K additionally uses the explicitly admitted abstraction constructor.
K-curried : (A B : Ty) → G.Program A (B ⇒ A)
K-curried A B = G.lambda (compile (K-body A B))
K-curried-computes : (A B : Ty) (a : Val A) (b : Val B)
  → G.run (K-curried A B) a b ≡ a
K-curried-computes A B a b = refl

-- Retention makes the input of K recoverable without making its output map
-- reversible. Here the retained value is paired with the complete input.
K-retained : (A B : Ty) → EProgram (A ⊗ B) ((A ⊗ B) ⊗ A)
K-retained A B = pair identity first
K-input-recovered : (A B : Ty) (p : Val (A ⊗ B))
  → fst (run (K-retained A B) p) ≡ p
K-input-recovered A B p = refl
projection-not-reversible : (recover : Bool → Bool × Bool)
  → ((p : Bool × Bool) → recover (fst p) ≡ p) → ⊥
projection-not-reversible recover law = false≢true
  (cong snd (sym (law (false , false)) ∙ law (false , true)))

-- Reuse the checked next-Q packaging: the program tree and Extended derivation
-- remain retained; these are not claims of generation in the original Resolve.
retained-K-source : (A B : Ty) → G.Source
retained-K-source A B = G.source (A ⊗ B) ((A ⊗ B) ⊗ A) (compile (K-retained A B))
