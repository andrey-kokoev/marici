# Transition absence is level-relative

## Bounded correction

The absent-transition trichotomy is meaningful only after fixing what counts as
a transition. Structural coupling, state-conditioned transfer, detection
probability, and physical record are different levels. Zero at one level need
not be zero at another.

## Four levels

Let \(P_A\) and \(P_B\) denote source and target sectors.

### Structural capability

For a linear constructor word \(T_w\), define

\[
C_w=P_BT_wP_A.
\]

The condition \(C_w\neq0\) means that some source vector in the declared sector
has a nonzero target component under that word. It does not mean that every
source state makes the transition.

### State-conditioned transfer

For a frozen source state \(\rho_A\) and channel \(\Phi_w\), define the target
packet

\[
\sigma_{B,w}=P_B\Phi_w(\rho_A)P_B.
\]

This packet can vanish even when \(C_w\neq0\), because the chosen source state
may lie in a dark subspace of the structural coupling.

### Effect probability

For a positive target effect \(E_B\), define

\[
p_w=\operatorname{Tr}(E_B\sigma_{B,w}).
\]

The probability can vanish because the state-conditioned target packet is zero
or because its support is orthogonal to the selected effect.

### Physical record

Let the instrument and detector map the effect value to a record

\[
y_w=R(p_w,\nu),
\]

where \(\nu\) contains independently typed noise, loss, threshold, and
instrument state. A zero or absent record can occur even when \(p_w>0\).

## Typed zero ladder

The implications run downward:

\[
C_w=0
\Longrightarrow
\sigma_{B,w}=0
\Longrightarrow
p_w=0.
\]

Their converses generally fail. The final implication

\[
p_w=0\Longrightarrow y_w=0
\]

depends on the record convention, while

\[
y_w=0\Longrightarrow p_w=0
\]

fails for thresholded or lossy detectors.

Therefore an endpoint statement of absence must name its level.

## Level-relative trichotomy

At each level, the three explanatory alternatives must be reformulated against
the complete packet and constructor family appropriate to that level.

### Record-hidden probability

\[
p_{w_0}>0,
\qquad
y_{w_0}=0.
\]

The detector or record map hides a positive effect value.

### Effect-hidden target packet

\[
\sigma_{B,w_0}\neq0,
\qquad
p_{w_0}=0.
\]

The selected effect is blind to a nonzero target packet. Another effect on the
same output can reveal it.

### State-dark structural capability

\[
C_{w_0}\neq0,
\qquad
\sigma_{B,w_0}=0.
\]

The word has structural capability, but the chosen source state does not use
it. Changing the source preparation changes the trial, not merely the readout.

### Route deficiency

At any frozen level, the current word has zero complete packet while another
authorized word has a nonzero packet at that same level.

### Structural prohibition

\[
P_B\mathcal A P_A=0.
\]

This is the strongest algebraic prohibition: no authorized word has even
structural source-to-target capability.

## Why positivity helps

When \(E_B\ge0\) and \(\sigma_{B,w}\ge0\),

\[
\operatorname{Tr}(E_B\sigma_{B,w})=0
\]

implies orthogonality of their supported positive components. There is no
signed scalar cancellation analogous to a trace of a general Hermitian
operator.

Thus a traceless nonzero operator is a valid witness for blindness of a linear
central functional, but it is not automatically a hidden positive detection
event. The coefficient and positivity type determines the interpretation of
zero.

## Polarizer typing

For ideal rank-one preparation and analysis,

\[
C_{w_0}=P_{\pi/2}P_0=0.
\]

The crossed-pair absence occurs already at structural capability. It is not a
detector-hidden probability or a state-dark use of a nonzero coupling.

After insertion,

\[
C_w=P_{\pi/2}P_\theta P_0\neq0.
\]

The constructor word changes and structural capability appears. Subsequent
loss can then reduce the positive effect probability, and a threshold can hide
the remaining probability at the record level. These are three different
failures in one apparatus.

## Coherence as latent route resource

A current packet can contain coherence outside the selected target population.
An additional constructor may rotate that coherence into the target effect.
Relative to the current effect it is hidden state information; relative to the
new word it becomes route-enabling input.

This does not collapse observation and construction into one operation. The
intermediate constructor consumes the latent packet and changes the route. A
nondisturbing tomographic effect and an active coherence rotation remain
different contexts.

## Finite decision order

For an absent physical record:

1. test detector and threshold faithfulness to decide whether \(p_{w_0}>0\);
2. use a jointly faithful effect family on the unchanged output to decide
   whether \(\sigma_{B,w_0}\neq0\);
3. vary source preparation only within an independently authorized family to
   decide whether \(C_{w_0}\neq0\);
4. if structural capability is zero, search the authorized constructor closure
   for another word;
5. certify structural prohibition only from complete closure or a preserved
   invariant.

Each step changes exactly one interface layer. Skipping levels makes the
explanation underdetermined.

## Deutschian consequence

A satisfactory explanation of an absent endpoint record must predict which
level changes under each criticism:

- detector replacement changes records while preserving effect probability;
- effect replacement changes observation while preserving the output packet;
- source preparation changes the trial while preserving the word;
- constructor insertion changes the route;
- a selection invariant survives every authorized word.

These interventions have incompatible footprints. That makes the alternatives
hard to vary once the levels are frozen.

## Falsifiers

- Calling a nonzero structural coupling an occurred transition for every source
  state.
- Calling a traceless Hermitian packet a hidden positive detection event without
  a positive state--effect pairing.
- Inferring zero probability from a missing thresholded record.
- Inferring structural prohibition from one dark source preparation.
- Treating source preparation, readout replacement, and constructor insertion
  as the same intervention.

## Claim boundary

This packet refines the finite linear trichotomy by adding quantum
state--effect and record typing. It does not supply a laboratory detector model
or prove nondisturbing access to a jointly faithful effect family.
