{-# OPTIONS --safe --cubical --guardedness #-}
module RadarClockPhysicalCertificates where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (_·_)
open import Cubical.Data.Int.Base using (pos)
open import NativeRadarReadout using (Rows; clocks; Time; before; center; after; Direction; x3; y4; xy5; frozen-calibration)
open import RadarClockAdmission
-- Generated arithmetic certificates only. Enclosure soundness for a real
-- null ray is NOT a theorem of this file. See the retained analytic receipt.
wave-arrival : Grid
wave-arrival before x3 = 1135910583808460634502222
wave-arrival before y4 = 1205304758334595931590493
wave-arrival before xy5 = 1283154547218961534562091
wave-arrival center x3 = 1439873475927412706228809
wave-arrival center y4 = 1505200895334662345166677
wave-arrival center xy5 = 1584600658381786843958222
wave-arrival after x3 = 1744291853308539521406885
wave-arrival after y4 = 1804525857301285630820640
wave-arrival after xy5 = 1885899972461260609208590
wave-lower : Grid
wave-lower before x3 = 1135910583808460207424026
wave-lower before y4 = 1205304758334595362152898
wave-lower before xy5 = 1283154547218960739869730
wave-lower center x3 = 1439873475927412250076628
wave-lower center y4 = 1505200895334661759136682
wave-lower center xy5 = 1584600658381786243597152
wave-lower after x3 = 1744291853308538946881020
wave-lower after y4 = 1804525857301285138707120
wave-lower after xy5 = 1885899972461259749436424
wave-upper : Grid
wave-upper before x3 = 1135910583808461061580418
wave-upper before y4 = 1205304758334596501028088
wave-upper before xy5 = 1283154547218962329254452
wave-upper center x3 = 1439873475927413162380990
wave-upper center y4 = 1505200895334662931196672
wave-upper center xy5 = 1584600658381787444319292
wave-upper after x3 = 1744291853308540095932750
wave-upper after y4 = 1804525857301286122934160
wave-upper after xy5 = 1885899972461261468980756
wave-below : Grid
wave-below before x3 = 427078196
wave-below before y4 = 569437595
wave-below before xy5 = 794692361
wave-below center x3 = 456152181
wave-below center y4 = 586029995
wave-below center xy5 = 600361070
wave-below after x3 = 574525865
wave-below after y4 = 492113520
wave-below after xy5 = 859772166
wave-above : Grid
wave-above before x3 = 427078196
wave-above before y4 = 569437595
wave-above before xy5 = 794692361
wave-above center x3 = 456152181
wave-above center y4 = 586029995
wave-above center xy5 = 600361070
wave-above after x3 = 574525865
wave-above after y4 = 492113520
wave-above after xy5 = 859772166
wave-width : Grid
wave-width before x3 = 854156392
wave-width before y4 = 1138875190
wave-width before xy5 = 1589384722
wave-width center x3 = 912304362
wave-width center y4 = 1172059990
wave-width center xy5 = 1200722140
wave-width after x3 = 1149051730
wave-width after y4 = 984227040
wave-width after xy5 = 1719544332
wave-delay : Grid
wave-delay before x3 = 229216219097488753472589
wave-delay before y4 = 298610393623624050560860
wave-delay before xy5 = 376460182507989653532458
wave-delay center x3 = 230947656312783531522632
wave-delay center y4 = 296275075720033170460500
wave-delay center xy5 = 375674838767157669252045
wave-delay after x3 = 233134578790253053024164
wave-delay after y4 = 293368582782999162437919
wave-delay after xy5 = 374742697942974140825869
wave-slack : Grid
wave-slack before x3 = 865387940
wave-slack before y4 = 580669142
wave-slack before xy5 = 130159610
wave-slack center x3 = 807239970
wave-slack center y4 = 547484342
wave-slack center xy5 = 518822192
wave-slack after x3 = 570492602
wave-slack after y4 = 735317292
wave-slack after xy5 = 0
wave-rows : Rows
wave-rows t d = clocks (pos (slot t · 302231454903657293676544)) (pos (wave-arrival t d))
wave-certificate : ClockCertificate 1208925819614629174706175 wave-rows
calibration wave-certificate = frozen-calibration
calibration-fixed wave-certificate = refl
quarter-ticks wave-certificate = 302231454903657293676544
denominator-grid wave-certificate = refl
arrival wave-certificate = wave-arrival
row-grid wave-certificate t d = refl
delay-minus-one wave-certificate = wave-delay
refinement wave-certificate = 0
lower wave-certificate = wave-lower
upper wave-certificate = wave-upper
below wave-certificate = wave-below
above wave-certificate = wave-above
width wave-certificate = wave-width
error-budget wave-certificate = 1719544332
slack wave-certificate = wave-slack
causal wave-certificate before x3 = refl
causal wave-certificate before y4 = refl
causal wave-certificate before xy5 = refl
causal wave-certificate center x3 = refl
causal wave-certificate center y4 = refl
causal wave-certificate center xy5 = refl
causal wave-certificate after x3 = refl
causal wave-certificate after y4 = refl
causal wave-certificate after xy5 = refl
inside-lower wave-certificate before x3 = refl
inside-lower wave-certificate before y4 = refl
inside-lower wave-certificate before xy5 = refl
inside-lower wave-certificate center x3 = refl
inside-lower wave-certificate center y4 = refl
inside-lower wave-certificate center xy5 = refl
inside-lower wave-certificate after x3 = refl
inside-lower wave-certificate after y4 = refl
inside-lower wave-certificate after xy5 = refl
inside-upper wave-certificate before x3 = refl
inside-upper wave-certificate before y4 = refl
inside-upper wave-certificate before xy5 = refl
inside-upper wave-certificate center x3 = refl
inside-upper wave-certificate center y4 = refl
inside-upper wave-certificate center xy5 = refl
inside-upper wave-certificate after x3 = refl
inside-upper wave-certificate after y4 = refl
inside-upper wave-certificate after xy5 = refl
width-exact wave-certificate before x3 = refl
width-exact wave-certificate before y4 = refl
width-exact wave-certificate before xy5 = refl
width-exact wave-certificate center x3 = refl
width-exact wave-certificate center y4 = refl
width-exact wave-certificate center xy5 = refl
width-exact wave-certificate after x3 = refl
width-exact wave-certificate after y4 = refl
width-exact wave-certificate after xy5 = refl
within-budget wave-certificate before x3 = refl
within-budget wave-certificate before y4 = refl
within-budget wave-certificate before xy5 = refl
within-budget wave-certificate center x3 = refl
within-budget wave-certificate center y4 = refl
within-budget wave-certificate center xy5 = refl
within-budget wave-certificate after x3 = refl
within-budget wave-certificate after y4 = refl
within-budget wave-certificate after xy5 = refl
moving-arrival : Grid
moving-arrival before x3 = 1167719957019506779927611
moving-arrival before y4 = 1256665696503739066840033
moving-arrival before xy5 = 1346596799615697998979499
moving-arrival center x3 = 1480136815794698069784808
moving-arrival center y4 = 1572553281161733119211021
moving-arrival center xy5 = 1665993559744598239048201
moving-arrival after x3 = 1792553674569889359642005
moving-arrival after y4 = 1888440865819727171582011
moving-arrival after xy5 = 1985390319873498479116903
moving-lower : Grid
moving-lower before x3 = 1167719957019506779927606
moving-lower before y4 = 1256665696503739066840028
moving-lower before xy5 = 1346596799615697998979494
moving-lower center x3 = 1480136815794698069784802
moving-lower center y4 = 1572553281161733119211016
moving-lower center xy5 = 1665993559744598239048196
moving-lower after x3 = 1792553674569889359642000
moving-lower after y4 = 1888440865819727171582006
moving-lower after xy5 = 1985390319873498479116898
moving-upper : Grid
moving-upper before x3 = 1167719957019506779927616
moving-upper before y4 = 1256665696503739066840038
moving-upper before xy5 = 1346596799615697998979504
moving-upper center x3 = 1480136815794698069784814
moving-upper center y4 = 1572553281161733119211026
moving-upper center xy5 = 1665993559744598239048206
moving-upper after x3 = 1792553674569889359642010
moving-upper after y4 = 1888440865819727171582016
moving-upper after xy5 = 1985390319873498479116908
moving-below : Grid
moving-below before x3 = 5
moving-below before y4 = 5
moving-below before xy5 = 5
moving-below center x3 = 6
moving-below center y4 = 5
moving-below center xy5 = 5
moving-below after x3 = 5
moving-below after y4 = 5
moving-below after xy5 = 5
moving-above : Grid
moving-above before x3 = 5
moving-above before y4 = 5
moving-above before xy5 = 5
moving-above center x3 = 6
moving-above center y4 = 5
moving-above center xy5 = 5
moving-above after x3 = 5
moving-above after y4 = 5
moving-above after xy5 = 5
moving-width : Grid
moving-width before x3 = 10
moving-width before y4 = 10
moving-width before xy5 = 10
moving-width center x3 = 12
moving-width center y4 = 10
moving-width center xy5 = 10
moving-width after x3 = 10
moving-width after y4 = 10
moving-width after xy5 = 10
moving-delay : Grid
moving-delay before x3 = 261025592308534898897978
moving-delay before y4 = 349971331792767185810400
moving-delay before xy5 = 439902434904726117949866
moving-delay center x3 = 271210996180068895078631
moving-delay center y4 = 363627461547103944504844
moving-delay center xy5 = 457067740129969064342024
moving-delay after x3 = 281396400051602891259284
moving-delay after y4 = 377283591301440703199290
moving-delay after xy5 = 474233045355212010734182
moving-slack : Grid
moving-slack before x3 = 2
moving-slack before y4 = 2
moving-slack before xy5 = 2
moving-slack center x3 = 0
moving-slack center y4 = 2
moving-slack center xy5 = 2
moving-slack after x3 = 2
moving-slack after y4 = 2
moving-slack after xy5 = 2
moving-rows : Rows
moving-rows t d = clocks (pos (slot t · 302231454903657293676544)) (pos (moving-arrival t d))
moving-certificate : ClockCertificate 1208925819614629174706175 moving-rows
calibration moving-certificate = frozen-calibration
calibration-fixed moving-certificate = refl
quarter-ticks moving-certificate = 302231454903657293676544
denominator-grid moving-certificate = refl
arrival moving-certificate = moving-arrival
row-grid moving-certificate t d = refl
delay-minus-one moving-certificate = moving-delay
refinement moving-certificate = 0
lower moving-certificate = moving-lower
upper moving-certificate = moving-upper
below moving-certificate = moving-below
above moving-certificate = moving-above
width moving-certificate = moving-width
error-budget moving-certificate = 12
slack moving-certificate = moving-slack
causal moving-certificate before x3 = refl
causal moving-certificate before y4 = refl
causal moving-certificate before xy5 = refl
causal moving-certificate center x3 = refl
causal moving-certificate center y4 = refl
causal moving-certificate center xy5 = refl
causal moving-certificate after x3 = refl
causal moving-certificate after y4 = refl
causal moving-certificate after xy5 = refl
inside-lower moving-certificate before x3 = refl
inside-lower moving-certificate before y4 = refl
inside-lower moving-certificate before xy5 = refl
inside-lower moving-certificate center x3 = refl
inside-lower moving-certificate center y4 = refl
inside-lower moving-certificate center xy5 = refl
inside-lower moving-certificate after x3 = refl
inside-lower moving-certificate after y4 = refl
inside-lower moving-certificate after xy5 = refl
inside-upper moving-certificate before x3 = refl
inside-upper moving-certificate before y4 = refl
inside-upper moving-certificate before xy5 = refl
inside-upper moving-certificate center x3 = refl
inside-upper moving-certificate center y4 = refl
inside-upper moving-certificate center xy5 = refl
inside-upper moving-certificate after x3 = refl
inside-upper moving-certificate after y4 = refl
inside-upper moving-certificate after xy5 = refl
width-exact moving-certificate before x3 = refl
width-exact moving-certificate before y4 = refl
width-exact moving-certificate before xy5 = refl
width-exact moving-certificate center x3 = refl
width-exact moving-certificate center y4 = refl
width-exact moving-certificate center xy5 = refl
width-exact moving-certificate after x3 = refl
width-exact moving-certificate after y4 = refl
width-exact moving-certificate after xy5 = refl
within-budget moving-certificate before x3 = refl
within-budget moving-certificate before y4 = refl
within-budget moving-certificate before xy5 = refl
within-budget moving-certificate center x3 = refl
within-budget moving-certificate center y4 = refl
within-budget moving-certificate center xy5 = refl
within-budget moving-certificate after x3 = refl
within-budget moving-certificate after y4 = refl
within-budget moving-certificate after xy5 = refl
