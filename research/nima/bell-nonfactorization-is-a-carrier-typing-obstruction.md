# Bell Nonfactorization Is a Carrier Typing Obstruction

## Question

Can the intuition that entangled photons are local handles to one relational closure be given a finite operational meaning that does more than rename a local hidden variable?

## Claim boundary

This packet establishes an exact finite typing separation in the two-setting, two-record Bell scenario. It does not derive quantum theory from Carrier, select an interpretation of measurement, or establish that every Carrier has quantum structure.

## Two candidate types

A locally compiled Carrier has a source variable \(\lambda\) and independently evaluable response laws at its two ports:

\[
p(A,B\mid x,y,\lambda)
=
p(A\mid x,\lambda)p(B\mid y,\lambda).
\]

Convex mixtures reduce to deterministic extreme strategies for the CHSH test. Each extreme strategy assigns four records

\[
A_0,A_1,B_0,B_1\in\{-1,+1\}.
\]

Its CHSH value is

\[
S=A_0B_0+A_0B_1+A_1B_0-A_1B_1,
\]

and satisfies \(|S|=2\). Hence every locally factorized mixture satisfies \(|S|\leq2\).

A relational Carrier instead exposes local ports of one joint context-indexed state--effect law. For the singlet correlations and the standard four axes, the correlators may be oriented as

\[
E_{00}=E_{01}=E_{10}=-\frac1{\sqrt2},
\qquad
E_{11}=\frac1{\sqrt2}.
\]

Then

\[
S=E_{00}+E_{01}+E_{10}-E_{11}=-2\sqrt2,
\qquad
S^2=8.
\]

The exact joint record law

\[
p(A,B\mid x,y)=\frac14\left(1+AB E_{xy}\right)
\]

is normalized and nonnegative. Summing over either remote record gives \(1/2\), independent of the remote setting. Thus nonfactorization does not supply a signalling channel.

## Carrier typing theorem

For this finite experiment, the following three requirements cannot coexist:

1. both ports are complete independently evaluable local response carriers;
2. the source is combined only by classical mixing;
3. the observed correlations have \(S^2=8\).

The relational state therefore cannot descend losslessly to two complete local response carriers. The photons may be treated as local handles only if the handled object remains irreducibly joint.

## Hostile rename test

Suppose a proposed closure \(C\) still supplies local responses \(A_x(C)\) and \(B_y(C)\), or mixtures of such responses, independently at both ports. Then it is exactly a Bell-local hidden-variable model regardless of the word “closure,” and the checker bounds it by \(|S|\leq2\).

The word contributes content only when the proposed interface is joint and context-indexed, while its local marginals remain no-signalling.

## What this buys Marici

The result gives the Carrier analogy a quantitative falsifier:

- endpoint values are not the whole state;
- source identity may persist as a joint continuation law;
- local handles need not support reconstruction of the handled object;
- an authorized joint readout can expose distinctions invisible to either local port;
- nonlocal correlation and operational signalling remain different types.

The next problem is compositional. Sequential or alternative measurement constructors must be represented without assigning simultaneous records to incompatible contexts. A successful extension needs an instrument-level continuation law, not merely the static table checked here.

## Verification

Run:

```text
python research/nima/checkers/check_bell_carrier_typing.py
```

The checker uses exact rational arithmetic in \(\mathbb Q(\sqrt2)\), enumerates all sixteen deterministic local strategies, verifies the quantum record table and no-signalling marginals, and executes the hostile rename test.
