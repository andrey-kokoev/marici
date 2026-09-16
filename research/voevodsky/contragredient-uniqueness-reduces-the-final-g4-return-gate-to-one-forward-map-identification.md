# Contragredient uniqueness reduces the final G4 return gate to one forward-map identification

## Question

Must the arithmetic reciprocal/linking return be independently identified after the pair-to-bordered radial crossing is constructed, or is it forced by the forward crossing and the declared contragredient pairing?

## Claim boundary

It is forced once the forward G4 map is identified with the constructed pair-to-bordered crossing on nondegenerate declared pairings. Thus the final external gate reduces to one forward-map equality; no separate return coefficient or adjoint choice remains. The forward equality itself is still not exposed by the current Aspect contract and is RH-bearing through its consequence.

## Declared variance

The v3/v4 interface declares dagger as contragredient transpose on each named pairing, not as an arbitrary Hilbert adjoint. Let

$$
\langle-,-\rangle_P:
P^\vee\times P\to\mathbb C
$$

and

$$
\langle-,-\rangle_B:
B^\vee\times B\to\mathbb C
$$

be the nondegenerate pairings on the ordered-pair source and bordered radial target.

For a continuous forward map

$$
T:P\to B,
$$

its contragredient is defined by

$$
\langle T^\top\beta,x\rangle_P
=
\langle\beta,Tx\rangle_B
$$

for every \(x\in P\), \(\beta\in B^\vee\).

## Uniqueness

Suppose \(N_1,N_2:B^\vee\to P^\vee\) both satisfy the transpose identity. Then

$$
\langle(N_1-N_2)\beta,x\rangle_P=0
$$

for every \(x\). Nondegeneracy of the source pairing implies

$$
(N_1-N_2)\beta=0.
$$

Hence

$$
\boxed{N_1=N_2=T^\top.}
$$

There is no independent block-unitary or scalar freedom in the return.

## Application to the constructed crossing

Let

$$
T_{\rm PB}
=\mathcal T_{\rm pair\to border}
$$

be the constructed analytic-transpose crossing. Its bordered readout is

$$
\mathcal J_{\rm RL}T_{\rm PB}=R+2E.
$$

If the G4 forward arithmetic/radial incidence map \(U_{\rm G4}\) is identified by a source square as

$$
\boxed{U_{\rm G4}=T_{\rm PB},}
$$

then the declared return is automatically

$$
U_{\rm G4}^\top=T_{\rm PB}^\top.
$$

Pairing this return against the unchanged Evans state produces the same bordered section. A second declaration

$$
I^{({\rm recip})}+I^{({\rm link})}=R+2E
$$

would be redundant once the forward equality and pairings are fixed.

## Hermitian lane

On a Hilbert rung with the declared Real comparison, the same argument gives

$$
U_{\rm G4}^*=T_{\rm PB}^*.
$$

This does not identify analytic transpose with Hilbert adjoint across different rungs. Each is uniquely forced only within its own declared pairing.

## Exact external acceptance test

The G4 owner need expose only:

1. the forward map \(U_{\rm G4}:P\to B\);
2. its source and target pairings;
3. a source-derived equality or commuting square identifying \(U_{\rm G4}=T_{\rm PB}\);
4. confirmation that the Evans lower row uses the declared contragredient.

Then return equality is a theorem by uniqueness, and every shell/jet cancellation follows from radial Stokes.

## Why this is not a proof from typing

Current Aspect contract `polarized-pair-to-bordered-radial-crossing.v1` states that no authoritative arithmetic-adjoint target map is exposed. Without a named \(U_{\rm G4}\), the equality above cannot be tested. Defining \(U_{\rm G4}\) to equal \(T_{\rm PB}\) solely because its transpose cancels the Evans residual would remain circular.

## Disposition

The final G4 comparison has only one independent external datum: identify the authoritative forward arithmetic/radial incidence with the constructed pair-to-bordered crossing. Contragredient uniqueness then forces the reciprocal/linking return and removes every residual normalization choice. The current contract does not expose that forward map, so owner action remains necessary.