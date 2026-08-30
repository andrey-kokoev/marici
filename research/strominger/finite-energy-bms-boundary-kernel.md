# Finite news energy admits the low kernel; stronger magnetic endpoint conditions may not

## 1. Radiative energy

Let the Bondi shear have one normalized spin-two harmonic component

\[
 C(u,\Omega)=c\,f(u)\,{}_2Y_{lm}(\Omega),
 \qquad N=\partial_u C.
\]

Its radiative energy is proportional to

\[
 E_{lm}=|c|^2\int_{-\infty}^{\infty}|f'(u)|^2du.
\]

For `f=(1+tanh u)/2`, the integral is `1/3`. Therefore every smooth
`l=2,3,4` kernel mode can be switched between two boundary values by a
finite-energy news history.

A time-independent kernel mode has `N=0` and costs zero news energy. Finite
energy controls the retarded-time derivative, not the absolute shear zero
mode. Such modes must be classified by boundary data and the soft symplectic
extension, not removed by the energy norm.

## 2. Weak radiative phase space

Under the weak conditions

- `N in L2(du dOmega)`;
- smooth angular shear at finite `u`;
- finite limits `C^plus/minus(Omega)` as `u -> plus/minus infinity`;

both electric and magnetic `l=2,3,4` kernel modes are kinematically admitted.
Antipodal matching transports them isomorphically and does not change their
energy.

Thus finite energy by itself does not prove the desired no-go. It leaves 21
real magnetic low modes in the kernel of the magnetic grade-three transport.

## 3. Strong endpoint policies

Many scattering phase spaces impose an additional no-magnetic endpoint
condition, equivalently the vanishing of the magnetic curl/dual mass aspect
at the ends of null infinity. Under that policy,

\[
 C^M_{lm}(u=plus/minus infinity)=0.

\]

It removes stationary magnetic kernel records at the endpoints, including
`l=2,3,4`. This is an extra boundary condition, not a consequence of finite
energy or of the grade-three operator.

Electric low modes have a different status. For `l>=2` they can be generated
by large supertranslations of the shear vacuum. Whether they are quotiented
as gauge or retained as soft-vacuum data depends on the declared observable
algebra. Ordinary small-gauge reduction does not silently remove them.

## 4. Histories versus endpoints

Even with zero magnetic endpoints, a compact-time magnetic pulse

\[
 C^M(u)=c\,\operatorname{sech}^2u\,{}_{2}Y^M_{lm}
\]

has finite news energy and lies pointwise in the angular grade-three kernel
for `l=2,3,4`. It returns to zero at both ends. Therefore:

- endpoint memory does not see it;
- an intermediate-time shear port does;
- the grade-three angular density does not;
- time-resolved news or energy ports detect the pulse.

The physical kernel depends on whether the readout acts on endpoint memory,
instantaneous shear, or the complete news history.

## 5. Boundary-policy classification

| policy/readout | magnetic low modes |
|---|---|
| finite news energy only | admitted |
| time-independent endpoint datum | zero energy; admitted weakly |
| no-magnetic endpoint condition | excluded at endpoints |
| zero endpoints but time-resolved histories | finite-energy pulses admitted |
| endpoint memory only | returning pulses invisible |
| news/energy history port | returning pulses visible |

Hence a source-authorized no-go must invoke both a constructor restriction and
a specified boundary/readout policy. Energy alone is insufficient.

## Evidence

`checkers/finite_energy_bms_boundary_kernel_checks.py` verifies exact finite
energies for transition and returning profiles, zero energy of stationary
modes, parity-sector counts, and the distinction between endpoint and
time-resolved ports.
