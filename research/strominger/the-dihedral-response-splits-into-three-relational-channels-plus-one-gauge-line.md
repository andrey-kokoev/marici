# The Dihedral Response Splits into Three Relational Channels Plus One Gauge Line

## Correction

The title records the first Smith-level interpretation, but "splits" is too
strong. The gauge line is invariant; it does not have an invariant relational
complement. Passing to the three-dimensional relational quotient leaves a
rank-two response and one quotient-fixed direction whose lift shears into the
gauge line. The corrected object is a nonsplit filtered \(3+1\) packet. See the
subsequent gauge-shear packet.

## Result

Let \(R\in GL_4(\mathbb Z)\) be the reflection-label response matrix of the
explicit braid \(W_{\eta^2}\), and set

\[
\Delta=R-I_4.
\]

The determinantal divisors of \(\Delta\) are

\[
96,qquad
147456,qquad
2383937644045271040,qquad
0.
\]

Therefore the Smith invariant factors are

\[
96,qquad1536,qquad16167111843840,qquad0.
\]

The response has integral rank three.

## Meaning of the zero factor

Every row of \(\Delta\) sums to zero. Hence

\[
\Delta(1,1,1,1)^T=0.
\]

Simultaneously translating every reflection label changes the coordinate
origin on the polygon but no relative reflection geometry. The fourth Smith
factor is therefore a permanent gauge line, not an accidental loss of braid
information.

The reflection port consequently has a canonical \(3+1\) filtration:

- a three-dimensional relational quotient;
- one common-relabelling gauge channel.

It is not a canonical direct-sum decomposition.

No spacetime or chronological interpretation is involved.

## Exact kernel law over a finite modulus

Over \(\mathbb Z/n\), the kernel size is

\[
|\ker\Delta_n|
=n\,\gcd(n,96)\,\gcd(n,1536)\,
\gcd(n,16167111843840).
\]

The leading factor \(n\) is the permanent gauge line. The other three factors
measure arithmetic loss in the relational channels.

Total blindness means \(|\ker\Delta_n|=n^4\). Because 96 divides both later
nonzero Smith factors, this occurs exactly when

\[
n\mid96.
\]

Partial blindness has additional strata controlled by the larger factors. In
particular,

\[
1536=2^9\cdot3
\]

and

\[
16167111843840
=2^{13}\cdot3\cdot5\cdot19\cdot193\cdot35879.
\]

Thus moduli containing 5, 19, 193, or 35879 can affect only the deepest
relational invariant factor; they cannot create total blindness.

## Structural consequence

The scalar content 96 answers only whether every relational channel vanishes.
The Smith packet answers the stronger questions:

1. how many directions are invisible;
2. which invisibility is gauge and which is arithmetic;
3. how the kernel changes under a chosen finite observation modulus.

This is the invariant replacement for a census of individual finite groups.

## Replay

```powershell
uv run python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py
```
