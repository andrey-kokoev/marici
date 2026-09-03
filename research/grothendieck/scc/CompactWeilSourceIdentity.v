(** SCC / UniMath structural certificate for the compact-support Weil source identity.
    The classical explicit formula and analytic closure lemmas remain named
    hypotheses. This module proves only structural assembly. *)
Require Import UniMath.Foundations.All.

Section CompactWeilSourceIdentity.
Context {Test Scalar : UU}.
Context (addS : Scalar -> Scalar -> Scalar).
Context (eqS : Scalar -> Scalar -> hProp).
Definition form := Test -> Test -> Scalar.
Context (endpoint gamma prime completed : form).
Definition pointwise_sum (a b : form) : form :=
  fun f g => addS (a f g) (b f g).
Definition source_sector_sum : form :=
  pointwise_sum endpoint (pointwise_sum gamma prime).
Definition forms_equal (a b : form) : UU :=
  forall f g, eqS (a f g) (b f g).

(** Externally sourced premise, not proved by SCC. *)
Context (centered_completed_xi_explicit_formula :
  forms_equal completed source_sector_sum).
Context (half_divisor_normalization : UU).
Context (polar_endpoint_normalization : UU).

Theorem source_form_equals_endpoint_plus_gamma_plus_prime :
  forms_equal completed source_sector_sum.
Proof.
  exact centered_completed_xi_explicit_formula.
Defined.

(** Compact-support truncation remains an explicit analytic premise. *)
Context (PrimeIndex FinitePacket : UU).
Context (active_on_support : Test -> PrimeIndex -> hProp).
Context (packet_contains : FinitePacket -> PrimeIndex -> hProp).
Context (finite_active_support :
  forall f : Test, total2 (fun xs : FinitePacket =>
    forall n : PrimeIndex, active_on_support f n -> packet_contains xs n)).

Theorem compact_support_has_finite_prime_packet (f : Test) :
  total2 (fun xs : FinitePacket =>
    forall n : PrimeIndex, active_on_support f n -> packet_contains xs n).
Proof.
  exact (finite_active_support f).
Defined.

(** No positivity proposition is assumed or produced. *)
Definition positivity_is_not_assumed : unit := tt.
End CompactWeilSourceIdentity.
