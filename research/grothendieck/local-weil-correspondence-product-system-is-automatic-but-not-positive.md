# The local Weil correspondence product system is automatic but does not explain positivity

## Target

The surviving proposal replaced compressed endomorphisms of one cell by location-indexed local Weil fibers and prime correspondences.

## Exact strict product system

Fix one short-support cell `I` and let `H_x` be its translate to `I+x`. On the test-function level, logarithmic translation gives

`U_a:H_x -> H_(x+a)`.

Translations satisfy exactly

`U_a U_b=U_(a+b)`.

Therefore prime correspondences

`E_p(x)=U_(log p):H_x -> H_(x+log p)`

already form a strict product system. Unique factorization gives path independence, and the mixed square closes:

`E_2(x+log3)E_3(x)=E_3(x+log2)E_2(x)=U_(log6)`.

No RH input is needed. The first two prior problems—composition and mixed-prime coherence—were artifacts of compressing every route back into one fixed cell.

## Where positivity reappears

Local positivity supplies a Hilbert norm on each `H_x`. To form one global Hilbert colimit, one must specify cross-fiber inner products. Requiring those pairings to equal the complete Weil cross form gives the kernel

`K((x,f),(y,g))=W(U_x f*(U_y g)*)`.

A Hilbert Kolmogorov completion exists exactly when every finite matrix of this kernel is positive semidefinite. Since finite sums of translated short-support functions exhaust the compact test algebra, this condition is exactly global Weil positivity.

Thus:

- algebraic product-system composition is automatic;
- mixed-prime path coherence is automatic;
- positive faithful colimit is equivalent to the original RH-bearing theorem.

Minimality and density do not prove positivity; they become meaningful only after the cross kernel is positive.

## Falsification of the explanatory claim

The product-system proposal does not solve all three problems by one deeper mechanism. It solves the first two kinematically and restates the third as positive-definiteness of the Weil kernel. Calling the resulting Kolmogorov space a dilation before proving positivity is circular.

A signed two-fiber kernel can have positive diagonal blocks and an overlarge cross block. Its translation paths still compose perfectly while its global Gram matrix has a negative direction. Hence exact product-system coherence has no implication toward the missing positivity.

## Surviving research direction

A nonredundant conjecture must add a source inequality that controls cross-fiber pairings by local energies. The sharp form is a complete block-kernel domination or Markov property whose consequence is positive-definiteness, not positive-definiteness itself under another name.

The first genuine gate remains the normalized two-cell contraction, followed by a global gluing theorem controlling cycles. Prime-two passes in the proved support-constrained complete gamma model; the next new inequality must involve a mixed-prime three- or four-cell block and cannot be replaced by path commutation.

## Disposition

The correspondence product system exists exactly, but it is not an RH explanation. The positive-colimit clause is equivalent to Weil positivity and is therefore removed as a conjectural mechanism. The next falsifiable target is a source-derived cross-fiber domination inequality stronger than local positivity and weaker than the full global conclusion.
