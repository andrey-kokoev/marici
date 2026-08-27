# Vacuum wait and sign swap are control-equivalent but not constructor-equivalent

Owner: `marici.Kitaev`

## Bounded question

Which is the better physical target for closing the electric fusion qutrit:
the intermediate `A_L/B_L` swap or the native vacuum-energy corridor?

## Verdict

Under signed continuous Hamiltonian control, either target closes the same
qutrit control algebra and makes the other compilable. They are therefore
control-equivalent relative to that ideal actuator model.

They are not constructor-equivalent. The vacuum corridor uses an already
native energy distinction but requires reversible fusion, calibrated dwell
time, and analog phase control. The sign swap is a discrete involution that
could avoid analog dwell calibration if realized exactly, but no microscopic
source operation currently supplies it.

For fastest information gain, attack the reversible vacuum corridor. For a
fully discrete protected compiler, continue searching for a source-derived
fixed bridge such as the sign swap.

## Vacuum-corridor route

The established coherent corridor has effective Hamiltonian

\[
H_V=\Delta(P_B+P_C)=\Delta(I-P_A).
\]

Its off-block incidence is

\[
\langle w_2|H_V|u\rangle
=
-\frac{\sqrt2}{3}\Delta.
\]

For nonzero `Delta`, the single-bridge lemma and continuously pulsed braid
Hamiltonians give `u(3)`.

At dwell time

\[
t_\pi=\frac{\pi}{\Delta},
\]

the logical unitary is

\[
e^{-it_\pi H_V}
=
P_A-P_B-P_C
=
-(I-2P_A).
\]

Up to global phase, the native vacuum wait directly gives the desired data
reflection. No intermediate sign permutation is needed for this gate.

## Sign-swap route

The canonical involution `S_AB` has off-block norm

\[
\frac{2\sqrt2}{3}
\]

and likewise closes `u(3)` under signed continuous pulses. It gives the same
reflection by the discrete word

\[
S_{AB}(I-2P_B)S_{AB}=I-2P_A.
\]

Here `I-2P_B` is native electric exchange. This route replaces calibrated
vacuum dwell by one exact intermediate-channel swap and two uses of it.

## Mutual compilation under the continuous model

Once either bridge is admitted as a signed continuous Hamiltonian together
with the braid controls, the dynamic Lie algebra is `u(3)`. Hence every qutrit
unitary generated directly by the other route is reachable.

This establishes equality of reachable groups:

```text
braid Hamiltonians + vacuum projector control
braid Hamiltonians + intermediate swap control
```

Both reach `U(3)` in the ideal driftless model.

It does not establish a uniform translation of physical costs. Lie
controllability can hide long pulse words, precision demands, sign reversal,
leakage, and different spacetime supports.

## Why constructor equivalence fails

The vacuum route requires:

- coherent motion or deformation that exposes pair charge locally;
- one native vacuum-versus-nonvacuum energy split;
- a calibrated phase integral;
- inverse deformation and rank-one environment return.

The sign-swap route requires:

- a neutral operation mixing two intermediate fusion channels;
- a frozen fusion-frame phase convention;
- possibly an auxiliary sign-line network;
- return of every auxiliary degree of freedom.

The fault surfaces differ. Timing drift changes the vacuum route continuously
while an exact discrete swap would instead have path, leakage, and frame
faults. Equal endpoint unitaries do not identify these instruments or their
counterfactual behavior.

## Direct target comparison

| Criterion | Vacuum corridor | Sign swap |
|---|---|---|
| Algebraic bridge | Exact | Exact |
| Native source ingredient | Vacuum energy term | Sign fusion rule only |
| Missing physical operation | Reversible fusion corridor | Intermediate-channel actuator |
| Data reflection | One calibrated wait | Swap-exchange-swap |
| Continuous `U(3)` closure | Yes | Yes |
| Exactly topological continuous family | No | Not applicable to one fixed gate |
| Main coherent fault | branch-dependent fusion garbage | auxiliary/path nonreturn |
| Main analog fault | dwell or gap error | pulse error if continuously driven |
| Controlled external incidence | Still missing | Still missing |

The vacuum route is closer to the frozen Hamiltonian. The sign route is the
cleaner discrete algebraic target.

## Programme decision

The next source calculation should depend on the claimed endpoint.

### If the objective is physical controllability

Construct the reversible fusion isometry, gap path, and environment return for
the native vacuum corridor. This uses the most source authority already
available.

### If the objective is a protected discrete compiler

Find one fixed bridge angle or exact channel permutation, then prove density or
finite synthesis separately. Arbitrary vacuum waiting is an analog resource
and cannot be called topological merely because the storage medium is.

### If the objective is the catalytic controlled phase

Neither internal route is enough. One must still couple the data predicate
coherently to the common qutrit bus or control the reflection through a path
pointer.

## Highest-information experiment

Prioritize the vacuum corridor because it has a native microscopic energy
term. Prepare pair-channel superpositions, execute fuse–wait–unfuse, and test:

1. leakage and channel mixing;
2. rank-one final environment Gram matrix;
3. phase linearity in the integrated gap;
4. closure of the storage geometry;
5. sensitivity to one local fusion-region fault.

A successful corridor establishes physical hybrid controllability. It does
not establish an exactly protected analog angle.

In parallel conceptually, retain `S_AB` as the hostile alternative: two
systems may have the same reachable `U(3)` while one has a native discrete swap
and the other only an analog vacuum pulse. Scalar and endpoint gate tomography
can identify them even though their constructor theories differ.

## Falsifiers

- The vacuum Hamiltonian has zero off-block bridge incidence.
- A `pi/Delta` wait fails to give the vacuum reflection up to global phase.
- Either continuously controlled route fails the single-bridge Lie theorem
  under its stated assumptions.
- Equal reachable group is promoted to equal pulse cost, locality, leakage, or
  fault behavior.
- Arbitrary vacuum waiting is called an exactly topological gate family.
- The sign swap is called source-native merely because its label permutation
  follows from fusion rules.
- Either internal bridge is claimed to supply controlled external incidence.

## Claim boundary

This packet compares two already derived conditional routes. It does not
construct either missing microscopic corridor, synthesize pulse sequences, or
prove a fault threshold.

Its new result is the equivalence boundary: vacuum wait and sign swap generate
the same ideal continuous control group, but they remain different physical
constructors with different source authority and fault surfaces.

No build, checker, or Git operation was used.
