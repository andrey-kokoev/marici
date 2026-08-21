# The RH defect is a trace on the conjugation graph correspondence

Let `D` be a finite conjugation-stable truncation of the Xi zero divisor and
let `J(rho)=conj(rho)`. Define the graph embedding

```
iota_J : D -> D x D,
iota_J(rho)=(rho,J rho).
```

For two spectral variables set

```
K(rho,sigma)
 = [((rho-1/2)+(sigma-1/2))/2]^2
   /[1+(rho-1/2)(sigma-1/2)].                          (1)
```

On the conjugation graph,

```
K(rho,J rho)
 = (Re(rho)-1/2)^2/[1+|rho-1/2|^2].                   (2)
```

If `P_Gamma` denotes the diagonal projection in `l^2(D x D)` onto the graph
of `J`, then the truncated reflection defect is exactly

```
H_D = Tr(P_Gamma M_K)
    = sum_(rho in D) K(rho,J rho).                     (3)
```

This is a correspondence trace, not a product trace. A doubled explicit
formula that produces

```
sum_(rho,sigma in D) K(rho,sigma)
```

does not recover (3): it lacks the graph projector matching each zero to its
canonical conjugate.

## Mackey pull--push normalization

Let

```
q : D -> D/<J>
```

be the orbit quotient. With pullback `q*` and fiber-sum pushforward `q_*`,

```
q_* q* = |q^(-1)(orbit)| I.                            (4)
```

For nonreal conjugate pairs every fiber has size two, hence

```
q_* q* = 2I,
||q* v||^2 = 2||v||^2.                                (5)
```

This is the precise `|ker q|`/orbit-size norm in the smallest `C_2` model.
If fixed points occur, fiber size is not constant and the norm becomes the
diagonal orbit-cardinality operator rather than a scalar. Any theorem must
state the freeness or fixed-point correction.

## Algebraic theorem versus physical availability

Equations (3)--(5) are finite-set Hilbert-space identities. They justify a
Mackey/correspondence formulation of the coefficient--Betti pairing. They do
not construct a physical relative-chain pushforward, nor do they show that
the prime-side explicit formula supplies `P_Gamma`. That missing graph
projector is now the concrete source-side obstruction.

## Falsifier

A proposed doubled source formula fails if it only factors into independent
one-variable traces. It must exhibit an operator implementing the
conjugation graph, and its pull--push composite must reproduce the orbit-size
normalization, including fixed-point corrections.

