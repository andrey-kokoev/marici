# Selection-preserving left inverses require symmetry-breaking lift data

## Weighted-transfer theorem

Let `q:G->H` be a finite surjection of degree `d>1` over characteristic-zero
coefficients. A fiberwise weighted transfer has the form

`T(f)(h)=sum_(g in q^-1(h)) w_g f(g)`.

The left-inverse condition `Tq^*=id` says that the weights in every fiber sum
to one. If `T` is invariant under right translation by `ker(q)`, the kernel
acts transitively on every fiber, so all weights in a fiber are equal. Hence
each weight is `1/d`.

On the identity selector, this gives

`T(delta_0,G)=(1/d)delta_0,H`,

not `delta_0,H`. Therefore no kernel-equivariant weighted left inverse
preserves frozen identity selection for a nontrivial quotient.

## Symmetry-breaking escape

Without kernel equivariance, choose a section `s:H->G` with `s(0)=0` and set

`T_s(f)(h)=f(s(h))`.

Then `T_s q^*=id` and `T_s delta_0,G=delta_0,H`. But the result changes under
kernel translation: the section distinguishes one lift in each fiber. Thus a
selection-preserving split requires extra lift/section data and breaks deck
symmetry.

## Exact C4 control

For `C4->C2`, the section choosing lifts `0,1` preserves delta and splits
pullback but fails translation by two. Uniform averaging is translation
invariant and splits pullback but sends delta to `(1/2,0)`.

## Scope

This identifies the missing algebraic resource as a symmetry-breaking section
or equivalent geometric lift datum. It does not assert that source geometry
provides one, and it does not construct the Betti chain transfer.
