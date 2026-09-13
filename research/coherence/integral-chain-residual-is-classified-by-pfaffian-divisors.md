# The integral chain residual is classified by Pfaffian divisors

## Principal Pfaffians

Let an integral chain have vertices \(0,\ldots,n-1\) and gap weights

\[
x_0,\ldots,x_{n-2}.
\]

For \(i<j\), write

\[
w(i,j)=\prod_{r=i}^{j-1}x_r.
\]

Choose any even subset

\[
S=\{i_1<\cdots<i_{2k}\}.
\]

The corresponding principal skew minor is itself an ordered chain, so its Pfaffian is

\[
\operatorname{Pf}M_S
=
\prod_{r=1}^{k}w(i_{2r-1},i_{2r}).
\]

## Pfaffian determinantal divisors

Define

\[
D_0=1,
\]

and

\[
D_k=
\gcd_{|S|=2k}
\left|
\prod_{r=1}^{k}w(i_{2r-1},i_{2r})
\right|.
\]

Then the alternating elementary divisors are

\[
d_k=D_k/D_{k-1}.
\]

They satisfy

\[
d_1\mid d_2\mid\cdots.
\]

The integral alternating normal form is

\[
H(d_1)\oplus\cdots\oplus H(d_m)
\oplus 0^{\,n\bmod2},
\qquad m=\lfloor n/2\rfloor.
\]

## Even terminal divisor

For \(n=2m\), there is only one full principal Pfaffian, hence

\[
D_m
=
\left|x_0x_2\cdots x_{2m-2}\right|.
\]

This is the absolute adjacent Pfaffian torsion. But its factorization among the individual \(d_k\) depends on gcd data from all smaller principal subchains.

## Odd residual

For \(n=2m+1\), the top divisor \(D_m\) is the gcd of the maximal Pfaffian cofactors. It measures the non-primitivity of the canonical integral null vector. Dividing the cofactor vector by this gcd gives the primitive generator of the free residual line, while \(D_m\) records its integral scaling defect.

Thus an odd integral residual contains both:

```text
primitive null line
cofactor divisibility scale
```

## Coefficient-sensitive target

The complete integral output is therefore not one scalar torsion. It consists of:

- the sequence of alternating elementary divisors \((d_1,\ldots,d_m)\);
- the free null line at odd size;
- its cofactor divisibility scale;
- ordered framing data if later localization must recover adjacent pairs.

After inverting all selected gaps, each \(d_k\) becomes a unit and the arithmetic cokernel disappears, leaving the framed localized hyperbolic decomposition.

## Verification

```text
python research/coherence/check_integral_chain_pfaffian_divisors.py
```

The checker enumerates every principal Pfaffian for 80 chains of sizes two through nine, verifies all divisor chains, and confirms the terminal even formula.

Artifacts:

- `check_integral_chain_pfaffian_divisors.py`
- `integral-chain-pfaffian-divisors.v1.json`
