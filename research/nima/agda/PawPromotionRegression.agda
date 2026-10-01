{-# OPTIONS --safe --cubical --guardedness #-}
module PawPromotionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (rec)
open import Cubical.Data.List.Base using (List; []; _∷_; map; length)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
import RetainedRelationshipPromotion as Promotion
import TableFibrationCycle as F
import FirstRungFourRecordRegression as Floor
import WholePackageSigmaPi as Whole

data Vertex : Type where
  A B C D : Vertex
data Edge : Type where
  AB AC BC AD : Edge
vertices = A ∷ B ∷ C ∷ D ∷ []
edges = AB ∷ AC ∷ BC ∷ AD ∷ []
ends : Edge → Vertex × Vertex
ends AB = A , B
ends AC = A , C
ends BC = B , C
ends AD = A , D
rank : Edge → ℕ
rank AB = 0
rank AC = 1
rank BC = 2
rank AD = 3
less : ℕ → ℕ → Bool
less zero zero = false
less zero (suc n) = true
less (suc m) zero = false
less (suc m) (suc n) = less m n
before : Edge → Edge → Bool
before a b = less (rank a) (rank b)
eqV : Vertex → Vertex → Bool
eqV A A = true
eqV B B = true
eqV C C = true
eqV D D = true
eqV _ _ = false
impossible : {X : Type} → false ≡ true → X
impossible p = rec (true≢false (sym p))
eqV-sound : (a b : Vertex) → eqV a b ≡ true → a ≡ b
eqV-sound A A p = refl
eqV-sound B B p = refl
eqV-sound C C p = refl
eqV-sound D D p = refl
eqV-sound A B p = impossible p
eqV-sound A C p = impossible p
eqV-sound A D p = impossible p
eqV-sound B A p = impossible p
eqV-sound B C p = impossible p
eqV-sound B D p = impossible p
eqV-sound C A p = impossible p
eqV-sound C B p = impossible p
eqV-sound C D p = impossible p
eqV-sound D A p = impossible p
eqV-sound D B p = impossible p
eqV-sound D C p = impossible p
module P = Promotion.Promote Vertex Edge vertices edges ends before eqV eqV-sound

input-eight : length P.packets ≡ 8
input-eight = refl
four-fibers : length edges ≡ 4
four-fibers = refl
five-generated-links : length P.connections ≡ 5
five-generated-links = refl
ten-next-packets : length P.next-packets ≡ 10
ten-next-packets = refl

signature : P.Connection → Edge × Edge × Vertex
signature c = P.Connection.left c , P.Connection.right c , P.Connection.shared c
expected : List (Edge × Edge × Vertex)
expected = (AB , AC , A) ∷ (AB , BC , B) ∷ (AB , AD , A)
  ∷ (AC , BC , C) ∷ (AC , AD , A) ∷ []
actual-witnesses : map signature P.connections ≡ expected
actual-witnesses = refl

-- The generated table is accepted directly by the existing rung descent.
module NextFloor = Floor.Descent {L = P.Connection} {S = Edge} {T = Edge}
next-floor = NextFloor.floor P.next-table
next-packet-recovery : (p : P.NextPacket)
  → NextFloor.recover P.next-table (NextFloor.run P.next-table p) ≡ p
next-packet-recovery = NextFloor.roundtrip P.next-table

-- Promotion of the actual generated witness table is available as Complete.
promoted = P.next-input
source-still-present : P.RetainedPromotion.source-table (Whole.Universe.value promoted) ≡ P.source
source-still-present = refl
