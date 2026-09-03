# Source current row construction

Author: `marici.Grothendieck`
Status: finite source identity; endpoint sewing unresolved

## Question

Can the declared two-sheet flow itself construct the missing current row, rather than adding an arbitrary endpoint functional?

## Claim boundary

For

\[
u'=-zu-cf,\qquad v'=zv-cf,
\]

the local sheet current \(J_0=u^2-v^2\) satisfies

\[
J_0'=-2z(u^2+v^2)-2cf(u-v).
\]

Define the accumulated source-work row from the declared port,

\[
J_F(q)=2c\int_{q_0}^{q} f(\xi)(u(\xi)-v(\xi))\,d\xi.
\]

Then the closed current \(J_{\rm work}=J_0+J_F\) obeys the exact source identity

\[
J_{\rm work}'=-2z(u^2+v^2).
\]

This constructs a nonlocal current row from the base flow and forcing incidence, without a formal adjoint or fitted scalar factor. If scalar-null boundary data gives \(u+v=0\) at both endpoints, then \(J_0=(u+v)(u-v)\) vanishes there and

\[
J_{\rm work}(q_1)-J_{\rm work}(q_0)
=2c\int_{q_0}^{q_1} f(u-v).
\]

Consequently endpoint sewing is exactly the independent source-work orthogonality condition

\[
c\int_{q_0}^{q_1} f(u-v)=0.
\]

The current row is therefore derivable, but its endpoint equality is not.

## Orthogonality audit

For constant real \(z\) and \(c\), the common/relative equations imply

\[
r''-z^2r=2zcf.
\]

Common-mode nullity at both endpoints gives \(r'=-zw=0\) there. Multiplying by \(r\), integrating, and using the Neumann boundary terms yields

\[
2zc\int_{q_0}^{q_1}fr
=-\int_{q_0}^{q_1}(r')^2-z^2\int_{q_0}^{q_1}r^2.
\]

Thus, for real \(z\ne0\), source-work orthogonality can hold only when \(r=0\). The base flow does not generate orthogonality; away from \(z=0\) it gives the work pairing a definite nonzero value for every nontrivial relative response. Reflection symmetry does not help: the parity-compatible sectors make \(f\) and \(r\) have the same parity, so \(fr\) is even rather than cancellation-odd.

## Complex Hermitian sector

For complex sheets and a real path coordinate, use

\[
J_0^{\rm H}=|u|^2-|v|^2,
\qquad
B^{\rm H}=|u|^2+|v|^2.
\]

Direct differentiation gives

\[
(J_0^{\rm H})'
=-2\operatorname{Re}(z)B^{\rm H}
-2\operatorname{Re}\!\left(cf(\bar u-\bar v)\right).
\]

The Hermitian source-work row

\[
J_F^{\rm H}(q)=2\int_{q_0}^{q}
\operatorname{Re}\!\left(cf(\bar u-\bar v)\right)d\xi
\]

therefore yields

\[
(J_0^{\rm H}+J_F^{\rm H})'
=-2\operatorname{Re}(z)B^{\rm H}.
\]

With common-mode nullity at both endpoints, Hermitian work sewing and positive bulk force \(\operatorname{Re}(z)=0\), not \(z=0\). This is the correctly typed confinement statement if \(z\) is the full complex displacement from the target line. No conclusion about the tangential spectral coordinate follows from positivity.

## Spectral-coordinate audit

The source drift-reversal equations recorded in the parent packet are

\[
\psi_+'=-z\psi_+-F,
\qquad
\psi_-'=\bar z\psi_--F.
\]

They descend to the declared pair \(u'=-zu-cf\), \(v'=zv-cf\) only after imposing \(\bar z=z\). Thus the available source types \(z\) as a complex spectral coordinate; reality is an additional slice assumption, not a derived transverse-coordinate map. On that real slice, proving \(z=0\) concerns only the real-axis restriction and cannot establish confinement of general complex zeros. The Hermitian identity above removes this unsupported descent and proves exactly the transverse statement \(\operatorname{Re}(z)=0\), conditional on source-work sewing. To identify that locus with the critical line still requires a source normalization \(z=s-\tfrac12\), or an equivalent declared affine coordinate map.

Fourier reflection does not determine that normalization. If \(w=s-\tfrac12\), the odd, conjugation-compatible coordinate

\[
z=\phi(w)=w+w^3
\]

obeys \(\phi(-w)=-\phi(w)\) and \(\phi(\bar w)=\overline{\phi(w)}\), just as the centered functional equation requires. Nevertheless

\[
\operatorname{Re}\phi(x+iy)=x(1+x^2-3y^2),
\]

so \(\operatorname{Re}z=0\) contains the off-critical curves \(3y^2=1+x^2\) in addition to \(x=0\). Therefore oddness, conjugation, and a nonzero derivative at the center do not make Hermitian \(z\)-confinement equivalent to critical-line confinement. A source affine normalization \(z=a(s-\tfrac12)\) with real \(a\ne0\), or a global theorem that the preimage of the imaginary axis is exactly the critical line, is indispensable.

## Mellin-generator normalization

The additive Tate source supplies that affine normalization. Its normalized dilation action is

\[
(V_a h)(q)=e^{a/2}h(q+a),
\qquad
G=\partial_q+\tfrac12,
\]

and Fourier reversal obeys \(KG=-GK\). On the Mellin mode \(h_s(q)=e^{-sq}\),

\[
Gh_s=(\tfrac12-s)h_s.
\]

Hence the drift coefficient in \(u'=-zu\) is source-normalized as

\[
z=s-\tfrac12,
\]

up to the already displayed sign convention between the two sheets. This excludes nonlinear odd reparameterizations such as \(w+w^3\): they are not eigenvalues of the frozen first-order Mellin generator. Therefore the Hermitian conclusion \(\operatorname{Re}z=0\) is exactly \(\operatorname{Re}s=\tfrac12\). The path coordinate \(q\) is logarithmic dilation, not physical time. This repairs spectral typing but does not supply endpoint source-work sewing.

## Fourier-reversal sewing test

Reciprocal sheet sewing does not cancel the Hermitian source work. On a symmetric logarithmic interval, the conjugate reciprocal relation may be written

\[
v(q)=\overline{u(-q)}.
\]

Compatibility with the forward-forced equations requires
\(\overline{F(-q)}=-F(q)\). For

\[
W(q)=\operatorname{Re}\!\left(F(q)(\bar u(q)-\bar v(q))\right),
\]

the reciprocal relations give

\[
W(-q)=W(q).
\]

The source-work density is even, so its ordinary integral doubles rather than vanishes. The alternative reciprocal sign convention with even forcing gives the same conclusion. Reversing orientation on the second Fourier chart can cancel the work integral, but it simultaneously reverses the Green bulk contribution; this recovers the previously identified doubled-contour identity rather than a positive confinement law. Therefore exact Fourier reversal and forcing covariance do not provide endpoint work sewing.

## Evans-derivative test

A constant-forcing solution gives an exact obstruction to identifying source work with the scalar ideal. On \([0,L]\), take constant \(f\), impose \(w(0)=0\), and write \(r(0)=r_0\). For \(z\ne0\),

\[
r(q)=A\cosh(zq)-\frac{2cf}{z},
\qquad
w(q)=-A\sinh(zq),
\qquad
A=r_0+\frac{2cf}{z}.
\]

The terminal scalar is

\[
\Xi(z)=w(L)=-A\sinh(zL),
\]

whereas the accumulated source work is

\[
I_F(z)=c\int_0^Lfr(q)dq
=cf\left(\frac{A\sinh(zL)}{z}-\frac{2cfL}{z}\right).
\]

At every nonzero geometric zero \(z=i\pi n/L\) with \(A\ne0\), \(\Xi(z)=0\) but

\[
I_F(z)=-\frac{2c^2f^2L}{z}\ne0.
\]

These zeros are generically simple, so replacing \(\Xi\) by its spectral derivative would not make work vanish; it would instead turn sewing into an additional multiplicity or criticality condition. Thus source work belongs neither to the radical ideal of the terminal scalar nor to an automatic Evans-derivative zero relation.

## Reciprocal passivity sandwich

There is a weaker route than work sewing if the reflected boundary-value problems are compared with the same standard path orientation. With common-mode nullity at both endpoints, the Hermitian identity gives

\[
\delta B=-R,
\qquad
\delta=\operatorname{Re}z,
\quad
B=\int(|u|^2+|v|^2),
\quad
R=\int W.
\]

Universal passivity \(R\ge0\) would imply \(\delta\le0\). Applying the same bound to the functional-equation partner \(z^\#=-\bar z\) gives \(-\delta\le0\), hence \(\delta=0\).

Exact reciprocal response covariance is stronger and removes the sign axiom. If the reflected solution has

\[
B^\#=B,
\qquad
R^\#=R,
\]

then its Green identity is \(-\delta B=-R\). Together with \(\delta B=-R\), positive \(B\) forces \(\delta=R=0\). This comparison does not sum the oppositely oriented Fourier charts; it compares two reoriented boundary-value problems. Its unresolved gates are substantive: scalar nullity must close the common mode at both endpoints, and source Fourier transport must preserve the Hermitian bulk and ordinary work integral under that reorientation. Without those maps the argument is conditional, but endpoint work sewing is no longer separately required.

The exact source covariance fails the required work sign. For
\(z^\#=-\bar z\), the reflected solution is obtained at fixed path orientation by the sheet swap

\[
u^\#=v,
\qquad
v^\#=u.
\]

It satisfies the reflected drift equations with the same forcing. Consequently

\[
B^\#=B,
\qquad
W^\#=-W,
\qquad
R^\#=-R.
\]

The reflected Green identity is therefore

\[
-\delta B=R,
\]

which is exactly the negative of \(\delta B=-R\), not an independent equation. The reciprocal sandwich collapses to one identity. Imposing passivity on both reflected problems would force \(R=0\), but because source covariance exchanges \(R\) with \(-R\), that passivity condition is itself the missing asymmetric selector. Reciprocal response covariance cannot replace work sewing.

## One-sided passivity audit

A universal inequality \(R\ge0\) on every scalar-zero response would be sufficient: \(\delta B=-R\) excludes \(\delta>0\), and the functional equation reflects every \(\delta<0\) zero to one with positive transverse coordinate. The approved positive valuation cone does not supply such a universal domain. Fourier reflection exchanges the two cones and sends \(R\) to \(-R\). If a passivity domain contains both members of every reflected response pair, nonnegativity forces \(R=0\) and has inserted the desired sewing. If it contains only one cone, the reflected zero lies outside the domain, so the functional equation cannot apply the bound to eliminate the opposite half-plane. Projecting the reflected state back into the chosen cone changes the response and need not preserve scalar nullity.

Thus one-sided passivity closes confinement only with an additional selection arrow assigning every scalar zero a response in one fixed passive domain while preserving functional-equation reflection. No such arrow is source-derived; cone polarization alone is insufficient.

A sign-adapted formulation avoids demanding one Fourier-stable cone. For \(\delta\ne0\), select the positive or negative valuation cone according to \(\operatorname{sgn}\delta\) and require

\[
\operatorname{sgn}(\delta)R\ge0.
\]

Since every scalar-zero response with endpoint common-mode closure satisfies \(\delta B=-R\), this estimate gives

\[
|\delta|B=-\operatorname{sgn}(\delta)R\le0.
\]

Positive \(B\) then forces \(\delta=0\). This is a valid conditional confinement theorem, and using the known sign of the spectral parameter to choose a cone is not itself circular. The missing source content is now exact: a scalar-null-preserving map into the sign-adapted cone and an identification of its contraction/dissipation form with the work pairing \(R\). The approved valuation shifts supply a norm defect on each cone, but no map equates that defect with \(R\) for the reconstructed sheet response. Sign adaptation therefore sharpens the asymmetric interface without completing it.

## Unilateral-shift realization

The valuation cone gives an exact abstract model of the required sign. On the cone selected for \(\delta\), let

\[
W_\delta=p^{-|\delta|}S,
\]

where \(S\) is the unilateral forward shift. Then

\[
D_\delta(x)=\|x\|^2-\|W_\delta x\|^2
=(1-p^{-2|\delta|})\|x\|^2\ge0.
\]

The oriented candidate \(R_\delta=\operatorname{sgn}(\delta)D_\delta\) has exactly the passivity sign needed above. This is only a realization of the abstract inequality. The source work is

\[
R=\operatorname{Re}\int F(\bar u-\bar v),
\]

which is a forcing--response pairing, whereas \(D_\delta\) is a norm defect of an arbitrary valuation state. No approved map sends the scalar-zero sheet response to \(x\) and proves \(R=R_\delta\). Universally such an identity is impossible without restricting the response graph, because \(R\) is sign-indefinite while \(D_\delta\ge0\). On the purely forced sector it would amount to proving that the forcing-to-relative-mode transfer has a sign-adapted positive Hermitian part. The unilateral shift supplies the target passive colligation, not that transfer identification.

## Forcing-response positive-real test

The declared flow determines the sign of its transfer exactly, and it is opposite to the proposed passivity. Write \(z=\delta+i\tau\) and apply the unitary gauge

\[
U=e^{i\tau q}u,
\qquad
V=e^{i\tau q}v,
\qquad
F_\tau=e^{i\tau q}F.
\]

Then

\[
U'=-\delta U-F_\tau,
\qquad
V'=\delta V-F_\tau.
\]

For \(r=U-V\), common-mode nullity at both endpoints gives Neumann data and

\[
(-\partial_q^2+\delta^2)r=-2\delta F_\tau.
\]

Hence, for real \(\delta\ne0\),

\[
R=\operatorname{Re}\langle F_\tau,r\rangle
=-\frac{\|r'\|^2+\delta^2\|r\|^2}{2\delta},
\]

so

\[
\operatorname{sgn}(\delta)R<0
\]

for every nonzero relative response. The forcing-to-response operator
\(-2\delta(-\partial_q^2+\delta^2)^{-1}\) is self-adjoint with the anti-passive sign forced by the Green identity. Reversing the port sign can call it passive, but then the work term in the Green law reverses too and yields no contradiction. The proposed sign-adapted positive-real identification is therefore incompatible with the actual source transfer, not merely absent.

## Two-endpoint nullity test

The functional equation pairs terminal zeros but does not turn terminal common-mode nullity into initial nullity. In the unforced homogeneous flow on \([0,L]\),

\[
u(q)=u_0e^{-zq},
\qquad
v(q)=v_0e^{zq},
\]

so the terminal scalar is

\[
\Xi(z)=u_0e^{-zL}+v_0e^{zL}.
\]

For fixed nonzero \(u_0,v_0\), its zeros satisfy

\[
e^{2zL}=-\frac{u_0}{v_0}.
\]

At every such zero, \(w(L)=0\), while

\[
w(0)=u_0+v_0
\]

is generically nonzero. If \(|u_0|\ne|v_0|\), these zeros have nonzero transverse part

\[
\operatorname{Re}z=\frac{1}{2L}\log\left|\frac{u_0}{v_0}\right|.
\]

Sheet swap produces the reflected boundary-value problem and its paired zero, but preserves the distinction between initial and terminal evaluations. Thus even exact drift reciprocity, positive sheet norm, and a functional-equation zero pair do not supply two-endpoint common-mode closure. A source boundary transport identifying the reflected terminal readout with the original initial readout remains necessary.

## Hankel endpoint-readout test

The additive Tate Fourier operator cannot supply that transport as a pointwise endpoint identity. Its logarithmic-sheet action is Hankel:

\[
(Kh)(q)=\int k(q+r)h(r)\,dr.
\]

Therefore

\[
(Kh)(b)=\int k(b+r)h(r)\,dr
\]

is a global moment functional of \(h\), not the opposite endpoint evaluation \(h(a)\). Equality \((Kh)(b)=\alpha h(a)\) for every admissible \(h\) would require the distributional kernel \(k(b+r)=\alpha\delta(r-a)\), whereas the source Hankel kernel is not such a delta readout. Translation reversal \(KV_a=V_{-a}K\) reverses the generator action but does not convert this global functional into point evaluation.

Restricting to a one-dimensional vacuum line makes endpoint evaluations proportional only because all states are scalar multiples of one vector; then terminal nullity forces the selected state itself to vanish whenever the terminal evaluation is nonzero on that line, eliminating positive bulk. Hence neither the full Hankel operator nor vacuum restriction derives the required terminal-to-initial common-mode map.

## Moment-tower reconstruction test

Passing from one Hankel endpoint value to all polynomial moments still does not construct opposite-endpoint evaluation on the source Schwartz domain. For

\[
m_k(h)=\int q^k h(q)dq,
\]

one has \(m_k(h)=i^k\widehat h^{(k)}(0)\) up to the Fourier convention. Choose a nonzero smooth Fourier profile supported away from the origin and let \(h\) be its inverse Fourier transform. Then \(h\) is Schwartz and

\[
m_k(h)=0\quad\text{for every }k,
\]

while \(h(a)\) is not forced to vanish. Thus the raw full moment tower is not jointly faithful on the admitted Schwartz carrier. Every finite moment truncation is still less informative.

A quasi-analytic or Gaussian-restricted domain can make moments determining, but source scalar nullity supplies only one terminal functional, not vanishing of the complete tower. Such a restriction would also need a proved map from scalar zeros to all moment coordinates and preservation of positive sheet energy. The moment observer therefore cannot promote terminal nullity to initial nullity without both a stronger source domain and a jointly faithful scalar-to-tower map.

## Theta quasi-analyticity test

Theta completion can place the scalar in an entire, moment-determinate class without promoting one zero to the moment tower. The finite positive-measure model

\[
\mu=\tfrac12(\delta_{-1}+\delta_1),
\qquad
\Xi(t)=\int e^{itu}d\mu(u)=\cos t
\]

is entire and determined by its derivatives, yet

\[
\Xi(\pi/2)=0,
\qquad
\Xi'(\pi/2)=-1.
\]

Thus scalar nullity supplies one phase-cancellation relation, not vanishing of derivative moments. Quasi-analyticity states that vanishing of the complete derivative jet determines the function; it does not infer that jet from the zeroth coordinate. The same distinction applies to a positive theta measure. Consequently theta analyticity can make a full tower faithful after it is known, but cannot construct that tower from a scalar zero or derive opposite-endpoint nullity.

## Theta differential-equation test

A finite constant-coefficient spectral ODE cannot generate the missing jet for a genuine theta measure. If

\[
\Xi(t)=\int e^{itu}d\mu_\theta(u)
\]

satisfied \(P(\partial_t)\Xi=0\) for a nonzero polynomial \(P\), Fourier uniqueness would require

\[
P(iu)=0
\]

on the support of \(\mu_\theta\). Infinite theta support makes this impossible for finite-degree \(P\). The heat equation supplies a homogeneous PDE only after adjoining an auxiliary scale and its full spatial derivative tower; restriction to one spectral coordinate recreates the infinite moment hierarchy.

Even a supplied finite-order variable-coefficient ODE would not promote one zero to a solution jet: an order-\(m\) uniqueness theorem requires \(m\) initial coordinates, while scalar nullity gives only one. The source theta PDE therefore neither supplies a finite boundary-state system nor propagates a single scalar zero into the endpoint data required by the Green argument.

## Heat-state observability test

Even persistence of one Fourier zero along the full heat parameter does not observe the theta state. Let the initial datum on the real line be a positive symmetric Gaussian mixture centered at \(\pm a\). Its heat continuation remains a strictly positive Gaussian mixture, while its Fourier transform has the form

\[
\widehat\Theta_t(\xi)
=e^{-\gamma(t)\xi^2}\cos(a\xi),
\qquad \gamma(t)>0.
\]

For every heat parameter, it vanishes at

\[
\xi=\frac{\pi/2+\pi k}{a},
\]

although \(\Theta_t\) is nonzero and positive. The heat semigroup damps each Fourier mode but does not mix a zero mode into a jointly faithful observation. A scalar theta zero at one spectral point is weaker still. Heat unique continuation concerns vanishing on an open spacetime set or sufficient Cauchy data, not one Fourier coefficient. Hence theta PDE observability cannot supply the state or endpoint nullity needed for confinement.

## Quadratic-storage forcing test

No constant Hermitian quadratic storage can simultaneously produce a positive sheet bulk and couple the common forcing only to the common mode. After removing the tangential phase, write

\[
x'=\delta D x-Fe,
\qquad
D=\operatorname{diag}(-1,1),
\qquad
e=(1,1)^T.
\]

For \(K=x^*Px\), with

\[
P=\begin{pmatrix}a&b\\\bar b&d\end{pmatrix},
\]

the homogeneous bulk is governed by

\[
DP+PD=\begin{pmatrix}-2a&0\\0&2d\end{pmatrix}.
\]

A positive bulk requires \(a>0\) and \(d<0\). For the forcing term to depend only on the common mode, the row

\[
e^*P=(a+\bar b,\ b+d)
\]

must be proportional to \((1,1)\), which requires

\[
a-d=b-\bar b.
\]

The left side is positive real while the right side is purely imaginary, an impossibility. Exact bulk \(|U|^2+|V|^2\) further fixes \(a=1,d=-1\). Thus changing the constant quadratic current cannot move the forcing residual into the scalar common channel while retaining positivity. A variable storage cannot repair both bulk and boundary simultaneously. In common/relative coordinates, forcing through the common channel requires a Hermitian storage to be diagonal,

\[
P(q)=\operatorname{diag}(p(q),r(q)).
\]

For homogeneous drift matrix \(-\delta\sigma_x\), the negative storage derivative has bulk matrix

\[
-H(q)=
\begin{pmatrix}
-p'&\delta(p+r)\\
\delta(p+r)&-r'
\end{pmatrix}.
\]

Local positive choices exist, so variable coefficients evade the constant algebraic obstruction. Automatic boundary closure from common-mode nullity \(w=0\), however, requires the relative coefficient to vanish at both endpoints: \(r(q_0)=r(q_1)=0\). Positive semidefiniteness of \(-H\) forces \(-r'\ge0\), so \(r\) is nonincreasing. Equal zero endpoint values then give \(r'\equiv0\); positivity of a matrix with lower diagonal zero forces the off-diagonal entry to vanish, leaving no strictly positive relative-mode bulk. If the endpoint coefficients are not both zero, storage closure becomes a new condition on the uncontrolled relative endpoint values. Variable quadratic storage therefore trades the forcing residual for the same independent boundary datum.

## Smooth local-storage no-go

The obstruction is not specific to quadratic storage. Let \(K(w,r)\) be any differentiable local scalar current. For scalar common-mode nullity to close its endpoints without knowing the relative endpoint values, \(K(0,r)\) must be independent of \(r\). On the common-null line the source vector field is

\[
w'=-\delta r-2F,
\qquad
r'=0.
\]

Hence

\[
\mathcal L_VK(0,r)=K_w(0,r)(-\delta r-2F).
\]

Eliminating the forcing term for arbitrary source amplitude requires \(K_w(0,r)=0\). The spectral term \(-\delta rK_w(0,r)\) then vanishes as well, so the derivative cannot equal a strictly negative positive-energy density on a nonzero relative state. If \(K_w\ne0\), the current retains the forcing work and its endpoint closure is the unsourced work-orthogonality condition. Therefore no differentiable local current can obtain automatic scalar-null boundary closure, forcing cancellation, and positive relative bulk simultaneously.

## Minimal nonlocal memory state

The forcing residual has a universal one-dimensional dynamic extension. Introduce

\[
\eta'=2\operatorname{Re}\!\left(F(\bar u-\bar v)\right),
\qquad
\eta(q_0)=0,
\]

and set

\[
J_{\rm ext}=|u|^2-|v|^2+\eta.
\]

Then

\[
J_{\rm ext}'=-2\operatorname{Re}(z)(|u|^2+|v|^2).
\]

This accumulator is minimal in the following sense: any differentiable extension whose derivative cancels the forcing term must change its storage coordinate by

\[
\Delta K_{\rm mem}=2\int_{q_0}^{q_1}
\operatorname{Re}\!\left(F(\bar u-\bar v)\right)dq
\]

along each solution, up to a first integral. When common-mode nullity kills the local sheet current at both endpoints, extended-current closure is therefore exactly zero work holonomy. Reparameterizing the memory or expressing it through a primitive of \(F\) cannot alter that endpoint increment; it only redistributes it among additional mixed terms. A reset, periodic memory, or zero-holonomy law would be a new source readout. Nonlocal extension solves local current construction but cannot derive its boundary closure.

## Memory reset and reversibility

Exact reciprocal transport does not reset the accumulator. Sheet reflection sends the work density to its negative, so with the same zero initial memory,

\[
\eta^\#(q)=-\eta(q).
\]

The reflected endpoint increments cancel only after adding the two opposite problems; neither increment vanishes individually, and the corresponding Green identities remain redundant. More generally, an invertible reversible memory transport cannot map every admissible memory input to one fixed terminal reset state. A cyclic return from \(\eta(q_0)=0\) can occur only on a restricted zero-holonomy response class.

Adding \(\eta'=-\gamma\eta+2W\) or imposing a hard terminal reset changes the source dynamics and the exact Green identity. Such a map may define a dissipative or readout extension only after a process type, orientation, sink, and boundary authority are declared; the logarithmic path coordinate has no physical-time meaning by default. Fourier reversibility therefore cannot supply memory closure. The minimal new datum is an explicitly asymmetric record/reset map whose zero endpoint value is proved on scalar-zero responses.

## Valuation-boundary reset test

The canonical unilateral boundary does not provide that zero record. For the forward shift on \(\ell^2(\mathbb N)\),

\[
P_0=I-SS^*
\]

projects onto the zero-valuation line. The source-selected Gaussian valuation vector has nonzero coefficient \(g_0\), so

\[
P_0g=g_0e_0\ne0.
\]

This coefficient is fixed by the source vacuum and does not vanish when an unrelated completed scalar does. Projecting it away replaces the selected state by \((I-P_0)g\) and changes its Fourier--Poisson data. Multiplying the boundary record by \(\Xi\) would enforce scalar-zero reset only by inserting the target scalar into the incidence map.

The backward-shift norm balance confirms the role of this line: its defect contains the positive term \(|x_0|^2\), which survives at zero spectral weight. The valuation boundary is therefore an active incidence channel, not an automatic memory sink. It cannot reset the accumulated work without a new source-selected state or fitted scalar factor.

## Global boundary-incidence cancellation

Primewise assembly cannot cancel this defect while preserving positivity. At finite prime set \(S\), each zero-valuation boundary projection \(P_{0,p}\) is positive. Any positive weighted aggregate

\[
Q_S=\sum_{p\in S}\alpha_pP_{0,p},
\qquad \alpha_p>0,
\]

satisfies

\[
\langle g,Q_Sg\rangle
=\sum_{p\in S}\alpha_p\|P_{0,p}g\|^2>0
\]

for the tensor Gaussian vacuum. The union projection
\(I-\prod_{p\in S}(I-P_{0,p})\) is likewise positive with nonzero vacuum expectation. Cancellation requires signed prime weights or subtraction by an archimedean channel; either makes the boundary form indefinite and demands an independently proved coefficient identity. At infinite prime number, an unweighted positive sum diverges, while regularized signed sums are not Hilbert norms. Global Euler assembly therefore amplifies or regularizes the incidence but does not produce a source-positive zero boundary record.

## Product-formula cancellation test

The arithmetic product formula has the right global shape but the wrong typed inputs. For \(a\in\mathbb Q^\times\),

\[
\log|a|_\infty+
\sum_p\log|a|_p=0,
\qquad
\log|a|_p=-v_p(a)\log p,
\]

with integer valuations and finite support. The Gaussian boundary incidences \(\|P_{0,p}g\|^2\) are positive state amplitudes, not integer multiples of \(\log p\), and no source map assigns them to the valuations of one principal idele. Likewise the primitive spectral coefficients \((\log p)p^{-s}\) vary analytically with \(s\) and cannot be valuations of a fixed rational element.

A general idele can carry nonintegral local data, but the product formula does not vanish on arbitrary ideles; zero logarithmic norm is then an additional condition. Thus archimedean cancellation follows only after constructing a principal-idele or norm-one state map from the sheet boundary data. No such map is supplied by scalar nullity, Fourier sewing, or the Gaussian vacuum. Product-formula cancellation is therefore a well-typed conditional alternative, not an available endpoint theorem.

## Analytic principal-idele map test

A regular spectral family cannot supply the missing principal ideles. The diagonal subgroup \(\mathbb Q^\times\) is discrete in the idele group, and each nonarchimedean valuation \(v_p\) is integer-valued and locally constant. Therefore any continuous source map from a connected spectral neighborhood to principal ideles is locally constant. It cannot encode analytically varying boundary coefficients such as \(p^{-s}\) or Gaussian response amplitudes.

Defining principal ideles only at the discrete zero set avoids this continuity obstruction but makes the assignment zero-located and supplies no regular source map near a zero. A norm-one idele family can vary continuously, yet forcing norm one by choosing the archimedean component as the inverse product of the finite components defines the desired cancellation rather than derives the independently given archimedean channel. Hence neither principal nor norm-one ideles provide a non-fitted analytic boundary-state map for the present spectral family.

## DPC disposition

Conjecture: the base flow determines a current whose endpoint equality follows from scalar-null common-mode data. Rival: the flow determines only a work-balance current, leaving accumulated source work independent. The risky consequence of the conjecture is that common-mode nullity at both endpoints forces the source-work integral to vanish. The exact identity above refutes that consequence: endpoint common-mode data cancels \(J_0\) but leaves the integral unrestricted. The conjecture is rejected; the rival survives this calculation but is not thereby verified as a universal explanation.

## Disposition

This leaf replaces the vague missing-current-row blocker by a sharper split:

- local current construction: solved by \(J_F\);
- endpoint sewing: equivalent to source-work orthogonality and still absent;
- confinement: conditional on positive bulk and that orthogonality, since the integrated identity then forces \(z=0\).

No physical-time interpretation is assigned to the path coordinate \(q\).
