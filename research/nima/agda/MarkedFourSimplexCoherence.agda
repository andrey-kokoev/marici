{-# OPTIONS --safe --cubical --guardedness #-}
module MarkedFourSimplexCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (congEquiv; equivAdjointEquiv)
open import Cubical.Foundations.Path using (Square→compPath; compPathlEquiv; compPathrEquiv)
open import Cubical.Foundations.GroupoidLaws using (assoc; cong-∙; symDistr; pentagonIdentity)
import MarkedTetrahedronCoherence as Marked

-- Ordinary path algebra only: no Cubical-simplex decoder or presentation
-- bridge is used in the definition of the marked pentagon below.
private
  whisker-split : ∀ {ℓ ℓ'} {X : Type ℓ} {Y : Type ℓ'} (f : X → Y)
    {a b c : X} {d : Y} (p : a ≡ b) (q : b ≡ c) (r : f c ≡ d)
    → cong f (p ∙ q) ∙ r ≡ cong f p ∙ (cong f q ∙ r)
  whisker-split f p q r = cong (_∙ r) (cong-∙ f p q)
    ∙ sym (assoc (cong f p) (cong f q) r)

  slide : ∀ {ℓ} {X : Type ℓ} {a b c d z : X}
    (p : a ≡ b) (q : b ≡ c) (r : a ≡ d) (s : d ≡ c)
    → p ∙ q ≡ r ∙ s → (t : c ≡ z) → p ∙ (q ∙ t) ≡ r ∙ (s ∙ t)
  slide p q r s h t = assoc p q t ∙ cong (_∙ t) h ∙ sym (assoc r s t)

  naturality : ∀ {ℓ ℓ'} {X : Type ℓ} {Y : Type ℓ'} {f g : X → Y}
    (H : (x : X) → f x ≡ g x) {x y : X} (p : x ≡ y)
    → cong f p ∙ H y ≡ H x ∙ cong g p
  naturality H p = sym (Square→compPath (λ i j → H (p j) i))

module Pentagon {ℓ : Level} (A : Type ℓ) {x0 x1 x2 x3 x4 : A}
  (p : x0 ≡ x1) (q : x1 ≡ x2) (r : x2 ≡ x3) (s : x3 ≡ x4)
  (u : x0 ≡ x2) (v : x1 ≡ x3) (w : x2 ≡ x4)
  (x : x0 ≡ x3) (y : x1 ≡ x4) (z : x0 ≡ x4) where
  module M = Marked.Tetrahedra A
  record Faces : Type ℓ where
    constructor faces
    field
      a012 : p ∙ q ≡ u
      a123 : q ∙ r ≡ v
      a234 : r ∙ s ≡ w
      a013 : p ∙ v ≡ x
      a023 : u ∙ r ≡ x
      a124 : q ∙ w ≡ y
      a134 : v ∙ s ≡ y
      a014 : p ∙ y ≡ z
      a024 : u ∙ w ≡ z
      a034 : x ∙ s ≡ z

  edges0123 : M.Edges x0 x1 x2 x3
  edges0123 = record { e01 = p ; e12 = q ; e02 = u ; e23 = r ; e13 = v ; e03 = x }
  edges0124 : M.Edges x0 x1 x2 x4
  edges0124 = record { e01 = p ; e12 = q ; e02 = u ; e23 = w ; e13 = y ; e03 = z }
  edges0134 : M.Edges x0 x1 x3 x4
  edges0134 = record { e01 = p ; e12 = v ; e02 = x ; e23 = s ; e13 = y ; e03 = z }
  edges0234 : M.Edges x0 x2 x3 x4
  edges0234 = record { e01 = u ; e12 = r ; e02 = x ; e23 = s ; e13 = w ; e03 = z }
  edges1234 : M.Edges x1 x2 x3 x4
  edges1234 = record { e01 = q ; e12 = r ; e02 = v ; e23 = s ; e13 = w ; e03 = y }

  module WithFaces (a : Faces) where
    open Faces a
    T0123 = M.Over.Tetrahedron edges0123 a012 a123 a013 a023
    T0124 = M.Over.Tetrahedron edges0124 a012 a124 a014 a024
    T0134 = M.Over.Tetrahedron edges0134 a013 a134 a014 a034
    T0234 = M.Over.Tetrahedron edges0234 a023 a234 a024 a034
    T1234 = M.Over.Tetrahedron edges1234 a123 a234 a124 a134

    -- The five bracketings of four successive edges, with their reduction
    -- paths to the common diagonal. No tetrahedral witness is discarded.
    b1 = ((p ∙ q) ∙ r) ∙ s
    b2 = (p ∙ (q ∙ r)) ∙ s
    b3 = p ∙ ((q ∙ r) ∙ s)
    b4 = p ∙ (q ∙ (r ∙ s))
    b5 = (p ∙ q) ∙ (r ∙ s)
    r1 : b1 ≡ z
    r1 = cong (_∙ s) (cong (_∙ r) a012 ∙ a023) ∙ a034
    r2 : b2 ≡ z
    r2 = cong (_∙ s) (cong (p ∙_) a123 ∙ a013) ∙ a034
    r3 : b3 ≡ z
    r3 = cong (p ∙_) (cong (_∙ s) a123 ∙ a134) ∙ a014
    r4 : b4 ≡ z
    r4 = cong (p ∙_) (cong (q ∙_) a234 ∙ a124) ∙ a014
    r5 : b5 ≡ z
    r5 = cong (_∙ (r ∙ s)) a012 ∙ (cong (u ∙_) a234 ∙ a024)

    a12 : b1 ≡ b2
    a12 = cong (_∙ s) (sym (assoc p q r))
    a23 : b2 ≡ b3
    a23 = sym (assoc p (q ∙ r) s)
    a34 : b3 ≡ b4
    a34 = cong (p ∙_) (sym (assoc q r s))
    a15 : b1 ≡ b5
    a15 = sym (assoc (p ∙ q) r s)
    a54 : b5 ≡ b4
    a54 = sym (assoc p q (r ∙ s))

    edge12 : T0123 → r1 ≡ a12 ∙ r2
    edge12 t = cong (λ k → cong (_∙ s) k ∙ a034) t
      ∙ whisker-split (_∙ s) (sym (assoc p q r)) (cong (p ∙_) a123 ∙ a013) a034

    edge23 : T0134 → r2 ≡ a23 ∙ r3
    edge23 t = whisker-split (_∙ s) (cong (p ∙_) a123) a013 a034
      ∙ cong (cong (λ k → (p ∙ k) ∙ s) a123 ∙_) t
      ∙ slide _ _ _ _ (naturality (λ k → sym (assoc p k s)) a123)
          (cong (p ∙_) a134 ∙ a014)
      ∙ cong (a23 ∙_) (sym (whisker-split (p ∙_) (cong (_∙ s) a123) a134 a014))

    -- The third edge is an equivalence of witness spaces, allowing the
    -- opposite tetrahedron to be solved while retaining its full witness.
    edge34-equivalence : T1234 ≃ (r3 ≡ a34 ∙ r4)
    edge34-equivalence = compEquiv
      (congEquiv (compEquiv (congEquiv (compPathlEquiv p)) (compPathrEquiv a014)))
      (compPathrEquiv
        (whisker-split (p ∙_) (sym (assoc q r s)) (cong (q ∙_) a234 ∙ a124) a014))
    edge34 : T1234 → r3 ≡ a34 ∙ r4
    edge34 = equivFun edge34-equivalence

    edge15 : T0234 → r1 ≡ a15 ∙ r5
    edge15 t = whisker-split (_∙ s) (cong (_∙ r) a012) a023 a034
      ∙ cong (cong (λ k → (k ∙ r) ∙ s) a012 ∙_) t
      ∙ slide _ _ _ _ (naturality (λ k → sym (assoc k r s)) a012)
          (cong (u ∙_) a234 ∙ a024)

    edge54 : T0124 → r5 ≡ a54 ∙ r4
    edge54 t = slide _ _ _ _ (Square→compPath (λ i j → a012 i ∙ a234 j)) a024
      ∙ cong (cong ((p ∙ q) ∙_) a234 ∙_) t
      ∙ slide _ _ _ _ (naturality (λ k → sym (assoc p q k)) a234)
          (cong (p ∙_) a124 ∙ a014)
      ∙ cong (a54 ∙_) (sym (whisker-split (p ∙_) (cong (q ∙_) a234) a124 a014))

    -- Reverse the library's associator pentagon and normalize its double
    -- composition. This is the boundary correction between the two routes.
    base-pentagon : a15 ∙ a54 ≡ a12 ∙ (a23 ∙ a34)
    base-pentagon = sym (symDistr (assoc p q (r ∙ s)) (assoc (p ∙ q) r s))
      ∙ cong sym (pentagonIdentity p q r s
        ∙ doubleCompPath≡compPath (cong (p ∙_) (assoc q r s))
            (assoc p (q ∙ r) s) (cong (_∙ s) (assoc p q r)))
      ∙ symDistr (cong (p ∙_) (assoc q r s))
          (assoc p (q ∙ r) s ∙ cong (_∙ s) (assoc p q r))
      ∙ cong (_∙ a34) (symDistr (assoc p (q ∙ r) s) (cong (_∙ s) (assoc p q r)))
      ∙ sym (assoc a12 a23 a34)

    pentagon-tail : a15 ∙ (a54 ∙ r4) ≡ a12 ∙ (a23 ∙ (a34 ∙ r4))
    pentagon-tail = assoc a15 a54 r4 ∙ cong (_∙ r4) base-pentagon
      ∙ sym (assoc a12 (a23 ∙ a34) r4)
      ∙ cong (a12 ∙_) (sym (assoc a23 a34 r4))

    record Horn : Type ℓ where
      constructor horn
      field
        t0123 : T0123
        t0124 : T0124
        t0134 : T0134
        t0234 : T0234

    Route : Type ℓ
    Route = r1 ≡ a12 ∙ (a23 ∙ (a34 ∙ r4))
    long-route : (h : Horn) → T1234 ≃ Route
    long-route h = compEquiv edge34-equivalence
      (compEquiv (congEquiv (compPathlEquiv a23))
        (compEquiv (congEquiv (compPathlEquiv a12))
          (compEquiv (compPathlEquiv (cong (a12 ∙_) (edge23 (Horn.t0134 h))))
            (compPathlEquiv (edge12 (Horn.t0123 h))))))
    short-route : Horn → Route
    short-route h = edge15 (Horn.t0234 h)
      ∙ (cong (a15 ∙_) (edge54 (Horn.t0124 h)) ∙ pentagon-tail)

    FourCell : Horn → T1234 → Type ℓ
    FourCell h t = equivFun (long-route h) t ≡ short-route h
    Missing : Horn → Type ℓ
    Missing h = Σ[ t ∈ T1234 ] FourCell h t
    unique1234 : (h : Horn) → isContr (Missing h)
    unique1234 h = equiv-proof (snd (long-route h)) (short-route h)
    complete : (h : Horn) → Missing h
    complete h = invEq (long-route h) (short-route h) , secEq (long-route h) (short-route h)
    solve1234 : (h : Horn) (t : T1234)
      → FourCell h t ≃ (t ≡ invEq (long-route h) (short-route h))
    solve1234 h t = invEquiv (equivAdjointEquiv (long-route h))
