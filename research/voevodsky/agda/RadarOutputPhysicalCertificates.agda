{-# OPTIONS --safe --cubical --guardedness #-}
module RadarOutputPhysicalCertificates where
open import Cubical.Foundations.Prelude
open import NativeRadarReadout using (before; center; after; x3; y4; xy5)
open import RadarClockAdmission using (Grid)
open import RadarClockPhysicalCertificates
open import RadarOutputEnclosure
wave-low-delay : Grid
wave-low-delay before x3 = 229216219097488326394394
wave-low-delay before y4 = 298610393623623481123266
wave-low-delay before xy5 = 376460182507988858840098
wave-low-delay center x3 = 230947656312783075370452
wave-low-delay center y4 = 296275075720032584430506
wave-low-delay center xy5 = 375674838767157068890976
wave-low-delay after x3 = 233134578790252478498300
wave-low-delay after y4 = 293368582782998670324400
wave-low-delay after xy5 = 374742697942973281053704
wave-high-delay : Grid
wave-high-delay before x3 = 229216219097489180550786
wave-high-delay before y4 = 298610393623624619998456
wave-high-delay before xy5 = 376460182507990448224820
wave-high-delay center x3 = 230947656312783987674814
wave-high-delay center y4 = 296275075720033756490496
wave-high-delay center xy5 = 375674838767158269613116
wave-high-delay after x3 = 233134578790253627550030
wave-high-delay after y4 = 293368582782999654551440
wave-high-delay after xy5 = 374742697942975000598036
wave-delays : DelayCertificate wave-certificate
low-delay wave-delays = wave-low-delay
high-delay wave-delays = wave-high-delay
lower-shift wave-delays before x3 = refl
lower-shift wave-delays before y4 = refl
lower-shift wave-delays before xy5 = refl
lower-shift wave-delays center x3 = refl
lower-shift wave-delays center y4 = refl
lower-shift wave-delays center xy5 = refl
lower-shift wave-delays after x3 = refl
lower-shift wave-delays after y4 = refl
lower-shift wave-delays after xy5 = refl
upper-shift wave-delays before x3 = refl
upper-shift wave-delays before y4 = refl
upper-shift wave-delays before xy5 = refl
upper-shift wave-delays center x3 = refl
upper-shift wave-delays center y4 = refl
upper-shift wave-delays center xy5 = refl
upper-shift wave-delays after x3 = refl
upper-shift wave-delays after y4 = refl
upper-shift wave-delays after xy5 = refl
moving-low-delay : Grid
moving-low-delay before x3 = 261025592308534898897974
moving-low-delay before y4 = 349971331792767185810396
moving-low-delay before xy5 = 439902434904726117949862
moving-low-delay center x3 = 271210996180068895078626
moving-low-delay center y4 = 363627461547103944504840
moving-low-delay center xy5 = 457067740129969064342020
moving-low-delay after x3 = 281396400051602891259280
moving-low-delay after y4 = 377283591301440703199286
moving-low-delay after xy5 = 474233045355212010734178
moving-high-delay : Grid
moving-high-delay before x3 = 261025592308534898897984
moving-high-delay before y4 = 349971331792767185810406
moving-high-delay before xy5 = 439902434904726117949872
moving-high-delay center x3 = 271210996180068895078638
moving-high-delay center y4 = 363627461547103944504850
moving-high-delay center xy5 = 457067740129969064342030
moving-high-delay after x3 = 281396400051602891259290
moving-high-delay after y4 = 377283591301440703199296
moving-high-delay after xy5 = 474233045355212010734188
moving-delays : DelayCertificate moving-certificate
low-delay moving-delays = moving-low-delay
high-delay moving-delays = moving-high-delay
lower-shift moving-delays before x3 = refl
lower-shift moving-delays before y4 = refl
lower-shift moving-delays before xy5 = refl
lower-shift moving-delays center x3 = refl
lower-shift moving-delays center y4 = refl
lower-shift moving-delays center xy5 = refl
lower-shift moving-delays after x3 = refl
lower-shift moving-delays after y4 = refl
lower-shift moving-delays after xy5 = refl
upper-shift moving-delays before x3 = refl
upper-shift moving-delays before y4 = refl
upper-shift moving-delays before xy5 = refl
upper-shift moving-delays center x3 = refl
upper-shift moving-delays center y4 = refl
upper-shift moving-delays center xy5 = refl
upper-shift moving-delays after x3 = refl
upper-shift moving-delays after y4 = refl
upper-shift moving-delays after xy5 = refl
