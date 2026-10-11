{-# OPTIONS --safe --cubical --guardedness #-}
module TetrahedronPresentationBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_; equivFun; invEq; invEquiv; compEquiv; retEq; secEq)
open import Cubical.Foundations.Equiv.Properties using (congEquiv)
open import Cubical.Foundations.Isomorphism using (iso)
open import Cubical.Foundations.Path using (PathP≃Path; Square→compPath; compPathr-cancel; compPathl-cancel)
open import Cubical.Foundations.GroupoidLaws using (assoc; lUnit; rUnit; rCancel; cong-∙; symDistr)
open import Cubical.Foundations.Transport using (substInPathsR)
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Foundations.HLevels using (isOfHLevelRetractFromIso)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv)
import FourSimplexHorn as Cube
import MarkedTetrahedronCoherence as Marked
import RetainedTetrahedralPackage as Retained
open import PathUnitCoherence using (left-unit-assoc)
open import PathSweepCoherence using (mapped-pathover-pasting)

-- Begin with a reversible horn-relative comparison, then prove that its
-- derived fourth face agrees with the independent triangle comparison.
-- FixedBoundaryTarget.equivalence gives the resulting all-four-face bridge.
module Bridge {ℓ : Level} (A : Type ℓ) {x0 x1 x2 x3 : A}
  (e : Marked.Tetrahedra.Edges A x0 x1 x2 x3) where
  module C = Cube.Simplex A
  module CE = C.OnEdges e
  module O = Marked.Tetrahedra.Over A e
  open Marked.Tetrahedra.Edges e

  module Horn
    (a : C.Triangle e01 e12 e02)
    (b : C.Triangle e12 e23 e13)
    (c : C.Triangle e01 e13 e03) where
    a' = equivFun (C.triangle-comparison e01 e12 e02) a
    b' = equivFun (C.triangle-comparison e12 e23 e13) b
    c' = equivFun (C.triangle-comparison e01 e13 e03) c
    D = C.Triangle e02 e23 e03
    B = C.Triangle e12 e23 e13
    Family : I → Type ℓ
    Family i = C.Triangle (a i) e23 (c i)

    -- The transport in Family gives a genuine path of whole marked
    -- triangle packages, not just a path between witness terms. This is the
    -- higher-dimensional input for the route coherence below.
    transportedTrianglePackage : D → I → C.TrianglePackage
    transportedTrianglePackage d i = C.triangle-package
      (e01 i) x2 x3 (a i) e23 (c i)
      (transport-filler (λ j → Family j) d i)
    transported-package-start : (d : D)
      → transportedTrianglePackage d i0
        ≡ C.triangle-package x0 x2 x3 e02 e23 e03 d
    transported-package-start d = refl
    transported-package-end : (d : D)
      → transportedTrianglePackage d i1
        ≡ C.triangle-package x1 x2 x3 e12 e23 e13
            (transport (λ i → Family i) d)
    transported-package-end d = refl
    old-transported-package-line : (d : D)
      → I → C.R.FacePackage
    old-transported-package-line d i =
      C.face-to-previous (transportedTrianglePackage d i)

    CubicalFiller : D → Type ℓ
    CubicalFiller d = CE.Tetrahedron (CE.surface a b c d)
    OldFiller : O.Face023 → Type ℓ
    OldFiller = O.Tetrahedron a' b' c'

    -- Moving in the cubical family, translating the terminal face, then
    -- solving the old route equation gives an equivalence of fourth faces.
    terminal-face : B ≃ O.Face023
    terminal-face = compEquiv (C.triangle-comparison e12 e23 e13)
      (compEquiv (O.route123 c') (invEquiv (O.route023 a')))
    fourth-face : D ≃ O.Face023
    fourth-face = compEquiv (pathToEquiv (λ i → Family i)) terminal-face
    filler-equivalence : (d : D)
      → CubicalFiller d ≃ OldFiller (equivFun fourth-face d)
    filler-equivalence d = compEquiv (PathP≃Path Family d b)
      (compEquiv (congEquiv terminal-face)
        (invEquiv (O.solve023 a' b' c' (equivFun fourth-face d))))

    CubicalCompletion : Type ℓ
    CubicalCompletion = Σ[ d ∈ D ] CubicalFiller d
    OldCompletion : Type ℓ
    OldCompletion = O.Missing023 a' b' c'
    completion-equivalence : CubicalCompletion ≃ OldCompletion
    completion-equivalence = Σ-cong-equiv fourth-face filler-equivalence
    to-old : CubicalCompletion → OldCompletion
    to-old = equivFun completion-equivalence
    to-cubical : OldCompletion → CubicalCompletion
    to-cubical = invEq completion-equivalence
    cubical-recovered : (p : CubicalCompletion) → to-cubical (to-old p) ≡ p
    cubical-recovered = retEq completion-equivalence
    old-recovered : (p : OldCompletion) → to-old (to-cubical p) ≡ p
    old-recovered = secEq completion-equivalence

    ReverseCompletion : Type ℓ
    ReverseCompletion = Σ[ d ∈ D ] PathP (λ i → Family (~ i)) b d
    reverse-completion : CubicalCompletion → ReverseCompletion
    reverse-completion (d , t) = d , symP t
    forward-completion : ReverseCompletion → CubicalCompletion
    forward-completion (d , t) = d , symP t
    cubical-unique : isContr CubicalCompletion
    cubical-unique = isOfHLevelRetractFromIso 0
      (iso reverse-completion forward-completion (λ _ → refl) (λ _ → refl))
      (isContrSinglP (λ i → Family (~ i)) b)
    cubical-complete : CubicalCompletion
    cubical-complete = fst cubical-unique
    old-complete : OldCompletion
    old-complete = fst (O.unique023 a' b' c')
    -- Equality includes the computed face AND tetrahedral witness.
    complete-then-translate : to-old cubical-complete ≡ old-complete
    complete-then-translate = isContr→isProp (O.unique023 a' b' c') _ _
    translate-then-complete : to-cubical old-complete ≡ cubical-complete
    translate-then-complete = isContr→isProp cubical-unique _ _

    -- The condition retaining the independent face023 translation. Its
    -- inhabitant is constructed below, after the route-coherence proof.
    FaceNaturality : Type ℓ
    FaceNaturality = (d : D)
      → equivFun fourth-face d ≡ equivFun (C.triangle-comparison e02 e23 e03) d

    -- The moving first vertex is connected to x0 by the initial segment of
    -- e01. Composing this segment with the moving face edges gives the two
    -- boundary sweeps used to compare the endpoint route maps.
    initialSegment : PathP (λ i → x0 ≡ e01 i) refl e01
    initialSegment i j = e01 (i ∧ j)
    leftEdgeSweep : (refl ∙ e02) ≡ (e01 ∙ e12)
    leftEdgeSweep i = initialSegment i ∙ a i
    rightEdgeSweep : (refl ∙ e03) ≡ (e01 ∙ e13)
    rightEdgeSweep i = initialSegment i ∙ c i
    EquationFamily : I → Type ℓ
    EquationFamily i = a i ∙ e23 ≡ c i
    comparisonAt : (i : I) → Family i → EquationFamily i
    comparisonAt i = equivFun (C.triangle-comparison (a i) e23 (c i))

    -- Naturality of the fiberwise triangle comparison under transport. This
    -- is obtained by mapping the transport filler through the family of
    -- comparison equivalences and then using PathP≃Path.
    comparison-pathover : (d : D)
      → PathP (λ i → EquationFamily i) (comparisonAt i0 d)
          (comparisonAt i1 (transport (λ i → Family i) d))
    comparison-pathover d i =
      comparisonAt i (transport-filler (λ j → Family j) d i)

    comparison-transport : (d : D)
      → transport (λ i → EquationFamily i)
          (comparisonAt i0 d)
        ≡ comparisonAt i1 (transport (λ i → Family i) d)
    comparison-transport d = equivFun
      (PathP≃Path EquationFamily (comparisonAt i0 d)
        (comparisonAt i1 (transport (λ i → Family i) d)))
      (comparison-pathover d)

    -- Whisker the transported triangle equation by the moving initial segment,
    -- then normalize its two moving boundaries back to the fixed old route.
    leftSweep-tail : (i : I) → leftEdgeSweep i ≡ leftEdgeSweep i1
    leftSweep-tail i j = leftEdgeSweep (i ∨ j)
    rightSweep-tail : (i : I) → rightEdgeSweep i ≡ rightEdgeSweep i1
    rightSweep-tail i j = rightEdgeSweep (i ∨ j)
    leftRoute-normalize : (i : I)
      → O.start ≡ (initialSegment i ∙ (a i ∙ e23))
    leftRoute-normalize i =
      cong (λ p → p ∙ e23) (sym (leftSweep-tail i))
        ∙ sym (assoc (initialSegment i) (a i) e23)
    rightRoute-normalize : (i : I)
      → (initialSegment i ∙ c i) ≡ e03
    rightRoute-normalize i = rightSweep-tail i ∙ c'

    route-from-equation : (i : I) → EquationFamily i → O.Route
    route-from-equation i t = leftRoute-normalize i
      ∙ (cong (λ p → initialSegment i ∙ p) t ∙ rightRoute-normalize i)

    transported-route-line : (d : D)
      → route-from-equation i0 (comparisonAt i0 d)
          ≡ route-from-equation i1
              (comparisonAt i1 (transport (λ i → Family i) d))
    transported-route-line d i = route-from-equation i
      (comparison-pathover d i)

    -- At the terminal vertex both sweep tails are reflexive. Remove the
    -- resulting left units explicitly (lUnit is oriented toward insertion).
    leftRoute-normalize-end : leftRoute-normalize i1 ≡ O.reassociate
    leftRoute-normalize-end = sym (lUnit O.reassociate)

    rightRoute-normalize-end : rightRoute-normalize i1 ≡ c'
    rightRoute-normalize-end = sym (lUnit c')

    route-line-end : (t : EquationFamily i1)
      → route-from-equation i1 t ≡ equivFun (O.route123 c') t
    route-line-end t i = leftRoute-normalize-end i
      ∙ (cong (λ p → e01 ∙ p) t ∙ rightRoute-normalize-end i)

    -- Applying the old route equivalence reduces FaceNaturality to one
    -- coherence square in the common route type.
    RouteNaturality : Type ℓ
    RouteNaturality = (d : D)
      → equivFun (O.route123 c')
          (equivFun (C.triangle-comparison e12 e23 e13)
            (transport (λ i → Family i) d))
        ≡ equivFun (O.route023 a')
          (equivFun (C.triangle-comparison e02 e23 e03) d)

    RouteStartNaturality : Type ℓ
    RouteStartNaturality = (d : D)
      → route-from-equation i0 (comparisonAt i0 d)
        ≡ equivFun (O.route023 a') (comparisonAt i0 d)

    RouteEndNaturality : Type ℓ
    RouteEndNaturality = (d : D)
      → route-from-equation i1
          (comparisonAt i1 (transport (λ i → Family i) d))
        ≡ equivFun (O.route123 c')
          (comparisonAt i1 (transport (λ i → Family i) d))

    route-naturality-from-endpoints : RouteStartNaturality → RouteEndNaturality
      → RouteNaturality
    route-naturality-from-endpoints normalizeStart normalizeEnd d =
      sym (normalizeEnd d) ∙ sym (transported-route-line d) ∙ normalizeStart d

    route-naturality-from-start : RouteStartNaturality → RouteNaturality
    route-naturality-from-start n = route-naturality-from-endpoints n
      (λ d → route-line-end (comparisonAt i1 (transport (λ i → Family i) d)))

    -- The selected comparison now has a proved sweep formula. This closes
    -- the right initial boundary without any normalization assumption.
    rightRoute-normalize-start : rightRoute-normalize i0 ≡ sym (lUnit e03)
    rightRoute-normalize-start = C.triangle-sweep-cancel e01 e13 e03 c

    left-sweep-factor : sym leftEdgeSweep ≡ a' ∙ lUnit e02
    left-sweep-factor = sym
      (cong (_∙ lUnit e02) (C.triangle-comparison-sweep e01 e12 e02 a)
        ∙ compPathr-cancel (lUnit e02) (sym leftEdgeSweep))

    -- This equation involves only two paths and the library's chosen
    -- unit/associator fillers. PathUnitCoherence proves it independently.
    UnitAssociativity : Type ℓ
    UnitAssociativity =
      cong (_∙ e23) (lUnit e02) ∙ sym (assoc refl e02 e23)
        ≡ lUnit (e02 ∙ e23)

    leftRoute-normalize-start : UnitAssociativity
      → leftRoute-normalize i0 ≡ cong (_∙ e23) a' ∙ lUnit (e02 ∙ e23)
    leftRoute-normalize-start u =
      cong (λ s → cong (_∙ e23) s ∙ sym (assoc refl e02 e23)) left-sweep-factor
      ∙ cong (_∙ sym (assoc refl e02 e23)) (cong-∙ (_∙ e23) a' (lUnit e02))
      ∙ sym (assoc (cong (_∙ e23) a') (cong (_∙ e23) (lUnit e02))
          (sym (assoc refl e02 e23)))
      ∙ cong (cong (_∙ e23) a' ∙_) u

    unit-whisker-normalize : (t : EquationFamily i0)
      → lUnit (e02 ∙ e23) ∙ (cong (refl ∙_) t ∙ sym (lUnit e03)) ≡ t
    unit-whisker-normalize t =
      assoc (lUnit (e02 ∙ e23)) (cong (refl ∙_) t) (sym (lUnit e03))
      ∙ cong (_∙ sym (lUnit e03))
          (Square→compPath (λ i j → lUnit (t j) i))
      ∙ sym (assoc t (lUnit e03) (sym (lUnit e03)))
      ∙ cong (t ∙_) (rCancel (lUnit e03))
      ∙ sym (rUnit t)

    route-start-from-unit-associativity : UnitAssociativity → RouteStartNaturality
    route-start-from-unit-associativity u d =
      (λ i → leftRoute-normalize-start u i
        ∙ (cong (refl ∙_) t ∙ rightRoute-normalize-start i))
      ∙ sym (assoc (cong (_∙ e23) a') (lUnit (e02 ∙ e23))
          (cong (refl ∙_) t ∙ sym (lUnit e03)))
      ∙ cong (cong (_∙ e23) a' ∙_) (unit-whisker-normalize t)
      where
        t = comparisonAt i0 d

    route-derived : (d : D)
      → equivFun (O.route023 a') (equivFun fourth-face d)
        ≡ equivFun (O.route123 c')
          (equivFun (C.triangle-comparison e12 e23 e13)
            (transport (λ i → Family i) d))
    route-derived d = secEq (O.route023 a')
      (equivFun (O.route123 c')
        (equivFun (C.triangle-comparison e12 e23 e13)
          (transport (λ i → Family i) d)))

    to-route-naturality : FaceNaturality → RouteNaturality
    to-route-naturality n d = sym (route-derived d)
      ∙ cong (equivFun (O.route023 a')) (n d)

    from-route-naturality : RouteNaturality → FaceNaturality
    from-route-naturality n d = equivFun
      (invEquiv (congEquiv (O.route023 a')))
      (route-derived d ∙ n d)

    face-naturality-from-start : RouteStartNaturality → FaceNaturality
    face-naturality-from-start n = from-route-naturality (route-naturality-from-start n)

    face-naturality-from-unit-associativity : UnitAssociativity → FaceNaturality
    face-naturality-from-unit-associativity u =
      face-naturality-from-start (route-start-from-unit-associativity u)

    unit-associativity : UnitAssociativity
    unit-associativity = left-unit-assoc e02 e23

    route-naturality : RouteNaturality
    route-naturality = route-naturality-from-start
      (route-start-from-unit-associativity unit-associativity)

    face-naturality : FaceNaturality
    face-naturality = from-route-naturality route-naturality

    fixed-face-equivalence : FaceNaturality → (d : D)
      → CubicalFiller d ≃ OldFiller (equivFun (C.triangle-comparison e02 e23 e03) d)
    fixed-face-equivalence natural d = compEquiv (filler-equivalence d)
      (pathToEquiv (cong OldFiller (natural d)))

    -- Computation of the selected filler map in the common old route type.
    -- This exposes its action to higher-dimensional clients without changing
    -- the equivalence or unfolding its inverse-equivalence implementation.
    terminal-route : B → O.Route
    terminal-route t = equivFun (O.route123 c') (comparisonAt i1 t)

    route-path : (d : D) (t : CubicalFiller d)
      → terminal-route (transport (λ i → Family i) d) ≡ terminal-route b
    route-path d t = cong terminal-route (equivFun (PathP≃Path Family d b) t)

    normalized-route-map : (d : D) → CubicalFiller d → OldFiller (comparisonAt i0 d)
    normalized-route-map d t = sym (route-naturality d) ∙ route-path d t

    raw-route-computation : (d : D) (t : CubicalFiller d)
      → equivFun (filler-equivalence d) t ≡ route-derived d ∙ route-path d t
    raw-route-computation d t = sym (Square→compPath
      (λ i j → secEq (O.route023 a')
        (terminal-route (equivFun (PathP≃Path Family d b) t j)) i))

    face-naturality-route-lift : (d : D)
      → cong (equivFun (O.route023 a')) (face-naturality d)
        ≡ route-derived d ∙ route-naturality d
    face-naturality-route-lift d = secEq (congEquiv (O.route023 a'))
      (route-derived d ∙ route-naturality d)

    fixed-face-route-computation : (d : D) (t : CubicalFiller d)
      → equivFun (fixed-face-equivalence face-naturality d) t ≡ normalized-route-map d t
    fixed-face-route-computation d t =
      substInPathsR (cong (equivFun (O.route023 a')) (face-naturality d))
        (equivFun (filler-equivalence d) t)
      ∙ (λ i → sym (face-naturality-route-lift d i) ∙ raw-route-computation d t i)
      ∙ cong (_∙ (route-derived d ∙ route-path d t))
          (symDistr (route-derived d) (route-naturality d))
      ∙ sym (assoc (sym (route-naturality d)) (sym (route-derived d))
          (route-derived d ∙ route-path d t))
      ∙ cong (sym (route-naturality d) ∙_)
          (compPathl-cancel (sym (route-derived d)) (route-path d t))

    route-sweep : (d : D) (t : CubicalFiller d)
      → route-from-equation i0 (comparisonAt i0 d)
        ≡ route-from-equation i1 (comparisonAt i1 b)
    route-sweep d t i = route-from-equation i (comparisonAt i (t i))

    sweep-map : (d : D) → CubicalFiller d → OldFiller (comparisonAt i0 d)
    sweep-map d t = sym (route-start-from-unit-associativity unit-associativity d)
      ∙ (route-sweep d t ∙ route-line-end b')

    -- Remove transport and its residual endpoint path from the computation
    -- formula. The chosen tetrahedron map is the corrected direct sweep of
    -- its input filler, not merely some equivalence of the same types.
    route-sweep-computation : (d : D) (t : CubicalFiller d)
      → normalized-route-map d t ≡ sweep-map d t
    route-sweep-computation d t =
      cong (_∙ s)
        (symDistr (sym end0) (sym u ∙ start)
          ∙ cong (_∙ end0) (symDistr (sym u) start)
          ∙ sym (assoc (sym start) u end0))
      ∙ sym (assoc (sym start) (u ∙ end0) s)
      ∙ cong (sym start ∙_) (sym (assoc u end0 s))
      ∙ cong (λ k → sym start ∙ (u ∙ k)) end-naturality
      ∙ cong (sym start ∙_) (assoc u w end1)
      ∙ cong (λ k → sym start ∙ (k ∙ end1)) sweep-pasting
      where
        q = equivFun (PathP≃Path Family d b) t
        s = route-path d t
        u = transported-route-line d
        start = route-start-from-unit-associativity unit-associativity d
        end0 = route-line-end (comparisonAt i1 (transport (λ i → Family i) d))
        end1 = route-line-end b'
        w = cong (λ z → route-from-equation i1 (comparisonAt i1 z)) q
        end-naturality : end0 ∙ s ≡ w ∙ end1
        end-naturality = Square→compPath
          (λ i j → route-line-end (comparisonAt i1 (q j)) i)
        sweep-pasting : u ∙ w ≡ route-sweep d t
        sweep-pasting = mapped-pathover-pasting Family O.Route
          (λ i z → route-from-equation i (comparisonAt i z)) t

    fixed-face-sweep-computation : (d : D) (t : CubicalFiller d)
      → equivFun (fixed-face-equivalence face-naturality d) t ≡ sweep-map d t
    fixed-face-sweep-computation d t =
      fixed-face-route-computation d t ∙ route-sweep-computation d t

-- The fully marked, independent-face target is named separately from the
-- intermediate horn-relative result and is now inhabited by equivalence.
module FixedBoundaryTarget {ℓ : Level} (A : Type ℓ) {x0 x1 x2 x3 : A}
  (e : Marked.Tetrahedra.Edges A x0 x1 x2 x3) where
  module C = Cube.Simplex A
  module CE = C.OnEdges e
  module O = Marked.Tetrahedra.Over A e
  open Marked.Tetrahedra.Edges e
  old-filler : CE.Surface → Type ℓ
  old-filler s = O.Tetrahedron
    (equivFun (C.triangle-comparison e01 e12 e02) (CE.Surface.a012 s))
    (equivFun (C.triangle-comparison e12 e23 e13) (CE.Surface.a123 s))
    (equivFun (C.triangle-comparison e01 e13 e03) (CE.Surface.a013 s))
    (equivFun (C.triangle-comparison e02 e23 e03) (CE.Surface.a023 s))
  Goal : Type ℓ
  Goal = (s : CE.Surface) → CE.Tetrahedron s ≃ old-filler s

  from-naturality :
    ((a : C.Triangle e01 e12 e02) (b : C.Triangle e12 e23 e13)
      (c : C.Triangle e01 e13 e03) → Bridge.Horn.FaceNaturality A e a b c)
    → Goal
  from-naturality n (CE.surface a b c d) = Bridge.Horn.fixed-face-equivalence A e a b c (n a b c) d

  -- Factor the target through the concrete library unit/associator law.
  from-unit-associativity :
    (cong (_∙ e23) (lUnit e02) ∙ sym (assoc refl e02 e23) ≡ lUnit (e02 ∙ e23))
    → Goal
  from-unit-associativity u = from-naturality
    (λ a b c → Bridge.Horn.face-naturality-from-unit-associativity A e a b c u)

  route-expression : (s : CE.Surface) → CE.Tetrahedron s → old-filler s
  route-expression (CE.surface a b c d) = Bridge.Horn.normalized-route-map A e a b c d

  sweep-expression : (s : CE.Surface) → CE.Tetrahedron s → old-filler s
  sweep-expression (CE.surface a b c d) = Bridge.Horn.sweep-map A e a b c d

  -- Keep the coherence implementation opaque to higher-dimensional clients.
  -- They use its equivalence laws and boundary-indexed type, not reduction of
  -- the entire route proof at every slice of a four-cell.
  abstract
    equivalence : Goal
    equivalence = from-naturality (λ a b c → Bridge.Horn.face-naturality A e a b c)

    equivalence-route-computation : (s : CE.Surface) (t : CE.Tetrahedron s)
      → equivFun (equivalence s) t ≡ route-expression s t
    equivalence-route-computation (CE.surface a b c d) =
      Bridge.Horn.fixed-face-route-computation A e a b c d

    equivalence-sweep-computation : (s : CE.Surface) (t : CE.Tetrahedron s)
      → equivFun (equivalence s) t ≡ sweep-expression s t
    equivalence-sweep-computation (CE.surface a b c d) =
      Bridge.Horn.fixed-face-sweep-computation A e a b c d

-- The triangle comparison preserves the graded 2 -> 1 -> 0 projections:
-- extracting each marked edge after translation is the same package as
-- translating the edge first, and its endpoint vertices are unchanged.
module TriangleProjection {ℓ : Level} (A : Type ℓ) where
  module C = Cube.Simplex A
  module R = Retained.Cells A
  open C.TrianglePackage

  edge-ab-square : (f : C.TrianglePackage)
    → R.edge-ab (C.face-to-previous f) ≡ C.triangle-ab f
  edge-ab-square f = refl
  edge-bc-square : (f : C.TrianglePackage)
    → R.edge-bc (C.face-to-previous f) ≡ C.triangle-bc f
  edge-bc-square f = refl
  edge-ac-square : (f : C.TrianglePackage)
    → R.edge-ac (C.face-to-previous f) ≡ C.triangle-ac f
  edge-ac-square f = refl

  endpoint-ab-source : (f : C.TrianglePackage)
    → R.EdgePackage.source (C.triangle-ab f) ≡ x f
  endpoint-ab-source f = refl
  endpoint-ab-target : (f : C.TrianglePackage)
    → R.EdgePackage.target (C.triangle-ab f) ≡ y f
  endpoint-ab-target f = refl
  endpoint-bc-source : (f : C.TrianglePackage)
    → R.EdgePackage.source (C.triangle-bc f) ≡ y f
  endpoint-bc-source f = refl
  endpoint-bc-target : (f : C.TrianglePackage)
    → R.EdgePackage.target (C.triangle-bc f) ≡ z f
  endpoint-bc-target f = refl
  endpoint-ac-source : (f : C.TrianglePackage)
    → R.EdgePackage.source (C.triangle-ac f) ≡ x f
  endpoint-ac-source f = refl
  endpoint-ac-target : (f : C.TrianglePackage)
    → R.EdgePackage.target (C.triangle-ac f) ≡ z f
  endpoint-ac-target f = refl

-- An opposing-face projection is explicit structure: a map from the
-- triangle package to the omitted vertex, together with its value on the
-- marked opposing triangle. The map is not fabricated from the face's three
-- included vertices.
module OpposingVertexProjection {ℓ : Level} (A : Type ℓ) where
  module C = Cube.Simplex A
  module R = Retained.Cells A

  record Projection : Type (ℓ-suc ℓ) where
    constructor opposing-projection
    field
      triangle : C.TrianglePackage
      omittedVertex : A
      project : C.TrianglePackage → A
      projectsToOmitted : project triangle ≡ omittedVertex

    oldTriangle : R.FacePackage
    oldTriangle = C.face-to-previous triangle

    -- The earlier presentation inherits the same projection through the
    -- inverse triangle equivalence, so the diagram commutes on the nose.
    oldProject : R.FacePackage → A
    oldProject f = project (C.face-from-previous f)

    projection-commutes : oldProject oldTriangle ≡ project triangle
    projection-commutes = cong project (C.cubical-roundtrip triangle)

    old-projects-to-omitted : oldProject oldTriangle ≡ omittedVertex
    old-projects-to-omitted = projection-commutes ∙ projectsToOmitted

-- Four opposing triangles of a marked tetrahedron, each equipped with its
-- projection to the omitted vertex. The projection maps are explicit input
-- structure; conversion preserves their values on all four faces.
module TetrahedralOpposingProjections {ℓ : Level} (A : Type ℓ) where
  module C = Cube.Simplex A
  module R = Retained.Cells A

  record Projections (t : C.TetraPackage) : Type (ℓ-suc ℓ) where
    constructor opposing-projections
    field
      project012 : C.TrianglePackage → A
      project012Value : project012 (C.face012 t)
        ≡ R.Vertices.v3 (C.TetraPackage.vertices t)
      project123 : C.TrianglePackage → A
      project123Value : project123 (C.face123 t)
        ≡ R.Vertices.v0 (C.TetraPackage.vertices t)
      project013 : C.TrianglePackage → A
      project013Value : project013 (C.face013 t)
        ≡ R.Vertices.v2 (C.TetraPackage.vertices t)
      project023 : C.TrianglePackage → A
      project023Value : project023 (C.face023 t)
        ≡ R.Vertices.v1 (C.TetraPackage.vertices t)

    recoverVertices : R.Vertices
    recoverVertices = R.vertices
      (project123 (C.face123 t))
      (project023 (C.face023 t))
      (project013 (C.face013 t))
      (project012 (C.face012 t))
    omitted-vertices-recovered : recoverVertices ≡ C.TetraPackage.vertices t
    omitted-vertices-recovered i = R.vertices
      (project123Value i) (project023Value i)
      (project013Value i) (project012Value i)

    oldProject012 : R.FacePackage → A
    oldProject012 f = project012 (C.face-from-previous f)
    oldProject123 : R.FacePackage → A
    oldProject123 f = project123 (C.face-from-previous f)
    oldProject013 : R.FacePackage → A
    oldProject013 f = project013 (C.face-from-previous f)
    oldProject023 : R.FacePackage → A
    oldProject023 f = project023 (C.face-from-previous f)

    face012-projects-to-omitted : oldProject012 (C.face-to-previous (C.face012 t))
      ≡ R.Vertices.v3 (C.TetraPackage.vertices t)
    face012-projects-to-omitted =
      cong project012 (C.cubical-roundtrip (C.face012 t)) ∙ project012Value
    face123-projects-to-omitted : oldProject123 (C.face-to-previous (C.face123 t))
      ≡ R.Vertices.v0 (C.TetraPackage.vertices t)
    face123-projects-to-omitted =
      cong project123 (C.cubical-roundtrip (C.face123 t)) ∙ project123Value
    face013-projects-to-omitted : oldProject013 (C.face-to-previous (C.face013 t))
      ≡ R.Vertices.v2 (C.TetraPackage.vertices t)
    face013-projects-to-omitted =
      cong project013 (C.cubical-roundtrip (C.face013 t)) ∙ project013Value
    face023-projects-to-omitted : oldProject023 (C.face-to-previous (C.face023 t))
      ≡ R.Vertices.v1 (C.TetraPackage.vertices t)
    face023-projects-to-omitted =
      cong project023 (C.cubical-roundtrip (C.face023 t)) ∙ project023Value

-- Canonical incidence projection: an opposing triangle is tagged by its
-- face slot in a marked tetrahedron. The tag determines the omitted vertex;
-- a bare triangle package alone does not.
module OpposingFaceIncidence {ℓ : Level} (A : Type ℓ) where
  module C = Cube.Simplex A
  module R = Retained.Cells A

  data FaceSlot : Type where
    face012 face123 face013 face023 : FaceSlot

  opposingTriangle : (t : C.TetraPackage) → FaceSlot → C.TrianglePackage
  opposingTriangle t face012 = C.face012 t
  opposingTriangle t face123 = C.face123 t
  opposingTriangle t face013 = C.face013 t
  opposingTriangle t face023 = C.face023 t

  omittedVertex : (t : C.TetraPackage) → FaceSlot → A
  omittedVertex t face012 = R.Vertices.v3 (C.TetraPackage.vertices t)
  omittedVertex t face123 = R.Vertices.v0 (C.TetraPackage.vertices t)
  omittedVertex t face013 = R.Vertices.v2 (C.TetraPackage.vertices t)
  omittedVertex t face023 = R.Vertices.v1 (C.TetraPackage.vertices t)

  opposingTriangle-old : (t : C.TetraPackage) (slot : FaceSlot) → R.FacePackage
  opposingTriangle-old t slot = C.face-to-previous (opposingTriangle t slot)
  -- Translating the opposing triangle changes its presentation, not its
  -- incidence slot; hence its omitted-vertex readout is unchanged.
  omittedVertex-after-face-translation : (t : C.TetraPackage) (slot : FaceSlot)
    → omittedVertex t slot ≡ omittedVertex t slot
  omittedVertex-after-face-translation t slot = refl

  recoveredVertices : (t : C.TetraPackage) → R.Vertices
  recoveredVertices t = R.vertices
    (omittedVertex t face123)
    (omittedVertex t face023)
    (omittedVertex t face013)
    (omittedVertex t face012)
  recover-tetrahedron-vertices : (t : C.TetraPackage)
    → recoveredVertices t ≡ C.TetraPackage.vertices t
  recover-tetrahedron-vertices t = refl

module TypedFixture where
  module F = Cube.TypedFixture
  module E = F.S.At.WithEdges F.v F.e
  module B = Bridge.Horn (Retained.TypedValue ℓ-zero) E.edges0123
    (E.Faces.a012 F.faces) (E.Faces.a123 F.faces) (E.Faces.a013 F.faces)
  supplied : B.CubicalCompletion
  supplied = E.Faces.a023 F.faces , F.H.Horn.t0123 F.horn
  full-witness-roundtrip : B.to-cubical (B.to-old supplied) ≡ supplied
  full-witness-roundtrip = B.cubical-recovered supplied
  completion-square : B.to-old B.cubical-complete ≡ B.old-complete
  completion-square = B.complete-then-translate

  module T = FixedBoundaryTarget (Retained.TypedValue ℓ-zero) E.edges0123
  fixed-surface : T.CE.Surface
  fixed-surface = T.CE.surface (E.Faces.a012 F.faces) (E.Faces.a123 F.faces)
    (E.Faces.a013 F.faces) (E.Faces.a023 F.faces)
  independently-translated-filler : T.old-filler fixed-surface
  independently-translated-filler = equivFun (T.equivalence fixed-surface) (snd supplied)
  fixed-boundary-roundtrip :
    invEq (T.equivalence fixed-surface) independently-translated-filler ≡ snd supplied
  fixed-boundary-roundtrip = retEq (T.equivalence fixed-surface) (snd supplied)
