{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureProductBoundary where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv-fst; Σ-cong-equiv-snd; fiberProjEquiv)
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.Pushout.Properties using (PushoutAlongEquiv)
open import ClosureCanonicalRejoin using (module Rejoin; module Naturality)

-- A concrete cofiber realization of ANY pointed target. The filtration is
-- Bool -> Unit -> X, so the nested attachment domain is nonempty.
module PointedModel (X : Type) (x₀ : X) where
  f : Bool → Unit
  f _ = tt

  g : Unit → X
  g _ = x₀

  module R = Rejoin f g

  coneEquiv : cofib g ≃ X
  coneEquiv = isoToEquiv (PushoutAlongEquiv (idEquiv Unit) g)

  presentation : R.Quotient ≃ X
  presentation = compEquiv R.rejoinEquiv coneEquiv

-- Once an observation is chosen, the correct ALWAYS-AVAILABLE factorization
-- is dependent: total data equals observation plus its homotopy fiber.
module Observation {X P : Type} (observe : X → P) where
  totalIso : Iso X (Σ[ p ∈ P ] fiber observe p)
  Iso.fun totalIso x = observe x , (x , refl)
  Iso.inv totalIso (_ , (x , _)) = x
  Iso.rightInv totalIso (p , (x , h)) i =
    h i , (x , λ j → h (i ∧ j))
  Iso.leftInv totalIso x = refl

  dependentPresentation : X ≃ (Σ[ p ∈ P ] fiber observe p)
  dependentPresentation = isoToEquiv totalIso

  -- A uniform product requires a coherent family of fiber equivalences,
  -- not merely a matching arity or an equality of numerical dimensions.
  productFromFibers : (R : Type) → ((p : P) → fiber observe p ≃ R) → X ≃ (P × R)
  productFromFibers R trivialize = compEquiv dependentPresentation
    (Σ-cong-equiv-snd trivialize)

  preservesObservation : (R : Type) (trivialize : (p : P) → fiber observe p ≃ R)
    (x : X) → fst (equivFun (productFromFibers R trivialize) x) ≡ observe x
  preservesObservation R trivialize x = refl

-- Positive case: a genuine Pi family and an independent boundary object.
module Split (I : Type) (B : I → Type) (R : Type)
  (p₀ : (i : I) → B i) (r₀ : R) where
  P : Type
  P = (i : I) → B i

  module M = PointedModel (P × R) (p₀ , r₀)

  factorization : M.R.Quotient ≃ (P × R)
  factorization = M.presentation

  encode : M.R.Quotient → P × R
  encode = equivFun factorization

  assemble : P × R → M.R.Quotient
  assemble = invEq factorization

  recoverCoordinates : (z : P × R) → encode (assemble z) ≡ z
  recoverCoordinates = secEq factorization

  recoverQuotient : (x : M.R.Quotient) → assemble (encode x) ≡ x
  recoverQuotient = retEq factorization

-- The split is compatible with the ACTUAL target-transport map on double
-- cofibers, not just an arbitrary equivalence between underlying types.
module SplitMap (I J : Type) (B : I → Type) (D : J → Type)
  (R S : Type) (p₀ : (i : I) → B i) (r₀ : R)
  (mapP : ((i : I) → B i) → ((j : J) → D j)) (mapR : R → S) where
  module Input = Split I B R p₀ r₀
  module Output = Split J D S (mapP p₀) (mapR r₀)

  coordinates : Input.P × R → Output.P × S
  coordinates (p , r) = mapP p , mapR r

  module N = Naturality Input.M.f Input.M.g coordinates

  coneNaturality : (y : cofib Input.M.g) →
    equivFun Output.M.coneEquiv (N.Lower.direct y) ≡
    coordinates (equivFun Input.M.coneEquiv y)
  coneNaturality (inl tt) = refl
  coneNaturality (inr z) = refl
  coneNaturality (push tt i) = refl

  factorizationNaturality : (x : Input.M.R.Quotient) →
    Output.encode (N.upper x) ≡ coordinates (Input.encode x)
  factorizationNaturality x =
    cong (equivFun Output.M.coneEquiv) (N.rejoinSquare x)
    ∙ coneNaturality (Input.M.R.rejoin x)

  coordinateOperation : Input.P × R → Output.P × S
  coordinateOperation z = Output.encode (N.upper (Input.assemble z))

  coordinateOperationLaw : (z : Input.P × R) → coordinateOperation z ≡ coordinates z
  coordinateOperationLaw z = factorizationNaturality (Input.assemble z)
    ∙ cong coordinates (Input.recoverCoordinates z)

  -- The four concrete signatures, now with actual Pi-and-boundary objects
  -- in the expanded positions. The unary positions remain single cofibers.
  F1 : cofib Input.M.g → cofib Output.M.g
  F1 = N.Lower.direct

  F2 : cofib Input.M.g → Output.P × S
  F2 y = Output.encode (Output.M.R.cut (F1 y))

  inputRejoin : Input.P × R → cofib Input.M.g
  inputRejoin z = Input.M.R.rejoin (Input.assemble z)

  outputRejoin : Output.P × S → cofib Output.M.g
  outputRejoin z = Output.M.R.rejoin (Output.assemble z)

  inputRejoinEquiv : (Input.P × R) ≃ cofib Input.M.g
  inputRejoinEquiv = compEquiv (invEquiv Input.factorization) Input.M.R.rejoinEquiv

  outputRejoinEquiv : (Output.P × S) ≃ cofib Output.M.g
  outputRejoinEquiv = compEquiv (invEquiv Output.factorization) Output.M.R.rejoinEquiv

  F3 : Input.P × R → cofib Output.M.g
  F3 z = F1 (inputRejoin z)

  F4 : Input.P × R → Output.P × S
  F4 = coordinateOperation

  outputRejoin-F2 : (y : cofib Input.M.g) → outputRejoin (F2 y) ≡ F1 y
  outputRejoin-F2 y =
    cong Output.M.R.rejoin (Output.recoverQuotient (Output.M.R.cut (F1 y)))
    ∙ Output.M.R.rejoin-cut (F1 y)

  outputRejoin-F4 : (z : Input.P × R) → outputRejoin (F4 z) ≡ F3 z
  outputRejoin-F4 z =
    cong Output.M.R.rejoin (Output.recoverQuotient (N.upper (Input.assemble z)))
    ∙ N.rejoinSquare (Input.assemble z)

  F4-as-F2 : (z : Input.P × R) → F4 z ≡ F2 (inputRejoin z)
  F4-as-F2 z = cong Output.encode
    (sym (Output.M.R.cut-rejoin (N.upper (Input.assemble z)))
      ∙ cong Output.M.R.cut (N.rejoinSquare (Input.assemble z)))

-- A family whose boundary genuinely depends on the Pi coordinate.
-- This gives an actual cofiber-model counterexample to a uniform residual
-- over a FIXED observation, not a claim that no other factorization exists.
module DependentCounterexample where
  P : Type
  P = Bool → Bool

  boundary : Bool → Type
  boundary false = Unit
  boundary true = Bool

  R : P → Type
  R p = boundary (p false)

  p₀ p₁ : P
  p₀ _ = false
  p₁ _ = true

  module M = PointedModel (Σ P R) (p₀ , tt)

  observe : M.R.Quotient → P
  observe x = fst (equivFun M.presentation x)

  fiberIdentification : (p : P) → fiber observe p ≃ R p
  fiberIdentification p = compEquiv
    (Σ-cong-equiv-fst {B = λ z → fst z ≡ p} M.presentation)
    (invEquiv (fiberProjEquiv P R p))

  noBoolUnit : Bool ≃ Unit → ⊥
  noBoolUnit e = false≢true (sym (retEq e false) ∙ retEq e true)

  noUniformBoundary : (R₀ : Type) → ((p : P) → fiber observe p ≃ R₀) → ⊥
  noUniformBoundary R₀ trivialize = noBoolUnit
    (compEquiv (invEquiv (fiberIdentification p₁))
      (compEquiv (trivialize p₁)
        (compEquiv (invEquiv (trivialize p₀)) (fiberIdentification p₀))))

  -- A product equivalence respecting the chosen Pi observation would
  -- trivialize all its fibers. Hence this stronger proposed split is absent.
  noProductOverObservation : (R₀ : Type) (e : M.R.Quotient ≃ (P × R₀)) →
    ((x : M.R.Quotient) → fst (equivFun e x) ≡ observe x) → ⊥
  noProductOverObservation R₀ e over = noUniformBoundary R₀ (λ p →
    compEquiv
      (pathToEquiv (cong (λ obs → fiber obs p) (sym (funExt over))))
      (compEquiv (Σ-cong-equiv-fst {B = λ z → fst z ≡ p} e)
        (invEquiv (fiberProjEquiv P (λ _ → R₀) p))))

-- The positive model has a product-shaped target BY CONSTRUCTION. It proves
-- this signature is realizable and coherent, not that arbitrary analytical
-- endpoint families supply such a split. The negative result keeps P fixed
-- and requires preservation of its observation, as a labelled presentation
-- must; it is not an unlabelled cardinality classification of total spaces.
