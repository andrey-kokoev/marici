# The connected channel has an exact global Schatten-three coefficient lift

## Question

Can the connected prime determinant be realized by one canonical global
Schatten-three operator before the missing seam and boundary augmentation are
constructed?

Yes.  The prime coefficient lens supplies an exact diagonal realization.

## Prime coefficient operator

Let

\[
\mathcal H_{prime}=\ell^2(\{p:p\text{ prime}\})
\]

with basis `e_p`.  Define

\[
K_s e_p=p^{-s}e_p.
\]

For `sigma=Re s`,

\[
\|K_s\|_{\mathcal S_3}^3
=
\sum_p p^{-3\sigma}.
\]

Hence

\[
K_s\in\mathcal S_3
\quad\Longleftrightarrow\quad
\sigma>\frac13.
\]

On compact subsets of that half-plane, the family is analytic in Schatten
class three and locally bounded there.

## Exact determinant identity

For one eigenvalue `q=p^-s`,

\[
\det_3(I-q)
=
(1-q)e^{q+q^2/2}.
\]

Therefore

\[
\det_3(I-K_s)^{-1}
=
\prod_p
\frac{e^{-p^{-s}-p^{-2s}/2}}{1-p^{-s}}
=
C_+(s).
\]

This is exactly the connected grade-three Euler determinant.  Its logarithm
is the `k>=3` prime-power tower.  No scalar fitting or zeta continuation is
used.

The cutoff compression to primes `p<=X` reproduces the exact finite connected
factor `C_{+,X}`.  Cutoff inclusions are diagonal and operator-natural.

## Invertibility and zero law

For `sigma>0`,

\[
|p^{-s}|\le2^{-\sigma}<1.
\]

Thus

\[
\|(I-K_s)^{-1}\|
\le
\frac1{1-2^{-\sigma}}.
\]

On every compact subset of `Re s>0`, the inverse bound is uniform.  It follows
that `C_+(s)` is zero-free throughout its Schatten-three domain
`Re s>1/3`.

This is a genuine operator explanation of the connected channel's zero law:
its diagonal prime contraction cannot acquire eigenvalue one.

## Reciprocal sector

Define

\[
K_s^- e_p=p^{-(1-s)}e_p.
\]

Then

\[
K_s^-\in\mathcal S_3
\quad\text{when}\quad
\operatorname{Re}s<\frac23,
\]

and

\[
C_-(s)=\det_3(I-K_s^-)^{-1}
\]

is zero-free there.  Both coefficient lifts coexist in the open band

\[
\frac13<\operatorname{Re}s<\frac23,
\]

which contains the critical seam.

The two lifts are exchanged by `s -> 1-s`.  They form the exact connected
component of the paired-sector architecture.

## Consequences for the three-by-two model

The `C` coordinate is now stronger than a regularity label:

- it has a canonical global coefficient Hilbert space;
- it has a source-labelled analytic `S_3` operator family;
- its finite cutoff bonding is exact;
- its determinant frame is fixed;
- its inverse margin is explicit;
- its reciprocal sector is constructed.

Therefore the connected channel is not part of the remaining RH-bearing
obstruction.  Any off-seam completed zero must enter through:

- primitive boundary exponentiation;
- square boundary exponentiation;
- seam or archimedean incidence;
- coupling of those channels to the connected determinant;
- failure of determinant-line sewing or compact-open completion.

## Coefficient lift versus completed boundary realization

This result lives in the quantum coefficient lens: `H_prime` records the
labelled prime eigenvalues and their determinant.  It is not yet the physical
or boundary operator acting on the complete theta/Tate source carrier.

The missing comparison is

\[
\mathcal H_{prime}
\longrightarrow
\mathcal H_{boundary},
\]

with typed `P/Q`, seam, forcing, endpoint, and archimedean blocks.  That lift
must preserve `Tr K`, `Tr K^2`, `det_3`, reciprocal reflection, and cutoff
naturality.

Thus “global operator lift” must be qualified:

- global coefficient operator: established;
- completed boundary colligation: open.

## DPC update

The DPC no longer needs to conjecture existence or framing of `C`.  Its
load-bearing claim reduces to a two-boundary-channel augmentation around an
already controlled connected bulk:

```text
P and Q boundary packet
  + exact zero-free connected S3 determinant
  + seam and archimedean incidence
  -> framed completed sector denominator.
```

This is a substantial narrowing.  The odd exponential adversary is rejected
by the exact determinant identity, not by an added probe.

## Falsifiers

- Failure of the `S_3` norm criterion at a declared point.
- A cutoff determinant differing from the product of local connected factors.
- A nonzero eigenvalue-one witness for `K_s` with `Re s>0`.
- Reciprocal reflection failing to exchange `K_s` and `K_s^-`.
- Treating this coefficient lift as the missing seam/boundary colligation.
- A proposed boundary lift that changes the connected determinant or its
  first two trace deficits.

## Verdict

The connected grade is solved at the global coefficient-operator level.  It
is an exact, framed, zero-free Schatten-three determinant on both reciprocal
sectors around the critical seam.

The remaining compiler problem is no longer `P/Q/C`.  It is:

> attach the two exceptional boundary currents `P` and `Q`, together with
> seam and archimedean incidence, to an already completed and invertible
> connected bulk without losing its determinant frame or inverse margin.
