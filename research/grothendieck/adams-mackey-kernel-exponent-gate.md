# Adams--Mackey kernel-exponent gate

## Theorem

Let \(q:G\to H\) be a surjection of finite abelian groups with kernel \(K\).
The power map \([n]:g\mapsto ng\) induces Adams operations on the integral
group rings and pullback operations on coefficient functions.

The coefficient square

\[
q_![n]^*=[n]^*q_!
\]

and the dual Betti square

\[
\psi_G^n q^!=q^!\psi_H^n
\]

hold if and only if multiplication by \(n\) is bijective on \(K\). Equivalently,

\[
\boxed{\gcd(n,\exp K)=1.}
\]

Indeed, \([n]\) sends a fiber \(g_0+K\) onto \(ng_0+nK\), with each image
point counted \(|K[n]|\) times. It equals the target fiber \(ng_0+K\) with
unit multiplicity precisely when \(nK=K\) and \(K[n]=0\).

## Five-site consequence

Every nontrivial branch kernel in the five-site Kummer tower is
\((C_2)^r\), \(1\le r\le5\), and has exponent two. Therefore every branch
quotient retains exactly the odd Adams operations. Even operations fail both
the coefficient fiber-sum square and the Betti fiber-lift square.

This identifies one common source for two earlier obstructions:

- even Adams operations change the frozen coefficient selector; and
- even Adams operations fail to commute with the Mackey correspondence legs.

The maximal common algebraic survivor is the odd multiplicative monoid. It
is not additively closed and does not provide a semiring of physical
operations.

## Scope

The theorem is algebraic. The Betti fiber lift is the canonical finite-set
linearization, not the unavailable source-derived pushforward of physical
relative chains. No physical branch specialization, Witt construction, or
Euler product follows.

## Verification

`checkers/adams_mackey_kernel_exponent_gate.py` exhausts all cyclic quotients
\(C_N\to C_M\) with \(M\mid N\), \(N\le12\), and Adams indices through 12,
checking both coefficient and Betti squares on their complete bases.
