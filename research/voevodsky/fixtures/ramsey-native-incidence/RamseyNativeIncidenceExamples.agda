{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyNativeIncidenceExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Agda.Builtin.String using (String)
open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1; face; count)
open import RamseyNativeRetainedIncidence
role : Vertex → Vertex → ℕ
role c0 c0 = 0
role c0 m0 = 1
role c0 c1 = 0
role c0 m1 = 1
role m0 c0 = 1
role m0 m0 = 0
role m0 c1 = 1
role m0 m1 = 0
role c1 c0 = 0
role c1 m0 = 1
role c1 c1 = 0
role c1 m1 = 1
role m1 c0 = 1
role m1 m0 = 0
role m1 c1 = 1
role m1 m1 = 0
Permit : Vertex → Type
Permit p = count (λ i → role p (face p i)) ≡ 2
cert : (p : Vertex) → Permit p
cert c0 = refl
cert m0 = refl
cert c1 = refl
cert m1 = refl
Inside : Vertex → Vertex → Type
Inside c0 c0 = ⊥
Inside c0 m0 = Unit
Inside c0 c1 = Unit
Inside c0 m1 = Unit
Inside m0 c0 = Unit
Inside m0 m0 = ⊥
Inside m0 c1 = Unit
Inside m0 m1 = Unit
Inside c1 c0 = Unit
Inside c1 m0 = Unit
Inside c1 c1 = ⊥
Inside c1 m1 = Unit
Inside m1 c0 = Unit
Inside m1 m0 = Unit
Inside m1 c1 = Unit
Inside m1 m1 = ⊥
packet : (p : Vertex) → Permit p → String
packet c0 _ = "{\"context\":\"base\",\"face\":[\"0,0,0,1\",\"0,0,1,0\",\"0,1,0,0\"],\"facet\":0,\"historyLocations\":[{\"history\":\"history-1\",\"index\":0}],\"lift\":0,\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"id\":0,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":0,\"target\":1},\"permit\":{\"MCount\":2,\"parentFace\":[\"0,0,0,1\",\"0,0,1,0\",\"0,1,0,0\"]},\"roles\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"faces\":[[\"1,0,0,0\",\"0,0,1,0\",\"0,1,0,0\"],[\"1,0,0,0\",\"0,1,0,0\",\"0,0,0,1\"],[\"1,0,0,0\",\"0,0,0,1\",\"0,0,1,0\"],[\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]],\"geometry\":\"proton\",\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"center\":[0.25,0.25,0.25,0.25],\"components\":[[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]],\"faces\":[[[1,0,0,0],[0,0,1,0],[0,1,0,0]],[[1,0,0,0],[0,1,0,0],[0,0,0,1]],[[1,0,0,0],[0,0,0,1],[0,0,1,0]],[[0,1,0,0],[0,0,1,0],[0,0,0,1]]],\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0],\"vertices\":[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-0\",\"index\":0,\"species\":\"proton\"},\"packet\":{\"chart\":0,\"id\":0,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"faces\":[[\"0,0,1,0\",\"0,1,0,0\",\"-1,1,0,1\"],[\"0,0,1,0\",\"-1,1,0,1\",\"0,0,0,1\"],[\"0,0,1,0\",\"0,0,0,1\",\"0,1,0,0\"],[\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]],\"geometry\":\"split\",\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"center\":[-0.5,0.5,0.5,0.5],\"components\":[[[0,0,1,0],[-1,1,0,1],[0,1,0,0],[0,0,0,1]],[[-1,1,0,1],[0,0,1,0],[-1,1,1,0],[0,1,0,0]],[[0,0,1,0],[-1,1,0,1],[-1,0,1,1],[-1,1,1,0]],[[-1,1,0,1],[0,0,1,0],[0,0,0,1],[-1,0,1,1]]],\"faces\":[[[0,0,1,0],[0,0,0,1],[0,1,0,0]],[[-1,1,0,1],[0,1,0,0],[0,0,0,1]],[[-1,1,0,1],[0,1,0,0],[-1,1,1,0]],[[0,0,1,0],[-1,1,1,0],[0,1,0,0]],[[0,0,1,0],[-1,1,1,0],[-1,0,1,1]],[[-1,1,0,1],[-1,0,1,1],[-1,1,1,0]],[[-1,1,0,1],[-1,0,1,1],[0,0,0,1]],[[0,0,1,0],[0,0,0,1],[-1,0,1,1]]],\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0],\"vertices\":[[0,0,1,0],[-1,1,0,1],[0,1,0,0],[0,0,0,1],[-1,1,1,0],[-1,0,1,1]]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":1,\"id\":\"chart-1\",\"index\":1,\"species\":\"neutron\"},\"packet\":{\"chart\":1,\"id\":1,\"origin\":0,\"permutation\":[3,1,2,0,4]}}}"
packet m0 _ = "{\"context\":\"complement\",\"face\":[\"0,0,0,1\",\"0,0,1,0\",\"1,0,0,0\"],\"facet\":1,\"historyLocations\":[{\"history\":\"history-1\",\"index\":0}],\"lift\":1,\"operation\":{\"face\":[\"1,0,0,0\",\"0,0,0,1\",\"0,0,1,0\"],\"id\":0,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":0,\"target\":1},\"permit\":{\"MCount\":2,\"parentFace\":[\"0,0,0,1\",\"0,0,1,0\",\"1,0,0,0\"]},\"roles\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"faces\":[[\"1,0,0,0\",\"0,0,1,0\",\"0,1,0,0\"],[\"1,0,0,0\",\"0,1,0,0\",\"0,0,0,1\"],[\"1,0,0,0\",\"0,0,0,1\",\"0,0,1,0\"],[\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]],\"geometry\":\"proton\",\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"center\":[0.25,0.25,0.25,0.25],\"components\":[[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]],\"faces\":[[[1,0,0,0],[0,0,1,0],[0,1,0,0]],[[1,0,0,0],[0,1,0,0],[0,0,0,1]],[[1,0,0,0],[0,0,0,1],[0,0,1,0]],[[0,1,0,0],[0,0,1,0],[0,0,0,1]]],\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0],\"vertices\":[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":0,\"id\":\"chart-0\",\"index\":0,\"species\":\"proton\"},\"packet\":{\"chart\":0,\"id\":0,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"target\":{\"cell\":{\"faces\":[[\"0,0,0,1\",\"0,0,1,0\",\"1,-1,1,0\"],[\"0,0,0,1\",\"1,-1,1,0\",\"1,0,0,0\"],[\"0,0,0,1\",\"1,0,0,0\",\"0,0,1,0\"],[\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]],\"geometry\":\"split\",\"id\":1,\"key\":\"0,0,0,1|0,0,1,0|1,-1,1,0|1,0,0,0\",\"owner\":{\"center\":[0.5,-0.5,0.5,0.5],\"components\":[[[1,-1,1,0],[0,0,0,1],[1,0,0,0],[1,-1,0,1]],[[0,0,0,1],[1,-1,1,0],[0,0,1,0],[1,0,0,0]],[[1,-1,1,0],[0,0,0,1],[0,-1,1,1],[0,0,1,0]],[[0,0,0,1],[1,-1,1,0],[1,-1,0,1],[0,-1,1,1]]],\"faces\":[[[1,-1,1,0],[1,-1,0,1],[1,0,0,0]],[[0,0,0,1],[1,0,0,0],[1,-1,0,1]],[[0,0,0,1],[1,0,0,0],[0,0,1,0]],[[1,-1,1,0],[0,0,1,0],[1,0,0,0]],[[1,-1,1,0],[0,0,1,0],[0,-1,1,1]],[[0,0,0,1],[0,-1,1,1],[0,0,1,0]],[[0,0,0,1],[0,-1,1,1],[1,-1,0,1]],[[1,-1,1,0],[1,-1,0,1],[0,-1,1,1]]],\"inverted\":false,\"key\":\"0,-1,1,1|0,0,0,1|0,0,1,0|1,-1,0,1|1,-1,1,0|1,0,0,0\",\"kind\":\"octahedron\",\"origin\":[0,-1,0,0],\"vertices\":[[1,-1,1,0],[0,0,0,1],[1,0,0,0],[1,-1,0,1],[0,0,1,0],[0,-1,1,1]]},\"vertices\":[\"0,0,0,1\",\"1,-1,1,0\",\"0,0,1,0\",\"1,0,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,1,0,0\",\"C1\":\"0,0,0,1\",\"C2\":\"1,-1,1,0\",\"M0\":\"1,0,0,0\",\"M1\":\"0,0,1,0\"},\"cell\":1,\"id\":\"chart-1\",\"index\":1,\"species\":\"neutron\"},\"packet\":{\"chart\":1,\"id\":1,\"origin\":0,\"permutation\":[3,1,2,0,4]}}}"
packet c1 _ = "{\"context\":\"base\",\"face\":[\"0,0,0,1\",\"0,1,0,0\",\"1,0,0,0\"],\"facet\":2,\"historyLocations\":[{\"history\":\"history-0\",\"index\":3}],\"lift\":0,\"operation\":{\"face\":[\"0,0,0,1\",\"1,0,0,0\",\"0,1,0,0\"],\"id\":6,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":6,\"target\":7},\"permit\":{\"MCount\":2,\"parentFace\":[\"0,0,0,1\",\"0,1,0,0\",\"1,0,0,0\"]},\"roles\":{\"0,0,0,1\":\"M\",\"0,0,1,0\":\"C\",\"0,1,0,0\":\"M\",\"1,0,0,0\":\"C\"},\"source\":{\"cell\":{\"faces\":[[\"1,0,0,0\",\"0,0,1,0\",\"0,1,0,0\"],[\"1,0,0,0\",\"0,1,0,0\",\"0,0,0,1\"],[\"1,0,0,0\",\"0,0,0,1\",\"0,0,1,0\"],[\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]],\"geometry\":\"proton\",\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"center\":[0.25,0.25,0.25,0.25],\"components\":[[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]],\"faces\":[[[1,0,0,0],[0,0,1,0],[0,1,0,0]],[[1,0,0,0],[0,1,0,0],[0,0,0,1]],[[1,0,0,0],[0,0,0,1],[0,0,1,0]],[[0,1,0,0],[0,0,1,0],[0,0,0,1]]],\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0],\"vertices\":[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":0,\"id\":\"chart-2\",\"index\":2,\"species\":\"proton\"},\"packet\":{\"chart\":2,\"id\":6,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"faces\":[[\"1,0,0,0\",\"0,0,0,1\",\"0,1,-1,1\"],[\"1,0,0,0\",\"0,1,-1,1\",\"0,1,0,0\"],[\"1,0,0,0\",\"0,1,0,0\",\"0,0,0,1\"],[\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]],\"geometry\":\"split\",\"id\":2,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,0,0\",\"owner\":{\"center\":[0.5,0.5,-0.5,0.5],\"components\":[[[1,0,0,0],[0,1,-1,1],[1,1,-1,0],[1,0,-1,1]],[[0,1,-1,1],[1,0,0,0],[0,1,0,0],[1,1,-1,0]],[[1,0,0,0],[0,1,-1,1],[0,0,0,1],[0,1,0,0]],[[0,1,-1,1],[1,0,0,0],[1,0,-1,1],[0,0,0,1]]],\"faces\":[[[1,0,0,0],[1,0,-1,1],[1,1,-1,0]],[[0,1,-1,1],[1,1,-1,0],[1,0,-1,1]],[[0,1,-1,1],[1,1,-1,0],[0,1,0,0]],[[1,0,0,0],[0,1,0,0],[1,1,-1,0]],[[1,0,0,0],[0,1,0,0],[0,0,0,1]],[[0,1,-1,1],[0,0,0,1],[0,1,0,0]],[[0,1,-1,1],[0,0,0,1],[1,0,-1,1]],[[1,0,0,0],[1,0,-1,1],[0,0,0,1]]],\"inverted\":false,\"key\":\"0,0,0,1|0,1,-1,1|0,1,0,0|1,0,-1,1|1,0,0,0|1,1,-1,0\",\"kind\":\"octahedron\",\"origin\":[0,0,-1,0],\"vertices\":[[1,0,0,0],[0,1,-1,1],[1,1,-1,0],[1,0,-1,1],[0,1,0,0],[0,0,0,1]]},\"vertices\":[\"1,0,0,0\",\"0,1,-1,1\",\"0,0,0,1\",\"0,1,0,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,1,0\",\"C1\":\"1,0,0,0\",\"C2\":\"0,1,-1,1\",\"M0\":\"0,0,0,1\",\"M1\":\"0,1,0,0\"},\"cell\":2,\"id\":\"chart-3\",\"index\":3,\"species\":\"neutron\"},\"packet\":{\"chart\":3,\"id\":7,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
packet m1 _ = "{\"context\":\"complement\",\"face\":[\"0,0,1,0\",\"0,1,0,0\",\"1,0,0,0\"],\"facet\":3,\"historyLocations\":[{\"history\":\"history-0\",\"index\":3}],\"lift\":1,\"operation\":{\"face\":[\"0,0,1,0\",\"0,1,0,0\",\"1,0,0,0\"],\"id\":6,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":6,\"target\":7},\"permit\":{\"MCount\":2,\"parentFace\":[\"0,0,1,0\",\"0,1,0,0\",\"1,0,0,0\"]},\"roles\":{\"0,0,0,1\":\"C\",\"0,0,1,0\":\"M\",\"0,1,0,0\":\"C\",\"1,0,0,0\":\"M\"},\"source\":{\"cell\":{\"faces\":[[\"1,0,0,0\",\"0,0,1,0\",\"0,1,0,0\"],[\"1,0,0,0\",\"0,1,0,0\",\"0,0,0,1\"],[\"1,0,0,0\",\"0,0,0,1\",\"0,0,1,0\"],[\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]],\"geometry\":\"proton\",\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"center\":[0.25,0.25,0.25,0.25],\"components\":[[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]],\"faces\":[[[1,0,0,0],[0,0,1,0],[0,1,0,0]],[[1,0,0,0],[0,1,0,0],[0,0,0,1]],[[1,0,0,0],[0,0,0,1],[0,0,1,0]],[[0,1,0,0],[0,0,1,0],[0,0,0,1]]],\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0],\"vertices\":[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":0,\"id\":\"chart-2\",\"index\":2,\"species\":\"proton\"},\"packet\":{\"chart\":2,\"id\":6,\"origin\":3,\"permutation\":[2,3,0,1,4]}},\"target\":{\"cell\":{\"faces\":[[\"0,1,0,0\",\"1,0,0,0\",\"1,0,1,-1\"],[\"0,1,0,0\",\"1,0,1,-1\",\"0,0,1,0\"],[\"0,1,0,0\",\"0,0,1,0\",\"1,0,0,0\"],[\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]],\"geometry\":\"split\",\"id\":2,\"key\":\"0,0,1,0|0,1,0,0|1,0,0,0|1,0,1,-1\",\"owner\":{\"center\":[0.5,0.5,0.5,-0.5],\"components\":[[[1,0,1,-1],[0,1,0,0],[1,1,0,-1],[1,0,0,0]],[[0,1,0,0],[1,0,1,-1],[0,1,1,-1],[1,1,0,-1]],[[1,0,1,-1],[0,1,0,0],[0,0,1,0],[0,1,1,-1]],[[0,1,0,0],[1,0,1,-1],[1,0,0,0],[0,0,1,0]]],\"faces\":[[[1,0,1,-1],[1,0,0,0],[1,1,0,-1]],[[0,1,0,0],[1,1,0,-1],[1,0,0,0]],[[0,1,0,0],[1,1,0,-1],[0,1,1,-1]],[[1,0,1,-1],[0,1,1,-1],[1,1,0,-1]],[[1,0,1,-1],[0,1,1,-1],[0,0,1,0]],[[0,1,0,0],[0,0,1,0],[0,1,1,-1]],[[0,1,0,0],[0,0,1,0],[1,0,0,0]],[[1,0,1,-1],[1,0,0,0],[0,0,1,0]]],\"inverted\":false,\"key\":\"0,0,1,0|0,1,0,0|0,1,1,-1|1,0,0,0|1,0,1,-1|1,1,0,-1\",\"kind\":\"octahedron\",\"origin\":[0,0,0,-1],\"vertices\":[[1,0,1,-1],[0,1,0,0],[1,1,0,-1],[1,0,0,0],[0,1,1,-1],[0,0,1,0]]},\"vertices\":[\"0,1,0,0\",\"1,0,1,-1\",\"1,0,0,0\",\"0,0,1,0\"]},\"chart\":{\"aliases\":{\"C0\":\"0,0,0,1\",\"C1\":\"0,1,0,0\",\"C2\":\"1,0,1,-1\",\"M0\":\"0,0,1,0\",\"M1\":\"1,0,0,0\"},\"cell\":2,\"id\":\"chart-3\",\"index\":3,\"species\":\"neutron\"},\"packet\":{\"chart\":3,\"id\":7,\"origin\":3,\"permutation\":[1,3,0,2,4]}}}"
module S = Incidence Vertex Vertex Permit Inside packet
edge : Vertex → Vertex → Bool → Vertex
edge a b false = a
edge a b true = b
data Three : Type where
  x y z : Three
triple : Vertex → Vertex → Vertex → Three → Vertex
triple a b c x = a
triple a b c y = b
triple a b c z = c
e01v2 : S.Common Bool (edge c0 m0)
e01v2 = c1 , (λ { false → tt ; true → tt })
e01v2-native : S.R.Resolve (S.selected Bool (edge c0 m0) (λ i → cert ((edge c0 m0) i)) e01v2)
e01v2-native = S.selected-proof Bool (edge c0 m0) (λ i → cert ((edge c0 m0) i)) e01v2
e01v3 : S.Common Bool (edge c0 m0)
e01v3 = m1 , (λ { false → tt ; true → tt })
e01v3-native : S.R.Resolve (S.selected Bool (edge c0 m0) (λ i → cert ((edge c0 m0) i)) e01v3)
e01v3-native = S.selected-proof Bool (edge c0 m0) (λ i → cert ((edge c0 m0) i)) e01v3
e02v1 : S.Common Bool (edge c0 c1)
e02v1 = m0 , (λ { false → tt ; true → tt })
e02v1-native : S.R.Resolve (S.selected Bool (edge c0 c1) (λ i → cert ((edge c0 c1) i)) e02v1)
e02v1-native = S.selected-proof Bool (edge c0 c1) (λ i → cert ((edge c0 c1) i)) e02v1
e02v3 : S.Common Bool (edge c0 c1)
e02v3 = m1 , (λ { false → tt ; true → tt })
e02v3-native : S.R.Resolve (S.selected Bool (edge c0 c1) (λ i → cert ((edge c0 c1) i)) e02v3)
e02v3-native = S.selected-proof Bool (edge c0 c1) (λ i → cert ((edge c0 c1) i)) e02v3
e03v1 : S.Common Bool (edge c0 m1)
e03v1 = m0 , (λ { false → tt ; true → tt })
e03v1-native : S.R.Resolve (S.selected Bool (edge c0 m1) (λ i → cert ((edge c0 m1) i)) e03v1)
e03v1-native = S.selected-proof Bool (edge c0 m1) (λ i → cert ((edge c0 m1) i)) e03v1
e03v2 : S.Common Bool (edge c0 m1)
e03v2 = c1 , (λ { false → tt ; true → tt })
e03v2-native : S.R.Resolve (S.selected Bool (edge c0 m1) (λ i → cert ((edge c0 m1) i)) e03v2)
e03v2-native = S.selected-proof Bool (edge c0 m1) (λ i → cert ((edge c0 m1) i)) e03v2
e12v0 : S.Common Bool (edge m0 c1)
e12v0 = c0 , (λ { false → tt ; true → tt })
e12v0-native : S.R.Resolve (S.selected Bool (edge m0 c1) (λ i → cert ((edge m0 c1) i)) e12v0)
e12v0-native = S.selected-proof Bool (edge m0 c1) (λ i → cert ((edge m0 c1) i)) e12v0
e12v3 : S.Common Bool (edge m0 c1)
e12v3 = m1 , (λ { false → tt ; true → tt })
e12v3-native : S.R.Resolve (S.selected Bool (edge m0 c1) (λ i → cert ((edge m0 c1) i)) e12v3)
e12v3-native = S.selected-proof Bool (edge m0 c1) (λ i → cert ((edge m0 c1) i)) e12v3
e13v0 : S.Common Bool (edge m0 m1)
e13v0 = c0 , (λ { false → tt ; true → tt })
e13v0-native : S.R.Resolve (S.selected Bool (edge m0 m1) (λ i → cert ((edge m0 m1) i)) e13v0)
e13v0-native = S.selected-proof Bool (edge m0 m1) (λ i → cert ((edge m0 m1) i)) e13v0
e13v2 : S.Common Bool (edge m0 m1)
e13v2 = c1 , (λ { false → tt ; true → tt })
e13v2-native : S.R.Resolve (S.selected Bool (edge m0 m1) (λ i → cert ((edge m0 m1) i)) e13v2)
e13v2-native = S.selected-proof Bool (edge m0 m1) (λ i → cert ((edge m0 m1) i)) e13v2
e23v0 : S.Common Bool (edge c1 m1)
e23v0 = c0 , (λ { false → tt ; true → tt })
e23v0-native : S.R.Resolve (S.selected Bool (edge c1 m1) (λ i → cert ((edge c1 m1) i)) e23v0)
e23v0-native = S.selected-proof Bool (edge c1 m1) (λ i → cert ((edge c1 m1) i)) e23v0
e23v1 : S.Common Bool (edge c1 m1)
e23v1 = m0 , (λ { false → tt ; true → tt })
e23v1-native : S.R.Resolve (S.selected Bool (edge c1 m1) (λ i → cert ((edge c1 m1) i)) e23v1)
e23v1-native = S.selected-proof Bool (edge c1 m1) (λ i → cert ((edge c1 m1) i)) e23v1
t012 : S.Common Three (triple c0 m0 c1)
t012 = m1 , (λ { x → tt ; y → tt ; z → tt })
t012-native : S.R.Resolve (S.selected Three (triple c0 m0 c1) (λ i → cert ((triple c0 m0 c1) i)) t012)
t012-native = S.selected-proof Three (triple c0 m0 c1) (λ i → cert ((triple c0 m0 c1) i)) t012
t013 : S.Common Three (triple c0 m0 m1)
t013 = c1 , (λ { x → tt ; y → tt ; z → tt })
t013-native : S.R.Resolve (S.selected Three (triple c0 m0 m1) (λ i → cert ((triple c0 m0 m1) i)) t013)
t013-native = S.selected-proof Three (triple c0 m0 m1) (λ i → cert ((triple c0 m0 m1) i)) t013
t023 : S.Common Three (triple c0 c1 m1)
t023 = m0 , (λ { x → tt ; y → tt ; z → tt })
t023-native : S.R.Resolve (S.selected Three (triple c0 c1 m1) (λ i → cert ((triple c0 c1 m1) i)) t023)
t023-native = S.selected-proof Three (triple c0 c1 m1) (λ i → cert ((triple c0 c1 m1) i)) t023
t123 : S.Common Three (triple m0 c1 m1)
t123 = c0 , (λ { x → tt ; y → tt ; z → tt })
t123-native : S.R.Resolve (S.selected Three (triple m0 c1 m1) (λ i → cert ((triple m0 c1 m1) i)) t123)
t123-native = S.selected-proof Three (triple m0 c1 m1) (λ i → cert ((triple m0 c1 m1) i)) t123
no-fourfold : S.Common Vertex (λ p → p) → ⊥
no-fourfold (c0 , w) = w c0
no-fourfold (m0 , w) = w m0
no-fourfold (c1 , w) = w c1
no-fourfold (m1 , w) = w m1
all-parents : S.R.Resolve (S.family Vertex (λ p → p) cert)
all-parents = S.family-proof Vertex (λ p → p) cert
