{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyExternalPE where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Agda.Builtin.String using (String)
import RamseyNativePNOverlapSpan as Span
import NativeTableResolution as Resolution
module G = Span.G
module N = Span.N

module Trees (Source : Type) (payload : Source → String) where
  data Tree : Type (ℓ-suc ℓ-zero) where
    leaf : Source → Tree
    product : (I : Type) → (I → Tree) → Tree
    selection : (I : Type) → (I → Tree) → I → Tree
  encode : Tree → G.Package
  encode (leaf s) = N.pack (G.atom-node String) (payload s)
  encode (product I f) = N.Pi-package I (λ i → encode (f i))
  encode (selection I f i) = N.E-package I (λ j → encode (f j)) i
  Admit : G.Package → Type (ℓ-suc ℓ-zero)
  Admit q = Σ Source (λ s → q ≡ encode (leaf s))
  module R = Resolution.Full ℓ-zero Admit
  realize : (t : Tree) → R.Resolve (encode t)
  realize (leaf s) = R.seed (s , refl)
  realize (product I f) = R.apply (N.P-kind , I , (λ i → encode (f i))) (λ { (lift i) → realize (f i) })
  realize (selection I f i) = R.apply (N.E-kind , I , (λ j → encode (f j)) , i) (λ { (lift j) → realize (f j) })
  -- E retains the whole prerequisite family, not only its selected branch.
  Occurrence : Tree → Type
  Occurrence (leaf s) = Unit
  Occurrence (product I f) = Σ I (λ i → Occurrence (f i))
  Occurrence (selection I f i) = Σ I (λ j → Occurrence (f j))
  origin : (t : Tree) → Occurrence t → Source
  origin (leaf s) tt = s
  origin (product I f) (i , o) = origin (f i) o
  origin (selection I f i) (j , o) = origin (f j) o
  Located : Type (ℓ-suc ℓ-zero)
  Located = Σ Tree Occurrence
  source-of : Located → Source
  source-of (t , o) = origin t o
  fixed-observation : {O : Type} (observe : Source → O) (x y : Located)
    → x ≡ y → observe (source-of x) ≡ observe (source-of y)
  fixed-observation observe x y path = cong (λ z → observe (source-of z)) path

module TracedSpans (Chart Face : Type) (Permit : Chart → Face → Type)
  (packet : (c : Chart) (f : Face) → Permit c f → String) where
  module S = Span.Spans Chart Face Permit packet
  module T = Trees S.InputIndex (λ { (c , (f , p)) → packet c f p })
  port : (c : Chart) (f : Face) → Permit c f → T.Tree
  port c f p = T.leaf (c , (f , p))
  leg : (a b : Chart) → S.Common a b → S.Side → T.Tree
  leg a b (f , (p , q)) S.source-leg = port a f p
  leg a b (f , (p , q)) S.target-leg = port b f q
  pair : (a b : Chart) → S.Common a b → T.Tree
  pair a b x = T.product S.Side (leg a b x)
  pair-cell : (a b : Chart) (x : S.Common a b) → T.encode (pair a b x) ≡ S.pair-package a b x
  pair-cell a b (f , (p , q)) = cong (N.Pi-package S.Side) (funExt (λ { S.source-leg → refl ; S.target-leg → refl }))
  selected : (a b : Chart) → S.Common a b → T.Tree
  selected a b x = T.selection (S.Common a b) (pair a b) x
  selected-cell : (a b : Chart) (x : S.Common a b) → T.encode (selected a b x) ≡ S.selected-package a b x
  selected-cell a b x = cong (λ f → N.E-package (S.Common a b) f x) (funExt (pair-cell a b))
  whole : (a b c : Chart) → S.Triple a b c → S.Three → T.Tree
  whole a b c (f , (p , (q , r))) S.first-port = port a f p
  whole a b c (f , (p , (q , r))) S.middle-port = port b f q
  whole a b c (f , (p , (q , r))) S.final-port = port c f r
  piece : (a b c : Chart) → S.Triple a b c → S.Piece → T.Tree
  piece a b c t S.AB = selected a b (S.ab-index t)
  piece a b c t S.BC = selected b c (S.bc-index t)
  piece a b c t S.AC = selected a c (S.ac-index t)
  piece a b c t S.full-source = T.product S.Three (whole a b c t)
  piece-cell : (a b c : Chart) (t : S.Triple a b c) (i : S.Piece)
    → T.encode (piece a b c t i) ≡ S.composition-part a b c t i
  piece-cell a b c t S.AB = selected-cell a b (S.ab-index t)
  piece-cell a b c t S.BC = selected-cell b c (S.bc-index t)
  piece-cell a b c t S.AC = selected-cell a c (S.ac-index t)
  piece-cell a b c (f , (p , (q , r))) S.full-source =
    cong (N.Pi-package S.Three) (funExt (λ { S.first-port → refl ; S.middle-port → refl ; S.final-port → refl }))
  composition : (a b c : Chart) → S.Triple a b c → T.Tree
  composition a b c t = T.product S.Piece (piece a b c t)
  composition-cell : (a b c : Chart) (t : S.Triple a b c)
    → T.encode (composition a b c t) ≡ S.composition-package a b c t
  composition-cell a b c t = cong (N.Pi-package S.Piece) (funExt (piece-cell a b c t))
