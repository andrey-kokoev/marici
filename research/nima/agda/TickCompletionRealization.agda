{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionRealization where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Algebra.CommRing.Base using (CommRing→Ring)
open import CauchyCompletionCommRing using (CompletionCommRing; oneCompletion)
open import CauchyCompletionAbGroup using (zeroCompletion)
import TickPolynomialRealization as Polynomial

-- The existing constructive rational Cauchy-completion ring, not an
-- assumed scalar ring. This supplies exact completion-valued amplitudes.
module Realization = Polynomial.Polynomial (CommRing→Ring CompletionCommRing)
module AtOrigin = Realization.ForSource (false , false)

fresh-target : AtOrigin.realization AtOrigin.D.fresh oneCompletion oneCompletion
  ≡ Realization.basis (true , true)
fresh-target = AtOrigin.target-preserved AtOrigin.D.fresh

swapped-target : AtOrigin.realization AtOrigin.D.swapped oneCompletion oneCompletion
  ≡ Realization.basis (true , true)
swapped-target = AtOrigin.target-preserved AtOrigin.D.swapped

-- The instantiated module also exports source, both intermediate corners,
-- both ordered schedule executions, and actual return endpoint proofs for
-- arbitrary Ticks. This module does not yet prove metric continuity.
