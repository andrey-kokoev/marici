(** SCC / UniMath dependency certificate for the current shifted-Gaussian RH model.
    This file proves only composition of named implications. It exposes finite
    double-contact exclusion as an unproved hypothesis. *)
Require Import UniMath.Foundations.All.

Section WeilGaussianRHReduction.

Context
  (BroadGaussianPositivity
   FiniteThresholdCharacterCoercivity
   FiniteDoubleContactExclusion
   AllScaleGaussianPositivity
   PositiveCompletedWeilDistribution
   WeilQuadraticPositivity
   RiemannHypothesis : UU).

(** Established analytically outside this certificate. *)
Context (broad_gaussian_positivity : BroadGaussianPositivity).
Context (finite_threshold_character_coercivity :
  FiniteThresholdCharacterCoercivity).

(** The current unresolved mathematical frontier. *)
Context (finite_double_contact_exclusion :
  FiniteDoubleContactExclusion).

(** Reviewed implication: broad positivity plus coercivity makes any first
    failure an attained finite double contact. Excluding that contact gives
    positivity at every Gaussian scale and translate. *)
Context (threshold_reduction :
  BroadGaussianPositivity ->
  FiniteThresholdCharacterCoercivity ->
  FiniteDoubleContactExclusion ->
  AllScaleGaussianPositivity).

(** Gaussian approximate identities promote all-scale translated positivity
    to positivity of the completed source distribution. *)
Context (gaussian_approximate_identity_promotion :
  AllScaleGaussianPositivity -> PositiveCompletedWeilDistribution).

(** The centered Mellin restriction of a multiplicative quadratic test is
    |F_g|^2, hence a positive completed distribution gives Weil positivity. *)
Context (positive_distribution_to_weil_quadratic :
  PositiveCompletedWeilDistribution -> WeilQuadraticPositivity).

(** Directly sourced Weil criterion. *)
Context (weil_criterion : WeilQuadraticPositivity -> RiemannHypothesis).

Theorem current_model_reduces_RH_to_finite_double_contact_exclusion :
  RiemannHypothesis.
Proof.
  apply weil_criterion.
  apply positive_distribution_to_weil_quadratic.
  apply gaussian_approximate_identity_promotion.
  exact (threshold_reduction
    broad_gaussian_positivity
    finite_threshold_character_coercivity
    finite_double_contact_exclusion).
Defined.

(** No constructor for this object is supplied in the current model. *)
Definition unresolved_frontier : UU := FiniteDoubleContactExclusion.

End WeilGaussianRHReduction.
