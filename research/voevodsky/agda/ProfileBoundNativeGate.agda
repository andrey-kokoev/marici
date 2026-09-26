{-# OPTIONS --safe --cubical --guardedness #-}
module ProfileBoundNativeGate where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (true)
open import Cubical.Data.Int.Properties using (posNotnegsuc)
import RetainedLocalTidalOverlap as L
import ObservationRespectingBoundary as Q
import NewtonianTidalKernel as K
open L using (Sector; newtonian; rosen; Channel; electric-corner; electric-and-dxExx)
module G = L.G
module N = L.N

-- A closed application policy, not an inferred authorization from arbitrary
-- metadata. The coefficient slots already use the supplied aligned calibration.
Payload : Channel → Type
Payload electric-corner = K.Tensor
Payload electric-and-dxExx = L.Fine
profile : Channel → L.ObservationProfile
profile electric-corner = L.coarse-profile
profile electric-and-dxExx = L.fine-profile
node : (c : Channel) → Sector → G.Node (Payload c)
node c s = G.retain-node (G.atom-node L.Cited.SourcePacket) (L.Cited.packet s)
  (G.retain-node (G.atom-node L.ObservationProfile) (profile c) (G.atom-node (Payload c)))
value : (c : Channel) → Sector → Payload c
value electric-corner = L.native-reading
value electric-and-dxExx = L.fine-reading
package : Channel → Sector → G.Package
package c s = (Payload c , node c s) , value c s
source-header : (c : Channel) (s : Sector) → G.header (node c s)
  ≡ G.retain-header L.Cited.SourcePacket (L.Cited.packet s) (Payload c)
source-header c s = refl
profile-header : (c : Channel) (s : Sector)
  → G.header (snd (G.child (node c s) (lift true)))
  ≡ G.retain-header L.ObservationProfile (profile c) (Payload c)
profile-header c s = refl
coarse-is-actual : (s : Sector) → package electric-corner s ≡ L.Cited.native-package s
coarse-is-actual s = refl
fine-is-actual : (s : Sector) → package electric-and-dxExx s ≡ G.encode-package (L.Cited.fine-package s)
fine-is-actual s = refl

-- Reader authorization covers all slots of the declared profile, not only the
-- marked sample. An electric-only view cannot be certified as the joint profile.
record Reader (c : Channel) : Type where
  constructor reader
  field
    run : Payload c → Payload c
    authorized : (x : Payload c) → run x ≡ x
canonical : (c : Channel) → Reader c
canonical c = reader (λ x → x) (λ x → refl)
record Gate (c : Channel) (s t : Sector) : Type where
  constructor gate
  field
    left right : Reader c
    comparison : Q.NativeObserved (package c s) (package c t) (Reader.run left) (Reader.run right)
normalize : {c : Channel} {s t : Sector} → Gate c s t
  → Q.NativeObserved (package c s) (package c t) (λ x → x) (λ x → x)
normalize (gate l r ((e , p) , h)) = (e , p) , λ x →
  sym (Reader.authorized r (equivFun e x)) ∙ h x ∙ Reader.authorized l x
coarse-admitted : Gate electric-corner newtonian rosen
coarse-admitted = gate (canonical _) (canonical _) Q.native-tidal
fine-rejected : Gate electric-and-dxExx newtonian rosen → ⊥
fine-rejected g = Q.no-joint (normalize g)

-- Any constant fine reader is excluded, not merely one specially chosen zero.
constant-rejected : (z : L.Fine) → ((x : L.Fine) → z ≡ x) → ⊥
constant-rejected z h = posNotnegsuc 0 143
  (cong snd (sym (h (L.fine-reading rosen)) ∙ h (L.fine-reading newtonian)))

rule : {c : Channel} {s t : Sector} → Gate c s t → N.Rule
rule {c} {s} {t} g = Q.native-rule
  {a = package c s} {b = package c t} {r = λ x → x} {s = λ x → x} (normalize g)
retained : {c : Channel} {s t : Sector} → Gate c s t → G.Package
retained {c} {s} {t} g = N.remember (N.output (rule {c} {s} {t} g))
  (N.pack (G.atom-node (Gate c s t)) g)
recovered : {c : Channel} {s t : Sector} (g : Gate c s t)
  → snd (retained {c} {s} {t} g) ≡ g
recovered g = refl

-- Gate closure uses canonicalized certificates, so independently presented
-- readers cannot introduce a mismatch at the intermediate object.
identity : (c : Channel) (s : Sector) → Gate c s s
identity c s = gate (canonical c) (canonical c) (Q.native-identity (package c s) (λ x → x))
inverse : {c : Channel} {s t : Sector} → Gate c s t → Gate c t s
inverse {c} {s} {t} g = gate (canonical c) (canonical c)
  (Q.native-inverse {a = package c s} {b = package c t} {r = λ x → x} {s = λ x → x} (normalize g))
compose : {c : Channel} {s t u : Sector} → Gate c s t → Gate c t u → Gate c s u
compose {c} {s} {t} {u} g h = gate (canonical c) (canonical c)
  (Q.native-compose {a = package c s} {b = package c t} {c = package c u}
    {r = λ x → x} {s = λ x → x} {t = λ x → x} (normalize g) (normalize h))
