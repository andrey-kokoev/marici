# The emergent coherencer is a four-port controlled transducer

## Question

Is the cross-sector mixed-probe architecture literally transistor-like, and
what terminal has been hidden in the three-port description?

## Four operative roles

The more accurate abstraction has four ports:

1. **Source:** injects the state, excitation, or labelled source flag.
2. **Drain:** carries the selected observer/readout.
3. **Gate:** changes the admissible source-to-drain transfer law.
4. **Body:** fixes the reference frame, threshold, boundary conditions,
   reservoir, and completion topology relative to which gate action is typed.

The mixed carrier is the channel joining source and drain. The coherencer is
the source-authorized gate/body law controlling that channel. Its scalar
shadow is an output coefficient, current, interference record, or generalized
minor.

## Why the fourth port matters

A gate voltage is relational: it is defined relative to another terminal or
reference. Hiding that reference can make a three-port description appear
closed while silently fixing the threshold, orientation, or completion law.

In Marici terms, tying body to source may erase:

- seam and endpoint boundary currents;
- orientation anchors;
- calibration frames;
- completion margins;
- common-mode fault carriers;
- the distinction between coordinate change and executable context.

Thus a three-port diagram is valid only after a source-authorized reduction of
the body/reference port.

## Transistor criterion

A passive junction merely transports source to drain. A controlled transducer
requires an independently executable gate parameter (g) such that the
channel (T(g)) changes while source, drain, and body conditions are held
fixed. Infinitesimally, the gate response is

\[
A(g)=\frac{dT}{dg}T(g)^{-1}.
\]

For chamber coherence, (A(g)) must lie in the source-derived Lie wedge or
tangent cone that preserves the declared chamber. This is the analogue of a
transconductance law.

Calling the object an active transistor additionally requires an independent
power or free-energy supply and a gain theorem. Without those, the established
structure is a controlled modulator or gated scattering channel.

## Exact two-readout model

Let a body amplitude (b\ne0) and gate coordinate (q) produce

\[
y_+(b,q)=\frac{b(1+q)}2,
\qquad
y_-(b,q)=\frac{b(1-q)}2.
\]

The joint Jacobian with respect to (b) and (q) has determinant

\[
-\frac b2.
\]

Therefore two complementary readouts locally distinguish body amplitude from
gate position. The scalar sum

\[
y_++y_-=b
\]

forgets the gate completely. Repeating that scalar cannot restore the missing
rank.

This is the transistor version of the relational-observer result: channel
control is visible only through a readout family that retains complementary
ports.

## Current RH typing

The tentative correspondence is:

- source: the labelled theta/Tate source flag;
- drain: the selected observer flag;
- channel: the relative completed colligation;
- gate: a source-derived chamber-preserving transport generator;
- body: seam, endpoint, primitive, square, and archimedean boundary data
  together with the completion topology;
- output: the ordered generalized minor whose scalar shadow is the completed
  source-observer coefficient.

This is not yet a constructed transistor. The missing facts are precisely the
independent gate operation, its Lie-wedge law, lawful reduction of the body
port, and a completion-margin theorem. No gain or power theorem is currently
present.

## Cross-sector tests

- Flavor has a momentum-dependent transfer characteristic and a visible Higgs
  detector projection. Its even readout retains a simultaneous sign torsor, so
  an orientation/body reference remains missing.
- Optics demonstrates that temporal repetition of the same loop product is
  not an independent gate. A calibrated leakage port is required.
- Control theory supplies the correct test: perturb the gate independently and
  measure the response rank while holding the body conditions fixed.
- Topological computation shows that a rank-losing measurement cannot act as a
  full-state gate without an expanded carrier.
- Weak categorical transport requires higher composition laws: local gate
  intertwiners do not define a global device when their pentagon fails.

## DPC

A transistor interpretation passes only if the sector supplies:

1. four independently typed roles or an authorized reduction of one;
2. a mixed source-to-drain carrier;
3. an independently executable gate operation;
4. a gate-response law preserving the declared chamber;
5. a body/reference law fixing threshold and completion;
6. a jointly faithful readout family;
7. a fault model for gate, body, channel, and readout;
8. a power-supply and gain theorem if active amplification is claimed.

## Disposition

The transistor analogy survives as a four-port controlled-transducer DPC. RH
currently has a transistor-shaped diagram, not a constructed transistor. The
analogy becomes explanatory only if theta/Tate operations generate the gate
and body laws independently of the desired scalar nonvanishing.

