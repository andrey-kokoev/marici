{-# OPTIONS --safe --cubical --guardedness #-}
module NativeTidalTableReadout where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Int.Base using (ℤ; pos; _+_; _-_; _·_)
open import Cubical.Data.Int.Properties using (0≢1-ℤ)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Sigma.Base using (_×_)
open import NewtonianTidalKernel using (Axis; x; y; z; Vec; Tensor; Source; mass; inverseCubeUnits; direction; delta)
open import NewtonianTidalFixture using (a; b; denominator)
import NewtonianTidalRoutes as Old
import NewtonianPotentialJet as OldJet
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
import TableFibrationCycle as Kernel
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

-- A declared exact second jet, in thirteen labelled scalar rows. This is
-- finite exact data, not a declaration of a continuum topology/completion.
data JetPort : Type where
  scalar : JetPort
  first : Axis → JetPort
  second : Axis → Axis → JetPort
JetTable : Type
JetTable = JetPort → ℤ
jet-table : JetTable → Kernel.Table ℤ Unit JetPort
jet-table f = Kernel.table JetPort f (λ _ → tt) (λ p → p)
jet-unique : (f : JetTable) → Kernel.UniqueEndpoints (jet-table f)
jet-unique f p q from-eq to-eq = to-eq

-- Independently defined arithmetic on those rows. Neither the old jet
-- evaluator nor any old-code decoder is called by this construction.
constant : ℤ → JetTable
constant c scalar = c
constant c (first i) = pos 0
constant c (second i j) = pos 0
add : JetTable → JetTable → JetTable
add f g p = f p + g p
scale : ℤ → JetTable → JetTable
scale c f p = c · f p
multiply : JetTable → JetTable → JetTable
multiply f g scalar = f scalar · g scalar
multiply f g (first i) = f (first i) · g scalar + f scalar · g (first i)
multiply f g (second i j) = f (second i j) · g scalar + f (first i) · g (first j)
  + f (first j) · g (first i) + f scalar · g (second i j)
coordinate : Axis → JetTable
coordinate i scalar = pos 0
coordinate i (first j) = delta i j
coordinate i (second j k) = pos 0
offset : Vec → Axis → JetTable
offset n i = add (coordinate i) (constant (pos 0 - n i))
distance-squared : Vec → JetTable
distance-squared n = add (multiply (offset n x) (offset n x))
  (add (multiply (offset n y) (offset n y)) (multiply (offset n z) (offset n z)))
t : Vec → JetTable
t n = add (distance-squared n) (constant (pos 0 - pos 1))
inverse-radius8 : Vec → JetTable
inverse-radius8 n = add (constant (pos 8))
  (add (scale (pos 0 - pos 4) (t n)) (scale (pos 3) (multiply (t n) (t n))))
source-jet : Source → JetTable
source-jet s = scale (pos 0 - mass s · inverseCubeUnits s) (inverse-radius8 (direction s))
read-tensor : JetTable → Tensor
read-tensor f i j = Kernel.Table.label (jet-table f) (second i j)
native-jet : JetTable
native-jet = add (source-jet a) (source-jet b)
native-tensor : Tensor
native-tensor = read-tensor native-jet
native-geometric : Tensor
native-geometric i j = pos 8 ·
  (mass a · inverseCubeUnits a · (delta i j - pos 3 · direction a i · direction a j)
    + mass b · inverseCubeUnits b · (delta i j - pos 3 · direction b i · direction b j))

-- Compare the independent thirteen-row calculation against the actual
-- polynomial route and the actual direct geometry in the same denominator.
ad-component : (i j : Axis) → native-tensor i j ≡ OldJet.potentialTotal8 a b i j
ad-component x x = refl
ad-component x y = refl
ad-component x z = refl
ad-component y x = refl
ad-component y y = refl
ad-component y z = refl
ad-component z x = refl
ad-component z y = refl
ad-component z z = refl
to-ad : native-tensor ≡ OldJet.potentialTotal8 a b
to-ad = funExt (λ i → funExt (ad-component i))
to-geometric : native-tensor ≡ Old.geometric8
to-geometric = to-ad ∙ Old.routeAgreement
geometric-commutes : native-geometric ≡ Old.geometric8
geometric-commutes = refl
route-node : Old.Route → G.Node Tensor
route-node r = G.retain-node (G.atom-node Old.Route) r
  (G.retain-node (G.atom-node (Source × Source)) (a , b)
    (G.retain-node (G.atom-node ℤ) (pos 8 · denominator) (G.atom-node Tensor)))
native-ad-package native-direct-package : G.Package
native-ad-package = N.pack (route-node Old.differentiated-potential) native-tensor
native-direct-package = N.pack (route-node Old.direct-geometry) native-geometric
ad-package-commutes : G.encode-package Old.adPackage ≡ native-ad-package
ad-package-commutes = cong (N.pack (route-node Old.differentiated-potential)) (sym to-ad)
direct-package-commutes : G.encode-package Old.directPackage ≡ native-direct-package
direct-package-commutes = refl
actual-comparison-commutes : G.encode-package (N.R.output Old.comparisonRule)
  ≡ N.output (N.encode-rule Old.comparisonRule)
actual-comparison-commutes = N.output-commutes Old.comparisonRule
module History = Resolution.ForOldSeeds ℓ-zero Old.Seeds
old-run : N.R.Closure Old.Seeds
old-run = N.O.Pi-package Bool Old.family , Old.history
translated-run : History.F.Closed
translated-run = equivFun History.closure-equivalence old-run
translated-endpoint : fst translated-run ≡ G.encode-package (fst old-run)
translated-endpoint = History.endpoint-commutes old-run
actual-history-recovered : invEq History.closure-equivalence translated-run ≡ old-run
actual-history-recovered = retEq History.closure-equivalence old-run

-- Hostile first-jet-only readout: exact agreement of scalar and gradient
-- does not determine the Hessian, even before considering any limiting norm.
FirstJet : Type
FirstJet = ℤ × Vec
first-jet : JetTable → FirstJet
first-jet f = Kernel.Table.label (jet-table f) scalar ,
  (λ i → Kernel.Table.label (jet-table f) (first i))
zero-jet bump-jet : JetTable
zero-jet = constant (pos 0)
bump-jet (second x x) = pos 1
bump-jet _ = pos 0
same-first-jet : first-jet zero-jet ≡ first-jet bump-jet
same-first-jet = refl
no-first-jet-factor : (f : FirstJet → Tensor)
  → ((j : JetTable) → f (first-jet j) ≡ read-tensor j) → ⊥
no-first-jet-factor f law = 0≢1-ℤ (cong (λ h → h x x)
  (sym (law zero-jet) ∙ cong f same-first-jet ∙ law bump-jet))
