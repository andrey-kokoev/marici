{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyExactSource where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Int.Base using (ℤ; pos; _+_; -_; abs)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Relation.Nullary using (Dec; yes; no; ¬_)
open import RamseyUniformRelative using (Slot; first; next; Word; nil; cons)
import RamseyUniformRelative as U
open import RamseyUniformSigned using (Point3; zero3; add3; signed-geometry)
import Cubical.Data.Int.Properties as Z
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

-- L is parametrized injectively by (a,b,c), with lattice point
-- (a+b,a+c,b+c). The all-index inverse on D3 is documented separately.
Shift = Point3
Bary : Type
Bary = Σ ℤ (λ _ → Σ ℤ (λ _ → Σ ℤ (λ _ → ℤ)))
project : Shift → Point3
project (a , (b , c)) = (a + b) , ((a + c) , (b + c))
shuffle : (x y z w : ℤ) → (x + y) + (z + w) ≡ (x + z) + (y + w)
shuffle x y z w = sym (Z.+Assoc x y (z + w))
  ∙ cong (λ v → x + v) (Z.+Assoc y z w ∙ cong (λ v → v + w) (Z.+Comm y z) ∙ sym (Z.+Assoc z y w))
  ∙ Z.+Assoc x z (y + w)
project-add : (s t : Shift) → project (add3 s t) ≡ add3 (project s) (project t)
project-add (a , (b , c)) (d , (e , f)) i = shuffle a d b e i , (shuffle a d c f i , shuffle b e c f i)
project-bary : Bary → Point3
project-bary (d , (a , (b , c))) = (a + b) , ((a + c) , (b + c))
data Label : Type where
  C0 M0 C1 M1 C2 : Label
data Context : Type where
  prepared : Shift → Context
-- All five references are derived, never independently assignable strings.
reference : Context → Label → Bary
reference (prepared (a , (b , c))) C0 = (-(a + (b + c)) + pos 1) , (a , (b , c))
reference (prepared (a , (b , c))) M0 = -(a + (b + c)) , ((a + pos 1) , (b , c))
reference (prepared (a , (b , c))) C1 = -(a + (b + c)) , (a , ((b + pos 1) , c))
reference (prepared (a , (b , c))) M1 = -(a + (b + c)) , (a , (b , (c + pos 1)))
reference (prepared (a , (b , c))) C2 = (-(a + (b + c)) + - (pos 1)) , ((a + pos 1) , (b , (c + pos 1)))
observed-point : Context → Point3
observed-point c = project-bary (reference c C0)
point-binding : (s : Shift) → observed-point (prepared s) ≡ project s
point-binding s = refl
Pbody Nbody : Context → Slot 4 → Bary
Pbody c first = reference c C0
Pbody c (next first) = reference c M0
Pbody c (next (next first)) = reference c C1
Pbody c (next (next (next first))) = reference c M1
Pbody c (next (next (next (next ()))))
Nbody c first = reference c M0
Nbody c (next first) = reference c C1
Nbody c (next (next first)) = reference c M1
Nbody c (next (next (next first))) = reference c C2
Nbody c (next (next (next (next ()))))
source-face target-face : Context → Slot 3 → Bary
source-face c first = Pbody c (next first)
source-face c (next first) = Pbody c (next (next first))
source-face c (next (next first)) = Pbody c (next (next (next first)))
source-face c (next (next (next ())))
target-face c first = Nbody c first
target-face c (next first) = Nbody c (next first)
target-face c (next (next first)) = Nbody c (next (next first))
target-face c (next (next (next ())))
shared-face : (c : Context) → source-face c ≡ target-face c
shared-face c = funExt (λ { first → refl ; (next first) → refl ; (next (next first)) → refl ; (next (next (next ()))) })
permutation : Slot 5 → Slot 5
permutation first = next (next (next first))
permutation (next first) = next first
permutation (next (next first)) = next (next first)
permutation (next (next (next first))) = first
permutation (next (next (next (next first)))) = next (next (next (next first)))
permutation (next (next (next (next (next ())))))
permutation-involution : (i : Slot 5) → permutation (permutation i) ≡ i
permutation-involution first = refl
permutation-involution (next first) = refl
permutation-involution (next (next first)) = refl
permutation-involution (next (next (next first))) = refl
permutation-involution (next (next (next (next first)))) = refl
permutation-involution (next (next (next (next (next ())))))

Truth : Bool → Type
Truth true = Unit
Truth false = ⊥
decTruth : (b : Bool) → Dec (Truth b)
decTruth true = yes tt
decTruth false = no (λ ())
leq : ℕ → ℕ → Bool
leq zero n = true
leq (suc m) zero = false
leq (suc m) (suc n) = leq m n
both : Bool → Bool → Bool
both true b = b
both false b = false
within : ℕ → Shift → Bool
within radius s with project s
... | x , (y , z) = both (leq (abs x) radius) (both (leq (abs y) radius) (leq (abs z) radius))
Member : ℕ → Shift → Type
Member radius s = Truth (within radius s)
Region : ℕ → Type
Region radius = Σ Shift (Member radius)
region-context : {radius : ℕ} → Region radius → Context
region-context (s , h) = prepared s
region-point : {radius : ℕ} → Region radius → Point3
region-point (s , h) = project s
region-binding : {radius : ℕ} (i : Region radius) → observed-point (region-context i) ≡ region-point i
region-binding (s , h) = refl
-- When the same shift belongs to two cutoffs, every full reference is equal.
cutoff-reference : {r t : ℕ} (s : Shift) (h : Member r s) (j : Member t s)
  → reference (region-context {r} (s , h)) ≡ reference (region-context {t} (s , j))
cutoff-reference s h j = refl

module Query (radius k n r : ℕ) (letters : Slot k → Shift)
  (color : Region radius → Slot r) where
  module A = U.Arithmetic signed-geometry (Slot k) letters
  module P = U.Arithmetic signed-geometry (Slot k) (λ a → project (letters a))
  project-word : {m : ℕ} (w : Word (Slot k) m) → project (A.phi w) ≡ P.phi w
  project-word nil = refl
  project-word (cons a w) = project-add (letters a) (A.phi w) ∙ cong (add3 (project (letters a))) (project-word w)
  project-repeat : (m : ℕ) (s : Shift) → project (A.repeat-add m s) ≡ P.repeat-add m (project s)
  project-repeat zero s = refl
  project-repeat (suc m) s = project-add s (A.repeat-add m s) ∙ cong (add3 (project s)) (project-repeat m s)
  Request = Word (Slot k) n
  Row : Type
  Row = Σ Context (λ _ → Slot r)
  fiber : Region radius → G.Package
  fiber i = N.pack (G.atom-node Row) (region-context i , color i)
  Admit : G.Package → Type (ℓ-suc ℓ-zero)
  Admit q = Σ (Region radius) (λ i → q ≡ fiber i)
  module R = Resolution.Full ℓ-zero Admit
  seed-at : (i : Region radius) → R.Resolve (fiber i)
  seed-at i = R.seed (i , refl)
  family : R.Resolve (N.Pi-package (Region radius) fiber)
  family = R.apply (N.P-kind , Region radius , fiber) (λ { (lift i) → seed-at i })
  empty-fiber : ⊥ → G.Package
  empty-fiber ()
  empty-package = N.Pi-package ⊥ empty-fiber
  empty-proof : R.Resolve empty-package
  empty-proof = R.apply (N.P-kind , ⊥ , empty-fiber) (λ { (lift ()) })
  data Decision (s : Shift) : Type where
    inside : Member radius s → Decision s
    outside : ¬ Member radius s → Decision s
  classify : (s : Shift) → Decision s
  classify s with decTruth (within radius s)
  ... | yes h = inside h
  ... | no h = outside h
  body : (s : Shift) → Decision s → G.Package
  body s (inside h) = N.E-package (Region radius) fiber (s , h)
  body s (outside h) = N.E-package (¬ Member radius s) (λ _ → empty-package) h
  body-proof : (s : Shift) (d : Decision s) → R.Resolve (body s d)
  body-proof s (inside h) = R.apply (N.E-kind , Region radius , fiber , (s , h)) (λ { (lift i) → seed-at i })
  body-proof s (outside h) = R.apply (N.E-kind , (¬ Member radius s) , (λ _ → empty-package) , h) (λ { (lift j) → empty-proof })
  instruction : Request → G.Package
  instruction w = body (A.phi w) (classify (A.phi w))
  instruction-proof : (w : Request) → R.Resolve (instruction w)
  instruction-proof w = body-proof (A.phi w) (classify (A.phi w))
  table : R.Resolve (N.Pi-package Request instruction)
  table = R.apply (N.P-kind , Request , instruction) (λ { (lift w) → instruction-proof w })
  query-package : Request → G.Package
  query-package w = N.E-package Request instruction w
  query : (w : Request) → R.Resolve (query-package w)
  query w = R.apply (N.E-kind , Request , instruction , w) (λ { (lift v) → instruction-proof v })
  data Component : Type where
    prepared-input compiled-program answer : Component
  part : Request → Component → G.Package
  part w prepared-input = N.Pi-package (Region radius) fiber
  part w compiled-program = N.Pi-package Request instruction
  part w answer = query-package w
  part-proof : (w : Request) (c : Component) → R.Resolve (part w c)
  part-proof w prepared-input = family
  part-proof w compiled-program = table
  part-proof w answer = query w
  result-package : Request → G.Package
  result-package w = N.Pi-package Component (part w)
  result : (w : Request) → R.Resolve (result-package w)
  result w = R.apply (N.P-kind , Component , part w) (λ { (lift c) → part-proof w c })
  result-value : (w : Request) → N.value (result-package w) answer ≡ (w , N.value (instruction w))
  result-value w = refl
  retains-input : (w : Request) → R.premise (result-package w , result w) (lift prepared-input)
    ≡ (N.Pi-package (Region radius) fiber , family)
  retains-input w = refl
  retains-program : (w : Request) → R.premise (result-package w , result w) (lift compiled-program)
    ≡ (N.Pi-package Request instruction , table)
  retains-program w = refl
  actual-point-square : (s : Shift) (h : Member radius s)
    → observed-point (fst (snd (N.value (body s (inside h))))) ≡ project s
  actual-point-square s h = refl
  actual-color-square : (s : Shift) (h : Member radius s)
    → snd (snd (N.value (body s (inside h)))) ≡ color (s , h)
  actual-color-square s h = refl
  substitution-source : (t : Word A.Token n) (a : Slot k)
    → R.Resolve (result-package (A.instantiate t a))
  substitution-source t a = result (A.instantiate t a)
  substitution-shift : (t : Word A.Token n) (a : Slot k)
    → A.phi (A.instantiate t a) ≡ add3 (A.base t) (A.repeat-add (A.multiplicity t) (letters a))
  substitution-shift = A.substitution-law
  substitution-point : (t : Word A.Token n) (a : Slot k)
    → project (A.phi (A.instantiate t a)) ≡ add3 (project (A.base t)) (P.repeat-add (A.multiplicity t) (project (letters a)))
  substitution-point t a = cong project (A.substitution-law t a)
    ∙ project-add (A.base t) (A.repeat-add (A.multiplicity t) (letters a))
    ∙ cong (add3 (project (A.base t))) (project-repeat (A.multiplicity t) (letters a))
