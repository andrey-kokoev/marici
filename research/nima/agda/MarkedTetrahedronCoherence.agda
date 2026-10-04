{-# OPTIONS --safe --cubical --guardedness #-}
module MarkedTetrahedronCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (congEquiv; equivAdjointEquiv)
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Path using (compPathlEquiv; compPathrEquiv; symIso)
open import Cubical.Foundations.GroupoidLaws using (assoc; rCancel; rUnit)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Bool.Base using (Bool; false)
open import Cubical.Data.Empty.Base using (⊥)
open import GradedBoundaryCoherence using
  (module Tower; twisted-filler; marked-fillers-distinct)
open import RelativeCoherentCompletion using (module Completion)
open import MarkedTriangleCoherence using (module Triangles)

-- Fibers with their equality orientation reversed remain contractible.
reverse-fiber-contr : {ℓ ℓ' : Level} {X : Type ℓ} {Y : Type ℓ'}
  (e : X ≃ Y) (y : Y) → isContr (Σ[ x ∈ X ] (y ≡ equivFun e x))
reverse-fiber-contr e y =
  (fst (fst c) , sym (snd (fst c))) , λ { (x , p) i →
    fst (snd c (x , sym p) i) , sym (snd (snd c (x , sym p) i)) }
  where c = equiv-proof (snd e) y

module Tetrahedra {ℓ : Level} (A : Type ℓ) where
  module Tri = Triangles A
  module TriangleClosure = Completion Tri.Horn Tri.Completion Tri.complete-unique

  -- Factoring the shared constructor leaves the previous triangle operations
  -- and its retained recovery witness definitionally unchanged.
  triangle-completion-preserved : TriangleClosure.complete ≡ Tri.complete
  triangle-completion-preserved = refl

  triangle-recovery-preserved : TriangleClosure.forget ≡ Tri.forget
  triangle-recovery-preserved = refl

  triangle-witness-preserved : (t : Tri.Filled)
    → TriangleClosure.complete-forget t ≡ Tri.complete-forget t
  triangle-witness-preserved t = refl

  record Edges (x0 x1 x2 x3 : A) : Type ℓ where
    field
      e01 : x0 ≡ x1
      e12 : x1 ≡ x2
      e02 : x0 ≡ x2
      e23 : x2 ≡ x3
      e13 : x1 ≡ x3
      e03 : x0 ≡ x3

  module Over {x0 x1 x2 x3 : A} (edges : Edges x0 x1 x2 x3) where
    open Edges edges

    Face012 Face123 Face013 Face023 : Type ℓ
    Face012 = Tri.Triangle e01 e12 e02
    Face123 = Tri.Triangle e12 e23 e13
    Face013 = Tri.Triangle e01 e13 e03
    Face023 = Tri.Triangle e02 e23 e03

    start : x0 ≡ x3
    start = (e01 ∙ e12) ∙ e23

    Route : Type ℓ
    Route = start ≡ e03

    reassociate : start ≡ e01 ∙ (e12 ∙ e23)
    reassociate = sym (assoc e01 e12 e23)

    left-route : Face012 → Face023 → Route
    left-route a d = cong (λ p → p ∙ e23) a ∙ d

    right-route : Face123 → Face013 → Route
    right-route b c = reassociate ∙ (cong (λ p → e01 ∙ p) b ∙ c)

    Tetrahedron : Face012 → Face123 → Face013 → Face023 → Type ℓ
    Tetrahedron a b c d = left-route a d ≡ right-route b c

    -- Each choice of the missing face gives an equivalence to the SAME
    -- composite-route space. Whiskering and concatenation retain witnesses.
    route023 : Face012 → Face023 ≃ Route
    route023 a = compPathlEquiv (cong (λ p → p ∙ e23) a)

    route012 : Face023 → Face012 ≃ Route
    route012 d = compEquiv (congEquiv (compPathrEquiv e23)) (compPathrEquiv d)

    route013 : Face123 → Face013 ≃ Route
    route013 b = compEquiv (compPathlEquiv (cong (λ p → e01 ∙ p) b))
      (compPathlEquiv reassociate)

    route123 : Face013 → Face123 ≃ Route
    route123 c = compEquiv (congEquiv (compPathlEquiv e01))
      (compEquiv (compPathrEquiv c) (compPathlEquiv reassociate))

    Missing023 : Face012 → Face123 → Face013 → Type ℓ
    Missing023 a b c = Σ[ d ∈ Face023 ] Tetrahedron a b c d

    unique023 : (a : Face012) (b : Face123) (c : Face013) → isContr (Missing023 a b c)
    unique023 a b c = equiv-proof (snd (route023 a)) (right-route b c)

    Missing012 : Face123 → Face013 → Face023 → Type ℓ
    Missing012 b c d = Σ[ a ∈ Face012 ] Tetrahedron a b c d

    unique012 : (b : Face123) (c : Face013) (d : Face023) → isContr (Missing012 b c d)
    unique012 b c d = equiv-proof (snd (route012 d)) (right-route b c)

    Missing013 : Face012 → Face123 → Face023 → Type ℓ
    Missing013 a b d = Σ[ c ∈ Face013 ] Tetrahedron a b c d

    unique013 : (a : Face012) (b : Face123) (d : Face023) → isContr (Missing013 a b d)
    unique013 a b d = reverse-fiber-contr (route013 b) (left-route a d)

    Missing123 : Face012 → Face013 → Face023 → Type ℓ
    Missing123 a c d = Σ[ b ∈ Face123 ] Tetrahedron a b c d

    unique123 : (a : Face012) (c : Face013) (d : Face023) → isContr (Missing123 a c d)
    unique123 a c d = reverse-fiber-contr (route123 c) (left-route a d)

    -- Equivalent formulations of the same fully marked coherence question.
    solve023 : (a : Face012) (b : Face123) (c : Face013) (d : Face023)
      → Tetrahedron a b c d ≃ (d ≡ invEq (route023 a) (right-route b c))
    solve023 a b c d = invEquiv (equivAdjointEquiv (route023 a))

    solve012 : (a : Face012) (b : Face123) (c : Face013) (d : Face023)
      → Tetrahedron a b c d ≃ (a ≡ invEq (route012 d) (right-route b c))
    solve012 a b c d = invEquiv (equivAdjointEquiv (route012 d))

    solve013 : (a : Face012) (b : Face123) (c : Face013) (d : Face023)
      → Tetrahedron a b c d ≃ (c ≡ invEq (route013 b) (left-route a d))
    solve013 a b c d = compEquiv (isoToEquiv symIso)
      (invEquiv (equivAdjointEquiv (route013 b)))

    solve123 : (a : Face012) (b : Face123) (c : Face013) (d : Face023)
      → Tetrahedron a b c d ≃ (b ≡ invEq (route123 c) (left-route a d))
    solve123 a b c d = compEquiv (isoToEquiv symIso)
      (invEquiv (equivAdjointEquiv (route123 c)))

    -- A wrong fully marked face is an obstruction, not a missing-edge request.
    incompatible-face : (a : Face012) (b : Face123) (c : Face013) (d : Face023)
      → ((d ≡ invEq (route023 a) (right-route b c)) → ⊥)
      → Tetrahedron a b c d → ⊥
    incompatible-face a b c d neq t = neq (equivFun (solve023 a b c d) t)

    -- Reuse ONE relative universal-property construction for all four horns.
    Horn023 Horn012 Horn013 Horn123 : Type ℓ
    Horn023 = Face012 × Face123 × Face013
    Horn012 = Face123 × Face013 × Face023
    Horn013 = Face012 × Face123 × Face023
    Horn123 = Face012 × Face013 × Face023

    Completion023 : Horn023 → Type ℓ
    Completion023 (a , b , c) = Missing023 a b c
    Completion012 : Horn012 → Type ℓ
    Completion012 (b , c , d) = Missing012 b c d
    Completion013 : Horn013 → Type ℓ
    Completion013 (a , b , d) = Missing013 a b d
    Completion123 : Horn123 → Type ℓ
    Completion123 (a , c , d) = Missing123 a c d

    module Close023 = Completion Horn023 Completion023 (λ { (a , b , c) → unique023 a b c })
    module Close012 = Completion Horn012 Completion012 (λ { (b , c , d) → unique012 b c d })
    module Close013 = Completion Horn013 Completion013 (λ { (a , b , d) → unique013 a b d })
    module Close123 = Completion Horn123 Completion123 (λ { (a , c , d) → unique123 a c d })

    module G = Tower A
    globular-boundary : Face012 → Face123 → Face013 → Face023 → G.Boundary 3
    globular-boundary a b c d = ((lift tt , x0 , x3) , start , e03) , left-route a d , right-route b c

    globular-filler-equivalence : (a : Face012) (b : Face123) (c : Face013) (d : Face023)
      → Tetrahedron a b c d ≃ G.Fill 3 (globular-boundary a b c d)
    globular-filler-equivalence a b c d = idEquiv _

  MarkedTetrahedron : (x0 x1 x2 x3 : A) → Type ℓ
  MarkedTetrahedron x0 x1 x2 x3 = Σ[ e ∈ Edges x0 x1 x2 x3 ] Over.Close023.Total e

  first-edge : {x0 x1 x2 x3 : A} → MarkedTetrahedron x0 x1 x2 x3 → x0 ≡ x1
  first-edge t = Edges.e01 (fst t)

  diagonal : {x0 x1 x2 x3 : A} → MarkedTetrahedron x0 x1 x2 x3 → x0 ≡ x3
  diagonal t = Edges.e03 (fst t)

module Types = Tetrahedra (Type ℓ-zero)

ordinary-edges twisted-edges : Types.Edges Bool Bool Bool Bool
ordinary-edges = record { e01 = refl ; e12 = refl ; e02 = refl ; e23 = refl ; e13 = refl ; e03 = refl }
twisted-edges = record
  { e01 = twisted-filler ; e12 = sym twisted-filler ; e02 = refl
  ; e23 = refl ; e13 = sym twisted-filler ; e03 = refl }

module Ordinary = Types.Over ordinary-edges
module Twisted = Types.Over twisted-edges

ordinary-horn : Ordinary.Horn023
ordinary-horn = rCancel refl , sym (rUnit refl) , rCancel refl

twisted-horn : Twisted.Horn023
twisted-horn = rCancel twisted-filler , sym (rUnit (sym twisted-filler)) , rCancel twisted-filler

ordinary twisted : Types.MarkedTetrahedron Bool Bool Bool Bool
ordinary = ordinary-edges , Ordinary.Close023.complete ordinary-horn
twisted = twisted-edges , Twisted.Close023.complete twisted-horn

same-diagonal : Types.diagonal ordinary ≡ Types.diagonal twisted
same-diagonal = refl

different-tetrahedra : ordinary ≡ twisted → ⊥
different-tetrahedra p = marked-fillers-distinct (cong Types.first-edge p)

no-diagonal-recovery : (recover : (Bool ≡ Bool) → Types.MarkedTetrahedron Bool Bool Bool Bool)
  → ((t : Types.MarkedTetrahedron Bool Bool Bool Bool) → recover (Types.diagonal t) ≡ t) → ⊥
no-diagonal-recovery recover law = different-tetrahedra (sym (law ordinary) ∙ law twisted)
