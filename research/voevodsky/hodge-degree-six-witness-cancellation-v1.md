# Degree-six witness cancellation and an actual replacement divisor witness

## Fresh task and fixed direction

Execute degree-six-witness-deformation-cancellation using the legitimate path P_(1,2)=t from the first-order note. Retain b_j=r_j+i s_j=u_j wedge u_(j+3). At the product point the following four degree-six classes are actual rational algebraic intersection products:

    v0=r1 r2 r3,
    v1=r1 s2 s3,
    v2=s1 r2 s3,
    v3=s1 s2 r3.

Their exterior expansions are linearly independent and

    R=-v0+v1+v2+v3.

The factors denote cohomology classes of rational algebraic divisors, possibly signed; no effectivity of these individual products is asserted.

## Differentiate the actual codimension-three classes

Write A=Re(u1 wedge u2), B=Im(u1 wedge u2), C=Re(u4 wedge u5), D=Im(u4 wedge u5). Here D is a form, not an envelope divisor. The prior chart derivative gives

    dot r1=-2B, dot s1=2A, dot r2=2D, dot s2=-2C,
    dot r3=dot s3=0,

where dot means D_dotJ acting on the fixed flat form, NOT motion of its cohomology class. Applying the derivation to the four degree-six products yields

    D_dotJ v0=(-2B r2+2r1 D)r3 = T,
    D_dotJ v3=(2A s2-2s1 C)r3 = T,
    D_dotJ v1=(-2B s2-2r1 C)s3 = S,
    D_dotJ v2=(2A r2+2s1 D)s3 = -S.

Exact exterior expansion gives eight nonzero terms in each image; T and S are independent. Thus every v_i fails the first-order (3,3) condition, not just its particular divisor factorization. The map on their four-dimensional span has rank2 and kernel

    span(K1,K2),  K1=v3-v0, K2=v1+v2.

Equivalently a vector sum x_i v_i lies in the kernel iff x0+x3=0 and x1-x2=0. R=K1+K2 survives by cancellation.

For any locally constant degree-six class supplied by a flat family of algebraic cycles, type(3,3) is necessary. Therefore none of the four flat v_i classes can individually extend as an algebraic-cycle class along this direction, regardless of a change in its factorization. This statement is stronger than the prior factor test, but still concerns these four selected classes rather than all possible realizations of R.

## The two kernel directions survive beyond first order

Along the entire path the native subspace span(u1,u2,u4,u5) is J*-invariant and has trace zero. Consequently b1 b2 is type(2,2), while b3 remains type(1,1). Hence

    K1=-Re(b1 b2) r3,
    K2= Im(b1 b2) s3

are type(3,3) along the whole path. Exact rational checks at t=plus/minus1/8 give rank2 for the degree-six operator on the four v_i and the same kernel. No general sufficiency of infinitesimal Hodge conditions is being inferred; exact invariance supplies this stronger statement for this path.

## A replacement witness, not just formal cancellation

There is an independent algebraic positive control on EVERY fiber of this path. Re-pair the native forms as

    c1=u1 wedge u5,
    c2=u2 wedge u4,
    c3=u3 wedge u6=b3.

For c1 the one-form eigenvalues are i and -i. For c2 the varying two-plane is invariant and the trace of J* is zero. For c3 both coordinates are unchanged with opposite eigenvalues. Thus all c_j are type(1,1), as are their integral real and imaginary parts. By Lefschetz(1,1) these are divisor classes on every polarized fiber.

The wedge-order signs are

    c1 c2=-b1 b2,
    c1 c2 c3=U=R+iI.

Accordingly R and I have actual divisor-product representatives on each fiber of this off-diagonal path, although the ORIGINAL four v_i classes cannot be transported individually. Moreover

    K1=Re(c1 c2) r3,
    K2=-Im(c1 c2) s3

also have divisor-product representatives on each fiber. This is not merely a cancellation in Hodge cohomology: pointwise algebraicity follows from independently verified replacement divisors.

No flat relative cycle family is constructed here, and no canonical choice of line bundles or divisors across the parameter disk is asserted. Pointwise existence on these fibers is enough for the stated algebraic control; Hodge cancellation alone would not have supplied it.

## Scope and next joint-family test

This path lies outside the simultaneous locus of the ORIGINAL factors for t nonzero, but inside a locus for a different pairing of factors. The previous exact factor locus therefore was not an all-witness locus. This reinforces the distinction with an actual replacement witness rather than only a warning. The path is not the selected full off-diagonal transcendental period, and no cycle is thereby transported to that fixed X.

Next bounded test: add the diagonal direction P_(1,1)=s while retaining P_(1,2)=t. Along the s-axis the original factors survive; along the t-axis the replacement factors survive. The native four-plane remains invariant in the joint family, so K1,K2 stay Hodge; another zero derivative test would be redundant. Instead compute the rational divisor Hodge space at a specified algebraically independent small real pair (s,t), and its degree-six product span. Test whether that joint family still supplies divisor-product representatives of K1,K2. Individual axis witnesses do not settle that question; failure of divisor generation would still not exclude non-divisor cycles.

Verification: exact degree-six exterior products, rank and kernel, finite-period Hodge checks and the re-pairing signs. Lefschetz(1,1) supplies the pointwise algebraic divisor control; a general variational Hodge theorem is not assumed. No proof-assistant certification or Hodge verdict is claimed.
