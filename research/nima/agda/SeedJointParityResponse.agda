{-# OPTIONS --safe --cubical --guardedness #-}
module SeedJointParityResponse where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Foundations.Univalence using (uaβ)
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (notEquiv)
open import Cubical.Data.Sigma.Base using (_×_)
import ActualSeedEndpointTable as Seed
import SeedSeamPathComparisonBoundary as Paths
import SeedFirstReturnActions as Actions
import SeedFaceObstruction as ABProbe
import SeedGeometricResponseState as G
import SeedTetrahedronBridge as Geometry
import SeedTriangleJointContext as Joint

open Seed using (Vertex; Occurrence; AB; BC; CA; AD; DB; BA)
Point = Bool × Bool

-- These are the TWO EXISTING proof probes, now read together. Declaring
-- this observation task does not select it as a physical instrument.
read : {v : Vertex} → G.State v → Point
read p = subst ABProbe.Probe p false , subst G.ReturnProbe p false

first-step second-step : Occurrence → Bool → Bool
first-step AB b = not b
first-step BC b = b
first-step CA b = b
first-step AD b = b
first-step DB b = b
first-step BA b = b
second-step AB b = b
second-step BC b = b
second-step CA b = b
second-step AD b = b
second-step DB b = b
second-step BA b = not b

update : Occurrence → Point → Point
update e (a , b) = first-step e a , second-step e b

first-transport : (e : Occurrence) (b : Bool)
  → subst ABProbe.Probe (Geometry.edge e) b ≡ first-step e b
first-transport AB b = uaβ notEquiv b
first-transport BC b = transportRefl b
first-transport CA b = transportRefl b
first-transport AD b = transportRefl b
first-transport DB b = transportRefl b
first-transport BA b = transportRefl b

second-transport : (e : Occurrence) (b : Bool)
  → subst G.ReturnProbe (Geometry.edge e) b ≡ second-step e b
second-transport AB b = transportRefl b
second-transport BC b = transportRefl b
second-transport CA b = transportRefl b
second-transport AD b = transportRefl b
second-transport DB b = transportRefl b
second-transport BA b = uaβ notEquiv b

primitive-square : (e : Occurrence) (p : G.State (Seed.source e))
  → read (G.advance e p) ≡ update e (read p)
primitive-square e p i =
  (substComposite ABProbe.Probe p (Geometry.edge e) false
    ∙ first-transport e (subst ABProbe.Probe p false)) i ,
  (substComposite G.ReturnProbe p (Geometry.edge e) false
    ∙ second-transport e (subst G.ReturnProbe p false)) i

not-twice : (b : Bool) → not (not b) ≡ b
not-twice false = refl
not-twice true = refl

update-twice : (e : Occurrence) (p : Point) → update e (update e p) ≡ p
update-twice AB (a , b) i = not-twice a i , b
update-twice BC p = refl
update-twice CA p = refl
update-twice AD p = refl
update-twice DB p = refl
update-twice BA (a , b) i = a , not-twice b i

module Finite = Actions.Effects (λ _ → Point) update

route-square : {s t : Vertex} (p : Paths.Path s t) (h : G.State s)
  → read (G.Response.run p h) ≡ Finite.run p (read h)
route-square Paths.stop h = refl
route-square (Paths.step e rest) h = route-square rest (G.advance e h)
  ∙ cong (Finite.run rest) (primitive-square e h)

base-reading : read (refl {x = Geometry.node Seed.A}) ≡ (false , false)
base-reading i = transportRefl false i , transportRefl false i

-- The actual compiled output, not an independently evaluated model state.
native-square : {t : Vertex} (p : Paths.Path Seed.A t)
  → read (G.FromA.current (G.FromA.RetainedRun.native (G.FromA.run p)))
    ≡ Finite.run p (false , false)
native-square p = cong read (G.FromA.RetainedRun.effect-agrees (G.FromA.run p))
  ∙ route-square p refl ∙ cong (Finite.run p) base-reading

flag : Joint.Choice → Bool
flag Joint.direct = true
flag Joint.indirect = false

finite-corner : (x y : Joint.Choice)
  → Finite.run (Joint.all-pairs-execution (x , y)) (false , false) ≡ (flag x , flag y)
finite-corner Joint.direct Joint.direct = refl
finite-corner Joint.direct Joint.indirect = refl
finite-corner Joint.indirect Joint.direct = refl
finite-corner Joint.indirect Joint.indirect = refl

native-corner : (x y : Joint.Choice)
  → read (G.FromA.current (G.FromA.RetainedRun.native
      (G.FromA.run (Joint.all-pairs-execution (x , y))))) ≡ (flag x , flag y)
native-corner x y = native-square (Joint.all-pairs-execution (x , y)) ∙ finite-corner x y

choice : Bool → Joint.Choice
choice false = Joint.indirect
choice true = Joint.direct
choice-flag : (x : Joint.Choice) → choice (flag x) ≡ x
choice-flag Joint.direct = refl
choice-flag Joint.indirect = refl

decode : Point → Joint.Choice × Joint.Choice
decode (a , b) = choice a , choice b

-- All four corners can now be recovered, whereas arrival recovered only
-- the return choice on this product domain. This does not admit the product
-- as a replacement for the original two-row context relation.
corner-recovered : (x y : Joint.Choice)
  → decode (read (G.FromA.current (G.FromA.RetainedRun.native
      (G.FromA.run (Joint.all-pairs-execution (x , y)))))) ≡ (x , y)
corner-recovered x y = cong decode (native-corner x y)
  ∙ (λ i → choice-flag x i , choice-flag y i)

-- A concrete extra question, not a uniquely selected physical scalar.
both : Point → Bool
both (false , b) = false
both (true , b) = b

both-00 : both (Finite.run Actions.r00 (false , false)) ≡ true
both-00 = refl
both-01 : both (Finite.run Actions.r01 (false , false)) ≡ false
both-01 = refl
both-10 : both (Finite.run Actions.r10 (false , false)) ≡ false
both-10 = refl
both-11 : both (Finite.run Actions.r11 (false , false)) ≡ false
both-11 = refl

-- A finite observer remains coarser than raw histories. Geometric state and
-- directed execution provenance are still retained by G.FromA.run.
