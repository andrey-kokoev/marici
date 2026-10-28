{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessGeneratorBadReverseDynamics where
open import NativeExtensionFamilyAudit using (Edge; D; A; AD)
-- Reverse presentation does not supply the absent reverse execution edge.
bad : Edge D A
bad = AD
