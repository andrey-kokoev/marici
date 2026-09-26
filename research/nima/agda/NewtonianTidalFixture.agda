{-# OPTIONS --safe --cubical --guardedness #-}
-- Generated from check_machian_newtonian_localization.py, sources_a/jet_a.
module NewtonianTidalFixture where
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc)
open import NewtonianTidalKernel

aDirection : Vec
aDirection x = pos 1
aDirection y = pos 0
aDirection z = pos 0
a : Source
a = source (pos 2) (pos 3) (pos 64) aDirection

bDirection : Vec
bDirection x = pos 0
bDirection y = pos 1
bDirection z = pos 0
b : Source
b = source (pos 1) (pos 4) (pos 27) bDirection

denominator : ℤ
denominator = pos 1728

exportedGradient : Vec
exportedGradient x = negsuc 383
exportedGradient y = negsuc 107
exportedGradient z = pos 0
exportedTensor : Tensor
exportedTensor x x = negsuc 228
exportedTensor x y = pos 0
exportedTensor x z = pos 0
exportedTensor y x = pos 0
exportedTensor y y = pos 74
exportedTensor y z = pos 0
exportedTensor z x = pos 0
exportedTensor z y = pos 0
exportedTensor z z = pos 155
exportedJet : Jet
exportedJet = jet (negsuc 1583) exportedGradient exportedTensor
