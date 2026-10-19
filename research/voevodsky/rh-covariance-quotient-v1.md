# Iteration 10: signed covariance, radical quotient and multiplicity

This finishes the audit specified in iteration 8. It uses the test space T,
half-divisor normalization and added triangle decoration of
`rh-analytic-dual-carrier-v1.md`. Analytic arguments below are not
machine-formalized. The accompanying checker tests exact finite controls and
freshness of the previous receipt; it does not infer global theorems from them.

## What the triangles compute

On a register (f,l), an edge labelled b acts by U_b(f,l)=(f,l+W_b f),
where (W_b g)(f)=b(f,g). With initial register (f,0):

- AB,BC,CA applies endpoint E, gamma Gamma, signed prime P. The output is
  (f,W_A f), A=E+Gamma+P; its paired scalar readout is b_A(f,f).
- BA,AD,DB applies -E,Z,E. The output is (f,W_Z f); its readout is
  b_Z(f,f)=(1/2) sum_rho m(rho) conjugate(Ff(conjugate(u_rho)))Ff(u_rho),
  u_rho=(rho-1/2)/i.

The common edge identifies the same test frame and the chosen endpoint
operator, reversed on BA. The shared analytic interface fixes Fourier and
half-divisor normalization. Geometry alone forces neither this decoration nor
the explicit formula. The formula gives A=Z unconditionally; positivity for
all tests is the RH question. Forward traversal of both faces adds A+Z;
comparison requires the inverse traversal of the second face.

## 1. Translation covariance is unconditional, not positivity

For real r, let T_r f(x)=f(x+r). These are continuous automorphisms of T:
p(k,m)(T_r f)<=exp(k|r|)p(k,m)(f), and F(T_r f)(u)=exp(iur)Ff(u).

Each source form is separately translation invariant:

- Endpoint integrals A_+ and A_- acquire exp(-r/2), exp(r/2); the factors cancel.
- On the real Fourier axis the gamma phase cancels.
- Translations commute in the prime correlation, and T_r is L2-unitary.
- At a complex divisor node, conjugate(exp(i conjugate(u) r))exp(iur)=1.
  The divisor cancellation does not assume u is real.

Thus b_j(T_r f,T_r g)=b_j(f,g) for j=E,Gamma,P,Z,A.
Define D_r l(f)=l(T_-r f). Then W_j T_r=D_r W_j. The map
R_r(f,l)=(T_r f,D_r l) preserves the fixed dual pairing and commutes with
all the source shears U_j. This is covariance of the added analytic carrier,
not a statement about the inherited native clock.

The checker uses synthetic nodes +/-pi/(2log2)+/-i/4 at r=4log2. Their
translation multipliers are 1/2 or 2. The conjugate-pair signed form is
preserved, but the ordinary positive norm is not. These are controls, not
asserted zeta zeros. Consequently signed translation invariance cannot prove RH.

## 2. A useful auxiliary atomic completion

Let Lambda be the DISTINCT nodes u_rho and w_u=m(u)/2. Define
K=l2(Lambda,w), with its auxiliary positive norm, and

  (Ef)(u)=Ff(u),       (Cv)(u)=v(conjugate(u)).

Divisor symmetry makes C a linear self-adjoint involution on K. It is a
permutation of entries, NOT conjugation of their values. Rapid strip decay
and polynomial zero counting imply Ef belongs to K. Then

  b_Z(f,g)=<C Ef,Eg>_K.

K's positive norm is not the signed Weil form. Introducing it assumes no RH.
The distinction matters: a vector supported on just one nonreal member of a
conjugate pair is isotropic for the signed form but not radical.

### Density of evaluation vectors

Fix u0. There are finitely many other distinct nodes with
|Re(u-u0)|<=2, since |Im u|<1/2 and the divisor is locally finite. Choose a
polynomial P vanishing at those other nodes with P(u0)=1, and set

  q_t(z)=P(z) exp(-t(z-u0)^2), t>=1.

Its inverse Fourier transform f_t is a finite combination of derivatives of
an exponentially modulated Gaussian, hence lies in T. At u0 the evaluation
is 1, and at the other nearby nodes it is 0. On remaining nodes write
u-u0=a+ib, where |a|>2 and |b|<1. Then

  |q_t(u)|^2=|P(u)|^2 exp(-2t(a^2-b^2))
             <=|P(u)|^2 exp(-2t(a^2-1)).

Polynomial divisor counting makes the t=1 majorant summable, including
multiplicities. Dominated convergence proves Ef_t converges in K to the
single-node atom. Thus E(T) is dense in K. This does not assert surjectivity
of E on T, or convergence in the original test-space topology.

### Radical and positivity

Let Rad b={f:b(f,g)=0 for all g in T}. Density and invertibility of C imply
Rad b=ker E. Thus T/Rad b embeds densely in K with signed form <Cv,w>.
The auxiliary norm ||Ef|| gives one explicit completion of this quotient;
it is not a canonical positive norm derived from b when b is indefinite.

If any nonreal node exists, its conjugate partner is distinct; the difference
of the two normalized atoms has negative signed square. Density approximates
it by evaluation vectors, so some test has negative b(f,f). Conversely, when
all nodes are real, C=I and b(f,f)=||Ef||^2>=0. This gives the expected RH
positivity equivalence on T, not a proof of positivity.

Under RH only, the positive radical quotient therefore completes to K in its
own form norm. Without positivity the isotropic cone {f:b(f,f)=0} must NOT be
used as the radical: it need not even be a linear subspace.

## 3. Conditional dynamics and multiplicity limitation

On K translation is S_r v(u)=exp(iur)v(u). Unconditionally it is bounded
for each r, strongly continuous, and preserves <Cv,w>; |Im u|<1/2 gives
||S_r||<=exp(|r|/2). Under RH it is a unitary group. In that case its
multiplication generator Mv(u)=u v(u), with domain
sum w_u |u v(u)|^2<infinity, is self-adjoint. Local finiteness and escape of
nodes to infinity give compact resolvent.

This is a SOURCE-defined operator using the divisor, not a construction of a
native seed operator or a proof of RH. Also, each DISTINCT node has a
one-dimensional eigenspace in this scalar evaluation model, irrespective of
its zeta multiplicity. Multiplicity is retained in the weight w_u, not as
m(u) independent spectral directions.

If a zero has multiplicity m, replacing that weighted coordinate by m copies
with weight 1/2 embeds scalar evaluations only in the diagonal subspace.
The remaining m-1 directions are invisible to all these tests. The checker
uses multiplicities (3,1): four repeated coordinates, but evaluation rank two.
One cannot infer a determinant with zero orders m(u) from the ordinary
spectral multiplicities of the scalar quotient operator. Extra multiplicity
fibers or an explicit weighted trace construction require separate justification.

Under RH, Cauchy vectors c_z(u)=1/(u-z), z off the real axis, belong to K.
For convergence, use the sharper Jensen bound already displayed in
`rh-full-divisor-window-v1.md`, N(v)=O(v log v), not merely its coarser O(v^2)
simplification. Then sum m(u)/(1+u^2)<infinity. Their Gram law retains the
half factor: <c_z,c_w>=sum m(u)/(2(u-conjugate(z))(u-w)). Density above
puts these vectors in the quotient completion. This alone does not identify
every externally normalized Pick kernel, nor give a zeta determinant identity.

## 4. Does the same comparison survive in both structures?

Yes, on the COMMON ADDED analytic register. Both source forms, their radical,
covariance, and conditional positive quotient are independent of which native
tag is used. Iteration 7 checked the metric-correct tag embedding in the
protonlike and neutron carriers. Nothing here changes that embedding or the
untouched native remainder.

No, if "same" means equivalent full native processors. The selected completion
still has the stage-rank obstruction (6 versus 33), the native clock still
satisfies W^5=W^2, and its nonzero source shears do not. Neither the positive
quotient nor translation covariance removes these obstructions. The finite
inherited form also still has only 14 positive directions; the 15-test witness
requires the added carrier.

## Verification and boundaries

Run `python research/voevodsky/checkers/check_rh_covariance_quotient.py`.
The output is `results/rh-covariance-quotient-v1.json`. Exact controls test
signed versus positive covariance, nonradical isotropic vectors, multiplicity
rank, and half-divisor normalization. Infinite-dimensional arguments above
remain mathematical arguments rather than formally checked theorems.

The user's comparison is resolved at the declared analytic-decoration level.
Further research, if desired, is a separate native-intertwining or
multiplicity-resolved determinant problem. No all-test positivity or RH proof
has been obtained.
