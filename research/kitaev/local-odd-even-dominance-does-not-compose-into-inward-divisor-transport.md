# Local Odd-Even Dominance Does Not Compose into Inward Divisor Transport

The DPC proposes that source-forced odd-to-even coefficient dominance explains
inward divisor motion. The first hostile test is contextual: does a block that
moves an isolated zero inward retain that sign after composition with a
positive background?

For a differentiable family

\[
F_t(z)=F_0(z)+tG(z)
\]

and a simple zero \(z_0\) of \(F_0\),

\[
z'(0)=-\frac{G(z_0)}{F_0'(z_0)}.
\]

The added block controls the numerator. The pre-existing section controls the
denominator. Coefficient dominance inside \(G\) alone therefore cannot fix the
velocity sign unless the authorized state class also fixes the phase of
\(F_0'(z_0)\).

## Exact hostile fixture

Choose \(a>0\) with

\[
\cosh a=2
\]

and set \(z_0=a+i\pi\). The identities

\[
\cosh 2a=7,
\qquad
\cosh 3a=26,
\qquad
\cosh 4a=97
\]

and

\[
\sinh a=\sqrt3,
\qquad
\sinh 2a=4\sqrt3,
\qquad
\sinh 3a=15\sqrt3
\]

are exact.

Take the positive background

\[
F_0(z)=\cosh z+4\cosh 2z+\cosh 3z.
\]

At \(z_0\), shell parity gives

\[
F_0(z_0)=-2+4\cdot7-26=0,
\]

while

\[
F_0'(z_0)
=-\sqrt3+8(4\sqrt3)-3(15\sqrt3)
=-14\sqrt3.
\]

Now add the coefficient-dominant odd-to-even block

\[
G(z)=\cosh 3z+\cosh 4z.
\]

Its outer even coefficient equals its inner odd coefficient, so it satisfies
weak dominance. Yet

\[
G(z_0)=-26+97=71
\]

and hence

\[
z'(0)=\frac{71}{14\sqrt3}>0.
\]

Since \(\operatorname{Re}z_0=a>0\),

\[
\operatorname{Re}z_0\,
\operatorname{Re}z'(0)>0.
\]

The dominant block moves the zero outward.

## What is refuted

This refutes the context-free implication

\[
\text{odd-to-even coefficient dominance}
\Longrightarrow
\text{inward zero motion}.
\]

It does not yet refute a stronger source theorem that excludes the hostile
background. The DPC can survive only by proving that its complete authorized
state cone is invariant and supplies the missing denominator orientation.

The repaired conjecture needs a global condition such as

\[
\operatorname{Re}z\,
\operatorname{Re}
\left(-\frac{G(z)}{F'(z)}\right)<0
\]

for every authorized pair \((F,G)\), not merely a coefficient inequality on
\(G\). Equivalently, the source constructor must control the relative phase
between the block evaluation \(G(z)\) and the background transversality
\(F'(z)\).

## Deeper explanatory defect

The phrase “source-authorized constructor” is not independently falsifiable
until the source laws and admitted state cone are frozen. Without that freeze,
any hostile background can be excluded after the fact. A Deutschian
explanation must derive, before inspecting zero motion:

- the complete invariant cone of admissible backgrounds;
- the block action on that cone;
- the relative-phase or transversality law;
- a uniform completion margin;
- an independently checkable deformation that would break the law.

Local dominance is at most a numerator lemma. The missing explanation lives in
the numerator-denominator pairing.

## Falsifiers for the repaired DPC

- An authorized background with reversed \(F'(z)) phase.
- An authorized dominant block with outward velocity.
- Failure of the proposed admissible cone to remain invariant under block
  composition.
- A transversality margin tending to zero under completion.
- Defining authorization only after observing the velocity sign.

## Process calibration

Pre-objective: excitement 10/10, confidence 8/10, expected information gain
10/10. The aim was to test whether the proposed local explanatory variable is
closed under context.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Exact positive data reverse the velocity despite local block dominance;
the conjecture must control the full background-block phase relation.
