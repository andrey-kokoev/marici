{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NativeTableBadCertificateErasure where
open import Cubical.Foundations.Prelude
open import NativeTableRegression using (certificate-zero; certificate-one)
-- EXPECTED FAILURE: equal outputs do not erase source-certificate data.
bad : certificate-zero ≡ certificate-one
bad = refl
