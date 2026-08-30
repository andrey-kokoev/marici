# RS-2: the canonical \(C_3\) Tate bridge exists

## Operator forecast

Before construction, Operator reported sensing that a canonical map exists
between the cosmological marked-Cut norm-homology line and the string
road/contact order-three extension. This was a prospective intuition, not a
mathematical argument.

## Two presentations of one coinvariant line

Let

\[
I_{\mathbb Z}=\ker(\epsilon:\mathbb Z[C_3]\to\mathbb Z)
\]

and \(I_{\mathbb F_3}=I_{\mathbb Z}\otimes\mathbb F_3\). In characteristic
three, writing \(x=g-1\),

\[
\mathbb F_3[C_3]\cong\mathbb F_3[x]/(x^3),
\qquad
N=1+g+g^2=x^2.
\]

Therefore

\[
\ker N=I_{\mathbb F_3},
\qquad
\operatorname{im}N=(g-1)I_{\mathbb F_3},
\]

and the marked-Cut syndrome is

\[
\boxed{
H(N)\cong
I_{\mathbb F_3}/(g-1)I_{\mathbb F_3}.
}
\]

For the integral road extension, the cyclic cohomology calculation gives

\[
\boxed{
H^1(C_3,I_{\mathbb Z})
\cong
I_{\mathbb Z}/(g-1)I_{\mathbb Z}
\cong\mathbb Z/3.
}
\]

The second equality follows from the Smith invariants \((1,3)\) of \(g-1\)
on the integral augmentation ideal.

Reduction modulo three identifies these quotient presentations. Equivalently,
the integral quotient is already killed by three, so

\[
\boxed{
\tau_{\rm Tate}:
H(N)\xrightarrow{\sim}
H^1(C_3,I_{\mathbb Z})
}
\]

is forced by the augmentation-ideal coinvariant construction.

## Canonicity under reflection

Choose \(a=e_1-e_0\), \(b=e_2-e_1\) only to audit the map. The relation in
both quotients is \(b=a\). Reflection \(s:g\mapsto g^{-1}\) sends

\[
a\longmapsto a+b\equiv2a=-a\pmod3.
\]

Thus both sides carry the same odd reflection character. Rotation is trivial
on coinvariants. The bridge is consequently \(D_3\)-equivariant; it is not an
arbitrary isomorphism between one-dimensional vector spaces.

## What has and has not been unified

This establishes a canonical comparison of the *one-orbit marked-Cut
syndrome line* with the *road/contact extension line*. Combined with
occurrence forgetting,

\[
H(N_{\rm two\ occurrences})
\xrightarrow{\bar F}
H(N_{\rm marked\ Cut})
\xrightarrow{\tau_{\rm Tate}}
H^1(C_3,I_{\mathbb Z}),
\]

we now have a source-normalized rank-one cross-sector coefficient bridge.

It does not identify the cosmological and string carriers, periods, or
physical observables. The scalar cosmological period still kills the syndrome.
What is shared is the integral \(C_3\) trace/augmentation calculus and its
canonical order-three coinvariant.

## Next falsifier

Transport \(\tau_{\rm Tate}\) through the actual sector-specific connection
or localization maps. It must commute with the marked-Cut transition on the
cosmology side and the filtered road recollement on the string side. Failure
would confine the bridge to a frozen algebraic fiber; success would establish
the first cross-sector natural transformation between coefficient lenses.

## Durable evidence

- Entries 356, 410, 436, 1552, and 1553;
- research/nima/checkers/check_rs2_canonical_c3_tate_bridge.py;
- research/nima/results/rs2-canonical-c3-tate-bridge.json.
