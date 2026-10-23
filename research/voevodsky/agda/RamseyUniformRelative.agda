{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyUniformRelative where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Relation.Nullary using (Discrete; yes; no; ¬_)
open import Agda.Builtin.String using (String)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

-- Finite domains and length-indexed requests. No fixed numerical cutoff.
Slot : ℕ → Type
Slot zero = ⊥
Slot (suc m) = Unit ⊎ Slot m
pattern first = inl tt
pattern next i = inr i
data Word (A : Type) : ℕ → Type where
  nil : Word A zero
  cons : {n : ℕ} → A → Word A n → Word A (suc n)
record Geometry : Type (ℓ-suc ℓ-zero) where
  field
    Point : Type
    origin : Point
    add : Point → Point → Point
    decide : Discrete Point
    unit-left : (x : Point) → add origin x ≡ x
    assoc : (x y z : Point) → add (add x y) z ≡ add x (add y z)
    comm : (x y : Point) → add x y ≡ add y x

module Arithmetic (geo : Geometry) (A : Type) (letters : A → Geometry.Point geo) where
  open Geometry geo
  phi : {n : ℕ} → Word A n → Point
  phi nil = origin
  phi (cons a w) = add (letters a) (phi w)
  data Token : Type where
    fixed : A → Token
    hole-token : Token
  instantiate : {n : ℕ} → Word Token n → A → Word A n
  instantiate nil a = nil
  instantiate (cons (fixed b) t) a = cons b (instantiate t a)
  instantiate (cons hole-token t) a = cons a (instantiate t a)
  base : {n : ℕ} → Word Token n → Point
  base nil = origin
  base (cons (fixed b) t) = add (letters b) (base t)
  base (cons hole-token t) = base t
  multiplicity : {n : ℕ} → Word Token n → ℕ
  multiplicity nil = zero
  multiplicity (cons (fixed b) t) = multiplicity t
  multiplicity (cons hole-token t) = suc (multiplicity t)
  repeat-add : ℕ → Point → Point
  repeat-add zero x = origin
  repeat-add (suc m) x = add x (repeat-add m x)
  interchange : (x y z : Point) → add x (add y z) ≡ add y (add x z)
  interchange x y z = sym (assoc x y z) ∙ cong (λ v → add v z) (comm x y) ∙ assoc y x z
  substitution-law : {n : ℕ} (t : Word Token n) (a : A)
    → phi (instantiate t a) ≡ add (base t) (repeat-add (multiplicity t) (letters a))
  substitution-law nil a = sym (unit-left origin)
  substitution-law (cons (fixed b) t) a = cong (add (letters b)) (substitution-law t a)
    ∙ sym (assoc (letters b) (base t) (repeat-add (multiplicity t) (letters a)))
  substitution-law (cons hole-token t) a = cong (add (letters a)) (substitution-law t a)
    ∙ interchange (letters a) (base t) (repeat-add (multiplicity t) (letters a))
  data HasVariable : {n : ℕ} → Word Token n → Type where
    here : {n : ℕ} (t : Word Token n) → HasVariable (cons hole-token t)
    later : {n : ℕ} (a : A) {t : Word Token n} → HasVariable t → HasVariable (cons (fixed a) t)
  positive-multiplicity : {n : ℕ} {t : Word Token n} → HasVariable t → Σ ℕ (λ m → multiplicity t ≡ suc m)
  positive-multiplicity (here t) = multiplicity t , refl
  positive-multiplicity (later a h) = positive-multiplicity h

module Lookup (geo : Geometry) where
  open Geometry geo
  Missing : {m : ℕ} → (Slot m → Point) → Point → Type
  Missing at p = (i : _) → ¬ (at i ≡ p)
  data Located {m : ℕ} (at : Slot m → Point) (p : Point) : Type where
    hit : (i : Slot m) → at i ≡ p → Located at p
    miss : Missing at p → Located at p
  find : {m : ℕ} (at : Slot m → Point) (p : Point) → Located at p
  find {zero} at p = miss (λ ())
  find {suc m} at p with decide (at first) p
  ... | yes e = hit first e
  ... | no neq with find (λ i → at (next i)) p
  ...   | hit i e = hit (next i) e
  ...   | miss absent = miss (λ { first → neq ; (next i) → absent i })

-- RELATIVE means exactly this: at/contexts are supplied separately. No theorem
-- below asserts that an opaque context string realizes its declared point.
module Compiler (geo : Geometry) (k m n r : ℕ)
  (letters : Slot k → Geometry.Point geo)
  (at : Slot m → Geometry.Point geo)
  (contexts : Slot m → String) (colors : Slot m → Slot r) where
  open Geometry geo
  module A = Arithmetic geo (Slot k) letters
  module L = Lookup geo
  Request = Word (Slot k) n
  Row : Type
  Row = Σ String (λ _ → Slot r)
  fiber : Slot m → G.Package
  fiber i = N.pack (G.atom-node Row) (contexts i , colors i)
  Admit : G.Package → Type (ℓ-suc ℓ-zero)
  Admit q = Σ (Slot m) (λ i → q ≡ fiber i)
  module R = Resolution.Full ℓ-zero Admit
  seed-at : (i : Slot m) → R.Resolve (fiber i)
  seed-at i = R.seed (i , refl)
  family : R.Resolve (N.Pi-package (Slot m) fiber)
  family = R.apply (N.P-kind , Slot m , fiber) (λ { (lift i) → seed-at i })
  empty-fiber : ⊥ → G.Package
  empty-fiber ()
  empty-package : G.Package
  empty-package = N.Pi-package ⊥ empty-fiber
  empty-proof : R.Resolve empty-package
  empty-proof = R.apply (N.P-kind , ⊥ , empty-fiber) (λ { (lift ()) })

  -- Computed lookup, never a caller-supplied selected region index.
  compile : (w : Request) → L.Located at (A.phi w)
  compile w = L.find at (A.phi w)
  body : (p : Point) → L.Located at p → G.Package
  body p (L.hit i e) = N.E-package (Slot m) fiber i
  body p (L.miss absent) = N.E-package (L.Missing at p) (λ _ → empty-package) absent
  body-proof : (p : Point) (s : L.Located at p) → R.Resolve (body p s)
  body-proof p (L.hit i e) = R.apply (N.E-kind , Slot m , fiber , i) (λ { (lift j) → seed-at j })
  body-proof p (L.miss absent) = R.apply (N.E-kind , L.Missing at p , (λ _ → empty-package) , absent)
    (λ { (lift h) → empty-proof })
  instruction : Request → G.Package
  instruction w = body (A.phi w) (compile w)
  instruction-proof : (w : Request) → R.Resolve (instruction w)
  instruction-proof w = body-proof (A.phi w) (compile w)
  table : R.Resolve (N.Pi-package Request instruction)
  table = R.apply (N.P-kind , Request , instruction) (λ { (lift w) → instruction-proof w })
  query-package : Request → G.Package
  query-package w = N.E-package Request instruction w
  query : (w : Request) → R.Resolve (query-package w)
  query w = R.apply (N.E-kind , Request , instruction , w) (λ { (lift v) → instruction-proof v })
  data Component : Type where
    prepared program answer : Component
  part : Request → Component → G.Package
  part w prepared = N.Pi-package (Slot m) fiber
  part w program = N.Pi-package Request instruction
  part w answer = query-package w
  part-proof : (w : Request) (c : Component) → R.Resolve (part w c)
  part-proof w prepared = family
  part-proof w program = table
  part-proof w answer = query w
  result-package : Request → G.Package
  result-package w = N.Pi-package Component (part w)
  result : (w : Request) → R.Resolve (result-package w)
  result w = R.apply (N.P-kind , Component , part w) (λ { (lift c) → part-proof w c })
  query-value : (w : Request) → N.value (result-package w) answer ≡ (w , N.value (instruction w))
  query-value w = refl
  request-retained : (w : Request) → fst (N.value (result-package w) answer) ≡ w
  request-retained w = refl
  prepared-history-retained : (w : Request) → R.premise (result-package w , result w) (lift prepared)
    ≡ (N.Pi-package (Slot m) fiber , family)
  prepared-history-retained w = refl
  program-history-retained : (w : Request) → R.premise (result-package w , result w) (lift program)
    ≡ (N.Pi-package Request instruction , table)
  program-history-retained w = refl

  data Certified (p : Point) : Type where
    selected : (i : Slot m) → at i ≡ p → (v : Row) → v ≡ (contexts i , colors i) → Certified p
    refused : L.Missing at p → Certified p
  certify-body : (p : Point) (s : L.Located at p) → Certified p
  certify-body p (L.hit i e) = selected (fst (N.value (body p (L.hit i e)))) e
    (snd (N.value (body p (L.hit i e)))) refl
  certify-body p (L.miss absent) = refused (fst (N.value (body p (L.miss absent))))
  certified-query : (w : Request) → Certified (A.phi w)
  certified-query w = certify-body (A.phi w) (compile w)

  -- Variable-word substitution on exactly this same input family and policy.
  substituted-package : (t : Word A.Token n) → Slot k → G.Package
  substituted-package t a = result-package (A.instantiate t a)
  substituted-query : (t : Word A.Token n) (a : Slot k) → R.Resolve (substituted-package t a)
  substituted-query t a = result (A.instantiate t a)
  substituted-certificate : (t : Word A.Token n) (a : Slot k)
    → Certified (add (A.base t) (A.repeat-add (A.multiplicity t) (letters a)))
  substituted-certificate t a = subst Certified (A.substitution-law t a) (certified-query (A.instantiate t a))
