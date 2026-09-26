{-# OPTIONS --safe --cubical --guardedness #-}
module NewtonRadialCoefficients where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc; _+_; _·_; -_)
open import Cubical.Data.Int.Properties using (-Involutive)
open import Cubical.Data.Sigma.Base using (_×_)
-- Compile the conditional continuum-interface theorem as part of this closure.
import NewtonFromPoisson

-- Formal Laurent coefficient calculus in dimension three:
-- Delta(r^n) = n(n+1) r^(n-2), away from zero.
-- Its interpretation as real differentiation is stated in the accompanying
-- mathematical proof, not established by this coefficient computation.
radialLaplacianCoefficient : ℤ → ℤ
radialLaplacianCoefficient n = n · (n + pos 1)
constant-is-vacuum : radialLaplacianCoefficient (pos 0) ≡ pos 0
constant-is-vacuum = refl
inverse-is-vacuum : radialLaplacianCoefficient (negsuc 0) ≡ pos 0
inverse-is-vacuum = refl
inverse-square-is-not-vacuum : radialLaplacianCoefficient (negsuc 1) ≡ pos 2
inverse-square-is-not-vacuum = refl

-- For Phi=A+B/r, normalized outward flux is -B.
-- The coefficient is SOLVED from supplied source flux, not assumed.
coefficient-from-flux : (B K : ℤ) → (- B) ≡ K → B ≡ (- K)
coefficient-from-flux B K flux = sym (-Involutive B) ∙ cong (λ v → - v) flux
source-normalization : (K : ℤ) → (- (- K)) ≡ K
source-normalization = -Involutive

-- Once radial vacuum integration has supplied A+B/r, decay removes A and
-- Gauss fixes B. This theorem is generic in the integer-scaled coefficients.
coefficientPair : ℤ → ℤ → ℤ × ℤ
coefficientPair A B = A , B
coefficients-derived : (A B K : ℤ) → A ≡ pos 0 → (- B) ≡ K
  → coefficientPair A B ≡ coefficientPair (pos 0) (- K)
coefficients-derived A B K decay flux = cong₂ _,_ decay (coefficient-from-flux B K flux)

normalizedFluxNumerator : ℤ → ℤ → ℤ
normalizedFluxNumerator radius slopeUnits = radius · radius · slopeUnits
flux-example : normalizedFluxNumerator (pos 2) (pos 3) ≡ pos 12
flux-example = refl
fixed-coefficients : coefficientPair (pos 0) (negsuc 5) ≡ coefficientPair (pos 0) (negsuc 5)
fixed-coefficients = coefficients-derived (pos 0) (negsuc 5) (pos 6) refl refl
