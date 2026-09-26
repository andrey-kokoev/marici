# The cosmological half-integer sector does not supply the proposed heavy-scalar dust limit

## Disposition

The proposed rapid-oscillation massive-scalar route to the Newtonian dust
fixture is NOT available within the primary source's main half-integer mode
sector in four-dimensional de Sitter. This is a parameter mismatch, not merely
an unimplemented averaging calculation. In addition, the Bunch-Davies
wavefunctional does not select the inhomogeneous two-particle source state.

This closes that narrow automatic bridge. It does not disprove other Newtonian
limits, interacting dust mechanisms, or heavy fields outside this special
sector. The primary source explicitly discusses a broader mode setup before
specializing; its scope must not be reduced to the half-integer case alone.

## Direct primary-source evidence

Inspected cached source:
`temp/triangle-measure-primary-2402.06558v3-source/IR_Divs.tex`.
The checker records its SHA-256 when available; this external cache was not
modified and is not a dependency for the rational algebra tests.

- Lines 509-541: the fixed-background scalar model, FRW metric, effective mass,
  curvature coupling, massless arbitrary-power-law branch and massive de Sitter
  branch are explicit inputs.
- Lines 542-550: Hankel order nu satisfies nu^2=1/4-mu_gamma^2; the text gives
  nu^2=d^2/4-m^2 ell_1^2 for minimal coupling in de Sitter.
- Lines 552-563: the main differential-operator construction specializes to
  nu=l+1/2, l a nonnegative integer, equivalently mu_gamma^2=-l(l+1).
- Lines 636-643: the boundary wavefunctional gives correlators by integrating
  field configurations against |Psi[Phi]|^2. It is a distribution over states,
  not a declaration of a particular two-mass density configuration.

One intervening printed effective-mass expression at line 542 has apparent
sign/bracketing problems. We do not base the argument on it. The minimal
order formula explicitly given at line 550 and the independent KG derivation
below agree. No silent correction to the source is made.

## Parameter obstruction

For a physical canonical scalar on four-dimensional de Sitter, with
H=1/ell_1, curvature coupling xi and conformal rescaling u=a phi, the free
mode equation is

    u_k'' + [k^2 + a^2 m^2 + (6 xi-1) a''/a] u_k = 0.

Here a=-1/(H eta), a''/a=2/eta^2. Comparison with the Bessel equation gives

    nu^2 = 9/4 - m^2/H^2 - 12 xi.

This derivation fixes which physical mass is being used; the negative
conformal-time coefficient mu_gamma^2 is not automatically a negative physical
mass squared. The source's half-integer condition then gives

    m^2/H^2 = 2 - l(l+1) - 12 xi.

For minimal coupling xi=0,

    m^2/H^2 = 2 - l(l+1) <= 2.

If physical m^2 is nonnegative, only l=0 (m^2/H^2=2) and l=1 (m=0) remain.
For l>=2 it is negative. For conformal coupling xi=1/6,

    m^2/H^2 = -l(l+1),

so the only nonnegative-mass case is l=0, m=0.

The proposed dust averaging route needs a parametrically rapid mass oscillation
compared with the background: m/H >> 1, as well as a slowly varying spatial
envelope and controlled stress corrections. There is no sequence in the
minimal or conformal half-integer sector meeting that hierarchy. The inequality
is for ALL nonnegative integers l, not inferred from a finite scan.

For contrast, a permitted heavy minimal scalar in the broader de Sitter free
mode equation, m/H=10, has nu^2=-391/4. Its order is imaginary, not l+1/2.
Studying that case changes the special analytic sector; the finite differential
operator from the half-integer plane-wave seed cannot simply be carried over.
The massless arbitrary-power-law branch likewise does not provide this specific
rest-mass-dominated mechanism. Neither statement rules out unrelated effective
matter mechanisms involving interactions or additional fields.

## State selection is a separate obstruction

Even a valid heavy-field sector would supply mode functions and a state
prescription, not automatically the point masses of the Newtonian toy.

Where a spatially translation-invariant Bunch-Davies state and symmetry-preserving
renormalized stress expectation are well defined, that expectation is spatially
homogeneous. It cannot equal two localized point masses. This argument concerns
the expectation, not each field configuration or its correlations. Some massless
sectors also have infrared subtleties, so no unrestricted existence claim about
a de Sitter-invariant renormalized state is made here.

Possible additional constructions include a specified excited/coherent state,
a conditioned field realization, or a probabilistic density readout. Each is
an explicit state/readout choice with its own stress and approximation analysis.
A sampled configuration is not selected by Fourier inversion alone, and its
quantum stress is not obtained by identifying graph energies with particle
masses. The primary text itself calls E_j=|p_j| an 'energy' with an abuse of
language in its graph-integral discussion.

Furthermore, a scalar theory on a prescribed FRW background is not yet its
backreacting Einstein solution. A successful matter-to-gravity bridge must
retain renormalization, background subtraction, the stress tensor including
nonminimal coupling, gravitational boundary data and the regime in which a
Poisson reduction is justified.

## What survives from the previous constructions

- Defect-indexed Euclidean momentum fibers remain valid conditional geometry.
- Their character groups supply dual displacement carriers.
- The declared particle-source model still gives the checked Newtonian jet.
- The periodic density-contrast adapter still solves its admitted discrete
  Poisson problem.
- Linearized Einstein with weak static negligible-stress sources still reduces
  to Newtonian Poisson and geodesic acceleration.

What fails is composing those arrows as though the half-integer Bunch-Davies
scalar sector had already generated the required massive localized dust state.
This is a source-model mismatch, not a failure of the individual constructions.

## Verification

Run:

    python research/voevodsky/check_cosmological_scalar_dust_gate.py

Seven exact Fraction controls passed. The checker tabulates l=0 through 8,
checks both coupling formulas, and tests a heavy-mass counterexample to
half-integer membership. The all-l obstruction is the written polynomial
inequality above. No checker proves an interacting state theorem, semiclassical
backreaction or a WKB error estimate.

Receipt: `research/voevodsky/cosmological-scalar-dust-gate.json`.

## Stop condition and justified alternatives

Do not extend the current chain with more fixture checks while calling it a
source-derived cosmological Newtonian limit. The gate is now explicit.

A subsequent investigation must choose its objective honestly:

1. Stay with the original half-integer scalar sector and compute its actual
   stress/correlation observables, without relabelling it massive dust.
2. Introduce a declared heavy scalar state and a controlled nonrelativistic
   approximation, accepting a change of analytic sector and added state data.
3. Keep the existing Newtonian particle toy as the physical realization and
   investigate its fibrations independently of a cosmological origin claim.

The original question about fibration and spatial geometry does not require
option 2. We should not introduce a new matter model merely to preserve a
conjectured identification between previously distinct research programmes.
