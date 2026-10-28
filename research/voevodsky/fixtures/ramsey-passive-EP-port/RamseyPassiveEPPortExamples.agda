{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPassiveEPPortExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Relation.Nullary using (Dec; yes; no)
open import Cubical.Data.Empty.Base using (⊥)
import Cubical.Data.Empty as Empty
open import Agda.Builtin.String using (String)
open import RamseySingleFrameFaces
open import RamseyRequestedPort
open import RamseyPassiveEPPort
data Chart : Type where
  q0 q1 q2 q3 q4 q5 q6 q7 q8 q9 q10 q11 q12 q13 q14 q15 q16 q17 q18 q19 q20 q21 q22 q23 : Chart
role : Chart → Vertex → ℕ
role q0 c0 = 1
role q0 m0 = 0
role q0 c1 = 1
role q0 m1 = 0
role q1 c0 = 1
role q1 m0 = 0
role q1 c1 = 0
role q1 m1 = 1
role q2 c0 = 1
role q2 m0 = 1
role q2 c1 = 0
role q2 m1 = 0
role q3 c0 = 1
role q3 m0 = 0
role q3 c1 = 0
role q3 m1 = 1
role q4 c0 = 1
role q4 m0 = 1
role q4 c1 = 0
role q4 m1 = 0
role q5 c0 = 1
role q5 m0 = 0
role q5 c1 = 1
role q5 m1 = 0
role q6 c0 = 0
role q6 m0 = 1
role q6 c1 = 1
role q6 m1 = 0
role q7 c0 = 0
role q7 m0 = 1
role q7 c1 = 0
role q7 m1 = 1
role q8 c0 = 1
role q8 m0 = 1
role q8 c1 = 0
role q8 m1 = 0
role q9 c0 = 0
role q9 m0 = 1
role q9 c1 = 0
role q9 m1 = 1
role q10 c0 = 1
role q10 m0 = 1
role q10 c1 = 0
role q10 m1 = 0
role q11 c0 = 0
role q11 m0 = 1
role q11 c1 = 1
role q11 m1 = 0
role q12 c0 = 0
role q12 m0 = 1
role q12 c1 = 1
role q12 m1 = 0
role q13 c0 = 0
role q13 m0 = 0
role q13 c1 = 1
role q13 m1 = 1
role q14 c0 = 1
role q14 m0 = 0
role q14 c1 = 1
role q14 m1 = 0
role q15 c0 = 0
role q15 m0 = 0
role q15 c1 = 1
role q15 m1 = 1
role q16 c0 = 1
role q16 m0 = 0
role q16 c1 = 1
role q16 m1 = 0
role q17 c0 = 0
role q17 m0 = 1
role q17 c1 = 1
role q17 m1 = 0
role q18 c0 = 0
role q18 m0 = 1
role q18 c1 = 0
role q18 m1 = 1
role q19 c0 = 0
role q19 m0 = 0
role q19 c1 = 1
role q19 m1 = 1
role q20 c0 = 1
role q20 m0 = 0
role q20 c1 = 0
role q20 m1 = 1
role q21 c0 = 0
role q21 m0 = 0
role q21 c1 = 1
role q21 m1 = 1
role q22 c0 = 1
role q22 m0 = 0
role q22 c1 = 0
role q22 m1 = 1
role q23 c0 = 0
role q23 m0 = 1
role q23 c1 = 0
role q23 m1 = 1
Permit : Chart → Vertex → Type
Permit c f = count (λ i → role c (face f i)) ≡ 2
packet : (c : Chart) (f : Vertex) → Permit c f → String
packet q0 c0 p = Empty.rec (one-not-two p)
packet q0 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-1\",\"species\":\"proton\"},\"packet\":{\"chart\":1,\"id\":1,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":0,\"face\":1,\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"id\":0,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":1,\"target\":2},\"originLift\":2,\"prefix\":[],\"priorChart\":7,\"priorFace\":1,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-1\",\"species\":\"proton\"},\"packet\":{\"chart\":1,\"id\":1,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":2,\"id\":\"chart-2\",\"species\":\"neutron\"},\"packet\":{\"chart\":2,\"id\":2,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q0 c1 p = Empty.rec (one-not-two p)
packet q0 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-1\",\"species\":\"proton\"},\"packet\":{\"chart\":1,\"id\":1,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":0,\"face\":3,\"operation\":{\"face\":[\"0,0,1,0\",\"0,1,0,0\",\"1,0,0,0\"],\"id\":2,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":3,\"target\":4},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":1,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":1,\"target\":3}],\"priorChart\":7,\"priorFace\":3,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-3\",\"species\":\"proton\"},\"packet\":{\"chart\":3,\"id\":3,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":3,\"id\":\"chart-4\",\"species\":\"neutron\"},\"packet\":{\"chart\":4,\"id\":4,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q1 c0 p = Empty.rec (one-not-two p)
packet q1 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-11\",\"species\":\"proton\"},\"packet\":{\"chart\":11,\"id\":12,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":1,\"face\":1,\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"id\":10,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":12,\"target\":13},\"originLift\":2,\"prefix\":[],\"priorChart\":6,\"priorFace\":1,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-11\",\"species\":\"proton\"},\"packet\":{\"chart\":11,\"id\":12,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":2,\"id\":\"chart-12\",\"species\":\"neutron\"},\"packet\":{\"chart\":12,\"id\":13,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q1 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-11\",\"species\":\"proton\"},\"packet\":{\"chart\":11,\"id\":12,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":1,\"face\":2,\"operation\":{\"face\":[\"0,0,0,1\",\"0,1,0,0\",\"1,0,0,0\"],\"id\":12,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":14,\"target\":15},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":11,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":12,\"target\":14}],\"priorChart\":6,\"priorFace\":2,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-13\",\"species\":\"proton\"},\"packet\":{\"chart\":13,\"id\":14,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":4,\"id\":\"chart-14\",\"species\":\"neutron\"},\"packet\":{\"chart\":14,\"id\":15,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q1 m1 p = Empty.rec (one-not-two p)
packet q2 c0 p = Empty.rec (one-not-two p)
packet q2 m0 p = Empty.rec (one-not-two p)
packet q2 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-20\",\"species\":\"proton\"},\"packet\":{\"chart\":20,\"id\":22,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":2,\"face\":2,\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,0,1\",\"0,1,0,0\"],\"id\":18,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":22,\"target\":23},\"originLift\":2,\"prefix\":[],\"priorChart\":13,\"priorFace\":2,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-20\",\"species\":\"proton\"},\"packet\":{\"chart\":20,\"id\":22,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":4,\"id\":\"chart-21\",\"species\":\"neutron\"},\"packet\":{\"chart\":21,\"id\":23,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q2 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-20\",\"species\":\"proton\"},\"packet\":{\"chart\":20,\"id\":22,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":2,\"face\":3,\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,1,0\",\"1,0,0,0\"],\"id\":20,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":24,\"target\":25},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":19,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":22,\"target\":24}],\"priorChart\":13,\"priorFace\":3,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-22\",\"species\":\"proton\"},\"packet\":{\"chart\":22,\"id\":24,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":3,\"id\":\"chart-23\",\"species\":\"neutron\"},\"packet\":{\"chart\":23,\"id\":25,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q3 c0 p = Empty.rec (one-not-two p)
packet q3 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-29\",\"species\":\"proton\"},\"packet\":{\"chart\":29,\"id\":32,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":3,\"face\":1,\"operation\":{\"face\":[\"0,0,0,1\",\"0,0,1,0\",\"1,0,0,0\"],\"id\":28,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":34,\"target\":35},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":27,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":32,\"target\":34}],\"priorChart\":12,\"priorFace\":1,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-31\",\"species\":\"proton\"},\"packet\":{\"chart\":31,\"id\":34,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":2,\"id\":\"chart-32\",\"species\":\"neutron\"},\"packet\":{\"chart\":32,\"id\":35,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q3 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-29\",\"species\":\"proton\"},\"packet\":{\"chart\":29,\"id\":32,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":3,\"face\":2,\"operation\":{\"face\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,0,1\"],\"id\":26,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":32,\"target\":33},\"originLift\":2,\"prefix\":[],\"priorChart\":12,\"priorFace\":2,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-29\",\"species\":\"proton\"},\"packet\":{\"chart\":29,\"id\":32,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":4,\"id\":\"chart-30\",\"species\":\"neutron\"},\"packet\":{\"chart\":30,\"id\":33,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q3 m1 p = Empty.rec (one-not-two p)
packet q4 c0 p = Empty.rec (one-not-two p)
packet q4 m0 p = Empty.rec (one-not-two p)
packet q4 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-38\",\"species\":\"proton\"},\"packet\":{\"chart\":38,\"id\":42,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":4,\"face\":2,\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,0,1\",\"1,0,0,0\"],\"id\":36,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":44,\"target\":45},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":35,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":42,\"target\":44}],\"priorChart\":19,\"priorFace\":2,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-40\",\"species\":\"proton\"},\"packet\":{\"chart\":40,\"id\":44,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":4,\"id\":\"chart-41\",\"species\":\"neutron\"},\"packet\":{\"chart\":41,\"id\":45,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q4 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-38\",\"species\":\"proton\"},\"packet\":{\"chart\":38,\"id\":42,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":4,\"face\":3,\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,1,0\",\"0,1,0,0\"],\"id\":34,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":42,\"target\":43},\"originLift\":2,\"prefix\":[],\"priorChart\":19,\"priorFace\":3,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-38\",\"species\":\"proton\"},\"packet\":{\"chart\":38,\"id\":42,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":3,\"id\":\"chart-39\",\"species\":\"neutron\"},\"packet\":{\"chart\":39,\"id\":43,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q5 c0 p = Empty.rec (one-not-two p)
packet q5 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-47\",\"species\":\"proton\"},\"packet\":{\"chart\":47,\"id\":52,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":5,\"face\":1,\"operation\":{\"face\":[\"0,0,1,0\",\"0,0,0,1\",\"1,0,0,0\"],\"id\":44,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":54,\"target\":55},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":43,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":52,\"target\":54}],\"priorChart\":18,\"priorFace\":1,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-49\",\"species\":\"proton\"},\"packet\":{\"chart\":49,\"id\":54,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":2,\"id\":\"chart-50\",\"species\":\"neutron\"},\"packet\":{\"chart\":50,\"id\":55,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q5 c1 p = Empty.rec (one-not-two p)
packet q5 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-47\",\"species\":\"proton\"},\"packet\":{\"chart\":47,\"id\":52,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":5,\"face\":3,\"operation\":{\"face\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\"],\"id\":42,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":52,\"target\":53},\"originLift\":2,\"prefix\":[],\"priorChart\":18,\"priorFace\":3,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-47\",\"species\":\"proton\"},\"packet\":{\"chart\":47,\"id\":52,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":3,\"id\":\"chart-48\",\"species\":\"neutron\"},\"packet\":{\"chart\":48,\"id\":53,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q6 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-15\",\"species\":\"proton\"},\"packet\":{\"chart\":15,\"id\":64,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":6,\"face\":0,\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"id\":52,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":64,\"target\":65},\"originLift\":2,\"prefix\":[],\"priorChart\":1,\"priorFace\":0,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-15\",\"species\":\"proton\"},\"packet\":{\"chart\":15,\"id\":64,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":1,\"id\":\"chart-16\",\"species\":\"neutron\"},\"packet\":{\"chart\":16,\"id\":65,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q6 m0 p = Empty.rec (one-not-two p)
packet q6 c1 p = Empty.rec (one-not-two p)
packet q6 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-15\",\"species\":\"proton\"},\"packet\":{\"chart\":15,\"id\":64,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":6,\"face\":3,\"operation\":{\"face\":[\"0,0,1,0\",\"1,0,0,0\",\"0,1,0,0\"],\"id\":54,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":66,\"target\":67},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":53,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":64,\"target\":66}],\"priorChart\":1,\"priorFace\":3,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-17\",\"species\":\"proton\"},\"packet\":{\"chart\":17,\"id\":66,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":3,\"id\":\"chart-58\",\"species\":\"neutron\"},\"packet\":{\"chart\":58,\"id\":67,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q7 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-0\",\"species\":\"proton\"},\"packet\":{\"chart\":0,\"id\":74,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":7,\"face\":0,\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"id\":60,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":74,\"target\":75},\"originLift\":2,\"prefix\":[],\"priorChart\":0,\"priorFace\":0,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-0\",\"species\":\"proton\"},\"packet\":{\"chart\":0,\"id\":74,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":1,\"id\":\"chart-5\",\"species\":\"neutron\"},\"packet\":{\"chart\":5,\"id\":75,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q7 m0 p = Empty.rec (one-not-two p)
packet q7 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-0\",\"species\":\"proton\"},\"packet\":{\"chart\":0,\"id\":74,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":7,\"face\":2,\"operation\":{\"face\":[\"0,0,0,1\",\"1,0,0,0\",\"0,1,0,0\"],\"id\":62,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":76,\"target\":77},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":61,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":74,\"target\":76}],\"priorChart\":0,\"priorFace\":2,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-6\",\"species\":\"proton\"},\"packet\":{\"chart\":6,\"id\":76,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":4,\"id\":\"chart-61\",\"species\":\"neutron\"},\"packet\":{\"chart\":61,\"id\":77,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q7 m1 p = Empty.rec (one-not-two p)
packet q8 c0 p = Empty.rec (one-not-two p)
packet q8 m0 p = Empty.rec (one-not-two p)
packet q8 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-40\",\"species\":\"proton\"},\"packet\":{\"chart\":40,\"id\":86,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":8,\"face\":2,\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,0,1\",\"1,0,0,0\"],\"id\":70,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":86,\"target\":87},\"originLift\":2,\"prefix\":[],\"priorChart\":15,\"priorFace\":2,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-40\",\"species\":\"proton\"},\"packet\":{\"chart\":40,\"id\":86,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":4,\"id\":\"chart-41\",\"species\":\"neutron\"},\"packet\":{\"chart\":41,\"id\":87,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q8 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-40\",\"species\":\"proton\"},\"packet\":{\"chart\":40,\"id\":86,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":8,\"face\":3,\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,1,0\",\"0,1,0,0\"],\"id\":72,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":88,\"target\":89},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":71,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":86,\"target\":88}],\"priorChart\":15,\"priorFace\":3,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-38\",\"species\":\"proton\"},\"packet\":{\"chart\":38,\"id\":88,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":3,\"id\":\"chart-39\",\"species\":\"neutron\"},\"packet\":{\"chart\":39,\"id\":89,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q9 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-53\",\"species\":\"proton\"},\"packet\":{\"chart\":53,\"id\":96,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":9,\"face\":0,\"operation\":{\"face\":[\"0,0,0,1\",\"0,0,1,0\",\"0,1,0,0\"],\"id\":80,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":98,\"target\":99},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":79,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":96,\"target\":98}],\"priorChart\":14,\"priorFace\":0,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-51\",\"species\":\"proton\"},\"packet\":{\"chart\":51,\"id\":98,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":1,\"id\":\"chart-52\",\"species\":\"neutron\"},\"packet\":{\"chart\":52,\"id\":99,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q9 m0 p = Empty.rec (one-not-two p)
packet q9 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-53\",\"species\":\"proton\"},\"packet\":{\"chart\":53,\"id\":96,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":9,\"face\":2,\"operation\":{\"face\":[\"0,1,0,0\",\"1,0,0,0\",\"0,0,0,1\"],\"id\":78,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":96,\"target\":97},\"originLift\":2,\"prefix\":[],\"priorChart\":14,\"priorFace\":2,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-53\",\"species\":\"proton\"},\"packet\":{\"chart\":53,\"id\":96,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":4,\"id\":\"chart-69\",\"species\":\"neutron\"},\"packet\":{\"chart\":69,\"id\":97,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q9 m1 p = Empty.rec (one-not-two p)
packet q10 c0 p = Empty.rec (one-not-two p)
packet q10 m0 p = Empty.rec (one-not-two p)
packet q10 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-22\",\"species\":\"proton\"},\"packet\":{\"chart\":22,\"id\":108,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":10,\"face\":2,\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,0,1\",\"0,1,0,0\"],\"id\":90,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":110,\"target\":111},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":89,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":108,\"target\":110}],\"priorChart\":21,\"priorFace\":2,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-20\",\"species\":\"proton\"},\"packet\":{\"chart\":20,\"id\":110,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":4,\"id\":\"chart-21\",\"species\":\"neutron\"},\"packet\":{\"chart\":21,\"id\":111,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q10 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-22\",\"species\":\"proton\"},\"packet\":{\"chart\":22,\"id\":108,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":10,\"face\":3,\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,1,0\",\"1,0,0,0\"],\"id\":88,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":108,\"target\":109},\"originLift\":2,\"prefix\":[],\"priorChart\":21,\"priorFace\":3,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-22\",\"species\":\"proton\"},\"packet\":{\"chart\":22,\"id\":108,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":3,\"id\":\"chart-23\",\"species\":\"neutron\"},\"packet\":{\"chart\":23,\"id\":109,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q11 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-35\",\"species\":\"proton\"},\"packet\":{\"chart\":35,\"id\":118,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":11,\"face\":0,\"operation\":{\"face\":[\"0,0,1,0\",\"0,0,0,1\",\"0,1,0,0\"],\"id\":98,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":120,\"target\":121},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":97,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":118,\"target\":120}],\"priorChart\":20,\"priorFace\":0,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-33\",\"species\":\"proton\"},\"packet\":{\"chart\":33,\"id\":120,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":1,\"id\":\"chart-34\",\"species\":\"neutron\"},\"packet\":{\"chart\":34,\"id\":121,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q11 m0 p = Empty.rec (one-not-two p)
packet q11 c1 p = Empty.rec (one-not-two p)
packet q11 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-35\",\"species\":\"proton\"},\"packet\":{\"chart\":35,\"id\":118,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":11,\"face\":3,\"operation\":{\"face\":[\"0,1,0,0\",\"1,0,0,0\",\"0,0,1,0\"],\"id\":96,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":118,\"target\":119},\"originLift\":2,\"prefix\":[],\"priorChart\":20,\"priorFace\":3,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-35\",\"species\":\"proton\"},\"packet\":{\"chart\":35,\"id\":118,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":3,\"id\":\"chart-77\",\"species\":\"neutron\"},\"packet\":{\"chart\":77,\"id\":119,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q12 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-33\",\"species\":\"proton\"},\"packet\":{\"chart\":33,\"id\":128,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":12,\"face\":0,\"operation\":{\"face\":[\"0,0,1,0\",\"0,0,0,1\",\"0,1,0,0\"],\"id\":104,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":128,\"target\":129},\"originLift\":2,\"prefix\":[],\"priorChart\":3,\"priorFace\":0,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-33\",\"species\":\"proton\"},\"packet\":{\"chart\":33,\"id\":128,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":1,\"id\":\"chart-34\",\"species\":\"neutron\"},\"packet\":{\"chart\":34,\"id\":129,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q12 m0 p = Empty.rec (one-not-two p)
packet q12 c1 p = Empty.rec (one-not-two p)
packet q12 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-33\",\"species\":\"proton\"},\"packet\":{\"chart\":33,\"id\":128,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":12,\"face\":3,\"operation\":{\"face\":[\"0,1,0,0\",\"1,0,0,0\",\"0,0,1,0\"],\"id\":106,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":130,\"target\":131},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":105,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":128,\"target\":130}],\"priorChart\":3,\"priorFace\":3,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-35\",\"species\":\"proton\"},\"packet\":{\"chart\":35,\"id\":130,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":3,\"id\":\"chart-77\",\"species\":\"neutron\"},\"packet\":{\"chart\":77,\"id\":131,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q13 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-24\",\"species\":\"proton\"},\"packet\":{\"chart\":24,\"id\":138,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":13,\"face\":0,\"operation\":{\"face\":[\"0,0,1,0\",\"0,1,0,0\",\"0,0,0,1\"],\"id\":112,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":138,\"target\":139},\"originLift\":2,\"prefix\":[],\"priorChart\":2,\"priorFace\":0,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-24\",\"species\":\"proton\"},\"packet\":{\"chart\":24,\"id\":138,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":1,\"id\":\"chart-25\",\"species\":\"neutron\"},\"packet\":{\"chart\":25,\"id\":139,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q13 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-24\",\"species\":\"proton\"},\"packet\":{\"chart\":24,\"id\":138,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":13,\"face\":1,\"operation\":{\"face\":[\"0,0,0,1\",\"1,0,0,0\",\"0,0,1,0\"],\"id\":114,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":140,\"target\":141},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":113,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":138,\"target\":140}],\"priorChart\":2,\"priorFace\":1,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-26\",\"species\":\"proton\"},\"packet\":{\"chart\":26,\"id\":140,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":2,\"id\":\"chart-74\",\"species\":\"neutron\"},\"packet\":{\"chart\":74,\"id\":141,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q13 c1 p = Empty.rec (one-not-two p)
packet q13 m1 p = Empty.rec (one-not-two p)
packet q14 c0 p = Empty.rec (one-not-two p)
packet q14 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-49\",\"species\":\"proton\"},\"packet\":{\"chart\":49,\"id\":148,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":14,\"face\":1,\"operation\":{\"face\":[\"0,0,1,0\",\"0,0,0,1\",\"1,0,0,0\"],\"id\":120,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":148,\"target\":149},\"originLift\":2,\"prefix\":[],\"priorChart\":9,\"priorFace\":1,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-49\",\"species\":\"proton\"},\"packet\":{\"chart\":49,\"id\":148,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":2,\"id\":\"chart-50\",\"species\":\"neutron\"},\"packet\":{\"chart\":50,\"id\":149,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q14 c1 p = Empty.rec (one-not-two p)
packet q14 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-49\",\"species\":\"proton\"},\"packet\":{\"chart\":49,\"id\":148,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":14,\"face\":3,\"operation\":{\"face\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\"],\"id\":122,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":150,\"target\":151},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":121,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":148,\"target\":150}],\"priorChart\":9,\"priorFace\":3,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-47\",\"species\":\"proton\"},\"packet\":{\"chart\":47,\"id\":150,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":3,\"id\":\"chart-48\",\"species\":\"neutron\"},\"packet\":{\"chart\":48,\"id\":151,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q15 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-44\",\"species\":\"proton\"},\"packet\":{\"chart\":44,\"id\":160,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":15,\"face\":0,\"operation\":{\"face\":[\"0,0,0,1\",\"0,1,0,0\",\"0,0,1,0\"],\"id\":132,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":162,\"target\":163},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":131,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":160,\"target\":162}],\"priorChart\":8,\"priorFace\":0,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-42\",\"species\":\"proton\"},\"packet\":{\"chart\":42,\"id\":162,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":1,\"id\":\"chart-43\",\"species\":\"neutron\"},\"packet\":{\"chart\":43,\"id\":163,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q15 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-44\",\"species\":\"proton\"},\"packet\":{\"chart\":44,\"id\":160,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":15,\"face\":1,\"operation\":{\"face\":[\"0,0,1,0\",\"1,0,0,0\",\"0,0,0,1\"],\"id\":130,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":160,\"target\":161},\"originLift\":2,\"prefix\":[],\"priorChart\":8,\"priorFace\":1,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-44\",\"species\":\"proton\"},\"packet\":{\"chart\":44,\"id\":160,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":2,\"id\":\"chart-66\",\"species\":\"neutron\"},\"packet\":{\"chart\":66,\"id\":161,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q15 c1 p = Empty.rec (one-not-two p)
packet q15 m1 p = Empty.rec (one-not-two p)
packet q16 c0 p = Empty.rec (one-not-two p)
packet q16 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-3\",\"species\":\"proton\"},\"packet\":{\"chart\":3,\"id\":170,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":16,\"face\":1,\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"id\":140,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":172,\"target\":173},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":139,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":170,\"target\":172}],\"priorChart\":23,\"priorFace\":1,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-1\",\"species\":\"proton\"},\"packet\":{\"chart\":1,\"id\":172,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":2,\"id\":\"chart-2\",\"species\":\"neutron\"},\"packet\":{\"chart\":2,\"id\":173,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q16 c1 p = Empty.rec (one-not-two p)
packet q16 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-3\",\"species\":\"proton\"},\"packet\":{\"chart\":3,\"id\":170,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":16,\"face\":3,\"operation\":{\"face\":[\"0,0,1,0\",\"0,1,0,0\",\"1,0,0,0\"],\"id\":138,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":170,\"target\":171},\"originLift\":2,\"prefix\":[],\"priorChart\":23,\"priorFace\":3,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-3\",\"species\":\"proton\"},\"packet\":{\"chart\":3,\"id\":170,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":3,\"id\":\"chart-4\",\"species\":\"neutron\"},\"packet\":{\"chart\":4,\"id\":171,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q17 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-17\",\"species\":\"proton\"},\"packet\":{\"chart\":17,\"id\":182,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":17,\"face\":0,\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"id\":150,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":184,\"target\":185},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":149,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":182,\"target\":184}],\"priorChart\":22,\"priorFace\":0,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-15\",\"species\":\"proton\"},\"packet\":{\"chart\":15,\"id\":184,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":1,\"id\":\"chart-16\",\"species\":\"neutron\"},\"packet\":{\"chart\":16,\"id\":185,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q17 m0 p = Empty.rec (one-not-two p)
packet q17 c1 p = Empty.rec (one-not-two p)
packet q17 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-17\",\"species\":\"proton\"},\"packet\":{\"chart\":17,\"id\":182,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":17,\"face\":3,\"operation\":{\"face\":[\"0,0,1,0\",\"1,0,0,0\",\"0,1,0,0\"],\"id\":148,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":182,\"target\":183},\"originLift\":2,\"prefix\":[],\"priorChart\":22,\"priorFace\":3,\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-17\",\"species\":\"proton\"},\"packet\":{\"chart\":17,\"id\":182,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":3,\"id\":\"chart-58\",\"species\":\"neutron\"},\"packet\":{\"chart\":58,\"id\":183,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q18 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-51\",\"species\":\"proton\"},\"packet\":{\"chart\":51,\"id\":192,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":18,\"face\":0,\"operation\":{\"face\":[\"0,0,0,1\",\"0,0,1,0\",\"0,1,0,0\"],\"id\":156,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":192,\"target\":193},\"originLift\":2,\"prefix\":[],\"priorChart\":5,\"priorFace\":0,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-51\",\"species\":\"proton\"},\"packet\":{\"chart\":51,\"id\":192,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":1,\"id\":\"chart-52\",\"species\":\"neutron\"},\"packet\":{\"chart\":52,\"id\":193,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q18 m0 p = Empty.rec (one-not-two p)
packet q18 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-51\",\"species\":\"proton\"},\"packet\":{\"chart\":51,\"id\":192,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":18,\"face\":2,\"operation\":{\"face\":[\"0,1,0,0\",\"1,0,0,0\",\"0,0,0,1\"],\"id\":158,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":194,\"target\":195},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":157,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":192,\"target\":194}],\"priorChart\":5,\"priorFace\":2,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-53\",\"species\":\"proton\"},\"packet\":{\"chart\":53,\"id\":194,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":4,\"id\":\"chart-69\",\"species\":\"neutron\"},\"packet\":{\"chart\":69,\"id\":195,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q18 m1 p = Empty.rec (one-not-two p)
packet q19 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-42\",\"species\":\"proton\"},\"packet\":{\"chart\":42,\"id\":204,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":19,\"face\":0,\"operation\":{\"face\":[\"0,0,0,1\",\"0,1,0,0\",\"0,0,1,0\"],\"id\":166,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":204,\"target\":205},\"originLift\":2,\"prefix\":[],\"priorChart\":4,\"priorFace\":0,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-42\",\"species\":\"proton\"},\"packet\":{\"chart\":42,\"id\":204,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":1,\"id\":\"chart-43\",\"species\":\"neutron\"},\"packet\":{\"chart\":43,\"id\":205,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q19 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-42\",\"species\":\"proton\"},\"packet\":{\"chart\":42,\"id\":204,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":19,\"face\":1,\"operation\":{\"face\":[\"0,0,1,0\",\"1,0,0,0\",\"0,0,0,1\"],\"id\":168,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":206,\"target\":207},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":167,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":204,\"target\":206}],\"priorChart\":4,\"priorFace\":1,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-44\",\"species\":\"proton\"},\"packet\":{\"chart\":44,\"id\":206,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":2,\"id\":\"chart-66\",\"species\":\"neutron\"},\"packet\":{\"chart\":66,\"id\":207,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q19 c1 p = Empty.rec (one-not-two p)
packet q19 m1 p = Empty.rec (one-not-two p)
packet q20 c0 p = Empty.rec (one-not-two p)
packet q20 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-31\",\"species\":\"proton\"},\"packet\":{\"chart\":31,\"id\":214,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":20,\"face\":1,\"operation\":{\"face\":[\"0,0,0,1\",\"0,0,1,0\",\"1,0,0,0\"],\"id\":174,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":214,\"target\":215},\"originLift\":2,\"prefix\":[],\"priorChart\":11,\"priorFace\":1,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-31\",\"species\":\"proton\"},\"packet\":{\"chart\":31,\"id\":214,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":2,\"id\":\"chart-32\",\"species\":\"neutron\"},\"packet\":{\"chart\":32,\"id\":215,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q20 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-31\",\"species\":\"proton\"},\"packet\":{\"chart\":31,\"id\":214,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":20,\"face\":2,\"operation\":{\"face\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,0,1\"],\"id\":176,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":216,\"target\":217},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":175,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":214,\"target\":216}],\"priorChart\":11,\"priorFace\":2,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-29\",\"species\":\"proton\"},\"packet\":{\"chart\":29,\"id\":216,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":4,\"id\":\"chart-30\",\"species\":\"neutron\"},\"packet\":{\"chart\":30,\"id\":217,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q20 m1 p = Empty.rec (one-not-two p)
packet q21 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-26\",\"species\":\"proton\"},\"packet\":{\"chart\":26,\"id\":224,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":21,\"face\":0,\"operation\":{\"face\":[\"0,0,1,0\",\"0,1,0,0\",\"0,0,0,1\"],\"id\":184,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":226,\"target\":227},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":183,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":224,\"target\":226}],\"priorChart\":10,\"priorFace\":0,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-24\",\"species\":\"proton\"},\"packet\":{\"chart\":24,\"id\":226,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":1,\"id\":\"chart-25\",\"species\":\"neutron\"},\"packet\":{\"chart\":25,\"id\":227,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q21 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-26\",\"species\":\"proton\"},\"packet\":{\"chart\":26,\"id\":224,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":21,\"face\":1,\"operation\":{\"face\":[\"0,0,0,1\",\"1,0,0,0\",\"0,0,1,0\"],\"id\":182,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":224,\"target\":225},\"originLift\":2,\"prefix\":[],\"priorChart\":10,\"priorFace\":1,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-26\",\"species\":\"proton\"},\"packet\":{\"chart\":26,\"id\":224,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":2,\"id\":\"chart-74\",\"species\":\"neutron\"},\"packet\":{\"chart\":74,\"id\":225,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q21 c1 p = Empty.rec (one-not-two p)
packet q21 m1 p = Empty.rec (one-not-two p)
packet q22 c0 p = Empty.rec (one-not-two p)
packet q22 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-13\",\"species\":\"proton\"},\"packet\":{\"chart\":13,\"id\":234,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":22,\"face\":1,\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"id\":192,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":236,\"target\":237},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":191,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":234,\"target\":236}],\"priorChart\":17,\"priorFace\":1,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-11\",\"species\":\"proton\"},\"packet\":{\"chart\":11,\"id\":236,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":2,\"id\":\"chart-12\",\"species\":\"neutron\"},\"packet\":{\"chart\":12,\"id\":237,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q22 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-13\",\"species\":\"proton\"},\"packet\":{\"chart\":13,\"id\":234,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":22,\"face\":2,\"operation\":{\"face\":[\"0,0,0,1\",\"0,1,0,0\",\"1,0,0,0\"],\"id\":190,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":234,\"target\":235},\"originLift\":2,\"prefix\":[],\"priorChart\":17,\"priorFace\":2,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-13\",\"species\":\"proton\"},\"packet\":{\"chart\":13,\"id\":234,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":4,\"id\":\"chart-14\",\"species\":\"neutron\"},\"packet\":{\"chart\":14,\"id\":235,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q22 m1 p = Empty.rec (one-not-two p)
packet q23 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-6\",\"species\":\"proton\"},\"packet\":{\"chart\":6,\"id\":244,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":23,\"face\":0,\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"id\":200,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":246,\"target\":247},\"originLift\":2,\"prefix\":[{\"face\":null,\"id\":199,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":244,\"target\":246}],\"priorChart\":16,\"priorFace\":0,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-0\",\"species\":\"proton\"},\"packet\":{\"chart\":0,\"id\":246,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":1,\"id\":\"chart-5\",\"species\":\"neutron\"},\"packet\":{\"chart\":5,\"id\":247,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet q23 m0 p = Empty.rec (one-not-two p)
packet q23 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-6\",\"species\":\"proton\"},\"packet\":{\"chart\":6,\"id\":244,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"chart\":23,\"face\":2,\"operation\":{\"face\":[\"0,0,0,1\",\"1,0,0,0\",\"0,1,0,0\"],\"id\":198,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":244,\"target\":245},\"originLift\":2,\"prefix\":[],\"priorChart\":16,\"priorFace\":2,\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-6\",\"species\":\"proton\"},\"packet\":{\"chart\":6,\"id\":244,\"origin\":2,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":4,\"id\":\"chart-61\",\"species\":\"neutron\"},\"packet\":{\"chart\":61,\"id\":245,\"origin\":2,\"permutation\":[3,1,2,0,4]}}}"
packet q23 m1 p = Empty.rec (one-not-two p)
electron : Chart → String
electron q0 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-10@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"-1,0,1,1\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,0,0\",\"M0\":\"-1,1,0,1\",\"M1\":\"0,0,1,0\",\"M2\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-10\",\"species\":\"electron\"},\"packet\":{\"chart\":10,\"id\":11,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q1 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-19@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"-1,0,1,1\",\"C1\":\"0,0,1,0\",\"C2\":\"0,1,0,0\",\"M0\":\"-1,1,0,1\",\"M1\":\"0,0,0,1\",\"M2\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-19\",\"species\":\"electron\"},\"packet\":{\"chart\":19,\"id\":21,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q2 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-28@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,-1,1\",\"C1\":\"0,0,0,1\",\"C2\":\"0,0,1,0\",\"M0\":\"-1,1,0,1\",\"M1\":\"0,1,0,0\",\"M2\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-28\",\"species\":\"electron\"},\"packet\":{\"chart\":28,\"id\":31,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q3 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-37@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,-1,1\",\"C1\":\"0,1,0,0\",\"C2\":\"0,0,1,0\",\"M0\":\"-1,1,0,1\",\"M1\":\"0,0,0,1\",\"M2\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-37\",\"species\":\"electron\"},\"packet\":{\"chart\":37,\"id\":41,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q4 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-46@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"-1,1,1,0\",\"C1\":\"0,0,1,0\",\"C2\":\"0,0,0,1\",\"M0\":\"-1,1,0,1\",\"M1\":\"0,1,0,0\",\"M2\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-46\",\"species\":\"electron\"},\"packet\":{\"chart\":46,\"id\":51,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q5 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-57@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"-1,1,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,0,0,1\",\"M0\":\"-1,1,0,1\",\"M1\":\"0,0,1,0\",\"M2\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-57\",\"species\":\"electron\"},\"packet\":{\"chart\":57,\"id\":63,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q6 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-60@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,-1,1,1\",\"C1\":\"0,0,0,1\",\"C2\":\"1,0,0,0\",\"M0\":\"1,-1,1,0\",\"M1\":\"0,0,1,0\",\"M2\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-60\",\"species\":\"electron\"},\"packet\":{\"chart\":60,\"id\":73,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q7 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-65@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,-1,1,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,0,0\",\"M0\":\"1,-1,1,0\",\"M1\":\"0,0,0,1\",\"M2\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-65\",\"species\":\"electron\"},\"packet\":{\"chart\":65,\"id\":85,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q8 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-68@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,-1,0,1\",\"C1\":\"0,0,0,1\",\"C2\":\"0,0,1,0\",\"M0\":\"1,-1,1,0\",\"M1\":\"1,0,0,0\",\"M2\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-68\",\"species\":\"electron\"},\"packet\":{\"chart\":68,\"id\":95,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q9 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-73@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,-1,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"0,0,1,0\",\"M0\":\"1,-1,1,0\",\"M1\":\"0,0,0,1\",\"M2\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-73\",\"species\":\"electron\"},\"packet\":{\"chart\":73,\"id\":107,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q10 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-76@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,1,-1\",\"C1\":\"0,0,1,0\",\"C2\":\"0,0,0,1\",\"M0\":\"1,-1,1,0\",\"M1\":\"1,0,0,0\",\"M2\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-76\",\"species\":\"electron\"},\"packet\":{\"chart\":76,\"id\":117,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q11 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-79@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,1,-1\",\"C1\":\"1,0,0,0\",\"C2\":\"0,0,0,1\",\"M0\":\"1,-1,1,0\",\"M1\":\"0,0,1,0\",\"M2\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-79\",\"species\":\"electron\"},\"packet\":{\"chart\":79,\"id\":127,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q12 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-81@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"-1,1,0,1\",\"C1\":\"0,0,0,1\",\"C2\":\"1,0,0,0\",\"M0\":\"0,1,-1,1\",\"M1\":\"0,1,0,0\",\"M2\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-81\",\"species\":\"electron\"},\"packet\":{\"chart\":81,\"id\":137,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q13 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-83@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"-1,1,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,0,0\",\"M0\":\"0,1,-1,1\",\"M1\":\"0,0,0,1\",\"M2\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-83\",\"species\":\"electron\"},\"packet\":{\"chart\":83,\"id\":147,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q14 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-87@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,-1,1\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,0,0\",\"M0\":\"0,1,-1,1\",\"M1\":\"1,0,0,0\",\"M2\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-87\",\"species\":\"electron\"},\"packet\":{\"chart\":87,\"id\":159,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q15 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-89@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,-1,1\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,0,0\",\"M0\":\"0,1,-1,1\",\"M1\":\"0,0,0,1\",\"M2\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-89\",\"species\":\"electron\"},\"packet\":{\"chart\":89,\"id\":169,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q16 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-93@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,1,-1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,0,0,1\",\"M0\":\"0,1,-1,1\",\"M1\":\"1,0,0,0\",\"M2\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-93\",\"species\":\"electron\"},\"packet\":{\"chart\":93,\"id\":181,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q17 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-95@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,1,-1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,0,0,1\",\"M0\":\"0,1,-1,1\",\"M1\":\"0,1,0,0\",\"M2\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-95\",\"species\":\"electron\"},\"packet\":{\"chart\":95,\"id\":191,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q18 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-99@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,1,-1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,0,0\",\"M0\":\"1,0,1,-1\",\"M1\":\"0,1,0,0\",\"M2\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-99\",\"species\":\"electron\"},\"packet\":{\"chart\":99,\"id\":203,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q19 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-101@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,1,-1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,0,0\",\"M0\":\"1,0,1,-1\",\"M1\":\"0,0,1,0\",\"M2\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-101\",\"species\":\"electron\"},\"packet\":{\"chart\":101,\"id\":213,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q20 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-103@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,-1,1,0\",\"C1\":\"0,0,1,0\",\"C2\":\"0,1,0,0\",\"M0\":\"1,0,1,-1\",\"M1\":\"1,0,0,0\",\"M2\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-103\",\"species\":\"electron\"},\"packet\":{\"chart\":103,\"id\":223,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q21 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-105@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,-1,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,0,0\",\"M0\":\"1,0,1,-1\",\"M1\":\"0,0,1,0\",\"M2\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-105\",\"species\":\"electron\"},\"packet\":{\"chart\":105,\"id\":233,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q22 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-107@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,1,0,-1\",\"C1\":\"0,1,0,0\",\"C2\":\"0,0,1,0\",\"M0\":\"1,0,1,-1\",\"M1\":\"1,0,0,0\",\"M2\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-107\",\"species\":\"electron\"},\"packet\":{\"chart\":107,\"id\":243,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
electron q23 = "{\"frame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-111@0\",\"species\":\"electron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,1,0,-1\",\"C1\":\"1,0,0,0\",\"C2\":\"0,0,1,0\",\"M0\":\"1,0,1,-1\",\"M1\":\"0,1,0,0\",\"M2\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-111\",\"species\":\"electron\"},\"packet\":{\"chart\":111,\"id\":255,\"origin\":0,\"permutation\":[4,3,2,1,0]}}}"
decide : (c : Chart) (f : Vertex) → Dec (Permit c f)
decide q0 c0 = no one-not-two
decide q0 m0 = yes refl
decide q0 c1 = no one-not-two
decide q0 m1 = yes refl
decide q1 c0 = no one-not-two
decide q1 m0 = yes refl
decide q1 c1 = yes refl
decide q1 m1 = no one-not-two
decide q2 c0 = no one-not-two
decide q2 m0 = no one-not-two
decide q2 c1 = yes refl
decide q2 m1 = yes refl
decide q3 c0 = no one-not-two
decide q3 m0 = yes refl
decide q3 c1 = yes refl
decide q3 m1 = no one-not-two
decide q4 c0 = no one-not-two
decide q4 m0 = no one-not-two
decide q4 c1 = yes refl
decide q4 m1 = yes refl
decide q5 c0 = no one-not-two
decide q5 m0 = yes refl
decide q5 c1 = no one-not-two
decide q5 m1 = yes refl
decide q6 c0 = yes refl
decide q6 m0 = no one-not-two
decide q6 c1 = no one-not-two
decide q6 m1 = yes refl
decide q7 c0 = yes refl
decide q7 m0 = no one-not-two
decide q7 c1 = yes refl
decide q7 m1 = no one-not-two
decide q8 c0 = no one-not-two
decide q8 m0 = no one-not-two
decide q8 c1 = yes refl
decide q8 m1 = yes refl
decide q9 c0 = yes refl
decide q9 m0 = no one-not-two
decide q9 c1 = yes refl
decide q9 m1 = no one-not-two
decide q10 c0 = no one-not-two
decide q10 m0 = no one-not-two
decide q10 c1 = yes refl
decide q10 m1 = yes refl
decide q11 c0 = yes refl
decide q11 m0 = no one-not-two
decide q11 c1 = no one-not-two
decide q11 m1 = yes refl
decide q12 c0 = yes refl
decide q12 m0 = no one-not-two
decide q12 c1 = no one-not-two
decide q12 m1 = yes refl
decide q13 c0 = yes refl
decide q13 m0 = yes refl
decide q13 c1 = no one-not-two
decide q13 m1 = no one-not-two
decide q14 c0 = no one-not-two
decide q14 m0 = yes refl
decide q14 c1 = no one-not-two
decide q14 m1 = yes refl
decide q15 c0 = yes refl
decide q15 m0 = yes refl
decide q15 c1 = no one-not-two
decide q15 m1 = no one-not-two
decide q16 c0 = no one-not-two
decide q16 m0 = yes refl
decide q16 c1 = no one-not-two
decide q16 m1 = yes refl
decide q17 c0 = yes refl
decide q17 m0 = no one-not-two
decide q17 c1 = no one-not-two
decide q17 m1 = yes refl
decide q18 c0 = yes refl
decide q18 m0 = no one-not-two
decide q18 c1 = yes refl
decide q18 m1 = no one-not-two
decide q19 c0 = yes refl
decide q19 m0 = yes refl
decide q19 c1 = no one-not-two
decide q19 m1 = no one-not-two
decide q20 c0 = no one-not-two
decide q20 m0 = yes refl
decide q20 c1 = yes refl
decide q20 m1 = no one-not-two
decide q21 c0 = yes refl
decide q21 m0 = yes refl
decide q21 c1 = no one-not-two
decide q21 m1 = no one-not-two
decide q22 c0 = no one-not-two
decide q22 m0 = yes refl
decide q22 c1 = yes refl
decide q22 m1 = no one-not-two
decide q23 c0 = yes refl
decide q23 m0 = no one-not-two
decide q23 c1 = yes refl
decide q23 m1 = no one-not-two
module R = Request Chart Vertex Permit packet decide
module A = Passive Chart Vertex Permit packet electron
refuse-0-0 : R.isAccepted (R.run q7 q0 c0 refl) ≡ false
refuse-0-0 = refl
accept-0-1 : R.isAccepted (R.run q0 q0 m0 refl) ≡ true
accept-0-1 = refl
native-0-1 : A.Both.R.Resolve (A.T.encode (A.context q0 m0 refl))
native-0-1 = A.native q0 m0 refl
needs-target-0-1 : A.Only.Good (A.context q0 m0 refl) → ⊥
needs-target-0-1 = A.needs-target q0 m0 refl
refuse-0-2 : R.isAccepted (R.run q7 q0 c1 refl) ≡ false
refuse-0-2 = refl
accept-0-3 : R.isAccepted (R.run q0 q0 m1 refl) ≡ true
accept-0-3 = refl
native-0-3 : A.Both.R.Resolve (A.T.encode (A.context q0 m1 refl))
native-0-3 = A.native q0 m1 refl
needs-target-0-3 : A.Only.Good (A.context q0 m1 refl) → ⊥
needs-target-0-3 = A.needs-target q0 m1 refl
refuse-1-0 : R.isAccepted (R.run q6 q1 c0 refl) ≡ false
refuse-1-0 = refl
accept-1-1 : R.isAccepted (R.run q1 q1 m0 refl) ≡ true
accept-1-1 = refl
native-1-1 : A.Both.R.Resolve (A.T.encode (A.context q1 m0 refl))
native-1-1 = A.native q1 m0 refl
needs-target-1-1 : A.Only.Good (A.context q1 m0 refl) → ⊥
needs-target-1-1 = A.needs-target q1 m0 refl
accept-1-2 : R.isAccepted (R.run q1 q1 c1 refl) ≡ true
accept-1-2 = refl
native-1-2 : A.Both.R.Resolve (A.T.encode (A.context q1 c1 refl))
native-1-2 = A.native q1 c1 refl
needs-target-1-2 : A.Only.Good (A.context q1 c1 refl) → ⊥
needs-target-1-2 = A.needs-target q1 c1 refl
refuse-1-3 : R.isAccepted (R.run q6 q1 m1 refl) ≡ false
refuse-1-3 = refl
refuse-2-0 : R.isAccepted (R.run q13 q2 c0 refl) ≡ false
refuse-2-0 = refl
refuse-2-1 : R.isAccepted (R.run q13 q2 m0 refl) ≡ false
refuse-2-1 = refl
accept-2-2 : R.isAccepted (R.run q2 q2 c1 refl) ≡ true
accept-2-2 = refl
native-2-2 : A.Both.R.Resolve (A.T.encode (A.context q2 c1 refl))
native-2-2 = A.native q2 c1 refl
needs-target-2-2 : A.Only.Good (A.context q2 c1 refl) → ⊥
needs-target-2-2 = A.needs-target q2 c1 refl
accept-2-3 : R.isAccepted (R.run q2 q2 m1 refl) ≡ true
accept-2-3 = refl
native-2-3 : A.Both.R.Resolve (A.T.encode (A.context q2 m1 refl))
native-2-3 = A.native q2 m1 refl
needs-target-2-3 : A.Only.Good (A.context q2 m1 refl) → ⊥
needs-target-2-3 = A.needs-target q2 m1 refl
refuse-3-0 : R.isAccepted (R.run q6 q3 c0 refl) ≡ false
refuse-3-0 = refl
accept-3-1 : R.isAccepted (R.run q3 q3 m0 refl) ≡ true
accept-3-1 = refl
native-3-1 : A.Both.R.Resolve (A.T.encode (A.context q3 m0 refl))
native-3-1 = A.native q3 m0 refl
needs-target-3-1 : A.Only.Good (A.context q3 m0 refl) → ⊥
needs-target-3-1 = A.needs-target q3 m0 refl
accept-3-2 : R.isAccepted (R.run q3 q3 c1 refl) ≡ true
accept-3-2 = refl
native-3-2 : A.Both.R.Resolve (A.T.encode (A.context q3 c1 refl))
native-3-2 = A.native q3 c1 refl
needs-target-3-2 : A.Only.Good (A.context q3 c1 refl) → ⊥
needs-target-3-2 = A.needs-target q3 c1 refl
refuse-3-3 : R.isAccepted (R.run q6 q3 m1 refl) ≡ false
refuse-3-3 = refl
refuse-4-0 : R.isAccepted (R.run q13 q4 c0 refl) ≡ false
refuse-4-0 = refl
refuse-4-1 : R.isAccepted (R.run q13 q4 m0 refl) ≡ false
refuse-4-1 = refl
accept-4-2 : R.isAccepted (R.run q4 q4 c1 refl) ≡ true
accept-4-2 = refl
native-4-2 : A.Both.R.Resolve (A.T.encode (A.context q4 c1 refl))
native-4-2 = A.native q4 c1 refl
needs-target-4-2 : A.Only.Good (A.context q4 c1 refl) → ⊥
needs-target-4-2 = A.needs-target q4 c1 refl
accept-4-3 : R.isAccepted (R.run q4 q4 m1 refl) ≡ true
accept-4-3 = refl
native-4-3 : A.Both.R.Resolve (A.T.encode (A.context q4 m1 refl))
native-4-3 = A.native q4 m1 refl
needs-target-4-3 : A.Only.Good (A.context q4 m1 refl) → ⊥
needs-target-4-3 = A.needs-target q4 m1 refl
refuse-5-0 : R.isAccepted (R.run q7 q5 c0 refl) ≡ false
refuse-5-0 = refl
accept-5-1 : R.isAccepted (R.run q5 q5 m0 refl) ≡ true
accept-5-1 = refl
native-5-1 : A.Both.R.Resolve (A.T.encode (A.context q5 m0 refl))
native-5-1 = A.native q5 m0 refl
needs-target-5-1 : A.Only.Good (A.context q5 m0 refl) → ⊥
needs-target-5-1 = A.needs-target q5 m0 refl
refuse-5-2 : R.isAccepted (R.run q7 q5 c1 refl) ≡ false
refuse-5-2 = refl
accept-5-3 : R.isAccepted (R.run q5 q5 m1 refl) ≡ true
accept-5-3 = refl
native-5-3 : A.Both.R.Resolve (A.T.encode (A.context q5 m1 refl))
native-5-3 = A.native q5 m1 refl
needs-target-5-3 : A.Only.Good (A.context q5 m1 refl) → ⊥
needs-target-5-3 = A.needs-target q5 m1 refl
accept-6-0 : R.isAccepted (R.run q6 q6 c0 refl) ≡ true
accept-6-0 = refl
native-6-0 : A.Both.R.Resolve (A.T.encode (A.context q6 c0 refl))
native-6-0 = A.native q6 c0 refl
needs-target-6-0 : A.Only.Good (A.context q6 c0 refl) → ⊥
needs-target-6-0 = A.needs-target q6 c0 refl
refuse-6-1 : R.isAccepted (R.run q1 q6 m0 refl) ≡ false
refuse-6-1 = refl
refuse-6-2 : R.isAccepted (R.run q1 q6 c1 refl) ≡ false
refuse-6-2 = refl
accept-6-3 : R.isAccepted (R.run q6 q6 m1 refl) ≡ true
accept-6-3 = refl
native-6-3 : A.Both.R.Resolve (A.T.encode (A.context q6 m1 refl))
native-6-3 = A.native q6 m1 refl
needs-target-6-3 : A.Only.Good (A.context q6 m1 refl) → ⊥
needs-target-6-3 = A.needs-target q6 m1 refl
accept-7-0 : R.isAccepted (R.run q7 q7 c0 refl) ≡ true
accept-7-0 = refl
native-7-0 : A.Both.R.Resolve (A.T.encode (A.context q7 c0 refl))
native-7-0 = A.native q7 c0 refl
needs-target-7-0 : A.Only.Good (A.context q7 c0 refl) → ⊥
needs-target-7-0 = A.needs-target q7 c0 refl
refuse-7-1 : R.isAccepted (R.run q0 q7 m0 refl) ≡ false
refuse-7-1 = refl
accept-7-2 : R.isAccepted (R.run q7 q7 c1 refl) ≡ true
accept-7-2 = refl
native-7-2 : A.Both.R.Resolve (A.T.encode (A.context q7 c1 refl))
native-7-2 = A.native q7 c1 refl
needs-target-7-2 : A.Only.Good (A.context q7 c1 refl) → ⊥
needs-target-7-2 = A.needs-target q7 c1 refl
refuse-7-3 : R.isAccepted (R.run q0 q7 m1 refl) ≡ false
refuse-7-3 = refl
refuse-8-0 : R.isAccepted (R.run q13 q8 c0 refl) ≡ false
refuse-8-0 = refl
refuse-8-1 : R.isAccepted (R.run q13 q8 m0 refl) ≡ false
refuse-8-1 = refl
accept-8-2 : R.isAccepted (R.run q8 q8 c1 refl) ≡ true
accept-8-2 = refl
native-8-2 : A.Both.R.Resolve (A.T.encode (A.context q8 c1 refl))
native-8-2 = A.native q8 c1 refl
needs-target-8-2 : A.Only.Good (A.context q8 c1 refl) → ⊥
needs-target-8-2 = A.needs-target q8 c1 refl
accept-8-3 : R.isAccepted (R.run q8 q8 m1 refl) ≡ true
accept-8-3 = refl
native-8-3 : A.Both.R.Resolve (A.T.encode (A.context q8 m1 refl))
native-8-3 = A.native q8 m1 refl
needs-target-8-3 : A.Only.Good (A.context q8 m1 refl) → ⊥
needs-target-8-3 = A.needs-target q8 m1 refl
accept-9-0 : R.isAccepted (R.run q9 q9 c0 refl) ≡ true
accept-9-0 = refl
native-9-0 : A.Both.R.Resolve (A.T.encode (A.context q9 c0 refl))
native-9-0 = A.native q9 c0 refl
needs-target-9-0 : A.Only.Good (A.context q9 c0 refl) → ⊥
needs-target-9-0 = A.needs-target q9 c0 refl
refuse-9-1 : R.isAccepted (R.run q0 q9 m0 refl) ≡ false
refuse-9-1 = refl
accept-9-2 : R.isAccepted (R.run q9 q9 c1 refl) ≡ true
accept-9-2 = refl
native-9-2 : A.Both.R.Resolve (A.T.encode (A.context q9 c1 refl))
native-9-2 = A.native q9 c1 refl
needs-target-9-2 : A.Only.Good (A.context q9 c1 refl) → ⊥
needs-target-9-2 = A.needs-target q9 c1 refl
refuse-9-3 : R.isAccepted (R.run q0 q9 m1 refl) ≡ false
refuse-9-3 = refl
refuse-10-0 : R.isAccepted (R.run q13 q10 c0 refl) ≡ false
refuse-10-0 = refl
refuse-10-1 : R.isAccepted (R.run q13 q10 m0 refl) ≡ false
refuse-10-1 = refl
accept-10-2 : R.isAccepted (R.run q10 q10 c1 refl) ≡ true
accept-10-2 = refl
native-10-2 : A.Both.R.Resolve (A.T.encode (A.context q10 c1 refl))
native-10-2 = A.native q10 c1 refl
needs-target-10-2 : A.Only.Good (A.context q10 c1 refl) → ⊥
needs-target-10-2 = A.needs-target q10 c1 refl
accept-10-3 : R.isAccepted (R.run q10 q10 m1 refl) ≡ true
accept-10-3 = refl
native-10-3 : A.Both.R.Resolve (A.T.encode (A.context q10 m1 refl))
native-10-3 = A.native q10 m1 refl
needs-target-10-3 : A.Only.Good (A.context q10 m1 refl) → ⊥
needs-target-10-3 = A.needs-target q10 m1 refl
accept-11-0 : R.isAccepted (R.run q11 q11 c0 refl) ≡ true
accept-11-0 = refl
native-11-0 : A.Both.R.Resolve (A.T.encode (A.context q11 c0 refl))
native-11-0 = A.native q11 c0 refl
needs-target-11-0 : A.Only.Good (A.context q11 c0 refl) → ⊥
needs-target-11-0 = A.needs-target q11 c0 refl
refuse-11-1 : R.isAccepted (R.run q1 q11 m0 refl) ≡ false
refuse-11-1 = refl
refuse-11-2 : R.isAccepted (R.run q1 q11 c1 refl) ≡ false
refuse-11-2 = refl
accept-11-3 : R.isAccepted (R.run q11 q11 m1 refl) ≡ true
accept-11-3 = refl
native-11-3 : A.Both.R.Resolve (A.T.encode (A.context q11 m1 refl))
native-11-3 = A.native q11 m1 refl
needs-target-11-3 : A.Only.Good (A.context q11 m1 refl) → ⊥
needs-target-11-3 = A.needs-target q11 m1 refl
accept-12-0 : R.isAccepted (R.run q12 q12 c0 refl) ≡ true
accept-12-0 = refl
native-12-0 : A.Both.R.Resolve (A.T.encode (A.context q12 c0 refl))
native-12-0 = A.native q12 c0 refl
needs-target-12-0 : A.Only.Good (A.context q12 c0 refl) → ⊥
needs-target-12-0 = A.needs-target q12 c0 refl
refuse-12-1 : R.isAccepted (R.run q1 q12 m0 refl) ≡ false
refuse-12-1 = refl
refuse-12-2 : R.isAccepted (R.run q1 q12 c1 refl) ≡ false
refuse-12-2 = refl
accept-12-3 : R.isAccepted (R.run q12 q12 m1 refl) ≡ true
accept-12-3 = refl
native-12-3 : A.Both.R.Resolve (A.T.encode (A.context q12 m1 refl))
native-12-3 = A.native q12 m1 refl
needs-target-12-3 : A.Only.Good (A.context q12 m1 refl) → ⊥
needs-target-12-3 = A.needs-target q12 m1 refl
accept-13-0 : R.isAccepted (R.run q13 q13 c0 refl) ≡ true
accept-13-0 = refl
native-13-0 : A.Both.R.Resolve (A.T.encode (A.context q13 c0 refl))
native-13-0 = A.native q13 c0 refl
needs-target-13-0 : A.Only.Good (A.context q13 c0 refl) → ⊥
needs-target-13-0 = A.needs-target q13 c0 refl
accept-13-1 : R.isAccepted (R.run q13 q13 m0 refl) ≡ true
accept-13-1 = refl
native-13-1 : A.Both.R.Resolve (A.T.encode (A.context q13 m0 refl))
native-13-1 = A.native q13 m0 refl
needs-target-13-1 : A.Only.Good (A.context q13 m0 refl) → ⊥
needs-target-13-1 = A.needs-target q13 m0 refl
refuse-13-2 : R.isAccepted (R.run q2 q13 c1 refl) ≡ false
refuse-13-2 = refl
refuse-13-3 : R.isAccepted (R.run q2 q13 m1 refl) ≡ false
refuse-13-3 = refl
refuse-14-0 : R.isAccepted (R.run q7 q14 c0 refl) ≡ false
refuse-14-0 = refl
accept-14-1 : R.isAccepted (R.run q14 q14 m0 refl) ≡ true
accept-14-1 = refl
native-14-1 : A.Both.R.Resolve (A.T.encode (A.context q14 m0 refl))
native-14-1 = A.native q14 m0 refl
needs-target-14-1 : A.Only.Good (A.context q14 m0 refl) → ⊥
needs-target-14-1 = A.needs-target q14 m0 refl
refuse-14-2 : R.isAccepted (R.run q7 q14 c1 refl) ≡ false
refuse-14-2 = refl
accept-14-3 : R.isAccepted (R.run q14 q14 m1 refl) ≡ true
accept-14-3 = refl
native-14-3 : A.Both.R.Resolve (A.T.encode (A.context q14 m1 refl))
native-14-3 = A.native q14 m1 refl
needs-target-14-3 : A.Only.Good (A.context q14 m1 refl) → ⊥
needs-target-14-3 = A.needs-target q14 m1 refl
accept-15-0 : R.isAccepted (R.run q15 q15 c0 refl) ≡ true
accept-15-0 = refl
native-15-0 : A.Both.R.Resolve (A.T.encode (A.context q15 c0 refl))
native-15-0 = A.native q15 c0 refl
needs-target-15-0 : A.Only.Good (A.context q15 c0 refl) → ⊥
needs-target-15-0 = A.needs-target q15 c0 refl
accept-15-1 : R.isAccepted (R.run q15 q15 m0 refl) ≡ true
accept-15-1 = refl
native-15-1 : A.Both.R.Resolve (A.T.encode (A.context q15 m0 refl))
native-15-1 = A.native q15 m0 refl
needs-target-15-1 : A.Only.Good (A.context q15 m0 refl) → ⊥
needs-target-15-1 = A.needs-target q15 m0 refl
refuse-15-2 : R.isAccepted (R.run q2 q15 c1 refl) ≡ false
refuse-15-2 = refl
refuse-15-3 : R.isAccepted (R.run q2 q15 m1 refl) ≡ false
refuse-15-3 = refl
refuse-16-0 : R.isAccepted (R.run q7 q16 c0 refl) ≡ false
refuse-16-0 = refl
accept-16-1 : R.isAccepted (R.run q16 q16 m0 refl) ≡ true
accept-16-1 = refl
native-16-1 : A.Both.R.Resolve (A.T.encode (A.context q16 m0 refl))
native-16-1 = A.native q16 m0 refl
needs-target-16-1 : A.Only.Good (A.context q16 m0 refl) → ⊥
needs-target-16-1 = A.needs-target q16 m0 refl
refuse-16-2 : R.isAccepted (R.run q7 q16 c1 refl) ≡ false
refuse-16-2 = refl
accept-16-3 : R.isAccepted (R.run q16 q16 m1 refl) ≡ true
accept-16-3 = refl
native-16-3 : A.Both.R.Resolve (A.T.encode (A.context q16 m1 refl))
native-16-3 = A.native q16 m1 refl
needs-target-16-3 : A.Only.Good (A.context q16 m1 refl) → ⊥
needs-target-16-3 = A.needs-target q16 m1 refl
accept-17-0 : R.isAccepted (R.run q17 q17 c0 refl) ≡ true
accept-17-0 = refl
native-17-0 : A.Both.R.Resolve (A.T.encode (A.context q17 c0 refl))
native-17-0 = A.native q17 c0 refl
needs-target-17-0 : A.Only.Good (A.context q17 c0 refl) → ⊥
needs-target-17-0 = A.needs-target q17 c0 refl
refuse-17-1 : R.isAccepted (R.run q1 q17 m0 refl) ≡ false
refuse-17-1 = refl
refuse-17-2 : R.isAccepted (R.run q1 q17 c1 refl) ≡ false
refuse-17-2 = refl
accept-17-3 : R.isAccepted (R.run q17 q17 m1 refl) ≡ true
accept-17-3 = refl
native-17-3 : A.Both.R.Resolve (A.T.encode (A.context q17 m1 refl))
native-17-3 = A.native q17 m1 refl
needs-target-17-3 : A.Only.Good (A.context q17 m1 refl) → ⊥
needs-target-17-3 = A.needs-target q17 m1 refl
accept-18-0 : R.isAccepted (R.run q18 q18 c0 refl) ≡ true
accept-18-0 = refl
native-18-0 : A.Both.R.Resolve (A.T.encode (A.context q18 c0 refl))
native-18-0 = A.native q18 c0 refl
needs-target-18-0 : A.Only.Good (A.context q18 c0 refl) → ⊥
needs-target-18-0 = A.needs-target q18 c0 refl
refuse-18-1 : R.isAccepted (R.run q0 q18 m0 refl) ≡ false
refuse-18-1 = refl
accept-18-2 : R.isAccepted (R.run q18 q18 c1 refl) ≡ true
accept-18-2 = refl
native-18-2 : A.Both.R.Resolve (A.T.encode (A.context q18 c1 refl))
native-18-2 = A.native q18 c1 refl
needs-target-18-2 : A.Only.Good (A.context q18 c1 refl) → ⊥
needs-target-18-2 = A.needs-target q18 c1 refl
refuse-18-3 : R.isAccepted (R.run q0 q18 m1 refl) ≡ false
refuse-18-3 = refl
accept-19-0 : R.isAccepted (R.run q19 q19 c0 refl) ≡ true
accept-19-0 = refl
native-19-0 : A.Both.R.Resolve (A.T.encode (A.context q19 c0 refl))
native-19-0 = A.native q19 c0 refl
needs-target-19-0 : A.Only.Good (A.context q19 c0 refl) → ⊥
needs-target-19-0 = A.needs-target q19 c0 refl
accept-19-1 : R.isAccepted (R.run q19 q19 m0 refl) ≡ true
accept-19-1 = refl
native-19-1 : A.Both.R.Resolve (A.T.encode (A.context q19 m0 refl))
native-19-1 = A.native q19 m0 refl
needs-target-19-1 : A.Only.Good (A.context q19 m0 refl) → ⊥
needs-target-19-1 = A.needs-target q19 m0 refl
refuse-19-2 : R.isAccepted (R.run q2 q19 c1 refl) ≡ false
refuse-19-2 = refl
refuse-19-3 : R.isAccepted (R.run q2 q19 m1 refl) ≡ false
refuse-19-3 = refl
refuse-20-0 : R.isAccepted (R.run q6 q20 c0 refl) ≡ false
refuse-20-0 = refl
accept-20-1 : R.isAccepted (R.run q20 q20 m0 refl) ≡ true
accept-20-1 = refl
native-20-1 : A.Both.R.Resolve (A.T.encode (A.context q20 m0 refl))
native-20-1 = A.native q20 m0 refl
needs-target-20-1 : A.Only.Good (A.context q20 m0 refl) → ⊥
needs-target-20-1 = A.needs-target q20 m0 refl
accept-20-2 : R.isAccepted (R.run q20 q20 c1 refl) ≡ true
accept-20-2 = refl
native-20-2 : A.Both.R.Resolve (A.T.encode (A.context q20 c1 refl))
native-20-2 = A.native q20 c1 refl
needs-target-20-2 : A.Only.Good (A.context q20 c1 refl) → ⊥
needs-target-20-2 = A.needs-target q20 c1 refl
refuse-20-3 : R.isAccepted (R.run q6 q20 m1 refl) ≡ false
refuse-20-3 = refl
accept-21-0 : R.isAccepted (R.run q21 q21 c0 refl) ≡ true
accept-21-0 = refl
native-21-0 : A.Both.R.Resolve (A.T.encode (A.context q21 c0 refl))
native-21-0 = A.native q21 c0 refl
needs-target-21-0 : A.Only.Good (A.context q21 c0 refl) → ⊥
needs-target-21-0 = A.needs-target q21 c0 refl
accept-21-1 : R.isAccepted (R.run q21 q21 m0 refl) ≡ true
accept-21-1 = refl
native-21-1 : A.Both.R.Resolve (A.T.encode (A.context q21 m0 refl))
native-21-1 = A.native q21 m0 refl
needs-target-21-1 : A.Only.Good (A.context q21 m0 refl) → ⊥
needs-target-21-1 = A.needs-target q21 m0 refl
refuse-21-2 : R.isAccepted (R.run q2 q21 c1 refl) ≡ false
refuse-21-2 = refl
refuse-21-3 : R.isAccepted (R.run q2 q21 m1 refl) ≡ false
refuse-21-3 = refl
refuse-22-0 : R.isAccepted (R.run q6 q22 c0 refl) ≡ false
refuse-22-0 = refl
accept-22-1 : R.isAccepted (R.run q22 q22 m0 refl) ≡ true
accept-22-1 = refl
native-22-1 : A.Both.R.Resolve (A.T.encode (A.context q22 m0 refl))
native-22-1 = A.native q22 m0 refl
needs-target-22-1 : A.Only.Good (A.context q22 m0 refl) → ⊥
needs-target-22-1 = A.needs-target q22 m0 refl
accept-22-2 : R.isAccepted (R.run q22 q22 c1 refl) ≡ true
accept-22-2 = refl
native-22-2 : A.Both.R.Resolve (A.T.encode (A.context q22 c1 refl))
native-22-2 = A.native q22 c1 refl
needs-target-22-2 : A.Only.Good (A.context q22 c1 refl) → ⊥
needs-target-22-2 = A.needs-target q22 c1 refl
refuse-22-3 : R.isAccepted (R.run q6 q22 m1 refl) ≡ false
refuse-22-3 = refl
accept-23-0 : R.isAccepted (R.run q23 q23 c0 refl) ≡ true
accept-23-0 = refl
native-23-0 : A.Both.R.Resolve (A.T.encode (A.context q23 c0 refl))
native-23-0 = A.native q23 c0 refl
needs-target-23-0 : A.Only.Good (A.context q23 c0 refl) → ⊥
needs-target-23-0 = A.needs-target q23 c0 refl
refuse-23-1 : R.isAccepted (R.run q0 q23 m0 refl) ≡ false
refuse-23-1 = refl
accept-23-2 : R.isAccepted (R.run q23 q23 c1 refl) ≡ true
accept-23-2 = refl
native-23-2 : A.Both.R.Resolve (A.T.encode (A.context q23 c1 refl))
native-23-2 = A.native q23 c1 refl
needs-target-23-2 : A.Only.Good (A.context q23 c1 refl) → ⊥
needs-target-23-2 = A.needs-target q23 c1 refl
refuse-23-3 : R.isAccepted (R.run q0 q23 m1 refl) ≡ false
refuse-23-3 = refl
