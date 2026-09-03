# Source current-row programme synthesis

Author: `marici.Grothendieck`
Status: minimal conditional theorem; approved-source promotion refuted
Predecessors: `approved-common-path-closure-extension.md`, `source-current-row-construction.md`

## Question

What is the weakest boundary certificate that converts a zero of the completed scalar into critical-line confinement for the source-derived two-sheet flow?

## Claim boundary

The additive Tate generator fixes the transverse spectral coordinate as

\[
z=s-\tfrac12.
\]

After removing the tangential phase, the Hermitian sheet balance is

\[
J_0(q_1)-J_0(q_0)
=-2\operatorname{Re}(z)B-2R,
\]

where

\[
J_0=|u|^2-|v|^2,
\qquad
B=\int_{q_0}^{q_1}(|u|^2+|v|^2)dq,
\qquad
R=\int_{q_0}^{q_1}\operatorname{Re}\!\left(F(\bar u-\bar v)\right)dq.
\]

Define the combined boundary-work defect

\[
D_{\rm bw}=J_0(q_1)-J_0(q_0)+2R.
\]

Then the exact source identity is

\[
D_{\rm bw}=-2\operatorname{Re}(z)B.
\]

Therefore the weakest conditional theorem is:

- scalar nullity implies \(D_{\rm bw}=0\);
- the same selected response has \(B>0\);
- hence \(\operatorname{Re}(z)=0\), equivalently \(\operatorname{Re}(s)=\tfrac12\).

Separate endpoint closure and zero work holonomy are sufficient but stronger than necessary; only their combined defect must vanish. At finite polynomial cutoff, the corresponding scalar-zero promotion is set-theoretic containment of the scalar zero set in the zero set of \(D_{\rm bw}\), not matching multiplicities.

## DPC issue boundary

**Problem.** Existing source constructors provide scalar terminal nullity, Fourier reflection, positive theta or sheet structures, and local boundary channels, but no proved arrow from scalar zeros to the combined boundary-work defect.

**Bold conjecture.** Approved Fourier--Tate sewing determines \(D_{\rm bw}\) as a source boundary object that vanishes at every zero of the completed scalar, without separately imposing endpoint current closure or work orthogonality.

**Named rivals.** Componentwise sewing treats endpoint closure and work orthogonality as independent axioms. Positivity-only routes attempt to infer state nullity from one scalar matrix coefficient. Reciprocal-cancellation routes pair reflected problems but preserve only a redundant signed identity. Fitted routes define the missing boundary or archimedean term using the target scalar.

**Risky consequences.** The conjecture requires every source-compatible scalar-zero response with positive bulk to have zero combined defect. It must survive off-line homogeneous responses, forcing-generated work, Fourier sheet exchange, valuation-boundary incidence, theta heat continuation, and global finite--archimedean assembly without inserting a scalar factor.

**Strongest falsification attempt and residual.** The homogeneous exact response

\[
u(q)=u_0e^{-zq},
\qquad
v(q)=v_0e^{zq}
\]

has terminal zeros determined by \(e^{2zL}=-u_0/v_0\). For \(|u_0|\ne|v_0|\), these zeros have \(\operatorname{Re}(z)\ne0\), positive bulk, and therefore

\[
D_{\rm bw}=-2\operatorname{Re}(z)B\ne0.
\]

Sheet reflection supplies the paired zero but reverses work and adds no second constraint. The source Hankel endpoint is a global moment functional rather than opposite-endpoint evaluation; the full raw moment tower is not faithful on Schwartz space; theta analyticity and heat observability do not promote one zero to a state jet; local or variable storage either retains work holonomy or loses positive relative bulk; valuation boundaries have nonzero Gaussian incidence; product-formula cancellation lacks a principal-idele state map. The exact residual is the absent source relation

\[
\Xi(s)=0\quad\Longrightarrow\quad D_{\rm bw}(s)=0.
\]

**Disposition and surviving scope.** The bold conjecture is rejected for the approved constructors. The combined-defect theorem survives as the minimal conditional interface. A future source enlargement is progressive only if it constructs \(D_{\rm bw}\) independently of \(\Xi\), proves its scalar-zero vanishing, and preserves positive bulk; merely repartitioning the defect among current, memory, valuation, or archimedean terms is not progress.

## Linear-terminal factorization obstruction

Let \(V\) be a complex response space, let the scalar terminal readout be a nonzero linear functional \(\ell:V\to\mathbb C\), and let the combined boundary-work defect be a Hermitian quadratic form

\[
D_{\rm bw}(y)=\langle y,Hy\rangle.
\]

If terminal nullity alone is to imply defect nullity for every admissible response, then

\[
\ker\ell\subseteq\{y:\langle y,Hy\rangle=0\}.
\]

Polarization on \(\ker\ell\) gives

\[
H|_{\ker\ell\times\ker\ell}=0.
\]

After choosing \(e\in V\) with \(\ell(e)=1\), the form must therefore factor as

\[
D_{\rm bw}(y)
=2\operatorname{Re}\!\left(\overline{\ell(y)}m(y)\right)
+c|\ell(y)|^2
\]

for a linear functional \(m\) and real \(c\). In finite dimension its Hermitian matrix has rank at most two; if the form is semidefinite, it reduces to \(c|\ell|^2\) and has rank at most one.

For the homogeneous two-sheet family off the critical line,

\[
D_{\rm bw}(y)=-2\operatorname{Re}(z)\langle y,G_z y\rangle,
\]

where \(G_z\) is the positive bulk Gram matrix. On a response space of dimension greater than two this has full rank and cannot have the required terminal factorization; already on a two-dimensional sheet space, the semidefinite form cannot factor through one scalar readout unless its rank drops to one. Thus no Green-concomitant rearrangement based only on a linear scalar terminal can construct the missing implication. A viable enlargement must either restrict admissible responses to a source-proved one-dimensional subspace, provide enough jointly faithful terminal probes, or introduce an independent boundary relation. The selected Gaussian supplies a distinguished response but does not prove any of these three conditions.

## Joint terminal-probe rank

Let \(L:V\to\mathbb C^r\) collect \(r\) linear terminal probes and let \(H\) be semidefinite. If joint terminal nullity is to imply defect nullity,

\[
\ker L\subseteq\ker H.
\]

Then \(H\) descends through \(L\): on \(\operatorname{im}L\) there is a semidefinite form \(C\) such that

\[
H=L^*CL.
\]

Consequently

\[
\operatorname{rank}H\leq\operatorname{rank}L\leq r.
\]

The bound is sharp: a rank-\(k\) semidefinite defect needs at least \(k\) jointly faithful scalar probes. For the two-dimensional homogeneous sheet state, the positive bulk Gram form has rank two, so two independent probes are necessary. The functional equation supplies a reflected copy of the same completed scalar, not a second independent probe. At a simple zero, derivatives do not vanish with the scalar and therefore do not enlarge the jointly null probe family.

At an \(n\)-dimensional cutoff, full-rank bulk requires \(n\) independent probes; in the unbounded Hilbert response space, no finite-rank terminal family can dominate a coercive bulk form. Thus replacing one terminal scalar by the minimum admissible probe family amounts to faithful terminal-state reconstruction. It does not follow from scalar nullity and is stronger than the sought confinement bridge.

## Selected-response line test

Suppose the Gaussian source selects a single nonzero response \(y_s\) for each spectral parameter, so response variation is restricted to the line \(V_s=\mathbb C y_s\). Write

\[
\ell_s(y_s)=\Xi(s),
\qquad
D_s(y_s)=D_{\rm bw}(s).
\]

Away from scalar zeros one can always define

\[
c(s)=\frac{D_{\rm bw}(s)}{|\Xi(s)|^2},
\]

but this is a fitted quotient, not a source factorization. Extension across a scalar zero already requires \(D_{\rm bw}=0\), so line selection merely restates the missing implication.

The local regularity test is sharper. Near a simple zero, \(|\Xi|^2\) vanishes to second real order. On a critical-line response with positive bulk,

\[
D_{\rm bw}=-2\operatorname{Re}(z)B
\]

vanishes generically to first transverse order. Hence no bounded continuous coefficient \(c\) can satisfy \(D_{\rm bw}=c|\Xi|^2\) there. A mixed real factorization

\[
D_{\rm bw}=2\operatorname{Re}(\overline{\Xi}m)
\]

has compatible first order, but constructing \(m\) from the local coordinate \(\Xi\) after assuming defect vanishing is again tautological. At an off-line scalar zero, \(D_{\rm bw}\ne0\) directly forbids either factorization.

Thus Gaussian response selection removes the probe-rank obstruction only by transferring the entire burden to a parameter-space scalar--defect divisibility theorem. The approved source supplies no such theorem.

## Mixed defect-multiplier test

A source-derived linear multiplier would be a second response functional \(m:V\to\mathbb C\) satisfying

\[
D_{
m bw}(y)=2\operatorname{Re}\!\left(\overline{\ell(y)}m(y)\right).
\]

Its Hermitian operator is

\[
H=\ell^*m+m^*\ell.
\]

This operator has rank at most two. Moreover, if \(H\) is semidefinite, then \(m\) must be proportional to \(\ell\): otherwise a vector in \(\ker\ell\) paired with a vector outside it produces both signs under arbitrarily small perturbations. The factorization then reduces to

\[
D_{
m bw}=c|\ell|^2
\]

with rank at most one, already excluded by the positive full-rank bulk form.

On the selected parameterized response alone, a smooth mixed multiplier exists locally near a simple zero whenever \(D_{\rm bw}\) is already known to vanish there. Indeed, using \(\operatorname{Re}\Xi\) and \(\operatorname{Im}\Xi\) as local coordinates, any smooth vanishing real function can be written as \(2\operatorname{Re}(\overline\Xi m)\). This is an ideal-membership restatement of the desired zero containment, not an independent derivation.

Thus a mixed multiplier has two exhaustive readings: as a linear response functional it fails the semidefinite rank test; as a coefficient defined only on the selected spectral curve it presupposes defect vanishing. It supplies no source-compatible bridge.

## Source boundary-isotropy test

Write the sheet current as \(J_0(x)=x^*Kx\) with

\[
K=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

For a linear sewing map \(U\), its boundary graph is isotropic for the Green boundary form precisely when

\[
U^*KU=K.
\]

The source Fourier sewing exchanges the two sheets. With

\[
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

one instead has

\[
S^*KS=-K.
\]

Hence the Fourier graph is anti-isometric, and its boundary residual is

\[
J_0(Sx)-J_0(x)=-2J_0(x),
\]

which vanishes only on the sheet-null cone. Scalar terminal nullity does not select that cone.

Adjoining the work accumulator \(\eta'=2\operatorname{Re}(F(\bar u-\bar v))\) turns the combined defect into the endpoint difference of \(J_0+\eta\). But Fourier sewing provides no transformation law for \(\eta\). Assigning an endpoint shift that cancels \(-2J_0\) defines the required work correction from the defect and is therefore fitted. Identity sewing would preserve \(J_0\), but it is not the source Fourier exchange; restricting to the common-mode subspace makes the two agree only after imposing the previously missing state constraint.

Thus the approved boundary transport does not land in an isotropic subspace for the combined Green form. Boundary isotropy remains a valid independent certificate, not a consequence of Fourier--Poisson sewing.

## Doubled reflected-graph test

Because \(S^*KS=-K\), the Fourier graph \(\{(x,Sx)\}\) is isotropic for the doubled same-sign form

\[
K\oplus K:
\qquad
J_0(x)+J_0(Sx)=0.
\]

This does not make it isotropic for the Green endpoint form \((-K)\oplus K\), whose restriction is \(-2J_0(x)\).

The same distinction appears in the bulk identities. A reflected pair has transverse coordinates with opposite real parts, so under matched bulk and work data,

\[
D_{\rm bw}(z)+D_{\rm bw}(z^\#)=0
\]

holds identically. This is the same-sign doubled isotropy. It cancels the two positive bulks after their coefficients acquire opposite signs and therefore leaves no equation proportional to \(\operatorname{Re}(z)B\). The difference of the two identities retains that term but doubles, rather than cancels, the boundary residual.

Thus doubling converts Fourier anti-isometry into an isotropic graph only in the direct-sum form that also erases the confinement signal. It supplies a reciprocal conservation identity, not an independent boundary condition.

## Fourier-square boundary-cycle test

Two Fourier exchanges restore the sheet-current form because \(S^2=I\); on the base function space the Fourier square is parity, which preserves the relevant norms and fixes the even Gaussian. Let the two reflected legs have positive bulks \(B_1,B_2\). Their transverse coordinates have opposite real parts, so

\[
D_1=-2\operatorname{Re}(z)B_1,
\qquad
D_2=+2\operatorname{Re}(z)B_2.
\]

Closing the two-leg cycle yields

\[
D_1+D_2=-2\operatorname{Re}(z)(B_1-B_2).
\]

Fourier unitarity and the reflected source identification give \(B_1=B_2\), so the cycle equation is identically zero for every \(z\). The difference

\[
D_1-D_2=-2\operatorname{Re}(z)(B_1+B_2)
\]

retains a positive bulk coefficient, but it is not the closed-cycle boundary form. Deliberately choosing \(B_1\ne B_2\) would create a confinement equation only by breaking the source Fourier identification.

Thus Fourier-square closure is isometric but redundant: the same symmetry that closes the boundary cycle equalizes the bulks and removes the transverse constraint.

## Reciprocal Mellin-weighted cycle

A meromorphic functional-equation coefficient \(\lambda(s)\) may obey

\[
\lambda(s)\lambda(1-s)=1.
\]

If it were a Hilbert-state transport, a reflected leg scaled by \(\lambda\) would have \(B_2=|\lambda(s)|^2B_1\), and a closed two-leg balance would formally contain

\[
2\operatorname{Re}(z)\bigl(|\lambda(s)|^2-1\bigr)B_1.
\]

This formal expression does not define the needed positive cycle. Mellin--Plancherel fibers are Hilbert fibers only on the unitary axis \(s=\tfrac12+it\). Off that axis, \(\lambda(s)\) is a meromorphic coefficient between analytically continued generalized characters, not a bounded state map whose modulus rescales a positive bulk norm. Treating \(|\lambda(s)|^2B_1\) as a transported Hilbert bulk therefore imports the critical-line unitary structure into the region where confinement is to be proved.

Conversely, retaining the genuine unitary Fourier transport fixes the reflected bulk norm and returns the redundant equal-bulk cycle. A source-positive weighted cycle would require a separately constructed off-axis Hilbert bundle, positive fiber metric, and reciprocal transport law whose monodromy determinant is the completed scalar. None is supplied by Tate completion or the Gaussian test vector.

Thus the reciprocal Mellin factor is analytic functional-equation data, not a positive nonunitary boundary transport. It cannot bridge scalar nullity to the Green bulk without a new Hilbert-bundle realization.

## Weighted Mellin fiber metric

For each real \(\sigma\), the natural positive weighted space

\[
\mathcal H_\sigma=L^2(\mathbb R_+,x^{2\sigma-1}dx)
\]

has Mellin--Plancherel transform on the line \(s=\sigma+it\). Fourier reciprocity acts there by a gamma-factor multiplier and reflection,

\[
\mathcal M(\mathcal Ff)(s)=\gamma(s)\mathcal Mf(1-s).
\]

Off the unitary line, \(|\gamma(\sigma+it)|\) has nonconstant power growth in \(|t|\). Thus multiplication by \(\gamma\) and its reciprocal cannot both be bounded between the unmodified natural Plancherel fibers unless \(\sigma=\tfrac12\). The weighted spaces are individually positive, but they do not form the reciprocal bounded Hilbert transport required by the cycle.

One can redefine a fiber metric by inserting \(|\gamma|\)-dependent weights so that reciprocity becomes unitary. This has two defects for the present use: the reciprocal metric is not uniquely selected, since any positive reflection-invariant weight may be added, and exact unitarization makes the reflected bulk norms equal, restoring the redundant cycle. Leaving the transport nonunitary preserves unequal formal norms but forfeits the bounded source map needed to compare positive bulks.

Therefore natural weighted Mellin spaces do not realize the proposed off-axis positive cycle. Metric renormalization either inserts extra choice or removes the only asymmetry that could produce confinement.

## Gaussian domain of the unbounded cycle

The selected Gaussian does evade the domain part of the preceding obstruction. For \(g(x)=e^{-\pi x^2}\),

\[
\|g\|_{\mathcal H_\sigma}^2
=\int_0^\infty e^{-2\pi x^2}x^{2\sigma-1}dx
=\tfrac12(2\pi)^{-\sigma}\Gamma(\sigma),
\]

which is finite for \(\sigma>0\). Both reflected norms are finite throughout \(0<\sigma<1\), and Fourier fixes the even Gaussian. Hence lack of a bounded operator on the whole weighted space does not exclude an unbounded reciprocal construction on this selected vector.

The two finite norms are generally unequal, but that fact alone is not a Green identity. The sheet-flow bulk is an integral of \(|u(q)|^2+|v(q)|^2\) over the declared dilation coordinate, whereas the formulas above are weighted base-space norms. Equating them requires an explicit intertwiner from the Gaussian Mellin fibers to the two-sheet response, including its forcing, endpoint traces, and work term. Without that map, subtracting the two Gaussian norms compares different positive spaces but does not produce the combined boundary-work defect.

Thus the Gaussian-domain proposal survives the boundedness test but remains conditional on a source-derived weighted-fiber-to-sheet-flow intertwiner. This is a narrower unresolved branch, not evidence for confinement.

## Weighted-fiber to sheet-flow intertwiner

Set \(x=e^q\) and use the half-density Gaussian envelope

\[
a(q)=e^{q/2}g(e^q).
\]

The natural candidate sheets

\[
u(q)=e^{-zq}a(q),
\qquad
v(q)=e^{zq}a(q)
\]

have squared integrals equal to the reflected weighted Gaussian norms. For \(0<\operatorname{Re}(s)<1\), both also vanish at \(q=\pm\infty\), so their bare endpoint current closes.

The candidate does not intertwine the approved common-forcing flow. Its derivatives are

\[
u'=-zu+e^{-zq}a',
\qquad
v'=zv+e^{zq}a'.
\]

Matching the approved common-forcing equations

\[
u'=-zu-F,
\qquad
v'=zv-F
\]

would require simultaneously

\[
F=-e^{-zq}a'=-e^{zq}a'.
\]

For the nonconstant Gaussian envelope this fails on every interval. Allowing separate sheet forcings realizes the two weighted norms, but then their work terms are independent and exactly retain the defect that endpoint closure was meant to remove. Replacing one envelope by a solution of the common-forcing compatibility equation destroys its identification with the reflected Gaussian weighted norm.

Hence the canonical logarithmic half-density map preserves the desired bulks and endpoints but fails the source forcing interface. The exact residual is the nonzero forcing mismatch

\[
(e^{-zq}-e^{zq})a'(q).
\]

## Common-forcing compatible reflected envelope

Keep \(u=e^{-zq}a(q)\) and write \(v=e^{zq}b(q)\). Common forcing is equivalent to

\[
b'(q)=e^{-2zq}a'(q).
\]

For the Gaussian half-density, imposing zero constants at both ends requires

\[
0=\int_{-\infty}^{\infty}e^{-2zq}a'(q)dq
=2z\int_{-\infty}^{\infty}e^{-2zq}a(q)dq.
\]

The remaining integral is a Gaussian Mellin gamma factor and has no zeros in its convergence domain. Thus simultaneous two-endpoint envelope closure forces \(z=0\), not the full critical line and not the completed-scalar zero set.

For \(\operatorname{Re}(z)\ne0\), one may instead choose the integration constant so that \(v=e^{zq}b\) vanishes on the exponentially growing side; the opposite side then decays automatically. This produces bare endpoint closure off the critical line, but \(b\) is no longer the reflected Gaussian envelope and the exact balance assigns the transverse bulk to nonzero work,

\[
R=-\operatorname{Re}(z)B.
\]

Hence solving common-forcing compatibility yields either an overstrong central-point condition under two-sided envelope normalization or an off-line family with uncompensated work. It does not preserve the weighted Fourier cycle needed for scalar-null confinement.

## Theta--Mellin compatible envelope

Normalize the standard theta-derived bilateral kernel \(a_\theta(q)\) so that, up to a fixed nowhere-zero completion factor and the declared dilation rescaling,

\[
\Xi\!\left(\tfrac12+z\right)
=\int_{-\infty}^{\infty}e^{-2zq}a_\theta(q)dq.
\]

Use \(u=e^{-zq}a_\theta\) and define the second envelope by common-forcing compatibility,

\[
b'=e^{-2zq}a_\theta',
\qquad
v=e^{zq}b.
\]

The two-sided compatibility residual is

\[
\int_{-\infty}^{\infty}e^{-2zq}a_\theta'(q)dq
=2z\,\Xi\!\left(\tfrac12+z\right)
\]

with the same harmless completion normalization. Therefore a noncentral scalar zero supplies a source-derived choice of integration constant for which the compatible envelope closes at both ends. This is a genuine promotion from scalar nullity to bare endpoint-current closure; unlike the Gaussian gamma moment, the theta moment has the target zeros.

It does not close the combined defect. With both endpoint currents zero, the exact Hermitian identity becomes

\[
R=-\operatorname{Re}(z)B,
\qquad
D_{\rm bw}=2R=-2\operatorname{Re}(z)B.
\]

Thus the theta zero removes the linear envelope boundary obstruction but leaves the quadratic work pairing unchanged. Proving \(R=0\) for this theta-selected compatible pair would yield confinement; it is not a consequence of the Mellin moment already used for endpoint closure.

## Theta-envelope work pairing

At a scalar zero, the theta moment closes the compatible envelope at both ends. The exact Hermitian balance then computes rather than merely bounds the remaining work:

\[
R_\theta(z)=-\operatorname{Re}(z)B_\theta(z).
\]

Since the constructed response is nonzero, \(B_\theta(z)>0\). Therefore

\[
R_\theta(z)=0
\quad\Longleftrightarrow\quad
\operatorname{Re}(z)=0
\]

on the scalar-zero locus. Work orthogonality for this envelope is consequently equivalent to the desired confinement statement, not an independent theta identity.

Theta reflection does not add it. The source kernel may be even before spectral weighting, but factors \(e^{\pm zq}\) break cancellation parity when \(\operatorname{Re}(z)\ne0\). Pairing the reflected zero changes the sign of the transverse coefficient and reproduces the reciprocal cancellation already audited; it does not force either individual work integral to vanish.

Thus the construction gives a precise reformulation: completed-scalar zeros are exactly the parameters where the theta-compatible common-forcing response has closed bare endpoints, and critical-line confinement is exactly zero accumulated work for that response. The latter remains the unresolved source boundary theorem.

## Theta work versus scalar derivatives

The scalar and its first derivative are linear moments of the theta envelope,

\[
\Xi(z)=\int e^{-2zq}a_\theta(q)dq,
\qquad
\Xi'(z)=-2\int q e^{-2zq}a_\theta(q)dq.
\]

The compatible second sheet is a Volterra transform,

\[
b(q)=C+\int_{-\infty}^{q}e^{-2zt}a_\theta'(t)dt,
\]

so its work pairing contains an ordered double integral with kernel supported on \(t<q\). This kernel is not a finite sum of separable moment kernels. Consequently the work cannot be reconstructed from \(\Xi\) and finitely many spectral derivatives by the Mellin representation alone.

The failure is stable under source-envelope perturbation: at fixed \(z\), the common kernel of any finite list of Mellin moments is infinite-dimensional. Perturbations in that kernel preserve the scalar jet and the endpoint compatibility moment while changing the positive bulk and hence, on the closed-endpoint locus,

\[
R=-\operatorname{Re}(z)B.
\]

Thus an identity such as \(R=2\operatorname{Re}(\overline\Xi M)\), with \(M\) constructed from a finite scalar jet, requires an additional theta-specific infinite-rank relation. Neither Mellin differentiation nor the functional equation supplies it.

## Full-transform representation of theta work

The full bilateral transform does determine the quadratic data. For the first sheet, Mellin--Plancherel gives

\[
\int_{\mathbb R}e^{-2\delta q}|a_\theta(q)|^2dq
=\frac1{2\pi}\int_{\mathbb R}
|A_\theta(\delta+it)|^2dt,
\]

where \(A_\theta\) is the bilateral transform identified, after fixed rescaling and completion, with \(\Xi\). The compatible second sheet is obtained by applying the Volterra multiplier to the same full transform, so its norm and the work pairing are likewise quadratic functionals of the complete vertical-line data.

This representation confirms rather than removes the obstruction. A point zero of \(A_\theta\) has measure zero in the positive Plancherel integral and does not annihilate either sheet norm. On the scalar-zero endpoint locus the full-transform functional remains

\[
R_\theta=-\delta B_\theta,
\qquad B_\theta>0.
\]

Thus the full transform reconstructs the work, but scalar evaluation at one spectral point does not control that global quadratic norm. Any implication from one point zero to zero work must add a reproducing-kernel or de Branges-type positivity theorem beyond Mellin--Plancherel reconstruction.

## Reproducing-kernel positivity test

A de Branges bridge would require an entire function \(E\) with

\[
\Xi\!\left(\tfrac12+iw\right)=\frac{E(w)+E^\#(w)}2
\]

and the Hermite--Biehler inequality

\[
|E(w)|>|E^\#(w)|
\qquad (\operatorname{Im}w>0).
\]

Its reproducing kernel then has positive diagonal proportional to

\[
\frac{|E(w)|^2-|E^\#(w)|^2}{\operatorname{Im}w}.
\]

At a zero of the displayed symmetric part, \(E^\#=-E\); strict positivity therefore excludes zeros off the real \(w\)-axis and gives the desired confinement.

The theta-compatible sheet construction does not derive this kernel. De Branges positivity comes from a homogeneous canonical system with a positive Hamiltonian and a Lagrange boundary identity. The theta sheet system is inhomogeneous, and its Lagrange identity contains exactly the accumulated work term

\[
R_\theta=-\operatorname{Re}(z)B_\theta
\]

on scalar-zero closed endpoints. Removing that term is the unresolved confinement condition. Defining \(E\) from \(\Xi\) and demanding the Hermite--Biehler inequality therefore repackages the target theorem unless a source-positive homogeneous realization is separately constructed.

## Affine forcing homogenization

The forced sheet system can be made formally homogeneous by adjoining a constant source coordinate:

\[
Y=(u,v,1),
\qquad
Y'=\begin{pmatrix}-z&0&-F\\0&z&-F\\0&0&0\end{pmatrix}Y.
\]

This triangular augmentation is not a positive canonical-system realization. A nondegenerate canonical Green form has even symplectic dimension, and selfadjoint source coupling requires the adjoint of the upper-right forcing block in the lower-left block. Keeping the source coordinate constant omits that reciprocal block and leaves the generator non-selfadjoint.

Adding the required dual source coordinate repairs formal selfadjointness, but its equation is driven by the sheet state. Its endpoint increment is precisely the forcing--state pairing that appears as accumulated work. The enlarged Lagrange boundary form therefore contains the new dual-source endpoint difference,

\[
\Delta J_{\rm source}=2R_\theta.
\]

Requiring the augmented boundary trace to be isotropic is then exactly the condition \(R_\theta=0\). Affine homogenization moves work from the interior identity to an added boundary coordinate; it does not derive closure of that coordinate. A degenerate Green form can hide the dual source, but cannot yield the strict positive reproducing kernel required by the de Branges argument.

## Theta source-port adjoint boundary

Let \(B_+:\mathcal U\to\mathcal H_+\) be forward theta-source incidence. Fourier--Tate reciprocity can transport it to another forward incidence,

\[
K B_+=B_-R_{\mathcal U},
\qquad
B_-:\mathcal U\to\mathcal H_-.
\]

The reciprocal block required by a selfadjoint homogeneous augmentation has the opposite arrow direction,

\[
B_+^*:\mathcal H_+\to\mathcal U.
\]

Unitary Fourier transport does not reverse this arrow. A Riesz identification can define the adjoint only after choosing Hilbert pairings on the source and state spaces; it still evaluates the nonzero source--state overlap whose integral is the dual-coordinate increment.

For the theta-compatible response that increment is \(2R_\theta\). Reflection carries it to the opposite increment in the reciprocal sector, so the doubled increments cancel, but no individual endpoint coordinate closes. Gaussian or theta self-Fourier invariance identifies the transported forward source, not its adjoint overlap with the relative sheet response.

Therefore source-port reciprocity supplies forward covariance but not the adjoint boundary law required by canonical closure. Promoting it to that law would conflate transport with adjunction and assume the work orthogonality under a chosen metric.

## Disposition

Mellin spectral normalization and the exact Hermitian balance are source-derived. Critical-line confinement is not. Further work should test only concrete new constructors for the combined scalar-to-boundary-work arrow; formal current rearrangements are exhausted within the audited local, memory, reciprocal, moment, valuation, and product-formula classes.
