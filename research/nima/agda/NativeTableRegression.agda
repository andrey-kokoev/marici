{-# OPTIONS --safe --cubical --guardedness #-}
module NativeTableRegression where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Relation.Nullary.Base using (Stable)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
import NandConstructions as Nand
import QBooleanity as Boolean
import BoundaryGeneratedQuestions as Boundary
import NativeTidalTableReadout
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero
module Run = Resolution.Full ℓ-zero (λ _ → Lift {j = ℓ-suc ℓ-zero} Unit)

-- Independently constructed table NAND, not a call to the old constructor.
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

-- Comparison uses the imported actual marked-boundary filler space. Forward
-- carriers and selected values agree definitionally, so the whole filler
-- (including the supplied equivalence and compatibility path) is unchanged.
actual-filler-equivalence : (a b : G.O.Complete)
  → Boundary.Filler a b ≃ N.Filler (G.encode-package a) (G.encode-package b)
actual-filler-equivalence a b = idEquiv _
filler-composition-commutes : (a b c : G.O.Complete)
  (f : Boundary.Filler a b) (g : Boundary.Filler b c)
  → equivFun (actual-filler-equivalence a c) (Boundary.compose {a = a} {b = b} {c = c} f g)
    ≡ N.compose-filler {a = G.encode-package a} {b = G.encode-package b} {c = G.encode-package c}
      (equivFun (actual-filler-equivalence a b) f) (equivFun (actual-filler-equivalence b c) g)
filler-composition-commutes a b c f g = refl

-- All twelve independently defined rule schemas are exercised as actual
-- applications. The universal signature/closure equivalences are elsewhere;
-- these instances do not substitute for those proofs.
unit-graph : G.Graph
unit-graph = G.atom-table Unit
unit-package : G.Package
unit-package = unit-graph , tt
family : Unit → G.Package
family _ = unit-package
rules : N.Kind → N.Rule
rules N.E-kind = N.E-kind , Unit , family , tt
rules N.P-kind = N.P-kind , Unit , family
rules N.compare-kind = N.compare-kind , unit-package , unit-package , idEquiv Unit , refl
rules N.identity-kind = N.identity-kind , unit-package
rules N.inverse-kind = N.inverse-kind , unit-package , unit-package , idEquiv Unit , refl
rules N.compose-kind = N.compose-kind , unit-package , unit-package , unit-package , idEquiv Unit , idEquiv Unit , refl , refl
rules N.higher-kind = N.higher-kind , unit-graph , tt , tt , refl , refl , refl
rules N.reflexivity-kind = N.reflexivity-kind , unit-package
rules N.path-lift-kind = N.path-lift-kind , unit-graph , unit-graph , idEquiv Unit , tt , tt
rules N.distribution-kind = N.distribution-kind , Unit , (λ _ → Unit) , (λ _ _ → unit-package) , (λ _ → tt , tt)
rules N.E-congruence-kind = N.E-congruence-kind , Unit , family , family , ((λ _ → idEquiv Unit) , (λ _ → refl)) , tt
rules N.P-congruence-kind = N.P-congruence-kind , Unit , family , family , (λ _ → idEquiv Unit) , (λ _ → refl)
applications : (k : N.Kind) → Run.Resolve (N.output (rules k))
applications k = Run.apply (rules k) (λ i → Run.seed (lift tt))

-- All eight tags are now supported; equal value types do not erase the tag.
function-atom function-map : G.Graph
function-atom = G.atom-table (Unit → Unit)
function-map = (Unit → Unit) , G.maps-node (G.atom-node Unit) (G.atom-node Unit)
is-map : G.Graph → Bool
is-map (A , G.table-node (G.maps-header _ _) children) = true
is-map _ = false
constructors-distinct : function-atom ≡ function-map → ⊥
constructors-distinct p = false≢true (cong is-map p)

-- Distinct actual equivalences at the SAME marked boundary remain distinct.
BoolSquare : Type
BoolSquare = Bool × Bool
square : G.Package
square = G.atom-table BoolSquare , (false , false)
swap : Iso BoolSquare BoolSquare
Iso.fun swap (x , y) = y , x
Iso.inv swap (x , y) = y , x
Iso.leftInv swap (x , y) = refl
Iso.rightInv swap (x , y) = refl
filler-id filler-swap : N.Filler square square
filler-id = idEquiv BoolSquare , refl
filler-swap = isoToEquiv swap , refl
fillers-distinct : filler-id ≡ filler-swap → ⊥
fillers-distinct p = false≢true (cong (λ f → fst (equivFun (fst f) (false , true))) p)

-- Source certificates are retained as data, not merely checked for existence.
module Certificates = Resolution.Full ℓ-zero (λ _ → Lift {j = ℓ-suc ℓ-zero} Bool)
certificate-zero certificate-one : Certificates.Closed
certificate-zero = unit-package , Certificates.seed (lift false)
certificate-one = unit-package , Certificates.seed (lift true)
certificate-bit : Certificates.Closed → Bool
certificate-bit (q , Certificates.seed a) = lower a
certificate-bit (q , Certificates.apply r ds) = false
certificates-distinct : certificate-zero ≡ certificate-one → ⊥
certificates-distinct p = false≢true (cong certificate-bit p)

-- Empty-source operation: zero-arity P is generated without any target seed.
module NoSeeds = Resolution.Full ℓ-zero (λ _ → Lift {j = ℓ-suc ℓ-zero} ⊥)
zero-rule : N.Rule
zero-rule = N.P-kind , ⊥ , (λ ())
zero-generated : NoSeeds.Resolve (N.output zero-rule)
zero-generated = NoSeeds.apply zero-rule (λ { (lift ()) })
