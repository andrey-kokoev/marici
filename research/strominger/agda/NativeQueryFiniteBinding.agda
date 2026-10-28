{-# OPTIONS --safe --cubical --guardedness #-}
module NativeQueryFiniteBinding where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.List.Base using (List; []; _∷_)
import NativeQueryControlledRecorder as R
import NativeSeedTransitionProbe as Q
import NativeQueryWordRealization as W
import SeedAttachedObserver as Seed
open Seed using (Vertex; A; B; C; D)
open W using (Op; LABC; LADB; QAB; QBC; QCA; QAD; QDB; QBA)

data G : Type where
  g0 g1 g2 g3 g4 g5 g6 g7 g8 g9 g10 g11 : G

perm : G → Vertex → Vertex
perm g0 A = A
perm g0 B = B
perm g0 C = C
perm g0 D = D
perm g1 A = A
perm g1 B = C
perm g1 C = D
perm g1 D = B
perm g2 A = A
perm g2 B = D
perm g2 C = B
perm g2 D = C
perm g3 A = B
perm g3 B = A
perm g3 C = D
perm g3 D = C
perm g4 A = B
perm g4 B = C
perm g4 C = A
perm g4 D = D
perm g5 A = B
perm g5 B = D
perm g5 C = C
perm g5 D = A
perm g6 A = C
perm g6 B = A
perm g6 C = B
perm g6 D = D
perm g7 A = C
perm g7 B = B
perm g7 C = D
perm g7 D = A
perm g8 A = C
perm g8 B = D
perm g8 C = A
perm g8 D = B
perm g9 A = D
perm g9 B = A
perm g9 C = C
perm g9 D = B
perm g10 A = D
perm g10 B = B
perm g10 C = A
perm g10 D = C
perm g11 A = D
perm g11 B = C
perm g11 C = B
perm g11 D = A

inverseG leftABC leftADB : G → G
inverseG g0 = g0
inverseG g1 = g2
inverseG g2 = g1
inverseG g3 = g3
inverseG g4 = g6
inverseG g5 = g9
inverseG g6 = g4
inverseG g7 = g10
inverseG g8 = g8
inverseG g9 = g5
inverseG g10 = g7
inverseG g11 = g11
leftABC g0 = g4
leftABC g1 = g3
leftABC g2 = g5
leftABC g3 = g7
leftABC g4 = g6
leftABC g5 = g8
leftABC g6 = g0
leftABC g7 = g1
leftABC g8 = g2
leftABC g9 = g10
leftABC g10 = g11
leftABC g11 = g9
leftADB g0 = g9
leftADB g1 = g11
leftADB g2 = g10
leftADB g3 = g2
leftADB g4 = g1
leftADB g5 = g0
leftADB g6 = g8
leftADB g7 = g6
leftADB g8 = g7
leftADB g9 = g5
leftADB g10 = g3
leftADB g11 = g4

right : (g : G) (v : Vertex) → perm g (perm (inverseG g) v) ≡ v
right g0 A = refl
right g0 B = refl
right g0 C = refl
right g0 D = refl
right g1 A = refl
right g1 B = refl
right g1 C = refl
right g1 D = refl
right g2 A = refl
right g2 B = refl
right g2 C = refl
right g2 D = refl
right g3 A = refl
right g3 B = refl
right g3 C = refl
right g3 D = refl
right g4 A = refl
right g4 B = refl
right g4 C = refl
right g4 D = refl
right g5 A = refl
right g5 B = refl
right g5 C = refl
right g5 D = refl
right g6 A = refl
right g6 B = refl
right g6 C = refl
right g6 D = refl
right g7 A = refl
right g7 B = refl
right g7 C = refl
right g7 D = refl
right g8 A = refl
right g8 B = refl
right g8 C = refl
right g8 D = refl
right g9 A = refl
right g9 B = refl
right g9 C = refl
right g9 D = refl
right g10 A = refl
right g10 B = refl
right g10 C = refl
right g10 D = refl
right g11 A = refl
right g11 B = refl
right g11 C = refl
right g11 D = refl

left : (g : G) (v : Vertex) → perm (inverseG g) (perm g v) ≡ v
left g0 A = refl
left g0 B = refl
left g0 C = refl
left g0 D = refl
left g1 A = refl
left g1 B = refl
left g1 C = refl
left g1 D = refl
left g2 A = refl
left g2 B = refl
left g2 C = refl
left g2 D = refl
left g3 A = refl
left g3 B = refl
left g3 C = refl
left g3 D = refl
left g4 A = refl
left g4 B = refl
left g4 C = refl
left g4 D = refl
left g5 A = refl
left g5 B = refl
left g5 C = refl
left g5 D = refl
left g6 A = refl
left g6 B = refl
left g6 C = refl
left g6 D = refl
left g7 A = refl
left g7 B = refl
left g7 C = refl
left g7 D = refl
left g8 A = refl
left g8 B = refl
left g8 C = refl
left g8 D = refl
left g9 A = refl
left g9 B = refl
left g9 C = refl
left g9 D = refl
left g10 A = refl
left g10 B = refl
left g10 C = refl
left g10 D = refl
left g11 A = refl
left g11 B = refl
left g11 C = refl
left g11 D = refl

equivalence : G → Vertex ≃ Vertex
equivalence g = isoToEquiv (iso (perm g) (perm (inverseG g)) (right g) (left g))

leftABC-value : (g : G) (v : Vertex) → perm (leftABC g) v ≡ Q.abc (perm g v)
leftABC-value g0 A = refl
leftABC-value g0 B = refl
leftABC-value g0 C = refl
leftABC-value g0 D = refl
leftABC-value g1 A = refl
leftABC-value g1 B = refl
leftABC-value g1 C = refl
leftABC-value g1 D = refl
leftABC-value g2 A = refl
leftABC-value g2 B = refl
leftABC-value g2 C = refl
leftABC-value g2 D = refl
leftABC-value g3 A = refl
leftABC-value g3 B = refl
leftABC-value g3 C = refl
leftABC-value g3 D = refl
leftABC-value g4 A = refl
leftABC-value g4 B = refl
leftABC-value g4 C = refl
leftABC-value g4 D = refl
leftABC-value g5 A = refl
leftABC-value g5 B = refl
leftABC-value g5 C = refl
leftABC-value g5 D = refl
leftABC-value g6 A = refl
leftABC-value g6 B = refl
leftABC-value g6 C = refl
leftABC-value g6 D = refl
leftABC-value g7 A = refl
leftABC-value g7 B = refl
leftABC-value g7 C = refl
leftABC-value g7 D = refl
leftABC-value g8 A = refl
leftABC-value g8 B = refl
leftABC-value g8 C = refl
leftABC-value g8 D = refl
leftABC-value g9 A = refl
leftABC-value g9 B = refl
leftABC-value g9 C = refl
leftABC-value g9 D = refl
leftABC-value g10 A = refl
leftABC-value g10 B = refl
leftABC-value g10 C = refl
leftABC-value g10 D = refl
leftABC-value g11 A = refl
leftABC-value g11 B = refl
leftABC-value g11 C = refl
leftABC-value g11 D = refl
leftABC-path : (g : G) → equivalence (leftABC g) ≡ compEquiv (equivalence g) Q.ABC
leftABC-path g = equivEq (funExt (leftABC-value g))

leftADB-value : (g : G) (v : Vertex) → perm (leftADB g) v ≡ Q.adb (perm g v)
leftADB-value g0 A = refl
leftADB-value g0 B = refl
leftADB-value g0 C = refl
leftADB-value g0 D = refl
leftADB-value g1 A = refl
leftADB-value g1 B = refl
leftADB-value g1 C = refl
leftADB-value g1 D = refl
leftADB-value g2 A = refl
leftADB-value g2 B = refl
leftADB-value g2 C = refl
leftADB-value g2 D = refl
leftADB-value g3 A = refl
leftADB-value g3 B = refl
leftADB-value g3 C = refl
leftADB-value g3 D = refl
leftADB-value g4 A = refl
leftADB-value g4 B = refl
leftADB-value g4 C = refl
leftADB-value g4 D = refl
leftADB-value g5 A = refl
leftADB-value g5 B = refl
leftADB-value g5 C = refl
leftADB-value g5 D = refl
leftADB-value g6 A = refl
leftADB-value g6 B = refl
leftADB-value g6 C = refl
leftADB-value g6 D = refl
leftADB-value g7 A = refl
leftADB-value g7 B = refl
leftADB-value g7 C = refl
leftADB-value g7 D = refl
leftADB-value g8 A = refl
leftADB-value g8 B = refl
leftADB-value g8 C = refl
leftADB-value g8 D = refl
leftADB-value g9 A = refl
leftADB-value g9 B = refl
leftADB-value g9 C = refl
leftADB-value g9 D = refl
leftADB-value g10 A = refl
leftADB-value g10 B = refl
leftADB-value g10 C = refl
leftADB-value g10 D = refl
leftADB-value g11 A = refl
leftADB-value g11 B = refl
leftADB-value g11 C = refl
leftADB-value g11 D = refl
leftADB-path : (g : G) → equivalence (leftADB g) ≡ compEquiv (equivalence g) Q.ADB
leftADB-path g = equivEq (funExt (leftADB-value g))

State : Type
State = G × Bool

embed : State → R.Carrier
embed (g , b) = equivalence g , b

step : Op → State → State
step LABC (g , b) = leftABC g , b
step LADB (g , b) = leftADB g , b
step QAB (g , bit) = g , R.toggle (Q.equal (perm g A) B) bit
step QBC (g , bit) = g , R.toggle (Q.equal (perm g B) C) bit
step QCA (g , bit) = g , R.toggle (Q.equal (perm g C) A) bit
step QAD (g , bit) = g , R.toggle (Q.equal (perm g A) D) bit
step QDB (g , bit) = g , R.toggle (Q.equal (perm g D) B) bit
step QBA (g , bit) = g , R.toggle (Q.equal (perm g B) A) bit

step-binding : (o : Op) (s : State) → embed (step o s) ≡ W.native-step o (embed s)
step-binding LABC (g , b) = cong (λ e → e , b) (leftABC-path g)
step-binding LADB (g , b) = cong (λ e → e , b) (leftADB-path g)
step-binding QAB (g , bit) = refl
step-binding QBC (g , bit) = refl
step-binding QCA (g , bit) = refl
step-binding QAD (g , bit) = refl
step-binding QDB (g , bit) = refl
step-binding QBA (g , bit) = refl

run : List Op → State → State
run [] s = s
run (o ∷ os) s = run os (step o s)

all-word-binding : (os : List Op) (s : State) → embed (run os s) ≡ W.native-run os (embed s)
all-word-binding [] s = refl
all-word-binding (o ∷ os) s = all-word-binding os (step o s) ∙ cong (W.native-run os) (step-binding o s)

record-reading : (os : List Op) (s : State) → snd (run os s) ≡ snd (W.native-run os (embed s))
record-reading os s = cong snd (all-word-binding os s)

access : G → List Op
access g0 = []
access g1 = LABC ∷ LADB ∷ []
access g2 = LABC ∷ LABC ∷ LADB ∷ LABC ∷ []
access g3 = LABC ∷ LADB ∷ LABC ∷ []
access g4 = LABC ∷ []
access g5 = LADB ∷ LADB ∷ []
access g6 = LABC ∷ LABC ∷ []
access g7 = LABC ∷ LABC ∷ LADB ∷ LADB ∷ []
access g8 = LABC ∷ LABC ∷ LADB ∷ []
access g9 = LADB ∷ []
access g10 = LADB ∷ LABC ∷ []
access g11 = LABC ∷ LADB ∷ LADB ∷ []

access-correct : (g : G) → run (access g) (g0 , false) ≡ (g , false)
access-correct g0 = refl
access-correct g1 = refl
access-correct g2 = refl
access-correct g3 = refl
access-correct g4 = refl
access-correct g5 = refl
access-correct g6 = refl
access-correct g7 = refl
access-correct g8 = refl
access-correct g9 = refl
access-correct g10 = refl
access-correct g11 = refl
