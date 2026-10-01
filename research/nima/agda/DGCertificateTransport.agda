{-# OPTIONS --safe --cubical --guardedness #-}
module DGCertificateTransport where

open import Cubical.Foundations.Prelude
open import DGHistoryTransport
open import DGFrameUpdates

-- Extra ordinary graded algebra laws needed for certificate inversion.
-- This remains a conditional algebra theorem, not a concrete DG instance.
record CertificateAlgebra : Type₁ where
  field
    frame-algebra : FrameAlgebra
  open FrameAlgebra frame-algebra public
  field
    neg1 : D1 → D1
    neg2 : D2 → D2
    delta-neg : (k : D2) → delta2 (neg2 k) ≡ neg1 (delta2 k)
    neg-sub : (x y : D1) → neg1 (sub1 x y) ≡ sub1 y x
    unit01 : (v : D1) → m01 one v ≡ v
    unit10 : (v : D1) → m10 v one ≡ v

module Certificates (A : CertificateAlgebra) where
  open CertificateAlgebra A
  module T = Transport fragment

  composite-K : D0 → D0 → D2 → D2 → D2
  composite-K h g kh kg = add2 (m02 h kg) (m20 kh g)

  composite-certificate : (h g : D0) (v : D1) (kh kg : D2)
    → delta2 kh ≡ T.commutator h v
    → delta2 kg ≡ T.commutator g v
    → delta2 (composite-K h g kh kg) ≡ T.commutator (m00 h g) v
  composite-certificate h g v kh kg ph pg =
    delta-add (m02 h kg) (m20 kh g)
    ∙ cong₂ add1 (delta-left h kg) (delta-right kh g)
    ∙ cong₂ add1 (cong (m01 h) pg) (cong (λ x → m10 x g) ph)
    ∙ T.cancellation h g v v

  inverse-K : D0 → D2 → D2
  inverse-K gi k = neg2 (m20 (m02 gi k) gi)

  inverse-cancellation : (g gi : D0) (v : D1)
    → m00 gi g ≡ one → m00 g gi ≡ one
    → m10 (m01 gi (T.commutator g v)) gi
      ≡ sub1 (m10 v gi) (m01 gi v)
  inverse-cancellation g gi v li ri =
    cong (λ x → m10 x gi) (left-sub gi (m01 g v) (m10 v g))
    ∙ right-sub (m01 gi (m01 g v)) (m01 gi (m10 v g)) gi
    ∙ cong₂ sub1
      (cong (λ x → m10 x gi)
        (assoc001 gi g v ∙ cong (λ x → m01 x v) li ∙ unit01 v))
      (cong (λ x → m10 x gi) (assoc010 gi v g)
        ∙ assoc100 (m01 gi v) g gi
        ∙ cong (m10 (m01 gi v)) ri
        ∙ unit10 (m01 gi v))

  inverse-certificate : (g gi : D0) (v : D1) (k : D2)
    → m00 gi g ≡ one → m00 g gi ≡ one
    → delta2 k ≡ T.commutator g v
    → delta2 (inverse-K gi k) ≡ T.commutator gi v
  inverse-certificate g gi v k li ri pk =
    delta-neg (m20 (m02 gi k) gi)
    ∙ cong neg1
      (delta-right (m02 gi k) gi
      ∙ cong (λ x → m10 x gi) (delta-left gi k)
      ∙ cong (λ x → m10 (m01 gi x) gi) pk
      ∙ inverse-cancellation g gi v li ri)
    ∙ neg-sub (m10 v gi) (m01 gi v)
