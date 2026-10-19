# C11 — exact core certificates and the three-port threshold limit

## Fixed operator and convention

Use the eleven-state core K and positive diagonal metric H from the pinned `native_joint_generator_resolvent.json`, with visible coordinates 0,1,2 and port metric diag(1196/15,20,20). P is the H-orthogonal projection onto those coordinates. No unspecified spectator coordinates are discarded from a larger model.

The source contact/lead equations give, for 0<k<pi,

    E=2-2cos(k), eta=exp(ik), Gamma=2sin(k),
    M(k)=E I-K+(eta-1)P, G(k)=M(k)^(-1),
    S(k)=I3-i Gamma G_PP(k).

C11 concerns this **coefficient** S. In the endpoint travelling-wave convention the outgoing amplitudes are b=-eta² S a. That common phase is not silently absorbed into a different limiting matrix.

## Fresh finite-dimensional checks

`check_three_port_threshold.py` reads the source core and verifies its source hashes, then checks directly over Q(sqrt(151)):

- all metric entries are positive and HK=K*H;
- rank(K)=10 and its one-dimensional kernel has a nonzero port projection;
- the three port basis vectors generate all eleven coordinates under **K itself**;
- the candidate coefficient S0 below is H_port-unitary, involutive and has trace 1, with rank(I-S0)=1 and rank(I+S0)=2.

Closure under the separate rational and radical parts would not suffice for the third item: it could be a stronger operator family. This checker uses only the actual K action.

## No open-band real response pole

If M(k)x=0, taking the imaginary part in the H inner product gives

    sin(k) ||P x||_H²=0.

Since sin(k)>0, Px=0, and the remaining equation is Kx=E x. For every port seed e_j and every nonnegative integer m, H-self-adjointness gives

    <K^m e_j,x>_H = E^m <e_j,x>_H=0.

The exactly verified cyclic span is the whole core, so x=0. Finite dimensionality gives invertibility of M(k) for every 0<k<pi. This is an all-energy argument, not an extrapolation from sampled energies or a statement about an eliminated hidden block alone.

## Threshold expansion

Whiten the core by H^(1/2), and write u for a unit vector spanning the whitened kernel. Let p=<u,Pu>>0 and Q0=I-uu*. The restriction of K to Q0 is invertible because its kernel is simple. On the compact finite core its inverse has finite norm.

Taylor expansion gives

    M(k)=-K+i k P+O(k²).

Relative to span(u) direct-sum Q0, the Q0 block remains invertible for sufficiently small k. The scalar Schur complement is i k p+O(k²); the off-diagonal blocks are O(k). Standard block inversion therefore yields the norm expansion

    G(k)=uu*/(i k p)+O(1).

This is justified by the invertible complementary block and p>0, not by treating a singular K as invertible. With Gamma=2k+O(k³), compressing onto ports gives

    H_port^(1/2) S(k) H_port^(-1/2)
      = I3-2 w w*+O(k),

where w=Pu/sqrt(p) is the normalized whitened port projection. The limit is a rank-one Householder reflection with eigenvalues (-1,1,1).

For an unnormalized original-coordinate kernel vector v, the equivalent exact coefficient matrix is

    S0=I3-2 v_P v_P* H_port/(v_P*H_port v_P).

Those entries and their weighted identities are independently recomputed by the checker. The analytic Schur argument supplies the limit; a successful finite-matrix multiplication alone would not prove a threshold expansion.

## Scope

This establishes C11 for the fixed eleven-state-plus-three-lead fixture. It neither proves full wave-operator completeness nor classifies singular-continuous spectrum. The threshold tails are bounded but not square summable, and the group velocity is zero at k=0: the limiting probabilities are not a nonzero-flux scattering assignment at the threshold itself. C6 can now use this result with C1, but is not automatically promoted by the dependency update.
