# C9 — no singular-continuous spectrum for the fixed three-port model

## Operator and metric

Whiten the eleven core coordinates by the positive diagonal core metric and each lead by its fixed positive port weight. This is a unitary change between the specified weighted and ordinary Hilbert spaces. Write K for the whitened Hermitian core, V:C3->C11 for the port inclusion, and P=VV*. The coupled operator has core block K+P, three free Dirichlet chain blocks H_D (diagonal 2, hopping -1), and contact off-diagonal blocks -V and -V*. It is bounded and self-adjoint on the whole Hilbert space.

This is precisely the finite core plus three chains in C9, not a larger space with unspecified spectators. Finite-rank coupling alone does not prove the conclusion below.

## Weyl function and finite-site free resolvent

Use the resolvent convention (H-z)^(-1), Im(z)>0. Put

    w(z)=<delta_1,(H_D-z)^(-1)delta_1>.

Schur elimination of the first site gives w=1/(2-z-w), equivalently

    w²+(z-2)w+1=0,   z=2-w-w^(-1).

The physical branch is w(z)~ -1/z at infinity, with Im(w)>0 and |w|<1 in the upper half-plane. One may write w=(2-z+sqrt(z(z-4)))/2 with the square root asymptotic to z-2. Its only real branch points are 0 and 4. On the band w(E+i0)=exp(ik), E=2-2cos(k), 0<k<pi.

For finite lead sites n,m>=1,

    G_D(n,m;z)=w^(|n-m|+1) sum_(r=0)^(min(n,m)-1) w^(2r).

This follows by the second-order recurrence, the zero boundary value at site 0 and the decaying branch at infinity. In particular G_D(n,1)=w^n. The polynomial formula has no artificial poles at w=+/-1; it is valid for every finite pair of sites.

## The full finite-support resolvent is rational in w

Eliminating the three free leads gives the core Schur matrix

    B(z)=K+P-zI-w(z)P.

It is invertible in the upper half-plane since the full operator and the eliminated lead operator are self-adjoint. Substitute z=2-w-w^(-1) and multiply by w:

    L(w)=w B(z)=I+w(K-2I+P)+w²(I-P).

Thus p(w)=det L(w) is a polynomial of degree at most 22 and p(0)=1. It is not identically zero, independently of any sampled determinant tests. The core resolvent B^(-1)=w adj(L)/p is rational in w. The same determinant can be computed before whitening, since the diagonal metric commutes with P.

Block inversion gives core-to-lead entries B^(-1)V w^n and lead-to-lead entries

    delta_jl G_D(n,m;z) + w^(n+m) [V*B^(-1)V]_jl.

Consequently every resolvent matrix element between finitely supported vectors is rational in w(z). The entire family shares the finite exceptional set consisting of 0,4 and the real energies whose physical boundary value w is a root of p. There are at most 22 such root values before cancellations; no claim that every root is an actual spectral pole is needed.

## Spectral measures, including exceptional energies

On every compact real interval avoiding that finite set, the upper boundary value of w is real-analytic and p(w) is bounded away from zero. Each finite-support scalar resolvent therefore has uniformly convergent, smooth boundary values there. Stieltjes inversion gives an absolutely continuous spectral measure on that interval, with density pi^(-1) Im <f,(H-E-i0)^(-1)f>. Outside the band the regular boundary value is real, giving zero density.

Any singular part of that scalar measure is thus supported on the finite exceptional set. A measure supported on a finite set is purely atomic; a singular-continuous measure, being atomless, assigns it zero mass. This covers both band edges without an incorrect claim that the resolvent is bounded there. A threshold resonance can make a boundary density unbounded near an endpoint, but cannot support a nonzero atomless measure concentrated at that single endpoint.

It follows that P_sc(H)f=0 for every finitely supported f. Such vectors are dense, and P_sc(H) is a bounded orthogonal projection. Therefore

    P_sc(H)=0

on the full coupled Hilbert space.

## What this does not prove

The argument does not count the point spectrum, prove that a threshold is or is not an eigenvalue, or identify the range of wave operators. It does not establish C2 by itself. It also does not transfer the conclusion to an infinite or nonalgebraic core, a different lead law, or unspecified spectators.

## Verification boundary

`check_no_singular_continuous.py` verifies the pinned source core/metric and exact Schur-pencil constant term, and checks representative finite-site Weyl recurrence identities with rational polynomial arithmetic. The all-site Green formula and the measure-theoretic density/finite-exception argument above are the analytic proof; the finite recurrence controls and source hashes are not a substitute for it. No floating spectral scan or source scattering solver is used.
