# Source Gauss audit and a conditional Coulomb binding realization

## Result and boundary

The inherited sources do not yet select a physical Coulomb interaction.
A one-bridge extension of the existing electric graphs gives a separable
internal pair energy, not a three-dimensional relative-space Coulomb kernel.

A separate continuum continuation **does** construct the standard
nonrelativistic Coulomb ground state and its lower bound, provided Maxwell
space/field laws, dimensional charges and masses are explicitly supplied.
It preserves the native electron doublet and all 24 internal potential folds.

This continuation is not a derivation of those physical inputs from the arrow
network. It uses no numerical hydrogen benchmark and infers no mass from a
transfer count. The difference between a source-selected law and an externally
supplied physical law is recorded in the executable contract and receipt.

## 1. Recover the strongest retained field law first

`research/strominger/contracts/common-endpoint-charging.json` and its receipt
supply a finite-graph electric law

    E_internal=(beta/2) rho^T L^+ rho.

The inherited proton electric graph has 12 vertices; the electron electric
graph has four. Both use unit internal electric edge weights. Their resistance
matrices are freshly reconstructed and compared exactly with the stored ones.
Their assigned charges are +1 and -1; these dimensionless assignments do not
supply a dimensional e, permittivity, mass or physical length.

These graphs belong to the prior selected-sector charging parent. Their
kinetic carriers are not silently identified with the eight-coordinate native
electron spinor. The audit concerns the electric Green operator alone.

## 2. What one electric bridge actually produces

As a declared extension, connect proton graph vertex a to electron graph
vertex b by one edge of conductance w>0. This electric edge is not assumed to
be identical to the original directed coefficient arrow.

For a neutral source rho=e_i-e_j, the exact effective resistance is

    R_pair(i,j)=R_p(i,a)+1/w+R_e(b,j).

This follows because the only bridge carries the full unit flux. Internal
fields minimize separately on the two sides; the bridge contributes 1/w.
The corresponding electric energy is

    E(i,j)=(beta/2)R_p(i,a)
          +(beta/2)R_e(b,j)+beta/(2w).

Every mixed difference vanishes:

    E(i,j)-E(i,0)-E(0,j)+E(0,0)=0.

Thus this finite electric term is a sum of independent endpoint costs and a
constant bridge cost. With independent source hopping its selected-sector
Hamiltonian remains separable. It supplies no spatial separation variable or
separated-particle continuum against which physical binding could be defined.
This does not prove that no richer parent can bind; it rejects obtaining a
Coulomb kernel merely by naming the one bridge a proton–electron connection.

Nine exact graph controls use three attachment choices and conductances
1/2,1,2. All 432 neutral sources satisfy Gauss law, the field-energy identity,
unit bridge flux and the resistance decomposition. Unit conductance copies the
parent's unit-edge convention; the other bridge conductances are explicit
controls, not secretly changed native internal weights.

## 3. What additional physics is actually required

The continuum branch supplies the following inputs independently:

| Input | Role |
|---|---|
| Relative Euclidean R3 and homogeneous isotropic Maxwell law | Select the spatial Green kernel |
| Positive permittivity epsilon | Set its normalization |
| Charges +e and -e | Select attractive electric interaction |
| Positive masses m_p,m_e | Select relative kinetic energy |
| hbar and physical time convention | Relate energy to phase evolution |
| Self-energy subtraction | Set the interaction reference at infinite separation |

The finite internal tetrahedron coordinates and mode disk do not supply a
translation-invariant relative R3, physical distance unit or continuum
Laplacian. Beta and eta in the retained charging parent are common fixture
coefficients, not values of epsilon, e or either mass.

In particular, a three-dimensional electromagnetic field is additional
energy-bearing content. It is not represented by one coefficient transfer
without an explicit compression and reconstruction contract.

## 4. Maxwell Green kernel and charge-density interaction

In the supplied continuum,

    -epsilon Delta G=delta,
    G(r)=1/(4pi epsilon r).

The checker verifies Delta(1/r)=0 away from the origin and the radius-independent
flux factor r² d(1/r)/dr=-1. With the Euclidean sphere area 4pi r², this fixes
the delta-source normalization.

After subtracting position-independent point-charge self energies, the cross
term is

    V(r)=q_p q_e G(r)=-kappa/r,
    kappa=e²/(4pi epsilon)>0.

Total field energy before subtraction is positive. Negative cross interaction
relative to separated particles does not contradict that positivity.
This is a density interaction, not a linear conversion of electron amplitude
into proton amplitude. It avoids the earlier central-symmetry obstruction to
scalar direct-sum mixing.

## 5. Relative kinetic law and internal Coulomb Hamiltonian

From supplied two-body masses, set

    M=m_p+m_e,
    mu=m_p m_e/M.

The centre-of-mass and relative gradient transformation gives

    H_total=-hbar²/(2M) Delta_COM + H_relative,
    H_relative=-A Delta_relative-kappa/r,
    A=hbar²/(2mu).

The cross derivative cancels exactly. Three rational controls check the
transformation independently. The orbital operator acts as the identity on
the retained electron doublet. The selected proton internal line is held fixed;
its physical spin and hyperfine coupling are not derived here.

The ground state below refers to the **relative internal Hamiltonian**. Free
centre-of-mass motion does not have a normalizable stationary ground on all
of R3. A centre-of-mass wavepacket can carry the bound internal state.

## 6. Exact ground state, not just a variational trial

Put

    b=kappa/(2A),
    a=1/b=hbar²/(mu kappa),
    E0=-A b²=-mu kappa²/(2hbar²).

The normalized ground orbital is

    phi(r)=(pi a³)^(-1/2) exp(-r/a).

Using Delta exp(-br)=(b²-2b/r)exp(-br),

    H_relative phi=[-A b²+(2Ab-kappa)/r]phi=E0 phi.

The remaining coefficient vanishes exactly. Its normalization follows from

    4 b³ integral_0^infinity r² exp(-2br)dr=1.

The lower bound follows by integration by parts:

    <psi,(H_relative-E0)psi>
       =A integral |grad psi+b rhat psi|² >=0.

The identity initially holds on suitable smooth functions and extends by
closure to the standard Coulomb quadratic-form domain. The orbital attains
it. Hence E0 is the true relative ground energy, not a fitted eigenvalue or
finite-grid estimate. The free scattering threshold is zero; every kappa>0
therefore gives a bound ground state.

The checker verifies the exact differential residual, normalization,

    <1/r>=1/a, <r>=3a/2,
    <T>=-E0, <V>=2E0,

and virial identity for three independently supplied mass/hbar/kappa controls.
No decimal integration, finite-domain boundary or experimental energy is used.

## 7. Retain the full electron potential realization

Every ground state has the form

    Psi(r)=phi(r) z,

where z is an arbitrary logical electron doublet, normalized when the full
state is normalized. The ground spin degeneracy is two. Because the orbital
is scalar and nonzero at finite r, it changes local norm but not the spinor's
Bloch ray, retained potential direction v or complex mode Gamma(v).

The native electron L,G,N intertwine its encoder exactly as before. The
existing proton-facing port is still an amplitude readout, not the Coulomb
mediator. The spinor–potential bridge reconstructs explicit ground-state
spinors in all 24 original fold interiors. The radius a is a relative orbital
length; v is an internal realization direction; Gamma(v) is an internal
complex mode. None is identified with the electrostatic potential V(r).

Unlike the earlier fixed-port attractive lattice model, Coulomb attraction is
spin-independent: bright and dark electron states bind at the same energy.
The internal potential folds are not different Coulomb energy levels.

## 8. Binding does not solve the original observation problem

For the arrow-dark direction d and i d, the potential direction, mode, norm
and link reading agree; the reading is zero. The internal phase witness differs.
Four exact phase controls verify that ambiguity after the continuum extension.
Spin-independent evolution multiplies both by the same ground phase, so no
additional spin information reaches the original arrow.

The stationary evolution is exp(-i E0 t/hbar)Psi. This uses the supplied
physical time/energy law, not the native assembly step count. Absolute phase
still needs a permitted reference to become observable.

## Verification and artifacts

    python research/voevodsky/checkers/check_source_gauss_to_coulomb_binding.py

Fresh checks and the frozen SCC challenge pass. Shared sources and receipts
are read-only.

SCC fingerprint:
`f94899162e4a6376dcc027877558ac56a59b87b3478f3eb1fc9b1eb90f2a1b01`.

- Contract: `inputs/source-gauss-to-coulomb-binding-v1.json`.
- Receipt: `results/source-gauss-to-coulomb-binding-v1.json`.
- Model: `scc-models/source-gauss-to-coulomb-binding-v1.json`.

## Disposition

The conditional physical-law continuation is complete at leading
nonrelativistic electric order. It is not a QED, magnetic, hyperfine,
relativistic or radiative calculation.

A source-derived physical binding claim is **not promoted**. It requires a
source-selected external field/relative kinetic layer and its dimensional
calibration. Replacing those inputs with familiar Maxwell and particle data
produces the familiar conditional ground state, but cannot establish that the
arrow construction independently predicts those data.
