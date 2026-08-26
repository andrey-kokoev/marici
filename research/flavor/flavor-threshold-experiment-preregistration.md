# Threshold experiment preregistration (WP428)

## Purpose

WP427 identifies executable multi-point threshold spectroscopy as the remaining
instrument gate for the conditional WP128 selector architecture. Following
Nima's sequence-4512 constraint, this packet freezes the rival class,
preparation law, intervention ports, detector response, and acceptance rule
before any response rank is computed.

This is a conditional protocol definition. It does not grant physical authority
to the portal or claim that the experiment currently exists.

## Frozen rival class

The bounded non-gauge rival class has exactly three labelled constructors:

1. `R_two_adjoint`: the renormalizable WP128 two-adjoint constructor;
2. `R_auxiliary`: the WP127 auxiliary-adjoint threshold constructor;
3. `R_contact`: a direct local contact constructor with no resolved pole.

All three are required to reproduce the same frozen low-energy coefficient
packet before threshold data are inspected. No rival may be added, removed, or
retuned after inspecting the selector-facing readout. Passing this class would
not establish open-world source identification.

## Frozen preparation law

The conditional source port is a common calibrated scalar-current impulse
(u(t)) coupled through the same declared singlet portal normalization. Its
integrated fluence is fixed to one detector-control unit by an inclusive control
channel that does not use the quartic-facing threshold bins.

Each rival receives the same commanded impulse. Rival-specific production
normalizations must be measured in the inclusive control channel and then
frozen; they may not be fitted using the four selector-facing readouts. If no
such common portal can be physically realized, the protocol fails before rank.

## Frozen interventions and readouts

An independently measured calibration pole supplies a center (omega_c) and
linewidth (Gamma_c>0). The three absorptive settings are

$$
\omega_- = \omega_c-2\Gamma_c,
\qquad
\omega_0 = \omega_c,
\qquad
\omega_+ = \omega_c+2\Gamma_c.
$$

The fourth readout is a subtracted off-shell contact bin centered at
(omega_c+6Gamma_c). Its subtraction coefficients are fixed from sidebands
before unblinding. The four readouts are labelled `loss_minus`, `loss_center`,
`loss_plus`, and `contact_far`.

Detector smearing is a normalized Gaussian with standard deviation
(sigma=\Gamma_c/2). The scan window is fixed to
([omega_c-3Gamma_c,\omega_c+7Gamma_c]). Calibration uncertainty and finite
support completion are deferred to a later robustness packet; they cannot be
silently absorbed into rival coefficients.

## Frozen acceptance and falsifiers

The successor calculation may claim contextual separation on this bounded
class only if the detector-smeared (4\times3) response matrix has column rank
three and its smallest singular value remains positive under the separately
declared calibration uncertainty set. Selection authority additionally
requires an independently sourced WP128 preparation law; rank alone is only
identification within the frozen rival class.

Predeclared falsifiers are:

- no common physical preparation portal;
- two rival columns become identical after smearing and subtraction;
- rank below three;
- smallest singular value reaches zero under admitted uncertainty;
- normalization or sideband subtraction uses selector-facing bins;
- a predeclared non-gauge rival outside the three-class packet reproduces all
  four readouts;
- threshold settings are moved after inspecting the desired outcome.

## No-outcome boundary

WP428 contains no response entries, determinant, singular value, or rank result.
Its checker verifies this absence as part of the preregistration. The successor
must import the generated JSON unchanged and compute the response without
altering any frozen field.

Run `uv run --with sympy python
research/flavor/checkers/wp428_threshold_experiment_preregistration.py` to
regenerate the JSON packet.
