{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessContinuationHistories where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (rUnit; lUnit)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Bool.Base using (true; false)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Empty using (⊥)
open import NativeExtensionFamilyAudit using (Vertex; Edge; A; B; D; Seeds; sigmaEquiv)
open import SourceIndexedExtensionFamilies using (Out)
open import InternalSourceComparisons
import InternalComparisonInterchange as Native
import SourceIndexedContinuationAdapter as Adapter
import CertifiedContinuationPolicies as Certified
import ForwardCertifiedPrograms as Producer
import ContinuationPolicyFamily as Policy
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- Exact source continuation domain: ALL Out edges. No endpoint filter,
-- reversibility guard, or freshly selected comparison at the next step.
data History : Vertex → Vertex → Type where
  done : {v : Vertex} → History v v
  next : {v t : Vertex} (o : Out v) → History (fst o) t → History v t

_++_ : {u v t : Vertex} → History u v → History v t → History u t
done ++ k = k
next o h ++ k = next o (h ++ k)

history-assoc : {u v t z : Vertex} (h : History u v) (k : History v t) (l : History t z)
  → (h ++ k) ++ l ≡ h ++ (k ++ l)
history-assoc done k l = refl
history-assoc (next o h) k l = cong (next o) (history-assoc h k l)

mapHistory : (m : Mode) {v t : Vertex} → History v t → History (act m v) (act m t)
mapHistory m done = done
mapHistory m (next o h) = next (edgeMap m o) (mapHistory m h)

runBody : {v t : Vertex} → History v t → Body v → Body t
runBody done a = a
runBody (next o h) a = runBody h (attach a o)

Carrier : {v : Vertex} → Body v → Type
Carrier a = El (expression (package a))
point : {v : Vertex} (a : Body v) → Carrier a
point a = value (package a)
Filler : (m : Mode) {v : Vertex} → Body v → Body (act m v) → Type
Filler m a b = Σ (Carrier a ≃ Carrier b) (λ e →
  (equivFun e (point a) ≡ point b) × ((x : Carrier a) → act m (reader a x) ≡ reader b (equivFun e x)))

record State (m : Mode) (v : Vertex) : Type₁ where
  constructor cell
  field
    left : Body v
    right : Body (act m v)
    selected : Filler m left right
open State

witness : {m : Mode} {v : Vertex} → State m v → Body (act m v)
witness {m} (cell a b (e , p , h)) = compare m a b e p h

module Local {m : Mode} {v : Vertex} (s : State m v) where
  module Law = Native.Interchange m v (left s) (right s)
    (fst (selected s)) (fst (snd (selected s))) (snd (snd (selected s)))
  advance : (o : Out v) → State m (fst o)
  advance o = cell (attach (left s) o) (attach (right s) (edgeMap m o))
    (Law.attachmentEquiv o , Law.attachmentPoint o , Law.attachmentPorts o)
  square : (o : Out v) → Filler stay (witness (advance o)) (attach (witness s) (edgeMap m o))
  square o = Law.interchangeEquiv o , Law.interchangePoint o , Law.interchangePorts o
  native-square : (o : Out v) → Resolve Seeds (package (Law.interchange o))
  native-square o = derivation (Law.interchange o)

-- Derived recursively from the SAME selected input. The only recursive
-- input is a source edge, never an independent comparison witness.
extend : {m : Mode} {v t : Vertex} (h : History v t) (a : Body v) (b : Body (act m v))
  → Filler m a b → Filler m (runBody h a) (runBody (mapHistory m h) b)
extend done a b f = f
extend {m} (next o h) a b f = extend h (attach a o) (attach b (edgeMap m o))
  (selected (Local.advance (cell {m = m} a b f) o))

run : {m : Mode} {v t : Vertex} → History v t → State m v → State m t
run {m} h (cell a b f) = cell (runBody h a) (runBody (mapHistory m h) b) (extend h a b f)

extendSame : {v t : Vertex} (h : History v t) (a b : Body v)
  → Filler stay a b → Filler stay (runBody h a) (runBody h b)
extendSame done a b f = f
extendSame (next o h) a b f = extendSame h (attach a o) (attach b o)
  (selected (Local.advance (cell {m = stay} a b f) o))
runSame : {v t : Vertex} → History v t → State stay v → State stay t
runSame h (cell a b f) = cell (runBody h a) (runBody h b) (extendSame h a b f)

composeFiller : {v : Vertex} {a b c : Body v}
  → Filler stay a b → Filler stay b c → Filler stay a c
composeFiller (e , p , h) (f , q , k) = compEquiv e f
  , (cong (equivFun f) p ∙ q) , (λ x → h x ∙ k (equivFun e x))

-- Whole finite interchange: compare after all attachments versus attach
-- after the original comparison. Both routes retain their actual bodies.
finiteSquare : {m : Mode} {v t : Vertex} (h : History v t) (s : State m v)
  → Filler stay (witness (run h s)) (runBody (mapHistory m h) (witness s))
finiteSquare done s = idEquiv _ , refl , (λ x → refl)
finiteSquare {m} (next o h) s = composeFiller
  {a = witness (run h (Local.advance s o))}
  {b = runBody (mapHistory m h) (witness (Local.advance s o))}
  {c = runBody (mapHistory m h) (attach (witness s) (edgeMap m o))}
  (finiteSquare h (Local.advance s o))
  (selected (runSame (mapHistory m h)
    (cell {m = stay} (witness (Local.advance s o)) (attach (witness s) (edgeMap m o)) (Local.square s o))))

squareState : {m : Mode} {v t : Vertex} (h : History v t) (s : State m v) → State stay (act m t)
squareState {m} h s = cell (witness (run h s)) (runBody (mapHistory m h) (witness s)) (finiteSquare h s)
finite-native : {m : Mode} {v t : Vertex} (h : History v t) (s : State m v)
  → Resolve Seeds (package (witness (squareState h s)))
finite-native h s = derivation (witness (squareState h s))

-- The constructed native comparison is itself a valid selected input for
-- the next arbitrary history. This is NOT admission of a reified higher atom.
recursively-reusable : {m : Mode} {u v t : Vertex} (h : History u v) (s : State m u)
  (k : History (act m v) t)
  → Resolve Seeds (package (witness (squareState k (squareState h s))))
recursively-reusable h s k = finite-native k (squareState h s)

-- Direct evaluation and staged evaluation agree as COMPLETE states,
-- including their selected fillers and the original Body derivations.
run-append : {m : Mode} {u v t : Vertex} (h : History u v) (k : History v t) (s : State m u)
  → run (h ++ k) s ≡ run k (run h s)
run-append done k s = refl
run-append (next o h) k s = run-append h k (Local.advance s o)

map-append : (m : Mode) {u v t : Vertex} (h : History u v) (k : History v t)
  → mapHistory m (h ++ k) ≡ mapHistory m h ++ mapHistory m k
map-append m done k = refl
map-append m (next o h) k = cong (next (edgeMap m o)) (map-append m h k)
body-append : {u v t : Vertex} (h : History u v) (k : History v t) (a : Body u)
  → runBody (h ++ k) a ≡ runBody k (runBody h a)
body-append done k a = refl
body-append (next o h) k a = body-append h k (attach a o)

-- An actual staged COMPLETE interchange filler, not an independently
-- selected replacement. Transport aligns complete endpoint presentations.
stagedSquare : {m : Mode} {u v t : Vertex} (h : History u v) (k : History v t) (s : State m u)
  → Filler stay (witness (run (h ++ k) s)) (runBody (mapHistory m (h ++ k)) (witness s))
stagedSquare {m} h k s = transport
  (λ i → Filler stay (lp (~ i)) (rp (~ i)))
  (composeFiller {a = witness (run k (run h s))}
    {b = runBody (mapHistory m k) (witness (run h s))}
    {c = runBody (mapHistory m k) (runBody (mapHistory m h) (witness s))}
    (finiteSquare k (run h s)) (selected (runSame (mapHistory m k) (squareState h s))))
  where
  lp = cong witness (run-append h k s)
  rp = cong (λ hs → runBody hs (witness s)) (map-append m h k)
    ∙ body-append (mapHistory m h) (mapHistory m k) (witness s)

-- Higher pasting of the constructed staging comparisons, without assuming
-- proof irrelevance of State, Code, arbitrary fillers, or Resolve.
paste-left : {m : Mode} {u v t z : Vertex} (h : History u v) (k : History v t) (l : History t z) (s : State m u)
  → run ((h ++ k) ++ l) s ≡ run l (run k (run h s))
paste-left h k l s = run-append (h ++ k) l s ∙ cong (run l) (run-append h k s)
paste-right : {m : Mode} {u v t z : Vertex} (h : History u v) (k : History v t) (l : History t z) (s : State m u)
  → run ((h ++ k) ++ l) s ≡ run l (run k (run h s))
paste-right h k l s = cong (λ hs → run hs s) (history-assoc h k l)
  ∙ (run-append h (k ++ l) s ∙ run-append k l (run h s))
higher-pasting : {m : Mode} {u v t z : Vertex} (h : History u v) (k : History v t) (l : History t z) (s : State m u)
  → paste-left h k l s ≡ paste-right h k l s
higher-pasting done k l s = sym (rUnit (run-append k l s)) ∙ lUnit (run-append k l s)
  ∙ cong (λ p → refl ∙ p) (lUnit (run-append k l s))
higher-pasting (next o h) k l s = higher-pasting h k l (Local.advance s o)

staged-native-history : {m : Mode} {u v t : Vertex} (h : History u v) (k : History v t) (s : State m u)
  → PathP (λ i → Resolve Seeds (package (witness (run-append h k s i))))
      (derivation (witness (run (h ++ k) s))) (derivation (witness (run k (run h s))))
staged-native-history h k s i = derivation (witness (run-append h k s i))

-- Actual native composition trees for the finite square's two legs.
closureOf : {v : Vertex} → Body v → Closure Seeds
closureOf a = package a , derivation a
pastingTree : {m : Mode} {v t : Vertex} (h : History v t) (s : State m v) → List (Closure Seeds)
pastingTree done s = closureOf (witness (squareState done s)) ∷ []
pastingTree {m} (next o h) s = closureOf (Local.Law.interchange s o)
  ∷ (compose-comparisons (package a) (package b) (package c) e f p q
      , apply (compose-rule (package a) (package b) (package c) e f p q)
        (λ { (lift true) → derivation (witness rec) ; (lift false) → derivation (witness lifted) }))
  ∷ pastingTree h (Local.advance s o)
  where
  rec = squareState h (Local.advance s o)
  lifted = runSame (mapHistory m h)
    (cell {m = stay} (witness (Local.advance s o)) (attach (witness s) (edgeMap m o)) (Local.square s o))
  a = left rec
  b = right rec
  c = right lifted
  e = fst (selected rec)
  p = fst (snd (selected rec))
  f = fst (selected lifted)
  q = fst (snd (selected lifted))

-- Opposite PRESENTATION uses the existing inverse-comparison rule. It does
-- not reverse an attachment edge or manufacture reverse execution dynamics.
opposite-native : {v : Vertex} (s : State stay v) → Resolve Seeds
  (inverse-comparison (package (left s)) (package (right s))
    (fst (selected s)) (fst (snd (selected s))))
opposite-native s = apply (inverse-rule (package (left s)) (package (right s))
  (fst (selected s)) (fst (snd (selected s)))) (λ _ → derivation (witness s))
oppositeState : {v : Vertex} → State stay v → State stay v
oppositeState (cell a b (e , p , h)) = cell b a (invEquiv e
  , (sym (cong (invEq e) p) ∙ retEq e (point a))
  , (λ y → sym (h (invEq e y) ∙ cong (reader b) (secEq e y))))
opposite-retains-original : {v : Vertex} (s : State stay v)
  → inverse-comparison (package (left s)) (package (right s))
      (fst (selected s)) (fst (snd (selected s)))
    ≡ remember (package (witness s)) (package (witness (oppositeState s)))
opposite-retains-original (cell a b (e , p , h)) = refl
opposite-full-value : {v : Vertex} (s : State stay v) (x : Carrier (left s))
  → equivFun (fst (selected (oppositeState s))) (equivFun (fst (selected s)) x) ≡ x
opposite-full-value s = retEq (fst (selected s))
-- A reversed history QUERY retains the forward history as data; no function
-- returning History t v is asserted for h : History v t.
OppositeQuery : Vertex → Vertex → Type
OppositeQuery t v = History v t
reverse-query : {v t : Vertex} → History v t → OppositeQuery t v
reverse-query h = h
no-DA : Edge D A → ⊥
no-DA ()

-- A single concrete witness, quantified over every source-admitted history.
chosen : State exchange A
chosen = cell (seedBody A) (seedBody B) (sigmaEquiv , refl , (λ x → refl))
chosen-universal : {t : Vertex} (h : History A t)
  → Resolve Seeds (package (witness (squareState h chosen)))
chosen-universal h = finite-native h chosen

-- ALL requests of the existing source-indexed adapter, then ALL histories.
module Source = Adapter.Adapter exchange (seedBody A) (seedBody B) sigmaEquiv refl (λ x → refl)
sourceState : (r : Source.Request) → State stay (fst (Source.route r))
sourceState r = cell (Source.sourceBody r) (Source.targetBody r)
  (Source.attachmentEquiv r , Source.attachmentPoint r , Source.attachmentPorts r)
source-universal : (r : Source.Request) {t : Vertex} (h : History (fst (Source.route r)) t)
  → Resolve Seeds (package (witness (squareState h (sourceState r))))
source-universal r h = finite-native h (sourceState r)

-- No new producer policy: every presentation of the actual certified family.
module CertifiedFamily (m : Mode) {v : Vertex} (p : Producer.Program v) (q : Producer.Program (act m v))
  (ok : Producer.Pair.Guard m p q) where
  module C = Certified.Compiled m p q ok
  module F = C.R.F
  state : (control : C.Control) (k : Policy.Presentation)
    → State stay (fst (F.S.route (C.R.synchronize control)))
  state control k = cell (F.output r k) (F.output r Policy.target)
    (F.toTarget r k , F.point r k , F.ports r k)
    where r = C.R.synchronize control
  producer-native : (control : C.Control) (k : Policy.Presentation) → Closure Seeds
  producer-native control k = Certified.native (Certified.policyP m p q ok control k Certified.comparison)
  all-continuations : (control : C.Control) (k : Policy.Presentation) {t : Vertex}
    (h : History (fst (F.S.route (C.R.synchronize control))) t)
    → Resolve Seeds (package (witness (squareState h (state control k))))
  all-continuations control k h = finite-native h (state control k)

-- Reification retains the original history, not a quotient by its endpoints.
HistoryValue : Type₁
HistoryValue = Σ Vertex (λ v → Σ Vertex (λ t → Σ Mode (λ m → State m v × History v t)))
retainHistory : HistoryValue → Whole.Universe.Complete (ℓ-suc ℓ-zero)
retainHistory x = Whole.Universe.pack (Whole.Universe.atom HistoryValue) x
history-recovery : (x : HistoryValue) → Whole.Universe.value (retainHistory x) ≡ x
history-recovery x = refl
-- Formation/recovery here is NOT a Resolve claim for the reified atom.
