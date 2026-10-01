{-# OPTIONS --safe --cubical --guardedness #-}
module ActualSeedEndpointTable where

open import Cubical.Foundations.Prelude
import TableFibrationCycle as T

-- The supplied primitive data, without a payload-map/equivalence adapter.
data Vertex : Type where
  A B C D : Vertex

data Occurrence : Type where
  AB BC CA AD DB BA : Occurrence

source target : Occurrence → Vertex
source AB = A
source BC = B
source CA = C
source AD = A
source DB = D
source BA = B
target AB = B
target BC = C
target CA = A
target AD = D
target DB = B
target BA = A

seed : T.Table Occurrence Vertex Vertex
seed = T.table Occurrence (λ e → e) source target

source-recovery : T.TableIso (T.unpack (T.group-from seed)) seed
source-recovery = T.unpack-correct seed

four-recovery : T.TableIso (T.four seed) seed
four-recovery = T.four-correct seed

-- Endpoint witnesses of the two directed triangles. These are not
-- equivalences between payload types carried by vertices.
ABC-AB-BC : target AB ≡ source BC
ABC-AB-BC = refl
ABC-BC-CA : target BC ≡ source CA
ABC-BC-CA = refl
ABC-CA-AB : target CA ≡ source AB
ABC-CA-AB = refl
ADB-AD-DB : target AD ≡ source DB
ADB-AD-DB = refl
ADB-DB-BA : target DB ≡ source BA
ADB-DB-BA = refl
ADB-BA-AD : target BA ≡ source AD
ADB-BA-AD = refl

-- Reversal of the presentation retains AB's label. It does not replace
-- the row with the separately supplied BA occurrence.
reversed-AB-label : T.Table.label (T.transpose seed) AB ≡ AB
reversed-AB-label = refl
reversed-AB-source : T.Table.from (T.transpose seed) AB ≡ B
reversed-AB-source = refl
reversed-AB-target : T.Table.to (T.transpose seed) AB ≡ A
reversed-AB-target = refl
