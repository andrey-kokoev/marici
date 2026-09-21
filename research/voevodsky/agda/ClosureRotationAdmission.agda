{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureRotationAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua; uaIdEquiv; uaCompEquiv)
import Cubical.HITs.Pushout.Base as PO
open import Cubical.HITs.Pushout.Properties using (PushoutAlongEquiv)
open import ClosureFiniteGluingNormalization using (module System)
open import ClosureGluingReassociation using (module Chain)
open import ClosureReferenceNormalForm using (module Model)

module Admission (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module N = System K Piece Boundary attachL attachR
  open N

  module Edges {a b : K} (w : Word a b) where
    module Canonical = Comparisons w

    -- An arbitrary function does NOT receive admission automatically.
    record Admitted (p q : Bracket w) : Type where
      constructor admitted
      field
        action : Realize p → Realize q
        square : (x : Realize p) →
          equivFun (normalize q) (action x) ≡ equivFun (normalize p) x
    open Admitted public

    matchesNormalForm : {p q : Bracket w} (e : Admitted p q) (x : Realize p) →
      action e x ≡ Canonical.change p q x
    matchesNormalForm {q = q} e x = sym (retEq (normalize q) (action e x))
      ∙ cong (invEq (normalize q)) (square e x)

    actionEquiv : {p q : Bracket w} → Admitted p q → Realize p ≃ Realize q
    actionEquiv {p} {q} e = action e , subst isEquiv
      (sym (funExt (matchesNormalForm e)))
      (snd (compEquiv (normalize p) (invEquiv (normalize q))))

    module Presentations (p : Bracket w) where
      module Views = Model (Bracket w) (λ _ → Realize p) Realize (Realize p) (Normal w)
        (λ _ → idEquiv (Realize p)) normalize (equivFun (normalize p))

      pack : (q : Bracket w) → Admitted p q → Views.Cuts.Compatible q
      pack q e = action e , funExt (square e)

      agreesWithGenerated : (q : Bracket w) (e : Admitted p q) →
        pack q e ≡ Views.Cuts.canonical q
      agreesWithGenerated q e = Views.Cuts.compare q (pack q e) (Views.Cuts.canonical q)

    data Route : Bracket w → Bracket w → Type where
      stay : (p : Bracket w) → Route p p
      step : {p q r : Bracket w} → Admitted q r → Route p q → Route p r

    -- These composites retain the supplied edge maps, rather than replacing
    -- each edge by a canonical map before running the route.
    runEquiv : {p q : Bracket w} → Route p q → Realize p ≃ Realize q
    runEquiv (stay p) = idEquiv (Realize p)
    runEquiv (step e route) = compEquiv (runEquiv route) (actionEquiv e)

    run : {p q : Bracket w} → Route p q → Realize p → Realize q
    run route = equivFun (runEquiv route)

    routeSquare : {p q : Bracket w} (route : Route p q) (x : Realize p) →
      equivFun (normalize q) (run route x) ≡ equivFun (normalize p) x
    routeSquare (stay p) x = refl
    routeSquare (step e route) x = square e (run route x) ∙ routeSquare route x

    routeNormalForm : {p q : Bracket w} (route : Route p q) (x : Realize p) →
      run route x ≡ Canonical.change p q x
    routeNormalForm {p} {q} route = matchesNormalForm {p} {q}
      (admitted (run route) (routeSquare route))

    compareRoutes : {p q : Bracket w} (r s : Route p q) → run r ≡ run s
    compareRoutes r s = funExt (λ x → routeNormalForm r x ∙ sym (routeNormalForm s x))

    cycleReturns : {p : Bracket w} (r : Route p p) (x : Realize p) → run r x ≡ x
    cycleReturns {p} r x = routeNormalForm r x ∙ retEq (normalize p) x

    typeRoute : {p q : Bracket w} → Route p q → Realize p ≡ Realize q
    typeRoute (stay p) = refl
    typeRoute (step e r) = typeRoute r ∙ ua (actionEquiv e)

    typeRouteNormalForm : {p q : Bracket w} (r : Route p q) → ua (runEquiv r) ≡ typeRoute r
    typeRouteNormalForm (stay p) = uaIdEquiv
    typeRouteNormalForm (step e r) = uaCompEquiv (runEquiv r) (actionEquiv e)
      ∙ cong (λ t → t ∙ ua (actionEquiv e)) (typeRouteNormalForm r)

    closedTypeRoute : {p : Bracket w} (r : Route p p) → typeRoute r ≡ refl
    closedTypeRoute {p} r = sym (typeRouteNormalForm r)
      ∙ cong ua (equivEq {f = idEquiv (Realize p)} (funExt (cycleReturns r))) ∙ uaIdEquiv

    residualIsIdentity : {p : Bracket w} (r : Route p p) (x : Realize p) →
      transport (typeRoute r) x ≡ x
    residualIsIdentity r x = cong (λ t → transport t x) (closedTypeRoute r) ∙ transportRefl x

  -- First independently proved admission case. The two left attachment
  -- maps are equivalences. The remaining piece can have arbitrary topology.
  -- This is NOT the general noninvertible-attachment theorem.
  module ThreeLeaf (a b c : K)
    (firstIsEquiv : isEquiv (attachL {a} {b}))
    (secondIsEquiv : isEquiv (attachL {b} {c})) where

    word : Word a c
    word = cons a (cons b (single c))

    leftTree rightTree : Bracket word
    leftTree = fork (fork (leaf a) (leaf b)) (leaf c)
    rightTree = fork (leaf a) (fork (leaf b) (leaf c))

    module Raw = Chain (Piece a) (Piece b) (Piece c)
      (Boundary a b) (Boundary b c) attachL attachR attachL attachR
    module E = Edges word

    middleInclusion : Piece b ≃ Raw.AB
    middleInclusion = isoToEquiv (invIso (PushoutAlongEquiv
      (attachL , firstIsEquiv) attachR))

    outerAttachment : Boundary b c ≃ Raw.AB
    outerAttachment = compEquiv (attachL , secondIsEquiv) middleInclusion

    rightmostInclusion : Piece c ≃ Realize leftTree
    rightmostInclusion = isoToEquiv (invIso (PushoutAlongEquiv outerAttachment attachR))

    -- Both normalized maps compute identically on the last piece. Its
    -- inclusion is an equivalence, so this proves agreement everywhere.
    -- No compatibility square has been assumed for Raw.associate.
    rotationSquare : (x : Realize leftTree) →
      equivFun (normalize rightTree) (Raw.associate x) ≡ equivFun (normalize leftTree) x
    rotationSquare x =
      sym (cong (λ z → equivFun (normalize rightTree) (Raw.associate z))
        (secEq rightmostInclusion x))
      ∙ cong (equivFun (normalize leftTree)) (secEq rightmostInclusion x)

    forward : E.Admitted leftTree rightTree
    forward = E.admitted Raw.associate rotationSquare

    backward : E.Admitted rightTree leftTree
    backward = E.admitted Raw.unassociate (λ y →
      sym (rotationSquare (Raw.unassociate y))
      ∙ cong (equivFun (normalize rightTree)) (Raw.associateSection y))

    nativeMatchesGenerated : Raw.associate ≡ Comparisons.change word leftTree rightTree
    nativeMatchesGenerated = funExt (E.matchesNormalForm forward)

    nativeEquivalenceRetained : E.actionEquiv forward ≡ Raw.reassociation
    nativeEquivalenceRetained = equivEq refl

-- Larger subtree rotations require explicit word-index reassociation and
-- a proof of their normalization square. Noninvertible attachments are not
-- silently admitted by the ThreeLeaf result.
