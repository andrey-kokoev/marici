# Five-site integral Adams gate

## Algebraic positive result

The integral Betti deck lattice

\[
R=\mathbf Z[(C_2)^5]
\]

is the representation ring of the dual finite abelian group. Declaring each
group basis element to be a line element gives its canonical special
\(\lambda\)-ring structure. Its Adams operations are

\[
\psi^n(g)=g^n.
\]

They are ring endomorphisms and satisfy

\[
\psi^m\psi^n=\psi^{mn},
\qquad
\psi^p(x)\equiv x^p\pmod p.
\]

For \((C_2)^5\), every odd \(\psi^n\) is the identity and every even
\(\psi^n\) is induced by the collapse \(g\mapsto1\). Entry 1252's rank-one
absolute Frobenius is exactly the reduction modulo two of \(\psi^2\), not an
independent geometric Frobenius.

## Physical selection obstruction

On the dual coefficient function algebra, pullback along \(g\mapsto g^n\)
sends the identity delta function to

\[
(\psi^n)^*\delta_0=
\begin{cases}
\delta_0,&n\text{ odd},\\
1,&n\text{ even}.
\end{cases}
\]

Thus all odd Adams operations preserve the frozen sheet selection, while
every even operation changes 31 of its 32 values. The full algebraic
\(\lambda\)-ring does not descend to a physical readout \(\lambda\)-ring.

This refines the earlier prohibition: Adams operations do exist canonically
on the independently integral Betti group ring. What fails is their promotion
to one selection-compatible paired physical system.

## Scope

The integral deck lattice is independently supplied coefficient/Betti data,
not derived from the bare Carrier. No relative-chain pushforward, geometric
Frobenius, Witt-vector object, Euler product, or Phase-II promotion follows.

## Verification

`checkers/five_site_integral_adams_gate.py` verifies the ring-homomorphism
law on every basis product for \(1\le n\le12\), all Adams compositions in
that range, Frobenius congruences at \(p=2,3,5,7\), and the exact physical
selection mismatch count.
