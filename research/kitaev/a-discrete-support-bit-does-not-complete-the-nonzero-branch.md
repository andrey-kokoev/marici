# A Discrete Support Bit Does Not Complete the Nonzero Branch

Adjoin a bit (b\in\{0,1\}) to a complex coupling (z). If the bit is meant
to encode live support, the admissible hybrid space is

\[
X={(0,0)}
\cup
\{(z,1):z\ne0}.
\]

Give \(\mathbf C\times\{0,1\}\) the product metric

\[
d((z,b),(w,c))=|z-w|+|b-c|.
\]

Then (X) is not closed and therefore not complete. The Cauchy sequence

\[
x_N=(1/N,1)
\]

converges in the ambient product to

\[
x_\infty=(0,1),
\]

which is excluded by the live-support law. The completion of (X) necessarily
adds this labelled-zero state.

Thus a discrete bit by itself preserves the branch label but does not preserve
strict nonvanishing of the analytic coordinate.

## Two coherent repairs

There are exactly two immediate typing choices.

First, impose a uniform gap:

\[
X_\delta={(0,0)}
\cup
\{(z,1):|z|\ge\delta}.
\]

This is closed. The bit continues to mean live support, and the nonzero-branch
decoder can remain uniformly bounded if its other estimates are uniform.

Second, admit the completion point ((0,1)) and reinterpret the bit as
provenance or source-sheet memory rather than current nonvanishing. The laws
become

\[
b=0\Rightarrow z=0,
\]

while (b=1) permits both (z\ne0) and labelled zero. A compiler switching on
(b) must then define its branch-one decoder at (z=0); it may not invoke a
formula containing (1/z).

These repairs are not equivalent. The gapped model excludes amplitude escape.
The provenance model records which source branch approached the boundary but
does not repair the lost analytic inverse.

## Completion trilemma

For a hybrid support compiler, one must choose among:

- live-support semantics plus a uniform nonzero gap;
- provenance semantics plus admitted labelled-zero boundary states;
- an incomplete source domain on which completion invalidates the switching
  law.

There is no fourth option in which the product-topology bit remains a live
nonzero certificate while (z_N\to0) is admitted.

## Decoder consequence

Suppose the branch-one decoder has norm proportional to (1/|z|). Retaining
(b=1) along (z_N\to0) keeps the routing decision constant but leaves the
decoder norm divergent. Controller memory has detected the branch; it has not
repaired the analytic actuator. This is the same separation as classical
command redundancy versus quantum actuator failure.

## Relation to scalar defect ports

Grothendieck's scalar compressed-shift ceiling remains in force. Even a
provenance bit requires an admitted internal-state or matrix lift if it is to
be represented independently of the one incoming and one outgoing scalar
defect ports. The abstract hybrid completion supplies no such lift.

## Falsifiers

- Calling (X) complete while excluding ((0,1)).
- Treating a provenance bit as a lower bound on \(|z|\).
- Applying a branch-one inverse at an admitted labelled zero.
- Claiming the bit repairs a diverging analytic decoder norm.
- Adding labelled-zero states without specifying their consumer semantics.
- Housing the bit in a scalar model without source-derived internal typing.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to test whether the discrete-switch repair itself survives
completion.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. A discrete bit preserves provenance, not nonvanishing; live-support
semantics still requires a uniform analytic gap.
