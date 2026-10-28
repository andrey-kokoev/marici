{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyExternalSeedPolicyExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
open import RamseyExternalPEExamples
open import RamseyExternalPEPolicy
BaseChart PairChart : C.Chart → Type
BaseChart C.q0 = Unit
BaseChart C.q1 = ⊥
BaseChart C.q2 = ⊥
BaseChart C.q3 = ⊥
BaseChart C.q4 = ⊥
BaseChart C.q5 = ⊥
BaseChart C.q6 = ⊥
BaseChart C.q7 = ⊥
BaseChart C.q8 = ⊥
BaseChart C.q9 = ⊥
BaseChart C.q10 = ⊥
BaseChart C.q11 = ⊥
BaseChart C.q12 = ⊥
BaseChart C.q13 = ⊥
BaseChart C.q14 = ⊥
BaseChart C.q15 = ⊥
BaseChart C.q16 = ⊥
BaseChart C.q17 = ⊥
BaseChart C.q18 = ⊥
BaseChart C.q19 = ⊥
BaseChart C.q20 = ⊥
BaseChart C.q21 = ⊥
BaseChart C.q22 = ⊥
BaseChart C.q23 = ⊥
PairChart C.q0 = Unit
PairChart C.q1 = ⊥
PairChart C.q2 = ⊥
PairChart C.q3 = ⊥
PairChart C.q4 = ⊥
PairChart C.q5 = ⊥
PairChart C.q6 = ⊥
PairChart C.q7 = Unit
PairChart C.q8 = ⊥
PairChart C.q9 = ⊥
PairChart C.q10 = ⊥
PairChart C.q11 = ⊥
PairChart C.q12 = ⊥
PairChart C.q13 = ⊥
PairChart C.q14 = ⊥
PairChart C.q15 = ⊥
PairChart C.q16 = ⊥
PairChart C.q17 = ⊥
PairChart C.q18 = ⊥
PairChart C.q19 = ⊥
PairChart C.q20 = ⊥
PairChart C.q21 = ⊥
PairChart C.q22 = ⊥
PairChart C.q23 = ⊥
module Base = Policy P.S.InputIndex (λ { (c , (v , p)) → E.A.vertex-packet c v p }) (λ i → BaseChart (fst i))
module Pair = Policy P.S.InputIndex (λ { (c , (v , p)) → E.A.vertex-packet c v p }) (λ i → PairChart (fst i))
pair-good-0-1-2 : Pair.Good tree-0-1-2
pair-good-0-1-2 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-0-1-2 : Pair.R.Resolve (P.T.encode tree-0-1-2)
pair-native-0-1-2 = Pair.realize tree-0-1-2 pair-good-0-1-2
not-base-0-1-2 : Base.Good tree-0-1-2 → ⊥
not-base-0-1-2 good = Base.all-leaves tree-0-1-2 good (P.S.full-source , (P.S.middle-port , tt))
pair-good-0-1-3 : Pair.Good tree-0-1-3
pair-good-0-1-3 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-0-1-3 : Pair.R.Resolve (P.T.encode tree-0-1-3)
pair-native-0-1-3 = Pair.realize tree-0-1-3 pair-good-0-1-3
not-base-0-1-3 : Base.Good tree-0-1-3 → ⊥
not-base-0-1-3 good = Base.all-leaves tree-0-1-3 good (P.S.full-source , (P.S.middle-port , tt))
pair-good-0-2-1 : Pair.Good tree-0-2-1
pair-good-0-2-1 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-0-2-1 : Pair.R.Resolve (P.T.encode tree-0-2-1)
pair-native-0-2-1 = Pair.realize tree-0-2-1 pair-good-0-2-1
not-base-0-2-1 : Base.Good tree-0-2-1 → ⊥
not-base-0-2-1 good = Base.all-leaves tree-0-2-1 good (P.S.full-source , (P.S.final-port , tt))
pair-good-0-2-3 : Pair.Good tree-0-2-3
pair-good-0-2-3 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-0-2-3 : Pair.R.Resolve (P.T.encode tree-0-2-3)
pair-native-0-2-3 = Pair.realize tree-0-2-3 pair-good-0-2-3
not-base-0-2-3 : Base.Good tree-0-2-3 → ⊥
not-base-0-2-3 good = Base.all-leaves tree-0-2-3 good (P.S.full-source , (P.S.final-port , tt))
pair-good-0-3-1 : Pair.Good tree-0-3-1
pair-good-0-3-1 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-0-3-1 : Pair.R.Resolve (P.T.encode tree-0-3-1)
pair-native-0-3-1 = Pair.realize tree-0-3-1 pair-good-0-3-1
not-base-0-3-1 : Base.Good tree-0-3-1 → ⊥
not-base-0-3-1 good = Base.all-leaves tree-0-3-1 good (P.S.full-source , (P.S.middle-port , tt))
pair-good-0-3-2 : Pair.Good tree-0-3-2
pair-good-0-3-2 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-0-3-2 : Pair.R.Resolve (P.T.encode tree-0-3-2)
pair-native-0-3-2 = Pair.realize tree-0-3-2 pair-good-0-3-2
not-base-0-3-2 : Base.Good tree-0-3-2 → ⊥
not-base-0-3-2 good = Base.all-leaves tree-0-3-2 good (P.S.full-source , (P.S.middle-port , tt))
pair-good-1-0-2 : Pair.Good tree-1-0-2
pair-good-1-0-2 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-1-0-2 : Pair.R.Resolve (P.T.encode tree-1-0-2)
pair-native-1-0-2 = Pair.realize tree-1-0-2 pair-good-1-0-2
not-base-1-0-2 : Base.Good tree-1-0-2 → ⊥
not-base-1-0-2 good = Base.all-leaves tree-1-0-2 good (P.S.full-source , (P.S.first-port , tt))
pair-good-1-0-3 : Pair.Good tree-1-0-3
pair-good-1-0-3 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-1-0-3 : Pair.R.Resolve (P.T.encode tree-1-0-3)
pair-native-1-0-3 = Pair.realize tree-1-0-3 pair-good-1-0-3
not-base-1-0-3 : Base.Good tree-1-0-3 → ⊥
not-base-1-0-3 good = Base.all-leaves tree-1-0-3 good (P.S.full-source , (P.S.first-port , tt))
pair-good-1-2-0 : Pair.Good tree-1-2-0
pair-good-1-2-0 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-1-2-0 : Pair.R.Resolve (P.T.encode tree-1-2-0)
pair-native-1-2-0 = Pair.realize tree-1-2-0 pair-good-1-2-0
not-base-1-2-0 : Base.Good tree-1-2-0 → ⊥
not-base-1-2-0 good = Base.all-leaves tree-1-2-0 good (P.S.full-source , (P.S.first-port , tt))
pair-good-1-2-3 : Pair.Good tree-1-2-3
pair-good-1-2-3 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-1-2-3 : Pair.R.Resolve (P.T.encode tree-1-2-3)
pair-native-1-2-3 = Pair.realize tree-1-2-3 pair-good-1-2-3
not-base-1-2-3 : Base.Good tree-1-2-3 → ⊥
not-base-1-2-3 good = Base.all-leaves tree-1-2-3 good (P.S.full-source , (P.S.first-port , tt))
pair-good-1-3-0 : Pair.Good tree-1-3-0
pair-good-1-3-0 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-1-3-0 : Pair.R.Resolve (P.T.encode tree-1-3-0)
pair-native-1-3-0 = Pair.realize tree-1-3-0 pair-good-1-3-0
not-base-1-3-0 : Base.Good tree-1-3-0 → ⊥
not-base-1-3-0 good = Base.all-leaves tree-1-3-0 good (P.S.full-source , (P.S.first-port , tt))
pair-good-1-3-2 : Pair.Good tree-1-3-2
pair-good-1-3-2 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-1-3-2 : Pair.R.Resolve (P.T.encode tree-1-3-2)
pair-native-1-3-2 = Pair.realize tree-1-3-2 pair-good-1-3-2
not-base-1-3-2 : Base.Good tree-1-3-2 → ⊥
not-base-1-3-2 good = Base.all-leaves tree-1-3-2 good (P.S.full-source , (P.S.first-port , tt))
pair-good-2-0-1 : Pair.Good tree-2-0-1
pair-good-2-0-1 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-2-0-1 : Pair.R.Resolve (P.T.encode tree-2-0-1)
pair-native-2-0-1 = Pair.realize tree-2-0-1 pair-good-2-0-1
not-base-2-0-1 : Base.Good tree-2-0-1 → ⊥
not-base-2-0-1 good = Base.all-leaves tree-2-0-1 good (P.S.full-source , (P.S.final-port , tt))
pair-good-2-0-3 : Pair.Good tree-2-0-3
pair-good-2-0-3 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-2-0-3 : Pair.R.Resolve (P.T.encode tree-2-0-3)
pair-native-2-0-3 = Pair.realize tree-2-0-3 pair-good-2-0-3
not-base-2-0-3 : Base.Good tree-2-0-3 → ⊥
not-base-2-0-3 good = Base.all-leaves tree-2-0-3 good (P.S.full-source , (P.S.final-port , tt))
pair-good-2-1-0 : Pair.Good tree-2-1-0
pair-good-2-1-0 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-2-1-0 : Pair.R.Resolve (P.T.encode tree-2-1-0)
pair-native-2-1-0 = Pair.realize tree-2-1-0 pair-good-2-1-0
not-base-2-1-0 : Base.Good tree-2-1-0 → ⊥
not-base-2-1-0 good = Base.all-leaves tree-2-1-0 good (P.S.full-source , (P.S.middle-port , tt))
pair-good-2-1-3 : Pair.Good tree-2-1-3
pair-good-2-1-3 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-2-1-3 : Pair.R.Resolve (P.T.encode tree-2-1-3)
pair-native-2-1-3 = Pair.realize tree-2-1-3 pair-good-2-1-3
not-base-2-1-3 : Base.Good tree-2-1-3 → ⊥
not-base-2-1-3 good = Base.all-leaves tree-2-1-3 good (P.S.full-source , (P.S.middle-port , tt))
pair-good-2-3-0 : Pair.Good tree-2-3-0
pair-good-2-3-0 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-2-3-0 : Pair.R.Resolve (P.T.encode tree-2-3-0)
pair-native-2-3-0 = Pair.realize tree-2-3-0 pair-good-2-3-0
not-base-2-3-0 : Base.Good tree-2-3-0 → ⊥
not-base-2-3-0 good = Base.all-leaves tree-2-3-0 good (P.S.full-source , (P.S.middle-port , tt))
pair-good-2-3-1 : Pair.Good tree-2-3-1
pair-good-2-3-1 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-2-3-1 : Pair.R.Resolve (P.T.encode tree-2-3-1)
pair-native-2-3-1 = Pair.realize tree-2-3-1 pair-good-2-3-1
not-base-2-3-1 : Base.Good tree-2-3-1 → ⊥
not-base-2-3-1 good = Base.all-leaves tree-2-3-1 good (P.S.full-source , (P.S.middle-port , tt))
pair-good-3-0-1 : Pair.Good tree-3-0-1
pair-good-3-0-1 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-3-0-1 : Pair.R.Resolve (P.T.encode tree-3-0-1)
pair-native-3-0-1 = Pair.realize tree-3-0-1 pair-good-3-0-1
not-base-3-0-1 : Base.Good tree-3-0-1 → ⊥
not-base-3-0-1 good = Base.all-leaves tree-3-0-1 good (P.S.full-source , (P.S.first-port , tt))
pair-good-3-0-2 : Pair.Good tree-3-0-2
pair-good-3-0-2 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-3-0-2 : Pair.R.Resolve (P.T.encode tree-3-0-2)
pair-native-3-0-2 = Pair.realize tree-3-0-2 pair-good-3-0-2
not-base-3-0-2 : Base.Good tree-3-0-2 → ⊥
not-base-3-0-2 good = Base.all-leaves tree-3-0-2 good (P.S.full-source , (P.S.first-port , tt))
pair-good-3-1-0 : Pair.Good tree-3-1-0
pair-good-3-1-0 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-3-1-0 : Pair.R.Resolve (P.T.encode tree-3-1-0)
pair-native-3-1-0 = Pair.realize tree-3-1-0 pair-good-3-1-0
not-base-3-1-0 : Base.Good tree-3-1-0 → ⊥
not-base-3-1-0 good = Base.all-leaves tree-3-1-0 good (P.S.full-source , (P.S.first-port , tt))
pair-good-3-1-2 : Pair.Good tree-3-1-2
pair-good-3-1-2 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-3-1-2 : Pair.R.Resolve (P.T.encode tree-3-1-2)
pair-native-3-1-2 = Pair.realize tree-3-1-2 pair-good-3-1-2
not-base-3-1-2 : Base.Good tree-3-1-2 → ⊥
not-base-3-1-2 good = Base.all-leaves tree-3-1-2 good (P.S.full-source , (P.S.first-port , tt))
pair-good-3-2-0 : Pair.Good tree-3-2-0
pair-good-3-2-0 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-3-2-0 : Pair.R.Resolve (P.T.encode tree-3-2-0)
pair-native-3-2-0 = Pair.realize tree-3-2-0 pair-good-3-2-0
not-base-3-2-0 : Base.Good tree-3-2-0 → ⊥
not-base-3-2-0 good = Base.all-leaves tree-3-2-0 good (P.S.full-source , (P.S.first-port , tt))
pair-good-3-2-1 : Pair.Good tree-3-2-1
pair-good-3-2-1 = λ { P.S.AB → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.BC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.AC → λ { (v , (p , q)) → λ { P.S.source-leg → tt ; P.S.target-leg → tt } } ; P.S.full-source → λ { P.S.first-port → tt ; P.S.middle-port → tt ; P.S.final-port → tt } }
pair-native-3-2-1 : Pair.R.Resolve (P.T.encode tree-3-2-1)
pair-native-3-2-1 = Pair.realize tree-3-2-1 pair-good-3-2-1
not-base-3-2-1 : Base.Good tree-3-2-1 → ⊥
not-base-3-2-1 good = Base.all-leaves tree-3-2-1 good (P.S.full-source , (P.S.first-port , tt))
