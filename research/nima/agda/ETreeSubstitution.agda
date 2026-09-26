{-# OPTIONS --safe --cubical --guardedness #-}
module ETreeSubstitution where
open import Cubical.Foundations.Prelude hiding (fill)
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true; true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
module Q = Whole.Universe ℓ-zero

-- Finite inductive closure of a tagged E layer. Recursive induction is an
-- explicit foundation here; it is not derived from the old Resolve rules.
data Tree (A : Type) : Type where
  leaf : A → Tree A
  node : Tree A → Tree A → Tree A

layer-code : Type → Type → Q.Code
layer-code A X = Q.E Bool λ { false → Q.atom A ; true → Q.E X (λ _ → Q.atom X) }
Layer : Type → Type → Type
Layer A X = Q.El (layer-code A X)
unroll : {A : Type} → Tree A → Layer A (Tree A)
unroll (leaf a) = false , a
unroll (node l r) = true , l , r
roll : {A : Type} → Layer A (Tree A) → Tree A
roll (false , a) = leaf a
roll (true , l , r) = node l r
layer-iso : (A : Type) → Iso (Tree A) (Layer A (Tree A))
Iso.fun (layer-iso A) = unroll
Iso.inv (layer-iso A) = roll
Iso.rightInv (layer-iso A) (false , a) = refl
Iso.rightInv (layer-iso A) (true , l , r) = refl
Iso.leftInv (layer-iso A) (leaf a) = refl
Iso.leftInv (layer-iso A) (node l r) = refl

fold : {A B : Type} → (A → B) → (B → B → B) → Tree A → B
fold atoms branch (leaf a) = atoms a
fold atoms branch (node l r) = branch (fold atoms branch l) (fold atoms branch r)
fold-unique : {A B : Type} (atoms : A → B) (branch : B → B → B)
  (h : Tree A → B)
  → ((a : A) → h (leaf a) ≡ atoms a)
  → ((l r : Tree A) → h (node l r) ≡ branch (h l) (h r))
  → (t : Tree A) → h t ≡ fold atoms branch t
fold-unique atoms branch h hl hn (leaf a) = hl a
fold-unique atoms branch h hl hn (node l r) = hn l r ∙
  cong₂ branch (fold-unique atoms branch h hl hn l) (fold-unique atoms branch h hl hn r)

-- Substitution is a particular fold, not a list of K/S reduction axioms.
plug : {A B : Type} → Tree A → (A → Tree B) → Tree B
plug t sigma = fold sigma node t
hole-beta : {A B : Type} (a : A) (sigma : A → Tree B) → plug (leaf a) sigma ≡ sigma a
hole-beta a sigma = refl
plug-identity : {A : Type} (t : Tree A) → plug t leaf ≡ t
plug-identity (leaf a) = refl
plug-identity (node l r) = cong₂ node (plug-identity l) (plug-identity r)
plug-compose : {A B C : Type} (t : Tree A) (sigma : A → Tree B) (tau : B → Tree C)
  → plug (plug t sigma) tau ≡ plug t (λ a → plug (sigma a) tau)
plug-compose (leaf a) sigma tau = refl
plug-compose (node l r) sigma tau =
  cong₂ node (plug-compose l sigma tau) (plug-compose r sigma tau)

-- Two and three input templates; environments come from tuples of trees.
lookup2 : {A : Type} → Tree A → Tree A → Bool → Tree A
lookup2 x y false = x
lookup2 x y true = y
K-template : Tree Bool
K-template = leaf false
instantiate2 : {A : Type} → Tree Bool → Tree A → Tree A → Tree A
instantiate2 t x y = plug t (lookup2 x y)
K-expands : {A : Type} (x y : Tree A) → instantiate2 K-template x y ≡ x
K-expands x y = refl

data Slot : Type where
  f-slot g-slot x-slot : Slot
lookup3 : {A : Type} → Tree A → Tree A → Tree A → Slot → Tree A
lookup3 f g x f-slot = f
lookup3 f g x g-slot = g
lookup3 f g x x-slot = x
S-template : Tree Slot
S-template = node (node (leaf f-slot) (leaf x-slot)) (node (leaf g-slot) (leaf x-slot))
instantiate3 : {A : Type} → Tree Slot → Tree A → Tree A → Tree A → Tree A
instantiate3 t f g x = plug t (lookup3 f g x)
S-expands : {A : Type} (f g x : Tree A)
  → instantiate3 S-template f g x ≡ node (node f x) (node g x)
S-expands f g x = refl

-- One-hole abstraction is a template, not yet an internal function value.
data Hole (A : Type) : Type where
  free : A → Hole A
  bound : Hole A
fill : {A : Type} → Tree (Hole A) → Tree A → Tree A
fill body arg = plug body λ { (free a) → leaf a ; bound → arg }
fill-bound : {A : Type} (arg : Tree A) → fill (leaf bound) arg ≡ arg
fill-bound arg = refl
fill-free : {A : Type} (a : A) (arg : Tree A) → fill (leaf (free a)) arg ≡ leaf a
fill-free a arg = refl
fill-node : {A : Type} (l r : Tree (Hole A)) (arg : Tree A)
  → fill (node l r) arg ≡ node (fill l arg) (fill r arg)
fill-node l r arg = refl

-- E trees acting on E trees: flattening is obtained from the same fold.
flatten : {A : Type} → Tree (Tree A) → Tree A
flatten t = plug t (λ x → x)
root : {A : Type} → Tree A → Bool
root (leaf a) = true
root (node l r) = false
no-flatten-recovery : {A : Type} (a : A) (recover : Tree A → Tree (Tree A))
  → ((t : Tree (Tree A)) → recover (flatten t) ≡ t) → ⊥
no-flatten-recovery a recover law = true≢false
  (cong root (sym (law (leaf (node (leaf a) (leaf a))))
    ∙ law (node (leaf (leaf a)) (leaf (leaf a)))))

-- The eliminator admits different node algebras. It does not choose execution.
left-readout right-readout : Tree Bool → Bool
left-readout = fold (λ b → b) (λ l r → l)
right-readout = fold (λ b → b) (λ l r → r)
algebra-choice-matters : left-readout (node (leaf false) (leaf true))
  ≡ right-readout (node (leaf false) (leaf true)) → ⊥
algebra-choice-matters p = false≢true p

-- One-hole templates do not represent the whole function type. Even a
-- label-changing recursive map cannot be expressed by insertion alone.
flip-leaves : Tree Bool → Tree Bool
flip-leaves = fold (λ { false → leaf true ; true → leaf false }) node
not-all-functions-are-templates : (t : Tree (Hole Bool))
  → ((arg : Tree Bool) → fill t arg ≡ flip-leaves arg) → ⊥
not-all-functions-are-templates (leaf bound) law =
  false≢true (cong left-readout (law (leaf false)))
not-all-functions-are-templates (leaf (free false)) law =
  false≢true (cong left-readout (law (leaf false)))
not-all-functions-are-templates (leaf (free true)) law =
  true≢false (cong left-readout (law (leaf true)))
not-all-functions-are-templates (node l r) law =
  false≢true (cong root (law (leaf false)))

-- Keep the template, every argument, the result and its compatibility path.
record Instance (V A : Type) : Type where
  constructor witnessed
  field
    body : Tree V
    arguments : V → Tree A
    result : Tree A
    compatible : plug body arguments ≡ result
instantiate-retained : {V A : Type} (t : Tree V) (env : V → Tree A) → Instance V A
instantiate-retained t env = witnessed t env (plug t env) refl
as-Q : {V A : Type} → Instance V A → Q.Complete
as-Q {V} {A} p = Q.pack (Q.atom (Instance V A)) p
K-unused-input-retained : {A : Type} (x y : Tree A)
  → Instance.arguments (Q.value (as-Q (instantiate-retained K-template (lookup2 x y)))) true ≡ y
K-unused-input-retained x y = refl
