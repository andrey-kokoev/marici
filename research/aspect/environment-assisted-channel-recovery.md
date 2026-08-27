# Environment-assisted recovery is a larger optical instrument

## Reduced collapse and joint reversibility coexist

Model polarization as a qubit and loss as amplitude transfer into a retained
environment mode. At complete damping, the dilation acts on the occupied input
port as

```text
|0,0> -> |0,0>
|1,0> -> |0,1>.
```

Consequently every reduced system output is `|0><0|`. System-only tomography
correctly reports a constant channel with no inverse. Nevertheless the joint
output retains the entire input superposition in the environment port, and the
inverse unitary restores it exactly.

This is not a contradiction and not an improved estimator. Opening the
environment port changes the admitted instrument from a reduced channel to a
unitary dilation.

## Rank is not enough: retain a control margin

For a rational partial-transfer pilot with field amplitudes `3/5` and `4/5`,
the damping probability is `16/25`. The reduced Bloch action contracts its
least-sensitive direction by `9/25`, giving inverse gain `25/9`. The joint
unitary still has singular values equal to one.

Thus an operational equivalence should preserve at least:

- the typed set of accessible ports;
- future-context action on those ports;
- the smallest actionable singular value, or reconstruction margin;
- whether recovery is a physical operation on the admitted state domain.

Two records can agree on the reduced detector while differing completely in
recoverability because one instrument retained a coherent environment mode.

## Optical realization

A path or time-bin mode can serve as the environment. A calibrated beamsplitter
couples polarization occupation into that mode. Discarding the auxiliary port
implements the reduced damping channel; coherently collecting both ports and
applying the inverse interferometer implements dilation recovery. Visibility,
phase stability, and mode overlap then become measured reconstruction margins.

The experimentally decisive comparison is therefore not numerical inversion
of reduced tomography. It is a controlled intervention: discard versus retain
the auxiliary port, followed by the same spanning polarization probes.

## Claim boundary

The checker uses an ideal two-qubit dilation, perfect coherent access, and exact
state vectors. Finite visibility, uncontrolled environment dimension,
detector loss, and irreversible thermalization remain open.

## Verification

```text
python research/aspect/checkers/check_environment_assisted_channel_recovery.py
```
