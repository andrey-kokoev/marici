# Tate residue–radial mixed incidence: exact finite audit and refinement gap

## Result and scope

The operator-supplied candidate

\[
C_{p,h}=R_pT_h(I-R_p)
\]

has the stated four-state matrix at p=2, N=1. An exact rational audit also checks 48 radial compressions across p=2,3,5,7, N=1,2,3, and every nontrivial translation valuation admitted in each packet.

The active singular-value gap extends algebraically beyond N=1: for every finite packet, the only possible nonzero singular values are

\[
1,\qquad \sqrt{1-(p-1)^{-2}}.
\]

The second value occurs only for odd p; active rank depends on the packet and translation. This is a finite Tate operator theorem, not an identification with the existing arithmetic primitive/square Green packet. No log(p) normalization, cycle 1/k law, global positive Weil realization, or restricted-product completion theorem is inferred.

## Carrier and conventions

Use a character of conductor Z_p and self-dual additive Haar measure. The packet of functions supported in p^(-N) Z_p and invariant under p^N Z_p is identified with functions on Z/(p^(2N)). The additive Fourier transform preserves it.

Translation acts by pushing coordinate vectors forward, equivalently

\[
(T_hf)(x)=f(x-h).
\]

It is an endomorphism of this packet for h in p^(-N) Z_p. Unit averaging, with total unit Haar mass one, is the orthogonal projection R_p onto valuation shells.

For any such h,

\[
R_pC_{p,h}=C_{p,h},\quad C_{p,h}R_p=0,\quad C_{p,h}^2=0,
\]

\[
C_{p,h}^*=(I-R_p)T_{-h}R_p.
\]

A descended translation satisfying R_p T_h = T_bar R_p exists exactly when C_(p,h)=0. Thus C is precisely the obstruction to that linear descent. Reading it as a two-term incidence differential is legitimate, but does not by itself identify it with a pre-existing physical boundary differential.

Fourier conjugation gives

\[
\mathcal F_p C_{p,h}\mathcal F_p^{-1}
=R_pM_{\chi_h}(I-R_p),
\]

where the sign in chi_h follows the Fourier convention. Fourier commutes with unit averaging because inversion of a unit preserves normalized unit Haar measure.

For the unitary dilation D_a f(x)=|a|_p^(1/2) f(ax),

\[
D_aR_p=R_pD_a,\qquad
D_aC_{p,h}D_a^{-1}=C_{p,h/a}.
\]

This is an identity on the full local carrier or between the transported finite packets. A nonunit dilation does not generally preserve a fixed symmetric packet V_N.

## General radial compression

Let m=v_p(h), with -N <= m < N, and put k=N+m. Coordinates j modulo p^(2N) represent x=j/p^N. Multiplication by units reduces the translation to addition by p^k.

Set

\[
A=R_pT_hR_p\big|_{R_pV_N}.
\]

The radial space has dimension 2N+1. The k shells with valuation less than m are fixed by A. On the remaining shells, separate the shell of valuation m from the N-m inner shells (including the zero coset).

In normalized shell indicators, the latter block has the form

\[
\begin{pmatrix}
\frac{p-2}{p-1}&v^*\\
v&0
\end{pmatrix},
\qquad \|v\|^2=\frac1{p-1}.
\]

The off-diagonal coefficients are square roots of inner-shell size divided by the size of the valuation-m shell. Their squared sum equals 1/(p-1). Translation of an inner point lands in the valuation-m shell; a fraction (p-2)/(p-1) of that outer shell stays in the same shell.

Therefore A is self-adjoint and its spectrum, with multiplicities, is

\[
1^{(N+m+1)},\qquad
\left(-\frac1{p-1}\right)^{(1)},\qquad
0^{(N-m-1)}.
\]

Since translation is unitary,

\[
C_{p,h}C_{p,h}^*\big|_{R_pV_N}=I-AA^*=I-A^2.
\]

Consequently its spectrum is

\[
0^{(N+m+1)},\qquad
\left(1-\frac1{(p-1)^2}\right)^{(1)},\qquad
1^{(N-m-1)}.
\]

For p=2, the middle eigenvalue is also zero. Hence

\[
\operatorname{rank}C_{p,h}
=\begin{cases}
N-m-1,&p=2,\\
N-m,&p>2.
\end{cases}
\]

If h lies in p^N Z_p, translation is already the identity on the packet and C=0. If h lies outside p^(-N) Z_p, enlarge or transport the packet before treating translation as an endomorphism.

On every nonzero active sector the singular-value lower bound is 1 at p=2 and at least sqrt(3)/2 at odd primes. This excludes active singular-value collapse under these finite local refinements; it does not remove exact kernels or prove bounds for differently weighted arithmetic identifications.

## Four-state fixture

For p=2, N=1, h=1/2, the checker constructs averaging and translation independently on the four coordinate vectors and obtains

\[
C=\frac12
\begin{pmatrix}
0&-1&0&1\\
0&0&0&0\\
0&1&0&-1\\
0&0&0&0
\end{pmatrix}.
\]

Thus C(e_1-e_3)=e_2-e_0. Both C*C and CC* are rank-one orthogonal projections.

For N=1 and h=1/p, the general spectrum gives exactly the proposed eigenvalues 1,-1/(p-1),0 of the three-dimensional radial compression. At p=2 the incidence has only one active direction. Keeping h=1/2 and refining to N=2 gives rank two; any proposed two-direction boundary identification must account for this resolution dependence rather than claim rank two already at N=1.

## Verification

Run

```text
python research/nima/checkers/check_tate_radial_mixed_incidence.py
```

Fresh execution passed 48 exact rational radial cases and the independent full four-state fixture. Output: `results/tate-radial-mixed-incidence.json`.

The checker derives compression matrices by enumerating translated shell points, verifies weighted self-adjointness, checks the annihilating polynomial and all eigenvalue multiplicities by rational ranks, and verifies the active Gram ranks. The argument above supplies the all-packet formulas; the finite audit is not substituted for that proof.

## Remaining comparison

The next source interface must specify a map from the radial image into the actual primitive/square valuation boundary packet, with its labels, metric, orientation, Mellin normalization, and cycle operation. Additive translation at finite level and multiplicative prime-power return are different operations. Their comparison must be constructed before log(p) and 1/k weights can be claimed for C_(p,h).

The candidate operator and its finite refinement gap are established here. The arithmetic comparison and subsequent completion remain separate obligations. Files are local; no commit or publication was performed.
