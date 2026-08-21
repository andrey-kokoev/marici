# Selector-admissible resonance lattice

## Combined theorem

Let `G` be finite, let `c:G->R` be a frozen coefficient selector, and put

`S=Stab_R(c)={s in G : c(gs)=c(g) for every g in G}`.

The coefficient-admissible quotient kernels form the down-set

`L_c={K normal in G : K subset S}`.

For `K` in `L_c`, let

`A_K=im(G -> Aut(K))`

be the conjugation image and decorate `K` by

`R(K)=rad(exp(K) exp(A_K))`.

Then the basis-level power--Mackey operations compatible with both the
selector and the quotient `G->G/K` are exactly

`U(K)={n>=1 : gcd(n,R(K))=1}`.

If `K_1 subset K_2` in `L_c`, then

`R(K_1) | R(K_2)` and hence `U(K_2) subset U(K_1)`.

Thus selector admission is downward closed, while the compatible operation
system is contravariantly monotone along kernel inclusion.

## Proof of monotonicity

Because `K_1` is a subgroup of `K_2`, `exp(K_1)` divides `exp(K_2)`.
Both kernels are normal in `G`, so conjugation preserves each. Restricting a
conjugation automorphism of `K_2` to `K_1` gives a surjection

`A_{K_2} -> A_{K_1}`.

It is well-defined because any element of `G` acting trivially on `K_2`
acts trivially on `K_1`, and it is surjective by the definitions of the two
images. Therefore `exp(A_{K_1})` divides `exp(A_{K_2})`. Taking radicals
proves the claimed divisibility.

## Five-site specialization

For `G=(C2)^5`, conjugation is trivial. The identity kernel has label `1`;
every nontrivial kernel has label `2`. Consequently:

- `delta_0` admits only the identity kernel and all positive indices;
- a selector with hyperplane stabilizer admits every subspace kernel in that
  hyperplane; its identity quotient admits all indices and each nontrivial
  quotient admits precisely the odd indices;
- the constant trace admits the full subspace lattice with the same labels,
  but it is a different observable.

This resolves an apparent tension: the frozen five-site selector has no
nontrivial quotient at all, not an odd-index family of physical quotients.
Odd indices appear only after a separately admitted selector allows a
nontrivial kernel.

## Falsifier and scope

An algebraic falsifier would be normal kernels `K_1 subset K_2` for which a
prime divides `R(K_1)` but not `R(K_2)`. The restriction-surjection proof
rules this out under the stated finite-group definitions.

The theorem remains coefficient-side. It supplies neither a specialization
map on relative chains nor boundary covariance, orientation, multiplicity,
or a physical pairing. No algebraic lattice label authorizes those missing
Betti data.
