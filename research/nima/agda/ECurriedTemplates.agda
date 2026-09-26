{-# OPTIONS --safe --cubical --guardedness #-}
module ECurriedTemplates where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true; true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import ETreeSubstitution using (Tree; leaf; node; plug; flip-leaves; left-readout; root)
import WholePackageSigmaPi as Whole
module Q = Whole.Universe ℓ-zero

-- Arity and variable scope are explicit source data.
data Index : ℕ → Type where
  here : {n : ℕ} → Index (suc n)
  there : {n : ℕ} → Index n → Index (suc n)
data Scope (n : ℕ) (A : Type) : Type where
  free : A → Scope n A
  slot : Index n → Scope n A
data Args (A : Type) : ℕ → Type where
  [] : Args A zero
  _::_ : {n : ℕ} → A → Args A n → Args A (suc n)
infixr 10 _::_
lookup : {A : Type} {n : ℕ} → Args A n → Index n → A
lookup (a :: rest) here = a
lookup (a :: rest) (there i) = lookup rest i
Template : ℕ → Type → Type
Template n A = Tree (Scope n A)
embed : {A : Type} {n : ℕ} → Tree A → Template n A
embed t = plug t (λ a → leaf (free a))
instantiate : {A : Type} {n : ℕ} → Template n A → Args (Tree A) n → Tree A
instantiate t env = plug t λ { (free a) → leaf a ; (slot i) → lookup env i }

-- Application consumes one formal slot and returns a residual template.
-- This is generic tree elimination, with no K/S-specific cases.
partial : {A : Type} {n : ℕ} → Template (suc n) A → Tree A → Template n A
partial body arg = plug body λ
  { (free a) → leaf (free a)
  ; (slot here) → embed arg
  ; (slot (there i)) → leaf (slot i) }
instantiate-embed : {A : Type} {n : ℕ} (t : Tree A) (env : Args (Tree A) n)
  → instantiate (embed t) env ≡ t
instantiate-embed (leaf a) env = refl
instantiate-embed (node l r) env = cong₂ node (instantiate-embed l env) (instantiate-embed r env)

-- The beta compatibility law for partial application is proved by induction.
partial-beta : {A : Type} {n : ℕ} (body : Template (suc n) A)
  (arg : Tree A) (env : Args (Tree A) n)
  → instantiate (partial body arg) env ≡ instantiate body (arg :: env)
partial-beta (leaf (free a)) arg env = refl
partial-beta (leaf (slot here)) arg env = instantiate-embed arg env
partial-beta (leaf (slot (there i))) arg env = refl
partial-beta (node l r) arg env = cong₂ node (partial-beta l arg env) (partial-beta r arg env)

run-arguments : {A : Type} {n : ℕ} → Template n A → Args (Tree A) n → Tree A
run-arguments body [] = instantiate body []
run-arguments body (arg :: rest) = run-arguments (partial body arg) rest
run-correct : {A : Type} {n : ℕ} (body : Template n A) (env : Args (Tree A) n)
  → run-arguments body env ≡ instantiate body env
run-correct body [] = refl
run-correct body (arg :: rest) = run-correct (partial body arg) rest ∙ partial-beta body arg rest

K : {A : Type} → Template 2 A
K = leaf (slot here)
S : {A : Type} → Template 3 A
S = node
  (node (leaf (slot here)) (leaf (slot (there (there here)))))
  (node (leaf (slot (there here))) (leaf (slot (there (there here)))))
K-law : {A : Type} (x y : Tree A) → run-arguments K (x :: y :: []) ≡ x
K-law x y = run-correct K (x :: y :: [])
S-law : {A : Type} (f g x : Tree A)
  → run-arguments S (f :: g :: x :: []) ≡ node (node f x) (node g x)
S-law f g x = run-correct S (f :: g :: x :: [])

-- Pointwise beta extends to equality of interpreted environment functions.
-- This is not equality of raw code or a proof of function-space completeness.
partial-interpretation : {A : Type} {n : ℕ} (body : Template (suc n) A) (arg : Tree A)
  → (λ env → instantiate (partial body arg) env)
     ≡ (λ env → instantiate body (arg :: env))
partial-interpretation body arg = funExt (partial-beta body arg)

-- A strict expressivity boundary: insertion templates cannot inspect an input
-- to flip its labels, even though this map is definable by tree elimination.
not-full-P : (body : Template 1 Bool)
  → ((arg : Tree Bool) → instantiate body (arg :: []) ≡ flip-leaves arg) → ⊥
not-full-P (leaf (free false)) law = false≢true (cong left-readout (law (leaf false)))
not-full-P (leaf (free true)) law = true≢false (cong left-readout (law (leaf true)))
not-full-P (leaf (slot here)) law = false≢true (cong left-readout (law (leaf false)))
not-full-P (leaf (slot (there ()))) law
not-full-P (node l r) law = false≢true (cong root (law (leaf false)))

record Application (n : ℕ) (A : Type) : Type where
  constructor applied
  field
    source : Template (suc n) A
    argument : Tree A
    residual : Template n A
    compatible : partial source argument ≡ residual
apply-retained : {A : Type} {n : ℕ} → Template (suc n) A → Tree A → Application n A
apply-retained body arg = applied body arg (partial body arg) refl
as-Q : {A : Type} {n : ℕ} → Application n A → Q.Complete
as-Q {A} {n} step = Q.pack (Q.atom (Application n A)) step
argument-recovered : {A : Type} {n : ℕ} (body : Template (suc n) A) (arg : Tree A)
  → Application.argument (Q.value (as-Q (apply-retained body arg))) ≡ arg
argument-recovered body arg = refl
