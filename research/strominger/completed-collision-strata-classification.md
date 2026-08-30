# Collision kernels are moment-map deficiencies of coincident source labels

## Exact collision

Let a collision cluster contain `n` independently labelled magnetic source
jets `T_i(p,q)` of order at most `J`, all at the same celestial point. The
label-blind gravitational source field receives only

\[
 \Sigma(T_1,\ldots,T_n)=\sum_{i=1}^nT_i.
\]

Writing `d_J=(J+1)(J+2)/2`,

\[
 \boxed{\dim\ker\Sigma=(n-1)d_J.}
\]

A primitive basis consists of pair differences
`e_i tensor m-e_n tensor m` for every jet monomial `m`. This is the first
nonfaithful arrow on the exact collision stratum. Grade-three transport after
the sum is injective, so it neither creates nor removes this kernel.

This loss is physical only when the source constructor is label blind at
coincident direction. If an external hard-particle record retains identities,
the joint `(field,label)` port is faithful; the radiative field alone is not.

## Collision blow-up and moments

Resolve a one-parameter collision by

\[
 \xi_i(\epsilon)=\xi_0+\epsilon t_i.
\]

Taylor expansion gives the moment coordinates

\[
 \mu_k=\frac1{k!}\sum_i c_i t_i^k,
 \qquad 0\leq k\leq L.
\]

The moment matrix is a factorially normalized Vandermonde matrix. For
distinct tangent directions,

\[
 \boxed{\operatorname{rank}V_L=\min(n,L+1).}
\]

Therefore moments through `L=n-1` reconstruct all `n` labelled amplitudes;
lower resolution leaves an `(n-L-1)`-dimensional collision kernel. In two real
transverse directions, replace `t_i^k` by monomials `t_i^r bar(t_i)^s` with
`r+s<=L`; the generic rank is

\[
 \min\left(n,\binom{L+2}{2}\right),
\]

but special tangent configurations can have additional algebraic deficiency.

## Local circuits

Collision circuits are geometry dependent. With three tangent offsets and
only value and first-moment ports, the kernel solves

\[
 \sum_i c_i=0,\qquad\sum_i t_ic_i=0.
\]

For `t=(0,1,3/2)`, the primitive vector is

\[
 (1,-3,2).
\]

The same integers as the former magnetic `E_2` circuit can therefore occur,
but here they are forced by a nonuniform collision stencil. Changing the
tangent directions changes the primitive vector. It is not a universal
grade-two exception.

## Collision taxonomy

| retained target | collision kernel |
|---|---|
| field value only | zero-sum labelled packets |
| moments through `L` | nullspace of `V_L` |
| moments through `n-1`, distinct 1D tangents | zero |
| complete two-dimensional moments, generic tangents | zero once dimension permits |
| exact coincident field plus external label record | zero jointly |
| exact coincident field without labels | `(n-1)d_J` |

Thus collision loss is a supported-information birth at the specialization
map. It is neither chart failure nor transport failure.

## Evidence

`checkers/completed_collision_strata_checks.py` verifies the arbitrary-size
Vandermonde rank law, exact-collision kernel dimension, two-dimensional generic
moment ranks, the primitive `(1,-3,2)` stencil, and injectivity of the
subsequent grade-three symbol.
