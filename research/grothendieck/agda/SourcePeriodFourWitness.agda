{-# OPTIONS --safe --cubical --guardedness #-}
module SourcePeriodFourWitness where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.Nat.Properties using (injSuc; snotz)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import ActualSeedEndpointTable
import SeedSeamPathComparisonBoundary as H
import PeriodFourWitness as P

-- Explicit selection, not inferred uniqueness from the endpoint table.
next : Vertex → Vertex
next A = D
next D = B
next B = C
next C = A

chosen-edge : (v : Vertex) → Occurrence
chosen-edge A = AD
chosen-edge D = DB
chosen-edge B = BC
chosen-edge C = CA

chosen-source : (v : Vertex) → source (chosen-edge v) ≡ v
chosen-source A = refl
chosen-source B = refl
chosen-source C = refl
chosen-source D = refl

chosen-target : (v : Vertex) → target (chosen-edge v) ≡ next v
chosen-target A = refl
chosen-target B = refl
chosen-target C = refl
chosen-target D = refl

module Selected = P.PeriodFour next

fourth-return : (v : Vertex) → Selected.fourth v ≡ v
fourth-return A = refl
fourth-return B = refl
fourth-return C = refl
fourth-return D = refl

canonical : (v : Vertex) → Selected.Per4
canonical v = v , fourth-return v

canonical-four-shifts : (v : Vertex)
  → Selected.shift (Selected.shift (Selected.shift (Selected.shift (canonical v))))
    ≡ canonical v
canonical-four-shifts v = Selected.shift-four-return (canonical v)

-- Identity projection on active vertices; no equality on history is asserted.
record ReturnWindow (a : Vertex) : Type where
  constructor window
  field
    endpoint : Vertex
    history : H.Path a endpoint
    four-occurrences : H.length history ≡ 4
    active-return : endpoint ≡ a

cycle : H.Path A A
cycle = H.step AD (H.step DB (H.step BC (H.step CA H.stop)))

selected-window : ReturnWindow A
selected-window = window A cycle refl refl

positive : ℕ → Bool
positive 0 = false
positive (suc n) = true

cycle-not-empty : cycle ≡ H.stop → ⊥
cycle-not-empty p = true≢false (cong (λ h → positive (H.length h)) p)

-- The return record retains the original occurrence word, not just endpoints.
retains-cycle : ReturnWindow.history selected-window ≡ cycle
retains-cycle = refl

append-cycle : {s : Vertex} → H.Path s A → H.Path s A
append-cycle H.stop = cycle
append-cycle (H.step e rest) = H.step e (append-cycle rest)

append-length-differs : {s : Vertex} (h : H.Path s A)
  → H.length (append-cycle h) ≡ H.length h → ⊥
append-length-differs H.stop p = snotz p
append-length-differs (H.step e rest) p =
  append-length-differs rest (injSuc p)

accumulated-history-does-not-return : {s : Vertex} (h : H.Path s A)
  → append-cycle h ≡ h → ⊥
accumulated-history-does-not-return h p =
  append-length-differs h (cong H.length p)

-- A second source-permitted outgoing edge at A refutes unique selection.
is-D : Vertex → Bool
is-D A = false
is-D B = false
is-D C = false
is-D D = true

alternative-source : source AB ≡ A
alternative-source = refl

alternative-target-distinct : next A ≡ target AB → ⊥
alternative-target-distinct p = true≢false (cong is-D p)
