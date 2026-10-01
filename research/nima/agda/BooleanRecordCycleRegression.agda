{-# OPTIONS --safe --cubical --guardedness #-}
module BooleanRecordCycleRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Nat.Base using (ℕ; suc)
import TableFibrationCycle as F
import WholePackageSigmaPi as Whole
import NativeNormalizationRouteCompiler as Native

-- The supplied cycle is the existing four-operation table cycle:
-- group-from / unpack-reversed / group-from / unpack-reversed.
-- Compile its two compound row equivalences with the existing native compiler.
module Cycle {ℓ : Level} {L S T : Type ℓ} (q : F.Table L S T) where
  open Whole.Universe ℓ
  Q = atom (F.Table.Rows q)
  module C = Native.Compiler ℓ Q
  module H = C.H

  q1 = F.twice q
  q2 = F.four q
  e1 = invEquiv (isoToEquiv (F.TableIso.rows (F.twice-correct q)))
  e2 = invEquiv (isoToEquiv (F.TableIso.rows (F.twice-correct q1)))
  P1 = H.advance H.original (atom (F.Table.Rows q1)) e1
  P2 = H.advance P1 (atom (F.Table.Rows q2)) e2
  route : H.Route H.original P2
  route = H.next {P = H.original} {R = P1} {T = P2}
    (H.advance-map H.original (atom (F.Table.Rows q1)) e1)
    (H.next {P = P1} {R = P2} {T = P2}
      (H.advance-map P1 (atom (F.Table.Rows q2)) e2) (H.stop {P = P2}))

  steps : {P R : H.Presentation} → H.Route P R → ℕ
  steps H.stop = 0
  steps (H.next f rest) = suc (steps rest)
  two-comparison-slots : steps route ≡ 2
  two-comparison-slots = refl

  run = C.retain-compilation route
  certified = C.compile-leaves route
  recovered : F.Table.Rows q → F.Table.Rows q
  recovered x = Iso.fun (F.TableIso.rows (F.four-correct q)) (C.execute route x)
  recovery : (x : F.Table.Rows q) → recovered x ≡ x
  recovery x = refl

  -- A retained package can have an arbitrary source presentation. Decode its
  -- faithful coordinates rather than pretending all Retained values use ours.
  decode : C.Retained → F.Table.Rows q
  decode r = H.N.reconstruct Q
    (equivFun (H.Presentation.coordinates (C.Retained.source r))
      (C.Retained.input-value r))
  decode-run : (x : F.Table.Rows q) → decode (run x) ≡ x
  decode-run x = refl
  run-injective : (x y : F.Table.Rows q) → run x ≡ run y → x ≡ y
  run-injective x y p = cong decode p

  promoted : F.Table (Lift {j = ℓ-suc ℓ} L)
    (Lift {j = ℓ-suc ℓ} S) (Lift {j = ℓ-suc ℓ} T)
  promoted = F.table C.Retained
    (λ r → lift (F.Table.label q (decode r)))
    (λ r → lift (F.Table.from q (decode r)))
    (λ r → lift (F.Table.to q (decode r)))

  -- Promotion keeps precisely the existing next-Q value; it does not unwrap
  -- the previous history into an unrecorded seed.
  promoted-value : (x : F.Table.Rows q)
    → Whole.Universe.value (C.next-Q (run x)) ≡ run x
  promoted-value x = refl

X : Type
X = Bool × Bool
base : F.Table Unit Bool Bool
base = F.table X (λ _ → tt) fst snd
module C0 = Cycle base
module C1 = Cycle C0.promoted
module C2 = Cycle C1.promoted

cycle1 = C0.run
cycle2 : X → C1.C.Retained
cycle2 x = C1.run (cycle1 x)
cycle3 : X → C2.C.Retained
cycle3 x = C2.run (cycle2 x)

recover3 : C2.C.Retained → X
recover3 r = C0.decode (C1.decode (C2.decode r))
original-retained : (x : X) → recover3 (cycle3 x) ≡ x
original-retained x = refl
three-cycle-injective : (x y : X) → cycle3 x ≡ cycle3 y → x ≡ y
three-cycle-injective x y p = cong recover3 p

-- Four explicit reachable inputs; injectivity keeps these four outputs distinct.
input00 : X
input00 = false , false
input01 : X
input01 = false , true
input10 : X
input10 = true , false
input11 : X
input11 = true , true
output00 = cycle3 input00
output01 = cycle3 input01
output10 = cycle3 input10
output11 = cycle3 input11

-- Full history of the preceding run is literally the next run's input.
previous-record-is-input : (x : X)
  → C2.C.Retained.input-value (cycle3 x) ≡ cycle2 x
previous-record-is-input x = refl
second-record-is-input : (x : X)
  → C1.C.Retained.input-value (cycle2 x) ≡ cycle1 x
second-record-is-input x = refl
