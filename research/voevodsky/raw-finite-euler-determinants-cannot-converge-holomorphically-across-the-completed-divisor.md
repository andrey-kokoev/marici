# Raw finite Euler determinants cannot converge holomorphically across the completed divisor

## Question

Can the finite direct-Euler determinant sections converge compact-locally as holomorphic functions on a domain reaching the critical strip?

## Claim boundary

No on any connected domain containing a pole of the meromorphic continuation of the direct inverse-zeta section. This rules out the raw global-frame completion proposed after the finite-stage reflected-pair construction. It does not rule out meromorphic convergence after local renormalization.

## Argument

Each finite section

$$
D_{+,N}(s)=A_{\infty,N}(s)
\prod_{p\in S_N}(1-p^{-s})
$$

is holomorphic away from explicitly declared elementary archimedean singularities. On \(\operatorname{Re}s>1\), the finite products converge to the direct inverse-Euler section

$$
D_+(s)=A_\infty(s)\zeta(s)^{-1}.
$$

Assume the raw sections converged locally uniformly to a finite-valued holomorphic function \(H\) on a connected domain \(\Omega\) intersecting \(\operatorname{Re}s>1\). The identity theorem would force

$$
H(s)=A_\infty(s)\zeta(s)^{-1}
$$

throughout the common continuation domain.

If \(\Omega\) contains a zeta zero not cancelled by the declared elementary factor, the right side has a pole there, contradicting holomorphy of \(H\). Therefore raw locally uniform holomorphic convergence cannot cross that divisor.

Independently, ordinary prime-product convergence already fails at \(\operatorname{Re}s\le1\), so continuation cannot be obtained merely by taking larger finite prime sets in the unrenormalized product topology.

## Correct completion object

A completed compiler must use a meromorphic line section. Locally it is represented by quotients

$$
D_+|_{U_\alpha}=\frac{N_{+,\alpha}}{Q_{+,\alpha}},
$$

with holomorphic numerator and denominator and invertible transition functions on overlaps. Reflection supplies corresponding local data for \(D_-\). Divisor multiplicity is then the order difference

$$
\operatorname{ord}(D_+)
=
\operatorname{ord}(N_+)-\operatorname{ord}(Q_+).
$$

## Disposition

The raw finite Euler determinants cannot complete as global holomorphic frames across the completed-zeta divisor. The executable continuation problem is to construct compatible local renormalized numerator/denominator sections and prove their cutoff-independent transition laws.