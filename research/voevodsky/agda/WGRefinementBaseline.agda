{-# OPTIONS --safe --cubical --guardedness #-}
module WGRefinementBaseline where

-- Independent ordinary dependent-pair implementation. No WG imports.
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso; iso)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)

-- INPUT: identical data to ComposableWitnessSpecialization.ProofDependentFixture.
Source : Type₁
Source = Lift {j = ℓ-suc ℓ-zero} Bool
source₁ source₂ source₃ : Source
source₁ = lift true
source₂ = lift false
source₃ = lift true

State₁ : Type
State₁ = Bool × Bool
Edge₁ : State₁ → State₁ → Type
Edge₁ x y = (fst y ≡ not (fst x)) × Bool
next₁ : State₁ → State₁
next₁ (s , p) = not s , not p
edge₁ : (x : State₁) → Edge₁ x (next₁ x)
edge₁ (s , p) = refl , p

-- TWO LAYERS: second evidence depends on the first edge's Bool, not endpoints.
Nested Flat : Type
Nested = State₁ × Bool
Flat = Bool × (Bool × Bool)
SecondEvidence : (x y : Nested) → Edge₁ (fst x) (fst y) → Type
SecondEvidence x y w = snd w ≡ snd (fst x)
NestedEdge : Nested → Nested → Type
NestedEdge x y = Σ[ w ∈ Edge₁ (fst x) (fst y) ] SecondEvidence x y w
FlatEdge : Flat → Flat → Type
FlatEdge x y = Σ[ r ∈ (fst y ≡ not (fst x)) ] Σ[ e ∈ Bool ] e ≡ fst (snd x)
nextN : Nested → Nested
nextN ((s , p) , q) = (not s , not p) , not q
edgeN : (x : Nested) → NestedEdge x (nextN x)
edgeN ((s , p) , q) = (refl , p) , refl
nextF : Flat → Flat
nextF (s , p , q) = not s , not p , not q
edgeF : (x : Flat) → FlatEdge x (nextF x)
edgeF (s , p , q) = refl , p , refl

flatten : Nested → Flat
flatten ((s , p) , q) = s , p , q
unflatten : Flat → Nested
unflatten (s , p , q) = (s , p) , q
flattenEdge : {x y : Nested} → NestedEdge x y → FlatEdge (flatten x) (flatten y)
flattenEdge ((r , e) , f) = r , e , f
unflattenEdge : {x y : Flat} → FlatEdge x y → NestedEdge (unflatten x) (unflatten y)
unflattenEdge (r , e , f) = (r , e) , f
states : Iso Nested Flat
states = iso flatten unflatten (λ _ → refl) (λ _ → refl)
steps : (x : Nested) → Iso (Σ[ y ∈ Nested ] NestedEdge x y)
  (Σ[ y ∈ Flat ] FlatEdge (flatten x) y)
steps x = iso (λ { (y , w) → flatten y , flattenEdge {x = x} {y = y} w })
  (λ { (y , w) → unflatten y , unflattenEdge {x = flatten x} {y = y} w }) (λ _ → refl) (λ _ → refl)
endpoints : (x : Nested) (z : Σ[ y ∈ Nested ] NestedEdge x y)
  → fst (Iso.fun (steps x) z) ≡ flatten (fst z)
endpoints x z = refl
generated : (x : Nested)
  → Iso.fun (steps x) (nextN x , edgeN x) ≡ (nextF (flatten x) , edgeF (flatten x))
generated x = refl
sources : Source × Source
sources = source₁ , source₂
recover₁ : fst sources ≡ source₁
recover₁ = refl
recover₂ : snd sources ≡ source₂
recover₂ = refl
rejectsErasure : SecondEvidence ((false , true) , false) ((true , false) , true)
  (refl , false) → ⊥
rejectsErasure = false≢true

-- THIRD LAYER: re-use the composite and retain dependency on its first payload.
Left Right : Type
Left = Bool × ((Bool × Bool) × Bool)
Right = Bool × (Bool × (Bool × Bool))
LeftEdge : Left → Left → Type
LeftEdge (s , (p , q) , z) (t , (p' , q') , z') =
  Σ[ r ∈ (t ≡ not s) ] Σ[ ef ∈ (Σ[ e ∈ Bool ] e ≡ p) ] fst ef ≡ p
RightEdge : Right → Right → Type
RightEdge (s , p , q , z) (t , p' , q' , z') =
  Σ[ r ∈ (t ≡ not s) ] Σ[ e ∈ Bool ] (e ≡ p) × (e ≡ p)
nextL : Left → Left
nextL (s , (p , q) , z) = not s , (not p , not q) , not z
edgeL : (x : Left) → LeftEdge x (nextL x)
edgeL (s , (p , q) , z) = refl , (p , refl) , refl
nextR : Right → Right
nextR (s , p , q , z) = not s , not p , not q , not z
edgeR : (x : Right) → RightEdge x (nextR x)
edgeR (s , p , q , z) = refl , p , refl , refl
associate : Left → Right
associate (s , (p , q) , z) = s , p , q , z
unassociate : Right → Left
unassociate (s , p , q , z) = s , (p , q) , z
associateEdge : {x y : Left} → LeftEdge x y → RightEdge (associate x) (associate y)
associateEdge (r , (e , f) , h) = r , e , f , h
unassociateEdge : {x y : Right} → RightEdge x y → LeftEdge (unassociate x) (unassociate y)
unassociateEdge (r , e , f , h) = r , (e , f) , h
associatedStates : Iso Left Right
associatedStates = iso associate unassociate (λ _ → refl) (λ _ → refl)
associatedSteps : (x : Left) → Iso (Σ[ y ∈ Left ] LeftEdge x y)
  (Σ[ y ∈ Right ] RightEdge (associate x) y)
associatedSteps x = iso (λ { (y , w) → associate y , associateEdge {x = x} {y = y} w })
  (λ { (y , w) → unassociate y , unassociateEdge {x = associate x} {y = y} w }) (λ _ → refl) (λ _ → refl)
associatedEndpoints : (x : Left) (z : Σ[ y ∈ Left ] LeftEdge x y)
  → fst (Iso.fun (associatedSteps x) z) ≡ associate (fst z)
associatedEndpoints x z = refl
associatedGenerated : (x : Left)
  → Iso.fun (associatedSteps x) (nextL x , edgeL x) ≡ (nextR (associate x) , edgeR (associate x))
associatedGenerated x = refl
sourceAssociator : Iso ((Source × Source) × Source) (Source × (Source × Source))
sourceAssociator = iso (λ { ((a , b) , c) → a , b , c })
  (λ { (a , b , c) → (a , b) , c }) (λ _ → refl) (λ _ → refl)
sourcePreserved : Iso.fun sourceAssociator ((source₁ , source₂) , source₃)
  ≡ (source₁ , source₂ , source₃)
sourcePreserved = refl
