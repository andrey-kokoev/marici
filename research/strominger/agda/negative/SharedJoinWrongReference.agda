{-# OPTIONS --safe --cubical --guardedness #-}
module SharedJoinWrongReference where
open import Cubical.Data.Bool.Base using (false)
open import NativeSharedReaderJoin
module P = Prepared (λ _ → false)
-- Equal scalar payloads do not make distinct reference identities identical.
bad : RecordAt E+
bad = N.value (P.input E-)
