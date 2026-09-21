{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureNativeDecompositionCalculus where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import ClosureNativeSubtreeContextAdmission using (module Native)
open import ClosureCoherentComposition using (module Composition)
open import ClosureTreeBoundarySemantics using (module Semantics)

module Calculus (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  private
    module NativeModel = Native K Piece Boundary attachL attachR using (module C; module Trees)
    module Compose = Composition K Piece Boundary attachL attachR
  module C = NativeModel.C
  module O = Semantics K Piece Boundary attachL attachR
  open C.C.A.N

  -- A directed, unquotiented syntax. A rotation is contextualized by syntax
  -- constructors, not by replacing its map with a canonical comparison.
  data Move : {a b : K} {w : Word a b} → Bracket w → Bracket w → Type where
    rotate : {a b c d e f : K} {u : Word a b} {v : Word c d} {w : Word e f}
      (p : Bracket u) (q : Bracket v) (r : Bracket w) →
      Move (NativeModel.Trees.R.leftTree p q r) (NativeModel.Trees.R.rightTree p q r)
    onLeft : {a b c d : K} {u : Word a b} {v : Word c d} {p p′ : Bracket u} →
      Move p p′ → (q : Bracket v) → Move (fork p q) (fork p′ q)
    onRight : {a b c d : K} {u : Word a b} {v : Word c d} (p : Bracket u) {q q′ : Bracket v} →
      Move q q′ → Move (fork p q) (fork p q′)

  evaluateMove : {a b : K} {w : Word a b} {p q : Bracket w} → Move p q → C.Coherent p q
  evaluateMove (rotate p q r) = NativeModel.Trees.coherent p q r
  evaluateMove (onLeft m q) = C.forkCoherent (evaluateMove m) (C.identity q)
  evaluateMove (onRight p m) = C.forkCoherent (C.identity p) (evaluateMove m)

  data Route {a b : K} {w : Word a b} : Bracket w → Bracket w → Type where
    done : (p : Bracket w) → Route p p
    step : {p q r : Bracket w} → Move q r → Route p q → Route p r

  append : {a b : K} {w : Word a b} {p q r : Bracket w} → Route p q → Route q r → Route p r
  append route (done q) = route
  append route (step m rest) = step m (append route rest)

  leftUnit : {a b : K} {w : Word a b} {p q : Bracket w} (route : Route p q) →
    append (done p) route ≡ route
  leftUnit (done p) = refl
  leftUnit (step m rest) = cong (step m) (leftUnit rest)
  rightUnit : {a b : K} {w : Word a b} {p q : Bracket w} (route : Route p q) →
    append route (done q) ≡ route
  rightUnit route = refl
  associative : {a b : K} {w : Word a b} {p q r s : Bracket w}
    (x : Route p q) (y : Route q r) (z : Route r s) →
    append (append x y) z ≡ append x (append y z)
  associative x y (done r) = refl
  associative x y (step m z) = cong (step m) (associative x y z)

  evaluate : {a b : K} {w : Word a b} {p q : Bracket w} → Route p q → C.Coherent p q
  evaluate (done p) = C.identity p
  evaluate (step m rest) = Compose.Compose.coherent (evaluate rest) (evaluateMove m)

  run : {a b : K} {w : Word a b} {p q : Bracket w} → Route p q → Realize p → Realize q
  run route = equivFun (C.C.frame (C.Coherent.base (evaluate route)))
  run-append : {a b : K} {w : Word a b} {p q r : Bracket w}
    (x : Route p q) (y : Route q r) (z : Realize p) →
    run (append x y) z ≡ run y (run x z)
  run-append x (done q) z = refl
  run-append x (step m y) z = cong (equivFun (C.C.frame (C.Coherent.base (evaluateMove m))))
    (run-append x y z)

  observe : {a b : K} {w : Word a b} {p q : Bracket w} {X : Type} →
    Route p q → O.Local q X → O.Local p X
  observe {p = p} {q} route = O.pull p q (run route)
  observe-identity : {a b : K} {w : Word a b} (p : Bracket w) {X : Type} (d : O.Local p X) →
    observe (done p) d ≡ d
  observe-identity = O.pull-identity
  observe-compose : {a b : K} {w : Word a b} {p q r : Bracket w} {X : Type}
    (x : Route p q) (y : Route q r) (d : O.Local r X) →
    observe x (observe y d) ≡ observe (append x y) d
  observe-compose {p = p} {q} {r} x y d = O.pull-compose p q r (run x) (run y) d
    ∙ cong (λ F → O.pull p r F d) (sym (funExt (run-append x y)))

  observe-first : {a b : K} {w : Word a b} {p q : Bracket w} {X : Type}
    (route : Route p q) (d : O.Local q X) (x : Piece a) →
    O.assemble p (observe route d) (firstAt p x) ≡ O.assemble q d (firstAt q x)
  observe-first {p = p} {q} route d x =
    cong (λ F → F (firstAt p x)) (O.pull-realizes p q (run route) d)
    ∙ cong (O.assemble q d) (C.Coherent.firstPort (evaluate route) x)
  observe-last : {a b : K} {w : Word a b} {p q : Bracket w} {X : Type}
    (route : Route p q) (d : O.Local q X) (x : Piece b) →
    O.assemble p (observe route d) (lastAt p x) ≡ O.assemble q d (lastAt q x)
  observe-last {p = p} {q} route d x =
    cong (λ F → F (lastAt p x)) (O.pull-realizes p q (run route) d)
    ∙ cong (O.assemble q d) (C.Coherent.lastPort (evaluate route) x)

  fromNormal : {a b : K} {w : Word a b} (p : Bracket w) {X : Type} →
    (Normal w → X) → O.Local p X
  fromNormal p h = O.restrict p (λ x → h (equivFun (normalize p) x))
  normal-naturality : {a b : K} {w : Word a b} {p q : Bracket w} {X : Type}
    (route : Route p q) (h : Normal w → X) → observe route (fromNormal q h) ≡ fromNormal p h
  normal-naturality {p = p} {q} route h = cong (O.restrict p)
    (cong (λ F x → F (run route x)) (O.assemble-restrict q _)
      ∙ (λ i x → h (equivFun (C.C.normalization (C.Coherent.base (evaluate route)) i) x)))

  admit : {a b : K} {w : Word a b} {p q : Bracket w} → Route p q → C.C.A.Edges.Admitted w p q
  admit route = C.C.A.Edges.admitted (run route)
    (λ x i → equivFun (C.C.normalization (C.Coherent.base (evaluate route)) i) x)

  module InHole {a b : K} (w : Word a b) where
    module H = C.InHole w

    liftMove : {c d : K} {v : Word c d} (context : H.Context v) {p q : Bracket w} →
      Move p q → Move (H.plug context p) (H.plug context q)
    liftMove H.hole m = m
    liftMove (H.left context sibling) m = onLeft (liftMove context m) sibling
    liftMove (H.right sibling context) m = onRight sibling (liftMove context m)

    liftMove-correct : {c d : K} {v : Word c d} (context : H.Context v) {p q : Bracket w}
      (m : Move p q) → evaluateMove (liftMove context m) ≡ H.lift context (evaluateMove m)
    liftMove-correct H.hole m = refl
    liftMove-correct (H.left context sibling) m =
      cong (λ e → C.forkCoherent e (C.identity sibling)) (liftMove-correct context m)
    liftMove-correct (H.right sibling context) m =
      cong (λ e → C.forkCoherent (C.identity sibling) e) (liftMove-correct context m)

    liftRoute : {c d : K} {v : Word c d} (context : H.Context v) {p q : Bracket w} →
      Route p q → Route (H.plug context p) (H.plug context q)
    liftRoute context (done p) = done (H.plug context p)
    liftRoute context (step m rest) = step (liftMove context m) (liftRoute context rest)

    liftRoute-append : {c d : K} {v : Word c d} (context : H.Context v) {p q r : Bracket w}
      (x : Route p q) (y : Route q r) →
      liftRoute context (append x y) ≡ append (liftRoute context x) (liftRoute context y)
    liftRoute-append context x (done q) = refl
    liftRoute-append context x (step m y) =
      cong (step (liftMove context m)) (liftRoute-append context x y)

-- Evaluation retains both higher endpoint cells on COMPLETE routes.
-- The source is not quotiented by pentagons. Specified higher generators,
-- their relations, and inverse/empty-object syntax are future extensions.
