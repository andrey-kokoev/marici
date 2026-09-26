{-# OPTIONS --safe --cubical --guardedness #-}
module TypedPhysicalComparisons where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Int.Base using (ℤ; pos; _-_)
open import Cubical.Data.Int.Properties using (posNotnegsuc)
open import Cubical.Data.Empty.Base using (⊥)
import ObservationRespectingBoundary as Q
import ActionChartComparison as C

module Over (V : Type) where
  record Object : Type₁ where
    constructor object
    field
      Carrier : Type
      point : Carrier
      readout : Carrier → V
  open Object
  record Map (X Y : Object) : Type where
    constructor map
    field
      run : Carrier X → Carrier Y
      marked : run (point X) ≡ point Y
      commutes : (x : Carrier X) → readout Y (run x) ≡ readout X x
  open Map
  Agreement : Object → Object → Type
  Agreement X Y = readout X (point X) ≡ readout Y (point Y)
  agreement : {X Y : Object} → Map X Y → Agreement X Y
  agreement {X} {Y} f = sym (commutes f (point X)) ∙ cong (readout Y) (marked f)
  identity : (X : Object) → Map X X
  identity X = map (λ x → x) refl (λ x → refl)
  compose : {X Y Z : Object} → Map X Y → Map Y Z → Map X Z
  compose f g = map (λ x → run g (run f x))
    (cong (run g) (marked f) ∙ marked g)
    (λ x → commutes g (run f x) ∙ commutes f x)
  record Presentation (X Y : Object) : Type where
    constructor presentation
    field
      forward : Map X Y
      invertible : isEquiv (run forward)
  record Restriction (X Y : Object) : Type where
    constructor restriction
    field
      forward : Map X Y
      retract : Carrier Y → Carrier X
      left-inverse : (x : Carrier X) → retract (run forward x) ≡ x
  -- Split injections are sufficient for this concrete restriction test.
  -- General embeddings need not admit a supplied retraction.
  restriction-compose : {X Y Z : Object} → Restriction X Y → Restriction Y Z → Restriction X Z
  restriction-compose f g = restriction
    (compose (Restriction.forward f) (Restriction.forward g))
    (λ z → Restriction.retract f (Restriction.retract g z))
    (λ x → cong (Restriction.retract f) (Restriction.left-inverse g
      (run (Restriction.forward f) x)) ∙ Restriction.left-inverse f x)
  presentation-identity : (X : Object) → Presentation X X
  presentation-identity X = presentation (identity X) (snd (idEquiv (Carrier X)))
  as-restriction : {X Y : Object} → Presentation X Y → Restriction X Y
  as-restriction (presentation f e) = restriction f
    (invEq (run f , e)) (retEq (run f , e))
  presentation-inverse : {X Y : Object} → Presentation X Y → Presentation Y X
  presentation-inverse {X} {Y} (presentation f e) = presentation
    (map (invEq (run f , e))
      (cong (invEq (run f , e)) (sym (marked f)) ∙ retEq (run f , e) (point X))
      (λ y → sym (commutes f (invEq (run f , e) y))
        ∙ cong (readout Y) (secEq (run f , e) y)))
    (snd (invEquiv (run f , e)))
  presentation-compose : {X Y Z : Object} → Presentation X Y → Presentation Y Z → Presentation X Z
  presentation-compose (presentation f e) (presentation g d) =
    presentation (compose f g) (snd (compEquiv (run f , e) (run g , d)))

module Coarsen {V W : Type} (q : V → W) where
  module A = Over V
  module B = Over W
  object : A.Object → B.Object
  object X = B.object (A.Object.Carrier X) (A.Object.point X) (λ x → q (A.Object.readout X x))
  map : {X Y : A.Object} → A.Map X Y → B.Map (object X) (object Y)
  map f = B.map (A.Map.run f) (A.Map.marked f) (λ x → cong q (A.Map.commutes f x))
  agreement : {X Y : A.Object} → A.Agreement X Y → B.Agreement (object X) (object Y)
  agreement p = cong q p
  presentation : {X Y : A.Object} → A.Presentation X Y → B.Presentation (object X) (object Y)
  presentation f = B.presentation (map (A.Presentation.forward f)) (A.Presentation.invertible f)
  restriction : {X Y : A.Object} → A.Restriction X Y → B.Restriction (object X) (object Y)
  restriction f = B.restriction (map (A.Restriction.forward f))
    (A.Restriction.retract f) (A.Restriction.left-inverse f)

-- Adapter to the actual retained-package boundary interface.
module Boundary {V : Type} where
  module A = Over V
  object : (p : Q.O.Complete) → (Q.Ty p → V) → A.Object
  object p r = A.object (Q.Ty p) (Q.O.value p) r
  from-observed : {p q : Q.O.Complete} {r : Q.Ty p → V} {s : Q.Ty q → V}
    → Q.Observed p q r s → A.Presentation (object p r) (object q s)
  from-observed ((e , p) , h) = A.presentation (A.map (equivFun e) p h) (snd e)
  -- The abstract object forgets provenance. Keep the owner's actual retained
  -- package alongside it; do not substitute the abstraction for source history.
  retain : {p q : Q.O.Complete} {r : Q.Ty p → V} {s : Q.Ty q → V}
    → Q.Observed p q r s → Q.O.Complete
  retain {p} {q} {r} {s} f = Q.retained-certificate {a = p} {b = q} {r} {s} f
  recovered : {p q : Q.O.Complete} {r : Q.Ty p → V} {s : Q.Ty q → V}
    (f : Q.Observed p q r s) → Q.O.value (retain {p} {q} {r} {s} f) ≡ f
  recovered f = refl
module Jet = Over (ℤ × ℤ)
chart-presentation : (c : C.Chart) → Jet.Presentation
  (Boundary.object (C.package C.angle) C.observe) (Boundary.object (C.package c) C.observe)
chart-presentation c = Boundary.from-observed {p = C.package C.angle} {q = C.package c}
  {r = C.observe} {s = C.observe} (C.comparison c)

-- Exact integer tangent-coordinate model of the scalar-plane inclusion.
-- Analytic target geometry and mixed scattering remain in the checked physical
-- packet; this is NOT a formal real-field or continuum theorem.
module Plane where
  module A = Over ℤ
  Full = ℤ × (ℤ × ℤ)
  small = A.object ℤ (pos 0) (λ x → x)
  full = A.object Full (pos 0 , pos 0 , pos 0) fst
  inclusion : A.Map small full
  inclusion = A.map (λ x → x , pos 0 , pos 0) refl (λ x → refl)
  restriction : A.Restriction small full
  restriction = A.restriction inclusion fst (λ x → refl)
  zero-not-one : pos 0 ≡ pos 1 → ⊥
  zero-not-one p = posNotnegsuc 0 0 (sym (cong (λ z → z - pos 1) p))
  no-right-inverse : (r : Full → ℤ)
    → ((y : Full) → A.Map.run inclusion (r y) ≡ y) → ⊥
  no-right-inverse r h = zero-not-one (cong (λ y → fst (snd y)) (h (pos 0 , pos 1 , pos 0)))
  no-presentation-of-inclusion : isEquiv (A.Map.run inclusion) → ⊥
  no-presentation-of-inclusion e = no-right-inverse
    (invEq (A.Map.run inclusion , e)) (secEq (A.Map.run inclusion , e))
  -- Stronger: no alternative equivalence can preserve this fixed scalar
  -- readout either. Extra target states lie in the same observation fiber.
  no-observed-presentation : A.Presentation small full → ⊥
  no-observed-presentation p = zero-not-one (cong (λ y → fst (snd y))
    (sym (A.Map.marked f) ∙ sym (cong (A.Map.run f) x-zero) ∙ secEq e y))
    where
    f = A.Presentation.forward p
    e = A.Map.run f , A.Presentation.invertible p
    y : Full
    y = pos 0 , pos 1 , pos 0
    x = invEq e y
    x-zero : x ≡ pos 0
    x-zero = sym (A.Map.commutes f x) ∙ cong fst (secEq e y)

-- Marked observation agreement need not furnish ANY commuting map.
module AgreementControl where
  module A = Over Bool
  X = A.object Bool false (λ b → b)
  Y = A.object Bool false (λ _ → false)
  agrees : A.Agreement X Y
  agrees = refl
  no-map : A.Map X Y → ⊥
  no-map f = false≢true (A.Map.commutes f true)

-- The logarithmic and quartic-truncated canonical profiles agree only after
-- forgetting the sixth derivative. Numbers are supplied by the prior checks.
module Refinement where
  Profile = (ℤ × ℤ) × ℤ
  log truncated : Profile
  log = (pos 2 , pos 16) , pos 512
  truncated = (pos 2 , pos 16) , pos 0
  coarse-agreement : fst log ≡ fst truncated
  coarse-agreement = refl
  no-fine-agreement : log ≡ truncated → ⊥
  no-fine-agreement p = posNotnegsuc 511 0 (cong (λ x → snd x - pos 1) p)
