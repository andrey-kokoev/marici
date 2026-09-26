{-# OPTIONS --cubical --guardedness #-}
------------------------------------------------------------------------
-- PhysicsConstants.agda
--
-- Arithmetic theorems for every physics domain in the carrier programme.
-- Each theorem expresses a physical constant as a Nat expression
-- in the four Gram numbers (11, 12, 4, 10).
------------------------------------------------------------------------
module PhysicsConstants where

open import Agda.Builtin.Nat
  using (Nat; zero; suc; _+_; _*_; _-_)
open import Cubical.Foundations.Prelude
  using (_≡_; refl)

-- The four Gram numbers
r : Nat; r = 11
l : Nat; l = 12
s : Nat; s = 4
c : Nat; c = 10

-- Squares
r2 : Nat; r2 = 121; r2-ok : r * r ≡ r2; r2-ok = refl
l2 : Nat; l2 = 144; l2-ok : l * l ≡ l2; l2-ok = refl
s2 : Nat; s2 = 16;  s2-ok : s * s ≡ s2; s2-ok = refl
c2 : Nat; c2 = 100; c2-ok : c * c ≡ c2; c2-ok = refl

-- 1.  FINE-STRUCTURE: alpha-inv = 137 = r2 + s2
alpha-inv : Nat; alpha-inv = 137
alpha-ok : r2 + s2 ≡ alpha-inv; alpha-ok = refl

-- 2.  HIGGS: m_H = 125 = r2 + s
higgs-mass : Nat; higgs-mass = 125
higgs-ok : r2 + s ≡ higgs-mass; higgs-ok = refl
higgs-vev : Nat; higgs-vev = 246
vev-ok : 2 * r2 + s ≡ higgs-vev; vev-ok = refl

-- 3.  BARYON FRACTION: Omega_b = (c - s) / r2 = 6/121
Ob-num-ok : c - s ≡ 6;    Ob-num-ok = refl
Ob-den-ok : r2 ≡ 121;     Ob-den-ok = refl

-- 4.  DARK MATTER FRACTION: Omega_DM = (c - s) / (l + r) = 6/23
ODM-num-ok : c - s ≡ 6;  ODM-num-ok = refl
ODM-den-ok : l + r ≡ 23; ODM-den-ok = refl

-- 5.  DARK ENERGY FRACTION: Omega_de = r / (l + s) = 11/16
Ode-num-ok : r ≡ 11;     Ode-num-ok = refl
Ode-den-ok : l + s ≡ 16; Ode-den-ok = refl

-- 6.  PROTON-ELECTRON RATIO: l * (l2 + (s-1)^2) = 1836
p-e-ratio : Nat; p-e-ratio = 1836
pe-ok : l * (l2 + (s - 1) * (s - 1)) ≡ p-e-ratio; pe-ok = refl

-- 7.  CKM CORRECTION: (s/l)^2 = 16/144 = 1/9 (numerator/denominator)
-- Only the correction is Gram-derived; pi/3 is not.
CKM-num-ok : s2 ≡ 16;  CKM-num-ok = refl
CKM-den-ok : l2 ≡ 144; CKM-den-ok = refl

-- 8.  LARMOR FACTOR: s2 / (l2 * c) = 16/1440 = 1/90
L-num-ok : s2 ≡ 16;    L-num-ok = refl
L-den-ok : l2 * c ≡ 1440; L-den-ok = refl

-- 9.  MACHIAN DENOMINATOR: 5280 = l * s * r * c
machian-den : Nat; machian-den = 5280
machian-ok : l * s * r * c ≡ 5280; machian-ok = refl

-- 10. PMNS PHASE: ratio l/c = 12/10 = 6/5 is exact in rationals.
-- The full phase (l/c)*pi = 6*pi/5 requires real analysis.
-- See WolframBooleanAlgebra.agda for the Boolean algebra NAND proof.