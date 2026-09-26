{-# OPTIONS --safe --cubical --guardedness #-}
module AmplitudeDiagramExpansion where
open import Cubical.Foundations.Prelude
open import Cubical.Data.List.Base using (List; []; _∷_; _++_; map)
open import Cubical.Algebra.Semiring.Base
import NativeAmplitudeResolution as Resolution

module Expansion (A : Type) (S : Semiring ℓ-zero) (weight : A → fst S) where
  open SemiringStr (snd S)
  module E = Resolution.Algebra A (fst S) weight 0r 1r _+_ _·_
  open E using (Expr; zero-expr; one-expr; factor; binary; sum-mode; product-mode)
  word : List A → fst S
  word [] = 1r
  word (a ∷ as) = weight a · word as
  sum-words : List (List A) → fst S
  sum-words [] = 0r
  sum-words (a ∷ as) = word a + sum-words as
  cross : List (List A) → List (List A) → List (List A)
  cross [] bs = []
  cross (a ∷ as) bs = map (a ++_) bs ++ cross as bs
  diagrams : Expr → List (List A)
  diagrams zero-expr = []
  diagrams one-expr = [] ∷ []
  diagrams (factor a) = (a ∷ []) ∷ []
  diagrams (binary sum-mode l r) = diagrams l ++ diagrams r
  diagrams (binary product-mode l r) = cross (diagrams l) (diagrams r)
  word-append : (as bs : List A) → word (as ++ bs) ≡ word as · word bs
  word-append [] bs = sym (·IdL (word bs))
  word-append (a ∷ as) bs = cong (weight a ·_) (word-append as bs)
    ∙ ·Assoc (weight a) (word as) (word bs)
  sum-append : (as bs : List (List A)) → sum-words (as ++ bs) ≡ sum-words as + sum-words bs
  sum-append [] bs = sym (+IdL (sum-words bs))
  sum-append (a ∷ as) bs = cong (word a +_) (sum-append as bs)
    ∙ +Assoc (word a) (sum-words as) (sum-words bs)
  left-product : (a : List A) (bs : List (List A)) → sum-words (map (a ++_) bs) ≡ word a · sum-words bs
  left-product a [] = sym (AnnihilR (word a))
  left-product a (b ∷ bs) = cong₂ _+_ (word-append a b) (left-product a bs)
    ∙ sym (·DistR+ (word a) (word b) (sum-words bs))
  cross-product : (as bs : List (List A)) → sum-words (cross as bs) ≡ sum-words as · sum-words bs
  cross-product [] bs = sym (AnnihilL (sum-words bs))
  cross-product (a ∷ as) bs = sum-append (map (a ++_) bs) (cross as bs)
    ∙ cong₂ _+_ (left-product a bs) (cross-product as bs)
    ∙ sym (·DistL+ (word a) (sum-words as) (sum-words bs))
  expansion-correct : (e : Expr) → sum-words (diagrams e) ≡ E.evaluate e
  expansion-correct zero-expr = refl
  expansion-correct one-expr = +IdR 1r
  expansion-correct (factor a) = cong (_+ 0r) (·IdR (weight a)) ∙ +IdR (weight a)
  expansion-correct (binary sum-mode l r) = sum-append (diagrams l) (diagrams r)
    ∙ cong₂ _+_ (expansion-correct l) (expansion-correct r)
  expansion-correct (binary product-mode l r) = cross-product (diagrams l) (diagrams r)
    ∙ cong₂ _·_ (expansion-correct l) (expansion-correct r)
  native-diagram-sum : (e : Expr) → E.readout e (snd (E.package e)) ≡ sum-words (diagrams e)
  native-diagram-sum e = E.native-correct e ∙ sym (expansion-correct e)
  translated-diagram-sum : (e : Expr) → E.readout e (E.aligned-value e) ≡ sum-words (diagrams e)
  translated-diagram-sum e = E.translated-amplitude e ∙ sym (expansion-correct e)
