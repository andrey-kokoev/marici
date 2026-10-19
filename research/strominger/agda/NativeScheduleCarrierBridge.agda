{-# OPTIONS --safe --cubical --guardedness #-}
module NativeScheduleCarrierBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_; map)
import TwoBlockLeafGeneration as G
import NativeGeneratingLeafTable as N
import NativeOuterFamilyEncoding as O
import ActualNativeOuterFamilies as A
import TableFibrationCycle as T
import WholePackageSigmaPi as W

-- The source's actual label/tag conventions, not an equality of counts.
branch : G.Kind → O.Key
branch G.arrow = O.text (97 ∷ [])
branch G.state = O.text (115 ∷ [])
endpoint : G.Kind → List ℕ → O.Key
endpoint k xs = O.tuple (branch k ∷ map O.nat xs)
leaf-id : ℕ → O.Key
leaf-id n = O.tuple (O.text (108 ∷ 101 ∷ 97 ∷ 102 ∷ []) ∷ O.nat n ∷ [])
skeleton : O.Row → O.Key
skeleton r = O.tuple (O.label r ∷ O.source r ∷ O.target r ∷ [])
encode : ℕ → List N.Label → List O.Key
encode n [] = []
encode n ((k , x) ∷ xs) =
  O.tuple (leaf-id n ∷ endpoint k (N.sources x) ∷ endpoint k (N.targets x) ∷ [])
  ∷ encode (suc n) xs
native-labels : G.Frame → List N.Label
native-labels f = map (λ x → G.arrow , x) (G.Blocks.arrows (N.output-blocks f))
  ++ map (λ x → G.state , x) (G.Blocks.states (N.output-blocks f))
native-skeleton : G.Frame → List O.Key
native-skeleton f = encode 0 (native-labels f)

-- Checked against separately source-exported fields, including order and IDs.
actual-structural-bridge : native-skeleton G.actual-frame ≡ map skeleton A.original
actual-structural-bridge = refl

swap-endpoints : O.Key → O.Key
swap-endpoints (O.tuple (l ∷ s ∷ t ∷ [])) = O.tuple (l ∷ t ∷ s ∷ [])
swap-endpoints x = x
first-source-zero : List O.Key → Bool
first-source-zero (O.tuple (l ∷ O.tuple (tag ∷ O.nat n ∷ ns) ∷ rest) ∷ rs) = O.same 0 n
first-source-zero _ = false
wrong-endpoint-bridge : map swap-endpoints (native-skeleton G.actual-frame)
  ≡ map skeleton A.original → ⊥
wrong-endpoint-bridge p = false≢true (cong first-source-zero p)

forest : Bool → List O.Row
forest false = A.inherited
forest true = A.common
forest-bridge : (policy : Bool)
  → map skeleton (O.leaves (forest policy)) ≡ native-skeleton G.actual-frame
forest-bridge false = cong (map skeleton) A.inherited-leaves ∙ sym actual-structural-bridge
forest-bridge true = cong (map skeleton) A.common-leaves ∙ sym actual-structural-bridge

-- A complete typed schedule result, retaining the actual generated predecessor
-- AND the outer forest. This is a finite structural bridge, not a mean evaluator.
record Linked (p : N.Presented) (k : T.Column) : Type₁ where
  constructor linked
  field
    native : N.Generated
    native-correct : native ≡ N.run p k
    policy : Bool
    outer-forest : List O.Row
    policy-correct : outer-forest ≡ forest policy
    carrier-bridge : map skeleton (O.leaves outer-forest) ≡ native-skeleton (N.Presented.seed p)
    outer-view : T.Table O.Key O.Key O.Key
    phase-correct : outer-view ≡ T.restore-table k (T.fibrate-table (O.outer-table outer-forest) k)
    recovery : T.TableIso outer-view (O.outer-table outer-forest)
    reference : O.Key
    reference-correct : reference ≡ A.direct-reference

run-linked : (input-phase output-phase : T.Column) (policy : Bool)
  → Linked (N.present G.actual-frame input-phase) output-phase
run-linked i o policy = linked (N.run (N.present G.actual-frame i) o) refl
  policy (forest policy) refl (forest-bridge policy)
  (T.restore-table o (T.fibrate-table (O.outer-table (forest policy)) o)) refl
  (O.restored (forest policy) o) A.direct-reference refl

complete-linked : (i o : T.Column) → Bool → W.Universe.Complete (ℓ-suc ℓ-zero)
complete-linked i o b = W.Universe.pack
  (W.Universe.atom (Linked (N.present G.actual-frame i) o)) (run-linked i o b)

retained-predecessor : (i o : T.Column) (b : Bool)
  → N.Generated.predecessor (Linked.native (W.Universe.value (complete-linked i o b)))
      ≡ N.present G.actual-frame i
retained-predecessor i o b = refl
retained-selector : (i o : T.Column) (b : Bool)
  → N.Generated.selector (Linked.native (W.Universe.value (complete-linked i o b))) ≡ o
retained-selector i o b = refl
retained-forest : (i o : T.Column) (b : Bool)
  → Linked.outer-forest (W.Universe.value (complete-linked i o b)) ≡ forest b
retained-forest i o b = refl
retained-reference : (i o : T.Column) (b : Bool)
  → Linked.reference (W.Universe.value (complete-linked i o b)) ≡ A.direct-reference
retained-reference i o b = refl

-- Row recovery is on the OUTER carrier. Flattening is a different map.
outer-table-recovery : (i o : T.Column) (b : Bool)
  → Linked.outer-view (run-linked i o b) ≡ O.outer-table (forest b)
outer-table-recovery i o b = T.table-path (O.restored (forest b) o)
