# Local gauge-assisted motion does not preserve the electrostatic field vacuum

Date: 2026-10-10

## Result

The reduced electrostatic binding model now has a concrete reduction test.
On a single square plaquette, local charge-preserving hopping necessarily
changes the retained circulation field as well as the longitudinal Gauss field.
The exact transverse vacuum is not an invariant matter-motion sector.

For an explicitly declared noncompact harmonic field parent at beta=kappa=q=t=1:

- one local hop has transverse excitation probability 1-exp(-1/16), about 6.06%;
- a closed four-hop loop returns the charge configuration but leaves excitation
  probability 1-exp(-1), about 63.21%;
- the two routes between opposite corners leave distinguishable field states,
  with overlap exp(-1/2);
- a gradient-only hop avoids this excitation, but changes all four links rather
  than the traversed one;
- a tree control has no circulation coordinate and no such transverse kick.

This does not invalidate the preceding reduced 3D binding theorem. It shows why
that theorem cannot be transferred unchanged to a local dynamical field theory.
A controlled low-energy approximation is nevertheless available on this finite
gapped plaquette, with explicit error bounds below.

## 1. Parent model and what is newly supplied

Reuse the local matter/link coupling and Gauss bookkeeping of
`research/nima/record-gauge-feedback-loop.md` and the geometric circulation
analysis in `spinor-face-magnetic-action.md`.

Take four vertices and oriented links 0->1->2->3->0. One mobile charge +q and
one retained charge -q at vertex 0 give the neutral density

    rho_x=q(delta_x-delta_0).

Moving the positive constituent never removes the negative one. The fixed
negative source is a local test fixture, not an infinite-mass proton claim.
The square is a plaquette of the supplied cubic spatial graph, not a replacement
for either particle's internal simplex.

Use real, noncompact link coordinates A_e and conjugate E_e, with
[A_e,E_f]=i delta_ef. The electric energy is beta||E||^2/2. For an exactly soluble
parent, declare the quadratic magnetic energy

    kappa (C A)^2/2, C=(1,1,1,1).

This harmonic, noncompact parent is **not** silently identified with the earlier
compact cosine model. Its exact numerical formulas are conditional on this
choice. The more general failure of exact vacuum invariance does not require
a harmonic ground state.

Work in the Gauss-reduced physical Hilbert space, one L2 cycle coordinate per
matter position. This is a reduced quantization prescription; it does not treat
delta-function longitudinal constraints as normalizable states of the
unconstrained continuous-link L2 space.

## 2. Exact longitudinal and transverse decomposition

Let B be the vertex/link incidence, L=B B^T, and L^+ its inverse on neutral
vertex vectors. Define

    P_long=B^T L^+ B,
    P_trans=I-P_long.

For this square, with u=(1,1,1,1)/2,

    P_trans=u u^T,  E_long(x)=B^T L^+ rho_x.

The electrostatic energies at x=0,1,2,3 are respectively

    0, 3 beta q^2/8, beta q^2/2, 3 beta q^2/8.

A local hop across oriented link e must shift E by q e_e to retain Gauss:

    B(q e_e)=rho_head-rho_tail.

Its longitudinal part is exactly the difference of the two minimum Gauss
fields. Its remaining part is

    q P_trans e_e=(q/4)(1,1,1,1),
    ||q P_trans e_e||^2=q^2/4.

Thus Gauss preservation does not imply remaining at the minimum field. The
local current leaves a circulation record. A bare matter hop with unchanged E
would instead violate Gauss at its two endpoints.

The alternative q P_long e_e is (3q/4,-q/4,-q/4,-q/4), up to link permutation.
It preserves Gauss and has no transverse component, but acts on every link.
On larger graphs the gradient replacement is a spatial Green-function pattern,
not the original single-link local operation.

## 3. A genuine unitary hop, with its positive kinetic generator

Write a=u^T A and e=u^T E, so [a,e]=i. In the reduced chart, a forward hop has
field multiplier

    W=exp(i q a/2).

This shifts transverse momentum by q/2. Its reverse uses W^dagger. Define the
local matter/field swap

    R_link=|head><tail| tensor W
           +|tail><head| tensor W^dagger
           +I on other matter positions.

Then R_link^dagger=R_link and R_link^2=I. The positive edge kinetic term is

    t(I-R_link)=t D_link^dagger D_link,
    D_link psi=psi_head-W psi_tail.

This reuses the positive operation-defect construction while retaining the
field action. The checker verifies the identities with exact Laurent
polynomials in W, not a truncated oscillator commutator. Summing the four links
gives the diagonal kinetic term 2t, which must not be thrown away on reduction.

The full reduced-chart parent is

    H=H_transverse+U_electrostatic(position)+K_dressed.

After subtracting one common transverse vacuum energy, it is positive and
self-adjoint: the oscillator is confining and the matter/hopping perturbations
are bounded. Its autonomous unitary evolution conserves this total H. That is
different from externally commanding a sequence of bare swaps.

## 4. Exact oscillator readout of the retained circulation

The transverse Hamiltonian is

    H_transverse=beta e^2/2+2kappa a^2,
    omega=2sqrt(beta kappa),
    <a^2>_vac=sqrt(beta)/(4sqrt(kappa)).

Its vacuum expectation of a local link multiplier is

    Z=<W>=exp[-q^2 sqrt(beta)/(32sqrt(kappa))].

The displaced field has mean occupation

    n_bar=q^2 sqrt(beta)/(16sqrt(kappa)),

so its vacuum probability is exp(-n_bar), and its mean extra field energy is

    omega n_bar=beta q^2/8.

At unit coefficients the excitation probability is about 0.0605869372. All
reported exponential intervals are enclosed by rational alternating-series
bounds. No finite Fock truncation supplies the conclusion.

### Why this is not merely a harmonic peculiarity

For nonzero q, multiplication by exp(i q a/2) has no normalizable eigenfunction
on a continuous cycle coordinate. If W psi=c psi, nonzero psi must be supported
on the measure-zero set where exp(i q a/2)=c. Consequently any normalizable
fixed field state fails exact invariance under this local hop. The analogous
statement holds for a nonconstant integer-character multiplier on a compact
phase circle.

A delta-localized phase or an endpoint-factorized model without an independent
cycle coordinate changes the assumptions. The latter is precisely why the
previous `spinor-endpoint-constructor.md` was a different architecture rather
than a finite-stiffness proof.

## 5. Endpoint return is not field-record return

The routes 0->1->2 and 0->3->2 have the same final charge density and longitudinal
field. Their currents differ by one full loop. Their transverse momenta are
respectively shifted by +q and -q; their normalized field-state overlap is

    exp[-q^2 sqrt(beta)/(2sqrt(kappa))].

At unit coefficients this is exp(-1/2), not one. Tracing out the field therefore
loses path coherence; keeping the field preserves the full unitary record.

Executing 0->1->2->3->0 produces W^4=exp(i2q a), not identity. It returns the
matter configuration while shifting transverse momentum by 2q. Its mean added
field energy is 2 beta q^2, and its excitation probability at unit coefficients
is 1-exp(-1). A hop followed by its actual inverse cancels, as checked by
R_link^2=I. The distinction is a retained loop current, not an extra particle.

These energy increments describe commanded operations. Their controller must
supply the corresponding work, including any electrostatic change on open
paths. A closed matter route is not free energy production, and its step count
is not a derived physical clock.

## 6. What vacuum compression actually gives

Let P denote the transverse vacuum tensored with all four matter positions.
The compressed kinetic operator is

    P K_dressed P=2t I-t Z adjacency
                 =Z t L_square+2t(1-Z)I.

It is not simply tL_square, nor just a rescaled hopping after discarding the
constant term. The full sector is not invariant: for an initially localized
matter state,

    ||(I-P) H (|x> tensor |vac>)||^2=2t^2(1-Z^2)>0.

This is the explicit failed step in an exact electrostatic reduction. It does
not assert that all effective low-energy approximations fail.

## 7. A controlled finite-graph approximation does exist

Keep beta=q=t=1 and kappa=s^2, for s=1,4,16. The excited-field block obeys

    Q H Q >= omega Q, omega=2s,
    ||Q H P||^2 <= 4(1-Z^2) <= 1/(4s).

The uniform matter trial gives a full ground-energy ceiling

    E <= 5/16+2(1-Z) <= E_bar=5/16+1/(16s) < omega.

The Schur/Feshbach correction at that ground energy is therefore bounded by

    eta = 1/[4s(2s-E_bar)].

If lambda_P is the vacuum-compressed ground energy and lambda_full the full
parent ground energy, then

    lambda_P-eta <= lambda_full <= lambda_P.

Also ||H_PP-(L_square+U_electrostatic)||<=1/(16s), yielding the conservative
comparison with the purely electrostatic square model:

| kappa | Ground-energy error upper bound, model units |
|---:|---:|
| 1 | 0.216346154 |
| 16 | 0.023771640 |
| 256 | 0.004399408 |

These are rigorous finite-plaquette bounds, not measured errors or equalities.
Increasing stiffness makes the vacuum approximation better here without making
it exact at finite stiffness. The energy deposited by a *commanded* bare hop
remains 1/8: rarer excitations cost more energy. That does not contradict a
low-energy ground-state comparison.

## 8. Remaining gate for the certified 3D binding branch

The preceding `gauss-derived-spatial-binding.md` remains a checked reduced
model. The new parent calculation supplies both an exact-reduction obstruction
and a finite gapped error estimate, but **does not transfer its infinite-volume
binding certificate to a full spatial quantum field**.

A massless lattice field has transverse frequencies approaching zero with
increasing volume. The finite-plaquette Schur denominator is not a uniform
large-volume gap. The next construction must control those modes and compare
composite and breakup energies within the same full field theory. Copying the
finite error bound into the infinite lattice would hide the very missing step.

Separately, the physical source still must justify the charged spatial
translation representation, field degrees of freedom and units. This test
constructs a conditional gauge-compatible motion, not a derivation of charge
or mass from the internal coefficient counts.

## Gapless successor

`gapless-gauss-binding.md` replaces the finite-gap comparison by energy-weighted
infrared estimates and a full-field variational comparison. It proves energetic
binding in an explicitly stated large-stiffness regime without a photon gap.
The stronger charged-hop wavefunction estimate still diverges, and binding at
unit stiffness remains unsettled. This is not a uniform extension of the old
plaquette Schur bound or a physical calibration of the model.

## Verification

```sh
python research/voevodsky/checkers/check_gauss_dressed_hopping.py
```

Receipt: `results/gauss_dressed_hopping.json`. Checks cover exact graph Hodge
projectors, Gauss shifts, positive dressed kinetic gates, retained loop words,
the tree control, both equal-endpoint paths, rational exponential enclosures
and the explicit finite-gap comparison bounds. The prior 3D binding receipt's
source hashes are checked; no earlier physical conclusion is silently upgraded.
