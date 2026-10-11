# Gapless field control and a conditional full-field binding witness

Date: 2026-10-10

## Result

We can advance beyond the finite-plaquette gap argument without pretending that
the transverse vacuum is an invariant sector.

1. A single charged hop has a finite inverse-energy-weighted field excitation
   in three dimensions, uniformly as the photon gap closes.
2. Its stronger inverse-energy-squared quantity diverges logarithmically. The
   old finite-gap wavefunction argument therefore cannot simply be reused.
3. Coherent translation of a bounded neutral pair cancels that divergence;
   independent constituent hops and arbitrary breakup separations do not
   automatically inherit this cancellation.
4. A full-field variational trial and a same-field breakup lower bound prove
   **energetic binding in an explicit large-stiffness parameter regime**.
5. This certificate does not settle binding at the original unit stiffness.
   No physical stiffness, charge, mass or length has been selected.

The full-field proof does not require exact electrostatic reduction. The
previously certified electrostatic state can instead be used as a trial state
in the larger, dynamical theory, with its additional kinetic cost retained.

## 1. Specify the same full field on both sides of breakup

Use the supplied infinite cubic lattice and two conserved species with q_p=+1,
q_e=-1. Their positive hopping coefficients obey t_p+t_e=t=1; neither individual
coefficient is calibrated as a physical mass. Both particles move. Their
internal retained carrier energies are unchanged in the comparison and cancel.

The transverse field is the noncompact harmonic Fock field extending the
preceding plaquette parent. Write

    lambda(k)=2 sum_j(1-cos k_j),
    omega(k)=sqrt(beta kappa) sqrt(lambda(k)),
    P_T(k)=I-d(k)^dagger d(k)/lambda(k),
    |d_j(k)|^2=2-2cos k_j.

Momentum integrals below use normalized measure dk/(2pi)^3 on the Brillouin
zone. The k=0 point has measure zero; no positive photon gap is imposed.
The field Hamiltonian is H_f=dGamma(omega), with one common vacuum normalization
in all particle configurations. The retained longitudinal self-energies are
separate and are not discarded by this transverse vacuum convention.

A directed hop of species s carries W_s=exp(i q_s A_j(x)); its reverse carries
W_s^dagger. The kinetic energy K_s is the positive sum of gauge-assisted edge
defects, as in the plaquette construction. Each hop preserves the species and
reconstructs the Gauss-compatible longitudinal field; its transverse Weyl
factor retains the circulation part of the local current.

After subtracting the **same two static source self-energies** as before,

    H_full=H_f+K_p+K_e-beta G(x_p-x_e).

Here G is the infinite-lattice electric Green function. This is an explicitly
admitted Coulomb-gauge, noncompact harmonic quantum model, not a microscopic
identification of our particle candidates. It is not the earlier compact
cosine model. The lattice provides the ultraviolet cutoff; physical length,
action and time units remain uncalibrated.

The matter kinetic terms and potential are bounded, while H_f is self-adjoint
and positive. Thus H_full is self-adjoint on D(H_f) and bounded below. The Weyl
hops are well defined because their smearing functions have finite norm in 3D.
No independent field vacuum or reservoir is introduced at breakup.

## 2. Gapless single-hop estimates

For a link in direction j, write its Weyl-displaced vacuum as the coherent
state W(f_j)|0>. Its mode intensity is

    |f_j(k)|^2=q^2 beta P_T,jj(k)/(2 omega(k)).

Define

    a=||f_j||^2,
    b=integral |f_j(k)|^2/omega(k),
    c=integral |f_j(k)|^2/omega(k)^2.

Cubic symmetry and tr(P_T)=2 give

    a=q^2 sqrt(beta) J/(3sqrt(kappa)), J=integral lambda^(-1/2),
    b=q^2 G(0)/(3kappa), G(0)=integral lambda^(-1).

The preceding Fourier-ball inequality gives G(0)<=11/16. Cauchy–Schwarz then
gives J<=sqrt(G(0))<1. At beta=q=1,

    a<=1/(3sqrt(kappa)),
    b<=11/(48kappa).

Neither estimate contains a lowest photon frequency.

For nonzero-momentum grid quadratures of side N, an independent shell bound
also works uniformly. Since lambda>=16|m|^2/N^2 and a maximum-norm shell has
24m^2+2 points,

    G_N(0)<=3/4+1/(4N)<=7/8, N>=2.

Hence b_N<=7/(24kappa) and J_N<1. These are quadratures of the infinite field,
not a claim that fixing the harmonic zero mode of a physical finite torus is
preserved by every local charged hop. Such a finite-torus claim would require
its own harmonic-mode treatment.

## 3. What these norms do and do not control

Let Q=I-|0><0| in Fock space. Expanding the coherent state by photon number gives

    ||H_f^(-1/2) Q W(f)|0>||^2
      = exp(-a) sum_(n>=1) (1/n!)
          integral product_i |f(k_i)|^2 / sum_i omega(k_i).

Bounding the denominator by any one positive omega(k_i), followed by the
exponential sum, gives

    ||H_f^(-1/2) Q W(f)|0>||^2
       <= b (1-exp(-a))/a <= b.

Thus the energy-weighted excitation is controlled without a photon gap. The
checker tests this series estimate, with exact tails, on finite rational mode
fixtures; the integral proof supplies the infinite-volume statement.

For the stronger norm ||H_f^(-1) Q W(f)|0>||^2, its one-photon term already
contains exp(-a)c. At small k, lambda is quadratic and P_T,jj is positive on a
cone of nonzero solid angle. Consequently

    c contains a positive multiple of integral_0 dk/k = infinity.

This is a genuine distinction between an energy-form bound and a wavefunction
bound. It does not prove that the interacting neutral system has no ground
state. Nor does the finite b alone provide a Feshbach estimate for H_full:
its excited-field sector also contains matter binding and arbitrarily soft
photons, not the isolated positive gap of the old plaquette argument.

## 4. Neutrality cancellation has a precise scope

For a simultaneous equal translation of two opposite charges separated by an
integer vector R, the coherent displacement is

    f_pair(k)=(1-exp(i k.R)) f_j(k).

The lattice telescoping inequality gives

    |1-exp(i k.R)|^2 <= |R|^2 lambda(k).

It follows that the inverse-energy-squared integral is finite and satisfies

    c_pair <= |R|^2 q^2 J/(3sqrt(beta) kappa^(3/2)).

This removes the single-hop logarithmic divergence for a fixed bounded dipole.
It is not a uniform bound as |R| tends to infinity, nor a replacement for every
independent hop in K_p+K_e. Calling the total pair neutral would not justify
silently substituting a correlated rigid translation for those operations.

The numerical momentum sums are diagnostic, not the proof:

| Grid side N | Charged inverse-energy-squared sum | Unit-dipole sum |
|---:|---:|---:|
| 8 | 0.0440318 | 0.0354351 |
| 16 | 0.0557482 | 0.0362870 |
| 32 | 0.0674582 | 0.0364885 |
| 64 | 0.0791646 | 0.0365383 |

The charged logarithmic growth and bounded dipole behavior agree with the
analytic comparison. A finite list of sums alone would not establish either.

## 5. A same-field breakup bound without gap assumptions

Define the separation threshold by restricting normalized states to
|x_p-x_e|>=R and taking the limiting energy infimum as R tends to infinity.
All these states live in the same field theory and particle-number sector.

Since H_f>=0 and each K_s>=0,

    H_full >= -beta sup_(|r|>=R) G(r)

on those supports. G(r)->0, so the full-field separation threshold Sigma obeys

    Sigma>=0.

Zero is a **lower bound**, not a calculation of the exact dynamically dressed
breakup energy. In particular, isolated charged kinetic/field dressing has not
been replaced by its bare or vacuum-compressed energy. This conservative bound
is enough if a normalized full-field trial has energy below zero.

## 6. Reuse the certified spatial trial in the full theory

The earlier exact integer certificate supplies a normalized relative tent
wavefunction psi with

    <psi,(L-beta G)psi> <= -B,
    B=3002659063386680106684521/6445167900889805988323917824,

at beta=t=1. Keep that same trial and its R=88 profile. Do not refit the potential
or discard any of its energy terms.

Normalize the common position with a constant wavefunction F_L supported on a
cube of side L, and take the full state

    F_L(x_p) psi(x_e-x_p) tensor |vac>.

This is a normalizable state in the full matter/field Hilbert space; no
non-normalizable center-of-mass plane wave is used. A unit translation of F_L
has overlap 1-1/L, adding at most 6t_p/L to the bare kinetic expectation.

Every single-charge link vacuum factor is Z=exp(-a/2), for either sign of q.
The full kinetic expectation retains both terms

    Z <K_bare> + 6(t_p+t_e)(1-Z).

In particular the diagonal vacuum-compression cost has not been erased.
Because t_p+t_e=1, beta=q=1, and 1-exp(-a/2)<=a/2,

    <H_full> <= -B + 6(1-Z)+6/L
             <= -B + 1/sqrt(kappa)+6/L.

This is a variational upper bound in the full gapless field, not an exact
restriction to an invariant vacuum sector. Lack of invariance does not prevent
using a vacuum-containing trial state.

Therefore the explicit sufficient condition

    1/sqrt(kappa)+6/L < B

proves energy strictly below Sigma. It uses no photon gap, isolated charged
mass estimate, fitted measured binding, or altered breakup reference.

### Constructive parameter example and its limitation

For kappa=2^24 and L=2^16 the certified full trial satisfies

    <H_full> <= -839058999001064082772073
                 /6445167900889805988323917824
              approximately -0.000130184196 < 0 <= Sigma.

This supplies an energetic binding witness in that stated parameter regime.
The same conservative bound is positive at kappa=1,16,256. It does not settle
binding or nonbinding there. The large stiffness is an explicit new parameter
choice for the theorem's example, **not a physically derived value and not a
repair at unchanged unit stiffness**.

The condition is sufficient, not necessary. It is deliberately conservative:
the true breakup threshold can exceed the zero lower bound used here, and the
trial does not optimize its field dressing.

## 7. What is and is not closed

Completed conditionally:

- a gapless energy-weighted control on the actual local Weyl hop;
- a precise stronger infrared obstruction and a bounded-dipole cancellation;
- a common full-field separation comparison with all reference terms retained;
- energetic binding in an explicit full-field parameter regime.

Not completed:

- binding at the original unit stiffness;
- existence of an isolated eigenstate of the full translating, massless-field
  Hamiltonian—energetic binding is a weaker claim;
- a physical choice of magnetic stiffness, spatial charge/translation action,
  mass ratio or length/time/energy units;
- identification of this noncompact harmonic model with physical hydrogen.

The next worthwhile quantitative test is a dressed pair-versus-dressed breakup
comparison at a fixed source-justified stiffness, retaining shared soft-field
correlations. Merely increasing stiffness can produce more conditional
witnesses but does not determine the physical parameter.

## Verification

```sh
python research/voevodsky/checkers/check_gapless_gauss_binding.py
```

Receipt: `results/gapless_gauss_binding.json`. The checker binds the earlier
static certificate and its solver-free replay, checks their current source
hashes, verifies rational shell and coherent-state estimates, records the
finite-mode diagnostics and checks the full-field trial inequalities exactly.
The analytic arguments above establish the infinite-volume conclusions; no
finite momentum grid or Fock cutoff is substituted for them.
