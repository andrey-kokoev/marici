{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedWolframConstruction where
open import Cubical.Foundations.Prelude
open import Cubical.Data.List.Base using ([])
open import RefutationConstructionWG

A B C : Formula
A = atom 0
B = atom 1
C = atom 2
N : Formula → Formula → Formula
N X Y = arrow (product X Y) bottom
W D : Formula
W = N (N (N A B) C) (N A (N (N A C) A))
D = arrow (arrow C bottom) bottom

forward : Proof [] (arrow W D)
forward = (abstraction (abstraction (application (hypothesis (there here)) (pair (abstraction (application (hypothesis (there here)) (second (hypothesis here)))) (abstraction (application (second (hypothesis here)) (pair (abstraction (application (hypothesis (there (there here))) (second (hypothesis here)))) (first (hypothesis here)))))))))
forward-trace : Trace forward
forward-trace = trace forward
forward-preserved : construct forward ≡ forward
forward-preserved = construct-correct forward

backward : Proof [] (arrow D W)
backward = (abstraction (abstraction (application (hypothesis (there here)) (abstraction (application (first (hypothesis (there here))) (pair (abstraction (application (second (hypothesis (there (there here)))) (pair (first (hypothesis here)) (abstraction (application (first (hypothesis here)) (pair (first (hypothesis (there here))) (hypothesis (there (there here))))))))) (hypothesis here)))))))
backward-trace : Trace backward
backward-trace = trace backward
backward-preserved : construct backward ≡ backward
backward-preserved = construct-correct backward

swap : Proof [] (arrow (N A B) (N B A))
swap = (abstraction (abstraction (application (hypothesis (there here)) (pair (second (hypothesis here)) (first (hypothesis here))))))
swap-trace : Trace swap
swap-trace = trace swap
swap-preserved : construct swap ≡ swap
swap-preserved = construct-correct swap
