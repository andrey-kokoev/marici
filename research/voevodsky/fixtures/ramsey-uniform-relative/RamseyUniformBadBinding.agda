{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyUniformBadBinding where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (zero; suc)
open import Cubical.Data.Int.Base using (pos; negsuc)
open import Agda.Builtin.String using (String)
open import RamseyUniformRelative
open import RamseyUniformSigned
at110 : Slot 1 → Point3
at110 first = pos 1 , (pos 1 , pos 0)
ctx : Slot 1 → String
ctx first = "{\"PN\":{\"operation\":{\"face\":[\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"],\"id\":170,\"kind\":\"PN\",\"permutation\":[3,1,2,0,4],\"phaseDelta\":0,\"source\":0,\"target\":256},\"target\":{\"cell\":{\"id\":1,\"key\":\"-1,1,0,1|0,0,0,1|0,0,1,0|0,1,0,0\",\"owner\":{\"inverted\":false,\"key\":\"-1,0,1,1|-1,1,0,1|-1,1,1,0|0,0,0,1|0,0,1,0|0,1,0,0\",\"kind\":\"octahedron\",\"origin\":[-1,0,0,0]},\"vertices\":[\"0,0,1,0\",\"-1,1,0,1\",\"0,1,0,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":1,\"id\":\"chart-256\",\"species\":\"neutron\"},\"packet\":{\"chart\":256,\"id\":256,\"origin\":0,\"permutation\":[3,1,2,0,4]}},\"targetFrame\":{\"context\":{\"index\":2,\"role\":\"C\",\"vertex\":\"-1,1,0,1\"},\"id\":\"chart-256@0\",\"species\":\"neutron\",\"window\":[{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"},{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"}]}},\"frame\":{\"context\":{\"index\":1,\"role\":\"M\",\"vertex\":\"0,0,0,1\"},\"id\":\"chart-0@0\",\"species\":\"proton\",\"window\":[{\"index\":0,\"role\":\"C\",\"vertex\":\"1,0,0,0\"},{\"index\":0,\"role\":\"M\",\"vertex\":\"0,1,0,0\"},{\"index\":1,\"role\":\"C\",\"vertex\":\"0,0,1,0\"}]},\"index\":85,\"packet\":{\"cell\":{\"id\":0,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"owner\":{\"inverted\":false,\"key\":\"0,0,0,1|0,0,1,0|0,1,0,0|1,0,0,0\",\"kind\":\"tetrahedron\",\"origin\":[0,0,0,0]},\"vertices\":[\"1,0,0,0\",\"0,1,0,0\",\"0,0,1,0\",\"0,0,0,1\"]},\"chart\":{\"aliases\":{\"C0\":\"1,0,0,0\",\"C1\":\"0,0,1,0\",\"C2\":\"-1,1,0,1\",\"M0\":\"0,1,0,0\",\"M1\":\"0,0,0,1\"},\"cell\":0,\"id\":\"chart-0\",\"species\":\"proton\"},\"packet\":{\"chart\":0,\"id\":0,\"origin\":0,\"permutation\":[0,1,2,3,4]}},\"point\":[0,0,0],\"shift\":[0,0,0,0]}"
c : Slot 1 → Slot 1
c first = first
module U = Compiler signed-geometry 1 1 1 1 at110 at110 ctx c
w : U.Request
w = cons first nil
native-valid : U.R.Resolve (U.result-package w)
native-valid = U.result w
relative-certificate : U.Certified (U.A.phi w)
relative-certificate = U.certified-query w

claimed-sector-binding : zero3 ≡ at110 first
claimed-sector-binding = refl
