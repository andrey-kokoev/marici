# The exact Evans graph norm closes the uniform mixed seam pairing but not its cancellation

## Question

Does the centered arithmetic adjoint of the exact Evans history exist uniformly
on compact parameter sets, or is a limiting-absorption estimate still required
for that mixed block?

## Claim boundary

The mixed adjoint exists and is locally uniform in the parameter. This follows
from the exact Evans \(H^1\) theorem and the scale-independent wall-extended
cut-atom norm. The result proves boundedness of
\(B_\Sigma^\dagger u_z\), not its vanishing.

## Two established estimates

At a zero of the Xi section, the exact global Evans history satisfies

\[
 u_z\in H^1(\mathbb R).
\]

More generally, on every compact parameter set \(K\subset\mathbb C\), the
left and right source integrals have locally uniform graph bounds on their
respective ends. When the mismatch vanishes, these bounds combine into

\[
 \sup_{z\in K\cap Z(\tau)}\|u_z\|_{H^1}<\infty.
\]

The wall-extended unweighted cut atom at logarithmic scale \(a\) has the exact
norm

\[
 \|c_a\|_{G}^2
 =\|\Phi\|_2^2+\|\Phi'\|_2^2+|\Phi(0)|^2
 =:C_{\rm cut}^2,
\]

independent of \(a\).

## Uniform relative pairing

Use the declared positive direct-sum Green graph pairing before adding any
separately ordered skew linking form. Cauchy--Schwarz gives

\[
 |\langle c_a,u_z\rangle_G|
 \le C_{\rm cut}\|u_z\|_G.
\]

Therefore, for every compact \(K\),

\[
 \sup_{z\in K\cap Z(\tau)}\sup_{a>0}
 |\langle c_a,u_z\rangle_G|<\infty.
\]

Taking \(a=\log p\) proves the uniform prime pairing required by the earlier
mixed-seam packet.

## Arithmetic source norm

For the centered primitive incidence

\[
 b_p=p^{-1/2}c_{\log p}
\]

and source metric

\[
 \|x\|_U^2=\sum_p(\log p)|x_p|^2,
\]

the adjoint coordinate is

\[
 (B_\Sigma^\dagger u_z)_p
 =\frac{p^{-1/2}\langle c_{\log p},u_z\rangle_G}{\log p}.
\]

Hence

\[
 \|B_\Sigma^\dagger u_z\|_U^2
 \le C_{\rm cut}^2\|u_z\|_G^2
 \sum_p\frac1{p\log p}.
\]

The prime sum converges. Consequently

\[
 B_\Sigma^\dagger u_z\in U
\]

with norm locally uniform on compact subsets of the Xi divisor.

This reproduces, in the wall-extended Green topology, the abstract conclusion
already implied when \(B_\Sigma\) is treated as Hilbert--Schmidt.

## Parameter derivatives

If \(z_0\) has Xi multiplicity \(m\), then for \(0\le j<m\), the root vector
\(\partial_z^ju(\cdot;z_0)\) belongs to the same graph domain. The same estimate
gives

\[
 B_\Sigma^\dagger\partial_z^ju(\cdot;z_0)\in U.
\]

Thus every multiplicity residual is a well-defined arithmetic vector. No
closure-of-range argument or distributional reinterpretation is needed.

## Linking-form qualification

The estimate uses the positive wall-extended direct-sum graph form. If the
final conservative pairing adds an ordered Stokes/Wronskian linking term, its
continuity on this common completed carrier must be proved separately. The
positive estimate cannot silently authorize an unbounded skew cross-term.

Accordingly the result closes the primitive mixed block and its regular
wall/derivative completion. It does not close an undeclared linking port.

## Why this does not advance the RH implication by itself

The estimate proves existence and compact-local control of the residual

\[
 r_U(z)=B_\Sigma^\dagger u_z.
\]

It supplies no identity forcing \(r_U(z)=0\). The ordinary theta-tail component
has eventually strict prime-shell sign, so cancellation still requires explicit
source-derived derivative, wall, reciprocal, or linking terms.

Boundedness, trace-class convergence, and compact-local holomorphy cannot
replace those shell identities.

## Disposition

The mixed seam-pairing and arithmetic-target rigging gates are closed for the
exact Evans history in the positive wall-extended Green topology. The remaining
obstructions are continuity of any extra linking polarization and the
RH-bearing arithmetic cancellation itself. No RH conclusion is authorized.
