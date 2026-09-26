{-# OPTIONS --safe --cubical --guardedness #-}
module negative.AmplitudeResolveBadSeed where
open import ScalarAmplitudeResolveFixture
-- EXPECTED FAILURE: an algebra-constant seed cannot replace the complete
-- application tree at the expression's typed native endpoint.
bad : E.Run.Resolve (E.package expression)
bad = E.Run.seed E.zero-seed
