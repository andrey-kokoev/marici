{-# OPTIONS --safe --cubical --guardedness #-}
module SeedCompositionPortQuotient where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Data.Sigma.Base using (_×_)
import ActualSeedEndpointTable as Seed
import SeedSeamPathComparisonBoundary as Paths
import SeedFirstReturnActions as Actions
import SeedArrivalEffects as Arrival

open Seed using (Vertex; Occurrence; source; target)
open Paths using (Path; stop; step)

-- Match the existing ledger's POSITIVE path interface, including its source
-- and target indices. No identities are silently added to this carrier.
data Positive : Vertex → Vertex → Type where
  nonempty : {t : Vertex} (e : Occurrence) → Path (target e) t
    → Positive (source e) t

word : {s t : Vertex} → Positive s t → Path s t
word (nonempty e rest) = step e rest

join : {s m t : Vertex} → Positive s m → Positive m t → Positive s t
join (nonempty e rest) q = nonempty e (Actions.append rest (word q))

join-word : {s m t : Vertex} (p : Positive s m) (q : Positive m t)
  → word (join p q) ≡ Actions.append (word p) (word q)
join-word (nonempty e rest) q = refl

-- The source index is retained even though the active arrival lives at t.
-- Dropping that source index produces the old insufficient binary interface.
Port : Vertex → Vertex → Type
Port s t = Arrival.Arrival t

read : {s t : Vertex} → Positive s t → Port s t
read (nonempty e rest) = Arrival.Read.run rest (e , refl)

run-positive : {s t : Vertex} (p : Positive s t) (initial : Arrival.Arrival s)
  → Arrival.Read.run (word p) initial ≡ read p
run-positive (nonempty e rest) initial = refl

port-join : {s m t : Vertex} → Port s m → Port m t → Port s t
port-join left right = right

-- For known matching indices this is a right projection. The required
-- middle vertex is NOT optional data when assembling total port records.
composition-square : {s m t : Vertex} (p : Positive s m) (q : Positive m t)
  → read (join p q) ≡ port-join {s} {m} {t} (read p) (read q)
composition-square (nonempty e rest) q =
  Arrival.Read.run-append rest (word q) (e , refl)
    ∙ run-positive q (Arrival.Read.run rest (e , refl))

binary-congruence : {s m t : Vertex} (p p' : Positive s m) (q q' : Positive m t)
  → read p ≡ read p' → read q ≡ read q'
  → read (join p q) ≡ read (join p' q')
binary-congruence p p' q q' left-equal right-equal =
  composition-square p q ∙ right-equal ∙ sym (composition-square p' q')

port-associative : {a b c d : Vertex} (p : Port a b) (q : Port b c) (r : Port c d)
  → port-join {a} {c} {d} (port-join {a} {b} {c} p q) r
    ≡ port-join {a} {b} {d} p (port-join {b} {c} {d} q r)
port-associative p q r = refl

-- Contexts may have empty prefixes/suffixes. The observed middle path is
-- positive, so it initializes its own arrival without an external choice.
context-reading : {a s t b : Vertex} (prefix : Path a s) (p : Positive s t)
  (suffix : Path t b) (initial : Arrival.Arrival a) → Arrival.Arrival b
context-reading prefix p suffix initial = Arrival.Read.run
  (Actions.append prefix (Actions.append (word p) suffix)) initial

context-reduction : {a s t b : Vertex} (prefix : Path a s) (p : Positive s t)
  (suffix : Path t b) (initial : Arrival.Arrival a)
  → context-reading prefix p suffix initial ≡ Arrival.Read.run suffix (read p)
context-reduction prefix p suffix initial =
  Arrival.Read.run-append prefix (Actions.append (word p) suffix) initial
    ∙ Arrival.Read.run-append (word p) suffix (Arrival.Read.run prefix initial)
    ∙ cong (Arrival.Read.run suffix) (run-positive p (Arrival.Read.run prefix initial))

ContextEqual : {s t : Vertex} → Positive s t → Positive s t → Type
ContextEqual {s} {t} p q = (a b : Vertex) (prefix : Path a s)
  (suffix : Path t b) (initial : Arrival.Arrival a)
  → context-reading prefix p suffix initial ≡ context-reading prefix q suffix initial

current-to-context : {s t : Vertex} (p q : Positive s t)
  → read p ≡ read q → ContextEqual p q
current-to-context p q equal a b prefix suffix initial =
  context-reduction prefix p suffix initial
    ∙ cong (Arrival.Read.run suffix) equal
    ∙ sym (context-reduction prefix q suffix initial)

-- The actual seed has an arriving row at every vertex. These witnesses
-- are used only for the empty-context converse, not as a physical reset.
initial-at : (s : Vertex) → Arrival.Arrival s
initial-at Seed.A = Seed.CA , refl
initial-at Seed.B = Seed.AB , refl
initial-at Seed.C = Seed.BC , refl
initial-at Seed.D = Seed.AD , refl

context-to-current : {s t : Vertex} (p q : Positive s t)
  → ContextEqual p q → read p ≡ read q
context-to-current {s} {t} p q equal =
  sym (context-reduction stop p stop (initial-at s))
    ∙ equal s t stop stop (initial-at s)
    ∙ context-reduction stop q stop (initial-at s)

-- Total ports explicitly contain BOTH endpoint fields and the active row.
AllPorts : Type
AllPorts = Σ[ s ∈ Vertex ] Σ[ t ∈ Vertex ] Port s t

pack-port : {s t : Vertex} → Positive s t → AllPorts
pack-port {s} {t} p = s , t , read p

-- No coefficient averaging or physical readout is added here. Finite-family
-- summation/distributivity remains a separate rational algebra interface.
