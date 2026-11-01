{-# OPTIONS --safe --cubical --guardedness #-}
module Su32JoinInconsistentConsumer where
open import Cubical.Foundations.Prelude
import NativeSharedReaderJoin as Native
module N = Native.N
open import Su32CoherentReferenceCarrier
module Z = Counterexample.Z
bad : N.Ty Z.Consumer.result
bad = (N.value Z.C.result , Counterexample.changedD , refl) , N.value Z.Consumer.provenance
