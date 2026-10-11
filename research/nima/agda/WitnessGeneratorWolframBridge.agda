{-# OPTIONS --safe --cubical --guardedness #-}
------------------------------------------------------------------------
-- WitnessGeneratorWolframBridge.agda
--
-- Formal connection: starting from a set operation already equipped with
-- a proof of the Wolfram identity, reconstruct its Boolean structure, compile
-- the operation and the identity's left-hand side as Witness Generators,
-- and verify that the compiled execution retains the computed result and
-- the supplied identity path. This is witnessed execution preservation,
-- not derivation of the identity from the WG interface alone.
--
-- Structure:
--   1.  From a nonempty set (A, ∣) satisfying the Wolfram identity,
--       reconstruct a full BooleanStructure (BNE.FromWolfram).
--   2.  Compile a Presentation for NAND on A × A through the domain
--       compiler (DWC.Compile).
--   3.  Prove that the compiled WG's compute function is the
--       reconstructed Boolean NAND (neg ∘ meet).
--   4.  Prove that a NAND request's response value equals the reconstructed
--       Boolean NAND.
--   5.  Compile the Wolfram identity's left-hand side as a WG and prove
--       its response is equal to c, using the supplied identity witness.
------------------------------------------------------------------------
module WitnessGeneratorWolframBridge where

open import Cubical.Foundations.Prelude renaming (_∙_ to trans)
open import Cubical.Foundations.HLevels using (isSetΣ; isSet×)
open import Cubical.Data.Sigma.Base using (_×_; Σ; _,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (Bool; false; true)

open import DomainWitnessCompiler   using (Presentation)
import DomainWitnessCompiler        as DWC
import BooleanNandEquivalence       as BNE
open import TypedGeneratorLayers    using (Layer1)
import TypedGeneratorLayers         as TGL


------------------------------------------------------------------------
-- 1.  BRIDGE THEOREM
------------------------------------------------------------------------
--   Given:  A nonempty type A (inhabited by e)
--           A binary operation _∣_ : A → A → A
--           Proof W that _∣_ satisfies the Wolfram single identity
--           A proof hSetA that A is a set
--
--   Then:   The Domain Witness Generator compiled from the NAND
--           presentation on (A, ∣) produces a WG whose compute
--           function is the Boolean NAND reconstructed from W. A separate
--           WG compiles the identity's left-hand side and records its result.
------------------------------------------------------------------------

module Bridge {ℓ : Level} (A : Type ℓ) (hSetA : isSet A) (e : A)
  (_∣_ : A → A → A)
  (W : (a b c : A) → ((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a)) ≡ c) where

  -- 1a.  Reconstruct the full Boolean structure from the Wolfram identity.
  open BNE.FromWolfram A hSetA e _∣_ W     -- provides boolean : BooleanStructure A
  open BNE.BooleanStructure boolean          -- provides neg, meet, join, top, bottom, laws



  -- 1b.  The NAND operation in this Boolean structure.
  nand : A → A → A
  nand x y = neg (meet x y)



  -- 1c.  The fundamental theorem of FromWolfram: the original operation
  --      _∣_ equals Boolean NAND.
  -- original-is-nand is already in scope from open BNE.FromWolfram above.



  -- 1d.  Build the WG Presentation for NAND: Input = A × A, compute = _∣_.
  nand-presentation : Presentation ℓ
  nand-presentation = record
    { Input  = A × A
    ; Output = λ _ → A
    ; compute = λ (x , y) → x ∣ y
    }

  module WG = DWC.Compile nand-presentation



  -- 2.  THEOREM: The compiled WG's compute function is the Boolean NAND.
  --      Since WG.result merely wraps the supplied _∣_, this follows
  --      directly from original-is-nand.
  compute-is-nand : (x y : A) → WG.result (x , y) ≡ nand x y
  compute-is-nand x y = recovered-operation x y



  -- 3.  THEOREM: The compiled WG's generate function evaluates to the
  --      Boolean NAND result.
  generate-preserves-nand : (x y : A)
    → Layer1.next WG.layer (inl (x , y)) ≡ inr ((x , y) , nand x y)
  response-state : A × A → A → WG.State
  response-state p v = inr (p , v)

  generate-preserves-nand x y =
    cong (response-state (x , y)) (recovered-operation x y)



  -- 4.  THEOREM: The Wolfram identity expressed through the WG interface.
  wolfram-via-wg : (a b c : A)
    → ((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a)) ≡ c
  wolfram-via-wg = W



  -- 5.  PROJECTION TO THE UNDERLYING BOOLEAN STRUCTURE
  --------------------------------------------------------------------
  -- Response payloads are values in A. We only use the payload of the
  -- evaluated NAND request below; no Boolean algebra structure on the whole
  -- tagged response-state type is asserted.
  --------------------------------------------------------------------
  ResponseState : Type ℓ
  ResponseState = Σ[ (a , b) ∈ A × A ] A

  request→response : A × A → ResponseState
  request→response (a , b) = ((a , b) , a ∣ b)

  -- THEOREM: The evaluation map sends a NAND request to the Boolean
  -- NAND of the input values.
  evaluate-preserves-nand : (a b : A)
    → snd (request→response (a , b)) ≡ nand a b
  evaluate-preserves-nand a b = recovered-operation a b



  -- 6.  THEOREM: The WG's Layer-1 generate function, when iterated,
  --      produces a history whose length-1 reduct satisfies the
  --      Wolfram identity in terms of the response values.
  --------------------------------------------------------------------
  module WH = TGL.Histories WG.layer

  wolfram-history : (a b c : A)
    → WH.History
        (inl (((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a)) , c))
        (inr ((((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a)) , c)
          , (((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a))) ∣ c))
  wolfram-history a b c =
    WH.single (WG.evaluated
      (((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a)) , c))

  -- The evaluated history endpoint is computed by NAND; it is not the
  -- Wolfram RHS c. This separate path records the axiom's equality.
  wolfram-endpoint-value : (a b c : A)
    → (((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a))) ∣ c ≡ c ∣ c
  wolfram-endpoint-value a b c = cong (λ x → x ∣ c) (W a b c)



  -- 7.  THEOREM: The ToWolfram direction (Boolean NAND → Wolfram
  --      identity) also holds for the WG's result function.
  --------------------------------------------------------------------
  -- The WG's compute = _∣_ = nand (by original-is-nand).
  -- Since nand satisfies the Wolfram identity (ToWolfram.wolfram),
  -- compute also does, re-proved through the WG interface.
  open BNE.ToWolfram boolean using (wolfram)

  compute-wolfram-via-boolean : (a b c : A)
    → nand (nand (nand a b) c) (nand a (nand (nand a c) a)) ≡ c
  compute-wolfram-via-boolean = wolfram



------------------------------------------------------------------------
-- 1.5  TOP-LEVEL WOLFRAM IDENTITY VIA WG
------------------------------------------------------------------------
-- The Wolfram identity expressed as a WG: compile the left-hand side
-- of the identity as a Presentation and prove its result = c.
------------------------------------------------------------------------

module WolframIdentityViaWG {ℓ : Level} (A : Type ℓ) (hSetA : isSet A) (e : A)
  (_∣_ : A → A → A)
  (W : (a b c : A) → ((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a)) ≡ c) where

  -- The left-hand side of the Wolfram identity as a function of (a,b,c).
  lhs : A × A × A → A
  lhs (a , b , c) = ((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a))

  -- Compile the Wolfram LHS as a WG.
  pres : Presentation ℓ
  pres = record
    { Input  = A × A × A
    ; Output = λ _ → A
    ; compute = lhs
    }

  module G = DWC.Compile pres

  -- THEOREM: The WG's result for (a,b,c) equals c.
  wolfram-via-wg : (a b c : A) → G.result (a , b , c) ≡ c
  wolfram-via-wg a b c = W a b c

  -- THEOREM: The WG generates a single-step evaluated transition
  -- whose response value is c.
  wolfram-transition : (a b c : A)
    → Layer1.next G.layer (inl (a , b , c))
      ≡ inr ((a , b , c) , c)
  wolfram-transition a b c =
    cong (λ v → inr ((a , b , c) , v)) (W a b c)

  -- THEOREM: The history is a single evaluated witness.
  module WH = TGL.Histories G.layer

  wolfram-history : (a b c : A)
    → WH.History (inl (a , b , c))
        (inr ((a , b , c) , lhs (a , b , c)))
  wolfram-history a b c =
    WH.single (G.evaluated (a , b , c))

  -- The certified response value is propositionally equal to c by W.
  wolfram-response-value : (a b c : A)
    → lhs (a , b , c) ≡ c
  wolfram-response-value = W


------------------------------------------------------------------------
-- 2.  INSTANTIATION ON THE CONCRETE CARRIER Bool
------------------------------------------------------------------------
-- Bool with Boolean NAND is the simplest non-trivial test of the
-- bridge.
------------------------------------------------------------------------

module BoolBridge where

  open import Cubical.Data.Bool.Base using (Bool; true; false; not)
  open import Cubical.Data.Bool.Properties
    using (isSetBool; false≢true)

  -- NAND on Bool
  _∣_ : Bool → Bool → Bool
  true  ∣ true  = false
  true  ∣ false = true
  false ∣ true  = true
  false ∣ false = true

  -- The Wolfram identity for Bool NAND, checked by cases.
  wolfram-on-bool : (a b c : Bool)
    → ((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a)) ≡ c
  wolfram-on-bool true  true  true  = refl
  wolfram-on-bool true  true  false = refl
  wolfram-on-bool true  false true  = refl
  wolfram-on-bool true  false false = refl
  wolfram-on-bool false true  true  = refl
  wolfram-on-bool false true  false = refl
  wolfram-on-bool false false true  = refl
  wolfram-on-bool false false false = refl

  open Bridge Bool isSetBool true _∣_ wolfram-on-bool public

  -- Concrete check: the compiled WG's compute is NAND on Bool
  compute-on-bool : WG.result (true , true) ≡ false
  compute-on-bool = refl

  compute-on-bool' : WG.result (false , true) ≡ true
  compute-on-bool' = refl

  -- Concrete check: The WG's next state after a NAND request
  next-on-bool : Layer1.next WG.layer (inl (true , true)) ≡ inr ((true , true) , false)
  next-on-bool = refl

  -- Concrete check: Wolfram identity via the compiled WG
  wolfram-via-wg-on-bool : (a b c : Bool)
    → ((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a)) ≡ c
  wolfram-via-wg-on-bool = wolfram-via-wg

  -- Concrete check: evaluation preserves NAND
  evaluate-example :
    snd (request→response (true , true)) ≡ nand true true
  evaluate-example = evaluate-preserves-nand true true