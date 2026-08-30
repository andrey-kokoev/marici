# Pointed pi_0 fixes the dual cutoff scale without fitting

Epistemic-graph event: 1399.

## Ordered self-dual lattice

Under the explicit pointed monoidal relaxation, the Carrier derives the
initial semiring `M`, its ordered group completion

`L=Gr(M)`,

and the primitive positive generator `U`.  The dual lattice

`L_dual=Hom(L,Z)`

has the unique primitive positive functional `U_dual` satisfying

`U_dual(U)=1`.

Consequently the real symplectic double

`L_R direct_sum L_dual_R`

has canonical positive coordinates `x,p` in pointed lattice units, primitive
cutoffs

`x>=1`, `p>=1`,

and unimodular phase-cell covolume one.  Neither cutoff length is fitted to
zero data.

## Fourier and Planck normalization

Admit the same self-dual archimedean Fourier convention used by theta
completion,

`F(f)(p)=integral f(x) exp(-2 pi i x p) dx`.

Then the momentum operator is

`p_hat=(1/(2 pi i))d/dx`,

so `hbar=1/(2 pi)` and one Planck cell has area `2 pi hbar=1`, exactly the
unimodular lattice cell.

The symmetric dilation Hamiltonian is

`H_hat=(x p_hat+p_hat x)/2`

`=(1/(2 pi))[-i(x d/dx+1/2)]`.

If `t` denotes the conventional Mellin spectral parameter, its dimensionless
phase-space energy is therefore

`E=t/(2 pi)`.

## Counting theorem

For `x,p>=1` and `xp<=E`, the exact area is

`E log E-E+1`.

Substituting `E=t/(2 pi)` gives

`N_phase(t)=t/(2 pi)log(t/(2 pi))-t/(2 pi)+1`.

Thus the conditional pointed lattice plus its dual and the already explicit
Fourier realization derive the full scale of the two growing
Riemann--von Mangoldt terms.  No arbitrary `L`, cutoff product, or Planck
constant is fitted.

## Remaining defect

The constant is still `1`, whereas the smooth zeta-zero count has `7/8`.
The phase cell also supplies no fluctuation `S(t)`.  These cannot be repaired
by rescaling without destroying the two already correct growing terms.

Most importantly, the phase-space region is not yet a self-adjoint quantum
boundary condition: simultaneous sharp `x` and `p` cutoffs are Fourier-dual
and nonlocal.  The next gate is a source-derived metaplectic/boundary phase
whose quantization produces the missing `-1/8` correction without using the
Riemann--Siegel phase as input.

## Scope

The initial semiring and positivity are conditional on the pointed monoidal
relaxation, while Fourier analysis is the explicit archimedean input of
Ledger 1362.  No discrete zero spectrum or determinant `xi` is asserted.
