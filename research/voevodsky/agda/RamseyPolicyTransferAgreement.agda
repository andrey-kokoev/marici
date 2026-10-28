{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPolicyTransferAgreement where
open import Cubical.Foundations.Prelude
open import Agda.Builtin.String using (String)
import RamseyExternalPolicyTransport as Transport

module Agreement (Source : Type) (payload : Source → String)
  (Allowed TargetAllowed : Source → Type) where
  module F = Transport.Transfer Source payload Allowed TargetAllowed
  agree : (s t : F.T.Tree)
    {back₀ back₁ : F.T.Occurrence t → F.T.Occurrence s}
    (back-path : back₀ ≡ back₁)
    {admit₀ : (o : F.T.Occurrence t) → Allowed (F.T.origin s (back₀ o)) → TargetAllowed (F.T.origin t o)}
    {admit₁ : (o : F.T.Occurrence t) → Allowed (F.T.origin s (back₁ o)) → TargetAllowed (F.T.origin t o)}
    (admit-path : PathP (λ i → (o : F.T.Occurrence t) → Allowed (F.T.origin s (back-path i o)) → TargetAllowed (F.T.origin t o)) admit₀ admit₁)
    → F.transfer s t back₀ admit₀ ≡ F.transfer s t back₁ admit₁
  agree s t back-path admit-path i = F.transfer s t (back-path i) (admit-path i)
