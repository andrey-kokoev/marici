{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPEConstructorComparison where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_)
open import Agda.Builtin.String using (String)
import RamseyExternalPE as External

module Compare (Source : Type) (payload : Source → String)
  (LeafRelation : Source → Source → Type) where
  module T = External.Trees Source payload
  closed : T.Tree → T.R.Closed
  closed t = T.encode t , T.realize t

  data Correspondence : T.Tree → T.Tree → Type₁ where
    leaf : (s t : Source) → LeafRelation s t → Correspondence (T.leaf s) (T.leaf t)
    product : (I J : Type) (e : I ≃ J) (f : I → T.Tree) (g : J → T.Tree)
      → ((i : I) → Correspondence (f i) (g (fst e i)))
      → Correspondence (T.product I f) (T.product J g)
    selection : (I J : Type) (e : I ≃ J) (f : I → T.Tree) (g : J → T.Tree)
      (selected : I) (target : J) → fst e selected ≡ target
      → ((i : I) → Correspondence (f i) (g (fst e i)))
      → Correspondence (T.selection I f selected) (T.selection J g target)

  -- Owner-local relation indexed by the actual compiled native packages AND proofs.
  -- This is not an equality relation or a new constructor of native Resolve.
  data NativeComparison : T.R.Closed → T.R.Closed → Type₁ where
    seed : (s t : Source) → LeafRelation s t
      → NativeComparison (closed (T.leaf s)) (closed (T.leaf t))
    product : (I J : Type) (e : I ≃ J) (f : I → T.Tree) (g : J → T.Tree)
      → ((i : I) → NativeComparison (closed (f i)) (closed (g (fst e i))))
      → NativeComparison (closed (T.product I f)) (closed (T.product J g))
    selection : (I J : Type) (e : I ≃ J) (f : I → T.Tree) (g : J → T.Tree)
      (selected : I) (target : J) → fst e selected ≡ target
      → ((i : I) → NativeComparison (closed (f i)) (closed (g (fst e i))))
      → NativeComparison (closed (T.selection I f selected)) (closed (T.selection J g target))

  compile : {s t : T.Tree} → Correspondence s t → NativeComparison (closed s) (closed t)
  compile (leaf s t witness) = seed s t witness
  compile (product I J e f g branches) = product I J e f g (λ i → compile (branches i))
  compile (selection I J e f g selected target agreement branches) =
    selection I J e f g selected target agreement (λ i → compile (branches i))

  product-premises : (I J : Type) (e : I ≃ J) (f : I → T.Tree) (g : J → T.Tree)
    → ((i : I) → Correspondence (f i) (g (fst e i)))
    → (i : I) → NativeComparison
      (T.R.premise (closed (T.product I f)) (lift i))
      (T.R.premise (closed (T.product J g)) (lift (fst e i)))
  product-premises I J e f g branches i = compile (branches i)

  -- Quantified over ALL E prerequisites, including the unselected ones.
  selection-premises : (I J : Type) (e : I ≃ J) (f : I → T.Tree) (g : J → T.Tree)
    (selected : I) (target : J) → fst e selected ≡ target
    → ((i : I) → Correspondence (f i) (g (fst e i)))
    → (i : I) → NativeComparison
      (T.R.premise (closed (T.selection I f selected)) (lift i))
      (T.R.premise (closed (T.selection J g target)) (lift (fst e i)))
  selection-premises I J e f g selected target agreement branches i = compile (branches i)
