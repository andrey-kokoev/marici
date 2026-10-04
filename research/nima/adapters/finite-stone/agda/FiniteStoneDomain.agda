{-# OPTIONS --safe --cubical --guardedness #-}
module FiniteStoneDomain where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using (isPropΠ; isProp×; isSet×)
open import Cubical.Data.Bool.Base using (Bool; false; true; not; _and_; _or_)
import Cubical.Data.Bool.Properties as BP
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Empty.Base using (⊥; rec)
open import Cubical.Data.Empty.Properties using (isProp⊥)
import BooleanNandEquivalence as Boolean

-- The domain is explicitly supplied, not synthesized by the native constructor.
A : Type
A = Bool × Bool
setA : isSet A
setA = isSet× BP.isSetBool BP.isSetBool
pairPath : {a b c d : Bool} → a ≡ b → c ≡ d → (a , c) ≡ (b , d)
pairPath p q i = p i , q i
zero one e₀ e₁ : A
zero = false , false
one = true , true
e₀ = true , false
e₁ = false , true
neg : A → A
neg (a , b) = not a , not b
meet join : A → A → A
meet (a , b) (c , d) = a and c , b and d
join (a , b) (c , d) = a or c , b or d

and-absorb : (a b : Bool) → a and (a or b) ≡ a
and-absorb false b = refl
and-absorb true b = refl
or-absorb : (a b : Bool) → a or (a and b) ≡ a
or-absorb false b = refl
or-absorb true b = refl
and-distrib : (a b c : Bool) → a and (b or c) ≡ (a and b) or (a and c)
and-distrib false b c = refl
and-distrib true b c = refl
or-distrib : (a b c : Bool) → a or (b and c) ≡ (a or b) and (a or c)
or-distrib false b c = refl
or-distrib true b c = refl
and-complement : (a : Bool) → a and not a ≡ false
and-complement false = refl
and-complement true = refl
or-complement : (a : Bool) → a or not a ≡ true
or-complement false = refl
or-complement true = refl

boolean : Boolean.BooleanStructure A
boolean = record
  { carrier-is-set = setA ; bottom = zero ; top = one ; neg = neg ; meet = meet ; join = join
  ; meet-comm = λ a b → pairPath (BP.and-comm (fst a) (fst b)) (BP.and-comm (snd a) (snd b))
  ; join-comm = λ a b → pairPath (BP.or-comm (fst a) (fst b)) (BP.or-comm (snd a) (snd b))
  ; meet-assoc = λ a b c → pairPath (sym (BP.and-assoc (fst a) (fst b) (fst c))) (sym (BP.and-assoc (snd a) (snd b) (snd c)))
  ; join-assoc = λ a b c → pairPath (sym (BP.or-assoc (fst a) (fst b) (fst c))) (sym (BP.or-assoc (snd a) (snd b) (snd c)))
  ; meet-idem = λ a → pairPath (BP.and-idem (fst a)) (BP.and-idem (snd a))
  ; join-idem = λ a → pairPath (BP.or-idem (fst a)) (BP.or-idem (snd a))
  ; meet-absorb = λ a b → pairPath (and-absorb (fst a) (fst b)) (and-absorb (snd a) (snd b))
  ; join-absorb = λ a b → pairPath (or-absorb (fst a) (fst b)) (or-absorb (snd a) (snd b))
  ; meet-distrib = λ a b c → pairPath (and-distrib (fst a) (fst b) (fst c)) (and-distrib (snd a) (snd b) (snd c))
  ; join-distrib = λ a b c → pairPath (or-distrib (fst a) (fst b) (fst c)) (or-distrib (snd a) (snd b) (snd c))
  ; meet-top = λ a → pairPath (BP.and-identityʳ (fst a)) (BP.and-identityʳ (snd a))
  ; join-bottom = λ a → pairPath (BP.or-identityʳ (fst a)) (BP.or-identityʳ (snd a))
  ; meet-complement = λ a → pairPath (and-complement (fst a)) (and-complement (snd a))
  ; join-complement = λ a → pairPath (or-complement (fst a)) (or-complement (snd a)) }

-- Actual order-theoretic atoms: nonzero, with no smaller nonzero element.
IsAtom : A → Type
IsAtom a = (a ≡ zero → ⊥) × ((b : A) → meet b a ≡ b → (b ≡ zero → ⊥) → b ≡ a)
atom-prop : (a : A) → isProp (IsAtom a)
atom-prop a = isProp× (isPropΠ (λ _ → isProp⊥))
  (isPropΠ (λ b → isPropΠ (λ _ → isPropΠ (λ _ → setA b a))))
Atom : Type
Atom = Σ A IsAtom
nonzero₀ : e₀ ≡ zero → ⊥
nonzero₀ p = BP.true≢false (cong fst p)
nonzero₁ : e₁ ≡ zero → ⊥
nonzero₁ p = BP.true≢false (cong snd p)
minimal₀ : (b : A) → meet b e₀ ≡ b → (b ≡ zero → ⊥) → b ≡ e₀
minimal₀ (false , false) p nz = rec (nz refl)
minimal₀ (false , true) p nz = rec (BP.false≢true (cong snd p))
minimal₀ (true , false) p nz = refl
minimal₀ (true , true) p nz = rec (BP.false≢true (cong snd p))
minimal₁ : (b : A) → meet b e₁ ≡ b → (b ≡ zero → ⊥) → b ≡ e₁
minimal₁ (false , false) p nz = rec (nz refl)
minimal₁ (false , true) p nz = refl
minimal₁ (true , false) p nz = rec (BP.false≢true (cong fst p))
minimal₁ (true , true) p nz = rec (BP.false≢true (cong fst p))
point : Bool → Atom
point false = e₀ , nonzero₀ , minimal₀
point true = e₁ , nonzero₁ , minimal₁
not-top-atom : IsAtom one → ⊥
not-top-atom p = BP.false≢true (cong snd (snd p e₀ refl nonzero₀))
locate : Atom → Bool
locate ((false , false) , nz , m) = rec (nz refl)
locate ((false , true) , p) = true
locate ((true , false) , p) = false
locate ((true , true) , p) = rec (not-top-atom p)
locate-point : (i : Bool) → locate (point i) ≡ i
locate-point false = refl
locate-point true = refl
point-locate : (a : Atom) → point (locate a) ≡ a
point-locate ((false , false) , nz , m) = rec (nz refl)
point-locate ((false , true) , p) = Σ≡Prop atom-prop refl
point-locate ((true , false) , p) = Σ≡Prop atom-prop refl
point-locate ((true , true) , p) = rec (not-top-atom p)
points-iso : Iso Bool Atom
points-iso = iso point locate point-locate locate-point

-- Boolean-valued subsets of the two-point space, and actual incidence with atoms.
P : Type
P = Bool → Bool
evaluate : A → P
evaluate a false = fst a
evaluate a true = snd a
assemble : P → A
assemble f = f false , f true
algebra-roundtrip : (a : A) → assemble (evaluate a) ≡ a
algebra-roundtrip a = refl
subset-roundtrip : (f : P) → evaluate (assemble f) ≡ f
subset-roundtrip f = funExt (λ { false → refl ; true → refl })
representation : Iso A P
representation = iso evaluate assemble subset-roundtrip algebra-roundtrip
incidence-to : (i : Bool) (a : A) → meet (fst (point i)) a ≡ fst (point i) → evaluate a i ≡ true
incidence-to false a p = cong fst p
incidence-to true a p = cong snd p
incidence-from : (i : Bool) (a : A) → evaluate a i ≡ true → meet (fst (point i)) a ≡ fst (point i)
incidence-from false a p = pairPath p refl
incidence-from true a p = pairPath refl p
represent : A → Atom → Bool
represent a p = evaluate a (locate p)
reconstruct : (Atom → Bool) → A
reconstruct u = u (point false) , u (point true)
represent-reconstruct : (u : Atom → Bool) → represent (reconstruct u) ≡ u
represent-reconstruct u = funExt (λ p → step (locate p) ∙ cong u (point-locate p))
  where
  step : (i : Bool) → evaluate (reconstruct u) i ≡ u (point i)
  step false = refl
  step true = refl
stone : Iso A (Atom → Bool)
stone = iso represent reconstruct represent-reconstruct (λ a → refl)

eval-zero : (i : Bool) → evaluate zero i ≡ false
eval-zero false = refl
eval-zero true = refl
eval-one : (i : Bool) → evaluate one i ≡ true
eval-one false = refl
eval-one true = refl
eval-neg : (a : A) (i : Bool) → evaluate (neg a) i ≡ not (evaluate a i)
eval-neg a false = refl
eval-neg a true = refl
eval-meet : (a b : A) (i : Bool) → evaluate (meet a b) i ≡ evaluate a i and evaluate b i
eval-meet a b false = refl
eval-meet a b true = refl
eval-join : (a b : A) (i : Bool) → evaluate (join a b) i ≡ evaluate a i or evaluate b i
eval-join a b false = refl
eval-join a b true = refl
-- The actual atom representation preserves every Boolean operation.
stone-zero : represent zero ≡ (λ _ → false)
stone-zero = funExt (λ p → eval-zero (locate p))
stone-one : represent one ≡ (λ _ → true)
stone-one = funExt (λ p → eval-one (locate p))
stone-neg : (a : A) → represent (neg a) ≡ (λ p → not (represent a p))
stone-neg a = funExt (λ p → eval-neg a (locate p))
stone-meet : (a b : A) → represent (meet a b) ≡ (λ p → represent a p and represent b p)
stone-meet a b = funExt (λ p → eval-meet a b (locate p))
stone-join : (a b : A) → represent (join a b) ≡ (λ p → represent a p or represent b p)
stone-join a b = funExt (λ p → eval-join a b (locate p))

record Preserves (h : A → A) : Type where
  field
    bottom : h zero ≡ zero
    top : h one ≡ one
    complement : (a : A) → h (neg a) ≡ neg (h a)
    intersection : (a b : A) → h (meet a b) ≡ meet (h a) (h b)
    union : (a b : A) → h (join a b) ≡ join (h a) (h b)
open Preserves
preserves-prop : (h : A → A) → isProp (Preserves h)
preserves-prop h p q i = record
  { bottom = setA _ _ (bottom p) (bottom q) i
  ; top = setA _ _ (top p) (top q) i
  ; complement = λ a → setA _ _ (complement p a) (complement q a) i
  ; intersection = λ a b → setA _ _ (intersection p a b) (intersection q a b) i
  ; union = λ a b → setA _ _ (union p a b) (union q a b) i }
Hom : Type
Hom = Σ (A → A) Preserves
pull : (Bool → Bool) → A → A
pull f a = assemble (λ i → evaluate a (f i))
eval-pull : (f : Bool → Bool) (a : A) (i : Bool) → evaluate (pull f a) i ≡ evaluate a (f i)
eval-pull f a false = refl
eval-pull f a true = refl
pull-preserves : (f : Bool → Bool) → Preserves (pull f)
pull-preserves f = record
  { bottom = pairPath (eval-zero (f false)) (eval-zero (f true))
  ; top = pairPath (eval-one (f false)) (eval-one (f true))
  ; complement = λ a → pairPath (eval-neg a (f false)) (eval-neg a (f true))
  ; intersection = λ a b → pairPath (eval-meet a b (f false)) (eval-meet a b (f true))
  ; union = λ a b → pairPath (eval-join a b (f false)) (eval-join a b (f true)) }
arrow : (Bool → Bool) → Hom
arrow f = pull f , pull-preserves f
select : Hom → Bool → Bool
select h i = not (evaluate (fst h e₀) i)
eval-e₀ : (i : Bool) → evaluate e₀ i ≡ not i
eval-e₀ false = refl
eval-e₀ true = refl
recover-e₀ : (a : A) → pull (λ i → not (evaluate a i)) e₀ ≡ a
recover-e₀ a = pairPath
  (eval-e₀ (not (fst a)) ∙ BP.notnot (fst a))
  (eval-e₀ (not (snd a)) ∙ BP.notnot (snd a))
recover-function : (h : Hom) → pull (select h) ≡ fst h
recover-function h = funExt step
  where
  step : (a : A) → pull (select h) a ≡ fst h a
  step (false , false) = bottom (pull-preserves (select h)) ∙ sym (bottom (snd h))
  step (false , true) = complement (pull-preserves (select h)) e₀
    ∙ cong neg (recover-e₀ (fst h e₀)) ∙ sym (complement (snd h) e₀)
  step (true , false) = recover-e₀ (fst h e₀)
  step (true , true) = top (pull-preserves (select h)) ∙ sym (top (snd h))
select-arrow : (f : Bool → Bool) → select (arrow f) ≡ f
select-arrow f = funExt (λ i → cong not (eval-pull f e₀ i ∙ eval-e₀ (f i)) ∙ BP.notnot (f i))
arrow-select : (h : Hom) → arrow (select h) ≡ h
arrow-select h = Σ≡Prop preserves-prop (recover-function h)
arrows-iso : Iso Hom (Bool → Bool)
arrows-iso = iso select arrow select-arrow arrow-select
pull-identity : (a : A) → pull (λ i → i) a ≡ a
pull-identity a = refl
pull-compose : (f g : Bool → Bool) (a : A)
  → pull (λ i → f (g i)) a ≡ pull g (pull f a)
pull-compose f g a = pairPath (sym (eval-pull f a (g false))) (sym (eval-pull f a (g true)))
naturality : (h : Hom) (a : A) (i : Bool)
  → evaluate (fst h a) i ≡ evaluate a (select h i)
naturality h a i = cong (λ k → evaluate (k a) i) (sym (recover-function h)) ∙ eval-pull (select h) a i
atom-map : Hom → Atom → Atom
atom-map h p = point (select h (locate p))
atom-naturality : (h : Hom) (a : A) (p : Atom)
  → represent (fst h a) p ≡ represent a (atom-map h p)
atom-naturality h a p = naturality h a (locate p)
  ∙ cong (evaluate a) (sym (locate-point (select h (locate p))))

identity-hom : Hom
identity-hom = (λ a → a) , record
  { bottom = refl ; top = refl ; complement = λ _ → refl
  ; intersection = λ _ _ → refl ; union = λ _ _ → refl }
compose-hom : Hom → Hom → Hom
compose-hom k h = (λ a → fst k (fst h a)) , record
  { bottom = cong (fst k) (bottom (snd h)) ∙ bottom (snd k)
  ; top = cong (fst k) (top (snd h)) ∙ top (snd k)
  ; complement = λ a → cong (fst k) (complement (snd h) a) ∙ complement (snd k) (fst h a)
  ; intersection = λ a b → cong (fst k) (intersection (snd h) a b) ∙ intersection (snd k) (fst h a) (fst h b)
  ; union = λ a b → cong (fst k) (union (snd h) a b) ∙ union (snd k) (fst h a) (fst h b) }
select-identity : select identity-hom ≡ (λ i → i)
select-identity = cong select (Σ≡Prop preserves-prop {u = identity-hom} {v = arrow (λ i → i)} refl)
  ∙ select-arrow (λ i → i)
select-compose : (k h : Hom) → select (compose-hom k h) ≡ (λ i → select h (select k i))
select-compose k h = cong select
  (Σ≡Prop preserves-prop {u = compose-hom k h} {v = arrow (λ i → select h (select k i))} recover)
  ∙ select-arrow (λ i → select h (select k i))
  where
  recover : fst (compose-hom k h) ≡ pull (λ i → select h (select k i))
  recover = funExt (λ a →
    cong (fst k) (sym (cong (λ f → f a) (recover-function h)))
    ∙ sym (cong (λ f → f (pull (select h) a)) (recover-function k))
    ∙ sym (pull-compose (select h) (select k) a))
atom-map-compose : (k h : Hom) (p : Atom)
  → atom-map (compose-hom k h) p ≡ atom-map h (atom-map k p)
atom-map-compose k h p = cong (λ f → point (f (locate p))) (select-compose k h)
  ∙ cong (λ i → point (select h i)) (sym (locate-point (select k (locate p))))

-- Symmetry is retained, not quotiented into cardinality or a selected atom.
swap : A → A
swap = pull not
swap-e₀ : swap e₀ ≡ e₁
swap-e₀ = refl
swap-not-identity : swap e₀ ≡ e₀ → ⊥
swap-not-identity p = BP.false≢true (cong fst p)
no-invariant-point : (i : Bool) → not i ≡ i → ⊥
no-invariant-point = BP.not≢const

-- This unordered readout records whether both/at least one coordinate is true.
profile : A → A
profile (a , b) = a and b , a or b
profile-collides : profile e₀ ≡ profile e₁
profile-collides = refl
no-profile-decoder : (d : A → A) → ((a : A) → d (profile a) ≡ a) → ⊥
no-profile-decoder d recover = BP.true≢false (cong fst
  (sym (recover e₀) ∙ cong d profile-collides ∙ recover e₁))
