import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum

/-!
Finite-support branch of Grothendieck's scalar-weighted reduced exclusion
energy trichotomy.
-/

namespace MariciFormal

open Finset
open scoped BigOperators

/-- A reduced exclusion port is visible exactly when its label is not
divisible by the port index. -/
def exclusionVisible (port label : ℕ) : Prop :=
  ¬ port ∣ label

def supportProduct (ports : Finset ℕ) : ℕ :=
  ∏ p ∈ ports, p

theorem member_divides_supportProduct
    (ports : Finset ℕ) {p : ℕ} (hp : p ∈ ports) :
    p ∣ supportProduct ports := by
  unfold supportProduct
  exact Finset.dvd_prod_of_mem id hp

/-- Every port in a finite support vanishes on the product label. -/
theorem finiteSupport_productLabel_invisible
    (ports : Finset ℕ) :
    ∀ p ∈ ports, ¬ exclusionVisible p (supportProduct ports) := by
  intro p hp
  simpa [exclusionVisible] using member_divides_supportProduct ports hp

/-- If the ports are nontrivial, their product is a nonvacuum label missed by
every port in the finite family. -/
theorem finiteSupport_not_jointlyFaithful_on_nonvacuum
    (ports : Finset ℕ) (hnonempty : ports.Nonempty)
    (hports : ∀ p ∈ ports, 2 ≤ p) :
    supportProduct ports ≠ 1 ∧
      ∀ p ∈ ports, ¬ exclusionVisible p (supportProduct ports) := by
  constructor
  · obtain ⟨p, hp⟩ := hnonempty
    have hpdiv : p ∣ supportProduct ports := member_divides_supportProduct ports hp
    intro hproduct
    rw [hproduct] at hpdiv
    have hpone : p = 1 := Nat.dvd_one.mp hpdiv
    omega
  · exact finiteSupport_productLabel_invisible ports

theorem ports_two_three_miss_six :
    supportProduct {2, 3} = 6 ∧
      ¬ exclusionVisible 2 6 ∧ ¬ exclusionVisible 3 6 := by
  norm_num [supportProduct, exclusionVisible]

end MariciFormal
