# The conjugation graph is a spectral copying correspondence

For a finite divisor `D`, let `H=l^2(D)` with atomic basis `e_rho` and
antiunitary conjugation `J e_rho=e_(conj rho)`. Define

```
C_J : H -> H tensor H,
C_J e_rho = e_rho tensor e_(conj rho).                 (1)
```

Then

```
C_J* C_J = I_H,
C_J C_J* = P_Gamma,                                   (2)
```

where `P_Gamma` is the orthogonal projection onto the conjugation-graph
subspace. Hence for a multiplication kernel `M_K` on `H tensor H`,

```
Tr_H(C_J* M_K C_J)
 = Tr_(H tensor H)(P_Gamma M_K)
 = sum_rho K(rho,conj rho).                            (3)
```

The RH reflection defect is obtained by inserting the previously defined
kernel `K`.

## Frobenius structure

The unreflected copy map `C e_rho=e_rho tensor e_rho`, together with its
adjoint multiplication, is the standard special commutative dagger-Frobenius
algebra of the atomic algebra `l^infinity(D)`. Equation (1) is its second leg
twisted by `J`.

This identifies the required source structure more precisely than “a
Hilbert space with conjugation.” One needs:

1. a normal spectral operator or commutative observable algebra;
2. its atomic/spectral copying correspondence;
3. a compatible real involution `J`; and
4. a trace compatible with pull--push.

## Why `J` alone is insufficient

The copy map depends on the distinguished atomic basis. An abstract Hilbert
space and antiunitary real structure admit many orthonormal bases related by
real unitaries, producing different diagonal subspaces in `H tensor H`.
Thus `J` does not canonically determine `P_Gamma`.

If a normal operator has simple discrete spectrum, its rank-one spectral
projections recover the atomic algebra and hence the copy map. With
multiplicities, the operator determines only higher-dimensional eigenspaces;
additional coefficient/Betti labels or a maximal abelian refinement are
needed. This is where the proposed paired system can carry genuine content.

## Relation to pull--push norms

The graph embedding is isometric, giving `C_J* C_J=I`. The factor two found
for the orbit quotient is a different correspondence: quotient pullback
repeats one orbit value on two points, so fiber-sum after pullback is `2I`.
Confusing the graph embedding with the orbit quotient produces the wrong
normalization.

## Physical limitation

These are finite spectral Hilbert-space identities. They do not supply a
physical relative-chain pushforward. A source-side theorem must construct
the dagger-Frobenius/copy structure from arithmetic or topology and verify
that its trace agrees with the Xi graph trace.

