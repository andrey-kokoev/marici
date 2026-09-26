{-# OPTIONS --safe --cubical --guardedness #-}
module RecursiveTableRegression where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Relation.Nullary.Base using (Stable)
import RecursiveConstructorTables as Tables
import RecursiveTableRuntime as Runtime
import NandConstructions as Nand
import QBooleanity as Boolean
module G = Tables.Core ℓ-zero
module Run = Runtime.Runtime ℓ-zero (λ _ → Lift {j = ℓ-suc ℓ-zero} Unit)

-- Built entirely by the NEW table constructors and interpreted without the
-- old decoder. The old system occurs only on the other side of the theorem.
pair-table : Type → Type → G.Graph
pair-table A B = G.E-table A (λ _ → G.atom-table B)
nand-table : Type → Type → G.Graph
nand-table A B = G.P-table (G.Value (pair-table A B)) (λ _ → G.atom-table ⊥)
TableN : Type → Type → Type
TableN A B = G.Value (nand-table A B)
constructor-commutes : (A B : Type) → G.decode (nand-table A B) ≡ Nand.nandCode A B
constructor-commutes A B = refl
operation-commutes : TableN ≡ Boolean.N
operation-commutes = refl
TableW : Type → Type → Type → Type
TableW A B C = TableN (TableN (TableN A B) C) (TableN A (TableN (TableN A C) A))
wolfram-double : (A B C : Type) → TableW A B C ≃ Boolean.D C
wolfram-double = Boolean.wolfram-double
wolfram-stable : (A B C : Type) → isProp C → Stable C → TableW A B C ≃ C
wolfram-stable = Boolean.wolfram-stable

-- A declaration row is present even when the node has no children.
empty-E empty-P : G.Graph
empty-E = G.E-table ⊥ (λ ())
empty-P = G.P-table ⊥ (λ ())
is-P : G.Graph → Bool
is-P (G.vertex (G.P-header I) children) = true
is-P _ = false
empty-constructions-distinct : empty-E ≡ empty-P → ⊥
empty-constructions-distinct p = false≢true (cong is-P p)
empty-E-uninhabited : G.Value empty-E → ⊥
empty-E-uninhabited (() , v)
empty-P-inhabited : G.Value empty-P
empty-P-inhabited = λ ()

-- Repeated E/P operations preserve the entire input trees, including values
-- in branches not selected by E.
bit : Bool → Run.Run
bit b = Run.literal (G.atom-table Bool) b (lift tt)
family : Bool → Run.Run
family b = bit b
choice : Run.Run
choice = Run.assemble-E Bool family false
product : Run.Run
product = Run.assemble-P Bool family
chosen-value : Run.selected choice ≡ (false , false)
chosen-value = refl
product-value : Run.selected product ≡ (λ b → b)
product-value = refl
unused-input-retained : Run.Row.label (Run.rows choice (Run.argument true)) ≡ Run.nested (bit true)
unused-input-retained = refl
choice-generated : Run.R.Resolve Run.Seeds (Run.meaning choice)
choice-generated = Run.derive choice
product-generated : Run.R.Resolve Run.Seeds (Run.meaning product)
product-generated = Run.derive product

-- No constructor-coverage promotion: ordinary maps codes are not in this
-- independent table grammar yet, even when their values are functions.
maps-still-unsupported : G.Supported (G.O.maps (G.O.atom Unit) (G.O.atom Unit)) → ⊥
maps-still-unsupported ()

-- Distinct supplied certificates remain distinct even at the same package.
module Certificates = Runtime.Runtime ℓ-zero (λ _ → Lift {j = ℓ-suc ℓ-zero} Bool)
certificate-zero certificate-one : Certificates.Run
certificate-zero = Certificates.literal (G.atom-table Unit) tt (lift false)
certificate-one = Certificates.literal (G.atom-table Unit) tt (lift true)
same-result : Certificates.meaning certificate-zero ≡ Certificates.meaning certificate-one
same-result = refl
certificate-bit : Certificates.Run → Bool
certificate-bit (Certificates.literal g v a) = lower a
certificate-bit _ = false
certificates-distinct : certificate-zero ≡ certificate-one → ⊥
certificates-distinct p = false≢true (cong certificate-bit p)

-- With an empty source policy there are no literal seeds. The zero-arity
-- Pi rule still constructs its result by an application, not a target seed.
module NoSeeds = Runtime.Runtime ℓ-zero (λ _ → Lift {j = ℓ-suc ℓ-zero} ⊥)
no-literal-seeds : {q : NoSeeds.O.Complete} → NoSeeds.Seeds q → ⊥
no-literal-seeds (NoSeeds.given g v (lift ()))
zero-P : NoSeeds.Run
zero-P = NoSeeds.assemble-P ⊥ (λ ())
zero-P-generated : NoSeeds.R.Resolve NoSeeds.Seeds (NoSeeds.meaning zero-P)
zero-P-generated = NoSeeds.derive zero-P
