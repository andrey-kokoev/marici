{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedSquareReversal where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (_×_)
import ObserverCoherenceCube as Observer
import WholePackageSigmaPi as Whole

-- Reverse the actual source cell and its section, retaining its two schedules.
module Construction {ℓ : Level} (O R : Type ℓ) (e : O ≃ R) where
  module G = Observer.Geometry O R e
  module W = Whole.Universe ℓ

  backward-cell : I → I → Type ℓ
  backward-cell i j = G.square (~ i) (~ j)
  backward-section : (s : O × O) (i j : I) → backward-cell i j
  backward-section s i j = G.square-section s (~ i) (~ j)
  backward-start : (u v : O)
    → backward-section (u , v) i0 i0 ≡ (G.expand u , G.expand v)
  backward-start u v = refl
  backward-end : (u v : O) → backward-section (u , v) i1 i1 ≡ (u , v)
  backward-end u v = refl
  double-reverse-cell : (i j : I) → backward-cell (~ i) (~ j) ≡ G.square i j
  double-reverse-cell i j = refl
  double-reverse-section : (s : O × O) (i j : I)
    → backward-section s (~ i) (~ j) ≡ G.square-section s i j
  double-reverse-section s i j = refl

  record RetainedReturn : Type ℓ where
    constructor retained-return
    field
      original : G.RealizedSquare
      return-section : (i j : I) → backward-cell i j
      start-law : return-section i0 i0 ≡ G.RealizedSquare.target original
      end-law : return-section i1 i1 ≡ G.RealizedSquare.source original

  make-return : O × O → RetainedReturn
  make-return (u , v) = retained-return
    (W.value (G.nextQ (u , v))) (backward-section (u , v)) refl refl
  next-returned-Q : O × O → W.Complete
  next-returned-Q s = W.pack (W.atom RetainedReturn) (make-return s)
  recover-forward : (s : O × O)
    → RetainedReturn.original (W.value (next-returned-Q s)) ≡ W.value (G.nextQ s)
  recover-forward (u , v) = refl
  recover-source : (s : O × O)
    → G.RealizedSquare.source (RetainedReturn.original (W.value (next-returned-Q s))) ≡ s
  recover-source (u , v) = refl
  recover-first : (s : O × O)
    → G.ComparedRoutes.first (G.RealizedSquare.comparison
        (RetainedReturn.original (W.value (next-returned-Q s)))) ≡ G.leftFirst
  recover-first (u , v) = refl
  recover-second : (s : O × O)
    → G.ComparedRoutes.second (G.RealizedSquare.comparison
        (RetainedReturn.original (W.value (next-returned-Q s)))) ≡ G.rightFirst
  recover-second (u , v) = refl
