{-# OPTIONS --safe --cubical --guardedness #-}
module negative.RecursiveTablesBadCertificateErasure where
open import Cubical.Foundations.Prelude
open import RecursiveTableRegression using (certificate-zero; certificate-one)
-- EXPECTED FAILURE: the same output does not identify supplied certificates.
bad : certificate-zero ≡ certificate-one
bad = refl
