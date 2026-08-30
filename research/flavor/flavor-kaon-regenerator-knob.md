# Executable neutral-kaon regenerator knob (WP406)

## Physical construction

WP406 replaces the hypothetical WP400 context with a historical flavor
operation. A physical $K^0$--$\bar K^0$ beam crosses a regenerator of fixed
composition and momentum. The controlled material column density is the knob.
Coherent forward scattering distinguishes the two flavor states and regenerates
a $K_S$ component from an incident $K_L$ beam.

For scattering-center density $n$, write the forward-amplitude difference as
$a+ib$. In the $(K_L,K_S)$ basis the off-diagonal matter term is

\[
\rho(n)=n(a+ib).
\]

The same density setting therefore changes both the dispersive shift $na$ and
the absorptive shift $nb$. Their unit-density calibration Jacobian with respect
to $(a,b)$ is the identity. Tagged-kaon interference measures the coherent
phase, while transmission or total-cross-section information constrains the
absorptive part. These are complementary readouts of one source-generated
complex amplitude, not two fitted projectors.

Neutral-kaon regeneration and its forward amplitude have been measured in
carbon using tagged $K^0$ and $\bar K^0$ interference. KLOE also observed
regeneration peaks in physical beam-pipe and drift-chamber materials. See the
[CPLEAR measurement](https://doi.org/10.1016/S0370-2693(97)01193-3), the
[CERN record for arbitrary coherent-state regeneration](https://cds.cern.ch/record/406476),
and the [dispersion analysis](https://arxiv.org/abs/hep-ex/9905007).

## Exact finite-thickness law

Let $\lambda_j=m_j-i\Gamma_j/2$, $\mu=(\lambda_L+\lambda_S)/2$,
$\delta=(\lambda_L-\lambda_S)/2$, and
$\Omega=(\delta^2+\rho^2)^{1/2}$. A homogeneous slab of traversal time $\tau$
has exact regeneration amplitude

\[
U_{SL}=-i e^{-i\mu\tau}\frac{\rho}{\Omega}\sin(\Omega\tau).
\]

This includes both physical decay widths and all repeated coherent interactions
within the frozen homogeneous two-state model. The finite-thickness response is
nonlinear even though the source shift is affine, so a linear extrapolation is
not substituted for the exact transfer law.

## Completion and withheld test

The first nonlinear source completion is

\[
\rho(n)=n(a+ib)+n^2(q_R+iq_I).
\]

Vacuum, unit-density, and double-density phase/attenuation calibrations have an
exact nonzero design determinant and can test $q_R=q_I=0$. A second material
component adds $n_2(a_2+ib_2)$ and is separately identifiable precisely when
$ab_2-a_2b\ne0$. This states the extra-mediator analogue rather than silently
absorbing it into the original amplitude.

After freezing $(a,b)$, both quadratic coefficients, the material composition,
the kaon mass and width packet, momentum, and slab geometry, the triple-density
regeneration amplitude is withheld. The checker supplies its exact symbolic
value for the declared benchmark. A discrepancy rejects this material-transfer
packet without refitting.

## Scope

This is a genuine relational flavor experiment over the stabilizer groupoid of
the prepared beam, regenerator composition, momentum, and detector convention.
It does not reveal an absolute phase and it is not a selector of the quark
`physical16` quotient. It establishes that flavor physics contains a real
source-generated, executable knob architecture of the required causal type.

The remaining empirical step is narrower: assemble phase and attenuation data
for one common material and momentum into the declared calibration, reserve a
third column density, and compare its regenerated displacement without
refitting.

Run `uv run --with sympy python
research/flavor/checkers/wp406_kaon_regenerator_knob.py` to regenerate the JSON
result.
