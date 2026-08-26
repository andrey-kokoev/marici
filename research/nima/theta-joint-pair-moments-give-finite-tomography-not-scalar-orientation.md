# Theta joint pair moments give finite tomography, not scalar orientation

## Status

Exact finite two-copy theorem. Mixed product-ratio moments determine every
finite ordered-pair packet. On the physical positive rank-one cone they
determine the one-copy source packet up to global phase.

Nevertheless a fully reconstructed positive rank-one packet can lie in the
kernel of the scalar readout. Finite tomography proves observability, not
scalar orientation or zero exclusion.

## Bivariate moment system

Let the one-copy arithmetic module have basis (e_n), logarithmic degree

\[
Le_n=(\log n)e_n,
\]

and augmentation \(\varepsilon(e_n)=1\). On the ordered-pair module define

\[
\nu_{ab}(X)
=
(\varepsilon\otimes\overline\varepsilon)
(L^a\otimes\overline L^{,b})X.
\]

For a finite pair packet

\[
X=\sum_{i=1}^r\sum_{j=1}^s
x_{ij},e_{n_i}\otimes\overline{e_{m_j}},
\]

we have

\[
\nu_{ab}(X)
=
\sum_{i,j}
x_{ij}(\log n_i)^a(\log m_j)^b.
\]

The rectangular collection with (0\leq a<r) and (0\leq b<s) is the tensor
product of two Vandermonde systems. Since the labels are distinct, both
Vandermonde matrices are invertible. Therefore these (rs) moments determine
all (rs) coefficients (x_{ij}).

The ordered-pair moment tower is a complete finite observer.

## Product-ratio equivalence

On the pair module, write

\[
L_{\Sigma}=L\otimes I+I\otimes\overline L,
\qquad
L_{\Delta}=L\otimes I-I\otimes\overline L.
\]

Because

\[
L\otimes I=\frac{L_{\Sigma}+L_{\Delta}}2,
\qquad
I\otimes\overline L=\frac{L_{\Sigma}-L_{\Delta}}2,
\]

the mixed moments of (L_{\Sigma}) and (L_{\Delta}) span exactly the same
finite polynomial observer as the bivariate moments \(\nu_{ab}\).

Thus retaining both product and ratio jets loses no finite ordered-pair data.

## Physical rank-one cone

For a one-copy packet

\[
c=\sum_ia_ie_{n_i},
\]

the physical autocorrelation packet is

\[
X_c=c\otimes\overline c.
\]

Its bivariate moments factor:

\[
\nu_{ab}(X_c)
=
\mu_a(c)\overline{\mu_b(c)},
\qquad
\mu_a(c)=\varepsilon L^ac.
\]

The infinite moment matrix is positive semidefinite and rank one. Finite
Vandermonde inversion reconstructs (X_c), and a nonzero rank-one positive
matrix reconstructs (c) up to multiplication by one global phase.

That phase does not affect the zero set of a linear scalar transform.

## Complete observation still permits cancellation

Let (u) denote the all-ones readout vector on the finite label support. The
scalar amplitude is

\[
\sigma(c)=u^*c.
\]

The corresponding two-copy readout is

\[
|\sigma(c)|^2
=u^*X_cu.
\]

Even though (X_c\) is positive semidefinite and nonzero, this readout vanishes
whenever

\[
c\perp u.
\]

Positivity of the state does not make a rank-one readout faithful. Complete
tomography tells us exactly which nonzero state is invisible; it does not
forbid invisibility.

At a spectral parameter (z), the source coefficients acquire complex route
phases. A packet with positive source weights can evolve into a vector
orthogonal to (u). Grothendieck's three-translate hostile family realizes
exactly this phenomenon while all finite labels and moments remain observable.

## Control-theoretic meaning

The distinction is:

- tomography reconstructs the state from the full family of outputs;
- scalar orientation requires one distinguished output never to vanish along
  the admitted source orbit.

No rank condition on the complete observer implies that safety property. One
needs a dynamical invariant restricting the orbit relative to the distinguished
readout kernel.

## Completion boundary

The finite result is exhaustive. Any genuinely new information must enter
through at least one of these mechanisms:

1. the infinite-label completion has states not determined by the joint moment
   tower;
2. completed primal-dual Poisson sewing restricts the admitted orbit inside the
   fully observed state space;
3. a boundary current supplies a new distinguished output not factoring
   through algebraic pair moments;
4. an arithmetic positivity cone survives spectral evolution and remains
   disjoint from the scalar readout kernel.

The fourth option is already strongly constrained by hostile positive sources
and prior cone no-go results. The first three require source-derived completion
data.

## Finite falsifier for orientation claims

Given any proposed finite moment-orientation theorem, reconstruct (X_c\) from
the mixed moments and test

\[
u^*X_cu.
\]

A nonzero positive rank-one (X_c\) with zero readout disproves the implication
from complete observation to orientation. The smallest abstract witness is

\[
c=(1,-1),
\qquad
X_c=
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
\]

It is positive semidefinite of rank one, completely reconstructible, and
annihilated by (u=(1,1)^T).

## Consequence

The finite polarized arithmetic programme is now informationally complete but
dynamically nonselective. More finite moments, more pair labels, or exact state
reconstruction cannot supply RH orientation. The remaining question is which
completed theta-specific operation restricts the source orbit so that its
fully observed rank-one state cannot meet the distinguished readout kernel off
the seam.
