{-# OPTIONS --safe --cubical --guardedness #-}
module NativeTableResolution where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import IndexedResolutionTransport as Transport
import TableFibrationCycle as Table
import WholePackageSigmaPi as Legacy
import WholePackageResolution as Resolution

module Full (ℓ : Level) (Admit : Tables.Core.Package ℓ → Type (ℓ-suc ℓ)) where
  module G = Tables.Core ℓ
  module N = Rules.Native ℓ

  -- The target derivation datatype is instantiated from NATIVE states,
  -- rules and operations. It is not Resolve of a decoded original endpoint.
  module Target = Transport.Theory G.Package N.Rule N.Arity N.input N.output Admit
  open Target public

  data Declaration : Type (ℓ-suc ℓ) where
    literal : (q : G.Package) → Admit q → Declaration
    application : N.Rule → Declaration
  declaration : Closed → Declaration
  declaration (q , seed a) = literal q a
  declaration (q , apply r ds) = application r
  Ports : Closed → Type (ℓ-suc ℓ)
  Ports (q , seed a) = Lift ⊥
  Ports (q , apply r ds) = N.Arity r
  premise : (d : Closed) → Ports d → Closed
  premise (q , seed a) (lift ())
  premise (q , apply r ds) i = N.input r i , ds i
  data Port (I : Type (ℓ-suc ℓ)) : Type (ℓ-suc ℓ) where
    header : Port I
    argument : I → Port I
  row-label : (d : Closed) → Port (Ports d) → Declaration ⊎ Closed
  row-label d header = inl (declaration d)
  row-label d (argument i) = inr (premise d i)
  kernel-table : (d : Closed) → Table.Table (Declaration ⊎ Closed)
    (Lift {j = ℓ-suc ℓ} Unit) (Port (Ports d))
  kernel-table d = Table.table (Port (Ports d)) (row-label d) (λ _ → lift tt) (λ p → p)
  kernel-unique : (d : Closed) → Table.UniqueEndpoints (kernel-table d)
  kernel-unique d p q from-eq to-eq = to-eq
  kernel-four-return : (d : Closed) → Table.four (kernel-table d) ≡ kernel-table d
  kernel-four-return d = Table.four-path (kernel-table d)

  -- Only the proof section below mentions the legacy closure.
  module O = N.O
  module R = N.R
  OldSeeds : O.Complete → Type (ℓ-suc ℓ)
  OldSeeds q = Admit (G.encode-package q)
  module Source = Transport.Theory O.Complete R.Rule R.Arity R.input R.output OldSeeds
  to-generic : {q : O.Complete} → R.Resolve OldSeeds q → Source.Resolve q
  to-generic (R.seed a) = Source.seed a
  to-generic (R.apply r ds) = Source.apply r (λ i → to-generic (ds i))
  from-generic : {q : O.Complete} → Source.Resolve q → R.Resolve OldSeeds q
  from-generic (Source.seed a) = R.seed a
  from-generic (Source.apply r ds) = R.apply r (λ i → from-generic (ds i))
  old-roundtrip : {q : O.Complete} (d : R.Resolve OldSeeds q) → from-generic (to-generic d) ≡ d
  old-roundtrip (R.seed a) = refl
  old-roundtrip (R.apply r ds) = cong (R.apply r) (funExt (λ i → old-roundtrip (ds i)))
  generic-roundtrip : {q : O.Complete} (d : Source.Resolve q) → to-generic (from-generic d) ≡ d
  generic-roundtrip (Source.seed a) = refl
  generic-roundtrip (Source.apply r ds) = cong (Source.apply r) (funExt (λ i → generic-roundtrip (ds i)))
  original-iso : Iso (R.Closure OldSeeds) Source.Closed
  Iso.fun original-iso (q , d) = q , to-generic d
  Iso.inv original-iso (q , d) = q , from-generic d
  Iso.leftInv original-iso (q , d) = cong (λ e → q , e) (old-roundtrip d)
  Iso.rightInv original-iso (q , d) = cong (λ e → q , e) (generic-roundtrip d)
  module T = Transport.Transfer G.Package N.Rule N.Arity N.input N.output Admit
  signature-transfer : T.Result O.Complete G.complete-equivalence R.Rule R.Arity R.input R.output OldSeeds
  signature-transfer = T.transport-theory G.complete-equivalence N.rule-equivalence
    R.Arity R.input R.output OldSeeds N.port-equivalence N.input-commutes N.output-commutes
    (λ q → idEquiv (Admit (G.encode-package q)))
  closure-equivalence : R.Closure OldSeeds ≃ Closed
  closure-equivalence = compEquiv (isoToEquiv original-iso) (fst signature-transfer)
  endpoint-commutes : (d : R.Closure OldSeeds)
    → fst (equivFun closure-equivalence d) ≡ G.encode-package (fst d)
  endpoint-commutes d = snd signature-transfer (Iso.fun original-iso d)
  closure-iso : Iso (R.Closure OldSeeds) Closed
  closure-iso = equivToIso closure-equivalence
  old-derivation-recovered : (d : R.Closure OldSeeds)
    → Iso.inv closure-iso (Iso.fun closure-iso d) ≡ d
  old-derivation-recovered = Iso.leftInv closure-iso
  native-derivation-recovered : (d : Closed)
    → Iso.fun closure-iso (Iso.inv closure-iso d) ≡ d
  native-derivation-recovered = Iso.rightInv closure-iso

-- Every original source policy is covered, not merely a policy invented for
-- the new syntax. Only its admission interface is transported; the native
-- operations and native Resolve datatype remain independently defined.
module ForOldSeeds (ℓ : Level)
  (S : Legacy.Universe.Complete ℓ → Type (ℓ-suc ℓ)) where
  module G = Tables.Core ℓ
  module O = Legacy.Universe ℓ
  module R = Resolution.Generators ℓ
  package-iso : Iso O.Complete G.Package
  package-iso = equivToIso G.complete-equivalence
  NativeSeeds : G.Package → Type (ℓ-suc ℓ)
  NativeSeeds q = S (Iso.inv package-iso q)
  module F = Full ℓ NativeSeeds
  seed-equivalence : (q : O.Complete) → S q ≃ F.OldSeeds q
  seed-equivalence q = pathToEquiv (cong S (sym (Iso.leftInv package-iso q)))
  forward : {q : O.Complete} → R.Resolve S q → R.Resolve F.OldSeeds q
  forward = R.mapSeeds (λ q → equivFun (seed-equivalence q))
  backward : {q : O.Complete} → R.Resolve F.OldSeeds q → R.Resolve S q
  backward = R.mapSeeds (λ q → invEq (seed-equivalence q))
  forward-backward : {q : O.Complete} (d : R.Resolve F.OldSeeds q) → forward (backward d) ≡ d
  forward-backward (R.seed {q} a) = cong R.seed (secEq (seed-equivalence q) a)
  forward-backward (R.apply r ds) = cong (R.apply r) (funExt (λ i → forward-backward (ds i)))
  backward-forward : {q : O.Complete} (d : R.Resolve S q) → backward (forward d) ≡ d
  backward-forward (R.seed {q} a) = cong R.seed (retEq (seed-equivalence q) a)
  backward-forward (R.apply r ds) = cong (R.apply r) (funExt (λ i → backward-forward (ds i)))
  policy-iso : Iso (R.Closure S) (R.Closure F.OldSeeds)
  Iso.fun policy-iso (q , d) = q , forward d
  Iso.inv policy-iso (q , d) = q , backward d
  Iso.leftInv policy-iso (q , d) = cong (λ e → q , e) (backward-forward d)
  Iso.rightInv policy-iso (q , d) = cong (λ e → q , e) (forward-backward d)
  closure-equivalence : R.Closure S ≃ F.Closed
  closure-equivalence = compEquiv (isoToEquiv policy-iso) F.closure-equivalence
  endpoint-commutes : (d : R.Closure S)
    → fst (equivFun closure-equivalence d) ≡ G.encode-package (fst d)
  endpoint-commutes d = F.endpoint-commutes (Iso.fun policy-iso d)
  readout-commutes : {ℓ' : Level} {X : Type ℓ'}
    (old-readout : O.Complete → X) (native-readout : G.Package → X)
    → ((q : O.Complete) → native-readout (G.encode-package q) ≡ old-readout q)
    → (d : R.Closure S)
    → native-readout (fst (equivFun closure-equivalence d)) ≡ old-readout (fst d)
  readout-commutes old-readout native-readout comparison d =
    cong native-readout (endpoint-commutes d) ∙ comparison (fst d)
