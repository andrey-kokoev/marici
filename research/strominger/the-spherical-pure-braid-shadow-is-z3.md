# The Spherical Pure-Braid Shadow Is Z3

## Question

Does the local pure-braid hostile survive after the four-zero configuration is
globalized from a disk chart to the celestial sphere?

## Spherical braid abelianization

The spherical braid group \(B_4(S^2)\) has the ordinary Artin relations and
the additional sphere relation

\[
\sigma_1\sigma_2\sigma_3^2\sigma_2\sigma_1=1.
\]

After abelianization, the braid relations identify all three generators. The
sphere relation has exponent six. Hence

\[
B_4(S^2)_{\mathrm{ab}}\cong\mathbb Z/6.
\]

The Smith normal form of the abelian relation matrix is \((1,1,6)\).

## Endpoint-invisible residue

The sign of the endpoint permutation is exponent reduction modulo two. Pure
endpoint paths therefore land in the even subgroup

\[
\{0,2,4\}\subset\mathbb Z/6,
\]

which is canonically \(\mathbb Z/3\). The class of \(\sigma_1^2\) is its
generator, so the smallest local hostile remains nontrivial after spherical
globalization.

Thus endpoint relabeling and the static \(A_3\) packet miss a three-valued
global abelian coherence residue.

## What this does not prove

The \(\mathbb Z/3\) port is not faithful on the spherical pure braid group.
Three copies of \(\sigma_1^2\) vanish in this abelian quotient without thereby
being proved trivial as a braid. Full coherence still requires a nonabelian
`BraidWitness` or a source representation with a demonstrated kernel.

The numerical three is not identified with the three \(A_3\) coordinates or
with any three ports in the \(3+2+1\) instrument. Those objects have different
types: static redistribution directions versus a path-coherence residue.

## Prediction

A globally coherent four-zero selector needs, at minimum, an additional
ternary path port detecting the even exponent class modulo six. Passing that
port still does not certify full pure-braid coherence.

## Disposition

The local braid obstruction survives globally and acquires a finite first
readout: the endpoint-invisible abelian shadow is \(\mathbb Z/3\).

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/spherical_pure_braid_z3_residue_checks.py
```
