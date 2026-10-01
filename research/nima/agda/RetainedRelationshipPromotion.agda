{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedRelationshipPromotion where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (rec)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_; map)
open import Cubical.Data.Sigma.Base using (_×_)
import TableFibrationCycle as F
import WholePackageSigmaPi as Whole
import WholePackageResolution as Native

-- Explicit new promotion adapter. Pairing and shared-endpoint generation are
-- supplied operations, not claimed consequences of reversible normalization.
module Promote (V E : Type) (vertices : List V) (edges : List E)
  (ends : E → V × V) (before : E → E → Bool) (eqV : V → V → Bool)
  (eqV-sound : (a b : V) → eqV a b ≡ true → a ≡ b) where

  Packet = E × Bool
  label : Packet → E
  label = fst
  from : Packet → V
  from (e , false) = fst (ends e)
  from (e , true) = snd (ends e)
  to : Packet → V
  to (e , false) = snd (ends e)
  to (e , true) = fst (ends e)
  source : F.Table E V V
  source = F.table Packet label from to
  grouped = F.group-label source
  Fiber : E → Type
  Fiber e = F.fibrate label e
  member : (e : E) → Bool → Fiber e
  member e d = (e , d) , refl
  packet-recovery = F.column-recovery source F.label-column

  fiber-two : (e : E) → Iso (Fiber e) Bool
  Iso.fun (fiber-two e) ((e' , d) , witness) = d
  Iso.inv (fiber-two e) = member e
  Iso.rightInv (fiber-two e) d = refl
  Iso.leftInv (fiber-two e) ((e' , d) , witness) i =
    (witness (~ i) , d) , (λ j → witness (~ i ∨ j))

  packets : List Packet
  packets = concat-pairs edges
    where
    concat-pairs : List E → List Packet
    concat-pairs [] = []
    concat-pairs (e ∷ es) = (e , false) ∷ (e , true) ∷ concat-pairs es

  open Whole.Universe ℓ-zero hiding (E)
  open Native.Generators ℓ-zero
  packet-package : Packet → Complete
  packet-package p = pack (atom Packet) p
  -- The only native seeds are actual input packets, not arbitrary boundary data.
  Seed : Complete → Type₁
  Seed q = Σ[ p ∈ Packet ] (q ≡ packet-package p)
  vertex-package : E → Complete
  vertex-package e = Pi-package Bool (λ d → packet-package (e , d))
  compile-vertex : (e : E) → Resolve Seed (vertex-package e)
  compile-vertex e = apply (Pi-rule Bool (λ d → packet-package (e , d)))
    (λ { (lift d) → seed ((e , d) , refl) })

  either : Bool → Bool → Bool
  either false b = b
  either true b = true
  touches : V → E → Bool
  touches v e = either (eqV v (fst (ends e))) (eqV v (snd (ends e)))
  record Connection : Type where
    constructor connection
    field
      left right : E
      ordered : before left right ≡ true
      shared : V
      left-witness : touches shared left ≡ true
      right-witness : touches shared right ≡ true
  open Connection

  either-witness : (a b : Bool) → either a b ≡ true → (a ≡ true) ⊎ (b ≡ true)
  either-witness true b p = inl refl
  either-witness false true p = inr refl
  either-witness false false p = rec (true≢false (sym p))
  EndpointWitness : V → E → Type
  EndpointWitness v e = (fst (ends e) ≡ v) ⊎ (snd (ends e) ≡ v)
  touch-proof : (v : V) (e : E) → touches v e ≡ true → EndpointWitness v e
  touch-proof v e p with either-witness (eqV v (fst (ends e))) (eqV v (snd (ends e))) p
  ... | inl left = inl (sym (eqV-sound v (fst (ends e)) left))
  ... | inr right = inr (sym (eqV-sound v (snd (ends e)) right))
  real-left : (c : Connection) → EndpointWitness (shared c) (left c)
  real-left c = touch-proof (shared c) (left c) (left-witness c)
  real-right : (c : Connection) → EndpointWitness (shared c) (right c)
  real-right c = touch-proof (shared c) (right c) (right-witness c)

  select : (b : Bool) → (b ≡ true → List Connection) → List Connection
  select false yes = []
  select true yes = yes refl
  at : E → E → V → List Connection
  at e f v = select (before e f) (λ ordered →
    select (touches v e) (λ lp → select (touches v f) (λ rp →
      connection e f ordered v lp rp ∷ [])))
  join : {A B : Type} → (A → List B) → List A → List B
  join f [] = []
  join f (a ∷ as) = f a ++ join f as
  connections : List Connection
  connections = join (λ e → join (λ f → join (at e f) vertices) edges) edges

  NextPacket = Connection × Bool
  next-packets : List NextPacket
  next-packets = join (λ c → (c , false) ∷ (c , true) ∷ []) connections
  next-from : NextPacket → E
  next-from (c , false) = left c
  next-from (c , true) = right c
  next-to : NextPacket → E
  next-to (c , false) = right c
  next-to (c , true) = left c
  next-table : F.Table Connection E E
  next-table = F.table NextPacket fst next-from next-to

  record RetainedPromotion : Type₁ where
    constructor retained-promotion
    field
      source-table : F.Table E V V
      source-agrees : source-table ≡ source
      retained-packets : List Packet
      packets-agree : retained-packets ≡ packets
      retained-fibers : F.Grouped E V V
      fibers-agree : retained-fibers ≡ grouped
      native-vertices : (e : E) → Resolve Seed (vertex-package e)
      generated-connections : List Connection
      connections-agree : generated-connections ≡ connections
      promoted-table : F.Table Connection E E
      table-agrees : promoted-table ≡ next-table

  run : RetainedPromotion
  run = retained-promotion source refl packets refl grouped refl
    compile-vertex connections refl next-table refl
  next-input : Whole.Universe.Complete (ℓ-suc ℓ-zero)
  next-input = Whole.Universe.pack (Whole.Universe.atom RetainedPromotion) run

  source-survives : RetainedPromotion.source-table (Whole.Universe.value next-input) ≡ source
  source-survives = refl
  generated-links-survive : RetainedPromotion.generated-connections
    (Whole.Universe.value next-input) ≡ connections
  generated-links-survive = refl
