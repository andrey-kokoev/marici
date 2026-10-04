{-# OPTIONS --safe --cubical --guardedness #-}
module NativeApplicationBadReadout where
open import NativeApplicationGate
-- Retaining operands with a successful external readout is not a derivation
-- whose endpoint is the retained evaluated codomain package.
bad : Run.Resolve retained-answer
bad = paired-run
