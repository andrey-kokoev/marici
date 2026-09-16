# Nontrivial V-D couplings are character-diagonal on the multiplicity-free Fourier fiber

## Question

What form can a nontrivial presentation-edge action on the order-four Fourier fiber take while preserving quarter-turn equivariance?

## Claim boundary

On the finite boundary quotient where the four Fourier characters have multiplicity one, every equivariant linear coupling is uniquely diagonal in the four canonical character projectors. This classification does not choose the four coefficients from semilocal source data and does not extend unchanged when completion introduces repeated character multiplicities.

Let \(\mathfrak D_k\) carry \(\mathcal F_k^4=1\), and let

$$
P_\lambda
=
\frac14\sum_{a=0}^3\lambda^{-a}\mathcal F_k^a,
\qquad
\lambda\in\{1,-1,i,-i\}.
$$

The projectors are orthogonal, sum to the identity, and have rank one on the finite boundary quotient. Let

$$
T_{ij,k}:\mathfrak D_k\longrightarrow\mathfrak D_k
$$

be a prospective fiber action for a presentation edge. Quarter-turn equivariance requires

$$
\mathcal F_kT_{ij,k}=T_{ij,k}\mathcal F_k.
$$

Commutation implies that \(T_{ij,k}\) preserves every Fourier eigenspace. Since each eigenspace has multiplicity one, there are unique scalars \(t_{ij,k}(\lambda)\) such that

$$
T_{ij,k}
=
\sum_{\lambda\in\{1,-1,i,-i\}}
t_{ij,k}(\lambda)P_\lambda.
$$

Conversely, every operator of this form commutes with \(\mathcal F_k\). Thus the equivariant coupling problem reduces from an arbitrary endomorphism to four source-derived character coefficients per presentation edge.

Composition of presentation edges requires

$$
t_{i\ell,k}(\lambda)
=
t_{j\ell,k}(\lambda)t_{ij,k}(\lambda)
$$

for every \(i<j<\ell\) and every character \(\lambda\). An invertible coupling additionally requires

$$
t_{ij,k}(\lambda)\ne0
$$

for all four characters, with reverse coefficients

$$
t_{ji,k}(\lambda)=t_{ij,k}(\lambda)^{-1}.
$$

## Completion boundary

If completion introduces multiplicity greater than one in a character sector, the scalar coefficient is replaced by an endomorphism of that isotypic block. Fourier commutation alone then does not select a basis or a canonical coupling inside the block.

## Source-coefficient audit

A repository search found no packet assigning character coefficients \(t_{ij,k}(\lambda)\) to the six semilocal presentation edges. The retained observer coalgebra does contain nontrivial constructor actions that preserve each Fourier character. Its Adams-weighted endpoint map has source coefficient

$$
\rho_r(p,k)=\frac1r p^{-(r-1)k/2}
$$

and is natural in all four Fourier presentations. This proves that source-derived character-diagonal couplings exist for named Adams/endpoint constructors. It does not identify that constructor with any \(C_{ij}\), and the recorded norm \(|\rho_r(p,k)|\) alone does not determine four complex character coefficients.

Therefore the only coupling currently attached to every semilocal \(C_{ij}\) is the identity fiber action from the minimal product construction. Assigning a nonidentity diagonal action to a semilocal edge would be fitted without a new source interface.

## Disposition

The nontrivial quarter-turn-equivariant coupling problem has an exact finite classifier: four character coefficients for each \(V\)-edge, subject to pointwise tetrahedral composition and nonvanishing for reversibility. No source packet currently supplies those coefficients for the semilocal edges. Nontrivial coefficients are constructed only for separately named observer-coalgebra generators.