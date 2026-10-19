{-# OPTIONS --safe --cubical --guardedness #-}
module NativeGeneratingLeafTable where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import TwoBlockLeafGeneration using (Kind; arrow; state; Leaf; edge; point; pair;
  Frame; full-arrows; input; compare; Blocks; actual-frame; count; generated-count)
import TableFibrationCycle as T
import WholePackageSigmaPi as W

-- Occurrence indices, not bare leaf values: no duplicate is silently collapsed.
data Occ {A : Type} : List A → Type where
  here : {x : A} {xs : List A} → Occ (x ∷ xs)
  there : {x : A} {xs : List A} → Occ xs → Occ (x ∷ xs)
at : {A : Type} {xs : List A} → Occ xs → A
at {xs = x ∷ xs} here = x
at (there i) = at i

Label : Type
Label = Σ[ k ∈ Kind ] Leaf k
Endpoint : Type
Endpoint = Σ[ k ∈ Kind ] List ℕ
sources targets : {k : Kind} → Leaf k → List ℕ
sources (edge i j) = i ∷ []
sources (point i) = i ∷ []
sources (pair a b) = sources a ++ sources b
targets (edge i j) = j ∷ []
targets (point i) = i ∷ []
targets (pair a b) = targets a ++ targets b
from-label to-label : Label → Endpoint
from-label (k , x) = k , sources x
to-label (k , x) = k , targets x

LeafTable : Type₁
LeafTable = T.Table Label Endpoint Endpoint
primitive-table : Frame → LeafTable
primitive-table f = T.table (Occ (full-arrows f))
  (λ i → arrow , at i) (λ i → arrow , sources (at i)) (λ i → arrow , targets (at i))

output-blocks : Frame → Blocks
output-blocks f = compare (input f)
output-rows : Frame → Type
output-rows f = Occ (Blocks.arrows (output-blocks f)) ⊎ Occ (Blocks.states (output-blocks f))
output-label : (f : Frame) → output-rows f → Label
output-label f (inl i) = arrow , at i
output-label f (inr i) = state , at i
generated-table : Frame → LeafTable
generated-table f = T.table (output-rows f) (output-label f)
  (λ i → from-label (output-label f i)) (λ i → to-label (output-label f i))

-- Existing native grouping/restoration, including its endpoint certificates.
view : LeafTable → T.Column → LeafTable
view q k = T.restore-table k (T.fibrate-table q k)
view-correct : (q : LeafTable) (k : T.Column) → T.TableIso (view q k) q
view-correct = T.restore-correct

record Presented : Type₁ where
  constructor presented
  field
    seed : Frame
    selector : T.Column
    table-view : LeafTable
    phase-correct : table-view ≡ view (primitive-table seed) selector
    recovery : T.TableIso table-view (primitive-table seed)

present : (f : Frame) → T.Column → Presented
present f k = presented f k (view (primitive-table f) k) refl (view-correct (primitive-table f) k)

record Generated : Type₁ where
  constructor generated
  field
    predecessor : Presented
    selector : T.Column
    table-view : LeafTable
    phase-correct : table-view ≡ view (generated-table (Presented.seed predecessor)) selector
    recovery : T.TableIso table-view (generated-table (Presented.seed predecessor))

-- This whole-package operation uses the retained frame and certified native
-- view. It is not a map from one primitive row to one generated row.
run : Presented → T.Column → Generated
run p k = generated p k (view (generated-table (Presented.seed p)) k) refl
  (view-correct (generated-table (Presented.seed p)) k)

complete-run : Presented → T.Column → W.Universe.Complete (ℓ-suc ℓ-zero)
complete-run p k = W.Universe.pack (W.Universe.atom Generated) (run p k)
retains-predecessor : (p : Presented) (k : T.Column)
  → Generated.predecessor (W.Universe.value (complete-run p k)) ≡ p
retains-predecessor p k = refl
retains-selector : (p : Presented) (k : T.Column)
  → Generated.selector (W.Universe.value (complete-run p k)) ≡ k
retains-selector p k = refl

-- The comparison identifies recovered TABLE DATA, not full operation syntax.
source-target-view-comparison : (f : Frame)
  → Generated.table-view (run (present f T.from-column) T.to-column)
      ≡ generated-table f
source-target-view-comparison f = T.table-path (view-correct (generated-table f) T.to-column)
actual-count : count (output-blocks actual-frame) ≡ 137
actual-count = generated-count

-- A genuine phase hostile on the ACTUAL input, with labels preserved.
-- Transpose can permute endpoints, but cannot be a label-preserving identity.
head : Endpoint → ℕ
head (k , []) = zero
head (k , x ∷ xs) = x
is-zero : ℕ → Bool
is-zero zero = true
is-zero (suc n) = false
no-labelled-endpoint-reversal :
  T.TableIso (primitive-table actual-frame) (T.transpose (primitive-table actual-frame)) → ⊥
no-labelled-endpoint-reversal e = false≢true (cong is-zero
  (sym (cong (λ l → head (to-label l)) (T.TableIso.preserves-label e here))
   ∙ cong head (T.TableIso.preserves-from e here)))
