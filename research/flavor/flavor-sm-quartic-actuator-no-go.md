# Standard Model quartic-actuator no-go (WP419)

## Acceptance condition

To make the physical Higgs quartic an executable source control, a laboratory
command $x$ must enter the action through

$$
\Delta\mathcal L=-g_x\,x(H^\dagger H)^2,
\qquad
\frac{\partial\lambda_{\rm physical}}{\partial x}=g_x\ne0.
$$

The command must be the prepared state of a physical source, not an analysis
hypothesis, renormalization scale, or external symbol.

## Renormalizable Standard Model obstruction

The operator $(H^\dagger H)^2$ has canonical dimension four. A multiplier that
keeps the interaction within the renormalizable Standard Model must therefore
have dimension zero and be a Lorentz-scalar gauge singlet. No nonconstant
dynamical Standard Model field has those properties.

- The elementary Higgs has dimension one but is an electroweak doublet.
- The lowest Higgs-built gauge singlet, $H^\dagger H$, has dimension two.
  Multiplying the quartic by it gives $(H^\dagger H)^3$, a dimension-six EFT
  operator.
- Fermion bilinears and gauge kinetic scalars have still higher dimensions.
- A dimensionless spacetime-dependent coupling is an external spurion until a
  physical preparation mechanism and source field are supplied.

The Standard Model Higgs potential is the most general renormalizable form
$V=\mu^2H^\dagger H+\lambda(H^\dagger H)^2$; its coefficients are parameters,
not dynamical laboratory registers. See the [CERN Higgs-mechanism
summary](https://repository.cern/records/gekvm-aze63/files/Anastasoaie_2.pdf?download=1)
and [CERN Standard Model field-theory lectures](https://arxiv.org/abs/1012.3883).

## Apparent evasions

Changing collider energy probes the running and momentum dependence of a fixed
theory; it does not prepare a second value of the physical coupling in the same
apparatus. Treating a coupling as a spacetime-dependent external field is a
valid generating-functional construction, but it is not an executable physical
source until the field and its preparation are named.

A real evasion must add at least one of:

1. a new dynamical singlet or modulus;
2. an externally prepared coupling field with a physical instrument;
3. a higher-dimensional EFT operator with an observed controllable source.

Each changes the admitted source theory beyond the renormalizable Standard
Model. It must then survive collider bounds, stability, finite-width,
decoherence, and common-reference calibration before it can inherit WP416's
rank-two authority.

## Verdict

WP417 established measurement sensitivity. WP418 established an executable
analogue architecture in another domain. WP419 proves that their missing arrow
cannot be supplied by rearranging the renormalizable Standard Model field
content. Closing the requested actuation gate requires new physical source
evidence, not further algebra on existing coordinates.

Run `uv run --with sympy python
research/flavor/checkers/wp419_sm_quartic_actuator_no_go.py` to regenerate the
JSON result.
