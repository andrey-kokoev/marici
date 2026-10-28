{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyRequestedPortExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Relation.Nullary using (Dec; yes; no)
import Cubical.Data.Empty as Empty
open import Agda.Builtin.String using (String)
open import RamseySingleFrameFaces
open import RamseyRequestedPort
data Chart : Type where
  q0 q1 q2 q3 q4 q5 q6 q7 q8 q9 q10 q11 q12 q13 q14 q15 q16 q17 q18 q19 q20 q21 q22 q23 : Chart
role : Chart → Vertex → ℕ
role q0 c0 = 0
role q0 m0 = 1
role q0 c1 = 0
role q0 m1 = 1
role q1 c0 = 0
role q1 m0 = 1
role q1 c1 = 1
role q1 m1 = 0
role q2 c0 = 0
role q2 m0 = 0
role q2 c1 = 1
role q2 m1 = 1
role q3 c0 = 0
role q3 m0 = 1
role q3 c1 = 1
role q3 m1 = 0
role q4 c0 = 0
role q4 m0 = 0
role q4 c1 = 1
role q4 m1 = 1
role q5 c0 = 0
role q5 m0 = 1
role q5 c1 = 0
role q5 m1 = 1
role q6 c0 = 1
role q6 m0 = 0
role q6 c1 = 0
role q6 m1 = 1
role q7 c0 = 1
role q7 m0 = 0
role q7 c1 = 1
role q7 m1 = 0
role q8 c0 = 0
role q8 m0 = 0
role q8 c1 = 1
role q8 m1 = 1
role q9 c0 = 1
role q9 m0 = 0
role q9 c1 = 1
role q9 m1 = 0
role q10 c0 = 0
role q10 m0 = 0
role q10 c1 = 1
role q10 m1 = 1
role q11 c0 = 1
role q11 m0 = 0
role q11 c1 = 0
role q11 m1 = 1
role q12 c0 = 1
role q12 m0 = 0
role q12 c1 = 0
role q12 m1 = 1
role q13 c0 = 1
role q13 m0 = 1
role q13 c1 = 0
role q13 m1 = 0
role q14 c0 = 0
role q14 m0 = 1
role q14 c1 = 0
role q14 m1 = 1
role q15 c0 = 1
role q15 m0 = 1
role q15 c1 = 0
role q15 m1 = 0
role q16 c0 = 0
role q16 m0 = 1
role q16 c1 = 0
role q16 m1 = 1
role q17 c0 = 1
role q17 m0 = 0
role q17 c1 = 0
role q17 m1 = 1
role q18 c0 = 1
role q18 m0 = 0
role q18 c1 = 1
role q18 m1 = 0
role q19 c0 = 1
role q19 m0 = 1
role q19 c1 = 0
role q19 m1 = 0
role q20 c0 = 0
role q20 m0 = 1
role q20 c1 = 1
role q20 m1 = 0
role q21 c0 = 1
role q21 m0 = 1
role q21 c1 = 0
role q21 m1 = 0
role q22 c0 = 0
role q22 m0 = 1
role q22 c1 = 1
role q22 m1 = 0
role q23 c0 = 1
role q23 m0 = 0
role q23 c1 = 1
role q23 m1 = 0
Permit : Chart → Vertex → Type
Permit c f = count (λ i → role c (face f i)) ≡ 2
packet : (c : Chart) (f : Vertex) → Permit c f → String
packet q0 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-0\",\"species\":\"proton\"},\"packet\":{\"chart\":0,\"id\":0,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-0@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"chart\":0,\"face\":0,\"faceVertices\":[\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"id\":0,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":0,\"target\":1},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-0\",\"species\":\"proton\"},\"packet\":{\"chart\":0,\"id\":0,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-0@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":1,\"id\":\"chart-1\",\"species\":\"neutron\"},\"packet\":{\"chart\":1,\"id\":1,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-1@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}}"
packet q0 m0 p = Empty.rec (one-not-two p)
packet q0 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-0\",\"species\":\"proton\"},\"packet\":{\"chart\":0,\"id\":0,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-0@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"chart\":0,\"face\":2,\"faceVertices\":[\"0,0,0,1\",\"1,0,0,0\",\"0,1,0,0\"],\"operation\":{\"face\":[\"0,0,0,1\",\"1,0,0,0\",\"0,1,0,0\"],\"id\":2,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":2,\"target\":3},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":1,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":0,\"target\":2}],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-2\",\"species\":\"proton\"},\"packet\":{\"chart\":2,\"id\":2,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-2@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":2,\"id\":\"chart-3\",\"species\":\"neutron\"},\"packet\":{\"chart\":3,\"id\":3,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"0,1,-1,1\"},\"id\":\"chart-3@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"}]}}"
packet q0 m1 p = Empty.rec (one-not-two p)
packet q1 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-4\",\"species\":\"proton\"},\"packet\":{\"chart\":4,\"id\":5,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-4@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"chart\":1,\"face\":0,\"faceVertices\":[\"0,1,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"id\":4,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":5,\"target\":6},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-4\",\"species\":\"proton\"},\"packet\":{\"chart\":4,\"id\":5,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-4@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":1,\"id\":\"chart-5\",\"species\":\"neutron\"},\"packet\":{\"chart\":5,\"id\":6,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-5@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"}]}}"
packet q1 m0 p = Empty.rec (one-not-two p)
packet q1 c1 p = Empty.rec (one-not-two p)
packet q1 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-4\",\"species\":\"proton\"},\"packet\":{\"chart\":4,\"id\":5,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-4@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"chart\":1,\"face\":3,\"faceVertices\":[\"0,0,1,0\",\"1,0,0,0\",\"0,1,0,0\"],\"operation\":{\"face\":[\"0,0,1,0\",\"1,0,0,0\",\"0,1,0,0\"],\"id\":6,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":7,\"target\":8},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":5,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":5,\"target\":7}],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-6\",\"species\":\"proton\"},\"packet\":{\"chart\":6,\"id\":7,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-6@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":3,\"id\":\"chart-7\",\"species\":\"neutron\"},\"packet\":{\"chart\":7,\"id\":8,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"1,0,1,-1\"},\"id\":\"chart-7@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"}]}}"
packet q2 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-8\",\"species\":\"proton\"},\"packet\":{\"chart\":8,\"id\":10,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-8@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"chart\":2,\"face\":0,\"faceVertices\":[\"0,0,1,0\",\"0,1,0,0\",\"0,0,0,1\"],\"operation\":{\"face\":[\"0,0,1,0\",\"0,1,0,0\",\"0,0,0,1\"],\"id\":8,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":10,\"target\":11},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-8\",\"species\":\"proton\"},\"packet\":{\"chart\":8,\"id\":10,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-8@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":1,\"id\":\"chart-9\",\"species\":\"neutron\"},\"packet\":{\"chart\":9,\"id\":11,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-9@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}}"
packet q2 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-8\",\"species\":\"proton\"},\"packet\":{\"chart\":8,\"id\":10,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-8@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"chart\":2,\"face\":1,\"faceVertices\":[\"0,0,0,1\",\"1,0,0,0\",\"0,0,1,0\"],\"operation\":{\"face\":[\"0,0,0,1\",\"1,0,0,0\",\"0,0,1,0\"],\"id\":10,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":12,\"target\":13},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":9,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":10,\"target\":12}],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-10\",\"species\":\"proton\"},\"packet\":{\"chart\":10,\"id\":12,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-10@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":4,\"id\":\"chart-11\",\"species\":\"neutron\"},\"packet\":{\"chart\":11,\"id\":13,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"1,-1,1,0\"},\"id\":\"chart-11@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"}]}}"
packet q2 c1 p = Empty.rec (one-not-two p)
packet q2 m1 p = Empty.rec (one-not-two p)
packet q3 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-12\",\"species\":\"proton\"},\"packet\":{\"chart\":12,\"id\":15,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-12@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"chart\":3,\"face\":0,\"faceVertices\":[\"0,0,1,0\",\"0,0,0,1\",\"0,1,0,0\"],\"operation\":{\"face\":[\"0,0,1,0\",\"0,0,0,1\",\"0,1,0,0\"],\"id\":12,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":15,\"target\":16},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-12\",\"species\":\"proton\"},\"packet\":{\"chart\":12,\"id\":15,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-12@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":1,\"id\":\"chart-13\",\"species\":\"neutron\"},\"packet\":{\"chart\":13,\"id\":16,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-13@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"}]}}"
packet q3 m0 p = Empty.rec (one-not-two p)
packet q3 c1 p = Empty.rec (one-not-two p)
packet q3 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-12\",\"species\":\"proton\"},\"packet\":{\"chart\":12,\"id\":15,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-12@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"chart\":3,\"face\":3,\"faceVertices\":[\"0,1,0,0\",\"1,0,0,0\",\"0,0,1,0\"],\"operation\":{\"face\":[\"0,1,0,0\",\"1,0,0,0\",\"0,0,1,0\"],\"id\":14,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":17,\"target\":18},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":13,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":15,\"target\":17}],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-14\",\"species\":\"proton\"},\"packet\":{\"chart\":14,\"id\":17,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-14@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":3,\"id\":\"chart-15\",\"species\":\"neutron\"},\"packet\":{\"chart\":15,\"id\":18,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"1,0,1,-1\"},\"id\":\"chart-15@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"}]}}"
packet q4 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-16\",\"species\":\"proton\"},\"packet\":{\"chart\":16,\"id\":20,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-16@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"chart\":4,\"face\":0,\"faceVertices\":[\"0,0,0,1\",\"0,1,0,0\",\"0,0,1,0\"],\"operation\":{\"face\":[\"0,0,0,1\",\"0,1,0,0\",\"0,0,1,0\"],\"id\":16,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":20,\"target\":21},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-16\",\"species\":\"proton\"},\"packet\":{\"chart\":16,\"id\":20,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-16@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":1,\"id\":\"chart-17\",\"species\":\"neutron\"},\"packet\":{\"chart\":17,\"id\":21,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-17@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"}]}}"
packet q4 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-16\",\"species\":\"proton\"},\"packet\":{\"chart\":16,\"id\":20,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-16@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"chart\":4,\"face\":1,\"faceVertices\":[\"0,0,1,0\",\"1,0,0,0\",\"0,0,0,1\"],\"operation\":{\"face\":[\"0,0,1,0\",\"1,0,0,0\",\"0,0,0,1\"],\"id\":18,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":22,\"target\":23},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":17,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":20,\"target\":22}],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-18\",\"species\":\"proton\"},\"packet\":{\"chart\":18,\"id\":22,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-18@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":4,\"id\":\"chart-19\",\"species\":\"neutron\"},\"packet\":{\"chart\":19,\"id\":23,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"1,-1,1,0\"},\"id\":\"chart-19@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}}"
packet q4 c1 p = Empty.rec (one-not-two p)
packet q4 m1 p = Empty.rec (one-not-two p)
packet q5 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-20\",\"species\":\"proton\"},\"packet\":{\"chart\":20,\"id\":25,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-20@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"chart\":5,\"face\":0,\"faceVertices\":[\"0,0,0,1\",\"0,0,1,0\",\"0,1,0,0\"],\"operation\":{\"face\":[\"0,0,0,1\",\"0,0,1,0\",\"0,1,0,0\"],\"id\":20,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":25,\"target\":26},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-20\",\"species\":\"proton\"},\"packet\":{\"chart\":20,\"id\":25,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-20@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":1,\"id\":\"chart-21\",\"species\":\"neutron\"},\"packet\":{\"chart\":21,\"id\":26,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-21@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"}]}}"
packet q5 m0 p = Empty.rec (one-not-two p)
packet q5 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-20\",\"species\":\"proton\"},\"packet\":{\"chart\":20,\"id\":25,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-20@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"chart\":5,\"face\":2,\"faceVertices\":[\"0,1,0,0\",\"1,0,0,0\",\"0,0,0,1\"],\"operation\":{\"face\":[\"0,1,0,0\",\"1,0,0,0\",\"0,0,0,1\"],\"id\":22,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":27,\"target\":28},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":21,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":25,\"target\":27}],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-22\",\"species\":\"proton\"},\"packet\":{\"chart\":22,\"id\":27,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-22@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":2,\"id\":\"chart-23\",\"species\":\"neutron\"},\"packet\":{\"chart\":23,\"id\":28,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"0,1,-1,1\"},\"id\":\"chart-23@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}}"
packet q5 m1 p = Empty.rec (one-not-two p)
packet q6 c0 p = Empty.rec (one-not-two p)
packet q6 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-24\",\"species\":\"proton\"},\"packet\":{\"chart\":24,\"id\":30,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-24@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"chart\":6,\"face\":1,\"faceVertices\":[\"1,0,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"id\":24,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":30,\"target\":31},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-24\",\"species\":\"proton\"},\"packet\":{\"chart\":24,\"id\":30,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-24@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":4,\"id\":\"chart-25\",\"species\":\"neutron\"},\"packet\":{\"chart\":25,\"id\":31,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"1,-1,1,0\"},\"id\":\"chart-25@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}}"
packet q6 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-24\",\"species\":\"proton\"},\"packet\":{\"chart\":24,\"id\":30,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-24@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"chart\":6,\"face\":2,\"faceVertices\":[\"0,0,0,1\",\"0,1,0,0\",\"1,0,0,0\"],\"operation\":{\"face\":[\"0,0,0,1\",\"0,1,0,0\",\"1,0,0,0\"],\"id\":26,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":32,\"target\":33},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":25,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":30,\"target\":32}],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-26\",\"species\":\"proton\"},\"packet\":{\"chart\":26,\"id\":32,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-26@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":2,\"id\":\"chart-27\",\"species\":\"neutron\"},\"packet\":{\"chart\":27,\"id\":33,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"0,1,-1,1\"},\"id\":\"chart-27@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"}]}}"
packet q6 m1 p = Empty.rec (one-not-two p)
packet q7 c0 p = Empty.rec (one-not-two p)
packet q7 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-28\",\"species\":\"proton\"},\"packet\":{\"chart\":28,\"id\":35,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-28@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"chart\":7,\"face\":1,\"faceVertices\":[\"1,0,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"id\":28,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":35,\"target\":36},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-28\",\"species\":\"proton\"},\"packet\":{\"chart\":28,\"id\":35,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-28@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":4,\"id\":\"chart-29\",\"species\":\"neutron\"},\"packet\":{\"chart\":29,\"id\":36,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"1,-1,1,0\"},\"id\":\"chart-29@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"}]}}"
packet q7 c1 p = Empty.rec (one-not-two p)
packet q7 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-28\",\"species\":\"proton\"},\"packet\":{\"chart\":28,\"id\":35,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-28@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"chart\":7,\"face\":3,\"faceVertices\":[\"0,0,1,0\",\"0,1,0,0\",\"1,0,0,0\"],\"operation\":{\"face\":[\"0,0,1,0\",\"0,1,0,0\",\"1,0,0,0\"],\"id\":30,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":37,\"target\":38},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":29,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":35,\"target\":37}],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-30\",\"species\":\"proton\"},\"packet\":{\"chart\":30,\"id\":37,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-30@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":3,\"id\":\"chart-31\",\"species\":\"neutron\"},\"packet\":{\"chart\":31,\"id\":38,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"1,0,1,-1\"},\"id\":\"chart-31@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"}]}}"
packet q8 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-18\",\"species\":\"proton\"},\"packet\":{\"chart\":18,\"id\":40,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-18@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"chart\":8,\"face\":0,\"faceVertices\":[\"0,0,0,1\",\"0,1,0,0\",\"0,0,1,0\"],\"operation\":{\"face\":[\"0,0,0,1\",\"0,1,0,0\",\"0,0,1,0\"],\"id\":34,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":42,\"target\":43},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":33,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":40,\"target\":42}],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-16\",\"species\":\"proton\"},\"packet\":{\"chart\":16,\"id\":42,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-16@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":1,\"id\":\"chart-17\",\"species\":\"neutron\"},\"packet\":{\"chart\":17,\"id\":43,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-17@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"}]}}"
packet q8 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-18\",\"species\":\"proton\"},\"packet\":{\"chart\":18,\"id\":40,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-18@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"chart\":8,\"face\":1,\"faceVertices\":[\"0,0,1,0\",\"1,0,0,0\",\"0,0,0,1\"],\"operation\":{\"face\":[\"0,0,1,0\",\"1,0,0,0\",\"0,0,0,1\"],\"id\":32,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":40,\"target\":41},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-18\",\"species\":\"proton\"},\"packet\":{\"chart\":18,\"id\":40,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-18@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":4,\"id\":\"chart-19\",\"species\":\"neutron\"},\"packet\":{\"chart\":19,\"id\":41,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"1,-1,1,0\"},\"id\":\"chart-19@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}}"
packet q8 c1 p = Empty.rec (one-not-two p)
packet q8 m1 p = Empty.rec (one-not-two p)
packet q9 c0 p = Empty.rec (one-not-two p)
packet q9 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-32\",\"species\":\"proton\"},\"packet\":{\"chart\":32,\"id\":45,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-32@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"chart\":9,\"face\":1,\"faceVertices\":[\"0,0,1,0\",\"0,0,0,1\",\"1,0,0,0\"],\"operation\":{\"face\":[\"0,0,1,0\",\"0,0,0,1\",\"1,0,0,0\"],\"id\":36,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":45,\"target\":46},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-32\",\"species\":\"proton\"},\"packet\":{\"chart\":32,\"id\":45,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-32@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":4,\"id\":\"chart-33\",\"species\":\"neutron\"},\"packet\":{\"chart\":33,\"id\":46,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"1,-1,1,0\"},\"id\":\"chart-33@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"}]}}"
packet q9 c1 p = Empty.rec (one-not-two p)
packet q9 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-32\",\"species\":\"proton\"},\"packet\":{\"chart\":32,\"id\":45,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-32@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"chart\":9,\"face\":3,\"faceVertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\"],\"operation\":{\"face\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\"],\"id\":38,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":47,\"target\":48},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":37,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":45,\"target\":47}],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-34\",\"species\":\"proton\"},\"packet\":{\"chart\":34,\"id\":47,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-34@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":3,\"id\":\"chart-35\",\"species\":\"neutron\"},\"packet\":{\"chart\":35,\"id\":48,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"1,0,1,-1\"},\"id\":\"chart-35@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"}]}}"
packet q10 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-10\",\"species\":\"proton\"},\"packet\":{\"chart\":10,\"id\":50,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-10@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"chart\":10,\"face\":0,\"faceVertices\":[\"0,0,1,0\",\"0,1,0,0\",\"0,0,0,1\"],\"operation\":{\"face\":[\"0,0,1,0\",\"0,1,0,0\",\"0,0,0,1\"],\"id\":42,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":52,\"target\":53},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":41,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":50,\"target\":52}],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-8\",\"species\":\"proton\"},\"packet\":{\"chart\":8,\"id\":52,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-8@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,1,0,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,0,0,1\"},\"cell\":1,\"id\":\"chart-9\",\"species\":\"neutron\"},\"packet\":{\"chart\":9,\"id\":53,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-9@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}}"
packet q10 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-10\",\"species\":\"proton\"},\"packet\":{\"chart\":10,\"id\":50,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-10@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"chart\":10,\"face\":1,\"faceVertices\":[\"0,0,0,1\",\"1,0,0,0\",\"0,0,1,0\"],\"operation\":{\"face\":[\"0,0,0,1\",\"1,0,0,0\",\"0,0,1,0\"],\"id\":40,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":50,\"target\":51},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-10\",\"species\":\"proton\"},\"packet\":{\"chart\":10,\"id\":50,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-10@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"1,0,0,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"0,0,1,0\"},\"cell\":4,\"id\":\"chart-11\",\"species\":\"neutron\"},\"packet\":{\"chart\":11,\"id\":51,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"1,-1,1,0\"},\"id\":\"chart-11@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"}]}}"
packet q10 c1 p = Empty.rec (one-not-two p)
packet q10 m1 p = Empty.rec (one-not-two p)
packet q11 c0 p = Empty.rec (one-not-two p)
packet q11 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-36\",\"species\":\"proton\"},\"packet\":{\"chart\":36,\"id\":55,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-36@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"chart\":11,\"face\":1,\"faceVertices\":[\"0,0,0,1\",\"0,0,1,0\",\"1,0,0,0\"],\"operation\":{\"face\":[\"0,0,0,1\",\"0,0,1,0\",\"1,0,0,0\"],\"id\":44,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":55,\"target\":56},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-36\",\"species\":\"proton\"},\"packet\":{\"chart\":36,\"id\":55,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-36@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":4,\"id\":\"chart-37\",\"species\":\"neutron\"},\"packet\":{\"chart\":37,\"id\":56,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"1,-1,1,0\"},\"id\":\"chart-37@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"}]}}"
packet q11 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-36\",\"species\":\"proton\"},\"packet\":{\"chart\":36,\"id\":55,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-36@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"chart\":11,\"face\":2,\"faceVertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,0,1\"],\"operation\":{\"face\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,0,1\"],\"id\":46,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":57,\"target\":58},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":45,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":55,\"target\":57}],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-38\",\"species\":\"proton\"},\"packet\":{\"chart\":38,\"id\":57,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-38@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":2,\"id\":\"chart-39\",\"species\":\"neutron\"},\"packet\":{\"chart\":39,\"id\":58,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"0,1,-1,1\"},\"id\":\"chart-39@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}}"
packet q11 m1 p = Empty.rec (one-not-two p)
packet q12 c0 p = Empty.rec (one-not-two p)
packet q12 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-38\",\"species\":\"proton\"},\"packet\":{\"chart\":38,\"id\":60,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-38@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"chart\":12,\"face\":1,\"faceVertices\":[\"0,0,0,1\",\"0,0,1,0\",\"1,0,0,0\"],\"operation\":{\"face\":[\"0,0,0,1\",\"0,0,1,0\",\"1,0,0,0\"],\"id\":50,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":62,\"target\":63},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":49,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":60,\"target\":62}],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-36\",\"species\":\"proton\"},\"packet\":{\"chart\":36,\"id\":62,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-36@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":4,\"id\":\"chart-37\",\"species\":\"neutron\"},\"packet\":{\"chart\":37,\"id\":63,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"1,-1,1,0\"},\"id\":\"chart-37@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"}]}}"
packet q12 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-38\",\"species\":\"proton\"},\"packet\":{\"chart\":38,\"id\":60,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-38@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"chart\":12,\"face\":2,\"faceVertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,0,1\"],\"operation\":{\"face\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,0,1\"],\"id\":48,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":60,\"target\":61},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-38\",\"species\":\"proton\"},\"packet\":{\"chart\":38,\"id\":60,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-38@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":2,\"id\":\"chart-39\",\"species\":\"neutron\"},\"packet\":{\"chart\":39,\"id\":61,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,-1,1\"},\"id\":\"chart-39@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}}"
packet q12 m1 p = Empty.rec (one-not-two p)
packet q13 c0 p = Empty.rec (one-not-two p)
packet q13 m0 p = Empty.rec (one-not-two p)
packet q13 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-40\",\"species\":\"proton\"},\"packet\":{\"chart\":40,\"id\":65,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-40@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"chart\":13,\"face\":2,\"faceVertices\":[\"1,0,0,0\",\"0,0,0,1\",\"0,1,0,0\"],\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,0,1\",\"0,1,0,0\"],\"id\":52,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":65,\"target\":66},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-40\",\"species\":\"proton\"},\"packet\":{\"chart\":40,\"id\":65,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-40@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":2,\"id\":\"chart-41\",\"species\":\"neutron\"},\"packet\":{\"chart\":41,\"id\":66,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,-1,1\"},\"id\":\"chart-41@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"}]}}"
packet q13 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-40\",\"species\":\"proton\"},\"packet\":{\"chart\":40,\"id\":65,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-40@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"chart\":13,\"face\":3,\"faceVertices\":[\"0,1,0,0\",\"0,0,1,0\",\"1,0,0,0\"],\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,1,0\",\"1,0,0,0\"],\"id\":54,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":67,\"target\":68},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":53,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":65,\"target\":67}],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-42\",\"species\":\"proton\"},\"packet\":{\"chart\":42,\"id\":67,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-42@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":3,\"id\":\"chart-43\",\"species\":\"neutron\"},\"packet\":{\"chart\":43,\"id\":68,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"1,0,1,-1\"},\"id\":\"chart-43@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"}]}}"
packet q14 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-22\",\"species\":\"proton\"},\"packet\":{\"chart\":22,\"id\":70,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-22@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"chart\":14,\"face\":0,\"faceVertices\":[\"0,0,0,1\",\"0,0,1,0\",\"0,1,0,0\"],\"operation\":{\"face\":[\"0,0,0,1\",\"0,0,1,0\",\"0,1,0,0\"],\"id\":58,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":72,\"target\":73},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":57,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":70,\"target\":72}],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-20\",\"species\":\"proton\"},\"packet\":{\"chart\":20,\"id\":72,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-20@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":1,\"id\":\"chart-21\",\"species\":\"neutron\"},\"packet\":{\"chart\":21,\"id\":73,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-21@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"}]}}"
packet q14 m0 p = Empty.rec (one-not-two p)
packet q14 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-22\",\"species\":\"proton\"},\"packet\":{\"chart\":22,\"id\":70,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-22@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"chart\":14,\"face\":2,\"faceVertices\":[\"0,1,0,0\",\"1,0,0,0\",\"0,0,0,1\"],\"operation\":{\"face\":[\"0,1,0,0\",\"1,0,0,0\",\"0,0,0,1\"],\"id\":56,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":70,\"target\":71},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-22\",\"species\":\"proton\"},\"packet\":{\"chart\":22,\"id\":70,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-22@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":2,\"id\":\"chart-23\",\"species\":\"neutron\"},\"packet\":{\"chart\":23,\"id\":71,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,-1,1\"},\"id\":\"chart-23@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}}"
packet q14 m1 p = Empty.rec (one-not-two p)
packet q15 c0 p = Empty.rec (one-not-two p)
packet q15 m0 p = Empty.rec (one-not-two p)
packet q15 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-44\",\"species\":\"proton\"},\"packet\":{\"chart\":44,\"id\":75,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-44@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"chart\":15,\"face\":2,\"faceVertices\":[\"0,1,0,0\",\"0,0,0,1\",\"1,0,0,0\"],\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,0,1\",\"1,0,0,0\"],\"id\":60,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":75,\"target\":76},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-44\",\"species\":\"proton\"},\"packet\":{\"chart\":44,\"id\":75,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-44@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":2,\"id\":\"chart-45\",\"species\":\"neutron\"},\"packet\":{\"chart\":45,\"id\":76,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,-1,1\"},\"id\":\"chart-45@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"}]}}"
packet q15 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-44\",\"species\":\"proton\"},\"packet\":{\"chart\":44,\"id\":75,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-44@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"chart\":15,\"face\":3,\"faceVertices\":[\"1,0,0,0\",\"0,0,1,0\",\"0,1,0,0\"],\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,1,0\",\"0,1,0,0\"],\"id\":62,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":77,\"target\":78},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":61,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":75,\"target\":77}],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-46\",\"species\":\"proton\"},\"packet\":{\"chart\":46,\"id\":77,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-46@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":3,\"id\":\"chart-47\",\"species\":\"neutron\"},\"packet\":{\"chart\":47,\"id\":78,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"1,0,1,-1\"},\"id\":\"chart-47@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"}]}}"
packet q16 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-2\",\"species\":\"proton\"},\"packet\":{\"chart\":2,\"id\":80,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-2@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"chart\":16,\"face\":0,\"faceVertices\":[\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"id\":66,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":82,\"target\":83},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":65,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":80,\"target\":82}],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-0\",\"species\":\"proton\"},\"packet\":{\"chart\":0,\"id\":82,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-0@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":1,\"id\":\"chart-1\",\"species\":\"neutron\"},\"packet\":{\"chart\":1,\"id\":83,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-1@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}}"
packet q16 m0 p = Empty.rec (one-not-two p)
packet q16 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-2\",\"species\":\"proton\"},\"packet\":{\"chart\":2,\"id\":80,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-2@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"chart\":16,\"face\":2,\"faceVertices\":[\"0,0,0,1\",\"1,0,0,0\",\"0,1,0,0\"],\"operation\":{\"face\":[\"0,0,0,1\",\"1,0,0,0\",\"0,1,0,0\"],\"id\":64,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":80,\"target\":81},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-2\",\"species\":\"proton\"},\"packet\":{\"chart\":2,\"id\":80,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-2@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":2,\"id\":\"chart-3\",\"species\":\"neutron\"},\"packet\":{\"chart\":3,\"id\":81,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,-1,1\"},\"id\":\"chart-3@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"}]}}"
packet q16 m1 p = Empty.rec (one-not-two p)
packet q17 c0 p = Empty.rec (one-not-two p)
packet q17 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-26\",\"species\":\"proton\"},\"packet\":{\"chart\":26,\"id\":85,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-26@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"chart\":17,\"face\":1,\"faceVertices\":[\"1,0,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"id\":70,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":87,\"target\":88},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":69,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":85,\"target\":87}],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-24\",\"species\":\"proton\"},\"packet\":{\"chart\":24,\"id\":87,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-24@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":4,\"id\":\"chart-25\",\"species\":\"neutron\"},\"packet\":{\"chart\":25,\"id\":88,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"1,-1,1,0\"},\"id\":\"chart-25@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}}"
packet q17 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-26\",\"species\":\"proton\"},\"packet\":{\"chart\":26,\"id\":85,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-26@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"chart\":17,\"face\":2,\"faceVertices\":[\"0,0,0,1\",\"0,1,0,0\",\"1,0,0,0\"],\"operation\":{\"face\":[\"0,0,0,1\",\"0,1,0,0\",\"1,0,0,0\"],\"id\":68,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":85,\"target\":86},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-26\",\"species\":\"proton\"},\"packet\":{\"chart\":26,\"id\":85,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-26@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,1,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"1,0,0,0\"},\"cell\":2,\"id\":\"chart-27\",\"species\":\"neutron\"},\"packet\":{\"chart\":27,\"id\":86,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"0,1,-1,1\"},\"id\":\"chart-27@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"}]}}"
packet q17 m1 p = Empty.rec (one-not-two p)
packet q18 c0 p = Empty.rec (one-not-two p)
packet q18 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-34\",\"species\":\"proton\"},\"packet\":{\"chart\":34,\"id\":90,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-34@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"chart\":18,\"face\":1,\"faceVertices\":[\"0,0,1,0\",\"0,0,0,1\",\"1,0,0,0\"],\"operation\":{\"face\":[\"0,0,1,0\",\"0,0,0,1\",\"1,0,0,0\"],\"id\":74,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":92,\"target\":93},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":73,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":90,\"target\":92}],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-32\",\"species\":\"proton\"},\"packet\":{\"chart\":32,\"id\":92,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-32@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":4,\"id\":\"chart-33\",\"species\":\"neutron\"},\"packet\":{\"chart\":33,\"id\":93,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"1,-1,1,0\"},\"id\":\"chart-33@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"}]}}"
packet q18 c1 p = Empty.rec (one-not-two p)
packet q18 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-34\",\"species\":\"proton\"},\"packet\":{\"chart\":34,\"id\":90,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-34@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"chart\":18,\"face\":3,\"faceVertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\"],\"operation\":{\"face\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\"],\"id\":72,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":90,\"target\":91},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-34\",\"species\":\"proton\"},\"packet\":{\"chart\":34,\"id\":90,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-34@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":3,\"id\":\"chart-35\",\"species\":\"neutron\"},\"packet\":{\"chart\":35,\"id\":91,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,1,-1\"},\"id\":\"chart-35@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"}]}}"
packet q19 c0 p = Empty.rec (one-not-two p)
packet q19 m0 p = Empty.rec (one-not-two p)
packet q19 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-46\",\"species\":\"proton\"},\"packet\":{\"chart\":46,\"id\":95,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-46@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"chart\":19,\"face\":2,\"faceVertices\":[\"0,1,0,0\",\"0,0,0,1\",\"1,0,0,0\"],\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,0,1\",\"1,0,0,0\"],\"id\":78,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":97,\"target\":98},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":77,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":95,\"target\":97}],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-44\",\"species\":\"proton\"},\"packet\":{\"chart\":44,\"id\":97,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-44@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":2,\"id\":\"chart-45\",\"species\":\"neutron\"},\"packet\":{\"chart\":45,\"id\":98,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"0,1,-1,1\"},\"id\":\"chart-45@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"1,0,0,0\"}]}}"
packet q19 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-46\",\"species\":\"proton\"},\"packet\":{\"chart\":46,\"id\":95,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-46@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"chart\":19,\"face\":3,\"faceVertices\":[\"1,0,0,0\",\"0,0,1,0\",\"0,1,0,0\"],\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,1,0\",\"0,1,0,0\"],\"id\":76,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":95,\"target\":96},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-46\",\"species\":\"proton\"},\"packet\":{\"chart\":46,\"id\":95,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-46@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":3,\"id\":\"chart-47\",\"species\":\"neutron\"},\"packet\":{\"chart\":47,\"id\":96,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,1,-1\"},\"id\":\"chart-47@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"}]}}"
packet q20 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-14\",\"species\":\"proton\"},\"packet\":{\"chart\":14,\"id\":100,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-14@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"chart\":20,\"face\":0,\"faceVertices\":[\"0,0,1,0\",\"0,0,0,1\",\"0,1,0,0\"],\"operation\":{\"face\":[\"0,0,1,0\",\"0,0,0,1\",\"0,1,0,0\"],\"id\":82,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":102,\"target\":103},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":81,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":100,\"target\":102}],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-12\",\"species\":\"proton\"},\"packet\":{\"chart\":12,\"id\":102,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-12@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":1,\"id\":\"chart-13\",\"species\":\"neutron\"},\"packet\":{\"chart\":13,\"id\":103,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-13@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"}]}}"
packet q20 m0 p = Empty.rec (one-not-two p)
packet q20 c1 p = Empty.rec (one-not-two p)
packet q20 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-14\",\"species\":\"proton\"},\"packet\":{\"chart\":14,\"id\":100,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-14@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"chart\":20,\"face\":3,\"faceVertices\":[\"0,1,0,0\",\"1,0,0,0\",\"0,0,1,0\"],\"operation\":{\"face\":[\"0,1,0,0\",\"1,0,0,0\",\"0,0,1,0\"],\"id\":80,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":100,\"target\":101},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-14\",\"species\":\"proton\"},\"packet\":{\"chart\":14,\"id\":100,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-14@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":3,\"id\":\"chart-15\",\"species\":\"neutron\"},\"packet\":{\"chart\":15,\"id\":101,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,1,-1\"},\"id\":\"chart-15@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,1,0\"}]}}"
packet q21 c0 p = Empty.rec (one-not-two p)
packet q21 m0 p = Empty.rec (one-not-two p)
packet q21 c1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-42\",\"species\":\"proton\"},\"packet\":{\"chart\":42,\"id\":105,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-42@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"chart\":21,\"face\":2,\"faceVertices\":[\"1,0,0,0\",\"0,0,0,1\",\"0,1,0,0\"],\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,0,1\",\"0,1,0,0\"],\"id\":86,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":107,\"target\":108},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":85,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":105,\"target\":107}],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-40\",\"species\":\"proton\"},\"packet\":{\"chart\":40,\"id\":107,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-40@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"target\":{\"cell\":{\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"0,0,0,1\",\"C2\":\"0,1,-1,1\",\"M0\":\"1,0,0,0\",\"M1\":\"0,1,0,0\"},\"cell\":2,\"id\":\"chart-41\",\"species\":\"neutron\"},\"packet\":{\"chart\":41,\"id\":108,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"0,1,-1,1\"},\"id\":\"chart-41@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,1,0,0\"}]}}"
packet q21 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-42\",\"species\":\"proton\"},\"packet\":{\"chart\":42,\"id\":105,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-42@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"chart\":21,\"face\":3,\"faceVertices\":[\"0,1,0,0\",\"0,0,1,0\",\"1,0,0,0\"],\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,1,0\",\"1,0,0,0\"],\"id\":84,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":105,\"target\":106},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-42\",\"species\":\"proton\"},\"packet\":{\"chart\":42,\"id\":105,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-42@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,0,1,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,1,0,0\",\"M1\":\"1,0,0,0\"},\"cell\":3,\"id\":\"chart-43\",\"species\":\"neutron\"},\"packet\":{\"chart\":43,\"id\":106,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,1,-1\"},\"id\":\"chart-43@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"}]}}"
packet q22 c0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-6\",\"species\":\"proton\"},\"packet\":{\"chart\":6,\"id\":110,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-6@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"chart\":22,\"face\":0,\"faceVertices\":[\"0,1,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"id\":90,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":112,\"target\":113},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":89,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":110,\"target\":112}],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-4\",\"species\":\"proton\"},\"packet\":{\"chart\":4,\"id\":112,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-4@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":1,\"id\":\"chart-5\",\"species\":\"neutron\"},\"packet\":{\"chart\":5,\"id\":113,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-5@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"}]}}"
packet q22 m0 p = Empty.rec (one-not-two p)
packet q22 c1 p = Empty.rec (one-not-two p)
packet q22 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-6\",\"species\":\"proton\"},\"packet\":{\"chart\":6,\"id\":110,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-6@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"chart\":22,\"face\":3,\"faceVertices\":[\"0,0,1,0\",\"1,0,0,0\",\"0,1,0,0\"],\"operation\":{\"face\":[\"0,0,1,0\",\"1,0,0,0\",\"0,1,0,0\"],\"id\":88,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":110,\"target\":111},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-6\",\"species\":\"proton\"},\"packet\":{\"chart\":6,\"id\":110,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},\"id\":\"chart-6@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"}]},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"1,0,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"0,1,0,0\"},\"cell\":3,\"id\":\"chart-7\",\"species\":\"neutron\"},\"packet\":{\"chart\":7,\"id\":111,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,1,-1\"},\"id\":\"chart-7@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,1,0,0\"}]}}"
packet q23 c0 p = Empty.rec (one-not-two p)
packet q23 m0 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-30\",\"species\":\"proton\"},\"packet\":{\"chart\":30,\"id\":115,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-30@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"chart\":23,\"face\":1,\"faceVertices\":[\"1,0,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"id\":94,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":117,\"target\":118},\"permitMCount\":2,\"prefix\":[{\"face\":null,\"id\":93,\"kind\":\"reader-phase-advance\",\"permutation\":[2,3,0,1,4],\"phaseDelta\":1,\"source\":115,\"target\":117}],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-28\",\"species\":\"proton\"},\"packet\":{\"chart\":28,\"id\":117,\"origin\":1,\"permutation\":[2,3,0,1,4]}},\"sourceFrame\":{\"context\":{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},\"id\":\"chart-28@1\",\"species\":\"proton\",\"window\":[{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"}]},\"target\":{\"cell\":{\"id\":4,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":4,\"id\":\"chart-29\",\"species\":\"neutron\"},\"packet\":{\"chart\":29,\"id\":118,\"origin\":1,\"permutation\":[1,3,0,2,4]}},\"targetFrame\":{\"context\":{\"index\":3,\"role\":\"C\",\"vertex\":\"1,-1,1,0\"},\"id\":\"chart-29@1\",\"species\":\"neutron\",\"window\":[{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},{\"index\":2,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":2,\"role\":\"M\",\"vertex\":\"0,0,1,0\"}]}}"
packet q23 c1 p = Empty.rec (one-not-two p)
packet q23 m1 p = "{\"base\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-30\",\"species\":\"proton\"},\"packet\":{\"chart\":30,\"id\":115,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"baseFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-30@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"chart\":23,\"face\":3,\"faceVertices\":[\"0,0,1,0\",\"0,1,0,0\",\"1,0,0,0\"],\"operation\":{\"face\":[\"0,0,1,0\",\"0,1,0,0\",\"1,0,0,0\"],\"id\":92,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":115,\"target\":116},\"permitMCount\":2,\"prefix\":[],\"role\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-30\",\"species\":\"proton\"},\"packet\":{\"chart\":30,\"id\":115,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"sourceFrame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"},\"id\":\"chart-30@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"0,0,0,1\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"}]},\"target\":{\"cell\":{\"id\":3,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":3,\"id\":\"chart-31\",\"species\":\"neutron\"},\"packet\":{\"chart\":31,\"id\":116,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"1,0,1,-1\"},\"id\":\"chart-31@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"1,0,0,0\"}]}}"
decide : (c : Chart) (f : Vertex) → Dec (Permit c f)
decide q0 c0 = yes refl
decide q0 m0 = no one-not-two
decide q0 c1 = yes refl
decide q0 m1 = no one-not-two
decide q1 c0 = yes refl
decide q1 m0 = no one-not-two
decide q1 c1 = no one-not-two
decide q1 m1 = yes refl
decide q2 c0 = yes refl
decide q2 m0 = yes refl
decide q2 c1 = no one-not-two
decide q2 m1 = no one-not-two
decide q3 c0 = yes refl
decide q3 m0 = no one-not-two
decide q3 c1 = no one-not-two
decide q3 m1 = yes refl
decide q4 c0 = yes refl
decide q4 m0 = yes refl
decide q4 c1 = no one-not-two
decide q4 m1 = no one-not-two
decide q5 c0 = yes refl
decide q5 m0 = no one-not-two
decide q5 c1 = yes refl
decide q5 m1 = no one-not-two
decide q6 c0 = no one-not-two
decide q6 m0 = yes refl
decide q6 c1 = yes refl
decide q6 m1 = no one-not-two
decide q7 c0 = no one-not-two
decide q7 m0 = yes refl
decide q7 c1 = no one-not-two
decide q7 m1 = yes refl
decide q8 c0 = yes refl
decide q8 m0 = yes refl
decide q8 c1 = no one-not-two
decide q8 m1 = no one-not-two
decide q9 c0 = no one-not-two
decide q9 m0 = yes refl
decide q9 c1 = no one-not-two
decide q9 m1 = yes refl
decide q10 c0 = yes refl
decide q10 m0 = yes refl
decide q10 c1 = no one-not-two
decide q10 m1 = no one-not-two
decide q11 c0 = no one-not-two
decide q11 m0 = yes refl
decide q11 c1 = yes refl
decide q11 m1 = no one-not-two
decide q12 c0 = no one-not-two
decide q12 m0 = yes refl
decide q12 c1 = yes refl
decide q12 m1 = no one-not-two
decide q13 c0 = no one-not-two
decide q13 m0 = no one-not-two
decide q13 c1 = yes refl
decide q13 m1 = yes refl
decide q14 c0 = yes refl
decide q14 m0 = no one-not-two
decide q14 c1 = yes refl
decide q14 m1 = no one-not-two
decide q15 c0 = no one-not-two
decide q15 m0 = no one-not-two
decide q15 c1 = yes refl
decide q15 m1 = yes refl
decide q16 c0 = yes refl
decide q16 m0 = no one-not-two
decide q16 c1 = yes refl
decide q16 m1 = no one-not-two
decide q17 c0 = no one-not-two
decide q17 m0 = yes refl
decide q17 c1 = yes refl
decide q17 m1 = no one-not-two
decide q18 c0 = no one-not-two
decide q18 m0 = yes refl
decide q18 c1 = no one-not-two
decide q18 m1 = yes refl
decide q19 c0 = no one-not-two
decide q19 m0 = no one-not-two
decide q19 c1 = yes refl
decide q19 m1 = yes refl
decide q20 c0 = yes refl
decide q20 m0 = no one-not-two
decide q20 c1 = no one-not-two
decide q20 m1 = yes refl
decide q21 c0 = no one-not-two
decide q21 m0 = no one-not-two
decide q21 c1 = yes refl
decide q21 m1 = yes refl
decide q22 c0 = yes refl
decide q22 m0 = no one-not-two
decide q22 c1 = no one-not-two
decide q22 m1 = yes refl
decide q23 c0 = no one-not-two
decide q23 m0 = yes refl
decide q23 c1 = no one-not-two
decide q23 m1 = yes refl
module R = Request Chart Vertex Permit packet decide
case-0-0-0 : R.isAccepted (R.run q0 q0 c0 refl) ≡ true
case-0-0-0 = refl
case-0-0-1 : R.isAccepted (R.run q0 q1 c0 refl) ≡ true
case-0-0-1 = refl
case-0-0-2 : R.isAccepted (R.run q0 q2 c0 refl) ≡ true
case-0-0-2 = refl
case-0-0-3 : R.isAccepted (R.run q0 q3 c0 refl) ≡ true
case-0-0-3 = refl
case-0-0-4 : R.isAccepted (R.run q0 q4 c0 refl) ≡ true
case-0-0-4 = refl
case-0-0-5 : R.isAccepted (R.run q0 q5 c0 refl) ≡ true
case-0-0-5 = refl
case-0-0-6 : R.isAccepted (R.run q0 q6 c0 refl) ≡ false
case-0-0-6 = refl
case-0-0-7 : R.isAccepted (R.run q0 q7 c0 refl) ≡ false
case-0-0-7 = refl
case-0-0-8 : R.isAccepted (R.run q0 q8 c0 refl) ≡ true
case-0-0-8 = refl
case-0-0-9 : R.isAccepted (R.run q0 q9 c0 refl) ≡ false
case-0-0-9 = refl
case-0-0-10 : R.isAccepted (R.run q0 q10 c0 refl) ≡ true
case-0-0-10 = refl
case-0-0-11 : R.isAccepted (R.run q0 q11 c0 refl) ≡ false
case-0-0-11 = refl
case-0-0-12 : R.isAccepted (R.run q0 q12 c0 refl) ≡ false
case-0-0-12 = refl
case-0-0-13 : R.isAccepted (R.run q0 q13 c0 refl) ≡ false
case-0-0-13 = refl
case-0-0-14 : R.isAccepted (R.run q0 q14 c0 refl) ≡ true
case-0-0-14 = refl
case-0-0-15 : R.isAccepted (R.run q0 q15 c0 refl) ≡ false
case-0-0-15 = refl
case-0-0-16 : R.isAccepted (R.run q0 q16 c0 refl) ≡ true
case-0-0-16 = refl
case-0-0-17 : R.isAccepted (R.run q0 q17 c0 refl) ≡ false
case-0-0-17 = refl
case-0-0-18 : R.isAccepted (R.run q0 q18 c0 refl) ≡ false
case-0-0-18 = refl
case-0-0-19 : R.isAccepted (R.run q0 q19 c0 refl) ≡ false
case-0-0-19 = refl
case-0-0-20 : R.isAccepted (R.run q0 q20 c0 refl) ≡ true
case-0-0-20 = refl
case-0-0-21 : R.isAccepted (R.run q0 q21 c0 refl) ≡ false
case-0-0-21 = refl
case-0-0-22 : R.isAccepted (R.run q0 q22 c0 refl) ≡ true
case-0-0-22 = refl
case-0-0-23 : R.isAccepted (R.run q0 q23 c0 refl) ≡ false
case-0-0-23 = refl
case-0-2-0 : R.isAccepted (R.run q0 q0 c1 refl) ≡ true
case-0-2-0 = refl
case-0-2-1 : R.isAccepted (R.run q0 q1 c1 refl) ≡ false
case-0-2-1 = refl
case-0-2-2 : R.isAccepted (R.run q0 q2 c1 refl) ≡ false
case-0-2-2 = refl
case-0-2-3 : R.isAccepted (R.run q0 q3 c1 refl) ≡ false
case-0-2-3 = refl
case-0-2-4 : R.isAccepted (R.run q0 q4 c1 refl) ≡ false
case-0-2-4 = refl
case-0-2-5 : R.isAccepted (R.run q0 q5 c1 refl) ≡ true
case-0-2-5 = refl
case-0-2-6 : R.isAccepted (R.run q0 q6 c1 refl) ≡ true
case-0-2-6 = refl
case-0-2-7 : R.isAccepted (R.run q0 q7 c1 refl) ≡ false
case-0-2-7 = refl
case-0-2-8 : R.isAccepted (R.run q0 q8 c1 refl) ≡ false
case-0-2-8 = refl
case-0-2-9 : R.isAccepted (R.run q0 q9 c1 refl) ≡ false
case-0-2-9 = refl
case-0-2-10 : R.isAccepted (R.run q0 q10 c1 refl) ≡ false
case-0-2-10 = refl
case-0-2-11 : R.isAccepted (R.run q0 q11 c1 refl) ≡ true
case-0-2-11 = refl
case-0-2-12 : R.isAccepted (R.run q0 q12 c1 refl) ≡ true
case-0-2-12 = refl
case-0-2-13 : R.isAccepted (R.run q0 q13 c1 refl) ≡ true
case-0-2-13 = refl
case-0-2-14 : R.isAccepted (R.run q0 q14 c1 refl) ≡ true
case-0-2-14 = refl
case-0-2-15 : R.isAccepted (R.run q0 q15 c1 refl) ≡ true
case-0-2-15 = refl
case-0-2-16 : R.isAccepted (R.run q0 q16 c1 refl) ≡ true
case-0-2-16 = refl
case-0-2-17 : R.isAccepted (R.run q0 q17 c1 refl) ≡ true
case-0-2-17 = refl
case-0-2-18 : R.isAccepted (R.run q0 q18 c1 refl) ≡ false
case-0-2-18 = refl
case-0-2-19 : R.isAccepted (R.run q0 q19 c1 refl) ≡ true
case-0-2-19 = refl
case-0-2-20 : R.isAccepted (R.run q0 q20 c1 refl) ≡ false
case-0-2-20 = refl
case-0-2-21 : R.isAccepted (R.run q0 q21 c1 refl) ≡ true
case-0-2-21 = refl
case-0-2-22 : R.isAccepted (R.run q0 q22 c1 refl) ≡ false
case-0-2-22 = refl
case-0-2-23 : R.isAccepted (R.run q0 q23 c1 refl) ≡ false
case-0-2-23 = refl
case-1-0-0 : R.isAccepted (R.run q1 q0 c0 refl) ≡ true
case-1-0-0 = refl
case-1-0-1 : R.isAccepted (R.run q1 q1 c0 refl) ≡ true
case-1-0-1 = refl
case-1-0-2 : R.isAccepted (R.run q1 q2 c0 refl) ≡ true
case-1-0-2 = refl
case-1-0-3 : R.isAccepted (R.run q1 q3 c0 refl) ≡ true
case-1-0-3 = refl
case-1-0-4 : R.isAccepted (R.run q1 q4 c0 refl) ≡ true
case-1-0-4 = refl
case-1-0-5 : R.isAccepted (R.run q1 q5 c0 refl) ≡ true
case-1-0-5 = refl
case-1-0-6 : R.isAccepted (R.run q1 q6 c0 refl) ≡ false
case-1-0-6 = refl
case-1-0-7 : R.isAccepted (R.run q1 q7 c0 refl) ≡ false
case-1-0-7 = refl
case-1-0-8 : R.isAccepted (R.run q1 q8 c0 refl) ≡ true
case-1-0-8 = refl
case-1-0-9 : R.isAccepted (R.run q1 q9 c0 refl) ≡ false
case-1-0-9 = refl
case-1-0-10 : R.isAccepted (R.run q1 q10 c0 refl) ≡ true
case-1-0-10 = refl
case-1-0-11 : R.isAccepted (R.run q1 q11 c0 refl) ≡ false
case-1-0-11 = refl
case-1-0-12 : R.isAccepted (R.run q1 q12 c0 refl) ≡ false
case-1-0-12 = refl
case-1-0-13 : R.isAccepted (R.run q1 q13 c0 refl) ≡ false
case-1-0-13 = refl
case-1-0-14 : R.isAccepted (R.run q1 q14 c0 refl) ≡ true
case-1-0-14 = refl
case-1-0-15 : R.isAccepted (R.run q1 q15 c0 refl) ≡ false
case-1-0-15 = refl
case-1-0-16 : R.isAccepted (R.run q1 q16 c0 refl) ≡ true
case-1-0-16 = refl
case-1-0-17 : R.isAccepted (R.run q1 q17 c0 refl) ≡ false
case-1-0-17 = refl
case-1-0-18 : R.isAccepted (R.run q1 q18 c0 refl) ≡ false
case-1-0-18 = refl
case-1-0-19 : R.isAccepted (R.run q1 q19 c0 refl) ≡ false
case-1-0-19 = refl
case-1-0-20 : R.isAccepted (R.run q1 q20 c0 refl) ≡ true
case-1-0-20 = refl
case-1-0-21 : R.isAccepted (R.run q1 q21 c0 refl) ≡ false
case-1-0-21 = refl
case-1-0-22 : R.isAccepted (R.run q1 q22 c0 refl) ≡ true
case-1-0-22 = refl
case-1-0-23 : R.isAccepted (R.run q1 q23 c0 refl) ≡ false
case-1-0-23 = refl
case-1-3-0 : R.isAccepted (R.run q1 q0 m1 refl) ≡ false
case-1-3-0 = refl
case-1-3-1 : R.isAccepted (R.run q1 q1 m1 refl) ≡ true
case-1-3-1 = refl
case-1-3-2 : R.isAccepted (R.run q1 q2 m1 refl) ≡ false
case-1-3-2 = refl
case-1-3-3 : R.isAccepted (R.run q1 q3 m1 refl) ≡ true
case-1-3-3 = refl
case-1-3-4 : R.isAccepted (R.run q1 q4 m1 refl) ≡ false
case-1-3-4 = refl
case-1-3-5 : R.isAccepted (R.run q1 q5 m1 refl) ≡ false
case-1-3-5 = refl
case-1-3-6 : R.isAccepted (R.run q1 q6 m1 refl) ≡ false
case-1-3-6 = refl
case-1-3-7 : R.isAccepted (R.run q1 q7 m1 refl) ≡ true
case-1-3-7 = refl
case-1-3-8 : R.isAccepted (R.run q1 q8 m1 refl) ≡ false
case-1-3-8 = refl
case-1-3-9 : R.isAccepted (R.run q1 q9 m1 refl) ≡ true
case-1-3-9 = refl
case-1-3-10 : R.isAccepted (R.run q1 q10 m1 refl) ≡ false
case-1-3-10 = refl
case-1-3-11 : R.isAccepted (R.run q1 q11 m1 refl) ≡ false
case-1-3-11 = refl
case-1-3-12 : R.isAccepted (R.run q1 q12 m1 refl) ≡ false
case-1-3-12 = refl
case-1-3-13 : R.isAccepted (R.run q1 q13 m1 refl) ≡ true
case-1-3-13 = refl
case-1-3-14 : R.isAccepted (R.run q1 q14 m1 refl) ≡ false
case-1-3-14 = refl
case-1-3-15 : R.isAccepted (R.run q1 q15 m1 refl) ≡ true
case-1-3-15 = refl
case-1-3-16 : R.isAccepted (R.run q1 q16 m1 refl) ≡ false
case-1-3-16 = refl
case-1-3-17 : R.isAccepted (R.run q1 q17 m1 refl) ≡ false
case-1-3-17 = refl
case-1-3-18 : R.isAccepted (R.run q1 q18 m1 refl) ≡ true
case-1-3-18 = refl
case-1-3-19 : R.isAccepted (R.run q1 q19 m1 refl) ≡ true
case-1-3-19 = refl
case-1-3-20 : R.isAccepted (R.run q1 q20 m1 refl) ≡ true
case-1-3-20 = refl
case-1-3-21 : R.isAccepted (R.run q1 q21 m1 refl) ≡ true
case-1-3-21 = refl
case-1-3-22 : R.isAccepted (R.run q1 q22 m1 refl) ≡ true
case-1-3-22 = refl
case-1-3-23 : R.isAccepted (R.run q1 q23 m1 refl) ≡ true
case-1-3-23 = refl
case-2-0-0 : R.isAccepted (R.run q2 q0 c0 refl) ≡ true
case-2-0-0 = refl
case-2-0-1 : R.isAccepted (R.run q2 q1 c0 refl) ≡ true
case-2-0-1 = refl
case-2-0-2 : R.isAccepted (R.run q2 q2 c0 refl) ≡ true
case-2-0-2 = refl
case-2-0-3 : R.isAccepted (R.run q2 q3 c0 refl) ≡ true
case-2-0-3 = refl
case-2-0-4 : R.isAccepted (R.run q2 q4 c0 refl) ≡ true
case-2-0-4 = refl
case-2-0-5 : R.isAccepted (R.run q2 q5 c0 refl) ≡ true
case-2-0-5 = refl
case-2-0-6 : R.isAccepted (R.run q2 q6 c0 refl) ≡ false
case-2-0-6 = refl
case-2-0-7 : R.isAccepted (R.run q2 q7 c0 refl) ≡ false
case-2-0-7 = refl
case-2-0-8 : R.isAccepted (R.run q2 q8 c0 refl) ≡ true
case-2-0-8 = refl
case-2-0-9 : R.isAccepted (R.run q2 q9 c0 refl) ≡ false
case-2-0-9 = refl
case-2-0-10 : R.isAccepted (R.run q2 q10 c0 refl) ≡ true
case-2-0-10 = refl
case-2-0-11 : R.isAccepted (R.run q2 q11 c0 refl) ≡ false
case-2-0-11 = refl
case-2-0-12 : R.isAccepted (R.run q2 q12 c0 refl) ≡ false
case-2-0-12 = refl
case-2-0-13 : R.isAccepted (R.run q2 q13 c0 refl) ≡ false
case-2-0-13 = refl
case-2-0-14 : R.isAccepted (R.run q2 q14 c0 refl) ≡ true
case-2-0-14 = refl
case-2-0-15 : R.isAccepted (R.run q2 q15 c0 refl) ≡ false
case-2-0-15 = refl
case-2-0-16 : R.isAccepted (R.run q2 q16 c0 refl) ≡ true
case-2-0-16 = refl
case-2-0-17 : R.isAccepted (R.run q2 q17 c0 refl) ≡ false
case-2-0-17 = refl
case-2-0-18 : R.isAccepted (R.run q2 q18 c0 refl) ≡ false
case-2-0-18 = refl
case-2-0-19 : R.isAccepted (R.run q2 q19 c0 refl) ≡ false
case-2-0-19 = refl
case-2-0-20 : R.isAccepted (R.run q2 q20 c0 refl) ≡ true
case-2-0-20 = refl
case-2-0-21 : R.isAccepted (R.run q2 q21 c0 refl) ≡ false
case-2-0-21 = refl
case-2-0-22 : R.isAccepted (R.run q2 q22 c0 refl) ≡ true
case-2-0-22 = refl
case-2-0-23 : R.isAccepted (R.run q2 q23 c0 refl) ≡ false
case-2-0-23 = refl
case-2-1-0 : R.isAccepted (R.run q2 q0 m0 refl) ≡ false
case-2-1-0 = refl
case-2-1-1 : R.isAccepted (R.run q2 q1 m0 refl) ≡ false
case-2-1-1 = refl
case-2-1-2 : R.isAccepted (R.run q2 q2 m0 refl) ≡ true
case-2-1-2 = refl
case-2-1-3 : R.isAccepted (R.run q2 q3 m0 refl) ≡ false
case-2-1-3 = refl
case-2-1-4 : R.isAccepted (R.run q2 q4 m0 refl) ≡ true
case-2-1-4 = refl
case-2-1-5 : R.isAccepted (R.run q2 q5 m0 refl) ≡ false
case-2-1-5 = refl
case-2-1-6 : R.isAccepted (R.run q2 q6 m0 refl) ≡ true
case-2-1-6 = refl
case-2-1-7 : R.isAccepted (R.run q2 q7 m0 refl) ≡ true
case-2-1-7 = refl
case-2-1-8 : R.isAccepted (R.run q2 q8 m0 refl) ≡ true
case-2-1-8 = refl
case-2-1-9 : R.isAccepted (R.run q2 q9 m0 refl) ≡ true
case-2-1-9 = refl
case-2-1-10 : R.isAccepted (R.run q2 q10 m0 refl) ≡ true
case-2-1-10 = refl
case-2-1-11 : R.isAccepted (R.run q2 q11 m0 refl) ≡ true
case-2-1-11 = refl
case-2-1-12 : R.isAccepted (R.run q2 q12 m0 refl) ≡ true
case-2-1-12 = refl
case-2-1-13 : R.isAccepted (R.run q2 q13 m0 refl) ≡ false
case-2-1-13 = refl
case-2-1-14 : R.isAccepted (R.run q2 q14 m0 refl) ≡ false
case-2-1-14 = refl
case-2-1-15 : R.isAccepted (R.run q2 q15 m0 refl) ≡ false
case-2-1-15 = refl
case-2-1-16 : R.isAccepted (R.run q2 q16 m0 refl) ≡ false
case-2-1-16 = refl
case-2-1-17 : R.isAccepted (R.run q2 q17 m0 refl) ≡ true
case-2-1-17 = refl
case-2-1-18 : R.isAccepted (R.run q2 q18 m0 refl) ≡ true
case-2-1-18 = refl
case-2-1-19 : R.isAccepted (R.run q2 q19 m0 refl) ≡ false
case-2-1-19 = refl
case-2-1-20 : R.isAccepted (R.run q2 q20 m0 refl) ≡ false
case-2-1-20 = refl
case-2-1-21 : R.isAccepted (R.run q2 q21 m0 refl) ≡ false
case-2-1-21 = refl
case-2-1-22 : R.isAccepted (R.run q2 q22 m0 refl) ≡ false
case-2-1-22 = refl
case-2-1-23 : R.isAccepted (R.run q2 q23 m0 refl) ≡ true
case-2-1-23 = refl
case-3-0-0 : R.isAccepted (R.run q3 q0 c0 refl) ≡ true
case-3-0-0 = refl
case-3-0-1 : R.isAccepted (R.run q3 q1 c0 refl) ≡ true
case-3-0-1 = refl
case-3-0-2 : R.isAccepted (R.run q3 q2 c0 refl) ≡ true
case-3-0-2 = refl
case-3-0-3 : R.isAccepted (R.run q3 q3 c0 refl) ≡ true
case-3-0-3 = refl
case-3-0-4 : R.isAccepted (R.run q3 q4 c0 refl) ≡ true
case-3-0-4 = refl
case-3-0-5 : R.isAccepted (R.run q3 q5 c0 refl) ≡ true
case-3-0-5 = refl
case-3-0-6 : R.isAccepted (R.run q3 q6 c0 refl) ≡ false
case-3-0-6 = refl
case-3-0-7 : R.isAccepted (R.run q3 q7 c0 refl) ≡ false
case-3-0-7 = refl
case-3-0-8 : R.isAccepted (R.run q3 q8 c0 refl) ≡ true
case-3-0-8 = refl
case-3-0-9 : R.isAccepted (R.run q3 q9 c0 refl) ≡ false
case-3-0-9 = refl
case-3-0-10 : R.isAccepted (R.run q3 q10 c0 refl) ≡ true
case-3-0-10 = refl
case-3-0-11 : R.isAccepted (R.run q3 q11 c0 refl) ≡ false
case-3-0-11 = refl
case-3-0-12 : R.isAccepted (R.run q3 q12 c0 refl) ≡ false
case-3-0-12 = refl
case-3-0-13 : R.isAccepted (R.run q3 q13 c0 refl) ≡ false
case-3-0-13 = refl
case-3-0-14 : R.isAccepted (R.run q3 q14 c0 refl) ≡ true
case-3-0-14 = refl
case-3-0-15 : R.isAccepted (R.run q3 q15 c0 refl) ≡ false
case-3-0-15 = refl
case-3-0-16 : R.isAccepted (R.run q3 q16 c0 refl) ≡ true
case-3-0-16 = refl
case-3-0-17 : R.isAccepted (R.run q3 q17 c0 refl) ≡ false
case-3-0-17 = refl
case-3-0-18 : R.isAccepted (R.run q3 q18 c0 refl) ≡ false
case-3-0-18 = refl
case-3-0-19 : R.isAccepted (R.run q3 q19 c0 refl) ≡ false
case-3-0-19 = refl
case-3-0-20 : R.isAccepted (R.run q3 q20 c0 refl) ≡ true
case-3-0-20 = refl
case-3-0-21 : R.isAccepted (R.run q3 q21 c0 refl) ≡ false
case-3-0-21 = refl
case-3-0-22 : R.isAccepted (R.run q3 q22 c0 refl) ≡ true
case-3-0-22 = refl
case-3-0-23 : R.isAccepted (R.run q3 q23 c0 refl) ≡ false
case-3-0-23 = refl
case-3-3-0 : R.isAccepted (R.run q3 q0 m1 refl) ≡ false
case-3-3-0 = refl
case-3-3-1 : R.isAccepted (R.run q3 q1 m1 refl) ≡ true
case-3-3-1 = refl
case-3-3-2 : R.isAccepted (R.run q3 q2 m1 refl) ≡ false
case-3-3-2 = refl
case-3-3-3 : R.isAccepted (R.run q3 q3 m1 refl) ≡ true
case-3-3-3 = refl
case-3-3-4 : R.isAccepted (R.run q3 q4 m1 refl) ≡ false
case-3-3-4 = refl
case-3-3-5 : R.isAccepted (R.run q3 q5 m1 refl) ≡ false
case-3-3-5 = refl
case-3-3-6 : R.isAccepted (R.run q3 q6 m1 refl) ≡ false
case-3-3-6 = refl
case-3-3-7 : R.isAccepted (R.run q3 q7 m1 refl) ≡ true
case-3-3-7 = refl
case-3-3-8 : R.isAccepted (R.run q3 q8 m1 refl) ≡ false
case-3-3-8 = refl
case-3-3-9 : R.isAccepted (R.run q3 q9 m1 refl) ≡ true
case-3-3-9 = refl
case-3-3-10 : R.isAccepted (R.run q3 q10 m1 refl) ≡ false
case-3-3-10 = refl
case-3-3-11 : R.isAccepted (R.run q3 q11 m1 refl) ≡ false
case-3-3-11 = refl
case-3-3-12 : R.isAccepted (R.run q3 q12 m1 refl) ≡ false
case-3-3-12 = refl
case-3-3-13 : R.isAccepted (R.run q3 q13 m1 refl) ≡ true
case-3-3-13 = refl
case-3-3-14 : R.isAccepted (R.run q3 q14 m1 refl) ≡ false
case-3-3-14 = refl
case-3-3-15 : R.isAccepted (R.run q3 q15 m1 refl) ≡ true
case-3-3-15 = refl
case-3-3-16 : R.isAccepted (R.run q3 q16 m1 refl) ≡ false
case-3-3-16 = refl
case-3-3-17 : R.isAccepted (R.run q3 q17 m1 refl) ≡ false
case-3-3-17 = refl
case-3-3-18 : R.isAccepted (R.run q3 q18 m1 refl) ≡ true
case-3-3-18 = refl
case-3-3-19 : R.isAccepted (R.run q3 q19 m1 refl) ≡ true
case-3-3-19 = refl
case-3-3-20 : R.isAccepted (R.run q3 q20 m1 refl) ≡ true
case-3-3-20 = refl
case-3-3-21 : R.isAccepted (R.run q3 q21 m1 refl) ≡ true
case-3-3-21 = refl
case-3-3-22 : R.isAccepted (R.run q3 q22 m1 refl) ≡ true
case-3-3-22 = refl
case-3-3-23 : R.isAccepted (R.run q3 q23 m1 refl) ≡ true
case-3-3-23 = refl
case-4-0-0 : R.isAccepted (R.run q4 q0 c0 refl) ≡ true
case-4-0-0 = refl
case-4-0-1 : R.isAccepted (R.run q4 q1 c0 refl) ≡ true
case-4-0-1 = refl
case-4-0-2 : R.isAccepted (R.run q4 q2 c0 refl) ≡ true
case-4-0-2 = refl
case-4-0-3 : R.isAccepted (R.run q4 q3 c0 refl) ≡ true
case-4-0-3 = refl
case-4-0-4 : R.isAccepted (R.run q4 q4 c0 refl) ≡ true
case-4-0-4 = refl
case-4-0-5 : R.isAccepted (R.run q4 q5 c0 refl) ≡ true
case-4-0-5 = refl
case-4-0-6 : R.isAccepted (R.run q4 q6 c0 refl) ≡ false
case-4-0-6 = refl
case-4-0-7 : R.isAccepted (R.run q4 q7 c0 refl) ≡ false
case-4-0-7 = refl
case-4-0-8 : R.isAccepted (R.run q4 q8 c0 refl) ≡ true
case-4-0-8 = refl
case-4-0-9 : R.isAccepted (R.run q4 q9 c0 refl) ≡ false
case-4-0-9 = refl
case-4-0-10 : R.isAccepted (R.run q4 q10 c0 refl) ≡ true
case-4-0-10 = refl
case-4-0-11 : R.isAccepted (R.run q4 q11 c0 refl) ≡ false
case-4-0-11 = refl
case-4-0-12 : R.isAccepted (R.run q4 q12 c0 refl) ≡ false
case-4-0-12 = refl
case-4-0-13 : R.isAccepted (R.run q4 q13 c0 refl) ≡ false
case-4-0-13 = refl
case-4-0-14 : R.isAccepted (R.run q4 q14 c0 refl) ≡ true
case-4-0-14 = refl
case-4-0-15 : R.isAccepted (R.run q4 q15 c0 refl) ≡ false
case-4-0-15 = refl
case-4-0-16 : R.isAccepted (R.run q4 q16 c0 refl) ≡ true
case-4-0-16 = refl
case-4-0-17 : R.isAccepted (R.run q4 q17 c0 refl) ≡ false
case-4-0-17 = refl
case-4-0-18 : R.isAccepted (R.run q4 q18 c0 refl) ≡ false
case-4-0-18 = refl
case-4-0-19 : R.isAccepted (R.run q4 q19 c0 refl) ≡ false
case-4-0-19 = refl
case-4-0-20 : R.isAccepted (R.run q4 q20 c0 refl) ≡ true
case-4-0-20 = refl
case-4-0-21 : R.isAccepted (R.run q4 q21 c0 refl) ≡ false
case-4-0-21 = refl
case-4-0-22 : R.isAccepted (R.run q4 q22 c0 refl) ≡ true
case-4-0-22 = refl
case-4-0-23 : R.isAccepted (R.run q4 q23 c0 refl) ≡ false
case-4-0-23 = refl
case-4-1-0 : R.isAccepted (R.run q4 q0 m0 refl) ≡ false
case-4-1-0 = refl
case-4-1-1 : R.isAccepted (R.run q4 q1 m0 refl) ≡ false
case-4-1-1 = refl
case-4-1-2 : R.isAccepted (R.run q4 q2 m0 refl) ≡ true
case-4-1-2 = refl
case-4-1-3 : R.isAccepted (R.run q4 q3 m0 refl) ≡ false
case-4-1-3 = refl
case-4-1-4 : R.isAccepted (R.run q4 q4 m0 refl) ≡ true
case-4-1-4 = refl
case-4-1-5 : R.isAccepted (R.run q4 q5 m0 refl) ≡ false
case-4-1-5 = refl
case-4-1-6 : R.isAccepted (R.run q4 q6 m0 refl) ≡ true
case-4-1-6 = refl
case-4-1-7 : R.isAccepted (R.run q4 q7 m0 refl) ≡ true
case-4-1-7 = refl
case-4-1-8 : R.isAccepted (R.run q4 q8 m0 refl) ≡ true
case-4-1-8 = refl
case-4-1-9 : R.isAccepted (R.run q4 q9 m0 refl) ≡ true
case-4-1-9 = refl
case-4-1-10 : R.isAccepted (R.run q4 q10 m0 refl) ≡ true
case-4-1-10 = refl
case-4-1-11 : R.isAccepted (R.run q4 q11 m0 refl) ≡ true
case-4-1-11 = refl
case-4-1-12 : R.isAccepted (R.run q4 q12 m0 refl) ≡ true
case-4-1-12 = refl
case-4-1-13 : R.isAccepted (R.run q4 q13 m0 refl) ≡ false
case-4-1-13 = refl
case-4-1-14 : R.isAccepted (R.run q4 q14 m0 refl) ≡ false
case-4-1-14 = refl
case-4-1-15 : R.isAccepted (R.run q4 q15 m0 refl) ≡ false
case-4-1-15 = refl
case-4-1-16 : R.isAccepted (R.run q4 q16 m0 refl) ≡ false
case-4-1-16 = refl
case-4-1-17 : R.isAccepted (R.run q4 q17 m0 refl) ≡ true
case-4-1-17 = refl
case-4-1-18 : R.isAccepted (R.run q4 q18 m0 refl) ≡ true
case-4-1-18 = refl
case-4-1-19 : R.isAccepted (R.run q4 q19 m0 refl) ≡ false
case-4-1-19 = refl
case-4-1-20 : R.isAccepted (R.run q4 q20 m0 refl) ≡ false
case-4-1-20 = refl
case-4-1-21 : R.isAccepted (R.run q4 q21 m0 refl) ≡ false
case-4-1-21 = refl
case-4-1-22 : R.isAccepted (R.run q4 q22 m0 refl) ≡ false
case-4-1-22 = refl
case-4-1-23 : R.isAccepted (R.run q4 q23 m0 refl) ≡ true
case-4-1-23 = refl
case-5-0-0 : R.isAccepted (R.run q5 q0 c0 refl) ≡ true
case-5-0-0 = refl
case-5-0-1 : R.isAccepted (R.run q5 q1 c0 refl) ≡ true
case-5-0-1 = refl
case-5-0-2 : R.isAccepted (R.run q5 q2 c0 refl) ≡ true
case-5-0-2 = refl
case-5-0-3 : R.isAccepted (R.run q5 q3 c0 refl) ≡ true
case-5-0-3 = refl
case-5-0-4 : R.isAccepted (R.run q5 q4 c0 refl) ≡ true
case-5-0-4 = refl
case-5-0-5 : R.isAccepted (R.run q5 q5 c0 refl) ≡ true
case-5-0-5 = refl
case-5-0-6 : R.isAccepted (R.run q5 q6 c0 refl) ≡ false
case-5-0-6 = refl
case-5-0-7 : R.isAccepted (R.run q5 q7 c0 refl) ≡ false
case-5-0-7 = refl
case-5-0-8 : R.isAccepted (R.run q5 q8 c0 refl) ≡ true
case-5-0-8 = refl
case-5-0-9 : R.isAccepted (R.run q5 q9 c0 refl) ≡ false
case-5-0-9 = refl
case-5-0-10 : R.isAccepted (R.run q5 q10 c0 refl) ≡ true
case-5-0-10 = refl
case-5-0-11 : R.isAccepted (R.run q5 q11 c0 refl) ≡ false
case-5-0-11 = refl
case-5-0-12 : R.isAccepted (R.run q5 q12 c0 refl) ≡ false
case-5-0-12 = refl
case-5-0-13 : R.isAccepted (R.run q5 q13 c0 refl) ≡ false
case-5-0-13 = refl
case-5-0-14 : R.isAccepted (R.run q5 q14 c0 refl) ≡ true
case-5-0-14 = refl
case-5-0-15 : R.isAccepted (R.run q5 q15 c0 refl) ≡ false
case-5-0-15 = refl
case-5-0-16 : R.isAccepted (R.run q5 q16 c0 refl) ≡ true
case-5-0-16 = refl
case-5-0-17 : R.isAccepted (R.run q5 q17 c0 refl) ≡ false
case-5-0-17 = refl
case-5-0-18 : R.isAccepted (R.run q5 q18 c0 refl) ≡ false
case-5-0-18 = refl
case-5-0-19 : R.isAccepted (R.run q5 q19 c0 refl) ≡ false
case-5-0-19 = refl
case-5-0-20 : R.isAccepted (R.run q5 q20 c0 refl) ≡ true
case-5-0-20 = refl
case-5-0-21 : R.isAccepted (R.run q5 q21 c0 refl) ≡ false
case-5-0-21 = refl
case-5-0-22 : R.isAccepted (R.run q5 q22 c0 refl) ≡ true
case-5-0-22 = refl
case-5-0-23 : R.isAccepted (R.run q5 q23 c0 refl) ≡ false
case-5-0-23 = refl
case-5-2-0 : R.isAccepted (R.run q5 q0 c1 refl) ≡ true
case-5-2-0 = refl
case-5-2-1 : R.isAccepted (R.run q5 q1 c1 refl) ≡ false
case-5-2-1 = refl
case-5-2-2 : R.isAccepted (R.run q5 q2 c1 refl) ≡ false
case-5-2-2 = refl
case-5-2-3 : R.isAccepted (R.run q5 q3 c1 refl) ≡ false
case-5-2-3 = refl
case-5-2-4 : R.isAccepted (R.run q5 q4 c1 refl) ≡ false
case-5-2-4 = refl
case-5-2-5 : R.isAccepted (R.run q5 q5 c1 refl) ≡ true
case-5-2-5 = refl
case-5-2-6 : R.isAccepted (R.run q5 q6 c1 refl) ≡ true
case-5-2-6 = refl
case-5-2-7 : R.isAccepted (R.run q5 q7 c1 refl) ≡ false
case-5-2-7 = refl
case-5-2-8 : R.isAccepted (R.run q5 q8 c1 refl) ≡ false
case-5-2-8 = refl
case-5-2-9 : R.isAccepted (R.run q5 q9 c1 refl) ≡ false
case-5-2-9 = refl
case-5-2-10 : R.isAccepted (R.run q5 q10 c1 refl) ≡ false
case-5-2-10 = refl
case-5-2-11 : R.isAccepted (R.run q5 q11 c1 refl) ≡ true
case-5-2-11 = refl
case-5-2-12 : R.isAccepted (R.run q5 q12 c1 refl) ≡ true
case-5-2-12 = refl
case-5-2-13 : R.isAccepted (R.run q5 q13 c1 refl) ≡ true
case-5-2-13 = refl
case-5-2-14 : R.isAccepted (R.run q5 q14 c1 refl) ≡ true
case-5-2-14 = refl
case-5-2-15 : R.isAccepted (R.run q5 q15 c1 refl) ≡ true
case-5-2-15 = refl
case-5-2-16 : R.isAccepted (R.run q5 q16 c1 refl) ≡ true
case-5-2-16 = refl
case-5-2-17 : R.isAccepted (R.run q5 q17 c1 refl) ≡ true
case-5-2-17 = refl
case-5-2-18 : R.isAccepted (R.run q5 q18 c1 refl) ≡ false
case-5-2-18 = refl
case-5-2-19 : R.isAccepted (R.run q5 q19 c1 refl) ≡ true
case-5-2-19 = refl
case-5-2-20 : R.isAccepted (R.run q5 q20 c1 refl) ≡ false
case-5-2-20 = refl
case-5-2-21 : R.isAccepted (R.run q5 q21 c1 refl) ≡ true
case-5-2-21 = refl
case-5-2-22 : R.isAccepted (R.run q5 q22 c1 refl) ≡ false
case-5-2-22 = refl
case-5-2-23 : R.isAccepted (R.run q5 q23 c1 refl) ≡ false
case-5-2-23 = refl
case-6-1-0 : R.isAccepted (R.run q6 q0 m0 refl) ≡ false
case-6-1-0 = refl
case-6-1-1 : R.isAccepted (R.run q6 q1 m0 refl) ≡ false
case-6-1-1 = refl
case-6-1-2 : R.isAccepted (R.run q6 q2 m0 refl) ≡ true
case-6-1-2 = refl
case-6-1-3 : R.isAccepted (R.run q6 q3 m0 refl) ≡ false
case-6-1-3 = refl
case-6-1-4 : R.isAccepted (R.run q6 q4 m0 refl) ≡ true
case-6-1-4 = refl
case-6-1-5 : R.isAccepted (R.run q6 q5 m0 refl) ≡ false
case-6-1-5 = refl
case-6-1-6 : R.isAccepted (R.run q6 q6 m0 refl) ≡ true
case-6-1-6 = refl
case-6-1-7 : R.isAccepted (R.run q6 q7 m0 refl) ≡ true
case-6-1-7 = refl
case-6-1-8 : R.isAccepted (R.run q6 q8 m0 refl) ≡ true
case-6-1-8 = refl
case-6-1-9 : R.isAccepted (R.run q6 q9 m0 refl) ≡ true
case-6-1-9 = refl
case-6-1-10 : R.isAccepted (R.run q6 q10 m0 refl) ≡ true
case-6-1-10 = refl
case-6-1-11 : R.isAccepted (R.run q6 q11 m0 refl) ≡ true
case-6-1-11 = refl
case-6-1-12 : R.isAccepted (R.run q6 q12 m0 refl) ≡ true
case-6-1-12 = refl
case-6-1-13 : R.isAccepted (R.run q6 q13 m0 refl) ≡ false
case-6-1-13 = refl
case-6-1-14 : R.isAccepted (R.run q6 q14 m0 refl) ≡ false
case-6-1-14 = refl
case-6-1-15 : R.isAccepted (R.run q6 q15 m0 refl) ≡ false
case-6-1-15 = refl
case-6-1-16 : R.isAccepted (R.run q6 q16 m0 refl) ≡ false
case-6-1-16 = refl
case-6-1-17 : R.isAccepted (R.run q6 q17 m0 refl) ≡ true
case-6-1-17 = refl
case-6-1-18 : R.isAccepted (R.run q6 q18 m0 refl) ≡ true
case-6-1-18 = refl
case-6-1-19 : R.isAccepted (R.run q6 q19 m0 refl) ≡ false
case-6-1-19 = refl
case-6-1-20 : R.isAccepted (R.run q6 q20 m0 refl) ≡ false
case-6-1-20 = refl
case-6-1-21 : R.isAccepted (R.run q6 q21 m0 refl) ≡ false
case-6-1-21 = refl
case-6-1-22 : R.isAccepted (R.run q6 q22 m0 refl) ≡ false
case-6-1-22 = refl
case-6-1-23 : R.isAccepted (R.run q6 q23 m0 refl) ≡ true
case-6-1-23 = refl
case-6-2-0 : R.isAccepted (R.run q6 q0 c1 refl) ≡ true
case-6-2-0 = refl
case-6-2-1 : R.isAccepted (R.run q6 q1 c1 refl) ≡ false
case-6-2-1 = refl
case-6-2-2 : R.isAccepted (R.run q6 q2 c1 refl) ≡ false
case-6-2-2 = refl
case-6-2-3 : R.isAccepted (R.run q6 q3 c1 refl) ≡ false
case-6-2-3 = refl
case-6-2-4 : R.isAccepted (R.run q6 q4 c1 refl) ≡ false
case-6-2-4 = refl
case-6-2-5 : R.isAccepted (R.run q6 q5 c1 refl) ≡ true
case-6-2-5 = refl
case-6-2-6 : R.isAccepted (R.run q6 q6 c1 refl) ≡ true
case-6-2-6 = refl
case-6-2-7 : R.isAccepted (R.run q6 q7 c1 refl) ≡ false
case-6-2-7 = refl
case-6-2-8 : R.isAccepted (R.run q6 q8 c1 refl) ≡ false
case-6-2-8 = refl
case-6-2-9 : R.isAccepted (R.run q6 q9 c1 refl) ≡ false
case-6-2-9 = refl
case-6-2-10 : R.isAccepted (R.run q6 q10 c1 refl) ≡ false
case-6-2-10 = refl
case-6-2-11 : R.isAccepted (R.run q6 q11 c1 refl) ≡ true
case-6-2-11 = refl
case-6-2-12 : R.isAccepted (R.run q6 q12 c1 refl) ≡ true
case-6-2-12 = refl
case-6-2-13 : R.isAccepted (R.run q6 q13 c1 refl) ≡ true
case-6-2-13 = refl
case-6-2-14 : R.isAccepted (R.run q6 q14 c1 refl) ≡ true
case-6-2-14 = refl
case-6-2-15 : R.isAccepted (R.run q6 q15 c1 refl) ≡ true
case-6-2-15 = refl
case-6-2-16 : R.isAccepted (R.run q6 q16 c1 refl) ≡ true
case-6-2-16 = refl
case-6-2-17 : R.isAccepted (R.run q6 q17 c1 refl) ≡ true
case-6-2-17 = refl
case-6-2-18 : R.isAccepted (R.run q6 q18 c1 refl) ≡ false
case-6-2-18 = refl
case-6-2-19 : R.isAccepted (R.run q6 q19 c1 refl) ≡ true
case-6-2-19 = refl
case-6-2-20 : R.isAccepted (R.run q6 q20 c1 refl) ≡ false
case-6-2-20 = refl
case-6-2-21 : R.isAccepted (R.run q6 q21 c1 refl) ≡ true
case-6-2-21 = refl
case-6-2-22 : R.isAccepted (R.run q6 q22 c1 refl) ≡ false
case-6-2-22 = refl
case-6-2-23 : R.isAccepted (R.run q6 q23 c1 refl) ≡ false
case-6-2-23 = refl
case-7-1-0 : R.isAccepted (R.run q7 q0 m0 refl) ≡ false
case-7-1-0 = refl
case-7-1-1 : R.isAccepted (R.run q7 q1 m0 refl) ≡ false
case-7-1-1 = refl
case-7-1-2 : R.isAccepted (R.run q7 q2 m0 refl) ≡ true
case-7-1-2 = refl
case-7-1-3 : R.isAccepted (R.run q7 q3 m0 refl) ≡ false
case-7-1-3 = refl
case-7-1-4 : R.isAccepted (R.run q7 q4 m0 refl) ≡ true
case-7-1-4 = refl
case-7-1-5 : R.isAccepted (R.run q7 q5 m0 refl) ≡ false
case-7-1-5 = refl
case-7-1-6 : R.isAccepted (R.run q7 q6 m0 refl) ≡ true
case-7-1-6 = refl
case-7-1-7 : R.isAccepted (R.run q7 q7 m0 refl) ≡ true
case-7-1-7 = refl
case-7-1-8 : R.isAccepted (R.run q7 q8 m0 refl) ≡ true
case-7-1-8 = refl
case-7-1-9 : R.isAccepted (R.run q7 q9 m0 refl) ≡ true
case-7-1-9 = refl
case-7-1-10 : R.isAccepted (R.run q7 q10 m0 refl) ≡ true
case-7-1-10 = refl
case-7-1-11 : R.isAccepted (R.run q7 q11 m0 refl) ≡ true
case-7-1-11 = refl
case-7-1-12 : R.isAccepted (R.run q7 q12 m0 refl) ≡ true
case-7-1-12 = refl
case-7-1-13 : R.isAccepted (R.run q7 q13 m0 refl) ≡ false
case-7-1-13 = refl
case-7-1-14 : R.isAccepted (R.run q7 q14 m0 refl) ≡ false
case-7-1-14 = refl
case-7-1-15 : R.isAccepted (R.run q7 q15 m0 refl) ≡ false
case-7-1-15 = refl
case-7-1-16 : R.isAccepted (R.run q7 q16 m0 refl) ≡ false
case-7-1-16 = refl
case-7-1-17 : R.isAccepted (R.run q7 q17 m0 refl) ≡ true
case-7-1-17 = refl
case-7-1-18 : R.isAccepted (R.run q7 q18 m0 refl) ≡ true
case-7-1-18 = refl
case-7-1-19 : R.isAccepted (R.run q7 q19 m0 refl) ≡ false
case-7-1-19 = refl
case-7-1-20 : R.isAccepted (R.run q7 q20 m0 refl) ≡ false
case-7-1-20 = refl
case-7-1-21 : R.isAccepted (R.run q7 q21 m0 refl) ≡ false
case-7-1-21 = refl
case-7-1-22 : R.isAccepted (R.run q7 q22 m0 refl) ≡ false
case-7-1-22 = refl
case-7-1-23 : R.isAccepted (R.run q7 q23 m0 refl) ≡ true
case-7-1-23 = refl
case-7-3-0 : R.isAccepted (R.run q7 q0 m1 refl) ≡ false
case-7-3-0 = refl
case-7-3-1 : R.isAccepted (R.run q7 q1 m1 refl) ≡ true
case-7-3-1 = refl
case-7-3-2 : R.isAccepted (R.run q7 q2 m1 refl) ≡ false
case-7-3-2 = refl
case-7-3-3 : R.isAccepted (R.run q7 q3 m1 refl) ≡ true
case-7-3-3 = refl
case-7-3-4 : R.isAccepted (R.run q7 q4 m1 refl) ≡ false
case-7-3-4 = refl
case-7-3-5 : R.isAccepted (R.run q7 q5 m1 refl) ≡ false
case-7-3-5 = refl
case-7-3-6 : R.isAccepted (R.run q7 q6 m1 refl) ≡ false
case-7-3-6 = refl
case-7-3-7 : R.isAccepted (R.run q7 q7 m1 refl) ≡ true
case-7-3-7 = refl
case-7-3-8 : R.isAccepted (R.run q7 q8 m1 refl) ≡ false
case-7-3-8 = refl
case-7-3-9 : R.isAccepted (R.run q7 q9 m1 refl) ≡ true
case-7-3-9 = refl
case-7-3-10 : R.isAccepted (R.run q7 q10 m1 refl) ≡ false
case-7-3-10 = refl
case-7-3-11 : R.isAccepted (R.run q7 q11 m1 refl) ≡ false
case-7-3-11 = refl
case-7-3-12 : R.isAccepted (R.run q7 q12 m1 refl) ≡ false
case-7-3-12 = refl
case-7-3-13 : R.isAccepted (R.run q7 q13 m1 refl) ≡ true
case-7-3-13 = refl
case-7-3-14 : R.isAccepted (R.run q7 q14 m1 refl) ≡ false
case-7-3-14 = refl
case-7-3-15 : R.isAccepted (R.run q7 q15 m1 refl) ≡ true
case-7-3-15 = refl
case-7-3-16 : R.isAccepted (R.run q7 q16 m1 refl) ≡ false
case-7-3-16 = refl
case-7-3-17 : R.isAccepted (R.run q7 q17 m1 refl) ≡ false
case-7-3-17 = refl
case-7-3-18 : R.isAccepted (R.run q7 q18 m1 refl) ≡ true
case-7-3-18 = refl
case-7-3-19 : R.isAccepted (R.run q7 q19 m1 refl) ≡ true
case-7-3-19 = refl
case-7-3-20 : R.isAccepted (R.run q7 q20 m1 refl) ≡ true
case-7-3-20 = refl
case-7-3-21 : R.isAccepted (R.run q7 q21 m1 refl) ≡ true
case-7-3-21 = refl
case-7-3-22 : R.isAccepted (R.run q7 q22 m1 refl) ≡ true
case-7-3-22 = refl
case-7-3-23 : R.isAccepted (R.run q7 q23 m1 refl) ≡ true
case-7-3-23 = refl
case-8-0-0 : R.isAccepted (R.run q8 q0 c0 refl) ≡ true
case-8-0-0 = refl
case-8-0-1 : R.isAccepted (R.run q8 q1 c0 refl) ≡ true
case-8-0-1 = refl
case-8-0-2 : R.isAccepted (R.run q8 q2 c0 refl) ≡ true
case-8-0-2 = refl
case-8-0-3 : R.isAccepted (R.run q8 q3 c0 refl) ≡ true
case-8-0-3 = refl
case-8-0-4 : R.isAccepted (R.run q8 q4 c0 refl) ≡ true
case-8-0-4 = refl
case-8-0-5 : R.isAccepted (R.run q8 q5 c0 refl) ≡ true
case-8-0-5 = refl
case-8-0-6 : R.isAccepted (R.run q8 q6 c0 refl) ≡ false
case-8-0-6 = refl
case-8-0-7 : R.isAccepted (R.run q8 q7 c0 refl) ≡ false
case-8-0-7 = refl
case-8-0-8 : R.isAccepted (R.run q8 q8 c0 refl) ≡ true
case-8-0-8 = refl
case-8-0-9 : R.isAccepted (R.run q8 q9 c0 refl) ≡ false
case-8-0-9 = refl
case-8-0-10 : R.isAccepted (R.run q8 q10 c0 refl) ≡ true
case-8-0-10 = refl
case-8-0-11 : R.isAccepted (R.run q8 q11 c0 refl) ≡ false
case-8-0-11 = refl
case-8-0-12 : R.isAccepted (R.run q8 q12 c0 refl) ≡ false
case-8-0-12 = refl
case-8-0-13 : R.isAccepted (R.run q8 q13 c0 refl) ≡ false
case-8-0-13 = refl
case-8-0-14 : R.isAccepted (R.run q8 q14 c0 refl) ≡ true
case-8-0-14 = refl
case-8-0-15 : R.isAccepted (R.run q8 q15 c0 refl) ≡ false
case-8-0-15 = refl
case-8-0-16 : R.isAccepted (R.run q8 q16 c0 refl) ≡ true
case-8-0-16 = refl
case-8-0-17 : R.isAccepted (R.run q8 q17 c0 refl) ≡ false
case-8-0-17 = refl
case-8-0-18 : R.isAccepted (R.run q8 q18 c0 refl) ≡ false
case-8-0-18 = refl
case-8-0-19 : R.isAccepted (R.run q8 q19 c0 refl) ≡ false
case-8-0-19 = refl
case-8-0-20 : R.isAccepted (R.run q8 q20 c0 refl) ≡ true
case-8-0-20 = refl
case-8-0-21 : R.isAccepted (R.run q8 q21 c0 refl) ≡ false
case-8-0-21 = refl
case-8-0-22 : R.isAccepted (R.run q8 q22 c0 refl) ≡ true
case-8-0-22 = refl
case-8-0-23 : R.isAccepted (R.run q8 q23 c0 refl) ≡ false
case-8-0-23 = refl
case-8-1-0 : R.isAccepted (R.run q8 q0 m0 refl) ≡ false
case-8-1-0 = refl
case-8-1-1 : R.isAccepted (R.run q8 q1 m0 refl) ≡ false
case-8-1-1 = refl
case-8-1-2 : R.isAccepted (R.run q8 q2 m0 refl) ≡ true
case-8-1-2 = refl
case-8-1-3 : R.isAccepted (R.run q8 q3 m0 refl) ≡ false
case-8-1-3 = refl
case-8-1-4 : R.isAccepted (R.run q8 q4 m0 refl) ≡ true
case-8-1-4 = refl
case-8-1-5 : R.isAccepted (R.run q8 q5 m0 refl) ≡ false
case-8-1-5 = refl
case-8-1-6 : R.isAccepted (R.run q8 q6 m0 refl) ≡ true
case-8-1-6 = refl
case-8-1-7 : R.isAccepted (R.run q8 q7 m0 refl) ≡ true
case-8-1-7 = refl
case-8-1-8 : R.isAccepted (R.run q8 q8 m0 refl) ≡ true
case-8-1-8 = refl
case-8-1-9 : R.isAccepted (R.run q8 q9 m0 refl) ≡ true
case-8-1-9 = refl
case-8-1-10 : R.isAccepted (R.run q8 q10 m0 refl) ≡ true
case-8-1-10 = refl
case-8-1-11 : R.isAccepted (R.run q8 q11 m0 refl) ≡ true
case-8-1-11 = refl
case-8-1-12 : R.isAccepted (R.run q8 q12 m0 refl) ≡ true
case-8-1-12 = refl
case-8-1-13 : R.isAccepted (R.run q8 q13 m0 refl) ≡ false
case-8-1-13 = refl
case-8-1-14 : R.isAccepted (R.run q8 q14 m0 refl) ≡ false
case-8-1-14 = refl
case-8-1-15 : R.isAccepted (R.run q8 q15 m0 refl) ≡ false
case-8-1-15 = refl
case-8-1-16 : R.isAccepted (R.run q8 q16 m0 refl) ≡ false
case-8-1-16 = refl
case-8-1-17 : R.isAccepted (R.run q8 q17 m0 refl) ≡ true
case-8-1-17 = refl
case-8-1-18 : R.isAccepted (R.run q8 q18 m0 refl) ≡ true
case-8-1-18 = refl
case-8-1-19 : R.isAccepted (R.run q8 q19 m0 refl) ≡ false
case-8-1-19 = refl
case-8-1-20 : R.isAccepted (R.run q8 q20 m0 refl) ≡ false
case-8-1-20 = refl
case-8-1-21 : R.isAccepted (R.run q8 q21 m0 refl) ≡ false
case-8-1-21 = refl
case-8-1-22 : R.isAccepted (R.run q8 q22 m0 refl) ≡ false
case-8-1-22 = refl
case-8-1-23 : R.isAccepted (R.run q8 q23 m0 refl) ≡ true
case-8-1-23 = refl
case-9-1-0 : R.isAccepted (R.run q9 q0 m0 refl) ≡ false
case-9-1-0 = refl
case-9-1-1 : R.isAccepted (R.run q9 q1 m0 refl) ≡ false
case-9-1-1 = refl
case-9-1-2 : R.isAccepted (R.run q9 q2 m0 refl) ≡ true
case-9-1-2 = refl
case-9-1-3 : R.isAccepted (R.run q9 q3 m0 refl) ≡ false
case-9-1-3 = refl
case-9-1-4 : R.isAccepted (R.run q9 q4 m0 refl) ≡ true
case-9-1-4 = refl
case-9-1-5 : R.isAccepted (R.run q9 q5 m0 refl) ≡ false
case-9-1-5 = refl
case-9-1-6 : R.isAccepted (R.run q9 q6 m0 refl) ≡ true
case-9-1-6 = refl
case-9-1-7 : R.isAccepted (R.run q9 q7 m0 refl) ≡ true
case-9-1-7 = refl
case-9-1-8 : R.isAccepted (R.run q9 q8 m0 refl) ≡ true
case-9-1-8 = refl
case-9-1-9 : R.isAccepted (R.run q9 q9 m0 refl) ≡ true
case-9-1-9 = refl
case-9-1-10 : R.isAccepted (R.run q9 q10 m0 refl) ≡ true
case-9-1-10 = refl
case-9-1-11 : R.isAccepted (R.run q9 q11 m0 refl) ≡ true
case-9-1-11 = refl
case-9-1-12 : R.isAccepted (R.run q9 q12 m0 refl) ≡ true
case-9-1-12 = refl
case-9-1-13 : R.isAccepted (R.run q9 q13 m0 refl) ≡ false
case-9-1-13 = refl
case-9-1-14 : R.isAccepted (R.run q9 q14 m0 refl) ≡ false
case-9-1-14 = refl
case-9-1-15 : R.isAccepted (R.run q9 q15 m0 refl) ≡ false
case-9-1-15 = refl
case-9-1-16 : R.isAccepted (R.run q9 q16 m0 refl) ≡ false
case-9-1-16 = refl
case-9-1-17 : R.isAccepted (R.run q9 q17 m0 refl) ≡ true
case-9-1-17 = refl
case-9-1-18 : R.isAccepted (R.run q9 q18 m0 refl) ≡ true
case-9-1-18 = refl
case-9-1-19 : R.isAccepted (R.run q9 q19 m0 refl) ≡ false
case-9-1-19 = refl
case-9-1-20 : R.isAccepted (R.run q9 q20 m0 refl) ≡ false
case-9-1-20 = refl
case-9-1-21 : R.isAccepted (R.run q9 q21 m0 refl) ≡ false
case-9-1-21 = refl
case-9-1-22 : R.isAccepted (R.run q9 q22 m0 refl) ≡ false
case-9-1-22 = refl
case-9-1-23 : R.isAccepted (R.run q9 q23 m0 refl) ≡ true
case-9-1-23 = refl
case-9-3-0 : R.isAccepted (R.run q9 q0 m1 refl) ≡ false
case-9-3-0 = refl
case-9-3-1 : R.isAccepted (R.run q9 q1 m1 refl) ≡ true
case-9-3-1 = refl
case-9-3-2 : R.isAccepted (R.run q9 q2 m1 refl) ≡ false
case-9-3-2 = refl
case-9-3-3 : R.isAccepted (R.run q9 q3 m1 refl) ≡ true
case-9-3-3 = refl
case-9-3-4 : R.isAccepted (R.run q9 q4 m1 refl) ≡ false
case-9-3-4 = refl
case-9-3-5 : R.isAccepted (R.run q9 q5 m1 refl) ≡ false
case-9-3-5 = refl
case-9-3-6 : R.isAccepted (R.run q9 q6 m1 refl) ≡ false
case-9-3-6 = refl
case-9-3-7 : R.isAccepted (R.run q9 q7 m1 refl) ≡ true
case-9-3-7 = refl
case-9-3-8 : R.isAccepted (R.run q9 q8 m1 refl) ≡ false
case-9-3-8 = refl
case-9-3-9 : R.isAccepted (R.run q9 q9 m1 refl) ≡ true
case-9-3-9 = refl
case-9-3-10 : R.isAccepted (R.run q9 q10 m1 refl) ≡ false
case-9-3-10 = refl
case-9-3-11 : R.isAccepted (R.run q9 q11 m1 refl) ≡ false
case-9-3-11 = refl
case-9-3-12 : R.isAccepted (R.run q9 q12 m1 refl) ≡ false
case-9-3-12 = refl
case-9-3-13 : R.isAccepted (R.run q9 q13 m1 refl) ≡ true
case-9-3-13 = refl
case-9-3-14 : R.isAccepted (R.run q9 q14 m1 refl) ≡ false
case-9-3-14 = refl
case-9-3-15 : R.isAccepted (R.run q9 q15 m1 refl) ≡ true
case-9-3-15 = refl
case-9-3-16 : R.isAccepted (R.run q9 q16 m1 refl) ≡ false
case-9-3-16 = refl
case-9-3-17 : R.isAccepted (R.run q9 q17 m1 refl) ≡ false
case-9-3-17 = refl
case-9-3-18 : R.isAccepted (R.run q9 q18 m1 refl) ≡ true
case-9-3-18 = refl
case-9-3-19 : R.isAccepted (R.run q9 q19 m1 refl) ≡ true
case-9-3-19 = refl
case-9-3-20 : R.isAccepted (R.run q9 q20 m1 refl) ≡ true
case-9-3-20 = refl
case-9-3-21 : R.isAccepted (R.run q9 q21 m1 refl) ≡ true
case-9-3-21 = refl
case-9-3-22 : R.isAccepted (R.run q9 q22 m1 refl) ≡ true
case-9-3-22 = refl
case-9-3-23 : R.isAccepted (R.run q9 q23 m1 refl) ≡ true
case-9-3-23 = refl
case-10-0-0 : R.isAccepted (R.run q10 q0 c0 refl) ≡ true
case-10-0-0 = refl
case-10-0-1 : R.isAccepted (R.run q10 q1 c0 refl) ≡ true
case-10-0-1 = refl
case-10-0-2 : R.isAccepted (R.run q10 q2 c0 refl) ≡ true
case-10-0-2 = refl
case-10-0-3 : R.isAccepted (R.run q10 q3 c0 refl) ≡ true
case-10-0-3 = refl
case-10-0-4 : R.isAccepted (R.run q10 q4 c0 refl) ≡ true
case-10-0-4 = refl
case-10-0-5 : R.isAccepted (R.run q10 q5 c0 refl) ≡ true
case-10-0-5 = refl
case-10-0-6 : R.isAccepted (R.run q10 q6 c0 refl) ≡ false
case-10-0-6 = refl
case-10-0-7 : R.isAccepted (R.run q10 q7 c0 refl) ≡ false
case-10-0-7 = refl
case-10-0-8 : R.isAccepted (R.run q10 q8 c0 refl) ≡ true
case-10-0-8 = refl
case-10-0-9 : R.isAccepted (R.run q10 q9 c0 refl) ≡ false
case-10-0-9 = refl
case-10-0-10 : R.isAccepted (R.run q10 q10 c0 refl) ≡ true
case-10-0-10 = refl
case-10-0-11 : R.isAccepted (R.run q10 q11 c0 refl) ≡ false
case-10-0-11 = refl
case-10-0-12 : R.isAccepted (R.run q10 q12 c0 refl) ≡ false
case-10-0-12 = refl
case-10-0-13 : R.isAccepted (R.run q10 q13 c0 refl) ≡ false
case-10-0-13 = refl
case-10-0-14 : R.isAccepted (R.run q10 q14 c0 refl) ≡ true
case-10-0-14 = refl
case-10-0-15 : R.isAccepted (R.run q10 q15 c0 refl) ≡ false
case-10-0-15 = refl
case-10-0-16 : R.isAccepted (R.run q10 q16 c0 refl) ≡ true
case-10-0-16 = refl
case-10-0-17 : R.isAccepted (R.run q10 q17 c0 refl) ≡ false
case-10-0-17 = refl
case-10-0-18 : R.isAccepted (R.run q10 q18 c0 refl) ≡ false
case-10-0-18 = refl
case-10-0-19 : R.isAccepted (R.run q10 q19 c0 refl) ≡ false
case-10-0-19 = refl
case-10-0-20 : R.isAccepted (R.run q10 q20 c0 refl) ≡ true
case-10-0-20 = refl
case-10-0-21 : R.isAccepted (R.run q10 q21 c0 refl) ≡ false
case-10-0-21 = refl
case-10-0-22 : R.isAccepted (R.run q10 q22 c0 refl) ≡ true
case-10-0-22 = refl
case-10-0-23 : R.isAccepted (R.run q10 q23 c0 refl) ≡ false
case-10-0-23 = refl
case-10-1-0 : R.isAccepted (R.run q10 q0 m0 refl) ≡ false
case-10-1-0 = refl
case-10-1-1 : R.isAccepted (R.run q10 q1 m0 refl) ≡ false
case-10-1-1 = refl
case-10-1-2 : R.isAccepted (R.run q10 q2 m0 refl) ≡ true
case-10-1-2 = refl
case-10-1-3 : R.isAccepted (R.run q10 q3 m0 refl) ≡ false
case-10-1-3 = refl
case-10-1-4 : R.isAccepted (R.run q10 q4 m0 refl) ≡ true
case-10-1-4 = refl
case-10-1-5 : R.isAccepted (R.run q10 q5 m0 refl) ≡ false
case-10-1-5 = refl
case-10-1-6 : R.isAccepted (R.run q10 q6 m0 refl) ≡ true
case-10-1-6 = refl
case-10-1-7 : R.isAccepted (R.run q10 q7 m0 refl) ≡ true
case-10-1-7 = refl
case-10-1-8 : R.isAccepted (R.run q10 q8 m0 refl) ≡ true
case-10-1-8 = refl
case-10-1-9 : R.isAccepted (R.run q10 q9 m0 refl) ≡ true
case-10-1-9 = refl
case-10-1-10 : R.isAccepted (R.run q10 q10 m0 refl) ≡ true
case-10-1-10 = refl
case-10-1-11 : R.isAccepted (R.run q10 q11 m0 refl) ≡ true
case-10-1-11 = refl
case-10-1-12 : R.isAccepted (R.run q10 q12 m0 refl) ≡ true
case-10-1-12 = refl
case-10-1-13 : R.isAccepted (R.run q10 q13 m0 refl) ≡ false
case-10-1-13 = refl
case-10-1-14 : R.isAccepted (R.run q10 q14 m0 refl) ≡ false
case-10-1-14 = refl
case-10-1-15 : R.isAccepted (R.run q10 q15 m0 refl) ≡ false
case-10-1-15 = refl
case-10-1-16 : R.isAccepted (R.run q10 q16 m0 refl) ≡ false
case-10-1-16 = refl
case-10-1-17 : R.isAccepted (R.run q10 q17 m0 refl) ≡ true
case-10-1-17 = refl
case-10-1-18 : R.isAccepted (R.run q10 q18 m0 refl) ≡ true
case-10-1-18 = refl
case-10-1-19 : R.isAccepted (R.run q10 q19 m0 refl) ≡ false
case-10-1-19 = refl
case-10-1-20 : R.isAccepted (R.run q10 q20 m0 refl) ≡ false
case-10-1-20 = refl
case-10-1-21 : R.isAccepted (R.run q10 q21 m0 refl) ≡ false
case-10-1-21 = refl
case-10-1-22 : R.isAccepted (R.run q10 q22 m0 refl) ≡ false
case-10-1-22 = refl
case-10-1-23 : R.isAccepted (R.run q10 q23 m0 refl) ≡ true
case-10-1-23 = refl
case-11-1-0 : R.isAccepted (R.run q11 q0 m0 refl) ≡ false
case-11-1-0 = refl
case-11-1-1 : R.isAccepted (R.run q11 q1 m0 refl) ≡ false
case-11-1-1 = refl
case-11-1-2 : R.isAccepted (R.run q11 q2 m0 refl) ≡ true
case-11-1-2 = refl
case-11-1-3 : R.isAccepted (R.run q11 q3 m0 refl) ≡ false
case-11-1-3 = refl
case-11-1-4 : R.isAccepted (R.run q11 q4 m0 refl) ≡ true
case-11-1-4 = refl
case-11-1-5 : R.isAccepted (R.run q11 q5 m0 refl) ≡ false
case-11-1-5 = refl
case-11-1-6 : R.isAccepted (R.run q11 q6 m0 refl) ≡ true
case-11-1-6 = refl
case-11-1-7 : R.isAccepted (R.run q11 q7 m0 refl) ≡ true
case-11-1-7 = refl
case-11-1-8 : R.isAccepted (R.run q11 q8 m0 refl) ≡ true
case-11-1-8 = refl
case-11-1-9 : R.isAccepted (R.run q11 q9 m0 refl) ≡ true
case-11-1-9 = refl
case-11-1-10 : R.isAccepted (R.run q11 q10 m0 refl) ≡ true
case-11-1-10 = refl
case-11-1-11 : R.isAccepted (R.run q11 q11 m0 refl) ≡ true
case-11-1-11 = refl
case-11-1-12 : R.isAccepted (R.run q11 q12 m0 refl) ≡ true
case-11-1-12 = refl
case-11-1-13 : R.isAccepted (R.run q11 q13 m0 refl) ≡ false
case-11-1-13 = refl
case-11-1-14 : R.isAccepted (R.run q11 q14 m0 refl) ≡ false
case-11-1-14 = refl
case-11-1-15 : R.isAccepted (R.run q11 q15 m0 refl) ≡ false
case-11-1-15 = refl
case-11-1-16 : R.isAccepted (R.run q11 q16 m0 refl) ≡ false
case-11-1-16 = refl
case-11-1-17 : R.isAccepted (R.run q11 q17 m0 refl) ≡ true
case-11-1-17 = refl
case-11-1-18 : R.isAccepted (R.run q11 q18 m0 refl) ≡ true
case-11-1-18 = refl
case-11-1-19 : R.isAccepted (R.run q11 q19 m0 refl) ≡ false
case-11-1-19 = refl
case-11-1-20 : R.isAccepted (R.run q11 q20 m0 refl) ≡ false
case-11-1-20 = refl
case-11-1-21 : R.isAccepted (R.run q11 q21 m0 refl) ≡ false
case-11-1-21 = refl
case-11-1-22 : R.isAccepted (R.run q11 q22 m0 refl) ≡ false
case-11-1-22 = refl
case-11-1-23 : R.isAccepted (R.run q11 q23 m0 refl) ≡ true
case-11-1-23 = refl
case-11-2-0 : R.isAccepted (R.run q11 q0 c1 refl) ≡ true
case-11-2-0 = refl
case-11-2-1 : R.isAccepted (R.run q11 q1 c1 refl) ≡ false
case-11-2-1 = refl
case-11-2-2 : R.isAccepted (R.run q11 q2 c1 refl) ≡ false
case-11-2-2 = refl
case-11-2-3 : R.isAccepted (R.run q11 q3 c1 refl) ≡ false
case-11-2-3 = refl
case-11-2-4 : R.isAccepted (R.run q11 q4 c1 refl) ≡ false
case-11-2-4 = refl
case-11-2-5 : R.isAccepted (R.run q11 q5 c1 refl) ≡ true
case-11-2-5 = refl
case-11-2-6 : R.isAccepted (R.run q11 q6 c1 refl) ≡ true
case-11-2-6 = refl
case-11-2-7 : R.isAccepted (R.run q11 q7 c1 refl) ≡ false
case-11-2-7 = refl
case-11-2-8 : R.isAccepted (R.run q11 q8 c1 refl) ≡ false
case-11-2-8 = refl
case-11-2-9 : R.isAccepted (R.run q11 q9 c1 refl) ≡ false
case-11-2-9 = refl
case-11-2-10 : R.isAccepted (R.run q11 q10 c1 refl) ≡ false
case-11-2-10 = refl
case-11-2-11 : R.isAccepted (R.run q11 q11 c1 refl) ≡ true
case-11-2-11 = refl
case-11-2-12 : R.isAccepted (R.run q11 q12 c1 refl) ≡ true
case-11-2-12 = refl
case-11-2-13 : R.isAccepted (R.run q11 q13 c1 refl) ≡ true
case-11-2-13 = refl
case-11-2-14 : R.isAccepted (R.run q11 q14 c1 refl) ≡ true
case-11-2-14 = refl
case-11-2-15 : R.isAccepted (R.run q11 q15 c1 refl) ≡ true
case-11-2-15 = refl
case-11-2-16 : R.isAccepted (R.run q11 q16 c1 refl) ≡ true
case-11-2-16 = refl
case-11-2-17 : R.isAccepted (R.run q11 q17 c1 refl) ≡ true
case-11-2-17 = refl
case-11-2-18 : R.isAccepted (R.run q11 q18 c1 refl) ≡ false
case-11-2-18 = refl
case-11-2-19 : R.isAccepted (R.run q11 q19 c1 refl) ≡ true
case-11-2-19 = refl
case-11-2-20 : R.isAccepted (R.run q11 q20 c1 refl) ≡ false
case-11-2-20 = refl
case-11-2-21 : R.isAccepted (R.run q11 q21 c1 refl) ≡ true
case-11-2-21 = refl
case-11-2-22 : R.isAccepted (R.run q11 q22 c1 refl) ≡ false
case-11-2-22 = refl
case-11-2-23 : R.isAccepted (R.run q11 q23 c1 refl) ≡ false
case-11-2-23 = refl
case-12-1-0 : R.isAccepted (R.run q12 q0 m0 refl) ≡ false
case-12-1-0 = refl
case-12-1-1 : R.isAccepted (R.run q12 q1 m0 refl) ≡ false
case-12-1-1 = refl
case-12-1-2 : R.isAccepted (R.run q12 q2 m0 refl) ≡ true
case-12-1-2 = refl
case-12-1-3 : R.isAccepted (R.run q12 q3 m0 refl) ≡ false
case-12-1-3 = refl
case-12-1-4 : R.isAccepted (R.run q12 q4 m0 refl) ≡ true
case-12-1-4 = refl
case-12-1-5 : R.isAccepted (R.run q12 q5 m0 refl) ≡ false
case-12-1-5 = refl
case-12-1-6 : R.isAccepted (R.run q12 q6 m0 refl) ≡ true
case-12-1-6 = refl
case-12-1-7 : R.isAccepted (R.run q12 q7 m0 refl) ≡ true
case-12-1-7 = refl
case-12-1-8 : R.isAccepted (R.run q12 q8 m0 refl) ≡ true
case-12-1-8 = refl
case-12-1-9 : R.isAccepted (R.run q12 q9 m0 refl) ≡ true
case-12-1-9 = refl
case-12-1-10 : R.isAccepted (R.run q12 q10 m0 refl) ≡ true
case-12-1-10 = refl
case-12-1-11 : R.isAccepted (R.run q12 q11 m0 refl) ≡ true
case-12-1-11 = refl
case-12-1-12 : R.isAccepted (R.run q12 q12 m0 refl) ≡ true
case-12-1-12 = refl
case-12-1-13 : R.isAccepted (R.run q12 q13 m0 refl) ≡ false
case-12-1-13 = refl
case-12-1-14 : R.isAccepted (R.run q12 q14 m0 refl) ≡ false
case-12-1-14 = refl
case-12-1-15 : R.isAccepted (R.run q12 q15 m0 refl) ≡ false
case-12-1-15 = refl
case-12-1-16 : R.isAccepted (R.run q12 q16 m0 refl) ≡ false
case-12-1-16 = refl
case-12-1-17 : R.isAccepted (R.run q12 q17 m0 refl) ≡ true
case-12-1-17 = refl
case-12-1-18 : R.isAccepted (R.run q12 q18 m0 refl) ≡ true
case-12-1-18 = refl
case-12-1-19 : R.isAccepted (R.run q12 q19 m0 refl) ≡ false
case-12-1-19 = refl
case-12-1-20 : R.isAccepted (R.run q12 q20 m0 refl) ≡ false
case-12-1-20 = refl
case-12-1-21 : R.isAccepted (R.run q12 q21 m0 refl) ≡ false
case-12-1-21 = refl
case-12-1-22 : R.isAccepted (R.run q12 q22 m0 refl) ≡ false
case-12-1-22 = refl
case-12-1-23 : R.isAccepted (R.run q12 q23 m0 refl) ≡ true
case-12-1-23 = refl
case-12-2-0 : R.isAccepted (R.run q12 q0 c1 refl) ≡ true
case-12-2-0 = refl
case-12-2-1 : R.isAccepted (R.run q12 q1 c1 refl) ≡ false
case-12-2-1 = refl
case-12-2-2 : R.isAccepted (R.run q12 q2 c1 refl) ≡ false
case-12-2-2 = refl
case-12-2-3 : R.isAccepted (R.run q12 q3 c1 refl) ≡ false
case-12-2-3 = refl
case-12-2-4 : R.isAccepted (R.run q12 q4 c1 refl) ≡ false
case-12-2-4 = refl
case-12-2-5 : R.isAccepted (R.run q12 q5 c1 refl) ≡ true
case-12-2-5 = refl
case-12-2-6 : R.isAccepted (R.run q12 q6 c1 refl) ≡ true
case-12-2-6 = refl
case-12-2-7 : R.isAccepted (R.run q12 q7 c1 refl) ≡ false
case-12-2-7 = refl
case-12-2-8 : R.isAccepted (R.run q12 q8 c1 refl) ≡ false
case-12-2-8 = refl
case-12-2-9 : R.isAccepted (R.run q12 q9 c1 refl) ≡ false
case-12-2-9 = refl
case-12-2-10 : R.isAccepted (R.run q12 q10 c1 refl) ≡ false
case-12-2-10 = refl
case-12-2-11 : R.isAccepted (R.run q12 q11 c1 refl) ≡ true
case-12-2-11 = refl
case-12-2-12 : R.isAccepted (R.run q12 q12 c1 refl) ≡ true
case-12-2-12 = refl
case-12-2-13 : R.isAccepted (R.run q12 q13 c1 refl) ≡ true
case-12-2-13 = refl
case-12-2-14 : R.isAccepted (R.run q12 q14 c1 refl) ≡ true
case-12-2-14 = refl
case-12-2-15 : R.isAccepted (R.run q12 q15 c1 refl) ≡ true
case-12-2-15 = refl
case-12-2-16 : R.isAccepted (R.run q12 q16 c1 refl) ≡ true
case-12-2-16 = refl
case-12-2-17 : R.isAccepted (R.run q12 q17 c1 refl) ≡ true
case-12-2-17 = refl
case-12-2-18 : R.isAccepted (R.run q12 q18 c1 refl) ≡ false
case-12-2-18 = refl
case-12-2-19 : R.isAccepted (R.run q12 q19 c1 refl) ≡ true
case-12-2-19 = refl
case-12-2-20 : R.isAccepted (R.run q12 q20 c1 refl) ≡ false
case-12-2-20 = refl
case-12-2-21 : R.isAccepted (R.run q12 q21 c1 refl) ≡ true
case-12-2-21 = refl
case-12-2-22 : R.isAccepted (R.run q12 q22 c1 refl) ≡ false
case-12-2-22 = refl
case-12-2-23 : R.isAccepted (R.run q12 q23 c1 refl) ≡ false
case-12-2-23 = refl
case-13-2-0 : R.isAccepted (R.run q13 q0 c1 refl) ≡ true
case-13-2-0 = refl
case-13-2-1 : R.isAccepted (R.run q13 q1 c1 refl) ≡ false
case-13-2-1 = refl
case-13-2-2 : R.isAccepted (R.run q13 q2 c1 refl) ≡ false
case-13-2-2 = refl
case-13-2-3 : R.isAccepted (R.run q13 q3 c1 refl) ≡ false
case-13-2-3 = refl
case-13-2-4 : R.isAccepted (R.run q13 q4 c1 refl) ≡ false
case-13-2-4 = refl
case-13-2-5 : R.isAccepted (R.run q13 q5 c1 refl) ≡ true
case-13-2-5 = refl
case-13-2-6 : R.isAccepted (R.run q13 q6 c1 refl) ≡ true
case-13-2-6 = refl
case-13-2-7 : R.isAccepted (R.run q13 q7 c1 refl) ≡ false
case-13-2-7 = refl
case-13-2-8 : R.isAccepted (R.run q13 q8 c1 refl) ≡ false
case-13-2-8 = refl
case-13-2-9 : R.isAccepted (R.run q13 q9 c1 refl) ≡ false
case-13-2-9 = refl
case-13-2-10 : R.isAccepted (R.run q13 q10 c1 refl) ≡ false
case-13-2-10 = refl
case-13-2-11 : R.isAccepted (R.run q13 q11 c1 refl) ≡ true
case-13-2-11 = refl
case-13-2-12 : R.isAccepted (R.run q13 q12 c1 refl) ≡ true
case-13-2-12 = refl
case-13-2-13 : R.isAccepted (R.run q13 q13 c1 refl) ≡ true
case-13-2-13 = refl
case-13-2-14 : R.isAccepted (R.run q13 q14 c1 refl) ≡ true
case-13-2-14 = refl
case-13-2-15 : R.isAccepted (R.run q13 q15 c1 refl) ≡ true
case-13-2-15 = refl
case-13-2-16 : R.isAccepted (R.run q13 q16 c1 refl) ≡ true
case-13-2-16 = refl
case-13-2-17 : R.isAccepted (R.run q13 q17 c1 refl) ≡ true
case-13-2-17 = refl
case-13-2-18 : R.isAccepted (R.run q13 q18 c1 refl) ≡ false
case-13-2-18 = refl
case-13-2-19 : R.isAccepted (R.run q13 q19 c1 refl) ≡ true
case-13-2-19 = refl
case-13-2-20 : R.isAccepted (R.run q13 q20 c1 refl) ≡ false
case-13-2-20 = refl
case-13-2-21 : R.isAccepted (R.run q13 q21 c1 refl) ≡ true
case-13-2-21 = refl
case-13-2-22 : R.isAccepted (R.run q13 q22 c1 refl) ≡ false
case-13-2-22 = refl
case-13-2-23 : R.isAccepted (R.run q13 q23 c1 refl) ≡ false
case-13-2-23 = refl
case-13-3-0 : R.isAccepted (R.run q13 q0 m1 refl) ≡ false
case-13-3-0 = refl
case-13-3-1 : R.isAccepted (R.run q13 q1 m1 refl) ≡ true
case-13-3-1 = refl
case-13-3-2 : R.isAccepted (R.run q13 q2 m1 refl) ≡ false
case-13-3-2 = refl
case-13-3-3 : R.isAccepted (R.run q13 q3 m1 refl) ≡ true
case-13-3-3 = refl
case-13-3-4 : R.isAccepted (R.run q13 q4 m1 refl) ≡ false
case-13-3-4 = refl
case-13-3-5 : R.isAccepted (R.run q13 q5 m1 refl) ≡ false
case-13-3-5 = refl
case-13-3-6 : R.isAccepted (R.run q13 q6 m1 refl) ≡ false
case-13-3-6 = refl
case-13-3-7 : R.isAccepted (R.run q13 q7 m1 refl) ≡ true
case-13-3-7 = refl
case-13-3-8 : R.isAccepted (R.run q13 q8 m1 refl) ≡ false
case-13-3-8 = refl
case-13-3-9 : R.isAccepted (R.run q13 q9 m1 refl) ≡ true
case-13-3-9 = refl
case-13-3-10 : R.isAccepted (R.run q13 q10 m1 refl) ≡ false
case-13-3-10 = refl
case-13-3-11 : R.isAccepted (R.run q13 q11 m1 refl) ≡ false
case-13-3-11 = refl
case-13-3-12 : R.isAccepted (R.run q13 q12 m1 refl) ≡ false
case-13-3-12 = refl
case-13-3-13 : R.isAccepted (R.run q13 q13 m1 refl) ≡ true
case-13-3-13 = refl
case-13-3-14 : R.isAccepted (R.run q13 q14 m1 refl) ≡ false
case-13-3-14 = refl
case-13-3-15 : R.isAccepted (R.run q13 q15 m1 refl) ≡ true
case-13-3-15 = refl
case-13-3-16 : R.isAccepted (R.run q13 q16 m1 refl) ≡ false
case-13-3-16 = refl
case-13-3-17 : R.isAccepted (R.run q13 q17 m1 refl) ≡ false
case-13-3-17 = refl
case-13-3-18 : R.isAccepted (R.run q13 q18 m1 refl) ≡ true
case-13-3-18 = refl
case-13-3-19 : R.isAccepted (R.run q13 q19 m1 refl) ≡ true
case-13-3-19 = refl
case-13-3-20 : R.isAccepted (R.run q13 q20 m1 refl) ≡ true
case-13-3-20 = refl
case-13-3-21 : R.isAccepted (R.run q13 q21 m1 refl) ≡ true
case-13-3-21 = refl
case-13-3-22 : R.isAccepted (R.run q13 q22 m1 refl) ≡ true
case-13-3-22 = refl
case-13-3-23 : R.isAccepted (R.run q13 q23 m1 refl) ≡ true
case-13-3-23 = refl
case-14-0-0 : R.isAccepted (R.run q14 q0 c0 refl) ≡ true
case-14-0-0 = refl
case-14-0-1 : R.isAccepted (R.run q14 q1 c0 refl) ≡ true
case-14-0-1 = refl
case-14-0-2 : R.isAccepted (R.run q14 q2 c0 refl) ≡ true
case-14-0-2 = refl
case-14-0-3 : R.isAccepted (R.run q14 q3 c0 refl) ≡ true
case-14-0-3 = refl
case-14-0-4 : R.isAccepted (R.run q14 q4 c0 refl) ≡ true
case-14-0-4 = refl
case-14-0-5 : R.isAccepted (R.run q14 q5 c0 refl) ≡ true
case-14-0-5 = refl
case-14-0-6 : R.isAccepted (R.run q14 q6 c0 refl) ≡ false
case-14-0-6 = refl
case-14-0-7 : R.isAccepted (R.run q14 q7 c0 refl) ≡ false
case-14-0-7 = refl
case-14-0-8 : R.isAccepted (R.run q14 q8 c0 refl) ≡ true
case-14-0-8 = refl
case-14-0-9 : R.isAccepted (R.run q14 q9 c0 refl) ≡ false
case-14-0-9 = refl
case-14-0-10 : R.isAccepted (R.run q14 q10 c0 refl) ≡ true
case-14-0-10 = refl
case-14-0-11 : R.isAccepted (R.run q14 q11 c0 refl) ≡ false
case-14-0-11 = refl
case-14-0-12 : R.isAccepted (R.run q14 q12 c0 refl) ≡ false
case-14-0-12 = refl
case-14-0-13 : R.isAccepted (R.run q14 q13 c0 refl) ≡ false
case-14-0-13 = refl
case-14-0-14 : R.isAccepted (R.run q14 q14 c0 refl) ≡ true
case-14-0-14 = refl
case-14-0-15 : R.isAccepted (R.run q14 q15 c0 refl) ≡ false
case-14-0-15 = refl
case-14-0-16 : R.isAccepted (R.run q14 q16 c0 refl) ≡ true
case-14-0-16 = refl
case-14-0-17 : R.isAccepted (R.run q14 q17 c0 refl) ≡ false
case-14-0-17 = refl
case-14-0-18 : R.isAccepted (R.run q14 q18 c0 refl) ≡ false
case-14-0-18 = refl
case-14-0-19 : R.isAccepted (R.run q14 q19 c0 refl) ≡ false
case-14-0-19 = refl
case-14-0-20 : R.isAccepted (R.run q14 q20 c0 refl) ≡ true
case-14-0-20 = refl
case-14-0-21 : R.isAccepted (R.run q14 q21 c0 refl) ≡ false
case-14-0-21 = refl
case-14-0-22 : R.isAccepted (R.run q14 q22 c0 refl) ≡ true
case-14-0-22 = refl
case-14-0-23 : R.isAccepted (R.run q14 q23 c0 refl) ≡ false
case-14-0-23 = refl
case-14-2-0 : R.isAccepted (R.run q14 q0 c1 refl) ≡ true
case-14-2-0 = refl
case-14-2-1 : R.isAccepted (R.run q14 q1 c1 refl) ≡ false
case-14-2-1 = refl
case-14-2-2 : R.isAccepted (R.run q14 q2 c1 refl) ≡ false
case-14-2-2 = refl
case-14-2-3 : R.isAccepted (R.run q14 q3 c1 refl) ≡ false
case-14-2-3 = refl
case-14-2-4 : R.isAccepted (R.run q14 q4 c1 refl) ≡ false
case-14-2-4 = refl
case-14-2-5 : R.isAccepted (R.run q14 q5 c1 refl) ≡ true
case-14-2-5 = refl
case-14-2-6 : R.isAccepted (R.run q14 q6 c1 refl) ≡ true
case-14-2-6 = refl
case-14-2-7 : R.isAccepted (R.run q14 q7 c1 refl) ≡ false
case-14-2-7 = refl
case-14-2-8 : R.isAccepted (R.run q14 q8 c1 refl) ≡ false
case-14-2-8 = refl
case-14-2-9 : R.isAccepted (R.run q14 q9 c1 refl) ≡ false
case-14-2-9 = refl
case-14-2-10 : R.isAccepted (R.run q14 q10 c1 refl) ≡ false
case-14-2-10 = refl
case-14-2-11 : R.isAccepted (R.run q14 q11 c1 refl) ≡ true
case-14-2-11 = refl
case-14-2-12 : R.isAccepted (R.run q14 q12 c1 refl) ≡ true
case-14-2-12 = refl
case-14-2-13 : R.isAccepted (R.run q14 q13 c1 refl) ≡ true
case-14-2-13 = refl
case-14-2-14 : R.isAccepted (R.run q14 q14 c1 refl) ≡ true
case-14-2-14 = refl
case-14-2-15 : R.isAccepted (R.run q14 q15 c1 refl) ≡ true
case-14-2-15 = refl
case-14-2-16 : R.isAccepted (R.run q14 q16 c1 refl) ≡ true
case-14-2-16 = refl
case-14-2-17 : R.isAccepted (R.run q14 q17 c1 refl) ≡ true
case-14-2-17 = refl
case-14-2-18 : R.isAccepted (R.run q14 q18 c1 refl) ≡ false
case-14-2-18 = refl
case-14-2-19 : R.isAccepted (R.run q14 q19 c1 refl) ≡ true
case-14-2-19 = refl
case-14-2-20 : R.isAccepted (R.run q14 q20 c1 refl) ≡ false
case-14-2-20 = refl
case-14-2-21 : R.isAccepted (R.run q14 q21 c1 refl) ≡ true
case-14-2-21 = refl
case-14-2-22 : R.isAccepted (R.run q14 q22 c1 refl) ≡ false
case-14-2-22 = refl
case-14-2-23 : R.isAccepted (R.run q14 q23 c1 refl) ≡ false
case-14-2-23 = refl
case-15-2-0 : R.isAccepted (R.run q15 q0 c1 refl) ≡ true
case-15-2-0 = refl
case-15-2-1 : R.isAccepted (R.run q15 q1 c1 refl) ≡ false
case-15-2-1 = refl
case-15-2-2 : R.isAccepted (R.run q15 q2 c1 refl) ≡ false
case-15-2-2 = refl
case-15-2-3 : R.isAccepted (R.run q15 q3 c1 refl) ≡ false
case-15-2-3 = refl
case-15-2-4 : R.isAccepted (R.run q15 q4 c1 refl) ≡ false
case-15-2-4 = refl
case-15-2-5 : R.isAccepted (R.run q15 q5 c1 refl) ≡ true
case-15-2-5 = refl
case-15-2-6 : R.isAccepted (R.run q15 q6 c1 refl) ≡ true
case-15-2-6 = refl
case-15-2-7 : R.isAccepted (R.run q15 q7 c1 refl) ≡ false
case-15-2-7 = refl
case-15-2-8 : R.isAccepted (R.run q15 q8 c1 refl) ≡ false
case-15-2-8 = refl
case-15-2-9 : R.isAccepted (R.run q15 q9 c1 refl) ≡ false
case-15-2-9 = refl
case-15-2-10 : R.isAccepted (R.run q15 q10 c1 refl) ≡ false
case-15-2-10 = refl
case-15-2-11 : R.isAccepted (R.run q15 q11 c1 refl) ≡ true
case-15-2-11 = refl
case-15-2-12 : R.isAccepted (R.run q15 q12 c1 refl) ≡ true
case-15-2-12 = refl
case-15-2-13 : R.isAccepted (R.run q15 q13 c1 refl) ≡ true
case-15-2-13 = refl
case-15-2-14 : R.isAccepted (R.run q15 q14 c1 refl) ≡ true
case-15-2-14 = refl
case-15-2-15 : R.isAccepted (R.run q15 q15 c1 refl) ≡ true
case-15-2-15 = refl
case-15-2-16 : R.isAccepted (R.run q15 q16 c1 refl) ≡ true
case-15-2-16 = refl
case-15-2-17 : R.isAccepted (R.run q15 q17 c1 refl) ≡ true
case-15-2-17 = refl
case-15-2-18 : R.isAccepted (R.run q15 q18 c1 refl) ≡ false
case-15-2-18 = refl
case-15-2-19 : R.isAccepted (R.run q15 q19 c1 refl) ≡ true
case-15-2-19 = refl
case-15-2-20 : R.isAccepted (R.run q15 q20 c1 refl) ≡ false
case-15-2-20 = refl
case-15-2-21 : R.isAccepted (R.run q15 q21 c1 refl) ≡ true
case-15-2-21 = refl
case-15-2-22 : R.isAccepted (R.run q15 q22 c1 refl) ≡ false
case-15-2-22 = refl
case-15-2-23 : R.isAccepted (R.run q15 q23 c1 refl) ≡ false
case-15-2-23 = refl
case-15-3-0 : R.isAccepted (R.run q15 q0 m1 refl) ≡ false
case-15-3-0 = refl
case-15-3-1 : R.isAccepted (R.run q15 q1 m1 refl) ≡ true
case-15-3-1 = refl
case-15-3-2 : R.isAccepted (R.run q15 q2 m1 refl) ≡ false
case-15-3-2 = refl
case-15-3-3 : R.isAccepted (R.run q15 q3 m1 refl) ≡ true
case-15-3-3 = refl
case-15-3-4 : R.isAccepted (R.run q15 q4 m1 refl) ≡ false
case-15-3-4 = refl
case-15-3-5 : R.isAccepted (R.run q15 q5 m1 refl) ≡ false
case-15-3-5 = refl
case-15-3-6 : R.isAccepted (R.run q15 q6 m1 refl) ≡ false
case-15-3-6 = refl
case-15-3-7 : R.isAccepted (R.run q15 q7 m1 refl) ≡ true
case-15-3-7 = refl
case-15-3-8 : R.isAccepted (R.run q15 q8 m1 refl) ≡ false
case-15-3-8 = refl
case-15-3-9 : R.isAccepted (R.run q15 q9 m1 refl) ≡ true
case-15-3-9 = refl
case-15-3-10 : R.isAccepted (R.run q15 q10 m1 refl) ≡ false
case-15-3-10 = refl
case-15-3-11 : R.isAccepted (R.run q15 q11 m1 refl) ≡ false
case-15-3-11 = refl
case-15-3-12 : R.isAccepted (R.run q15 q12 m1 refl) ≡ false
case-15-3-12 = refl
case-15-3-13 : R.isAccepted (R.run q15 q13 m1 refl) ≡ true
case-15-3-13 = refl
case-15-3-14 : R.isAccepted (R.run q15 q14 m1 refl) ≡ false
case-15-3-14 = refl
case-15-3-15 : R.isAccepted (R.run q15 q15 m1 refl) ≡ true
case-15-3-15 = refl
case-15-3-16 : R.isAccepted (R.run q15 q16 m1 refl) ≡ false
case-15-3-16 = refl
case-15-3-17 : R.isAccepted (R.run q15 q17 m1 refl) ≡ false
case-15-3-17 = refl
case-15-3-18 : R.isAccepted (R.run q15 q18 m1 refl) ≡ true
case-15-3-18 = refl
case-15-3-19 : R.isAccepted (R.run q15 q19 m1 refl) ≡ true
case-15-3-19 = refl
case-15-3-20 : R.isAccepted (R.run q15 q20 m1 refl) ≡ true
case-15-3-20 = refl
case-15-3-21 : R.isAccepted (R.run q15 q21 m1 refl) ≡ true
case-15-3-21 = refl
case-15-3-22 : R.isAccepted (R.run q15 q22 m1 refl) ≡ true
case-15-3-22 = refl
case-15-3-23 : R.isAccepted (R.run q15 q23 m1 refl) ≡ true
case-15-3-23 = refl
case-16-0-0 : R.isAccepted (R.run q16 q0 c0 refl) ≡ true
case-16-0-0 = refl
case-16-0-1 : R.isAccepted (R.run q16 q1 c0 refl) ≡ true
case-16-0-1 = refl
case-16-0-2 : R.isAccepted (R.run q16 q2 c0 refl) ≡ true
case-16-0-2 = refl
case-16-0-3 : R.isAccepted (R.run q16 q3 c0 refl) ≡ true
case-16-0-3 = refl
case-16-0-4 : R.isAccepted (R.run q16 q4 c0 refl) ≡ true
case-16-0-4 = refl
case-16-0-5 : R.isAccepted (R.run q16 q5 c0 refl) ≡ true
case-16-0-5 = refl
case-16-0-6 : R.isAccepted (R.run q16 q6 c0 refl) ≡ false
case-16-0-6 = refl
case-16-0-7 : R.isAccepted (R.run q16 q7 c0 refl) ≡ false
case-16-0-7 = refl
case-16-0-8 : R.isAccepted (R.run q16 q8 c0 refl) ≡ true
case-16-0-8 = refl
case-16-0-9 : R.isAccepted (R.run q16 q9 c0 refl) ≡ false
case-16-0-9 = refl
case-16-0-10 : R.isAccepted (R.run q16 q10 c0 refl) ≡ true
case-16-0-10 = refl
case-16-0-11 : R.isAccepted (R.run q16 q11 c0 refl) ≡ false
case-16-0-11 = refl
case-16-0-12 : R.isAccepted (R.run q16 q12 c0 refl) ≡ false
case-16-0-12 = refl
case-16-0-13 : R.isAccepted (R.run q16 q13 c0 refl) ≡ false
case-16-0-13 = refl
case-16-0-14 : R.isAccepted (R.run q16 q14 c0 refl) ≡ true
case-16-0-14 = refl
case-16-0-15 : R.isAccepted (R.run q16 q15 c0 refl) ≡ false
case-16-0-15 = refl
case-16-0-16 : R.isAccepted (R.run q16 q16 c0 refl) ≡ true
case-16-0-16 = refl
case-16-0-17 : R.isAccepted (R.run q16 q17 c0 refl) ≡ false
case-16-0-17 = refl
case-16-0-18 : R.isAccepted (R.run q16 q18 c0 refl) ≡ false
case-16-0-18 = refl
case-16-0-19 : R.isAccepted (R.run q16 q19 c0 refl) ≡ false
case-16-0-19 = refl
case-16-0-20 : R.isAccepted (R.run q16 q20 c0 refl) ≡ true
case-16-0-20 = refl
case-16-0-21 : R.isAccepted (R.run q16 q21 c0 refl) ≡ false
case-16-0-21 = refl
case-16-0-22 : R.isAccepted (R.run q16 q22 c0 refl) ≡ true
case-16-0-22 = refl
case-16-0-23 : R.isAccepted (R.run q16 q23 c0 refl) ≡ false
case-16-0-23 = refl
case-16-2-0 : R.isAccepted (R.run q16 q0 c1 refl) ≡ true
case-16-2-0 = refl
case-16-2-1 : R.isAccepted (R.run q16 q1 c1 refl) ≡ false
case-16-2-1 = refl
case-16-2-2 : R.isAccepted (R.run q16 q2 c1 refl) ≡ false
case-16-2-2 = refl
case-16-2-3 : R.isAccepted (R.run q16 q3 c1 refl) ≡ false
case-16-2-3 = refl
case-16-2-4 : R.isAccepted (R.run q16 q4 c1 refl) ≡ false
case-16-2-4 = refl
case-16-2-5 : R.isAccepted (R.run q16 q5 c1 refl) ≡ true
case-16-2-5 = refl
case-16-2-6 : R.isAccepted (R.run q16 q6 c1 refl) ≡ true
case-16-2-6 = refl
case-16-2-7 : R.isAccepted (R.run q16 q7 c1 refl) ≡ false
case-16-2-7 = refl
case-16-2-8 : R.isAccepted (R.run q16 q8 c1 refl) ≡ false
case-16-2-8 = refl
case-16-2-9 : R.isAccepted (R.run q16 q9 c1 refl) ≡ false
case-16-2-9 = refl
case-16-2-10 : R.isAccepted (R.run q16 q10 c1 refl) ≡ false
case-16-2-10 = refl
case-16-2-11 : R.isAccepted (R.run q16 q11 c1 refl) ≡ true
case-16-2-11 = refl
case-16-2-12 : R.isAccepted (R.run q16 q12 c1 refl) ≡ true
case-16-2-12 = refl
case-16-2-13 : R.isAccepted (R.run q16 q13 c1 refl) ≡ true
case-16-2-13 = refl
case-16-2-14 : R.isAccepted (R.run q16 q14 c1 refl) ≡ true
case-16-2-14 = refl
case-16-2-15 : R.isAccepted (R.run q16 q15 c1 refl) ≡ true
case-16-2-15 = refl
case-16-2-16 : R.isAccepted (R.run q16 q16 c1 refl) ≡ true
case-16-2-16 = refl
case-16-2-17 : R.isAccepted (R.run q16 q17 c1 refl) ≡ true
case-16-2-17 = refl
case-16-2-18 : R.isAccepted (R.run q16 q18 c1 refl) ≡ false
case-16-2-18 = refl
case-16-2-19 : R.isAccepted (R.run q16 q19 c1 refl) ≡ true
case-16-2-19 = refl
case-16-2-20 : R.isAccepted (R.run q16 q20 c1 refl) ≡ false
case-16-2-20 = refl
case-16-2-21 : R.isAccepted (R.run q16 q21 c1 refl) ≡ true
case-16-2-21 = refl
case-16-2-22 : R.isAccepted (R.run q16 q22 c1 refl) ≡ false
case-16-2-22 = refl
case-16-2-23 : R.isAccepted (R.run q16 q23 c1 refl) ≡ false
case-16-2-23 = refl
case-17-1-0 : R.isAccepted (R.run q17 q0 m0 refl) ≡ false
case-17-1-0 = refl
case-17-1-1 : R.isAccepted (R.run q17 q1 m0 refl) ≡ false
case-17-1-1 = refl
case-17-1-2 : R.isAccepted (R.run q17 q2 m0 refl) ≡ true
case-17-1-2 = refl
case-17-1-3 : R.isAccepted (R.run q17 q3 m0 refl) ≡ false
case-17-1-3 = refl
case-17-1-4 : R.isAccepted (R.run q17 q4 m0 refl) ≡ true
case-17-1-4 = refl
case-17-1-5 : R.isAccepted (R.run q17 q5 m0 refl) ≡ false
case-17-1-5 = refl
case-17-1-6 : R.isAccepted (R.run q17 q6 m0 refl) ≡ true
case-17-1-6 = refl
case-17-1-7 : R.isAccepted (R.run q17 q7 m0 refl) ≡ true
case-17-1-7 = refl
case-17-1-8 : R.isAccepted (R.run q17 q8 m0 refl) ≡ true
case-17-1-8 = refl
case-17-1-9 : R.isAccepted (R.run q17 q9 m0 refl) ≡ true
case-17-1-9 = refl
case-17-1-10 : R.isAccepted (R.run q17 q10 m0 refl) ≡ true
case-17-1-10 = refl
case-17-1-11 : R.isAccepted (R.run q17 q11 m0 refl) ≡ true
case-17-1-11 = refl
case-17-1-12 : R.isAccepted (R.run q17 q12 m0 refl) ≡ true
case-17-1-12 = refl
case-17-1-13 : R.isAccepted (R.run q17 q13 m0 refl) ≡ false
case-17-1-13 = refl
case-17-1-14 : R.isAccepted (R.run q17 q14 m0 refl) ≡ false
case-17-1-14 = refl
case-17-1-15 : R.isAccepted (R.run q17 q15 m0 refl) ≡ false
case-17-1-15 = refl
case-17-1-16 : R.isAccepted (R.run q17 q16 m0 refl) ≡ false
case-17-1-16 = refl
case-17-1-17 : R.isAccepted (R.run q17 q17 m0 refl) ≡ true
case-17-1-17 = refl
case-17-1-18 : R.isAccepted (R.run q17 q18 m0 refl) ≡ true
case-17-1-18 = refl
case-17-1-19 : R.isAccepted (R.run q17 q19 m0 refl) ≡ false
case-17-1-19 = refl
case-17-1-20 : R.isAccepted (R.run q17 q20 m0 refl) ≡ false
case-17-1-20 = refl
case-17-1-21 : R.isAccepted (R.run q17 q21 m0 refl) ≡ false
case-17-1-21 = refl
case-17-1-22 : R.isAccepted (R.run q17 q22 m0 refl) ≡ false
case-17-1-22 = refl
case-17-1-23 : R.isAccepted (R.run q17 q23 m0 refl) ≡ true
case-17-1-23 = refl
case-17-2-0 : R.isAccepted (R.run q17 q0 c1 refl) ≡ true
case-17-2-0 = refl
case-17-2-1 : R.isAccepted (R.run q17 q1 c1 refl) ≡ false
case-17-2-1 = refl
case-17-2-2 : R.isAccepted (R.run q17 q2 c1 refl) ≡ false
case-17-2-2 = refl
case-17-2-3 : R.isAccepted (R.run q17 q3 c1 refl) ≡ false
case-17-2-3 = refl
case-17-2-4 : R.isAccepted (R.run q17 q4 c1 refl) ≡ false
case-17-2-4 = refl
case-17-2-5 : R.isAccepted (R.run q17 q5 c1 refl) ≡ true
case-17-2-5 = refl
case-17-2-6 : R.isAccepted (R.run q17 q6 c1 refl) ≡ true
case-17-2-6 = refl
case-17-2-7 : R.isAccepted (R.run q17 q7 c1 refl) ≡ false
case-17-2-7 = refl
case-17-2-8 : R.isAccepted (R.run q17 q8 c1 refl) ≡ false
case-17-2-8 = refl
case-17-2-9 : R.isAccepted (R.run q17 q9 c1 refl) ≡ false
case-17-2-9 = refl
case-17-2-10 : R.isAccepted (R.run q17 q10 c1 refl) ≡ false
case-17-2-10 = refl
case-17-2-11 : R.isAccepted (R.run q17 q11 c1 refl) ≡ true
case-17-2-11 = refl
case-17-2-12 : R.isAccepted (R.run q17 q12 c1 refl) ≡ true
case-17-2-12 = refl
case-17-2-13 : R.isAccepted (R.run q17 q13 c1 refl) ≡ true
case-17-2-13 = refl
case-17-2-14 : R.isAccepted (R.run q17 q14 c1 refl) ≡ true
case-17-2-14 = refl
case-17-2-15 : R.isAccepted (R.run q17 q15 c1 refl) ≡ true
case-17-2-15 = refl
case-17-2-16 : R.isAccepted (R.run q17 q16 c1 refl) ≡ true
case-17-2-16 = refl
case-17-2-17 : R.isAccepted (R.run q17 q17 c1 refl) ≡ true
case-17-2-17 = refl
case-17-2-18 : R.isAccepted (R.run q17 q18 c1 refl) ≡ false
case-17-2-18 = refl
case-17-2-19 : R.isAccepted (R.run q17 q19 c1 refl) ≡ true
case-17-2-19 = refl
case-17-2-20 : R.isAccepted (R.run q17 q20 c1 refl) ≡ false
case-17-2-20 = refl
case-17-2-21 : R.isAccepted (R.run q17 q21 c1 refl) ≡ true
case-17-2-21 = refl
case-17-2-22 : R.isAccepted (R.run q17 q22 c1 refl) ≡ false
case-17-2-22 = refl
case-17-2-23 : R.isAccepted (R.run q17 q23 c1 refl) ≡ false
case-17-2-23 = refl
case-18-1-0 : R.isAccepted (R.run q18 q0 m0 refl) ≡ false
case-18-1-0 = refl
case-18-1-1 : R.isAccepted (R.run q18 q1 m0 refl) ≡ false
case-18-1-1 = refl
case-18-1-2 : R.isAccepted (R.run q18 q2 m0 refl) ≡ true
case-18-1-2 = refl
case-18-1-3 : R.isAccepted (R.run q18 q3 m0 refl) ≡ false
case-18-1-3 = refl
case-18-1-4 : R.isAccepted (R.run q18 q4 m0 refl) ≡ true
case-18-1-4 = refl
case-18-1-5 : R.isAccepted (R.run q18 q5 m0 refl) ≡ false
case-18-1-5 = refl
case-18-1-6 : R.isAccepted (R.run q18 q6 m0 refl) ≡ true
case-18-1-6 = refl
case-18-1-7 : R.isAccepted (R.run q18 q7 m0 refl) ≡ true
case-18-1-7 = refl
case-18-1-8 : R.isAccepted (R.run q18 q8 m0 refl) ≡ true
case-18-1-8 = refl
case-18-1-9 : R.isAccepted (R.run q18 q9 m0 refl) ≡ true
case-18-1-9 = refl
case-18-1-10 : R.isAccepted (R.run q18 q10 m0 refl) ≡ true
case-18-1-10 = refl
case-18-1-11 : R.isAccepted (R.run q18 q11 m0 refl) ≡ true
case-18-1-11 = refl
case-18-1-12 : R.isAccepted (R.run q18 q12 m0 refl) ≡ true
case-18-1-12 = refl
case-18-1-13 : R.isAccepted (R.run q18 q13 m0 refl) ≡ false
case-18-1-13 = refl
case-18-1-14 : R.isAccepted (R.run q18 q14 m0 refl) ≡ false
case-18-1-14 = refl
case-18-1-15 : R.isAccepted (R.run q18 q15 m0 refl) ≡ false
case-18-1-15 = refl
case-18-1-16 : R.isAccepted (R.run q18 q16 m0 refl) ≡ false
case-18-1-16 = refl
case-18-1-17 : R.isAccepted (R.run q18 q17 m0 refl) ≡ true
case-18-1-17 = refl
case-18-1-18 : R.isAccepted (R.run q18 q18 m0 refl) ≡ true
case-18-1-18 = refl
case-18-1-19 : R.isAccepted (R.run q18 q19 m0 refl) ≡ false
case-18-1-19 = refl
case-18-1-20 : R.isAccepted (R.run q18 q20 m0 refl) ≡ false
case-18-1-20 = refl
case-18-1-21 : R.isAccepted (R.run q18 q21 m0 refl) ≡ false
case-18-1-21 = refl
case-18-1-22 : R.isAccepted (R.run q18 q22 m0 refl) ≡ false
case-18-1-22 = refl
case-18-1-23 : R.isAccepted (R.run q18 q23 m0 refl) ≡ true
case-18-1-23 = refl
case-18-3-0 : R.isAccepted (R.run q18 q0 m1 refl) ≡ false
case-18-3-0 = refl
case-18-3-1 : R.isAccepted (R.run q18 q1 m1 refl) ≡ true
case-18-3-1 = refl
case-18-3-2 : R.isAccepted (R.run q18 q2 m1 refl) ≡ false
case-18-3-2 = refl
case-18-3-3 : R.isAccepted (R.run q18 q3 m1 refl) ≡ true
case-18-3-3 = refl
case-18-3-4 : R.isAccepted (R.run q18 q4 m1 refl) ≡ false
case-18-3-4 = refl
case-18-3-5 : R.isAccepted (R.run q18 q5 m1 refl) ≡ false
case-18-3-5 = refl
case-18-3-6 : R.isAccepted (R.run q18 q6 m1 refl) ≡ false
case-18-3-6 = refl
case-18-3-7 : R.isAccepted (R.run q18 q7 m1 refl) ≡ true
case-18-3-7 = refl
case-18-3-8 : R.isAccepted (R.run q18 q8 m1 refl) ≡ false
case-18-3-8 = refl
case-18-3-9 : R.isAccepted (R.run q18 q9 m1 refl) ≡ true
case-18-3-9 = refl
case-18-3-10 : R.isAccepted (R.run q18 q10 m1 refl) ≡ false
case-18-3-10 = refl
case-18-3-11 : R.isAccepted (R.run q18 q11 m1 refl) ≡ false
case-18-3-11 = refl
case-18-3-12 : R.isAccepted (R.run q18 q12 m1 refl) ≡ false
case-18-3-12 = refl
case-18-3-13 : R.isAccepted (R.run q18 q13 m1 refl) ≡ true
case-18-3-13 = refl
case-18-3-14 : R.isAccepted (R.run q18 q14 m1 refl) ≡ false
case-18-3-14 = refl
case-18-3-15 : R.isAccepted (R.run q18 q15 m1 refl) ≡ true
case-18-3-15 = refl
case-18-3-16 : R.isAccepted (R.run q18 q16 m1 refl) ≡ false
case-18-3-16 = refl
case-18-3-17 : R.isAccepted (R.run q18 q17 m1 refl) ≡ false
case-18-3-17 = refl
case-18-3-18 : R.isAccepted (R.run q18 q18 m1 refl) ≡ true
case-18-3-18 = refl
case-18-3-19 : R.isAccepted (R.run q18 q19 m1 refl) ≡ true
case-18-3-19 = refl
case-18-3-20 : R.isAccepted (R.run q18 q20 m1 refl) ≡ true
case-18-3-20 = refl
case-18-3-21 : R.isAccepted (R.run q18 q21 m1 refl) ≡ true
case-18-3-21 = refl
case-18-3-22 : R.isAccepted (R.run q18 q22 m1 refl) ≡ true
case-18-3-22 = refl
case-18-3-23 : R.isAccepted (R.run q18 q23 m1 refl) ≡ true
case-18-3-23 = refl
case-19-2-0 : R.isAccepted (R.run q19 q0 c1 refl) ≡ true
case-19-2-0 = refl
case-19-2-1 : R.isAccepted (R.run q19 q1 c1 refl) ≡ false
case-19-2-1 = refl
case-19-2-2 : R.isAccepted (R.run q19 q2 c1 refl) ≡ false
case-19-2-2 = refl
case-19-2-3 : R.isAccepted (R.run q19 q3 c1 refl) ≡ false
case-19-2-3 = refl
case-19-2-4 : R.isAccepted (R.run q19 q4 c1 refl) ≡ false
case-19-2-4 = refl
case-19-2-5 : R.isAccepted (R.run q19 q5 c1 refl) ≡ true
case-19-2-5 = refl
case-19-2-6 : R.isAccepted (R.run q19 q6 c1 refl) ≡ true
case-19-2-6 = refl
case-19-2-7 : R.isAccepted (R.run q19 q7 c1 refl) ≡ false
case-19-2-7 = refl
case-19-2-8 : R.isAccepted (R.run q19 q8 c1 refl) ≡ false
case-19-2-8 = refl
case-19-2-9 : R.isAccepted (R.run q19 q9 c1 refl) ≡ false
case-19-2-9 = refl
case-19-2-10 : R.isAccepted (R.run q19 q10 c1 refl) ≡ false
case-19-2-10 = refl
case-19-2-11 : R.isAccepted (R.run q19 q11 c1 refl) ≡ true
case-19-2-11 = refl
case-19-2-12 : R.isAccepted (R.run q19 q12 c1 refl) ≡ true
case-19-2-12 = refl
case-19-2-13 : R.isAccepted (R.run q19 q13 c1 refl) ≡ true
case-19-2-13 = refl
case-19-2-14 : R.isAccepted (R.run q19 q14 c1 refl) ≡ true
case-19-2-14 = refl
case-19-2-15 : R.isAccepted (R.run q19 q15 c1 refl) ≡ true
case-19-2-15 = refl
case-19-2-16 : R.isAccepted (R.run q19 q16 c1 refl) ≡ true
case-19-2-16 = refl
case-19-2-17 : R.isAccepted (R.run q19 q17 c1 refl) ≡ true
case-19-2-17 = refl
case-19-2-18 : R.isAccepted (R.run q19 q18 c1 refl) ≡ false
case-19-2-18 = refl
case-19-2-19 : R.isAccepted (R.run q19 q19 c1 refl) ≡ true
case-19-2-19 = refl
case-19-2-20 : R.isAccepted (R.run q19 q20 c1 refl) ≡ false
case-19-2-20 = refl
case-19-2-21 : R.isAccepted (R.run q19 q21 c1 refl) ≡ true
case-19-2-21 = refl
case-19-2-22 : R.isAccepted (R.run q19 q22 c1 refl) ≡ false
case-19-2-22 = refl
case-19-2-23 : R.isAccepted (R.run q19 q23 c1 refl) ≡ false
case-19-2-23 = refl
case-19-3-0 : R.isAccepted (R.run q19 q0 m1 refl) ≡ false
case-19-3-0 = refl
case-19-3-1 : R.isAccepted (R.run q19 q1 m1 refl) ≡ true
case-19-3-1 = refl
case-19-3-2 : R.isAccepted (R.run q19 q2 m1 refl) ≡ false
case-19-3-2 = refl
case-19-3-3 : R.isAccepted (R.run q19 q3 m1 refl) ≡ true
case-19-3-3 = refl
case-19-3-4 : R.isAccepted (R.run q19 q4 m1 refl) ≡ false
case-19-3-4 = refl
case-19-3-5 : R.isAccepted (R.run q19 q5 m1 refl) ≡ false
case-19-3-5 = refl
case-19-3-6 : R.isAccepted (R.run q19 q6 m1 refl) ≡ false
case-19-3-6 = refl
case-19-3-7 : R.isAccepted (R.run q19 q7 m1 refl) ≡ true
case-19-3-7 = refl
case-19-3-8 : R.isAccepted (R.run q19 q8 m1 refl) ≡ false
case-19-3-8 = refl
case-19-3-9 : R.isAccepted (R.run q19 q9 m1 refl) ≡ true
case-19-3-9 = refl
case-19-3-10 : R.isAccepted (R.run q19 q10 m1 refl) ≡ false
case-19-3-10 = refl
case-19-3-11 : R.isAccepted (R.run q19 q11 m1 refl) ≡ false
case-19-3-11 = refl
case-19-3-12 : R.isAccepted (R.run q19 q12 m1 refl) ≡ false
case-19-3-12 = refl
case-19-3-13 : R.isAccepted (R.run q19 q13 m1 refl) ≡ true
case-19-3-13 = refl
case-19-3-14 : R.isAccepted (R.run q19 q14 m1 refl) ≡ false
case-19-3-14 = refl
case-19-3-15 : R.isAccepted (R.run q19 q15 m1 refl) ≡ true
case-19-3-15 = refl
case-19-3-16 : R.isAccepted (R.run q19 q16 m1 refl) ≡ false
case-19-3-16 = refl
case-19-3-17 : R.isAccepted (R.run q19 q17 m1 refl) ≡ false
case-19-3-17 = refl
case-19-3-18 : R.isAccepted (R.run q19 q18 m1 refl) ≡ true
case-19-3-18 = refl
case-19-3-19 : R.isAccepted (R.run q19 q19 m1 refl) ≡ true
case-19-3-19 = refl
case-19-3-20 : R.isAccepted (R.run q19 q20 m1 refl) ≡ true
case-19-3-20 = refl
case-19-3-21 : R.isAccepted (R.run q19 q21 m1 refl) ≡ true
case-19-3-21 = refl
case-19-3-22 : R.isAccepted (R.run q19 q22 m1 refl) ≡ true
case-19-3-22 = refl
case-19-3-23 : R.isAccepted (R.run q19 q23 m1 refl) ≡ true
case-19-3-23 = refl
case-20-0-0 : R.isAccepted (R.run q20 q0 c0 refl) ≡ true
case-20-0-0 = refl
case-20-0-1 : R.isAccepted (R.run q20 q1 c0 refl) ≡ true
case-20-0-1 = refl
case-20-0-2 : R.isAccepted (R.run q20 q2 c0 refl) ≡ true
case-20-0-2 = refl
case-20-0-3 : R.isAccepted (R.run q20 q3 c0 refl) ≡ true
case-20-0-3 = refl
case-20-0-4 : R.isAccepted (R.run q20 q4 c0 refl) ≡ true
case-20-0-4 = refl
case-20-0-5 : R.isAccepted (R.run q20 q5 c0 refl) ≡ true
case-20-0-5 = refl
case-20-0-6 : R.isAccepted (R.run q20 q6 c0 refl) ≡ false
case-20-0-6 = refl
case-20-0-7 : R.isAccepted (R.run q20 q7 c0 refl) ≡ false
case-20-0-7 = refl
case-20-0-8 : R.isAccepted (R.run q20 q8 c0 refl) ≡ true
case-20-0-8 = refl
case-20-0-9 : R.isAccepted (R.run q20 q9 c0 refl) ≡ false
case-20-0-9 = refl
case-20-0-10 : R.isAccepted (R.run q20 q10 c0 refl) ≡ true
case-20-0-10 = refl
case-20-0-11 : R.isAccepted (R.run q20 q11 c0 refl) ≡ false
case-20-0-11 = refl
case-20-0-12 : R.isAccepted (R.run q20 q12 c0 refl) ≡ false
case-20-0-12 = refl
case-20-0-13 : R.isAccepted (R.run q20 q13 c0 refl) ≡ false
case-20-0-13 = refl
case-20-0-14 : R.isAccepted (R.run q20 q14 c0 refl) ≡ true
case-20-0-14 = refl
case-20-0-15 : R.isAccepted (R.run q20 q15 c0 refl) ≡ false
case-20-0-15 = refl
case-20-0-16 : R.isAccepted (R.run q20 q16 c0 refl) ≡ true
case-20-0-16 = refl
case-20-0-17 : R.isAccepted (R.run q20 q17 c0 refl) ≡ false
case-20-0-17 = refl
case-20-0-18 : R.isAccepted (R.run q20 q18 c0 refl) ≡ false
case-20-0-18 = refl
case-20-0-19 : R.isAccepted (R.run q20 q19 c0 refl) ≡ false
case-20-0-19 = refl
case-20-0-20 : R.isAccepted (R.run q20 q20 c0 refl) ≡ true
case-20-0-20 = refl
case-20-0-21 : R.isAccepted (R.run q20 q21 c0 refl) ≡ false
case-20-0-21 = refl
case-20-0-22 : R.isAccepted (R.run q20 q22 c0 refl) ≡ true
case-20-0-22 = refl
case-20-0-23 : R.isAccepted (R.run q20 q23 c0 refl) ≡ false
case-20-0-23 = refl
case-20-3-0 : R.isAccepted (R.run q20 q0 m1 refl) ≡ false
case-20-3-0 = refl
case-20-3-1 : R.isAccepted (R.run q20 q1 m1 refl) ≡ true
case-20-3-1 = refl
case-20-3-2 : R.isAccepted (R.run q20 q2 m1 refl) ≡ false
case-20-3-2 = refl
case-20-3-3 : R.isAccepted (R.run q20 q3 m1 refl) ≡ true
case-20-3-3 = refl
case-20-3-4 : R.isAccepted (R.run q20 q4 m1 refl) ≡ false
case-20-3-4 = refl
case-20-3-5 : R.isAccepted (R.run q20 q5 m1 refl) ≡ false
case-20-3-5 = refl
case-20-3-6 : R.isAccepted (R.run q20 q6 m1 refl) ≡ false
case-20-3-6 = refl
case-20-3-7 : R.isAccepted (R.run q20 q7 m1 refl) ≡ true
case-20-3-7 = refl
case-20-3-8 : R.isAccepted (R.run q20 q8 m1 refl) ≡ false
case-20-3-8 = refl
case-20-3-9 : R.isAccepted (R.run q20 q9 m1 refl) ≡ true
case-20-3-9 = refl
case-20-3-10 : R.isAccepted (R.run q20 q10 m1 refl) ≡ false
case-20-3-10 = refl
case-20-3-11 : R.isAccepted (R.run q20 q11 m1 refl) ≡ false
case-20-3-11 = refl
case-20-3-12 : R.isAccepted (R.run q20 q12 m1 refl) ≡ false
case-20-3-12 = refl
case-20-3-13 : R.isAccepted (R.run q20 q13 m1 refl) ≡ true
case-20-3-13 = refl
case-20-3-14 : R.isAccepted (R.run q20 q14 m1 refl) ≡ false
case-20-3-14 = refl
case-20-3-15 : R.isAccepted (R.run q20 q15 m1 refl) ≡ true
case-20-3-15 = refl
case-20-3-16 : R.isAccepted (R.run q20 q16 m1 refl) ≡ false
case-20-3-16 = refl
case-20-3-17 : R.isAccepted (R.run q20 q17 m1 refl) ≡ false
case-20-3-17 = refl
case-20-3-18 : R.isAccepted (R.run q20 q18 m1 refl) ≡ true
case-20-3-18 = refl
case-20-3-19 : R.isAccepted (R.run q20 q19 m1 refl) ≡ true
case-20-3-19 = refl
case-20-3-20 : R.isAccepted (R.run q20 q20 m1 refl) ≡ true
case-20-3-20 = refl
case-20-3-21 : R.isAccepted (R.run q20 q21 m1 refl) ≡ true
case-20-3-21 = refl
case-20-3-22 : R.isAccepted (R.run q20 q22 m1 refl) ≡ true
case-20-3-22 = refl
case-20-3-23 : R.isAccepted (R.run q20 q23 m1 refl) ≡ true
case-20-3-23 = refl
case-21-2-0 : R.isAccepted (R.run q21 q0 c1 refl) ≡ true
case-21-2-0 = refl
case-21-2-1 : R.isAccepted (R.run q21 q1 c1 refl) ≡ false
case-21-2-1 = refl
case-21-2-2 : R.isAccepted (R.run q21 q2 c1 refl) ≡ false
case-21-2-2 = refl
case-21-2-3 : R.isAccepted (R.run q21 q3 c1 refl) ≡ false
case-21-2-3 = refl
case-21-2-4 : R.isAccepted (R.run q21 q4 c1 refl) ≡ false
case-21-2-4 = refl
case-21-2-5 : R.isAccepted (R.run q21 q5 c1 refl) ≡ true
case-21-2-5 = refl
case-21-2-6 : R.isAccepted (R.run q21 q6 c1 refl) ≡ true
case-21-2-6 = refl
case-21-2-7 : R.isAccepted (R.run q21 q7 c1 refl) ≡ false
case-21-2-7 = refl
case-21-2-8 : R.isAccepted (R.run q21 q8 c1 refl) ≡ false
case-21-2-8 = refl
case-21-2-9 : R.isAccepted (R.run q21 q9 c1 refl) ≡ false
case-21-2-9 = refl
case-21-2-10 : R.isAccepted (R.run q21 q10 c1 refl) ≡ false
case-21-2-10 = refl
case-21-2-11 : R.isAccepted (R.run q21 q11 c1 refl) ≡ true
case-21-2-11 = refl
case-21-2-12 : R.isAccepted (R.run q21 q12 c1 refl) ≡ true
case-21-2-12 = refl
case-21-2-13 : R.isAccepted (R.run q21 q13 c1 refl) ≡ true
case-21-2-13 = refl
case-21-2-14 : R.isAccepted (R.run q21 q14 c1 refl) ≡ true
case-21-2-14 = refl
case-21-2-15 : R.isAccepted (R.run q21 q15 c1 refl) ≡ true
case-21-2-15 = refl
case-21-2-16 : R.isAccepted (R.run q21 q16 c1 refl) ≡ true
case-21-2-16 = refl
case-21-2-17 : R.isAccepted (R.run q21 q17 c1 refl) ≡ true
case-21-2-17 = refl
case-21-2-18 : R.isAccepted (R.run q21 q18 c1 refl) ≡ false
case-21-2-18 = refl
case-21-2-19 : R.isAccepted (R.run q21 q19 c1 refl) ≡ true
case-21-2-19 = refl
case-21-2-20 : R.isAccepted (R.run q21 q20 c1 refl) ≡ false
case-21-2-20 = refl
case-21-2-21 : R.isAccepted (R.run q21 q21 c1 refl) ≡ true
case-21-2-21 = refl
case-21-2-22 : R.isAccepted (R.run q21 q22 c1 refl) ≡ false
case-21-2-22 = refl
case-21-2-23 : R.isAccepted (R.run q21 q23 c1 refl) ≡ false
case-21-2-23 = refl
case-21-3-0 : R.isAccepted (R.run q21 q0 m1 refl) ≡ false
case-21-3-0 = refl
case-21-3-1 : R.isAccepted (R.run q21 q1 m1 refl) ≡ true
case-21-3-1 = refl
case-21-3-2 : R.isAccepted (R.run q21 q2 m1 refl) ≡ false
case-21-3-2 = refl
case-21-3-3 : R.isAccepted (R.run q21 q3 m1 refl) ≡ true
case-21-3-3 = refl
case-21-3-4 : R.isAccepted (R.run q21 q4 m1 refl) ≡ false
case-21-3-4 = refl
case-21-3-5 : R.isAccepted (R.run q21 q5 m1 refl) ≡ false
case-21-3-5 = refl
case-21-3-6 : R.isAccepted (R.run q21 q6 m1 refl) ≡ false
case-21-3-6 = refl
case-21-3-7 : R.isAccepted (R.run q21 q7 m1 refl) ≡ true
case-21-3-7 = refl
case-21-3-8 : R.isAccepted (R.run q21 q8 m1 refl) ≡ false
case-21-3-8 = refl
case-21-3-9 : R.isAccepted (R.run q21 q9 m1 refl) ≡ true
case-21-3-9 = refl
case-21-3-10 : R.isAccepted (R.run q21 q10 m1 refl) ≡ false
case-21-3-10 = refl
case-21-3-11 : R.isAccepted (R.run q21 q11 m1 refl) ≡ false
case-21-3-11 = refl
case-21-3-12 : R.isAccepted (R.run q21 q12 m1 refl) ≡ false
case-21-3-12 = refl
case-21-3-13 : R.isAccepted (R.run q21 q13 m1 refl) ≡ true
case-21-3-13 = refl
case-21-3-14 : R.isAccepted (R.run q21 q14 m1 refl) ≡ false
case-21-3-14 = refl
case-21-3-15 : R.isAccepted (R.run q21 q15 m1 refl) ≡ true
case-21-3-15 = refl
case-21-3-16 : R.isAccepted (R.run q21 q16 m1 refl) ≡ false
case-21-3-16 = refl
case-21-3-17 : R.isAccepted (R.run q21 q17 m1 refl) ≡ false
case-21-3-17 = refl
case-21-3-18 : R.isAccepted (R.run q21 q18 m1 refl) ≡ true
case-21-3-18 = refl
case-21-3-19 : R.isAccepted (R.run q21 q19 m1 refl) ≡ true
case-21-3-19 = refl
case-21-3-20 : R.isAccepted (R.run q21 q20 m1 refl) ≡ true
case-21-3-20 = refl
case-21-3-21 : R.isAccepted (R.run q21 q21 m1 refl) ≡ true
case-21-3-21 = refl
case-21-3-22 : R.isAccepted (R.run q21 q22 m1 refl) ≡ true
case-21-3-22 = refl
case-21-3-23 : R.isAccepted (R.run q21 q23 m1 refl) ≡ true
case-21-3-23 = refl
case-22-0-0 : R.isAccepted (R.run q22 q0 c0 refl) ≡ true
case-22-0-0 = refl
case-22-0-1 : R.isAccepted (R.run q22 q1 c0 refl) ≡ true
case-22-0-1 = refl
case-22-0-2 : R.isAccepted (R.run q22 q2 c0 refl) ≡ true
case-22-0-2 = refl
case-22-0-3 : R.isAccepted (R.run q22 q3 c0 refl) ≡ true
case-22-0-3 = refl
case-22-0-4 : R.isAccepted (R.run q22 q4 c0 refl) ≡ true
case-22-0-4 = refl
case-22-0-5 : R.isAccepted (R.run q22 q5 c0 refl) ≡ true
case-22-0-5 = refl
case-22-0-6 : R.isAccepted (R.run q22 q6 c0 refl) ≡ false
case-22-0-6 = refl
case-22-0-7 : R.isAccepted (R.run q22 q7 c0 refl) ≡ false
case-22-0-7 = refl
case-22-0-8 : R.isAccepted (R.run q22 q8 c0 refl) ≡ true
case-22-0-8 = refl
case-22-0-9 : R.isAccepted (R.run q22 q9 c0 refl) ≡ false
case-22-0-9 = refl
case-22-0-10 : R.isAccepted (R.run q22 q10 c0 refl) ≡ true
case-22-0-10 = refl
case-22-0-11 : R.isAccepted (R.run q22 q11 c0 refl) ≡ false
case-22-0-11 = refl
case-22-0-12 : R.isAccepted (R.run q22 q12 c0 refl) ≡ false
case-22-0-12 = refl
case-22-0-13 : R.isAccepted (R.run q22 q13 c0 refl) ≡ false
case-22-0-13 = refl
case-22-0-14 : R.isAccepted (R.run q22 q14 c0 refl) ≡ true
case-22-0-14 = refl
case-22-0-15 : R.isAccepted (R.run q22 q15 c0 refl) ≡ false
case-22-0-15 = refl
case-22-0-16 : R.isAccepted (R.run q22 q16 c0 refl) ≡ true
case-22-0-16 = refl
case-22-0-17 : R.isAccepted (R.run q22 q17 c0 refl) ≡ false
case-22-0-17 = refl
case-22-0-18 : R.isAccepted (R.run q22 q18 c0 refl) ≡ false
case-22-0-18 = refl
case-22-0-19 : R.isAccepted (R.run q22 q19 c0 refl) ≡ false
case-22-0-19 = refl
case-22-0-20 : R.isAccepted (R.run q22 q20 c0 refl) ≡ true
case-22-0-20 = refl
case-22-0-21 : R.isAccepted (R.run q22 q21 c0 refl) ≡ false
case-22-0-21 = refl
case-22-0-22 : R.isAccepted (R.run q22 q22 c0 refl) ≡ true
case-22-0-22 = refl
case-22-0-23 : R.isAccepted (R.run q22 q23 c0 refl) ≡ false
case-22-0-23 = refl
case-22-3-0 : R.isAccepted (R.run q22 q0 m1 refl) ≡ false
case-22-3-0 = refl
case-22-3-1 : R.isAccepted (R.run q22 q1 m1 refl) ≡ true
case-22-3-1 = refl
case-22-3-2 : R.isAccepted (R.run q22 q2 m1 refl) ≡ false
case-22-3-2 = refl
case-22-3-3 : R.isAccepted (R.run q22 q3 m1 refl) ≡ true
case-22-3-3 = refl
case-22-3-4 : R.isAccepted (R.run q22 q4 m1 refl) ≡ false
case-22-3-4 = refl
case-22-3-5 : R.isAccepted (R.run q22 q5 m1 refl) ≡ false
case-22-3-5 = refl
case-22-3-6 : R.isAccepted (R.run q22 q6 m1 refl) ≡ false
case-22-3-6 = refl
case-22-3-7 : R.isAccepted (R.run q22 q7 m1 refl) ≡ true
case-22-3-7 = refl
case-22-3-8 : R.isAccepted (R.run q22 q8 m1 refl) ≡ false
case-22-3-8 = refl
case-22-3-9 : R.isAccepted (R.run q22 q9 m1 refl) ≡ true
case-22-3-9 = refl
case-22-3-10 : R.isAccepted (R.run q22 q10 m1 refl) ≡ false
case-22-3-10 = refl
case-22-3-11 : R.isAccepted (R.run q22 q11 m1 refl) ≡ false
case-22-3-11 = refl
case-22-3-12 : R.isAccepted (R.run q22 q12 m1 refl) ≡ false
case-22-3-12 = refl
case-22-3-13 : R.isAccepted (R.run q22 q13 m1 refl) ≡ true
case-22-3-13 = refl
case-22-3-14 : R.isAccepted (R.run q22 q14 m1 refl) ≡ false
case-22-3-14 = refl
case-22-3-15 : R.isAccepted (R.run q22 q15 m1 refl) ≡ true
case-22-3-15 = refl
case-22-3-16 : R.isAccepted (R.run q22 q16 m1 refl) ≡ false
case-22-3-16 = refl
case-22-3-17 : R.isAccepted (R.run q22 q17 m1 refl) ≡ false
case-22-3-17 = refl
case-22-3-18 : R.isAccepted (R.run q22 q18 m1 refl) ≡ true
case-22-3-18 = refl
case-22-3-19 : R.isAccepted (R.run q22 q19 m1 refl) ≡ true
case-22-3-19 = refl
case-22-3-20 : R.isAccepted (R.run q22 q20 m1 refl) ≡ true
case-22-3-20 = refl
case-22-3-21 : R.isAccepted (R.run q22 q21 m1 refl) ≡ true
case-22-3-21 = refl
case-22-3-22 : R.isAccepted (R.run q22 q22 m1 refl) ≡ true
case-22-3-22 = refl
case-22-3-23 : R.isAccepted (R.run q22 q23 m1 refl) ≡ true
case-22-3-23 = refl
case-23-1-0 : R.isAccepted (R.run q23 q0 m0 refl) ≡ false
case-23-1-0 = refl
case-23-1-1 : R.isAccepted (R.run q23 q1 m0 refl) ≡ false
case-23-1-1 = refl
case-23-1-2 : R.isAccepted (R.run q23 q2 m0 refl) ≡ true
case-23-1-2 = refl
case-23-1-3 : R.isAccepted (R.run q23 q3 m0 refl) ≡ false
case-23-1-3 = refl
case-23-1-4 : R.isAccepted (R.run q23 q4 m0 refl) ≡ true
case-23-1-4 = refl
case-23-1-5 : R.isAccepted (R.run q23 q5 m0 refl) ≡ false
case-23-1-5 = refl
case-23-1-6 : R.isAccepted (R.run q23 q6 m0 refl) ≡ true
case-23-1-6 = refl
case-23-1-7 : R.isAccepted (R.run q23 q7 m0 refl) ≡ true
case-23-1-7 = refl
case-23-1-8 : R.isAccepted (R.run q23 q8 m0 refl) ≡ true
case-23-1-8 = refl
case-23-1-9 : R.isAccepted (R.run q23 q9 m0 refl) ≡ true
case-23-1-9 = refl
case-23-1-10 : R.isAccepted (R.run q23 q10 m0 refl) ≡ true
case-23-1-10 = refl
case-23-1-11 : R.isAccepted (R.run q23 q11 m0 refl) ≡ true
case-23-1-11 = refl
case-23-1-12 : R.isAccepted (R.run q23 q12 m0 refl) ≡ true
case-23-1-12 = refl
case-23-1-13 : R.isAccepted (R.run q23 q13 m0 refl) ≡ false
case-23-1-13 = refl
case-23-1-14 : R.isAccepted (R.run q23 q14 m0 refl) ≡ false
case-23-1-14 = refl
case-23-1-15 : R.isAccepted (R.run q23 q15 m0 refl) ≡ false
case-23-1-15 = refl
case-23-1-16 : R.isAccepted (R.run q23 q16 m0 refl) ≡ false
case-23-1-16 = refl
case-23-1-17 : R.isAccepted (R.run q23 q17 m0 refl) ≡ true
case-23-1-17 = refl
case-23-1-18 : R.isAccepted (R.run q23 q18 m0 refl) ≡ true
case-23-1-18 = refl
case-23-1-19 : R.isAccepted (R.run q23 q19 m0 refl) ≡ false
case-23-1-19 = refl
case-23-1-20 : R.isAccepted (R.run q23 q20 m0 refl) ≡ false
case-23-1-20 = refl
case-23-1-21 : R.isAccepted (R.run q23 q21 m0 refl) ≡ false
case-23-1-21 = refl
case-23-1-22 : R.isAccepted (R.run q23 q22 m0 refl) ≡ false
case-23-1-22 = refl
case-23-1-23 : R.isAccepted (R.run q23 q23 m0 refl) ≡ true
case-23-1-23 = refl
case-23-3-0 : R.isAccepted (R.run q23 q0 m1 refl) ≡ false
case-23-3-0 = refl
case-23-3-1 : R.isAccepted (R.run q23 q1 m1 refl) ≡ true
case-23-3-1 = refl
case-23-3-2 : R.isAccepted (R.run q23 q2 m1 refl) ≡ false
case-23-3-2 = refl
case-23-3-3 : R.isAccepted (R.run q23 q3 m1 refl) ≡ true
case-23-3-3 = refl
case-23-3-4 : R.isAccepted (R.run q23 q4 m1 refl) ≡ false
case-23-3-4 = refl
case-23-3-5 : R.isAccepted (R.run q23 q5 m1 refl) ≡ false
case-23-3-5 = refl
case-23-3-6 : R.isAccepted (R.run q23 q6 m1 refl) ≡ false
case-23-3-6 = refl
case-23-3-7 : R.isAccepted (R.run q23 q7 m1 refl) ≡ true
case-23-3-7 = refl
case-23-3-8 : R.isAccepted (R.run q23 q8 m1 refl) ≡ false
case-23-3-8 = refl
case-23-3-9 : R.isAccepted (R.run q23 q9 m1 refl) ≡ true
case-23-3-9 = refl
case-23-3-10 : R.isAccepted (R.run q23 q10 m1 refl) ≡ false
case-23-3-10 = refl
case-23-3-11 : R.isAccepted (R.run q23 q11 m1 refl) ≡ false
case-23-3-11 = refl
case-23-3-12 : R.isAccepted (R.run q23 q12 m1 refl) ≡ false
case-23-3-12 = refl
case-23-3-13 : R.isAccepted (R.run q23 q13 m1 refl) ≡ true
case-23-3-13 = refl
case-23-3-14 : R.isAccepted (R.run q23 q14 m1 refl) ≡ false
case-23-3-14 = refl
case-23-3-15 : R.isAccepted (R.run q23 q15 m1 refl) ≡ true
case-23-3-15 = refl
case-23-3-16 : R.isAccepted (R.run q23 q16 m1 refl) ≡ false
case-23-3-16 = refl
case-23-3-17 : R.isAccepted (R.run q23 q17 m1 refl) ≡ false
case-23-3-17 = refl
case-23-3-18 : R.isAccepted (R.run q23 q18 m1 refl) ≡ true
case-23-3-18 = refl
case-23-3-19 : R.isAccepted (R.run q23 q19 m1 refl) ≡ true
case-23-3-19 = refl
case-23-3-20 : R.isAccepted (R.run q23 q20 m1 refl) ≡ true
case-23-3-20 = refl
case-23-3-21 : R.isAccepted (R.run q23 q21 m1 refl) ≡ true
case-23-3-21 = refl
case-23-3-22 : R.isAccepted (R.run q23 q22 m1 refl) ≡ true
case-23-3-22 = refl
case-23-3-23 : R.isAccepted (R.run q23 q23 m1 refl) ≡ true
case-23-3-23 = refl
