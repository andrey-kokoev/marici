{-# OPTIONS --safe --cubical --guardedness #-}
module FourSimplexPentagonBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_; equivFun; invEq; compEquiv; invEquiv)
open import Cubical.Foundations.Isomorphism using (isoToEquiv)
open import Cubical.Foundations.Path using (PathP≃Path; compPathlEquiv; symIso)
open import Cubical.Foundations.Univalence using (pathToEquiv)
import FourSimplexHorn as Cube
import FourSimplexEquationBridge as Equation
import MarkedFourSimplexCoherence as Marked
import RetainedTetrahedralPackage as Retained

-- The pentagon relation is authored independently in MarkedFourSimplexCoherence.
-- This module matches the boundary data and isolates, but does not assume or
-- prove, the higher coherence identifying it with the induced equation family.
module Bridge {ℓ : Level} (A : Type ℓ)
  (v : Cube.Simplex.Vertices A)
  (e : Cube.Simplex.At.Edges A v)
  (a : Cube.Simplex.At.WithEdges.Faces A v e) where
  module C = Cube.Simplex A
  module B = Equation.Bridge A v e a
  open C.Vertices v
  open C.At.Edges e
  open C.At.WithEdges.Faces a
  module P0 = Marked.Pentagon A e01 e12 e23 e34 e02 e13 e24 e03 e14 e04

  translated-faces : P0.Faces
  translated-faces = P0.faces
    (equivFun (C.triangle-comparison e01 e12 e02) a012)
    (equivFun (C.triangle-comparison e12 e23 e13) a123)
    (equivFun (C.triangle-comparison e23 e34 e24) a234)
    (equivFun (C.triangle-comparison e01 e13 e03) a013)
    (equivFun (C.triangle-comparison e02 e23 e03) a023)
    (equivFun (C.triangle-comparison e12 e24 e14) a124)
    (equivFun (C.triangle-comparison e13 e34 e14) a134)
    (equivFun (C.triangle-comparison e01 e14 e04) a014)
    (equivFun (C.triangle-comparison e02 e24 e04) a024)
    (equivFun (C.triangle-comparison e03 e34 e04) a034)
  module P = P0.WithFaces translated-faces

  pentagon-horn : B.EquationHorn → P.Horn
  pentagon-horn h = P.horn (B.EquationHorn.t0123 h) (B.EquationHorn.t0124 h)
    (B.EquationHorn.t0134 h) (B.EquationHorn.t0234 h)

  PentagonFourCell : B.EquationHorn → B.O1234 → Type ℓ
  PentagonFourCell h t = P.FourCell (pentagon-horn h) t

  induced-center : B.EquationHorn → B.O1234
  induced-center h = transport (λ i → B.EquationFamily (B.from-equation-horn h) i)
    (B.EquationHorn.t0234 h)
  pentagon-center : B.EquationHorn → B.O1234
  pentagon-center h = invEq (P.long-route (pentagon-horn h))
    (P.short-route (pentagon-horn h))

  -- Exact fixed-five-tetrahedron target. No replacement or quotienting of
  -- the fifth tetrahedron is allowed by this signature.
  Goal : Type ℓ
  Goal = (h : B.EquationHorn) (t : B.O1234)
    → B.OldFourCell h t ≃ PentagonFourCell h t

  CenterCoherence : Type ℓ
  CenterCoherence = (h : B.EquationHorn) → induced-center h ≡ pentagon-center h
  RouteCoherence : Type ℓ
  RouteCoherence = (h : B.EquationHorn)
    → equivFun (P.long-route (pentagon-horn h)) (induced-center h)
      ≡ P.short-route (pentagon-horn h)

  from-route-coherence : RouteCoherence → CenterCoherence
  from-route-coherence n h = equivFun
    (P.solve1234 (pentagon-horn h) (induced-center h)) (n h)
  to-route-coherence : CenterCoherence → RouteCoherence
  to-route-coherence n h = invEq
    (P.solve1234 (pentagon-horn h) (induced-center h)) (n h)

  from-center-coherence : CenterCoherence → Goal
  from-center-coherence n h t = compEquiv
    (PathP≃Path (B.EquationFamily (B.from-equation-horn h)) (B.EquationHorn.t0234 h) t)
    (compEquiv (compPathlEquiv (sym (n h)))
      (compEquiv (isoToEquiv symIso) (invEquiv (P.solve1234 (pentagon-horn h) t))))

  -- The same coherence is necessary: evaluate any proposed fixed-boundary
  -- comparison on the canonical transport filler, retaining its fifth face.
  to-center-coherence : Goal → CenterCoherence
  to-center-coherence compare h = equivFun
    (P.solve1234 (pentagon-horn h) (induced-center h))
    (equivFun (compare h (induced-center h))
      (transport-filler (λ i → B.EquationFamily (B.from-equation-horn h) i) (B.EquationHorn.t0234 h)))

  -- Extract the fifth-face part of the already proved completion square.
  -- This compares values in the SAME induced presentation; it does not
  -- compare the two independent completion spaces by contractibility.
  translated-center : B.F.Horn → B.O1234
  translated-center h = equivFun B.e1234 (fst (fst (B.F.unique h)))

  induced-center-on-image : (h : B.F.Horn)
    → induced-center (B.to-equation-horn h) ≡ translated-center h
  induced-center-on-image h = sym (cong fst (B.old-completion-square h))

  -- It is enough, and necessary, to verify the independent pentagon on the
  -- translated canonical Cubical completion. This statement has no decoding
  -- or endpoint-reindexing operations in its fifth tetrahedron.
  GeneratedRouteCoherence : Type ℓ
  GeneratedRouteCoherence = (h : B.F.Horn)
    → PentagonFourCell (B.to-equation-horn h) (translated-center h)

  -- Replace all five opaque comparison applications by their PROVED sweep
  -- formulas. This is a normalization of the chosen maps, not new choices.
  sweep-horn : B.F.Horn → P.Horn
  sweep-horn h = P.horn
    (B.B0123.sweep-expression B.F.s0123 (B.F.Horn.t0123 h))
    (B.B0124.sweep-expression B.F.s0124 (B.F.Horn.t0124 h))
    (B.B0134.sweep-expression B.F.s0134 (B.F.Horn.t0134 h))
    (B.B0234.sweep-expression B.F.s0234 (B.F.Horn.t0234 h))
  sweep-center : B.F.Horn → B.O1234
  sweep-center h = B.B1234.sweep-expression B.F.s1234 (fst (fst (B.F.unique h)))

  horn-sweep-computation : (h : B.F.Horn)
    → pentagon-horn (B.to-equation-horn h) ≡ sweep-horn h
  horn-sweep-computation h i = P.horn
    (B.B0123.equivalence-sweep-computation B.F.s0123 (B.F.Horn.t0123 h) i)
    (B.B0124.equivalence-sweep-computation B.F.s0124 (B.F.Horn.t0124 h) i)
    (B.B0134.equivalence-sweep-computation B.F.s0134 (B.F.Horn.t0134 h) i)
    (B.B0234.equivalence-sweep-computation B.F.s0234 (B.F.Horn.t0234 h) i)
  center-sweep-computation : (h : B.F.Horn) → translated-center h ≡ sweep-center h
  center-sweep-computation h = B.B1234.equivalence-sweep-computation
    B.F.s1234 (fst (fst (B.F.unique h)))

  sweep-pentagon-normalization : (h : B.F.Horn)
    → PentagonFourCell (B.to-equation-horn h) (translated-center h)
      ≃ P.FourCell (sweep-horn h) (sweep-center h)
  sweep-pentagon-normalization h = pathToEquiv
    (λ i → P.FourCell (horn-sweep-computation h i) (center-sweep-computation h i))

  generated-from-sweep : ((h : B.F.Horn) → P.FourCell (sweep-horn h) (sweep-center h))
    → GeneratedRouteCoherence
  generated-from-sweep n h = invEq (sweep-pentagon-normalization h) (n h)

  -- A genuine cube of paths from x0 to x4, obtained from a filled Cubical
  -- four-simplex by composing the three moving initial segments. Its six
  -- faces are explicit; five carry the tetrahedral witnesses and the sixth
  -- carries the collapsed 234 triangle. Endpoint normalization to the marked
  -- pentagon is still needed; the cube alone does not assert that theorem.
  flag-sweep : (h : B.F.Horn) (t : B.F.T1234) → B.F.FourCell h t
    → I → I → I → x0 ≡ x4
  flag-sweep h t u i j k = (λ l → e01 (i ∧ l))
    ∙ ((λ l → a012 i (j ∧ l))
      ∙ ((λ l → B.F.Horn.t0123 h i j (k ∧ l)) ∙ u i j k))

  flag-initial : (h : B.F.Horn) (t : B.F.T1234) (u : B.F.FourCell h t)
    → flag-sweep h t u i0 i0 i0 ≡ refl ∙ (refl ∙ (refl ∙ e04))
  flag-initial h t u = refl
  flag-terminal : (h : B.F.Horn) (t : B.F.T1234) (u : B.F.FourCell h t)
    → flag-sweep h t u i1 i1 i1 ≡ P.b4
  flag-terminal h t u = refl

  flag-boundary0234 : (h : B.F.Horn) (t : B.F.T1234) (u : B.F.FourCell h t) (j k : I)
    → flag-sweep h t u i0 j k
      ≡ refl ∙ ((λ l → e02 (j ∧ l))
        ∙ ((λ l → a023 j (k ∧ l)) ∙ B.F.Horn.t0234 h j k))
  flag-boundary0234 h t u j k = refl
  flag-boundary1234 : (h : B.F.Horn) (t : B.F.T1234) (u : B.F.FourCell h t) (j k : I)
    → flag-sweep h t u i1 j k
      ≡ e01 ∙ ((λ l → e12 (j ∧ l)) ∙ ((λ l → a123 j (k ∧ l)) ∙ t j k))
  flag-boundary1234 h t u j k = refl
  flag-boundary0134 : (h : B.F.Horn) (t : B.F.T1234) (u : B.F.FourCell h t) (i k : I)
    → flag-sweep h t u i i0 k
      ≡ (λ l → e01 (i ∧ l))
        ∙ (refl ∙ ((λ l → a013 i (k ∧ l)) ∙ B.F.Horn.t0134 h i k))
  flag-boundary0134 h t u i k = refl
  flag-boundary0124 : (h : B.F.Horn) (t : B.F.T1234) (u : B.F.FourCell h t) (i j : I)
    → flag-sweep h t u i j i0
      ≡ (λ l → e01 (i ∧ l))
        ∙ ((λ l → a012 i (j ∧ l)) ∙ (refl ∙ B.F.Horn.t0124 h i j))
  flag-boundary0124 h t u i j = refl
  flag-boundary0123 : (h : B.F.Horn) (t : B.F.T1234) (u : B.F.FourCell h t) (i j : I)
    → flag-sweep h t u i j i1
      ≡ (λ l → e01 (i ∧ l))
        ∙ ((λ l → a012 i (j ∧ l)) ∙ (B.F.Horn.t0123 h i j ∙ e34))
  flag-boundary0123 h t u i j = refl
  flag-collapsed234 : (h : B.F.Horn) (t : B.F.T1234) (u : B.F.FourCell h t) (i k : I)
    → flag-sweep h t u i i1 k
      ≡ (λ l → e01 (i ∧ l)) ∙ (a012 i ∙ ((λ l → e23 (k ∧ l)) ∙ a234 k))
  flag-collapsed234 h t u i k = refl

  from-generated-coherence : GeneratedRouteCoherence → CenterCoherence
  from-generated-coherence n h = subst
    (λ k → induced-center k ≡ pentagon-center k)
    (B.equation-horn-recovered h)
    (induced-center-on-image (B.from-equation-horn h)
      ∙ equivFun (P.solve1234 (pentagon-horn (B.to-equation-horn (B.from-equation-horn h)))
          (translated-center (B.from-equation-horn h))) (n (B.from-equation-horn h)))

  to-generated-coherence : CenterCoherence → GeneratedRouteCoherence
  to-generated-coherence n h = invEq
    (P.solve1234 (pentagon-horn (B.to-equation-horn h)) (translated-center h))
    (sym (induced-center-on-image h) ∙ n (B.to-equation-horn h))

  -- The dependent contraction retains both the fifth tetrahedron and its
  -- Cubical filler. Thus a proof at the canonical pair extends to every
  -- actual filled pair without assuming that fifth tetrahedra are equal.
  extend-generated-coherence : GeneratedRouteCoherence
    → (h : B.F.Horn) (t : B.F.T1234) → B.F.FourCell h t
    → PentagonFourCell (B.to-equation-horn h) (equivFun B.e1234 t)
  extend-generated-coherence n h t u = subst
    (λ pair → PentagonFourCell (B.to-equation-horn h) (equivFun B.e1234 (fst pair)))
    (snd (B.F.unique h) (t , u)) (n h)

  goal-from-generated-coherence : GeneratedRouteCoherence → Goal
  goal-from-generated-coherence n = from-center-coherence (from-generated-coherence n)

  cubical-to-pentagon : CenterCoherence → (h : B.F.Horn) (t : B.F.T1234)
    → B.F.FourCell h t ≃ PentagonFourCell (B.to-equation-horn h) (equivFun B.e1234 t)
  cubical-to-pentagon n h t = compEquiv (B.old-fourcell-equivalence h t)
    (from-center-coherence n (B.to-equation-horn h) (equivFun B.e1234 t))

module TypedFixture where
  module F = Cube.TypedFixture
  module B = Bridge (Retained.TypedValue ℓ-zero) F.v F.e F.faces
  h : B.B.EquationHorn
  h = B.B.to-equation-horn F.horn
  independently-completed : B.P.Missing (B.pentagon-horn h)
  independently-completed = B.P.complete (B.pentagon-horn h)
  recovered : independently-completed ≡ fst (B.P.unique1234 (B.pentagon-horn h))
  recovered = isContr→isProp (B.P.unique1234 (B.pentagon-horn h)) _ _
  translated-center-normalization : B.induced-center h ≡ B.translated-center F.horn
  translated-center-normalization = B.induced-center-on-image F.horn
  chosen-tetrahedron-sweep : B.translated-center F.horn ≡ B.sweep-center F.horn
  chosen-tetrahedron-sweep = B.center-sweep-computation F.horn
  explicit-cube : I → I → I → F.a ≡ F.b
  explicit-cube = B.flag-sweep F.horn (fst F.explicit) (snd F.explicit)
  explicit-terminal : explicit-cube i1 i1 i1 ≡ B.P.b4
  explicit-terminal = B.flag-terminal F.horn (fst F.explicit) (snd F.explicit)
  -- This identifies the induced and translated Cubical centers only. No
  -- equality with the independent B.pentagon-center h is asserted here.
