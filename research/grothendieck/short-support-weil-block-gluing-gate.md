# Short-support Weil positivity reduces the first global gate to a prime-two block contraction

## Unconditional local positivity

Let `W` be the centered Weil distribution and, in multiplicative notation,

`k=g*g^tau`,

where `g^tau(u)=conj(u^(-1)g(u^(-1)))`.  Burnol proves that there is a
constant `c>1` such that

`W(g*g^tau)>=0`

whenever `supp(g) subset [c^(-1),c]`.  A common multiplicative translate of
`g` does not change its autocorrelation, so the same positive form occurs on
every logarithmic interval of length `2 log c`.

Thus the source already supplies positive local Hilbert blocks.  Global Weil
positivity fails, if it fails at all, only in the couplings between separated
blocks.

## Logarithmic block decomposition

Write `x=log u`, choose a cell width `ell<log 2`, and decompose a compactly
supported test function as

`f=sum_j f_j`,  `supp(f_j) subset I_j`,

with intervals `I_j` of width at most `ell`.  Let

`Q_ij(f_i,f_j)=W(f_i*f_j^*)`.

Each diagonal form `Q_jj` is positive by the short-support theorem (after
choosing `ell` within its proved range).  For two cells the Gram operator is

`G_ij=[[A_i,B_ij],[B_ij^*,A_j]]`,

where `A_i=Q_ii`, `A_j=Q_jj`, and `B_ij=Q_ij`.  After quotienting the local
null spaces, this block is positive if and only if

`|B_ij(x,y)|^2 <= A_i(x,x) A_j(y,y)`

for all local vectors, equivalently

`||A_i^(-1/2) B_ij A_j^(-1/2)|| <= 1`

with the usual quadratic-form interpretation when the local operators are
unbounded.

This is the exact gluing condition.  A partition of unity alone proves
nothing: the cross operators must be contractions in the local Weil norms.

## Why prime two is the first edge

On the arithmetic side, the finite-place term contains shifts by

`+/- k log p`,  `p prime`, `k>=1`.

If the logarithmic diameter of an autocorrelation is less than `log 2`, all
prime-power samples vanish.  The first new arithmetic interaction when two
positive cells are separated is therefore the shift `log 2`; it comes solely
from `(p,k)=(2,1)`.  Before `log 3` is reached, no other prime can repair or
obscure this edge (although the archimedean term remains global).

Hence the smallest genuinely arithmetic self-adjointness test is not an
arbitrary large Weil matrix.  It is the two-cell block at separation `log 2`:

`G_2=[[A_0,B_2],[B_2^*,A_0]]`.

Translation invariance identifies the two diagonal blocks.  Positivity is
equivalent to

`||A_0^(-1/2) B_2 A_0^(-1/2)|| <= 1`.

The operator `B_2` is source-explicit: it is the archimedean cross kernel plus
the single negative prime-two evaluation coupling with weight
`(log 2)/sqrt(2)` in the standard centered normalization.

## Prime-two gluing conjecture

**Conjecture.** On any short-support block lying in Burnol's unconditional
positive range, the combined archimedean-plus-prime-two cross operator is a
contraction in the local Weil energy norm.

This conjecture is strictly more informative than checking positivity of an
isolated theta or prime term:

- it retains the cancellation between the gamma endpoint and the negative
  prime direction;
- it is expressed entirely on the arithmetic side;
- it has no zero input; and
- a single pair of local test functions with normalized cross pairing larger
  than one falsifies it.

It does **not** by itself prove RH.  Even if every individual prime-power edge
is contractive, a large block matrix need not be positive: cycles can amplify
compatible off-diagonal phases.  The next gate would be a global completion
theorem, such as a positive-kernel dilation or a chordal/Markov factorization
showing that the prime-power block graph glues without cycle defects.

## Smallest hostile experiment

Choose one real smooth bump `phi` supported in a logarithmic interval of width
less than the local positivity radius, and let

`phi_0(x)=phi(x)`, `phi_2(x)=phi(x-log 2)`.

Compute from the prime--gamma explicit formula

`a=W(phi_0*phi_0^*)`,

`b=W(phi_0*phi_2^*)`.

The two-packet Gram matrix is

`[[a,b],[conj(b),a]]`

and its least eigenvalue is `a-|b|`.  Therefore:

- `|b|>a` immediately kills prime-two gluing;
- `|b|<=a` for one bump is only a diagnostic;
- optimizing `|b|/a` over a finite basis of local bumps gives a convergent
  Galerkin lower bound for the cross-operator norm.

This is the next computation to run.  It attacks the first place where the
source ceases to be automatically positive, rather than testing the known
critical-line zeros.

## Relation to self-adjointness

If the local blocks admit compatible positive gluing for all prime-power
separations, their inductive completion gives a positive Weil space.  Mellin
multiplication is then symmetric on the compact test core; the remaining
analytic task is essential self-adjointness/extension control.  Weil
positivity forces every Xi spectral parameter to be real, so the jet boundary
operator becomes self-adjoint.

Conversely, failure of the two-cell contraction produces an explicit negative
Weil square and rules out any self-adjoint boundary descended from that local
gluing scheme.

## Scope

This isolates a new finite, source-only attack direction.  It does not prove
the prime-two contraction, the global block-completion theorem, RH, or the
physical coefficient--Betti pushforward.

Primary source:

- Jean-Francois Burnol, *Sur les Formules Explicites I: analyse invariante*,
  especially the short-support positivity theorem:
  https://arxiv.org/abs/math/0101068
