# Entry 1895 — The Six-Site Physical Branch and Homogeneous Cartier Excess Are Distinct Coefficient Layers

## Terminal comparison

Entries 1893–1894 establish a generic source-activated divisor (D_6(k,z)).
Entries 1888–1889 establish a homogeneous length-six descended Cartier
object, assembled from three occurrence-labelled length-two components at
(k=0).

The remaining question is whether the generic physical branch specializes
to that Cartier object.

## Flat closure of the physical branch

Let

\[
A(k)=1026+69k-500k^2+196k^3.
\]

The generic critical section has a polynomial closure obtained from

\[
A(k)(z,x,v,w)=(N_z,N_x,N_v,N_w).
\]

Since (A(0)=1026\ne0), its special fiber is the single point

\[
p_0=
\left(x,v,w,z\right)
=
\left(
\frac{82}{9},
\frac{46}{9},
\frac{46}{9},
\frac{49}{9}
\right).
\]

The special-fiber Jacobian is (1026) times a permutation matrix. Thus the
closure is regular there and its special fiber has reduced length one.

## Comparison with the exceptional scheme

The homogeneous critical scheme is

\[
(L^2,M),
\]

with

\[
L=-2+x-6z+4v+w,
\qquad
M=-6+2x-6z+5v-w.
\]

The point (p_0) lies on (L=M=0), but the exceptional object has Cartier
length two along the entire affine critical line. Moreover,

\[
D_6(0,z)=114(9z-49),
\qquad
\partial_zD_6|_{k=0}=1026\ne0.
\]

Hence the horizontal physical branch meets the exceptional support at one
reduced point and with base intersection multiplicity one. It does not
specialize to the length-two Cartier line.

## Normal-order data

All three source-wall multipliers vanish to exactly second order in (k):

\[
\operatorname{ord}_k(\alpha_{12})=
\operatorname{ord}_k(\alpha_{34})=
\operatorname{ord}_k(\alpha_{56})=2.
\]

Their second grades are nonzero. The transverse Hessian determinant vanishes
to exactly first order:

\[
\operatorname{ord}_k\det H_{\rm tr}=1.
\]

Thus the physical node degenerates at the Gram boundary, but the resulting
normal filtration does not turn its reduced flat closure into the global
Cartier double line.

## Terminal decision

\[
\boxed{
\begin{aligned}
&\text{The five-site source activation extends to a genuine generic}\\
&\text{six-site physical coefficient divisor;}\\
&\text{the homogeneous length-six Cartier object is a distinct vertical}\\
&\text{Gram-supported coefficient layer.}
\end{aligned}
}
\]

Therefore the tested six-site sector has the architecture

\[
\boxed{
\text{unchanged occurrence-resolved Carrier}
+\text{ horizontal physical coefficient support}
+\text{ vertical Cartier excess}.
}
\]

No undeclared incidence operation, fitted support summand, or new Carrier
stratum was required. H2 survives and receives a stronger refinement:
sector-specific coefficient objects may contain horizontal and purely
special-fiber layers that must not be identified by their intersection.

## Next research frontier

The next independent falsifier should determine whether this horizontal-plus-
vertical decomposition recurs for another six-site matching orbit or at
seven sites. The present objective is closed; repeating the same incidence
without a new arity or orbit would add confirmation but little entropy gain.

## Durable verification

- `research/benincasa/marici-gm/src/bin/six_site_disjoint_pair_triple_specialization.rs`
- `research/benincasa/results/six-site-disjoint-pair-triple-specialization.json`
- allocator claim: `seqclaim-077c4f58314cf47bf998a7ab`
- epistemic event: `ev-000000002260-97e4a84b-4ce1-447b-9284-e1871711d8c6`
- epistemic event: `ev-000000002260-97e4a84b-4ce1-447b-9284-e1871711d8c6`
