# The residual sewing phase is gauge for an isolated antiunitary reciprocal pair

## Scope

Chain-compatible Krein sewing is rigid up to a phase. Whether that phase is physical depends on the type of reciprocal operation. For an isolated two-sheet reciprocal pair, reflection is naturally antiunitary. In that case the phase is removable by a boundary-frame rephasing and is not an additional constructor invariant.

Let

\[
M_+=I
\]

for chain-preserving reflection and

\[
M_-=
\operatorname{diag}(1,-1)
\]

for chain-reversing reflection.

Let \(C\) denote coefficientwise complex conjugation.

## Antiunitary sewing

The general reciprocal sewing has the form

\[
R_\theta=e^{i\theta}M_\pm C.
\]

Because \(M_\pm\) is real and \(M_\pm^2=I\),

\[
R_\theta^2
=
e^{i\theta}M_\pm C
e^{i\theta}M_\pm C
=
e^{i\theta}e^{-i\theta}M_\pm^2
=
I.
\]

Thus involutivity does not restrict \(\theta\).

Likewise, antiunitary preservation of the real Krein matrix \(J\) holds for every phase. Reality alone therefore does not reduce the phase to \(\pm1\).

## Rephasing gauge

Change the boundary coefficient frame by

\[
T_\phi=e^{i\phi}I.
\]

For an antiunitary map,

\[
T_\phi R_\theta T_\phi^{-1}
=
e^{i(\theta+2\phi)}M_\pm C.
\]

Choosing

\[
\phi=-\frac{\theta}{2}
\]

sets the phase to zero. Hence every \(R_\theta\) is gauge-equivalent to

\[
R_0=M_\pm C.
\]

On an isolated reciprocal pair, the continuous sewing phase carries no gauge-invariant information.

## When the phase becomes observable

The rephasing ceases to be free if another source constructor fixes the boundary frame. Examples include:

- a determinant-line trivialization;
- a Wronskian normalization relative to a bulk basis;
- a causal-history port with a declared phase;
- an Euler current whose coefficient frame is independently frozen;
- or a cycle of several sewing maps whose total phase holonomy cannot be removed simultaneously.

In those cases the invariant is not the phase of one edge. It is a relative phase or cycle holonomy.

## Categorical interpretation

A single antiunitary edge has a phase coboundary:

\[
\theta\longmapsto\theta+2\phi.
\]

Only a closed constructor loop can retain a gauge-invariant phase class. Therefore the local wall cell should be strictified to the canonical sewing

\[
R_0=M_\pm C
\]

until an external source port supplies a relative phase frame.

This avoids fitting a local phase to reproduce the desired Euler odd sign.

## Remaining binary choice

After removing the phase, one genuine local choice remains:

\[
M_+=I
\]

or

\[
M_-=\operatorname{diag}(1,-1).
\]

This is the chain-orientation bit: reciprocal reflection either preserves or reverses the incidence arrow.

It must be fixed by the source reflection law for the derivative/history constructor. Unlike the phase, it cannot be removed by scalar rephasing.

## Completion consequence

Canonical antiunitary sewing has norm one and is cutoff independent:

\[
\|R_0x\|=\|x\|.
\]

It introduces no metric amplification. Any completion phase defect must arise from incompatible frame choices around a larger constructor cycle, not from one isolated reciprocal wall pair.

## Result

For an isolated reciprocal boundary pair,

\[
R_\theta=e^{i\theta}M_\pm C
\]

is gauge-equivalent to

\[
R_0=M_\pm C.
\]

The local sewing problem has therefore contracted from one phase plus one bit to one genuine bit. The next source calculation is the reflection covariance of the derivative incidence, which decides whether \(M_+\) or \(M_-\) is authorized.
