{-# OPTIONS --safe --cubical --guardedness #-}
module SyncBadIndependentRequest where
import ContinuationSidePolicies as P
open import SynchronizedContinuationAdapter
bad : Example.Request
bad = P.independent-pair
