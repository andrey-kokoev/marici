# Local Gauss energy supplies a spatial interaction and a certified 3D bound state

Date: 2026-10-10

## Result and architecture change

Reusing the prior positive electric-field energy and Gauss constraint produces
an interaction profile instead of choosing a wider attractive potential by hand.
On a supplied three-dimensional cubic lattice, opposite unit charges give

    H_relative = t L - beta G(x),  L G = delta_0.

Here L is the unit nearest-neighbour Laplacian and G its infinite-lattice Green
kernel. Both individual source self-energies are retained in the common breakup
reference. A finite, exact integer certificate proves a negative Rayleigh
quotient at the fixed t=beta=1:

    E_ground <= -3002659063386680106684521
                /6445167900889805988323917824
             < -0.0004658775.

This certifies a bound level in this **conditional reduced electrostatic 3D
model**. It is an upper bound on its ground energy, not its exact binding energy
and not a calibrated hydrogen result.

This is a genuine change of mediator architecture: a spatial longitudinal Gauss
field replaces the preceding single gapped onsite record. The earlier 3D
nonbinding theorem remains true for its own contact model. Its coupling has not
been increased to defeat that theorem.

## 1. Recovered prior work and new inputs

`open-flux-common-vacuum.md` and `weighted-matter-link-adapter.md` already supply
incidence-based Gauss constraints, positive electric energy, field elimination
and the requirement to retain boundary flux and reference energy. The former
explicitly stopped at a finite network, not a continuum Coulomb derivation.

`native-operation-energy-lift.md` supplies the positive operation-defect energy
rule. Apply it to three **supplied** spatial translations tau_j:

    D_j=tau_j-I,
    sum_j D_j^dagger D_j
       =6I-sum_j(tau_j+tau_j^dagger)=L.

After suppressing the common energy-unit coefficient, this supplies the kinetic
form tL. The checker verifies this identity with exact integer periodic
translation matrices. Translation is not being inferred from the five-cycle
that moves the internal electron attachment. The spatial lattice, translations,
length unit and kinetic coefficient are additional admitted data.

For the field, use the same nearest-neighbour graph, oriented incidence B, and

    L=B B^dagger,
    H_field=beta ||E||^2/2,
    B E=rho.

The charge map is the supplied point-monopole reading

    rho=q_p delta_(x_p)+q_e delta_(x_e), q_p=+1, q_e=-1.

These are conserved species-charge assignments, not values extracted from the
old polarization flux. The retained internal carrier/spin records are not
removed; the external source reading uses their number flags and a declared
center position. Deriving that reading from the internal face records remains
an obligation.

No experimental mass, binding energy or length enters. The kinetic coefficient
remains t=1 as in the preceding contact fixture. beta=1 reuses a prior electric
fixture. The former contact coupling g=1/2 is absent because its mediator has
been replaced, not reinterpreted as beta.

## 2. Derive the profile with all self-energies present

Let phi solve L phi=rho with the common decaying boundary convention. The
minimum-energy field is E_min=B^dagger phi. Any divergence-free addition is
orthogonal to that gradient and increases the energy. Thus

    U(rho)=beta <rho,G*rho>/2.

On the infinite 3D lattice, G is the energy-space Green kernel, not a bounded
inverse of L on all of l2. Although a single-source potential need not be in
l2, its gradient has finite squared norm G(0). The Fourier integral for G(0)
is finite in dimension three. This keeps the single-source field energies
finite without a subtracted point-charge ultraviolet divergence.

For separation r=x_e-x_p and unit opposite charges,

    U_pair(r)=beta [G(0)-G(r)],
    U_p=U_e=beta G(0)/2,
    U_pair(r)-U_p-U_e=-beta G(r).

Every term refers to the same infinite field and boundary convention. No
reservoir is removed, no different field vacuum is used for the pair, and no
particle-specific energy offset is introduced. Since 0<=G(r)<=G(0), the full
field energy is nonnegative even though its connected contribution is negative.
At coincidence it vanishes because the two source charges cancel; both
constituent-number records still remain.

Same-sign charges instead give +beta G(r), a nonnegative relative potential.
The checker tests the charge sign and self-energy subtraction on actual exact
finite incidence/Green data, keeping all grounded boundary edges in the field
norm. It also tests the general two-source Gram identity.

The nonzero spatial range is now a consequence of the admitted local field law:
G(r)>0 at every finite connected separation. It is not a freely chosen contact
radius. The three-dimensional Fourier symbol

    L(k)=2 sum_j(1-cos k_j)

has a quadratic zero at k=0. Its inverse is integrable in dimension three and
its Fourier coefficients tend to zero. Therefore G(r)->0 at separation and
the breakup threshold of H_relative is zero.

## 3. Reduced quantum model, not a hidden full gauge-field theorem

We explicitly define the relative quantum Hamiltonian tL-beta G(x) after this
longitudinal electrostatic elimination. In a fixed particle sector the bare
internal carrier energies are the same at contact and breakup and cancel.
The bounded decaying potential leaves the essential spectrum of tL unchanged;
a negative Rayleigh quotient therefore proves a discrete level below breakup.
The lower bound -beta G(0) prevents collapse in this lattice model.

This specifies a reduced electrostatic branch. It does **not** prove that
quantizing the complete independent-link matter/field theory and eliminating
its modes yields this Hamiltonian with no correction. Gauge-assisted hopping,
transverse field modes, radiation and possible kinetic corrections require a
separate construction. No instantaneous physical signaling claim is made.

The new interaction acts as identity on the admitted logical spins. Unlike the
preceding chosen singlet contact, it does not split singlets and triplets. The
same spatial result is compatible with either electron doublet embedding, and
does not choose chirality or spin lift. No spin-selection result has been
silently transported from the different mediator model.

## 4. Exact certificate rather than a floating-point eigenvalue

For a finite grounded cube B=[-M,M]^3, the Dirichlet Green function satisfies
G_B(x)<=G(x). A numerical sine-transform solve only proposes its values.
The checker then constructs integers h(x) and verifies exactly

    h>=0, L_B h <= S delta_0, S=2^40.

Because the grounded Laplacian has a nonnegative inverse,

    h/S <= G_B <= G.

The proposal is symmetrized and rounded. The barrier

    b(x)=3(M+1)^2-|x|^2

satisfies L_B b>=6, including boundary sites. Subtracting a verified multiple
of b corrects every positive residual; taking the positive part preserves the
subsolution inequality. Integer ranges are checked before arithmetic that
could overflow. The resulting certificate does not depend on trusting the
floating-point solver's accuracy.

The trial wavefunction is the product tent

    psi_R(x)=product_j max(R-|x_j|,0).

Its exact normalized kinetic energy is

    <tL> = 18t/(2R^2+1).

The weighted sum of h/S gives an exact rational lower bound on <G>, so

    <H_relative> <= 18t/(2R^2+1)-beta <h/S>.

The complete unrounded rational expression, not a displayed decimal, decides
its sign. The finite cube bounds only the attractive Green kernel; it does not
replace the infinite-volume self-energy in the breakup reference.

### Resolution control with unchanged coefficients

| Green certificate cube | Trial radius | Certified energy upper bound |
|---|---:|---:|
| M=64 | 60 | positive, approximately 0.000129318 |
| M=96 | 52 | positive, approximately 0.000075057 |
| M=96 | 60 | negative, approximately -0.000223234 |
| M=96 | 72 | negative, approximately -0.000413265 |
| M=96 | 88 | negative, approximately -0.000465878 |

The first small-box attempt did not certify binding. It was not evidence of
nonbinding. Enlarging the certificate box and trial support supplies a negative
witness without changing t, beta, charges, interaction law or reference.

The compact witness stores one cubic-symmetry chamber. Fresh replay reconstructs
the full integer array, checks the inequality and repeats the rational energy
calculation without SciPy. A one-unit alteration at a tested entry is rejected
by the inequality checker. The raw proposal is not the trusted certificate.

## 5. What is now justified, and what remains on the critical path

| Question | Disposition |
|---|---|
| Can a spatial interaction follow from the existing local positive field law? | Yes, conditionally: Gauss elimination gives the Green-kernel interaction. |
| Does attraction require throwing away field self-energy? | No. Both self-energies are retained and cancel against the same breakup reference. |
| Does a 3D bound-state witness exist without fitting a measured energy? | Yes, with an exact variational certificate at the declared fixed coefficients. |
| Was the failed onsite mediator repaired by the same assumptions? | No. This is a different, spatial Gauss-field branch. |
| Are native source records already proved to carry this spatial charge and translation action? | No. That attachment is still supplied. |
| Is the full gauge-field quantum reduction proved? | No. Only the explicitly defined reduced electrostatic model is certified. |
| Are physical mass, length, charge normalization or hydrogen binding predicted? | No. Model-unit binding is not calibration or particle identification. |

The most informative next task is now narrower: attach the retained carrier
records to a physical spatial charge/current and translation representation,
including the energy/time/length scales, or derive the reduced kinetic term
from a complete admitted gauge-field Hamiltonian. More potential-shape tuning
would not solve those remaining source-to-physics obligations.

## Dynamical successor

`gauss-dressed-hopping-reduction.md` constructs a local gauge-assisted hopping
parent on a square and tests this reduction instead of assuming it. Local hops
preserve Gauss but excite circulation; closed matter loops retain different
field states. Exact vacuum restriction fails, while a finite gapped harmonic
parent admits controlled ground-energy comparison bounds. Those bounds do not
yet extend uniformly to an infinite massless field or transfer the binding
certificate above to a full field theory.

## Verification

```sh
uv run --with numpy --with scipy python research/voevodsky/checkers/check_gauss_spatial_binding.py --half-width 64
uv run --with numpy --with scipy python research/voevodsky/checkers/check_gauss_spatial_binding.py
uv run --with numpy python research/voevodsky/checkers/check_gauss_spatial_binding.py --replay research/voevodsky/results/gauss_spatial_green_lower.npz
```

Receipts: `results/gauss_spatial_binding_box64.json`,
`results/gauss_spatial_binding.json`, `results/gauss_spatial_binding_replay.json`.
Compressed certificates: `results/gauss_spatial_green_lower_box64.npz` and
`results/gauss_spatial_green_lower.npz`.

The checker also verifies the current hashes of the preceding source-embedded
contact receipt's inputs. It does not rerun every historical research checker
or certify a physical implementation. No catalogue or viewer status is upgraded.
