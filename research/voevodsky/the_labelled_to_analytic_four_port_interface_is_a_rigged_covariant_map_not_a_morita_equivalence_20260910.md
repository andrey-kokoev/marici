# The labelled-to-analytic four-port interface is a rigged covariant map, not a Morita equivalence

## Question

What is the exact interface from the uniformly observable labelled behavior coalgebra to the noncoercive analytic four-port boundary system?

## Claim boundary

The source packets determine a three-rung projective rigging and an Euler-weighted synthesis with vanishing lower margin. This types the interface, its dagger, and its Adams covariance. It does not construct the still-missing common Green graph domain or a bounded inverse.

## Source and target

Let \(\mathcal M\) be the finite valuation monoid, \(T_\nu\) the retained type fiber, and

\[
q_\delta(c)=\sum_\nu e^{\delta\ell(\nu)}\|c_\nu\|_{T_\nu}.
\]

The source-selected rigging is

\[
\mathcal A_{\exp}
=
\bigcap_{\delta>0}\ell^1(\mathcal M,e^{\delta\ell};T)
\subset
\mathcal H_0=\ell^2(\mathcal M;T)
\subset
\mathcal A_{\exp}'.
\]

Here \(\mathcal A_{\exp}\) is the constructor algebra, \(\mathcal H_0\) is the uniformly observable labelled coefficient module, and \(\mathcal A_{\exp}'\) contains seam, endpoint, primitive, square, and archimedean boundary covectors of finite exponential order.

Let \(\mathcal G_4\) denote the retained four-port analytic graph, with complete boundary record \((P,Q,M,J)\). The interface is a continuous graph-valued synthesis

\[
U_4:\mathcal A_{\exp}\longrightarrow\mathcal G_4
\]

whose coefficient columns carry the Euler half-density. It may extend boundedly from selected Hilbert subrungs, but it is not bounded below on \(\mathcal H_0\).

## Coordinates retained and lost

The source coordinate is the complete labelled family \(c_{\nu,\alpha}\). Fourier--Bohr observation retains it isometrically:

\[
\|\mathcal Mc\|_{B^2}^2
=
\sum_{\nu,\alpha}|c_{\nu,\alpha}|^2.
\]

The analytic interface retains only the superposed boundary fields and their four typed traces. It preserves type distinctions carried into the four-port fiber, but does not retain a uniformly faithful coordinate on remote prime/grade labels.

For a prime-power atom,

\[
\|U_4e_{p,k}\|_{\rm an}
=
\frac1k p^{-k/2}\|\Phi\|_2
\]

on the weighted synthesis component. Thus \(U_4\) can be injective or pro-faithful while its inverse on the image is unbounded.

## Adams covariance

On the test algebra, Adams transport is seminorm transport:

\[
q_\delta(\psi^r c)=q_{r\delta}(c)
\]

up to the declared type-fiber map. On analytic columns, source-grade naturality gives

\[
U_4\psi^r
=
M_{\rho_r}\,\widetilde\psi^r U_4,
\qquad
\rho_r(p,k)=\frac1r p^{-(r-1)k/2}.
\]

This is covariance with a source-derived cocycle, not an isometry on the unweighted coefficient Hilbert module. Strict composition follows from the Adams action together with the cocycle law.

## Dagger typing

Boundary rows are elements of \(\mathcal A_{\exp}'\), not automatically vectors in \(\mathcal H_0\). The dagger of the interface is therefore the transpose relative to the rigged pairing:

\[
U_4^{\dagger}:\mathcal G_4'\longrightarrow\mathcal A_{\exp}',
\qquad
\langle U_4^{\dagger}\lambda,c\rangle
=
\langle\lambda,U_4c\rangle.
\]

Adams compatibility is the contragredient square obtained by transposing the covariance equation. If \(M_{\rho_r}\) denotes the analytic multiplier, then

\[
(\psi^r)'U_4^{\dagger}
=
U_4^{\dagger}(\widetilde\psi^r)'M_{\rho_r}'
\]

on the common dual domain. No Riesz map or Hilbert adjoint is authorized for seam and endpoint covectors unless boundedness on a named Hilbert rung is separately proved.

## Endpoint and archimedean attachments

Endpoint, seam, primitive, square, and archimedean rows factor as continuous maps

\[
\mathcal A_{\exp}
\xrightarrow{U_4}
\mathcal G_4
\xrightarrow{\operatorname{Tr}_b}
B_b,
\]

or equivalently as pullback covectors \(U_4^{\dagger}\operatorname{Tr}_b^{\dagger}\) in \(\mathcal A_{\exp}'\). Their finite-exponential coefficient growth makes the source-side pairing continuous. This establishes attachment naturality only on the declared common domain.

## Kernel and singular margin

No nonzero algebraic kernel is forced by the Euler weights because each weight is nonzero. The demonstrated defect is instead

\[
\inf_{\|c\|_{\mathcal H_0}=1}\|U_4c\|_{\rm an}=0.
\]

Hence:

- algebraic injectivity is compatible with the evidence;
- a closed retained graph is compatible with the evidence;
- bounded inverse, Hilbert equivalence, metric Morita equivalence, and reconstruction from analytic records are excluded.

## Missing square

The first genuinely absent object is the common graph domain

\[
\mathcal A_{\exp}
\subset D\subset
\mathcal A_{\exp}'
\]

on which doubled Clark--Green action, all four traces, primitive and square currents, connected tail, archimedean current, reciprocal sewing, and determinant pairing are simultaneously defined and continuous. Without \(D\), the displayed dagger and attachment squares are typed on their individual domains but not assembled into one global Green identity.

## Disposition

The labelled-to-analytic interface is now classified as a continuous rigged covariant synthesis with contragredient dagger. It is faithful only in an algebraic or pro sense and has zero Hilbert lower margin. The next substantive construction is the common graph domain \(D\); attempts to prove a bounded inverse or analytic Morita equivalence are closed by the prime-power atom sequence.
