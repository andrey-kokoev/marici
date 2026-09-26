{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedLocalTidalOverlap where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc; _+_; _-_; _·_)
open import Cubical.Data.Int.Properties using (posNotnegsuc)
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Tactics.CommRingSolver
open import Agda.Builtin.String using (String)
import NewtonianTidalKernel as K
import SourceAnchoredTidalOverlap as A
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import IndexedConstructorTables as Tables
import NativeTableResolution as Histories
import NativeTableRules as NativeRules
import BoundaryGeneratedQuestions as Boundary
module O = Whole.Universe ℓ-zero
module R = Resolution.Generators ℓ-zero
module G = Tables.Core ℓ-zero
module N = NativeRules.Native ℓ-zero

-- Different source declarations, not a claim that the laws are interderivable.
data Sector : Type where newtonian rosen : Sector
sector-bit : Sector → Bool
sector-bit newtonian = false
sector-bit rosen = true
Declaration : Sector → Type
Declaration newtonian = K.Source × K.Source
Declaration rosen = ℕ -- denominator of a in the declared cosh/cos wave family
selected-declaration : (s : Sector) → Declaration s
selected-declaration newtonian = A.source-x , A.source-z
selected-declaration rosen = 4

data LocalContext : Sector → Type where
  -- affine shifts are over the supplied jet denominator; Taylor bound N/D.
  newton-context : ℕ → ℤ → K.Vec → ℕ → ℕ → ℕ → LocalContext newtonian
  -- proper-clock square denominator, controlled u interval, epsilon=h^p,
  -- sigma=h^q. This is a limit route, not an equality for the frozen radar Y.
  wave-context : ℕ → ℤ → ℤ → ℕ → ℕ → LocalContext rosen
context : (s : Sector) → LocalContext s
context newtonian = newton-context 1728 (pos 7776) A.cancel-gradient 1 216 14641
context rosen = wave-context 2 (negsuc 0) (pos 2) 4 8

data Channel : Type where electric-corner electric-and-dxExx : Channel
data Frame : Type where fixed-nonrotating-xyz-at-corner : Frame
record ObservationProfile : Type where
  constructor profile
  field
    channel : Channel
    denominator : ℕ
    frame : Frame
coarse-profile fine-profile : ObservationProfile
coarse-profile = profile electric-corner 13824 fixed-nonrotating-xyz-at-corner
fine-profile = profile electric-and-dxExx 13824 fixed-nonrotating-xyz-at-corner

scale8 : K.Tensor → K.Tensor
scale8 t i j = pos 8 · t i j
source-reading : Sector → K.Tensor
source-reading newtonian = scale8 A.point-tensor
source-reading rosen = scale8 A.common
coarse-agreement : source-reading newtonian ≡ source-reading rosen
coarse-agreement = cong scale8 A.point-agrees

native-reading : Sector → K.Tensor
native-reading newtonian = A.native-tensor
native-reading rosen = scale8 A.common
source-native : (s : Sector) → source-reading s ≡ native-reading s
source-native newtonian = coarse-agreement ∙ sym A.native-agrees
source-native rosen = refl

Fine : Type
Fine = K.Tensor × ℤ
gradient-reading : Sector → ℤ
gradient-reading newtonian = negsuc 143 -- -1/96 over denominator 8*1728
gradient-reading rosen = pos 0
fine-reading : Sector → Fine
fine-reading s = source-reading s , gradient-reading s
no-gradient-factor : (f : K.Tensor → ℤ)
  → ((s : Sector) → f (source-reading s) ≡ gradient-reading s) → ⊥
no-gradient-factor f p = posNotnegsuc 0 143
  (sym (sym (p newtonian) ∙ cong f coarse-agreement ∙ p rosen))

-- The refined profile fixes the named channel's units and zero. Bare type
-- equivalence alone does not provide this physical compatibility condition.
record RespectfulRefinement : Type where
  field
    equivalence : Fine ≃ Fine
    preserves-electric : (v : Fine) → fst (equivFun equivalence v) ≡ fst v
    preserves-gradient : (v : Fine) → snd (equivFun equivalence v) ≡ snd v
    marked : equivFun equivalence (fine-reading newtonian) ≡ fine-reading rosen
no-respectful-refinement : RespectfulRefinement → ⊥
no-respectful-refinement r = posNotnegsuc 0 143 (sym
  (sym (RespectfulRefinement.preserves-gradient r (fine-reading newtonian))
   ∙ cong snd (RespectfulRefinement.marked r)))

-- A genuine hostile: an UNRESTRICTED equivalence can translate away the
-- difference, even while preserving the entire electric tensor projection.
shift : ℤ
shift = pos 144
undo-shift : (g c : ℤ) → (g + c) - c ≡ g
undo-shift g c = solve! ℤCommRing
redo-shift : (g c : ℤ) → (g - c) + c ≡ g
redo-shift g c = solve! ℤCommRing
shift-preserves-differences : (g h c : ℤ) → (g + c) - (h + c) ≡ g - h
shift-preserves-differences g h c = solve! ℤCommRing
loose-iso : Iso Fine Fine
Iso.fun loose-iso (e , g) = e , g + shift
Iso.inv loose-iso (e , g) = e , g - shift
Iso.rightInv loose-iso (e , g) i = e , redo-shift g shift i
Iso.leftInv loose-iso (e , g) i = e , undo-shift g shift i
loose-equivalence : Fine ≃ Fine
loose-equivalence = isoToEquiv loose-iso
loose-marked : equivFun loose-equivalence (fine-reading newtonian) ≡ fine-reading rosen
loose-marked i = coarse-agreement i , pos 0
loose-keeps-electric : (v : Fine) → fst (equivFun loose-equivalence v) ≡ fst v
loose-keeps-electric v = refl
loose-does-not-keep-gradient :
  ((v : Fine) → snd (equivFun loose-equivalence v) ≡ snd v) → ⊥
loose-does-not-keep-gradient h = posNotnegsuc 0 143 (h (fine-reading newtonian))

module WithEvidence
  (Admission : (s : Sector) → Declaration s → Type)
  (evidence : (s : Sector) → Admission s (selected-declaration s)) where

  SourcePacket : Type
  SourcePacket = Σ Sector (λ s → Σ (Declaration s) (λ d → Admission s d × LocalContext s))
  packet : Sector → SourcePacket
  packet s = s , selected-declaration s , evidence s , context s
  source-records-distinct : packet newtonian ≡ packet rosen → ⊥
  source-records-distinct p = false≢true (cong (λ q → sector-bit (fst q)) p)

  old-code : Sector → ObservationProfile → O.Code
  old-code s p = O.retain (O.atom SourcePacket) (packet s)
    (O.retain (O.atom ObservationProfile) p (O.atom K.Tensor))
  old-package : Sector → O.Complete
  old-package s = O.pack (old-code s coarse-profile) (source-reading s)
  native-node : Sector → G.Node K.Tensor
  native-node s = G.retain-node (G.atom-node SourcePacket) (packet s)
    (G.retain-node (G.atom-node ObservationProfile) coarse-profile (G.atom-node K.Tensor))
  native-package : Sector → G.Package
  native-package s = (K.Tensor , native-node s) , native-reading s
  native-package-comparison : (s : Sector) → G.encode-package (old-package s) ≡ native-package s
  native-package-comparison s i = (K.Tensor , native-node s) , source-native s i
  native-source-header : (s : Sector) → G.header (native-node s)
    ≡ G.retain-header SourcePacket (packet s) K.Tensor
  native-source-header s = refl
  native-profile-header : (s : Sector) → G.header (snd (G.child (native-node s) (lift true)))
    ≡ G.retain-header ObservationProfile coarse-profile K.Tensor
  native-profile-header s = refl

  -- Owner's actual boundary/filler and compare-rule, not a replacement API.
  coarse-filler : Boundary.Filler (old-package newtonian) (old-package rosen)
  coarse-filler = idEquiv K.Tensor , coarse-agreement
  comparison-rule : R.Rule
  comparison-rule = R.compare-rule (old-package newtonian) (old-package rosen)
    (fst coarse-filler) (snd coarse-filler)
  data Seeds : O.Complete → Type₁ where
    newton-seed : Seeds (old-package newtonian)
    rosen-seed : Seeds (old-package rosen)
  derivation : R.Resolve Seeds (R.output comparison-rule)
  derivation = R.apply comparison-rule λ { (lift true) → R.seed newton-seed ; (lift false) → R.seed rosen-seed }
  closure : R.Closure Seeds
  closure = R.output comparison-rule , derivation
  module H = Histories.ForOldSeeds ℓ-zero Seeds
  native-history : H.F.Closed
  native-history = equivFun H.closure-equivalence closure
  native-history-endpoint : fst native-history ≡ G.encode-package (fst closure)
  native-history-endpoint = H.endpoint-commutes closure
  history-retained : Iso.inv (equivToIso H.closure-equivalence) native-history ≡ closure
  history-retained = retEq H.closure-equivalence closure

  -- Also construct the native comparison directly from its actual independently
  -- calculated Newtonian rows. Only admission evidence is transported.
  selected-seed : (s : Sector) → Seeds (old-package s)
  selected-seed newtonian = newton-seed
  selected-seed rosen = rosen-seed
  native-admission : (s : Sector) → H.NativeSeeds (native-package s)
  native-admission s = subst H.NativeSeeds (native-package-comparison s)
    (equivFun (H.seed-equivalence (old-package s)) (selected-seed s))
  native-agreement : native-reading newtonian ≡ native-reading rosen
  native-agreement = sym (source-native newtonian) ∙ coarse-agreement ∙ source-native rosen
  actual-native-rule : N.Rule
  actual-native-rule = N.compare-kind , native-package newtonian , native-package rosen ,
    idEquiv K.Tensor , native-agreement
  actual-native-derivation : H.F.Resolve (N.output actual-native-rule)
  actual-native-derivation = H.F.apply actual-native-rule λ
    { (lift true) → H.F.seed (native-admission newtonian)
    ; (lift false) → H.F.seed (native-admission rosen) }
  actual-native-history : H.F.Closed
  actual-native-history = N.output actual-native-rule , actual-native-derivation
  actual-native-history-recovered : equivFun H.closure-equivalence
    (invEq H.closure-equivalence actual-native-history) ≡ actual-native-history
  actual-native-history-recovered = secEq H.closure-equivalence actual-native-history

  fine-package : Sector → O.Complete
  fine-package s = O.pack
    (O.retain (O.atom SourcePacket) (packet s)
      (O.retain (O.atom ObservationProfile) fine-profile (O.atom Fine)))
    (fine-reading s)
  unrestricted-fine-filler : Boundary.Filler (fine-package newtonian) (fine-package rosen)
  unrestricted-fine-filler = loose-equivalence , loose-marked

-- A concrete retained citation instance, not a postulate or a proof of real
-- analysis manufactured from a token. Analytic validity is supplied in the
-- referenced written derivations. The generic module also accepts stronger,
-- independently formalized admission evidence without changing the calculus.
record AnalyticReference : Type where
  constructor reference
  field artifact digest claim : String
reference-for : Sector → AnalyticReference
reference-for s = reference
  "research/voevodsky/source-anchored-tidal-overlap-is-local-and-stops-at-the-next-jet.md"
  "9e7fb956af22885ab81855b752c2f786af67dcd92ac6584908b14fee856cca80"
  (claim-for s)
  where
  claim-for : Sector → String
  claim-for newtonian = "Sections 2-5: Poisson source, affine frame, local bound, nonzero tidal gradient"
  claim-for rosen = "Sections 3,5,6: vacuum wave, proper clock, zero covariant tidal gradient, controlled radar limit"
CitedAdmission : (s : Sector) → Declaration s → Type
CitedAdmission s d = (d ≡ selected-declaration s) × AnalyticReference
cited-evidence : (s : Sector) → CitedAdmission s (selected-declaration s)
cited-evidence s = refl , reference-for s
module Cited = WithEvidence CitedAdmission cited-evidence
