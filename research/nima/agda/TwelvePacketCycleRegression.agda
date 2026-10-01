{-# OPTIONS --safe --cubical --guardedness #-}
module TwelvePacketCycleRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_×_)
import TableFibrationCycle as F
import BooleanRecordCycleRegression as Existing

flip : Bool → Bool
flip false = true
flip true = false

Address : Type
Address = Bool × Bool

data Change : Type where
  first second both : Change
Packet : Type
Packet = Address × Change

-- Four addresses times three nonidentity changes enumerate all twelve packets.
target : Packet → Address
target ((a , b) , first) = flip a , b
target ((a , b) , second) = a , flip b
target ((a , b) , both) = flip a , flip b

base : F.Table Packet Address Address
base = F.table Packet (λ p → p) fst target
module C0 = Existing.Cycle base
module C1 = Existing.Cycle C0.promoted
module C2 = Existing.Cycle C1.promoted

cycle1 : Packet → C0.C.Retained
cycle1 = C0.run
cycle2 : Packet → C1.C.Retained
cycle2 p = C1.run (cycle1 p)
cycle3 : Packet → C2.C.Retained
cycle3 p = C2.run (cycle2 p)

recover : C2.C.Retained → Packet
recover r = C0.decode (C1.decode (C2.decode r))
all-packets-retained : (p : Packet) → recover (cycle3 p) ≡ p
all-packets-retained p = refl
no-packet-merging : (p q : Packet) → cycle3 p ≡ cycle3 q → p ≡ q
no-packet-merging p q e = cong recover e
source-preserved : (p : Packet) → fst (recover (cycle3 p)) ≡ fst p
source-preserved p = refl
target-preserved : (p : Packet) → target (recover (cycle3 p)) ≡ target p
target-preserved p = refl
previous-cycle-is-input : (p : Packet)
  → C2.C.Retained.input-value (cycle3 p) ≡ cycle2 p
previous-cycle-is-input p = refl
