{-# OPTIONS --safe --cubical --guardedness #-}
module RecursiveTableRuntime where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv-snd; Σ≡Prop)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Unit.Base using (Unit; tt)
import RecursiveConstructorTables as Tables
import WholePackageSigmaPi as Legacy
import WholePackageResolution as Resolution
import TableFibrationCycle as Table

-- Independent operations with retained input trees. Stored data contains no
-- old Code, Complete, Rule or Resolve. The old system is used by the decoder
-- and simulation proof only.
module Runtime (ℓ : Level)
  (Admit : Tables.Core.Package ℓ → Type (ℓ-suc ℓ)) where
  module G = Tables.Core ℓ
  data Run : Type (ℓ-suc ℓ) where
    literal : (g : G.Graph) (v : G.Value g) → Admit (g , v) → Run
    assemble-E : (I : Type ℓ) → (I → Run) → I → Run
    assemble-P : (I : Type ℓ) → (I → Run) → Run
  code : Run → G.Graph
  code (literal g v a) = g
  code (assemble-E I inputs i) = G.E-table I (λ j → code (inputs j))
  code (assemble-P I inputs) = G.P-table I (λ i → code (inputs i))
  selected : (r : Run) → G.Value (code r)
  selected (literal g v a) = v
  selected (assemble-E I inputs i) = i , selected (inputs i)
  selected (assemble-P I inputs) = λ i → selected (inputs i)

  -- Three-column row schema for retained executions. Input rows contain
  -- recursive Run tables, not just their resulting values.
  data Declaration : Type (ℓ-suc ℓ) where
    literal-declaration : (g : G.Graph) (v : G.Value g) → Admit (g , v) → Declaration
    E-declaration : (I : Type ℓ) → I → Declaration
    P-declaration : Type ℓ → Declaration
  declaration : Run → Declaration
  declaration (literal g v a) = literal-declaration g v a
  declaration (assemble-E I inputs i) = E-declaration I i
  declaration (assemble-P I inputs) = P-declaration I
  Arity : Run → Type ℓ
  Arity (literal g v a) = Lift ⊥
  Arity (assemble-E I inputs i) = I
  Arity (assemble-P I inputs) = I
  input : (r : Run) → Arity r → Run
  input (literal g v a) (lift ())
  input (assemble-E I inputs i) j = inputs j
  input (assemble-P I inputs) i = inputs i
  data Port (I : Type ℓ) : Type ℓ where
    header : Port I
    argument : I → Port I
  data Label : Type (ℓ-suc ℓ) where
    declares : Declaration → Label
    nested : Run → Label
  record Row (r : Run) : Type (ℓ-suc ℓ) where
    constructor row
    field
      label : Label
      from : Lift {j = ℓ} Unit
      to : Port (Arity r)
  rows : (r : Run) → Port (Arity r) → Row r
  rows r header = row (declares (declaration r)) (lift tt) header
  rows r (argument i) = row (nested (input r i)) (lift tt) (argument i)
  all-inputs-retained : (I : Type ℓ) (F : I → Run) (i j : I)
    → Row.label (rows (assemble-E I F i) (argument j)) ≡ nested (F j)
  all-inputs-retained I F i j = refl

  kernel-table : (r : Run) → Table.Table Label (Lift {j = ℓ-suc ℓ} Unit)
    (Lift {j = ℓ-suc ℓ} (Port (Arity r)))
  kernel-table r = Table.table (Lift (Port (Arity r)))
    (λ { (lift p) → Row.label (rows r p) }) (λ _ → lift tt) (λ p → p)
  kernel-unique : (r : Run) → Table.UniqueEndpoints (kernel-table r)
  kernel-unique r p q from-eq to-eq = to-eq
  kernel-four-return : (r : Run) → Table.four (kernel-table r) ≡ kernel-table r
  kernel-four-return r = Table.four-path (kernel-table r)

  -- Legacy decoding reconstructs the actual retain wrappers. They are not
  -- stored as an opaque legacy expression in a table label.
  module O = Legacy.Universe ℓ
  module R = Resolution.Generators ℓ
  mutual
    old-code : Run → O.Code
    old-code (literal g v a) = G.decode g
    old-code (assemble-E I inputs i) = O.E I
      (λ j → O.retain (old-code (inputs j)) (old-selected (inputs j)) (old-code (inputs j)))
    old-code (assemble-P I inputs) = O.Pi I
      (λ i → O.retain (old-code (inputs i)) (old-selected (inputs i)) (old-code (inputs i)))
    old-selected : (r : Run) → O.El (old-code r)
    old-selected (literal g v a) = Iso.inv (equivToIso (G.value-equivalence g)) v
    old-selected (assemble-E I inputs i) = i , old-selected (inputs i)
    old-selected (assemble-P I inputs) = λ i → old-selected (inputs i)
  meaning : Run → O.Complete
  meaning r = O.pack (old-code r) (old-selected r)
  E-commutes : (I : Type ℓ) (F : I → Run) (i : I)
    → meaning (assemble-E I F i) ≡ O.E-package I (λ j → meaning (F j)) i
  E-commutes I F i = refl
  P-commutes : (I : Type ℓ) (F : I → Run)
    → meaning (assemble-P I F) ≡ O.Pi-package I (λ i → meaning (F i))
  P-commutes I F = refl
  type-equivalence : (r : Run) → O.El (old-code r) ≃ G.Value (code r)
  type-equivalence (literal g v a) = G.value-equivalence g
  type-equivalence (assemble-E I inputs i) = Σ-cong-equiv-snd (λ j → type-equivalence (inputs j))
  type-equivalence (assemble-P I inputs) = equivΠCod (λ i → type-equivalence (inputs i))
  selected-commutes : (r : Run) → equivFun (type-equivalence r) (old-selected r) ≡ selected r
  selected-commutes (literal g v a) = Iso.rightInv (equivToIso (G.value-equivalence g)) v
  selected-commutes (assemble-E I inputs i) = cong (λ v → i , v) (selected-commutes (inputs i))
  selected-commutes (assemble-P I inputs) = funExt (λ i → selected-commutes (inputs i))

  -- Source boundary: every literal carries an actual supplied Admit witness.
  -- No seed is inserted for an E/P result. Admit need not be a proposition:
  -- its actual witness is retained in both the row and the legacy derivation.
  data Seeds : O.Complete → Type (ℓ-suc ℓ) where
    given : (g : G.Graph) (v : G.Value g) (a : Admit (g , v)) → Seeds (meaning (literal g v a))
  derive : (r : Run) → R.Resolve Seeds (meaning r)
  derive (literal g v a) = R.seed (given g v a)
  derive (assemble-E I inputs i) = R.apply (R.E-rule I (λ j → meaning (inputs j)) i)
    (λ { (lift j) → derive (inputs j) })
  derive (assemble-P I inputs) = R.apply (R.Pi-rule I (λ i → meaning (inputs i)))
    (λ { (lift i) → derive (inputs i) })

  -- A precise legacy subtheory: these are exactly the seed/E/P schemas and
  -- boundaries, with all original input packages retained in their parameters.
  data EPDerivation : O.Complete → Type (ℓ-suc ℓ) where
    supplied : (g : G.Graph) (v : G.Value g) (a : Admit (g , v)) → EPDerivation (meaning (literal g v a))
    sum-step : (I : Type ℓ) (F : I → O.Complete) (i : I)
      → ((j : I) → EPDerivation (F j)) → EPDerivation (O.E-package I F i)
    product-step : (I : Type ℓ) (F : I → O.Complete)
      → ((i : I) → EPDerivation (F i)) → EPDerivation (O.Pi-package I F)
  forget : {q : O.Complete} → EPDerivation q → R.Resolve Seeds q
  forget (supplied g v a) = R.seed (given g v a)
  forget (sum-step I F i ds) = R.apply (R.E-rule I F i) (λ { (lift j) → forget (ds j) })
  forget (product-step I F ds) = R.apply (R.Pi-rule I F) (λ { (lift i) → forget (ds i) })
  Closed : Type (ℓ-suc ℓ)
  Closed = Σ O.Complete EPDerivation
  closed-E : (I : Type ℓ) → (I → Closed) → I → Closed
  closed-E I inputs i = O.E-package I (λ j → fst (inputs j)) i ,
    sum-step I (λ j → fst (inputs j)) i (λ j → snd (inputs j))
  closed-P : (I : Type ℓ) → (I → Closed) → Closed
  closed-P I inputs = O.Pi-package I (λ i → fst (inputs i)) ,
    product-step I (λ i → fst (inputs i)) (λ i → snd (inputs i))
  to-source : Run → Closed
  to-source (literal g v a) = meaning (literal g v a) , supplied g v a
  to-source (assemble-E I inputs i) = closed-E I (λ j → to-source (inputs j)) i
  to-source (assemble-P I inputs) = closed-P I (λ i → to-source (inputs i))
  from-derivation : {q : O.Complete} → EPDerivation q → Run
  from-derivation (supplied g v a) = literal g v a
  from-derivation (sum-step I F i ds) = assemble-E I (λ j → from-derivation (ds j)) i
  from-derivation (product-step I F ds) = assemble-P I (λ i → from-derivation (ds i))
  from-source : Closed → Run
  from-source (q , d) = from-derivation d
  source-roundtrip : {q : O.Complete} (d : EPDerivation q)
    → to-source (from-derivation d) ≡ (q , d)
  source-roundtrip (supplied g v a) = refl
  source-roundtrip (sum-step I F i ds) =
    cong (λ children → closed-E I children i) (funExt (λ j → source-roundtrip (ds j)))
  source-roundtrip (product-step I F ds) =
    cong (closed-P I) (funExt (λ i → source-roundtrip (ds i)))
  run-roundtrip : (r : Run) → from-source (to-source r) ≡ r
  run-roundtrip (literal g v a) = refl
  run-roundtrip (assemble-E I inputs i) =
    cong (λ children → assemble-E I children i) (funExt (λ j → run-roundtrip (inputs j)))
  run-roundtrip (assemble-P I inputs) =
    cong (assemble-P I) (funExt (λ i → run-roundtrip (inputs i)))
  runtime-iso : Iso Closed Run
  Iso.fun runtime-iso = from-source
  Iso.inv runtime-iso = to-source
  Iso.leftInv runtime-iso (q , d) = source-roundtrip d
  Iso.rightInv runtime-iso = run-roundtrip

  -- Relate the restricted syntax to the ACTUAL imported Resolve datatype,
  -- not just to a newly declared source copy.
  data OnlyEP : {q : O.Complete} → R.Resolve Seeds q → Type (ℓ-suc ℓ) where
    seed-only : {q : O.Complete} {s : Seeds q} → OnlyEP (R.seed s)
    E-only : {I : Type ℓ} {F : I → O.Complete} {i : I}
      {ds : (j : R.Arity (R.E-rule I F i)) → R.Resolve Seeds (R.input (R.E-rule I F i) j)}
      → ((j : I) → OnlyEP (ds (lift j))) → OnlyEP (R.apply (R.E-rule I F i) ds)
    P-only : {I : Type ℓ} {F : I → O.Complete}
      {ds : (j : R.Arity (R.Pi-rule I F)) → R.Resolve Seeds (R.input (R.Pi-rule I F) j)}
      → ((j : I) → OnlyEP (ds (lift j))) → OnlyEP (R.apply (R.Pi-rule I F) ds)
  only-prop : {q : O.Complete} (d : R.Resolve Seeds q) → isProp (OnlyEP d)
  only-prop (R.seed s) seed-only seed-only = refl
  only-prop (R.apply (R.E-rule I F i) ds) (E-only p) (E-only q) =
    cong E-only (funExt (λ j → only-prop (ds (lift j)) (p j) (q j)))
  only-prop (R.apply (R.Pi-rule I F) ds) (P-only p) (P-only q) =
    cong P-only (funExt (λ i → only-prop (ds (lift i)) (p i) (q i)))
  only-prop (R.apply (R.compare-rule _ _ _ _) ds) ()
  only-prop (R.apply (R.identity-rule _) ds) ()
  only-prop (R.apply (R.inverse-rule _ _ _ _) ds) ()
  only-prop (R.apply (R.compose-rule _ _ _ _ _ _ _) ds) ()
  only-prop (R.apply (R.higher-rule _ _ _ _ _ _) ds) ()
  only-prop (R.apply (R.reflexivity-rule _ _) ds) ()
  only-prop (R.apply (R.path-lift-rule _ _ _ _ _) ds) ()
  only-prop (R.apply (R.distribution-rule _ _ _ _) ds) ()
  only-prop (R.apply (R.E-congruence-rule _ _ _ _ _ _) ds) ()
  only-prop (R.apply (R.Pi-congruence-rule _ _ _ _ _) ds) ()
  forget-only : {q : O.Complete} (d : EPDerivation q) → OnlyEP (forget d)
  forget-only (supplied g v a) = seed-only
  forget-only (sum-step I F i ds) = E-only (λ j → forget-only (ds j))
  forget-only (product-step I F ds) = P-only (λ i → forget-only (ds i))
  parse : {q : O.Complete} {d : R.Resolve Seeds q} → OnlyEP d → EPDerivation q
  parse (seed-only {s = given g v a}) = supplied g v a
  parse (E-only {I} {F} {i} p) = sum-step I F i (λ j → parse (p j))
  parse (P-only {I} {F} p) = product-step I F (λ i → parse (p i))
  parse-forget : {q : O.Complete} (d : EPDerivation q) → parse (forget-only d) ≡ d
  parse-forget (supplied g v a) = refl
  parse-forget (sum-step I F i ds) = cong (sum-step I F i) (funExt (λ j → parse-forget (ds j)))
  parse-forget (product-step I F ds) = cong (product-step I F) (funExt (λ i → parse-forget (ds i)))
  forget-parse : {q : O.Complete} {d : R.Resolve Seeds q} (p : OnlyEP d) → forget (parse p) ≡ d
  forget-parse (seed-only {s = given g v a}) = refl
  forget-parse (E-only {I} {F} {i} p) =
    cong (R.apply (R.E-rule I F i)) (funExt (λ { (lift j) → forget-parse (p j) }))
  forget-parse (P-only {I} {F} p) =
    cong (R.apply (R.Pi-rule I F)) (funExt (λ { (lift i) → forget-parse (p i) }))
  ActualClosure : Type (ℓ-suc ℓ)
  ActualClosure = Σ O.Complete (λ q → Σ (R.Resolve Seeds q) OnlyEP)
  actual-iso : Iso Closed ActualClosure
  Iso.fun actual-iso (q , d) = q , forget d , forget-only d
  Iso.inv actual-iso (q , d , p) = q , parse p
  Iso.leftInv actual-iso (q , d) = cong (λ e → q , e) (parse-forget d)
  Iso.rightInv actual-iso (q , d , p) = cong (λ e → q , e) (Σ≡Prop only-prop (forget-parse p))
  actual-runtime-iso : Iso ActualClosure Run
  actual-runtime-iso = compIso (invIso actual-iso) runtime-iso
