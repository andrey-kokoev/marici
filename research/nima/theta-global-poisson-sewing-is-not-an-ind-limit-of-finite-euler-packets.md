# Global Poisson sewing is not an Ind-limit of finite Euler packets

## The restricted-product obstruction

The adelic Tate source is a restricted tensor product with a distinguished
unramified vector at almost every finite prime:

\[
\mathbf 1_{\mathbb Z_p}.
\]

Its local zeta integral produces

\[
(1-p^{-s})^{-1}.
\]

A finite Euler product

\[
E_X(s)
=
\prod_{p\in X}(1-p^{-s})^{-1}
\]

sets every omitted local factor to \(1\). At one prime this may be represented
by replacing the unramified vector with a unit-supported vector such as

\[
\mathbf 1_{\mathbb Z_p^\times}.
\]

But a finite set \(X\) omits infinitely many primes. Producing \(E_X\) from
the global source would therefore change the distinguished vector at
infinitely many places. The result is not an object of the original
restricted tensor product.

## Categorical consequence

Finite Euler packets do not form a cofinal diagram of admissible adelic source
objects whose colimit is the global Tate source.

There is a scalar diagnostic projection

\[
\text{global arithmetic expression}
\rightsquigarrow
E_X(s),
\]

but there is no corresponding source-authorized truncation functor that
commutes with global Fourier–Poisson sewing.

Therefore the square

\[
\begin{matrix}
\text{adelic source}&\longrightarrow&\text{Poisson-sewn source}\\
\downarrow&&\downarrow\\
\text{finite Euler packet}&\longrightarrow&\text{finite sewn packet}
\end{matrix}
\]

is not merely unproved. Its lower source arrow is not defined in the same
category.

## Archimedean action is separate

At finite analytic cutoff, the archimedean prefactor contributes an
independent determinant line

\[
\mathcal L_\infty(s).
\]

It tensors with the finite arithmetic determinant line:

\[
\mathcal L_X^{\mathrm{comp}}(s)
=
\mathcal L_\infty(s)\otimes\mathcal L_X(s).
\]

This operation creates no primitive-square mixed trace. It is a legitimate
finite determinant-line extension.

Global Poisson sewing is different. It acts on the full adelic test object
before Euler factorization. The two operations must not be merged into a
single finite-cutoff operator action.

## Corrected role of finite tests

Finite prime-chain and determinant calculations remain valid for:

- deriving local Euler factors;
- verifying prime-power typing;
- calculating determinant cumulants;
- testing algebraic elimination identities;
- finding hostiles for proposed local coercions;
- checking deletion naturality inside the finite arithmetic category.

They cannot establish:

- the global Poisson functional equation by cutoff passage;
- completion stability of the primitive current;
- uniqueness of the completed determinant-line trivialization;
- absence of an infinite-boundary defect.

Those are properties of the full restricted product and its rigged global
correspondence.

## Consequence for earlier compiler demands

A requirement that every finite Euler cutoff carry a Poisson sewing cell is
overconstrained and source-invalid. It should be removed.

The correct two-level compiler has:

1. a finite arithmetic layer with local block extension, deletion, and
   determinant reconstruction;
2. a global adelic layer with restricted-product admission, Fourier–Poisson
   correspondence, Tate readout, and completed determinant-line
   trivialization.

A crossing from the first layer to the second requires a separately defined
restricted-product constructor. Ordinary directed union of finite Euler
packets does not supply it.

## Completion is pointed, not merely increasing

The restricted product remembers the distinguished local vacuum at almost
every prime. Its global object is therefore controlled not only by which
finite labels are present but by the basepoint chosen at every omitted place.

This is the categorical reason ordinary cutoff convergence is too weak.
Completion must preserve an infinite pointed background, not simply add more
finite summands.

The primitive and square vacuum cocycles measure failure relative to that
background. Their divergent or non-absolutely-summable behavior is invisible
if omitted places are replaced by scalar \(1\) before the comparison.

## Exact remaining gate

The global theorem must construct, directly on the restricted source:

1. the Poisson correspondence;
2. its action on the primitive and square connection coordinates;
3. the connected order-three transition unit;
4. the independent archimedean line;
5. a canonical completed determinant-line section.

Then one must prove that this global trivialization is unique up to a
nowhere-vanishing unit and that its relevant exactness or orientation law
survives the rigged completion.

Finite Euler packets may test shadows of this object but cannot construct it.

## Falsifiers

Reject any proposed completion if:

- it obtains finite Euler truncation by changing infinitely many unramified
  vectors while claiming to remain in the restricted product;
- it demands a finite Poisson action on a packet with no source preimage;
- it derives global sewing by termwise scalar continuation of the primitive
  current;
- it treats agreement of all finite diagnostic projections as authority for
  a unique global source object;
- it forgets the distinguished vacuum at omitted primes.

## Disposition

The programme has found a categorical boundary rather than a missing
estimate. Global theta/Poisson sewing is not assembled from finite Euler
sewing cells.

The RH-bearing object is intrinsically global and pointed: a rigged
restricted-product correspondence carrying its determinant-three packet and
archimedean line before scalar readout.
