# Approved common-path closure extension

Author: `marici.Grothendieck`
Status: explicit conditional extension; not source-derived

## Objective

Extend the doubled transfer model so that scalar-null boundary data can imply
full-packet null transport. The operator approved pursuing this extension in
stimulus event `ev-000000010602-6b32a83f-c15e-4bd1-a66a-9c72205bf4ba`.

## Existing residual

The source equations are

\[
u'=-zu-cf,\qquad v'=zv-cf.
\]

Writing the common and relative channels as `w=u+v` and `r=u-v` gives

\[
w'=-z r-2cf,\qquad r'=-z w.
\]

The primitive-current identity leaves the residual

\[
-2zhc\,w.
\]

Terminal scalar nullity supplies at most `w(0)=0`; it does not imply
`w(q)=0` along the path.

## Added extension

Add the source constraint

\[
\mathsf C(z,u,v,f):=z(u-v)+2cf=0
\]

on the admissible solution family. This is equivalent to `w'=0` by the
existing equation for `w`. With the boundary condition `w(0)=0`, it implies

\[
w(q)=0
\]

throughout the interval. The residual then vanishes identically, and the
primitive current closes provided its endpoint values agree. The degenerate
case is also controlled conditionally: if \(c=0\), then \(C=zr=0\). If
\(r\neq0\), this gives \(z=0\) directly. If \(r=0\), then \(w=0\) implies
\(u=v=0\), so the positive-bulk hypothesis fails. Thus positive bulk excludes
the only \(c=0\) branch that would leave \(z\) unconstrained. More generally, once \(w=0\),
\[
u=\frac r2,\qquad v=-\frac r2,
\]
so \(u^2+v^2=r^2/2\). On an interval of positive length, positive bulk
therefore implies \(r\neq0\) in the constant-\(r\) sector. The constraint then
fixes \(z=-2cf/r\) wherever \(r\neq0\), while the Green identity is still
needed to prove that this fixed value is zero.

## Compatibility test

Under `w=0`, the relative equation gives `r'=0`. Preservation of the added
constraint requires

\[
0=(z r+2cf)'=z' r+z r'+2c'f+2cf'.
\]

The existing model declares `c'=0`; therefore compatibility further requires

\[
z' r+2cf'=0.
\]

This is an additional differential condition, not a consequence of scalar
nullity. It is required as a prolongation if the extension is to be preserved.
For example, at a point with constant `z=1`, `c=1`, `r=-2f`, and `f'=1`, the
constraint `C=0` holds but its derivative is `2`, so the base flow immediately
leaves the constrained locus. If `z` and `f` are constant, it reduces to `0=0`;
for variable spectral or source data it is a genuine integrability condition.
Differentiating the prolongation again, with `c'=0`, `r'=-zw`, and the imposed
`w=0`, yields `z''r+2cf''=0`. Generic source data therefore generate a
prolongation hierarchy rather than a finite closed extension. More explicitly,
under the imposed relations \(w=0\), \(r'=0\), and \(c'=0\), the \(n\)-th
prolongation is
\[
\mathsf C^{(n)}=\sum_{k=0}^{n}\binom{n}{k}z^{(k)}r
       +2c f^{(n)}=0,
\]
where the first sum is understood as
\(r\sum_{k=0}^{n}\binom{n}{k}z^{(k)}\) because all positive derivatives of
\(r\) vanish. Thus the hierarchy is an explicit infinite jet constraint on
\((z,f)\), not a hidden consequence of the two base flow equations. When \(c\neq0\),
there is nevertheless a simple parametrization of the constrained sector:
choose constant \(r\) and arbitrary smooth \(z\), set
\[
w=0,\qquad f=-\frac{zr}{2c},\qquad u=\frac r2,\qquad v=-\frac r2.
\]
Then the base flow and every prolongation hold identically: \(u'=v'=0\),
\(C^{(n)}=0\), and \(r'=0\). Equivalently, on this parametrized sector
the entire hierarchy is the jet of the single identity \(f=-zr/(2c)\), so no
additional finite-order equations are needed. For \(c=0\), the constraint instead requires
\(zr=0\), so a nonzero relative channel forces \(z=0\) directly. This gives
a complete conditional closure of the hierarchy, while remaining an imposed
sector selection rather than a source-derived consequence. On this sector the
bulk term is
\[
\int_{q_0}^{q_1}(u^2+v^2)\,dq
=\frac{r^2}{2}(q_1-q_0)>0
\]
whenever \(r\neq0\) and \(q_1>q_0\). Any endpoint-flux functional whose
vanishing condition is the stipulated \(w=0\) boundary condition therefore
vanishes here, but endpoint-current equality still has to be imposed
separately; it does not follow from positivity.

## Conditional closure

If the source supplies the constraint `C=0`, its compatibility condition,
vanishing endpoint flux, equal endpoint current, and

\[
\int (u^2+v^2)>0,
\]

then the Green identity reduces to

\[
2z\int (u^2+v^2)=0,
\]

so `z=0`.

## Endpoint boundary extension

Add the explicit boundary condition

\[
J_{\rm cl}(q_1)=J_{\rm cl}(q_0),
\qquad
J_{\rm cl}=u^2-v^2+J_{\rm p}.
\]

Together with `w=0`, finite positive bulk, and vanishing endpoint flux, the
Green identity then gives `z=0`. This is a sufficient conditional extension,
not a consequence of scalar nullity or of the base flow. Its source status
must remain open until a Fourier--Tate sewing law derives it.

## Conditional finite-cutoff adjoint completion

For a finite cutoff space \(\mathcal H_X\) with an explicitly declared Hilbert
pairing, let the forward forcing incidence be

\[
B_{+,X}:\mathcal U_X\longrightarrow\mathcal H_X,
\qquad B_{+,X}a=aF_X.
\]

The corresponding formal-adjoint candidate is

\[
B_{-,X}:=B_{+,X}^{*}:\mathcal H_X\longrightarrow\mathcal U_X,
\qquad B_{-,X}G=\langle F_X,G\rangle_X.
\]

Hence the typed residual \(R_X^{\rm adj}=B_{-,X}-B_{+,X}^{*}\) vanishes
identically by definition. This is a conditional model completion, not a
source-derived result: Fourier--Tate sewing has not supplied the pairing,
shown preservation of the primitive, square, seam, and archimedean grades, or
authorized the formal adjoint as dynamical incidence.

This construction therefore closes only the local variance defect under the
added finite-cutoff metric. It does not derive the path constraint
\(z(u-v)+2cf=0\) or the endpoint equality \(J_{\rm cl}(q_1)=J_{\rm cl}(q_0)\);
those remain imposed conditions.

## Confinement implication test

The formal adjoint identity constrains the incidence blocks, not the scalar
channels \(w,r,z,c,f\). Therefore it does not imply \(C=z r+2cf=0\). A direct
counterexample at one path point is \(z=c=f=1\), \(r=0\), and \(w=0\): the
formal adjoint block relation may hold, while \(C=2\ne0\) and
\(w'=-2\ne0\). Thus scalar-null data leave the constrained locus immediately.

The adjoint completion is compatible with confinement only after \(C=0\), its
prolongation conditions, and the endpoint-current equality are added
separately. It cannot derive those conditions.

## Endpoint implication test

Even on the anti-diagonal \(w=0\), the endpoint equality is independent. Indeed,
\(v=-u\) makes \(u^2-v^2=0\), so the condition reduces to
\(J_{\rm p}(q_1)=J_{\rm p}(q_0)\). Neither the formal adjoint identity nor the
base flow specifies this primitive endpoint value. Choosing admissible endpoint
primitive data with unequal values gives a nonzero endpoint jump while the
adjoint residual remains zero. Therefore adjoint completion cannot supply the
endpoint sewing condition either.

## Control-port sewing test

The finite Fourier identity \(F_N\Omega=N e_0\) changes the distinguished line
rather than preserving it. Exterior naturality consequently transports the
incidence to \(e_0\wedge\mathcal H_{\rm dual}\). This identifies a possible
control-port location for the missing source constructor, but it supplies no
map expanding \(e_0\) back to the completed output boundary.

Therefore the control-port identity does not imply either \(C=0\) or
\(J_{\rm cl}(q_1)=J_{\rm cl}(q_0)\). A Poisson comb reconstruction and its
current-preservation law would be required. Neither is present in the source
artifact, so the source-derived confinement claim remains unproved.

## Explicit comb-reconstruction extension

At finite \(N\), add the control-to-boundary map

\[
\mathcal R_N(e_0)=N^{-1}\Omega.
\]

This is the inverse-Fourier image of the control point, since
\(F_N^{-1}e_0=N^{-1}\Omega\). It restores the augmentation direction as an
explicit model operation. However, it still does not preserve the scalar
current: no map from \(e_0\wedge\mathcal H_{\rm dual}\) to
\(J_{\rm cl}(q_1)-J_{\rm cl}(q_0)\) has been defined. The reconstruction therefore
extends the incidence typing but leaves the confinement and endpoint residuals
unchanged.

## Conditional current-preserving coherence cell

Add a boundary readout \(\kappa_X\) on the reconstructed control port and
require

\[
\kappa_X\!\left(\mathcal R_N e_0\right)(q_1)
=\kappa_X\!\left(\mathcal R_N e_0\right)(q_0),
\qquad
\kappa_X\!\left(\mathcal R_N e_0\right)=J_{\rm cl}.
\]

This cell supplies exactly the missing endpoint equality. Combined with
\(C=0\), its prolongations, vanishing endpoint flux, and positive bulk, the
existing Green identity yields \(z=0\). The test therefore succeeds as a
conditional construction.

It does not establish source derivation: \(\kappa_X\), its equality, and its
compatibility with the Fourier–Tate grades are newly imposed data. The exact
remaining source residual is the failure to construct \(\kappa_X\) and prove
its current-preservation law from sewing.

## Minimal source-promotion datum

Promotion requires a source-provided finite-cutoff tuple
\[
(\mathcal H_X,\langle-,-\rangle_X,B_{-,X},\mathcal R_N,\kappa_X)
\]
with: \(B_{-,X}=B_{+,X}^{*}\) as a typed map; grade-preserving Poisson
reconstruction \(\mathcal R_N(e_0)=N^{-1}\Omega\); a defined current readout
\(\kappa_X=J_{\rm cl}\); and a proved sewing identity
\[
\kappa_X(\mathcal R_N e_0)(q_1)=\kappa_X(\mathcal R_N e_0)(q_0).
\]
The source must also derive \(C=0\) and its prolongations. The positive self-Fourier Poisson artifact supplies a decisive falsifier: a
strictly positive Fourier-fixed Schwartz carrier. A conditional vacuum-selection
clause can be written independently as \(A_t f=0\), where
\(A_t=\partial_x+2\pi t x\); its solution space is the Gaussian vacuum line,
so the positive Hermite deformation \(f_\delta\) is rejected before Mellin
aggregation. This clause narrows the carrier class, but it still does not
identify the path current, derive \(C\), or provide endpoint sewing.

A strictly positive Fourier-fixed Schwartz carrier with exact primal--dual Poisson
sewing can still have off-critical Mellin zeros. Therefore positivity,
Fourier self-duality, and Poisson sewing do not imply scalar-null confinement;
a separate vacuum-selection or arithmetic boundary-current law is necessary.
The local Euler-factor artifact supplies a second partial ingredient: the Euler factor is a boundary transfer function of an exact input--state--output system, while the internal valuation differential has determinant one. This supports a boundary-readout interpretation but supplies neither the positive path bulk \(\int(u^2+v^2)\,dq\) nor its identification with the transfer matrix. The affine self-sewing artifact adds a partial normalization result: Fourier self-sewing selects unit spacing and zero origin, matching the unshifted unit completion boundary. It fixes lattice scale and origin, but does not identify the path coordinate \(q\) with the spectral parameter \(s\), nor provide the current readout or constraint defect map. The primitive-current
artifact supplies a partial source ingredient: finite cutoff transitions obey a
triangle law and their logarithmic derivatives define a coherent line
connection. Its holonomy is an integrated transport quantity; endpoint
current equality is a pointwise boundary statement. Even trivial holonomy would
not imply the latter without an additional readout or differential identity.
It does not identify the spectral derivative variable \(s\) with the path
coordinate \(q\), nor provide a source map \(\sigma:q\mapsto s\) and readout
transport relating \(\partial_s\log g^{(1)}\) to \(J_{\rm cl}(q)\). Without
that typed parameter map, the primitive connection one-form cannot be inserted
into the endpoint equality. Conditionally, if a source map \(\sigma:q\mapsto s\)
and readout transport are supplied, the pulled-back connection coefficient is
\[
J_{\rm pull}(q)=\sigma'(q)\,\partial_s\log g^{(1)}_{S,T}(\sigma(q)).
\]
The endpoint condition would still be the separate equation
\(J_{\rm pull}(q_1)=J_{\rm pull}(q_0)\); it does not follow from the chain rule
or from trivial integrated holonomy. For a finite transition set \(T\setminus S\), the primitive connection coefficient is
\[
J_{S,T}(s)=\sum_{p\in T\setminus S}(\log p)p^{-s}.
\]
After choosing \(s=\sigma(q)\), endpoint sewing would require
\[
\sum_{p\in T\setminus S}(\log p)\bigl[p^{-\sigma(q_1)}-p^{-\sigma(q_0)}\bigr]=0,
\]
which is not implied by the cutoff triangle law. In the degenerate conditional case
\(\sigma'(q)=0\), the pullback current vanishes identically and endpoint
sewing is automatic, but this is a zero-readout construction, not evidence
that the primitive line connection has been identified with \(J_{\rm cl}\).
The confinement theorem requires equality of the endpoint readout, not a
nonzero current; the defect is missing identification and positive-bulk
coupling, rather than vanishing itself. It does not identify that line connection with the path current
\(J_{\rm cl}\), prove equality of endpoint values across the Fourier--Tate
seam, or derive the constraint jet. Without every component, the result remains a conditional extension. The current artifacts
supply only the algebraic candidate maps, not this source-provided tuple. To make the current determined by the conditional
transport, one would additionally require a readout \(K_X\) with
\(\kappa_X=K_X\circ S_X\) on the reconstructed control image and a theorem
that \(K_XS_X\) has equal endpoint values. The existing readout countermodel
shows that this factorization cannot be inferred from reconstruction alone. The
parameter map is independently substantive: \(\sigma_1(q)=q\) gives
\(J_1=\partial_s\log g^{(1)}(q)\), while \(\sigma_2(q)=2q\) gives
\(J_2=2\partial_s\log g^{(1)}(2q)\). Without a source normalization selecting
\(\sigma\), these are different current readouts from the same line data.

## Composite source theorem target

The partial constructors promote the result only through one joint theorem,
not by independent existence. Let \(\mathcal G_t\) be the source-function domain of \(A_t\), set
\(\mathcal V_t=\ker(A_t:\mathcal G_t\to\mathcal G_t)\), and require a typed
source-to-boundary map \(\iota_X:\mathcal V_t\to\mathcal H_X\). Also put
\[
A_X=T_{\rm FT}-S_X,
\qquad S_X=P_X\circ F_N,
\qquad \widetilde A_X(\Omega,\lambda)=A_X\Omega+\lambda a_X.
\]
A source-selected vacuum \(g_X\in\mathcal V_t\) and reconstructed state
\(\Omega_X=\iota_X(g_X)\) must satisfy
\[
\widetilde A_X(\Omega_X,1)=0,
\qquad \mathcal R_N(e_0)=N^{-1}\Omega_X,
\qquad \widetilde D_X=\widetilde Q_X\widetilde A_X,
\qquad \mathcal B_X=K_XS_X:\mathcal H_X\to C(I,\mathcal O_X),
\]
together with a current functional \(j_X:\mathcal O_X\to\mathbb R\) and
\[
B_{-,X}=B_{+,X}^{*},\quad w(0)=0,\quad \text{endpoint flux}=0,
\]
\[
j_X(\mathcal B_X\Omega_X(q_1))=j_X(\mathcal B_X\Omega_X(q_0)),
\qquad
L_X\Omega_X=(u,v),\qquad
\lVert L_X\Omega_X\rVert^2=\int(u^2+v^2)\,dq>0,
\]
where \((u,v)\) obey the declared base flow. The drift-reversal source artifact
derives
\[
\psi_+'=-z\psi_+-F,\qquad
\psi_-'=\overline z\,\psi_--F.
\]
It matches the declared base flow only under the typed identifications
\(u=\psi_+\), \(v=\psi_-\), \(\overline z=z\), and \(F=cf\), together with
the separate constancy law \(c'=0\). Thus the homogeneous drift and shared
forward forcing have source provenance, but the real-slice identification,
forcing factorization, and constancy of \(c\) remain explicit descent data.
Here the faithful observer must retain
\[
\mathcal O_X=O_{k=1}\oplus O_{k=2}\oplus O_{\ge3}
\oplus O_{\rm seam}\oplus O_{\infty}^{\rm mom},
\]
including both logarithmic sign components and the complete archimedean moment
rigging. The current functional is not generally linear: the native Green
flux \(J=|\psi_+|^2-|\psi_-|^2\) is quadratic, and the primitive correction
\(J_H=2\sqrt2\operatorname{Re}(H\bar d)\) is bilinear in seam and state data.
Thus the earlier linear ansatz \(\kappa_X=K_XS_X\) can represent a current only
after a separately typed quadratic-state lift or nonlinear readout; a linear
map on \(\mathcal H_X\) is type-incompatible with the source Green current.
The known arithmetic and archimedean channels cannot cancel the mixed bulk
residual universally. Primitive and square currents are logarithmic
connections on cutoff lines depending on \(s\) and prime labels; without an
additional state-incidence map, their derivatives contain no independent
\(H\bar m\) or \(H\bar d\) coefficient. The Fourier--dilation anomaly is
exactly endpoint-supported and has zero interior bulk. Hence these channels
cannot supply a current \(J_{\rm add}\) with
\(J_{\rm add}'=-R_{\rm mix}\) for every centered-tail solution. The only
uneliminated named candidate is a Clark-type state shear, which must be tested
as a bilinear source-state incidence rather than as a scalar cumulant. The
minimal constant-coefficient ansatz already fails. Put
\[
J_C=2\sqrt2\operatorname{Re}\!\left[H(a\bar m+b\bar d)\right].
\]
Matching the \(H\bar m\) and \(H\bar d\) coefficients in
\(J_C'=-R_{\rm mix}\) requires
\[
i\tau a-\delta b=\delta,\qquad
-\delta a+i\tau b=-i\tau.
\]
For \((\delta,\tau)\ne(0,0)\), the unique solution is \(a=0\), \(b=-1\),
so \(J_C=-J_H\). Its derivative cancels \(R_{\rm mix}\) only by also
reintroducing the original forcing polarization
\(-2\sqrt2\operatorname{Re}(F\bar d)\). Therefore no independent
constant-coefficient bilinear shear linear in \(H\) closes the identity. A
surviving Clark candidate must use additional source variables or a
nonconstant coefficient law and must show that its new derivative terms do
not recreate the forcing residual. For variable complex coefficients
\(a(q),b(q)\), exact differentiation shows that closure for every local
solution is equivalent, where \(H\ne0\), to
\[
a'+(F/H+i\tau)a-\delta b=\delta,
\qquad
b'-\delta a+(F/H+i\tau)b=-i\tau,
\]
together with \(\operatorname{Re}(HFa)=0\), which removes the source-only
term generated by differentiating \(\bar m\). These equations are a
conditional integrating-factor construction, not a consequence of the Clark
label. They are singular at the canonical seam basepoint \(H(0)=0\). If
\(F(0)\ne0\), regularity of the undivided coefficient equations forces
\(a(0)=b(0)=0\), adding boundary data not supplied by Fourier--Tate sewing.
For real coefficients the source-only condition gives \(a=0\); when
\(\delta\ne0\), coefficient matching then forces \(b=-1\), and the second
equation requires \(F/H=0\), impossible on a generic forced interval. Thus a
regular real variable shear is ruled out. A complex shear remains only as the
displayed singular conditional ODE and needs independent source selection and
endpoint regularity.
The first line couples vacuum selection to the Fourier--Poisson equalizer,
retains the typed control reconstruction, and forces the full constraint jet
to vanish. A naive sampling embedding does not establish nonvacuity. For
\(N=2\), sampling the unit Gaussian at labels \(0,1\) gives
\(v=(1,e^{-\pi})\), hence
\[
F_2v=(1+e^{-\pi},\,1-e^{-\pi}),
\]
which is not the control vector \(2e_0\). Conversely, the augmentation vector
\((1,1)\) is not the sampled Gaussian vacuum. Thus the exact finite
augmentation-to-control rotation and the source Gaussian vacuum do not share a
state under naive restriction. Exact periodization supplies the correct
cross-space replacement. Define
\[
(\iota_N^{\rm d}f)_j=\sum_{k\in\mathbb Z}f(j+kN),
\qquad
(\iota_N^{\rm *}\widehat f)_m
 =\sum_{\ell\in\mathbb Z}\widehat f\!\left(\ell+\frac mN\right).
\]
Poisson summation gives the exact intertwining identity
\[
F_N\iota_N^{\rm d}f=\iota_N^{\rm *}\widehat f.
\]
For the unit self-Fourier Gaussian, this yields a nonzero cross-equalizer
state \(F_N\iota_N^{\rm d}g=\iota_N^{\rm *}g\). It does not identify the
direct and dual boundary spaces or recover the augmentation vector; the
comparison map \(S_X\) must extend
\(S_X\iota_N^{\rm d}f=\iota_N^{\rm *}f\) on the source image. Thus completed periodization establishes algebraic nonvacuity of the
homogeneous cross-equalizer. It does not establish nonvacuity of the shifted
affine equalizer required by a nonzero forcing jet; path energy and current
readout also remain open. The remaining lines supply adjoint closure, scalar-null boundary
data, zero endpoint flux, current sewing, and a positive path bulk. Uniform completion, filtration,
and convergence conditions remain part of the theorem. The independent
source-to-observer audit supplies a methodological gate, not a transferable
map: its successful descent first freezes a source kernel and only then derives
the physical adapter and detector. Applied here, the additive Tate artifact supplies the operator that should be
frozen: on parity-tagged logarithmic sheets,
\[
\mathbb A_{\rm FT}=K_+\oplus K_-,
\]
where the exact Hankel kernels depend on \(r+q\). This operator acts on
\(L^2(dq)\), so its sheet norm is a source candidate for the positive bulk if
the path pair \((u,v)\) is derived as its two sheet components. It does not
supply a local Green boundary current: the Hankel operator is nonlocal, and no
boundary form yielding \(J_{\rm cl}\) is derived in the artifact. The exact
Mellin-translation covariance supplies part of the compatibility cell. If \(V_a h(q)=e^{a/2}h(q+a)\) and
\(G=\partial_q+\tfrac12\), then \(KV_a=V_{-a}K\) differentiates to
\[
KG=-GK.
\]
Thus additive Tate Fourier reverses the homogeneous Mellin drift exactly. The inhomogeneous extension is a source-port square. With forward incidences
\(B_+:\mathcal U_X\to\mathcal H_+\) and
\(B_-:\mathcal U_X\to\mathcal H_-\), it requires
\[
K B_+=B_-R_{\mathcal U},
\]
where \(R_{\mathcal U}\) is reciprocal transport on the source port. The
centered-tail artifact establishes the role-level content of this square: the
same real forcing enters both equations with forward incidence. It does not
establish the completed bounded-map identity on every boundary grade. Even if
that forward covariance is completed, it does not imply
\(B_-=B_+^*\); transport of a forward arrow and construction of its adjoint
are different operations. Neither remaining local source operator selects the
formal adjoint as dynamics. The ordered port
\[
(Sg)(q)=\int \operatorname{sgn}(v-q)g(v)\,dv
\]
is reciprocal-odd and acts \(\mathcal H_X\to\mathcal H_X\); it does not have
the codomain \(\mathcal U_X\) of \(B_+^*\). Pairing it with the source gives a
functional such as \(g\mapsto\langle F,Sg\rangle\), not
\(g\mapsto\langle F,g\rangle\), and its Hardy boundary remains universal
rather than labelled arithmetic incidence. The primitive seam \(H'=F\)
rewrites the forcing pairing by integration by parts, but introduces endpoint
and mixed-bulk terms; it likewise does not promote the metric functional to a
lower dynamic arrow. Thus the order port and primitive seam falsify as source
selectors for \(B_+^*\), although both remain relevant boundary-current
ingredients. Moreover, the Hankel endpoint action generates the full global
moment tower, not one scalar boundary line. Consequently \(K_X\) cannot be a
faithful finite-jet readout; it must factor through the full moment rigging and
the separately labelled arithmetic ports. Importing the
cosmological audit's detector maps would cross source identity and is
inadmissible. Each displayed map has
a separate countermodel when omitted, so this package cannot be shortened by
treating transport, positivity, or holonomy as automatic evidence.

## Hypothetical grade-equalizer route

The Fourier--Tate artifact supplies a concrete obstruction: ordinary sewing
reverses the boundary grade, so it cannot itself provide a common-grade current
cell. The weakest candidate additional structure is therefore a comparison
map \(S_X\) from the complementary-grade presentation to a common completed
object. Define the equalizer sector
\[
\mathcal E_X=\{\Omega:\ T_{\rm FT}\Omega=S_X\Omega\}.
\]
A current readout \(\kappa_X\) that factors through \(\mathcal E_X\), together
with endpoint equality on \(\mathcal E_X\), would supply the missing coherence
without pretending that ordinary Fourier--Tate transport preserves grade.
The adjacent Fourier--Poisson artifact supplies a typed candidate origin for
\(S_X\): Fourier transports \(\Omega\) to \(N e_0\), and Poisson comb
reconstruction expands the control port back into the completed output
boundary. Thus one may define \(S_X\) conditionally as this composite
transport--reconstruction map. This resolves the support/type mismatch but not
the scalar constraint: the artifact does not define a current readout, prove
endpoint sewing, or show that the resulting equalizer lies in \(\ker D_X\).
The construction is therefore a better-typed candidate, not source promotion.
The flat-connection artifact suggests a conditional relative model: for two
transports \(U_1,U_2\) on the completed boundary, define
\[
H_{\rm rel}=U_2^{-1}U_1,\qquad A_{\rm rel}=d\log H_{\rm rel}.
\]
A confinement candidate would require the scalar defect to factor through the
relative anomaly, \(D_X=Q_X(H_{\rm rel}-I)\), while the endpoint current is a
separate readout of \(A_{\rm rel}\). This preserves the distinction between
flat local transport and nonzero relative boundary data. For example, on
\([0,1]\), let \(H_{\rm rel}(q)=e^{q(1-q)}\). Its endpoint values are both one,
while \(d\log H_{\rm rel}=(1-2q)dq\) has endpoint coefficients \(1\) and
\(-1\). Endpoint-trivial relative transport therefore does not imply endpoint
current equality. Neither \(U_2\) nor
the factorization is supplied by the source artifact.
Writing \(P_X\) for the conditional Poisson comb reconstruction, the candidate
is \(S_X:=P_X\circ F_N\) on the augmentation/control component, with its
codomain understood as the common completion. This notation records the
transport path only; it does not assert that \(S_X\) is grade-preserving or
that it annihilates the constraint defect. The exact missing implication can be typed by a defect map
\[
D_X:\mathcal H_X\longrightarrow \mathcal J(C),
\qquad D_X(\Omega)=(C(\Omega),C'(\Omega),C''(\Omega),\ldots),
\]
where \(\mathcal J(C)\) is the constraint-jet space. This displayed map is
not linear on the stated variables: already
\(C=z(u-v)+2cf\) is affine in the path state when \(z,c,f\) are fixed, and is
bilinear when they vary. The ordinary kernel--factorization criterion therefore
does not apply to \(D_X\) as written. For fixed source coefficients, homogenize
on \(\widetilde{\mathcal H}_X=\mathcal H_X\oplus\mathbb C\) by
\[
\widetilde D_X(\Omega,\lambda)
 =D_X^{\rm lin}(\Omega)+\lambda j_X^{\rm src},
\]
where \(j_X^{\rm src}\) contains \(2cf\) and its prolongations. Extending the
comparison defect trivially as \((A_X\Omega,0)\) cannot work unless
\(j_X^{\rm src}=0\), since it kills \((0,1)\) while \(\widetilde D_X(0,1)
=j_X^{\rm src}\). A viable source factorization therefore needs an affine
comparison anomaly \(a_X\):
\[
\widetilde A_X(\Omega,\lambda)=A_X\Omega+\lambda a_X,
\qquad
\widetilde D_X=\widetilde Q_X\widetilde A_X.
\]
In particular, \(\widetilde Q_Xa_X=j_X^{\rm src}\). Only after this
homogenization does the finite-dimensional criterion
\(\ker\widetilde A_X\subseteq\ker\widetilde D_X\) become equivalent to linear
factorization. Thus Fourier--Poisson equality alone cannot force the
inhomogeneous constraint jet; the source must provide a comparison-anomaly
component carrying the forcing jet. This also changes the vacuum condition.
If the completed periodized Gaussian remains a homogeneous equalizer,
\(A_X\Omega_X=0\), then the shifted condition
\(\widetilde A_X(\Omega_X,1)=0\) forces \(a_X=0\), hence
\(j_X^{\rm src}=\widetilde Q_Xa_X=0\). This contradicts a generic nonzero
forcing jet beginning with \(2cf\). Therefore augmentation-to-control rotation
and exact Gaussian Poisson equality cannot themselves construct the affine
anomaly. A viable theorem must replace the homogeneous equalizer by the shifted
comparison law
\[
A_X\Omega_X=-a_X,
\]
or restrict to the degenerate zero-forcing sector. The shifted law requires a
new source incidence and sacrifices the existing Gaussian as an exact
homogeneous equalizer unless that incidence vanishes on it. The vacuum line
makes the solvability condition exact. Choose a nonzero Gaussian generator
\(g\), put \(\Omega_g=\iota_X(g)\), and set \(d_g=A_X\Omega_g\). Every
source-selected vacuum state is \(\alpha\Omega_g\), so
\[
A_X(\alpha\Omega_g)=-a_X
\]
has a solution precisely when \(a_X\in\operatorname{span}(d_g)\); positive
energy additionally requires \(\alpha\ne0\). For exact periodized Poisson
sewing, \(d_g=0\), hence only \(a_X=0\) is solvable. A generic forcing jet
therefore cannot coexist with both the one-dimensional Gaussian selection and
exact homogeneous sewing. Source promotion must either enlarge the selected
source space, replace exact sewing by a shifted comparison incidence, or prove
that the forcing jet vanishes. These are distinct changes, not consequences of periodization. For one fixed
anomaly, the weakest enlargement is not a second vacuum line but the affine
torsor
\[
\Omega_g+A_X^{-1}(-a_X).
\]
It is nonempty exactly when \(a_X\in\operatorname{im}A_X\). If selection is
required to remain linear and to contain both the exact Gaussian and one
shifted solution, its dimension is at least two; one extra direction \(h\)
with \(A_Xh=-a_X\) is algebraically sufficient. For a family of anomalies,
the required additional dimension is at least the rank of their span modulo
the homogeneous kernel. Neither positive energy nor Poisson reconstruction is
inherited automatically: one must separately prove
\(L_X(\Omega_g+h)\ne0\) and reconstruct the shifted state rather than the
original Gaussian. Thus an affine source selector is strictly weaker than an
unspecified enlarged vacuum module, but it remains new source data. The
reconstruction correction is also forced. If
\(\Omega_h=\Omega_g+h\) with \(A_Xh=-a_X\), unchanged inverse Fourier
reconstruction from the same control point \(e_0\) would require
\(F_Nh=0\), hence \(h=0\). For a nonzero shift the control datum must become
\[
e_h=e_0+N^{-1}F_Nh,
\qquad
F_N^{-1}e_h=N^{-1}(\Omega_g+h).
\]
Therefore the affine anomaly moves both the selected boundary state and the
distinguished control point. Positive energy is equivalent to
\(L_X(\Omega_g+h)\ne0\); it is lost only on the affine cancellation locus
\(L_Xh=-L_X\Omega_g\), but avoiding that locus requires a source theorem, not Fourier invertibility. A joint promotion must derive the pair \((h,e_h)\)
and its energy compatibility. Current sewing acquires another independent
correction. For linear \(\mathcal B_X\), define the observer cocycle
\[
\Delta_hj_X(q)=j_X\!\left(\mathcal B_X\Omega_g(q)+\mathcal B_Xh(q)\right)
-j_X\!\left(\mathcal B_X\Omega_g(q)\right).
\]
Endpoint sewing for \(\Omega_g+h\) follows from sewing for \(\Omega_g\) only
if \(\Delta_hj_X(q_1)=\Delta_hj_X(q_0)\). When \(j_X(x)=\beta_X(x,x)\) is
quadratic, this condition controls the endpoint jump of
\[
2\operatorname{Re}\beta_X(\mathcal B_X\Omega_g,\mathcal B_Xh)
+\beta_X(\mathcal B_Xh,\mathcal B_Xh).
\]
Neither the shifted control identity nor positive energy implies this cocycle
law. It is the weakest additional current compatibility for the affine shift.
For a quadratic observer, the entire shifted construction reduces to the
nonemptiness of the typed intersection
\[
\left\{h:A_Xh=-a_X\right\}
\cap
\left\{h:\left[2\operatorname{Re}\beta_X(\mathcal B_X\Omega_g,
\mathcal B_Xh)+\beta_X(\mathcal B_Xh,\mathcal B_Xh)\right]_{q_0}^{q_1}=0\right\}
\setminus
\left\{h:L_Xh=-L_X\Omega_g\right\}.
\]
The first locus is affine-linear, the second is a quadratic endpoint locus,
and the removed locus is energy cancellation. The Hankel moment tower computes
\(\mathcal B_Xh\) but does not make the quadratic endpoint equation automatic;
the arithmetic line connections likewise provide no state-quadratic pairing.
Thus current source artifacts do not establish that this intersection is
nonempty. It is nevertheless algebraically nonempty at finite cutoff. On
\(\mathbb R^2\), take \(\Omega_g=(1,1)\), \(A(x,y)=x-y\), \(a_X=1\),
endpoint observations \(B_0(x,y)=x\), \(B_1(x,y)=y\), and \(j(s)=s^2\).
The shift \(h=(-3/2,-1/2)\) satisfies \(Ah=-1\); the shifted state
\((-1/2,1/2)\) has equal endpoint currents and energy \(1/2\). The shift
\((0,1)\) satisfies the same affine equation but leaves current jump \(3\),
so sewing is independent rather than automatic. The exact-rational checker
`checkers/affine_shift_observer_witness.py` records both cases in
`results/affine-shift-observer-witness.json`. This proves finite algebraic consistency only; source transversality and
completion remain open. The finite transversality test has a one-variable
normal form. Choose one solution \(h_0\) of \(A_Xh=-a_X\) and
\(k\in\ker A_X\). Along \(h(t)=h_0+tk\), the quadratic endpoint jump is
\[
q(h(t))=\alpha t^2+\beta t+\gamma.
\]
A real sewn shift exists on this line exactly when either
\(\alpha\ne0\) and \(\beta^2-4\alpha\gamma\ge0\), or \(\alpha=0\) and the
resulting linear/constant equation is solvable. It is admissible only if at
one such root
\[
L_X(\Omega_g+h_0+tk)\ne0.
\]
This discriminant criterion is the cheapest finite source-transversality
certificate. Completion requires cutoff-dependent choices \(k_X,t_X\) with a
specified limit, uniform operator control, and a positive lower bound on the resulting energy;
levelwise nonnegative discriminants alone do not supply any of these. Three
one-dimensional families separate the requirements. First,
\(q_N(t)=(t-N)^2\) has a sewn root at every cutoff but every root diverges.
Second, \(q_N(t)=t^2\) may have the fixed root \(t_N=0\) while a compatible
sheet map assigns energy \(E_N=N^{-2}>0\), so positivity disappears in the
limit. Third, the already exhibited factorization \(A_N=1\), \(D_N=N\) has
\(Q_N=N\), so convergent states do not control the defect maps. Consequently a
completed affine witness needs all of
\[
\sup_N\|h_N\|<\infty,
\quad h_N\to h,
\quad \sup_N\|\widetilde Q_N\|<\infty,
\quad \inf_N\|L_N(\Omega_{g,N}+h_N)\|^2>0,
\]
plus convergence of observer cocycles and filtration compatibility. None can
be removed using levelwise solvability. At the completed Hilbert level, the
first obstruction is Fredholm-theoretic. For bounded
\(A:\widehat{\mathcal H}\to\widehat{\mathcal K}\), an exact affine shift
exists precisely when \(a\in\operatorname{ran}A\). If the range is closed,
this is equivalent to
\[
\langle a,y\rangle=0\qquad\text{for every }y\in\ker A^*.
\]
Without closed range, that orthogonality gives only
\(a\in\overline{\operatorname{ran}A}\), hence approximate rather than exact
constraint closure. Uniform finite-cutoff shifts require a lower singular-value
bound for \(A_N\) on the anomaly-supporting complement of \(\ker A_N\), or an
equivalent uniformly bounded right inverse. The homogeneous Gaussian in
\(\ker A\) supplies no information about \(\ker A^*\), closed range, or this
lower bound. The cokernel test becomes explicit when the two transports are
unitary. Write \(S=TU\), so
\[
A=T-S=T(I-U).
\]
Then
\[
\ker A=\ker(I-U),
\qquad
\ker A^*=T\ker(I-U^*).
\]
If \(U\) is unitary, its fixed spaces for \(U\) and \(U^*\) agree. Hence a
necessary closed-range solvability condition is
\[
\langle a,Tg\rangle=0
\]
for every Fourier--Poisson fixed vector \(g\). In particular, a forcing anomaly
with a nonzero component along the transported Gaussian fixed line cannot be
removed by any affine shift. Orthogonality is sufficient only when the range
of \(I-U\) is closed, equivalently when the relevant spectrum has a gap away
from \(1\) on the fixed-line complement. The current artifacts establish the
fixed Gaussian but compute neither its pairing with \(a\) nor this spectral
gap. The forcing jet does not generally determine that pairing. The equation
\(\widetilde Q a=j^{\rm src}\) determines \(a\) only modulo
\(\ker\widetilde Q\). Hence \(\langle a,Tg\rangle\) is determined by the jet
exactly when
\[
Tg\in(\ker\widetilde Q)^\perp
 =\overline{\operatorname{ran}\widetilde Q^*}.
\]
With closed adjoint range, this means there is a co-probe \(\eta_g\) such that
\[
\widetilde Q^*\eta_g=Tg,
\qquad
\langle a,Tg\rangle=\langle j^{\rm src},\eta_g\rangle.
\]
If no such co-probe exists, two anomalies with the same forcing jet can have
different cokernel pairings and opposite solvability dispositions. Therefore
the weakest source audit must construct \(\eta_g\) and test the forcing jet against it; the jet
factorization alone is insufficient. At finite cutoff this is an exact row-space
test: solve
\[
\widetilde Q_X^*\eta_{g,X}=T_Xg_X
\]
and retain the true residual. For example, if
\(\widetilde Q(x,y)=x\), then \(\widetilde Q^*\eta=(\eta,0)\).
The probe \(Tg=(1,0)\) has \(\eta_g=1\), and the jet fixes its anomaly
pairing. The probe \(Tg=(0,1)\) has no co-probe; anomalies \((j,y)\) share
the same jet \(j\) while their Gaussian pairing varies with \(y\). Thus rank
of \(\widetilde Q\) alone is insufficient; the transported Gaussian must lie
in its specific row space. Completion further requires bounded convergent
co-probes \(\eta_{g,X}\), since exact finite solutions may diverge when the
relevant singular value tends to zero. The finite comparison factor can always
be engineered at rank at most two under one scalar compatibility, showing why
existence alone has no source force. Given nonzero anomaly \(a\), target jet
\(j\), and transported Gaussian \(g_T\), require a co-probe \(\eta\) with
\[
\langle j,\eta\rangle=\langle a,g_T\rangle.
\]
Start with \(Q_0x=j\langle a,x\rangle/\|a\|^2\). Then
\(Q_0a=j\). Put \(r=g_T-Q_0^*\eta\); the scalar compatibility gives
\(r\perp a\). For \(\eta\ne0\), define
\[
Rx=\eta\,\frac{\langle r,x\rangle}{\|\eta\|^2},
\qquad Q=Q_0+R.
\]
Then \(Qa=j\) and \(Q^*\eta=g_T\), with \(\operatorname{rank}Q\le2\).
If \(j\ne0\), a compatible \(\eta\) can always be chosen; if \(j=0\), the
necessary condition is \(\langle a,g_T\rangle=0\). Because this construction
uses \(a\), \(j\), and \(g_T\) to fit \(Q\), it is only a realizability
witness. Source promotion must derive \(Q\) independently before these target
relations are tested. A frozen factor can be tested on a family without fitting.
For anomaly--jet pairs \((a_i,j_i)\), a single linear \(Q\) with
\(Qa_i=j_i\) exists on their span exactly when
\[
\sum_i c_i a_i=0\quad\Longrightarrow\quad\sum_i c_i j_i=0.
\]
Equivalently, the relation kernel of the anomaly matrix is contained in that
of the jet matrix. Requiring the same co-probe adds
\[
\langle j_i,\eta_g\rangle=\langle a_i,g_T\rangle
\qquad\text{for every }i.
\]
These two conditions are sufficient: the first defines \(Q\) on the anomaly
span, and the second makes its adjoint agree with \(g_T\) there; extension to
the orthogonal complement is separate noncanonical data. Thus the smallest
non-fitted audit uses at least a relation-bearing family of anomalies, not one
pair. Completion additionally requires stable anomaly-span conditioning and uniform bounds for the induced maps. The
present source data do not yet supply a relation-bearing family in one typed
domain. Scaling one forcing profile gives only
\((a_\lambda,j_\lambda)=\lambda(a_1,j_1)\), a rank-one family that cannot
distinguish a frozen factor from a fitted one. The prolongations are components
of one target jet, not independent domain anomalies. Primitive, square, and
tail variations live in different grades and cannot be combined as vectors in
one anomaly space without a new comparison map. The smallest informative
source family would contain two independently admissible forcing profiles and
their sum, with
\[
a(F_1+F_2)=a(F_1)+a(F_2),
\qquad
j(F_1+F_2)=j(F_1)+j(F_2).
\]
A frozen \(Q\) must carry this parallelogram and the common co-probe pairings.
The theta construction currently freezes one forcing profile, so this family
is a new source-variation requirement rather than an available test packet.
Vacuum rigidity explains the absence: for fixed \(t\),
\(\ker A_t=\operatorname{span}(g_t)\), so no two independent profiles survive
selection. Moreover,
\[
A_t(\partial_tg_t)=-(\partial_tA_t)g_t=-2\pi xg_t\ne0,
\]
so infinitesimal scale variation leaves the vacuum line. Prime dilation does
supply a cross-fiber alternative:
\[
D_pg_t=g_{p^2t},
\qquad
A_{p^2t}D_p=pD_pA_t.
\]
Therefore a non-fitted factor need not be tested by addition in one fiber if a
source theorem instead constructs anomaly and jet transports \(W_p,V_p\) with
\[
a_{p^2t}=W_pa_t,
\quad j_{p^2t}=V_pj_t,
\quad Q_{p^2t}W_p=V_pQ_t.
\]
This equivariant family respects vacuum selection, but the existing flat
Gaussian--dilation connection constructs neither \(a_t\), \(j_t\), nor the
naturality square for \(Q_t\). It supplies the correct indexing orbit, not the missing comparison factor.
The prime orbit imposes a coherence test stronger than separate naturality
squares. Writing the scale dependence explicitly, one needs
\[
W_{q,p^2t}W_{p,t}=W_{pq,t}=W_{p,q^2t}W_{q,t}
\]
and the analogous identity for \(V\). The factor squares must satisfy
\[
Q_{p^2t}W_{p,t}=V_{p,t}Q_t.
\]
Then transport through \(p\) and \(q\) gives the same factor at
\(p^2q^2t\). A nonzero difference between the two routes is not harmless
curvature: unless it is retained as a separately typed boundary 2-cell, it
makes the anomaly factor path-dependent and invalidates the source map. The
known identity \(D_pD_q=D_qD_p=D_{pq}\) verifies this coherence only for the
Gaussian carriers; it does not construct coherent \(W,V,Q\) on the anomaly and jet objects. The cutoff
anomaly line does not fill this gap. Its transition category is the poset of
finite prime-set inclusions \(S\subset T\), whereas prime dilation acts on
integer labels by \(n\mapsto pn\) and on Gaussian scale by \(t\mapsto p^2t\).
Multiplication by \(p\) does not send a prime set to a prime set: it sends a
prime \(q\) to the composite label \(pq\). Hence there is no canonical functor
from the prime-dilation orbit to the cutoff-poset line system, and the triangle
law for \(g^{(1)}_{S,T}\) cannot serve as the required \(W_p\) coherence. A
mixed comparison would have to act on labelled valuation towers, where
multiplication by \(p\) increments the \(p\)-valuation while cutoff inclusion
adds a prime locus. The bilateral valuation artifact supplies the minimal domain for that mixed
action. For each finite prime set \(S\), put
\(M_S^{\rm gp}=\bigoplus_{q\in S}\mathbb Z\). Cutoff enlargement gives
inclusions \(i_{S,T}\), while multiplication by \(p\in S\) is translation
\(\tau_{p,S}(r)=r+e_p\). They obey
\[
i_{S,T}\tau_{p,S}=\tau_{p,T}i_{S,T}.
\]
If \(p\notin S\), translation is typed only after the support extension
\(S\subset S\cup\{p\}\); it cannot be confused with that extension. Fourier
reversal \(R(r)=-r\) preserves support and satisfies
\[
R\tau_{p,S}R=\tau_{p,S}^{-1}.
\]
Thus the mixed indexing category exists on finite-support subgroups of the
bilateral valuation group and retains the two polarized cones. It repairs the
prior categorical mismatch, but still supplies no functor from these labelled
translations to \(a_S\), \(j_S\), or \(Q_S\). The observer lift can now be stated without conflating these operations. Let
\(\mathcal A_S\) and \(\mathcal J_S\) be anomaly and jet objects over
\(M_S^{\rm gp}\), with cutoff maps \(W^{\mathcal A}_{S,T}\),
\(W^{\mathcal J}_{S,T}\), valuation translations \(U^{\mathcal A}_{p,S}\),
\(U^{\mathcal J}_{p,S}\), and Fourier maps between opposite towers. A
comparison factor is a natural transformation only if the finite residuals
\[
\begin{aligned}
R^{\rm cut}_{S,T}&=Q_TW^{\mathcal A}_{S,T}
 -W^{\mathcal J}_{S,T}Q_S,\\
R^{\rm val}_{p,S}&=Q_SU^{\mathcal A}_{p,S}
 -U^{\mathcal J}_{p,S}Q_S,\\
R^{\rm FT}_{S}&=Q_{S,-}F^{\mathcal A}_{S,+-}
 -F^{\mathcal J}_{S,+-}Q_{S,+}
\end{aligned}
\]
all vanish, with the cutoff and valuation maps satisfying the mixed-category
relations above. The anomaly section must also be natural and obey
\(Q_Sa_S=j_S^{\rm src}\). These residuals are the smallest joint finite test;
checking any one family alone leaves fitted factors possible. Existing
artifacts separately construct carrier Fourier reversal, cutoff-line
transitions, and some jet grades, but not this common observer functor. A
finite exact-rational witness shows that the joint residual system is
consistent. On two valuation sheets take Fourier swap
\(F=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\),
\(U_+=\operatorname{diag}(2,1/2)\), \(U_-=\operatorname{diag}(1/2,2)\),
and \(Q=I\). Then \(FU_+=U_-F\), all three factor residuals vanish, and
\(Qa=j\) for \(a=j=(1,0)\). The deliberate alternative
\(Q_{\rm bad}=\operatorname{diag}(1,2)\) still preserves cutoff, valuation,
and the chosen anomaly--jet pair but has nonzero Fourier residual. The checker
`checkers/mixed_valuation_observer_witness.py` records these results in
`results/mixed-valuation-observer-witness.json`. This proves independence and finite consistency, not source derivation. The
actual cyclic source sharpens the missing lift. Fourier preserves cyclic word
length while exchanging the positive and negative valuation towers, so a
source comparison must be graded:
\[
Q_\pm=\prod_{k\ge1}Q_{k,\pm},
\qquad
Q_{k,-}F^{\mathcal A}_{k,+-}
 =F^{\mathcal J}_{k,+-}Q_{k,+}.
\]
The primitive and square packets provide only the grades \(k=1,2\), whereas
the Hankel endpoint observer requires the full moment tower. Consequently no
finite truncation of the known cyclic packets can be the faithful comparison
factor used by the confinement theorem. Promotion requires a completed graded
observer, uniform bounds on \(Q_{k,\pm}\), compatibility with cutoff maps at
every grade, and convergence of the induced nonlinear current. The raw full-moment lift
cannot satisfy the needed Hilbert boundedness. Its grade-\(k\) coordinate has
the form
\[
m_k(f)=\int_0^\infty y^k f(y)\,dy.
\]
For normalized translates supported near \(R\), \(|m_k(f_R)|\) grows like
\(R^k\), so \(m_k\) is unbounded on the ambient unweighted \(L^2\) carrier.
Consequently the full map is not bounded into \(\ell^2\), \(\ell^\infty\), or
any unweighted Hilbert product. On a Schwartz source every coordinate is
continuous and the map into the product Fréchet topology exists, but that
supplies neither a Hilbert adjoint co-probe nor convergence of the quadratic
current. A completed graded observer therefore requires source-derived moment
weights or a stronger rigged Hilbert domain; choosing weights merely to force convergence would be an inserted regulator.
A Gaussian rigging shows the exact conditional repair and its ambiguity. On
\[
H_\alpha=L^2\bigl((0,\infty),e^{\alpha y^2}dy\bigr)
\]
Cauchy--Schwarz gives
\[
\|m_k\|_{H_\alpha^*}^2
=\int_0^\infty y^{2k}e^{-\alpha y^2}dy
=\frac{\Gamma(k+\tfrac12)}{2\alpha^{k+1/2}}.
\]
Thus weights \(w_k\) satisfying
\(\sum_k w_k\Gamma(k+\tfrac12)\alpha^{-k}<\infty\) produce a bounded moment
map into \(\ell^2(w)\). The selected Gaussian \(g_t\) belongs to \(H_\alpha\)
for \(0<\alpha<2\pi t\), but source selection does not choose one \(\alpha\)
or one admissible weight sequence. Moreover Fourier does not preserve these
weighted real-line spaces as the same object; a Fock/Hermite transport would
be another declared comparison. Hence moment rigging is analytically
available but neither canonical nor yet Fourier-compatible. At the
Fourier-self-dual scale, the annihilator canonically determines the Hermite
basis and Fourier acts diagonally by fourth roots of unity. This does not
repair the raw moment observer: Hermite coefficients are Bargmann derivatives,
whereas \(m_k(f)\) is the derivative at zero of the ordinary Fourier transform
and is not bounded on \(L^2\). Oscillator Sobolev spaces of any fixed order
control only finitely many such derivatives; controlling every moment requires
the Schwartz intersection or an analytic scale with an extra radius parameter.
Thus the Fock/Hermite construction canonically supplies Fourier grading, but
not a single source-selected Hilbert norm on which the complete raw-moment
observer and its adjoint are bounded. Passing to the canonical nuclear rigging
does not recover the co-probe. The full moment map is continuous as
\[
M:\mathcal S(\mathbb R_+)\longrightarrow\omega=\mathbb C^{\mathbb N}
\]
with the product topology, because each coordinate is continuous. But
\(\omega'=c_{00}\): every continuous co-probe has finite support. Hence
\(M'\eta\) is integration against a polynomial
\(\sum_{k=0}^N\eta_ky^k\), and cannot equal the transported Gaussian \(Tg\).
A sequence topology whose dual admits an infinite Gaussian co-probe must be
strictly stronger than the product topology and must encode convergence
weights. Those weights are exactly the unsourced datum found in the Hilbert
audit. Thus the Gelfand triple relocates rather than removes the obstruction. There
is also a sharp diagonal-weight no-go at the self-dual Gaussian. For a target
\(\ell^2(w)\), boundedness of the moment map and membership of a Gaussian
co-probe \(e^{-\beta y^2}=\sum_n(-\beta)^ny^{2n}/n!\) require
\[
\sum_k w_k\|m_k\|^2<\infty,
\qquad
\sum_n\frac{\beta^{2n}}{(n!)^2w_{2n}}<\infty.
\]
Positive weights satisfying both exist exactly when
\(\sum_n \beta^n\|m_{2n}\|/n!<\infty\). Stirling asymptotics reduce this to
\(2\beta<\alpha\). But the same Gaussian belongs to
\(H_\alpha=L^2(e^{\alpha y^2}dy)\) only when \(\alpha<2\beta\). Therefore no
diagonal weighted sequence Hilbert target simultaneously contains the
self-dual Gaussian source, bounds all raw moments, and admits that Gaussian as
the adjoint co-probe. Any repair must change the coordinates or use different source and co-probe
Gaussian scales. Hermite coordinates provide a precise abstract escape: the
coefficient map \(H:L^2(\mathbb R)\to\ell^2\) is unitary, Fourier diagonal,
and sends the Gaussian to its vacuum coordinate. Therefore, if the defect
space of \(A_X\) were source-identified with this Fourier carrier, choosing
\(Q=H\) would give a bounded injective factor and a Gaussian co-probe without
moments. This does not yet apply to the declared forcing jet. Its coordinates
are derivatives of the flow constraint, while Hermite coefficients are taken
in the additive source variable; no source map identifies these domains.
Moreover the endpoint moment current is not continuous in the bare Hermite
\(\ell^2\) norm. The coordinate change can solve the comparison-factor problem
only after a typed defect-to-Fourier-carrier map is constructed; it cannot
replace the separate rigged nonlinear observer. The existing arrows point the
wrong way for that construction. The source provides
\(L_X:\mathcal H_X\to L^2(I;\mathbb R^2)\), while the affine constraint
produces a scalar defect in \(L^2(I)\). A Hermite lift would require a section
\[
J_X:L^2(I)\longrightarrow\mathcal H_X
\]
whose sheet image realizes a prescribed embedding of the scalar defect. Vacuum-
line injectivity of \(L_X\) does not construct such a section on arbitrary
defects. Choosing \(J_X\) selects a complement to \(\ker L_X\) and is
therefore equivalent to the missing reconstruction/right-inverse datum. The
Hermite coordinate repair is not an independent route around shifted
reconstruction; it factors through the same unsourced arrow. The Hilbert
structures do remove the arbitrary-complement choice once the correct
composite defect operator \(B_X:\mathcal H_X\to L^2(I)\) is source-defined.
If
\[
B_XB_X^*\ge\gamma I\qquad(\gamma>0),
\]
then the canonical minimum-norm section is
\[
J_X=B_X^*(B_XB_X^*)^{-1},
\qquad \|J_X\|\le\gamma^{-1/2},
\]
and the affine correction is \(h_X=-J_Xa_X\). Conversely a bounded
Moore--Penrose right inverse requires closed range, and surjectivity onto the
defect target gives such a positive lower bound. Thus pseudoinversion provides
a source-canonical section conditional on the same spectral gap already
isolated by the Fredholm audit; it does not derive that gap. Cutoff completion
requires a uniform \(\inf_X\gamma_X>0\) plus convergence of \(B_X\) and \(a_X\). Weighted moment completion cannot
supply this gap. Whenever weights make the full moment map
\(M:H_\alpha\to\ell^2(w)\) bounded by the sufficient summability condition
above, one has
\[
\|M\|_{\rm HS}^2=\sum_k w_k\|m_k\|_{H_\alpha^*}^2<\infty.
\]
Thus \(M\) is compact. Any bounded factor \(B=MA\) is compact as well, and a
compact map cannot be surjective onto an infinite-dimensional Hilbert target
or satisfy \(BB^*\ge\gamma I\): otherwise the identity on the target would be
compact. Hence every Hilbert--Schmidt moment regularization is structurally
incompatible with the Moore--Penrose spectral gap. Finite truncations may have
right inverses, but no completed uniform gap follows; a viable factor must
retain a noncompact faithful component, as the Hermite unitary does
abstractly. The minimal repair is a split interface, not a direct-sum demand
on one factor. Let \(Q_{\rm f}\) be a bounded comparison map that is bounded
below on the relevant defect subspace,
\[
\|Q_{\rm f}y\|\ge\kappa\|y\|,
\]
and let \(Q_{\rm c}\) be the separately rigged moment/current observer.
Affine closure and the co-probe use only \(Q_{\rm f}\); endpoint sewing uses
only \(Q_{\rm c}\) on regular solved states. Compactness of \(Q_{\rm c}\) then
has no bearing on the Moore--Penrose gap. In the weakest typed formulation one
may take \(Q_{\rm f}=I\) on the defect space, eliminating the engineered
forcing-jet factor entirely; the remaining requirement is that the transported
Gaussian co-probe actually inhabit that same typed defect space. This split
removes a false joint obstruction but leaves the defect/co-probe typing and the
rigged nonlinear current as independent source obligations. For the actual
Fourier comparison defect this typing condition is satisfied before passage to
the sheet constraint. Both \(T_{\rm FT}\) and \(S_X\) act on
\(\mathcal H_X\), so
\[
A_X=T_{\rm FT}-S_X:\mathcal H_X\to\mathcal H_X.
\]
The selected Gaussian \(g\) and its transport \(T_{\rm FT}g\) therefore lie in
the same defect Hilbert space. Taking \(Q_{\rm f}=I_{\mathcal H_X}\) gives the
co-probe \(\eta_g=T_{\rm FT}g\) without any moment or Hermite lift, and the
solvability obstruction is directly
\[
\langle a_X,T_{\rm FT}g\rangle=0.
\]
This is the minimal comparison theorem. It does not identify the later scalar
flow constraint with \(\mathcal H_X\); that constraint and its nonlinear endpoint observer remain downstream under
\(L_X\). The remaining pairing cannot be evaluated until the affine anomaly is
constructed in this carrier. A source-derived inhomogeneous comparison would
have to provide two forcing lifts
\(B_T,B_S:\mathcal U\to\mathcal H_X\) and
\[
a_X=(B_T-B_S)f.
\]
Then
\[
\langle a_X,T_{\rm FT}g\rangle
=\langle f,(B_T^*-B_S^*)T_{\rm FT}g\rangle_{\mathcal U}.
\]
The known covariance transports a forward forcing port but does not construct
the adjoint lifts appearing here. Hence the identity factor removes the
comparison-map ambiguity but exposes the exact missing datum: a pair of
same-codomain inhomogeneous source lifts, or equivalently their adjoint
difference on the transported Gaussian. A rank-one lift chosen to realize the pairing would again be fitted rather
than source-derived. Moreover, taking the only available forward covariance
literally, \(KB_+=B_-R_{\mathcal U}\), makes the two candidate lifts equal and
therefore gives \(a_X=0\). Its Gaussian pairing then vanishes trivially, but it
cannot produce the required nonzero shifted selected state. Any nonzero anomaly
must come from an additional typed boundary failure of this covariance, not from the covariant
bulk ports themselves. The canonical cutoff candidate also vanishes in the
Hilbert completion. If \(P_X\to I\) strongly are bounded cutoff projections,
then the boundary covariance defect
\[
a_X=[P_X,K]B_+f
\]
satisfies \(\|a_X\|\to0\), since both \(P_XKB_+f\) and \(KP_XB_+f\) converge
to \(KB_+f\). Its Gaussian pairing therefore tends to zero as well. A finite
cutoff can exhibit a nonzero moving-window anomaly, but it cannot produce a
nonzero completed affine shift for bounded source data. Retaining one requires
an unbounded renormalization, a nonconvergent source family, or a distributional
boundary target; each exits the Hilbert hypotheses needed by the identity co-probe and bounded
Moore--Penrose section. A Gelfand triple does not rescue finite-energy
solvability. Let \(\Phi\subset\mathcal H_X\subset\Phi'\). The bounded
comparison defect \(A_X:\mathcal H_X\to\mathcal H_X\) has range inside
\(\mathcal H_X\); therefore
\[
A_Xh=-a,\quad h\in\mathcal H_X,
\]
has no solution when \(a\in\Phi'\setminus\mathcal H_X\). The distributional
pairing \(\langle a,T_{\rm FT}g\rangle_{\Phi',\Phi}\) may exist, but its
vanishing is only a cokernel condition and cannot put \(a\) into the Hilbert
range. Allowing \(h\in\Phi'\setminus\mathcal H_X\) forfeits the declared sheet
energy and Green positivity. Thus a surviving distributional boundary anomaly
is incompatible with the present finite-energy confinement theorem unless a
new unbounded defect operator and renormalized positive form are independently
constructed. The boundary branch therefore has a sharp trichotomy under the
completion hypotheses. For convergent bounded source data and uniformly
bounded cutoff normalizations, commutator anomalies converge to zero in
\(\mathcal H_X\). A surviving limit outside \(\mathcal H_X\) has no
finite-energy affine correction. A nonzero limit inside \(\mathcal H_X\) can
only be obtained by unbounded renormalization or boundary-concentrating source
data, violating the declared uniform affine-factor or source-convergence
conditions. Hence no nonzero boundary-generated affine shift survives in the
current completed theorem. This does not rule out the unshifted branch
\(a_X=0\), where the selected Gaussian already obeys exact homogeneous sewing;
that branch must be audited directly for positive sheet energy and endpoint
current closure. The energy part succeeds conditionally on the declared sheet
norm: if \(\Omega_g\ne0\) and \(L_X\) is injective on the vacuum line, then
\(L_X\Omega_g\ne0\), so
\[
E_g=\|L_X\Omega_g\|_{L^2(I;\mathbb R^2)}^2>0.
\]
But homogeneous Fourier sewing does not imply that this sheet pair satisfies
the source flow
\(u'=-zu-cf,\ v'=zv-cf\), nor does it identify the two endpoint values of the
native quadratic current. Full-moment Fourier reconstruction and a nonlinear
endpoint cocycle are still required. Thus the unshifted Gaussian resolves
selection and positive energy without an affine anomaly, but it does not
supply the dynamics or current-sewing hypotheses needed by the Green
confinement implication. The declared flow itself gives a sharper necessary
test for any proposed Gaussian sheet identification. Put \(r=u-v\) and
\(s=u+v\). For constant \(z,c\), the flow and \(C=zr+2cf=0\) give
\[
r'=-zs,
\qquad s'=-C=0.
\]
If \(z\ne0\) and \(c\ne0\), then
\(r=-2cf/z\), \(s=2cf'/z^2\), and hence \(f''=0\). If \(c=0\), then
\(r=s=0\), contradicting positive sheet energy. Therefore a positive-energy
constrained off-null sheet state can exist only where the forcing is affine in
the flow coordinate. A non-affine Gaussian or theta forcing rules out such a
state before endpoint sewing. What remains unsourced is the identification of
that forcing coordinate and of \(L_X\Omega_g\) with this flow; without it the
argument is conditional rather than a theorem about the Fourier vacuum. The
present source equations type \(F=cf\) in the flow coordinate but do not equate
\(F\) with the Gaussian or theta profile selected in the additive carrier.
Without that extra arrow, affine forcing remains admissible. An exact off-null
countermodel is
\[
z=c=1,
\quad f(x)=x,
\quad u(x)=1-x,
\quad v(x)=1+x.
\]
It obeys \(u'=-zu-cf\), \(v'=zv-cf\), has
\(C=z(u-v)+2cf=0\), and has positive sheet energy on every nondegenerate bounded
interval. Therefore flow closure plus positivity alone cannot confine \(z\)
unless source nonaffinity is proved in the same coordinate. Identifying only the vacuum state, without identifying its forcing port, is
insufficient. The flow nevertheless has its own exact quadratic current
\[
J_0=u^2-v^2.
\]
Direct differentiation gives
\[
J_0'=-2z(u^2+v^2)-2cf(u-v).
\]
On \(C=z(u-v)+2cf=0\), this reduces to
\[
J_0'=-z(u+v)^2.
\]
Therefore endpoint sewing \(J_0(b)=J_0(a)\) and
\(\int_a^b(u+v)^2dx>0\) imply \(z=0\), without any forcing-nonaffinity
assumption. For the affine countermodel, \(J_0=-4x\), so it fails endpoint
sewing exactly as required. This is a complete flow-level confinement theorem;
source promotion still requires proving that the Fourier--Tate endpoint
observer descends to \(J_0\), rather than merely to a different quadratic moment current. The real doubled
tail source does make this descent: its native polarized flux is exactly
\(J=|\psi_+|^2-|\psi_-|^2\), hence \(J_0=u^2-v^2\) after the real sheet
identification. But Fourier reciprocal sewing exchanges the two sheets, so the
current is odd:
\[
(u,v)\longmapsto(v,u)
\quad\Longrightarrow\quad J_0\longmapsto-J_0.
\]
Thus self-sewing yields \(J_0(b)=-J_0(a)\), not the equal-endpoint condition
\(J_0(b)=J_0(a)\) used by the confinement identity. Both hold only when the
endpoint flux itself vanishes. The observer descent is therefore available,
but Fourier sewing supplies current reversal rather than current closure; a source-derived zero-flux condition remains necessary. Sewing does not itself
provide that selector because the polarized current is naturally a section of
the sign line exchanged by the two boundary presentations. Its law
\(J_0(b)=-J_0(a)\) is consistent with a nonzero section. Zero would follow only
if one additionally required \(J_0\) to descend as an ordinary scalar on the
sewn quotient, since scalar invariance and odd sewing give \(J_0=-J_0\). But
that requirement trivializes the sign line and identifies direct and dual
boundary grades, contrary to the retained Fourier--Tate orientation data.
Hence quotient descent is not a source-compatible zero-flux selector. A
separate isotropic boundary condition \(|u|=|v|\), or an independently derived
vanishing of the sign-line section, is still required. Gaussian self-duality
supplies isotropy only at a fixed seam of the reciprocal involution. If
\(x\mapsto\iota x\) exchanges the sheets, equivariance and \(K\Omega_g=
\Omega_g\) give \(u(x)=v(\iota x)\). At a fixed point \(x_0=\iota x_0\), this
yields \(u(x_0)=v(x_0)\) and \(J_0(x_0)=0\). For a paired boundary
\(b=\iota a\), it gives only cross-relations; endpoint data
\[
(u(a),v(a))=(2,1),
\qquad (u(b),v(b))=(1,2)
\]
obey exact sheet exchange while carrying fluxes \(3\) and \(-3\). Thus one
self-dual seam supplies at most one zero-flux endpoint. A second isotropic boundary, or a source path whose two ends are independently
fixed seams, is not present in the current construction. Tail decay cannot
supply the second endpoint while retaining the positive bulk used by \(J_0\).
On \(C=0\), the flow gives \(s'=(u+v)'=0\). If both sheets decay at the tail,
then \(s\to0\), hence \(s\equiv0\) and
\(\int s^2=0\). If the other endpoint is a self-dual seam, then also
\(r=u-v=0\) there; since \(r'=-zs=0\) and the tail decays, \(r\equiv0\).
The state is therefore zero and cannot have positive sheet energy. Thus
fixed-seam isotropy plus two-sheet tail decay closes the flux only by
collapsing the constrained state, not by proving scalar confinement for a
nonzero state. On a finite interval the role of two isotropic endpoints is
exact. Since \(C=0\) gives constant \(s=u+v\), while
\(r=u-v\) obeys \(r'=-zs\), one has
\[
J_0=rs,
\qquad
J_0(b)-J_0(a)=-z\,s^2(b-a).
\]
If \(s\ne0\), isotropy at both endpoints is equivalent to
\(r(a)=r(b)=0\), which forces \(z=0\). Conversely, \(z=0\) and isotropy at
one endpoint propagate isotropy to the other. Thus a second isotropic boundary
is not a weaker consequence of reciprocal sewing; under positive symmetric
bulk it is exactly the missing confinement boundary datum. Reciprocal exchange only gives \(r(b)=-r(a)\), allowing
\(2r(a)=zs(b-a)\) with \(z\ne0\). Recasting the boundary term with twisted
coefficients does not restore confinement. If \(J_0\) is treated as a section
of the Fourier sign local system, anti-sewing gives a closed twisted endpoint,
but its covariant derivative and hence the bulk \(zs^2\) take values in the
same sign line. A real line with holonomy \(-1\) has no global preserved
positive cone, so this bulk cannot carry the scalar positivity used to infer
\(z=0\). If \(zs^2\) is retained as an ordinary positive scalar instead, then
the Green identity is written in an ordinary trivialization and its boundary
term is \(J_0(b)-J_0(a)\), which anti-sewing does not cancel. Twisted closure and scalar positivity therefore cannot be obtained
simultaneously from the same Fourier sewing datum. Squaring the current does
not help. On \(C=0\), with constant \(s\),
\[
(J_0^2)'=-2zs^2J_0.
\]
Anti-sewing makes \(J_0^2(b)=J_0^2(a)\), but then the integrated identity is
\(zs^2\int_a^bJ_0dx=0\). Since \(J_0\) is affine and has opposite endpoint
values, its integral is zero independently of \(z\). More generally every
even orientation-invariant function of \(J_0\) differentiates to an odd
factor times \(zs^2\), whose reciprocal contributions cancel. Taking an
absolute value has the same cancellation and adds a nondifferentiable zero
set. Orientation-invariant nonlinearization closes the boundary only by removing
the sign-definite bulk. Multiplying by the Fourier-odd spectral coordinate
appears to evade this, since locally
\[
(zJ_0)'=-z^2s^2.
\]
But the endpoint comparison is ill-typed in either interpretation. On a fixed
spectral fiber, \(z\) has one value at both ends, so anti-sewing still gives
\((zJ_0)(b)=-(zJ_0)(a)\). If \(z\) is instead treated as a parallel section of
the same sign line as \(J_0\), then a nonzero global parallel \(z\) is
incompatible with holonomy \(-1\); assuming it exists already forces the
conclusion. Representing the sign change by a seam jump makes \(zJ_0\) scalar
but adds a distributional seam derivative that exactly restores the missing
boundary term. The spectral-sign tensor therefore does not provide a new
source-derived positive closed current. The doubled-cover calculation locates
the cancellation precisely. On the first chart, oriented by \(x\),
\(d(zJ_0)/dx=-z^2s^2\). Fourier sewing sends \((z,J_0)\) to
\((-z,-J_0)\) and reverses the dilation coordinate. Traversing the sewn second
chart with coordinate \(t\) therefore has \(dx/dt=-1\), so
\[
\frac{d}{dt}(zJ_0)=+z^2s^2.
\]
The two positive-looking local densities enter with opposite orientation and
cancel on the doubled contour. If one suppresses the orientation reversal to
make both signs negative, the resulting contour is not the source Fourier
sewing. Equivalently, encoding that suppression by a discontinuous
trivialization introduces the missing seam term. The completed cover thus gives an identity, not confinement. Selecting one
oriented chart retains the local positive density but reopens its boundary.
On that chart,
\[
zJ_0(b)-zJ_0(a)=-z^2\int_a^b s^2dx.
\]
A polarization projector \(\chi_+\) makes the same point distributionally:
\[
d(\chi_+zJ_0)=\chi_+d(zJ_0)+(d\chi_+)zJ_0,
\]
where the cut term is the omitted endpoint flux. The positive valuation cone
provides a canonical arithmetic polarization, but Fourier carries it to the
opposite cone, so it does not close this cut. The cut term vanishes exactly
under the independent zero-flux condition already found. Hence a half-contour
orientation selects the positive bulk but cannot also supply boundary closure;
a physical readout imposing that closure would be new source data. No approved
Fourier--Tate source map supplies such a physical boundary readout or an
orientation authority independent of the arithmetic polarization. The only
available scalar-null boundary candidate is common-mode cancellation
\(s=u+v=0\), which indeed gives \(J_0=rs=0\) at that endpoint. But on
\(C=0\), \(s'=0\), so terminal common-mode nullity propagates as
\(s\equiv0\) and annihilates the positive bulk \(\int s^2\) used by the
flow-current theorem. It cannot simultaneously close the cut and certify the
nonzero positive channel. Thus neither the approved source nor scalar nullity
provides the required zero-flux readout for this confinement route. The
primitive-current channel does retain a different positive bulk on the
common-mode-null branch. With \(s=u+v=0\), one has \(v=-u\), \(J_0=0\),
\(N=2u^2\), and the exact primitive identity becomes
\[
2zN=-J_{\rm p}',
\qquad J_{\rm p}=2hc(u-v).
\]
Combining \(s=0\) with \(C=0\) makes \(u\) constant and
\(f=-zu/c\) constant when \(c\ne0\); hence \(h'=f\) and
\(J_{\rm p}'=-4zu^2\). Equal primitive-current endpoints then force \(z=0\)
for a positive state. But this endpoint equality is equivalent here to zero
total primitive increment, \(f(b-a)=0\), and is not supplied by Fourier
anti-sewing. The primitive route restores a full positive norm, but relocates
the unsourced boundary condition from polarized flux to primitive holonomy.
Fourier--Poisson sewing cannot remove that holonomy by a primitive gauge
choice. For \(h'=f\),
\[
h(b)-h(a)=\int_a^bf(x)\,dx
\]
is invariant under \(h\mapsto h+\text{constant}\). A sewn or periodic primitive
exists only when this mean vanishes. On the common-mode-null constrained
branch, \(f=-zu/c\) is constant, so for a nondegenerate interval and positive
state its primitive holonomy vanishes exactly when \(z=0\). Imposing periodic
primitive sewing therefore restates the desired conclusion rather than
deriving it. The actual source primitive records the relative boundary anomaly; it is not a
zero-holonomy selector. The current-channel audit now has a sharp boundary.
The native polarized current gives a positive \(s^2\) bulk but is anti-sewn;
the primitive current gives the full positive norm on \(s=0\) but closes only
when its holonomy vanishes; even functions of the polarized current close but
have sign-cancelling bulk; twisted and spectral-sign constructions lose either
positivity or source orientation. Therefore any genuinely new source channel
must construct an ordinary scalar current \(K\) with
\[
K(b)=K(a),
\qquad
K'=-q(z)E,
\]
where \(E\ge0\) is source-derived and positive on the selected state, while
\(q(z)>0\) for real \(z\ne0\). Neither endpoint equality nor positivity may be
obtained by trivializing the Fourier sign line or by defining \(K\) as a formal
antiderivative. This interface is sufficient for confinement and excludes all
current repairs tested above. No local scalar sheet current can meet this
interface. On \(C=0\), \(s'=0\) and \(r'=-zs\). A Fourier-invariant scalar
current has the form \(K(r,s)=K(-r,s)\), so
\[
K'=-zs\,\partial_rK.
\]
Because \(\partial_rK\) is odd in \(r\), this derivative reverses sign between
the two reciprocal sheet states. It cannot equal \(-q(z)E(r,s)\) with
\(q(z)>0\) and a nonzero Fourier-invariant \(E\ge0\). This includes every
swap-invariant quadratic: for
\(K=a(u^2+v^2)+2buv\), one gets
\(K'=z(b-a)(u^2-v^2)\), never a positive bulk. The full moment tower can evade
this local no-go only through cross-grade or nonlocal variables with their own
source dynamics; the existing Hankel endpoint reconstruction supplies no such Green
evolution law. Even if the full tower is given the natural dilation evolution,
a general quadratic no-go remains. Let \(F\) be the Fourier sewing involution,
\(G\) the homogeneous generator with \(FG=-GF\), and
\(K(x)=\langle x,Px\rangle\) a bounded scalar quadratic current with
\(FP=PF\). Its bulk operator is
\[
D=G^*P+PG.
\]
Unitary conjugation gives \(F^*DF=-D\). If \(D\) were positive or negative
semidefinite, then \(-D\) would have the same sign, forcing \(D=0\).
Therefore no Fourier-invariant bounded quadratic current on the completed
moment tower can have a nonzero sign-definite homogeneous bulk. An escape must
break Fourier invariance through an independently authorized polarization or use genuinely nonlinear dynamics not supplied by the Hankel reconstruction.
The obstruction extends to every differentiable scalar current, not only
quadratics. Let \(V\) be the source vector field and \(F\) a reversing
involution with \(F_*V=-V\circ F\). For any differentiable
\(F\)-invariant scalar \(K\),
\[
(\mathcal L_VK)(Fx)=-(\mathcal L_VK)(x).
\]
If \(\mathcal L_VK\le0\) on an \(F\)-stable domain, applying the same inequality
at \(Fx\) forces \(\mathcal L_VK=0\). In particular no Fourier-invariant
nonlinear current can have derivative \(-E\) with nonzero \(E\ge0\) while the
exact forcing covariance preserves reversibility. A strictly positive Green
channel therefore requires a source-authorized restriction to one
polarization, a non-invariant current with an independent zero boundary, or a
genuine dissipative/readout operation that breaks Fourier reversal. Among the
approved constructions, only the positive valuation cone
\(M_+\subset M^{\rm gp}\) is a source-authorized symmetry-breaking
polarization. Gaussian vacuum selection is Fourier fixed; parity selection is
not preserved by the anticommuting generator; finite cutoffs restore the bulk
symmetry in completion; direct and dual boundary grades remain distinct; and
no physical readout or dissipative operation is declared. The \(M_+\)
polarization creates precisely the unilateral boundary incidence already seen
as the moving-window anomaly, but supplies no condition annihilating that
incidence on the selected state. Therefore the remaining source-shaped datum
is a boundary functional on the relative inclusion
\(M_+\hookrightarrow M^{\rm gp}\) that vanishes on the selected state while
leaving a nonzero positive bulk. The selected Gaussian does not annihilate the
canonical incidence. At one prime the positive valuation shift \(S\) on
\(\ell^2(\mathbb N)\) has boundary projection
\[
I-SS^*=P_0,
\]
the zero-valuation line where the two cones meet. The Gaussian valuation vector
has nonzero vacuum coefficient: its zero-valuation sample is \(g(1)>0\).
Consequently \(P_0g\ne0\). This one-prime witness already refutes boundary
nullity, and higher cyclic grades retain the corresponding vacuum word.
Subtracting \(P_0g\) would enforce incidence nullity only by replacing the
selected Gaussian with an unsourced projected state. The authorized arithmetic
polarization therefore couples, rather than decouples, the selected vacuum to
its boundary. Vacuum subtraction does not alter this Green obstruction. For a
current or incidence functional \(K\), replacing it by
\(:K:(x)=K(x)-K(g)\) changes neither its derivative nor its endpoint
difference:
\[
:K:(b)-:K:(a)=K(b)-K(a).
\]
Subtracting a transported vacuum \(g(x)\) can change the derivative only by an
additional counterterm. If \(g(x)\) obeys the same source dynamics, the
selected state has zero deviation and the normal-ordered bulk vanishes; if it
does not, the counterterm is an inserted boundary channel. Thus canonical
constant normal ordering leaves the obstruction intact, while path-dependent
normal ordering either destroys positive vacuum bulk or assumes the missing
source current. These audits imply a bounded no-go for the approved extension.
With exact Fourier reversal and forcing covariance, no differentiable
Fourier-invariant scalar current on an invariant completed domain has a
strictly sign-definite derivative. The native non-invariant current is
anti-sewn; the primitive completion requires zero holonomy; the sole approved
polarization has nonzero Gaussian boundary incidence; bounded cutoff anomalies
vanish, while distributional survivors admit no finite-energy correction.
Therefore scalar confinement is not derived by the present constructors. The
weakest surviving theorem remains conditional: either
\[
C=0,
\quad J_0(b)=J_0(a),
\quad \int (u+v)^2>0,
\]
or common-mode nullity with primitive-current endpoint closure and positive
\(N\), implies \(z=0\). Promotion requires one new asymmetric source datum:
a zero boundary/readout, a dissipative operation, or a nonvanishing relative
current with independently proved positive bulk. The weakest admissible
asymmetric extension can be specified without choosing among those mechanisms.
It must provide a source-typed domain \(X_+\) not closed under Fourier reversal,
a differentiable scalar current \(K:X_+\to\mathbb R\), and maps \(E,q\) such
that
\[
\mathcal L_{V_z}K=-q(z)E,
\qquad E\ge0,
\qquad q(z)>0\ \text{for }z\ne0.
\]
For the selected constrained state it must independently prove
\(K(b)=K(a)\) and \(\int E>0\). Every map, the tangency of \(V_z\) to \(X_+\),
and the boundary equality must descend from the source; none may be defined by
integrating \(E\) or by assuming the target scalar nullity. Within the audited
class, at least one of domain invariance, current invariance, or exact
reversibility must fail. These data are jointly sufficient and isolate the minimal promotion interface.
The positive valuation cone satisfies only the tangency part. For the
unilateral shift \(S\) and real spectral weight
\(W_z=p^{-z}S\),
\[
\|x\|^2-\|W_zx\|^2=(1-p^{-2z})\|x\|^2.
\]
This is a positive discrete bulk for \(z>0\), and reciprocal symmetry could
reduce a real audit to that half-line. But no nonzero unilateral state has the
source-derived norm closure \(\|W_zx\|=\|x\|\) except at the desired null
weight; imposing it is circular. Using the backward shift does not help:
\[
\|x\|^2-\|p^{-z}S^*x\|^2
=(1-p^{-2z})\|x\|^2+p^{-2z}|x_0|^2,
\]
so the nonzero boundary incidence survives even at \(z=0\). The cone provides
asymmetric tangent dynamics and a positive contraction, but still lacks an
independent closed boundary state. The unilateral spectrum rules out an
internal repair. The forward shift \(S\) has no nonzero eigenvectors, so
\(p^{-z}Sx=x\) has only the zero solution for every \(z\). The backward shift
\(S^*\) has eigenvectors \(x_n=\lambda^nx_0\) only for \(|\lambda|<1\).
Thus \(p^{-z}S^*x=x\) exists only for real \(z<0\), with
\(\lambda=p^z\). On that eigenstate the norm identity reads
\[
0=(1-p^{-2z})\|x\|^2+p^{-2z}|x_0|^2,
\]
so the boundary incidence exactly cancels the bulk term. For \(z>0\) no
nonzero closed state exists; for \(z<0\) closure exists only through exact
boundary cancellation. Projective renormalization removes the spectral norm factor and therefore
removes the proposed confinement signal. Tensoring primes does not change this
spectrum. On \(\ell^2(\mathbb N^S)\), the commuting forward shifts have no
nonzero joint eigenvector. Joint backward coherent vectors have
\[
x_{(n_p)}=x_0\prod_{p\in S}\lambda_p^{n_p},
\qquad |\lambda_p|<1,
\]
so the source choice \(\lambda_p=p^z\) is possible only for
\(\operatorname{Re}z<0\), and each prime boundary term again cancels its norm
bulk on the fixed vector. In the infinite-prime tensor relative to the vacuum,
existence additionally requires \(\sum_p p^{2\operatorname{Re}z}<\infty\),
which holds only for \(\operatorname{Re}z<-1/2\). Thus collective Euler
completion supplies no closed state near the centered line and no escape from
the one-prime boundary cancellation. Analytic renormalization cannot promote
these coherent vectors to positive states. At finite cutoff, normalized prime
coherent factors carry products of \(1-|p^z|^2\), and their exact transfer
identity is bulk plus boundary incidence equal to zero. Beyond the convergence
half-plane, an Euler or zeta continuation of that product need not be real or
positive and is not the norm of a vector in the completed Hilbert tensor.
Moreover continuation of the exact finite identity preserves the total zero;
separating a continued positive bulk from its continued boundary term is
regulator-dependent. Thus a renormalized Euler amplitude may define a
meromorphic scalar, but it supplies neither a positive state nor an authorized
arrow from that scalar to the Green energy. A GNS reconstruction does not
repair the continued Euler kernel at the centered strip. In the convergence
half-plane,
\[
K_\sigma(t_i,t_j)=\zeta\bigl(\sigma+i(t_i-t_j)\bigr)
=\sum_{n\ge1}n^{-\sigma}e^{-i(t_i-t_j)\log n}
\]
is positive definite for \(\sigma>1\), since it is a Gram kernel with positive
weights. Its analytic continuation to \(0<\sigma<1\) fails the first GNS test:
\(K_\sigma(t,t)=\zeta(\sigma)<0\). Hence the continued Euler scalar cannot be
the diagonal of a positive state near \(\sigma=1/2\). Archimedean completion
may define a different kernel, but that is not a continuation of the Euler
coherent-state norm and requires a separate positivity and source-map proof. Theta completion can
supply such positivity on the centered line without supplying confinement. If
the standard completed representation is written
\[
\Xi(t)=\int_{\mathbb R}e^{itu}\,d\mu_\theta(u)
\]
with the positive theta measure \(d\mu_\theta\), then
\(K(t_i,t_j)=\Xi(t_i-t_j)\) is positive definite and yields a GNS state. But
\(\Xi(t)=\langle\Omega,U_t\Omega\rangle\) is a matrix coefficient, not a norm;
it may vanish by phase cancellation in a positive Hilbert space. The kernel is
also parameterized on the centered line itself, so its positivity supplies no
map sending an off-line scalar zero to zero positive energy. Thus completed
theta GNS positivity is genuine but orthogonal to the required Green
factorization. Neither cyclicity nor rank-one positivity promotes a single
matrix-coefficient zero to zero energy. If
\(c=\|\Omega\|^2=\Xi(0)>0\) and \(\Xi(t)=0\), then the Gram matrix of
\(\Omega,U_t\Omega\) is
\[
\begin{pmatrix}c&0\\0&c\end{pmatrix},
\]
which is strictly positive, not degenerate. The rank-one effect
\(E_\Omega=|\Omega\rangle\langle\Omega|\) has expectation zero in
\(U_t\Omega\), but this means only that the state lies in
\(\ker E_\Omega\); the effect is not faithful. Cyclicity would force a vector
to vanish only if it were orthogonal to every translate of \(\Omega\), whereas
a scalar zero supplies one orthogonality relation. Thus the GNS route still
lacks a jointly faithful positive probe family tied to the same scalar null.
Translation covariance and zero multiplicity do not generate that family. A
zero \(\Xi(t_0)=0\) implies
\[
\langle U_a\Omega,U_{a+t_0}\Omega\rangle=0
\]
for every \(a\), but only for pairs at the fixed separation \(t_0\); cross
terms in arbitrary cyclic linear combinations remain unconstrained. The
functional equation adds only the reflected zero, and a zero of multiplicity
\(m\) adds the finite relations
\(\langle\Omega,A^kU_{t_0}\Omega\rangle=0\) for \(k<m\). No finite family is
jointly faithful on the infinite-dimensional GNS space. Infinite-order
vanishing would make the entire matrix coefficient identically zero,
contradicting \(\Xi(0)>0\). A single scalar zero therefore cannot generate the
faithful probe family required for zero-energy promotion. The required bridge
from scalar nullity to the Green theorem is not an energy map at all. It is a
source divisibility certificate for the vector constraint and scalar boundary
defect. Writing the completed scalar as \(\Xi(s)\), sufficient typed arrows
would have the form
\[
A_s\Omega_s=\Xi(s)R_A(s),
\qquad
K_s(b)-K_s(a)=\Xi(s)R_K(s),
\]
with \(R_A,R_K\) regular at the zeros, together with an independently positive
\(E_s\) and a Green identity. Then \(\Xi(s)=0\) gives constraint and boundary
closure while leaving \(E_s>0\). GNS positivity supplies only the matrix
coefficient \(\Xi(s)\); it supplies neither divisibility relation. Constructing
\(R_A\) or \(R_K\) by dividing after locating zeros is fitted and inadmissible.
Thus the minimal promotion datum is source-derived principal-ideal membership
of both defects, not stronger positivity of the scalar kernel. The theta
functional equation does not provide that ideal membership. For an analytic
defect \(D\), divisibility \(D\in(\Xi)\) requires every zero of \(\Xi\), with
its multiplicity, to be a zero of \(D\). Reflection parity only constrains
\(D(-z)=\pm D(z)\). The finite analytic model
\[
\Xi(z)=z^2-a^2
\]
has the required even reflection symmetry, while the invariant defect
\(D_+(z)=1\) and anti-invariant defect \(D_-(z)=z\) are both nonzero at generic
zeros \(\pm a\). Thus functional equation, conjugation, and Fourier covariance
cannot imply principal-ideal membership. In the actual source, homogeneous
Gaussian comparison is identically zero and hence trivially divisible, but the
downstream flow constraint and endpoint-current defect have no source map to
that homogeneous comparison. The promotion failure is therefore localized to those two downstream defects. Terminal nullity cannot establish
pathwise principal-ideal membership. Let \(s_+(x;\lambda)=u+v\) and suppose
the scalar is \(\Xi(\lambda)=s_+(b;\lambda)\). Since
\(s_+'=-C\),
\[
s_+(x;\lambda)=\Xi(\lambda)+\int_x^bC(y;\lambda)\,dy.
\]
At a scalar zero, pathwise vanishing of \(s_+\) is therefore equivalent to the
vanishing of every partial integral of \(C\), hence to \(C=0\) itself. The
analytic model \(\Xi(\lambda)=\lambda\),
\(s_+(x;\lambda)=\lambda+b-x\), and \(C=1\) has exact terminal nullity at
\(\lambda=0\) while the interior path remains nonzero. Dividing the full path
by \(\Xi\) is regular only after the desired constraint closure is already
known. Endpoint-to-path divisibility is thus circular without a new transport
law. The weakest sufficient propagation certificate is a homogeneous defect
evolution
\[
C'=M(x,\lambda)C,
\qquad
C(b;\lambda)=\Xi(\lambda)c_b(\lambda),
\]
with regular evolution operator. It gives
\(C(x;\lambda)=\Xi(\lambda)U(x,b)c_b(\lambda)\), hence pathwise closure at a
scalar zero. The declared flow does not have this form. Direct calculation
gives
\[
C''-z^2C=2cf'',
\]
so the defect evolution is inhomogeneous unless the forcing jet is included
and itself closes. Moreover terminal scalar nullity specifies
\(s_+(b)=\Xi=0\), not the required terminal defect \(C(b)=0\). Promotion thus
needs both an \(\Xi\)-divisible terminal defect jet and a closed homogeneous
forcing-augmented evolution; neither follows from the current scalar endpoint. The theta forcing cannot be
absorbed into a finite constant-coefficient jet system. In a tail coordinate
it has the form
\[
f(x)=\sum_{n\ge1}a_ne^{-\lambda_nx}
\]
with infinitely many distinct \(\lambda_n\). If a nonzero polynomial
\(P\) satisfied \(P(\partial_x)f=0\), uniqueness of the Laplace expansion would
give \(P(-\lambda_n)=0\) for every \(n\), impossible for finite-degree
\(P\). A single Gaussian may satisfy a first-order variable-coefficient law,
but the theta sum requires an infinite jet or an additional heat variable.
The formal jet evolution \((f,f',f'',\ldots)'=(f',f'',\ldots)\) has an
unbounded shift generator and needs a weighted domain, convergence theorem,
and \(\Xi\)-divisible terminal data at every retained grade. None is supplied by the present endpoint scalar. Adjoining the heat variable does give
a homogeneous infinite-dimensional block system. For
\(\partial_t\Theta=(4\pi)^{-1}\partial_y^2\Theta\) and
\(f(t)=\Theta(0,t)\), one has
\(f''=(4\pi)^{-2}\partial_y^4\Theta(0,t)\), so
\[
\partial_t
\begin{pmatrix}C\\C'\\\Theta\end{pmatrix}
=
\begin{pmatrix}
C'\\ z^2C+2c(4\pi)^{-2}\partial_y^4\Theta|_{y=0}\\
(4\pi)^{-1}\partial_y^2\Theta
\end{pmatrix}.
\]
This closes on a suitable Sobolev domain, but its theta component is nonzero at
a scalar zero and continues to drive \(C\). Homogeneous augmentation propagates
zero only when the entire terminal block is \(\Xi\)-divisible, not when one
common-mode coordinate vanishes. Subtracting the theta-driven particular
solution recreates the unsourced affine shift. The heat PDE repairs jet closure
but not scalar-to-constraint promotion. A Duhamel subtraction is canonical only
after extra boundary data are chosen, and still does not solve promotion. For
\(C''-z^2C=g\), the terminal-zero particular solution is
\[
C_{\rm p}(x)=\int_b^x\frac{\sinh(z(x-y))}{z}g(y)\,dy,
\qquad C_{\rm p}(b)=C_{\rm p}'(b)=0.
\]
Then \(\bar C=C-C_{\rm p}\) is homogeneous, but its terminal data are
\(C(b),C'(b)\), neither determined by \(\Xi=s_+(b)\). Choosing the particular
solution to match those unknown data makes \(\bar C=0\) tautologically and
leaves the nonzero forced \(C_{\rm p}\). At a scalar zero, \(C_{\rm p}\) itself
vanishes only if the forcing driver \(g=2cf''\) has the missing
\(\Xi\)-divisibility. Duhamel normalization therefore moves the obstruction
between source and terminal data without removing it. Spectral-independent
forcing makes the remaining divisibility criterion exact. If \(f''\not\equiv
0\) is independent of the spectral parameter, then
\[
2c(\lambda)f''\in(\Xi)
\quad\Longleftrightarrow\quad
c(\lambda)\in(\Xi)
\]
locally at a scalar zero. Thus regular driver divisibility forces
\(c(\lambda_0)=0\) whenever \(\Xi(\lambda_0)=0\). This would itself yield a
short confinement route: on \(C=0\), if \(c=0\) and \(z\ne0\), then
\(u-v=0\); differentiating gives \(u+v=0\), so the sheet energy vanishes.
Hence positive energy forces \(z=0\). The route needs no endpoint current, but
it depends on the new source identity \(c=\Xi\tilde c\). The current
construction treats \(c\) as an independent constant control and supplies no
such identity. In fact the identity is incompatible with the fixed nonzero
source forcing. The physical port is \(F=c f\). If
\(c=\Xi\tilde c\) with \(\tilde c\) regular, then at a scalar zero either
\(F\) vanishes or \(f=F/c\) develops a pole. The former changes the declared
inhomogeneous source precisely at the zero being tested; the latter violates
the regular forcing and finite-energy flow hypotheses. The rescaling
\((c,f)\mapsto(\alpha c,f/\alpha)\) is a harmless presentation change only for
nowhere-zero \(\alpha\); choosing \(\alpha=\Xi\) is singular and does not
construct a source descent. Thus the control-amplitude shortcut cannot be used
without replacing the approved forcing family. A Dirichlet-to-Neumann map also retains an affine
forcing defect. With terminal common mode \(s_+(b)=\Xi\) and
\(C(b)=-s_+'(b)\), any boundary response obtained from the forced evolution has
the form
\[
C(b;\lambda)=M(\lambda)\Xi(\lambda)+d_F(\lambda),
\]
where \(d_F\) is the zero-Dirichlet response of the fixed forcing. At a scalar
zero, the terminal defect is \(d_F\), not zero. Principal-ideal membership
requires \(d_F\in(\Xi)\), which is the same forcing-divisibility obstruction
found in the Duhamel calculation. In the homogeneous limit, the ratio
\(C(b)/\Xi\) is generically meromorphic and has poles rather than removable
values at Dirichlet zeros unless an independent boundary condition makes the
Cauchy data vanish together. No approved source condition cancels the affine DtN term. Replacing the scalar
by a joint boundary determinant does not promote the original zero set. Let
\[
B(\lambda)=\bigl(\Xi(\lambda),C(b;\lambda),
K(b;\lambda)-K(a;\lambda)\bigr).
\]
A determinant or norm built to vanish exactly when \(B=0\) defines the
intersection of three zero conditions, generally a strict subset of
\(Z(\Xi)\). For such an upgraded scalar \(\widehat\Xi\) to represent the same
divisor as \(\Xi\), one needs
\(\widehat\Xi=u\Xi\) with a nowhere-zero unit \(u\); then the additional
boundary components must already vanish on \(Z(\Xi)\), equivalently satisfy the
missing local divisibility conditions. Otherwise the construction changes the
spectral problem. A joint Evans determinant can encode confinement hypotheses, but cannot derive
them for the approved completed scalar. Principal-ideal membership is
sufficient but stronger than the set-theoretic promotion actually needed. For
a defect component \(D\), scalar nullity implies defect nullity exactly when
\[
Z(\Xi)\subseteq Z(D),
\]
equivalently \(D\in\sqrt{(\Xi)}\) in the local analytic ring. If
\(\Xi=(\lambda-\lambda_0)^m u\) and
\(D=(\lambda-\lambda_0)^n v\), only \(n\ge1\) is required; then
\(D^m\in(\Xi)\) even when \(D\notin(\Xi)\). Thus regular linear quotients are
not minimal. This correction does not rescue the source: parity countermodels,
the affine DtN response, and the spectral-independent forcing are generically
nonzero at scalar zeros and fail even radical membership. The weakest missing
certificate is common zero-set containment for both the path constraint and boundary defect.
At finite polynomial cutoff this condition is exactly testable without root
approximation. Put
\[
P_{\rm sf}=P/\gcd(P,P').
\]
Then \(Z(P)\subseteq Z(D_j)\) for every defect component exactly when
\(P_{\rm sf}\mid D_j\), equivalently
\(\deg\gcd(P_{\rm sf},D_j)=\deg P_{\rm sf}\). Rational defects additionally
require denominators coprime to \(P_{\rm sf}\). The exact-rational checker
`checkers/radical_containment_witness.py` verifies that
\(P=(x^2-1)^2\) and \(D=x^2-1\) pass radical containment while failing
principal divisibility, and that \(D=x-1\) deliberately misses one scalar
root. Results are in `results/radical-containment-witness.json`. The bordered
prime-transfer cutoff supplies a concrete source failure of the rational
version of this test. Its scalar is
\[
g_N(q)=\frac{1-q^{N+1}}{1-q},
\]
while the retained terminal logarithmic current has derivative
\[
D_N(q)=-\frac{2(N+1)q^N}{1-q^{N+1}}.
\]
Every zero of \(g_N\) is a nontrivial \((N+1)\)-st root of unity and hence a
pole of \(D_N\), because
\(1-q^{N+1}=(1-q)g_N(q)\). The denominator is therefore not coprime to the
squarefree scalar; the boundary defect fails even to be regular, much less
zero, on the scalar zero set. This finite source cutoff cannot satisfy radical promotion for its terminal
current. Exponentiation removes the pole but does not produce the required
Green law. The multiplicative terminal factor
\[
T_N(q)=(1-q^{N+1})^2=(1-q)^2g_N(q)^2
\]
is divisible by the scalar and its ordinary derivative also vanishes at scalar
zeros. This containment is tautological: \(T_N\) was reconstructed from the
scalar numerator, not from an independent boundary state. Its logarithmic
derivative is the meromorphic current above, while the polynomial derivative
\[
-T_N'(q)=2(N+1)q^N(1-q^{N+1})
\]
is positive only on the real interval \(0<q<1\). The nontrivial zeros of
\(g_N\) lie on the complex unit circle, so that order supplies no positivity at
the tested spectral points. Moreover \(T_N\to1\) and \(T_N'\to0\) on compact
subsets of \(|q|<1\) as \(N\to\infty\); the proposed bulk disappears under
completion. Exponentiation therefore gives algebraic zero containment but no
source-derived positive Green confinement. A Hermitian radial pairing does
give an exact finite identity but remains non-promoting. For \(m=N+1\), a
candidate endpoint \(q_0\), and radial parameter \(r\in[0,1]\), set
\[
E_{q_0}(r)=|1-(rq_0)^m|^2.
\]
Then
\[
-E_{q_0}'(r)=2m r^{m-1}
\left(\operatorname{Re}(q_0^m)-r^m|q_0|^{2m}\right).
\]
If \(g_N(q_0)=0\), then \(q_0^m=1\), so
\(E_{q_0}(1)=0\) and
\(-E_{q_0}'(r)=2m r^{m-1}(1-r^m)\ge0\). Conversely the endpoint equality
already says \(q_0^m=1\), hence \(|q_0|=1\); the Green identity does not derive
that condition independently. It merely repackages the geometric-sum
numerator. The radial variable is a declared deformation coordinate, not
physical time, and the energy has no supplied transport to the completed
scalar. Thus this is a valid finite-cutoff identity, not a confinement
mechanism for \(\Xi\). The only nondegenerate large-cutoff profile is an
\(N\)-dependent terminal boundary layer. With \(m=N+1\) and
\(r=e^{-x/m}\), the root-conditioned energy becomes
\[
E_N(x)=(1-e^{-x})^2,
\qquad
\frac{dE_N}{dx}=2e^{-x}(1-e^{-x})\ge0,
\]
independently of \(N\). This exact profile does not define a completed spectral
Green object. A sequence of roots
\(q_N=e^{2\pi i k_N/m}\) can converge to any point of the unit circle, while
the rescaled energy forgets \(k_N/m\) entirely. The coordinate
\(x=-m\log(q/q_N)\) is an \(N\)-dependent blowup around a moving terminal
root, not a fixed source coordinate on compact subsets of the completed
spectral domain. Hence the scaling retains a universal local boundary layer
but loses the spectral information needed for confinement. Retaining the full
geometric sum gives a two-scale limit. If
\(q_m=e^{2\pi i k_m/m}\), \(k_m/m\to\theta\in(0,1)\), and
\(r=e^{-x/m}\), then
\[
|g_{m-1}(rq_m)|^2
\longrightarrow
\frac{(1-e^{-x})^2}{|1-e^{2\pi i\theta}|^2}
=
\frac{(1-e^{-x})^2}{4\sin^2(\pi\theta)}.
\]
Its \(x\)-derivative is nonnegative. Thus the finite local transfer has a
phase-labelled radially coercive boundary-layer model away from the seam
\(\theta=0\). The free phase is compatible with radial confinement rather than
a failure of it. However the completed local factor is
\((1-q)^{-1}\), whose interior has no descendants of these truncation zeros;
the zeros become a dense boundary set and the weight is singular at the seam.
No source map sends this moving-root two-scale family to zeros of the global
completed scalar. The construction is therefore a finite-local prototype, not
a completed promotion. Primewise assembly also fails the source-coordinate
pullback. For the Euler ratio \(q_p=p^{-s}\), the unit circle supporting the
finite geometric-sum zeros is \(\operatorname{Re}s=0\), not the critical line.
Introducing \(\widetilde q_p=p^{1/2-s}\) moves the critical line to
\(|\widetilde q_p|=1\), but the source Euler factor is then
\[
(1-p^{-s})^{-1}=(1-p^{-1/2}\widetilde q_p)^{-1}.
\]
Its source truncations still have zeros at
\(|\widetilde q_p|=p^{1/2}\), not one. Truncating
\(\sum_k\widetilde q_p^k\) would insert weights \(p^{k/2}\) and change the
Euler coefficients. Moreover the additive prime logarithm is absolutely
controlled only in \(\operatorname{Re}s>1\); the recorded raw Euler-phase test
does not define a critical-line value. Consequently the nonnegative local
radial profiles neither share the target line nor admit a source-defined sum
there. Primewise positivity cannot be assembled into the required global
confinement form. Fourier duality does not remove the local half-density
weight. Put \(y=p^{1/2-s}\) and \(a=p^{-1/2}\). Pairing the source factor with
its reflected factor gives
\[
(1-ay)^{-1}(1-ay^{-1})^{-1}.
\]
After clearing the Laurent monomial, its denominator vanishes when
\[
y+y^{-1}=a+a^{-1},
\]
namely at \(y=a\) and \(y=a^{-1}\), not on the unit circle. A centered
geometric section \(\sum_{k=-N}^N y^k\) would have unit-circle zeros, but it
replaces the source coefficients \(a^{|k|}\) by one. The source-weighted
infinite centered kernel
\[
1+\sum_{k\ge1}a^k(y^k+y^{-k})
\]
is the Poisson-type kernel determined by the Euler factor and does not supply
those centered geometric zeros. Thus Fourier reflection provides reciprocal
radii but no source-derived self-inversive section whose zeros lie on the
critical unit circle. Reciprocal symmetry alone cannot supply confinement. For
any real \(0<a<1\),
\[
P_a(y)=(y-a)(y-a^{-1})
=y^2-(a+a^{-1})y+1
\]
is self-reciprocal, since \(y^2P_a(1/y)=P_a(y)\), but its roots lie strictly
inside and outside the unit circle. Conjugation adds no restriction because
the coefficients are real. In the \(s\)-coordinate this is exactly the
possibility of a pair reflected across the critical line. Therefore the global
functional equation supplies an orbit of zeros under reflection, not a fixed
locus. Excluding off-line reciprocal pairs requires an independent positive
Hermitian or self-adjoint structure whose null vectors are source-linked to
\(\Xi\); it cannot follow from Fourier reciprocity itself. A Hermite--Biehler route
makes the missing positive structure precise. After a source-fixed change of
spectral coordinate sending the critical line to the real axis, one would need
an entire \(E\) satisfying
\[
|E(z)|>|E^\#(z)|\quad(\operatorname{Im}z>0),
\qquad E^\#(z)=\overline{E(\bar z)},
\]
and a nowhere-zero unit identifying \(\Xi\) with one real boundary component
of \(E\). Equivalently, a source canonical system
\(JY'=zH(x)Y\) with \(H(x)\ge0\), self-adjoint separated boundary data, and
characteristic determinant equal to \(\Xi\) up to a unit would confine its
spectral zeros. The approved extension supplies none of these identifications:
its forced nonlinear trajectory is not a linear canonical eigenproblem, the
control port is inhomogeneous, and its scalar is a terminal readout rather than
a proved characteristic determinant. Defining \(E\) from \(\Xi\) and then
assuming the Hermite--Biehler inequality merely restates the desired real-zero
property. This route is a sufficient interface, not a derived theorem. Linearization
does not repair the positivity defect because the source flow is already
affine-linear:
\[
Y'=z\begin{pmatrix}-1&0\\0&1\end{pmatrix}Y-cf
\begin{pmatrix}1\\1\end{pmatrix}.
\]
For the homogeneous part, writing \(JY'=zHY\) forces, up to the sign convention
for \(J\),
\[
H=J\begin{pmatrix}-1&0\\0&1\end{pmatrix}
=\begin{pmatrix}0&-1\\-1&0\end{pmatrix},
\]
which has eigenvalues \(1\) and \(-1\). It is not a positive canonical
Hamiltonian. This is visible without matrix terminology: on an interval of
length \(L\), impose \(w(0)=w(L)=0\) in the unforced homogeneous system. A
nonzero initial relative mode gives \(w(L)\) proportional to
\(\sinh(zL)\), so the boundary determinant has zeros
\(z=i\pi n/L\), including nonzero off-target values, while the sheet norm is
positive. No equilibrium linearization converts the approved transfer into a
self-adjoint positive spectral problem. A Wick rotation changes rather than
repairs this conclusion. Substituting \(z=i\lambda\) turns
\(\sinh(zL)\) into \(i\sin(\lambda L)\), so the same nonzero zeros become real
in the new coordinate \(\lambda\); in the approved coordinate they remain
\(z=i\pi n/L\), whereas the Green conclusion sought is \(z=0\). A real
pairing-preserving change of sheet variables acts on the canonical Hamiltonian
by congruence and cannot change its \((1,1)\) inertia. A complex sheet rotation
can alter that displayed signature only by abandoning the source real/Hermitian
structure; it also changes the common readout \(u+v\), the forcing incidence
\((1,1)^T\), or the positive sheet expression. Thus neither spectral rotation
nor a fundamental-symmetry choice simultaneously preserves the source flow,
scalar boundary map, and positive bulk. No source-compatible Wick repair
exists in the declared two-sheet model. The indefinite Hamiltonian does become
positive on the relative-sheet polarization, but invariance is exactly the
missing constraint. In common/relative coordinates,
\[
Y^T H Y=-2uv=\frac{r^2-w^2}{2}.
\]
On \(w=0\), this equals the positive sheet expression
\(u^2+v^2=r^2/2\). However the source equation gives
\[
w'=-(zr+2cf)=-\mathsf C.
\]
Therefore the positive subspace \(w=0\) is flow-invariant if and only if the
added path constraint \(\mathsf C=0\) holds throughout. Scalar nullity selects
this subspace at one boundary point only. Restricting the canonical system to
its positive polarization hence does not derive closure; it is precisely the
conditional sector selection already isolated above. A variable positive graph
does not close the residual automatically. On a segment where \(r\neq0\), put
\(w=\kappa r\). The source equations give the exact Riccati law
\[
\kappa'=z(\kappa^2-1)-\frac{2cf}{r}.
\]
The canonical quadratic form is positive when \(|\kappa|<1\), but the
primitive-current residual becomes
\[
-2zhc\,w=-2zhc\,\kappa r,
\]
which has no sign and does not vanish inside that positive cone. Boundary
scalar nullity gives \(\kappa=0\) only where \(r\neq0\) at the endpoint; the
Riccati equation can immediately move it to either sign. A variable positive
polarization therefore weakens canonical positivity but not the Green closure
condition. The only remaining possibility in this direction is an independent
coercive estimate that strictly absorbs the residual into the sheet bulk. Such
an estimate yields a weaker conditional theorem than exact \(w=0\). After
endpoint-current closure, write the Green factor schematically as
\[
2z(B-R)=0,
\qquad
B=\int (u^2+v^2),
\qquad
R=\int hc\,w.
\]
If \(|R|<B\), then \(B-R\neq0\) and hence \(z=0\). For a real/Hermitian
pairing,
\[
|R|\le \|hc\|_2\|w\|_2
\le \sqrt2\,\|hc\|_2 B^{1/2},
\]
so the explicit sufficient gap \(B>2\|hc\|_2^2\) absorbs the residual. Mere
positivity \(B>0\) does not imply this gap. Pointwise,
\[
\frac{w^2+r^2}{2}-hc\,w
=\frac{r^2+(w-hc)^2-(hc)^2}{2},
\]
which can be negative. The source supplies neither a lower normalization of
\(B\) nor a relative form bound below one. Residual absorption is therefore a
strictly weaker conditional interface than common-mode vanishing, but remains
an additional coercivity axiom. Control-amplitude scaling cannot generate this
gap on the forcing-produced sector. With zero homogeneous data, linearity gives
\[
(u_c,v_c)=c(u_1,v_1),
\]
so
\[
B_c=c^2B_1,
\qquad
R_c=c^2R_1.
\]
Both the ratio \(|R_c|/B_c\) and the sufficient inequality
\(B_c>2\|hc\|_2^2\) are independent of nonzero rescaling of \(c\). Setting
\(c\) small or normalizing \(c=1\) therefore changes neither coercivity nor its
failure. If a homogeneous component is present, small \(c\) can suppress the
mixed residual only when that component has a separately supplied positive
norm lower bound; scalar nullity does not provide one. The actual missing datum
is a uniform relative form or observability estimate for the forced response,
not an amplitude choice. At finite cutoff this gate has an exact operator
form. Let \(S_X(z):\mathcal U_X\to\mathcal H_X\oplus\mathcal H_X\) be the
forced response, let
\[
A_X=S_X^*S_X,
\]
and let \(Q_X\) represent the residual form
\(R_X(a)=\langle a,Q_Xa\rangle\). On the quotient by \(\ker A_X\), uniform
absorption is exactly
\[
\rho_X(z):=
\sup_{a\ne0}
\frac{|\langle a,Q_Xa\rangle|}{\langle a,A_Xa\rangle}<1.
\]
Equivalently, \(\rho_X\) is the numerical radius of
\(A_X^{-1/2}Q_XA_X^{-1/2}\); for a Hermitian residual form it is the largest
absolute generalized eigenvalue of \(Q_Xa=\mu A_Xa\). For the one-dimensional
control used here this reduces to the exact scalar ratio \(|R_1|/B_1\).
Confinement would require a source-derived bound
\(\sup_{\Xi(z)=0}\rho_X(z)<1\), stable under cutoff completion, together with
endpoint-current closure. No response matrices, uniform gap, or completion
estimate are presently supplied. This is the mechanically testable form of the
remaining coercivity obligation. The weakest confinement statement isolated by
this programme is disjunctive. At every zero of \(\Xi\), assume positive sheet
bulk and either:

1. **short constrained route:** the control amplitude and the full path
   constraint vanish there, so \(c=0\) and \(zr=0\); if \(z\neq0\), the source
   equations force \(r=w=0\), contradicting positive bulk; or
2. **Green route:** every scalar-zero boundary defect, including endpoint flux
   and closed-current mismatch, vanishes set-theoretically, and the residual
   form satisfies \(|R|<B\) (with exact \(w=0\) as the special case
   \(R=0\)); then the closed identity \(2z(B-R)=0\) forces \(z=0\).

The exact algebraic requirement on each promoted defect is radical membership,
not matching zero multiplicity. Finite cutoffs can test this by squarefree gcds
and test the coercive branch by generalized eigenvalues. The approved source
currently supplies neither route: \(c\) is an independent nonzero control,
the path constraint and endpoint equality are not derived, the affine forcing
obstructs DtN promotion, and no response-operator gap is available. Reciprocity,
local truncation positivity, determinant upgrades, canonical linearization,
and Wick rotation do not replace these certificates. This is the minimal
conditional theorem and the irreducible source deficit established here.
This criterion is only a candidate organizational form until a
source constructs \(Q_X\), but it identifies a concrete theorem target rather
than treating equalizer membership as enough. In an analytic or filtered
setting, promotion additionally requires \(Q_X\) to descend to the completed
image and be continuous or bounded in the chosen topology, with the filtration
compatibility stated explicitly. Algebraic factorization alone proves only a
formal jet-kernel statement. Operationally, if \(\widehat{\mathcal H}_X\) and
\(\widehat{\mathcal J}(C)\) are the source completions, promotion requires a
map \(\widehat Q_X:\operatorname{im}\widehat A_X\to\widehat{\mathcal J}(C)\)
with \(\widehat D_X=\widehat Q_X\widehat A_X\) and a finite bound in the
chosen norms. This is an analytic condition on the completed connection, not
an additional consequence of the finite-cutoff identities. At each fixed
finite cutoff, all spaces are finite-dimensional, so any linear factorization
is automatically bounded. The genuine additional requirement is a bound that
is uniform in the cutoff (or a specified convergent replacement), together
with preservation of the filtration. A finite witness therefore verifies only
levelwise consistency, not existence of the completed connection. For example,
let \(A_N=1\) and \(D_N=N\) on one-dimensional cutoff spaces. Each level has
the valid factorization \(D_N=Q_NA_N\) with \(Q_N=N\), but
\(\sup_N\lVert Q_N\rVert=\infty\). Thus no uniformly bounded completed factor
follows from the finite witnesses alone. Filtration preservation is independent:
take \(\mathcal H=\mathbb C^2\) with \(F_0=\operatorname{span}(e_0)\),
\(F_1=\mathcal H\), let \(A=I\), and let \(D(e_0)=e_1\),
\(D(e_1)=0\). The bounded factorization \(D=Q A\) exists with \(Q=D\),
but it does not preserve \(F_0\). Hence boundedness alone cannot certify a
grade-preserving completed connection. Convergence is independent as well:
with one-dimensional spaces, take \(A_N=1\) and \(D_N=(-1)^N\). Then
\(Q_N=(-1)^N\) has uniform norm one, but the sequence has no limit in the
usual topology. A completed theorem therefore needs an explicit convergence
mode, not only uniform estimates.

The Fourier-dilation anomaly artifact supplies a sharper negative result: on a
finite Mellin window, the generator-reversal defect is exactly the endpoint
current \(b^sf(b)-a^sf(a)\), with no residual bulk integral. Thus archimedean
Fourier reversal cannot source the positive bulk term required by the Green
identity; any such term must come from an additional arithmetic or boundary
construction. The Fourier-saturation artifact supplies another partial result:
saturation creates a Fourier-invariant pro-Gram topology. A conditional path-energy map
must instead be a typed sheet-component map
\[
L_X:\mathcal H_X\longrightarrow L^2(I;\mathbb R^2),
\qquad L_X\Omega=(u,v),
\]
satisfying
\[
\|L_X\Omega\|_{L^2(I;\mathbb R^2)}^2
=\int_I(u^2+v^2)\,dq
\]
on the reconstructed real sector. On the one-dimensional vacuum line, nonzero exact periodization makes
\(\iota_X\) injective, so \(L_X\) can be defined on its image by pulling back
to the Gaussian and applying the logarithmic sheet transform. This gives a
nonzero finite-energy pair, but it does not prove that the pair obeys the
specific base flow \(u'=-zu-cf\), \(v'=zv-cf\). The artifact establishes
positivity of the Gram form, but it does not derive that dynamical
compatibility. Thus Gram positivity
cannot replace source identification of the Green-identity bulk.

The saturation artifact also supplies a Fourier-invariant pro-Gram topology with trivial finite-cutoff kernel,
but it does not merge the primitive and square grades into one Hilbert space.
It also leaves seam and archimedean incidence maps to be derived. Therefore
saturation cannot supply the missing common-grade current cell or the constraint
jet. A cross-sector observability audit independently sharpens this boundary: its
control theorem derives a required rank but not the theta seam row. Thus even
an available positivity or observability theorem would not supply the missing
current cell; the source must derive the specific seam/current row itself. A finite countermodel
makes the logical gap explicit: take \(\mathcal H_X=\mathbb C^2\), let
\(T_{\rm FT}=S_X=I\), so \(\mathcal E_X=\mathbb C^2\), and define
\(D_X(a,b)=(a,0,0,\ldots)\). The equalizer is nontrivial, but its element
\((1,0)\) has nonzero constraint defect. Hence a source comparison map and a
nontrivial equalizer do not suffice; the kernel inclusion
\(\mathcal E_X\subseteq\ker D_X\) is an independent required theorem.
See `research/kitaev/checkers/check_tail_seam_observability.py`, whose
`source_authority_boundary` records this distinction.

## Conditional dependency chain

The proof has four distinct arrows:
\[
C=0\ \Longrightarrow\ w'=0\ \Longrightarrow\ w=0,
\qquad
w=0\ \Longrightarrow\ \text{residual}=0,
\]
then current sewing closes the endpoint term, and positive bulk converts the
Green identity into \(z=0\). The first arrow uses the added constraint, the
second uses the initial condition, and the final conclusion uses positivity;
none of these arrows is supplied by formal adjointness alone.

## Conditional theorem boundary

Assume the base flow, \(C=0\), every compatibility prolongation, vanishing
endpoint flux, positive bulk \(\int(u^2+v^2)>0\), and the current-cell identity
\(J_{\rm cl}(q_1)=J_{\rm cl}(q_0)\). Then \(w'=0\) and \(w(0)=0\) imply
\(w\equiv0\); the Green identity reduces to
\[
2z\int (u^2+v^2)=0,
\]
so \(z=0\). Thus, for every base-flow solution selected by the listed
constraint, sewing, flux, and positivity hypotheses, scalar-null confinement
holds. This is not a universal statement about all base-flow solutions: the
explicit drifting trajectory violates the constraint prolongation. Its
converse and its source derivation are not asserted.

## Source residual

The corrected source-promotion residual is the conjunction of five absent
facts:

1. a nonzero source-selected state satisfying the shifted comparison law
   \(A_X\Omega_X=-a_X\), not merely homogeneous Gaussian sewing;
2. a uniformly controlled, filtration-compatible affine factorization
   \(\widetilde D_X=\widetilde Q_X\widetilde A_X\) carrying the complete
   forcing jet;
3. grade-preserving reconstruction compatible with that shifted state;
4. a sheet map deriving the real base flow and positive bulk from the same
   state; and
5. a faithful full-port observer with a quadratic or nonlinear current
   functional whose endpoint law and Green identity are source-derived.

The formal-adjoint incidence is one possible constructor for item 5, but it is
not used by the confinement implication once the Green identity itself is
proved. It is therefore not a minimal theorem hypothesis.

## Current-cell independence test

Fix the same finite-cutoff Fourier data and the same reconstructed control port.
Choose two primitive endpoint assignments with identical incidence data but
with \(J_{\rm p}(q_1)-J_{\rm p}(q_0)=0\) in the first and \(1\) in the second.
The Fourier and adjoint relations are unchanged, while the current-cell truth
value changes. Hence current preservation is independent of those relations.
The endpoint equality must be an additional source datum, not a consequence of
Fourier sewing or formal adjointness.

The conditional theorem is therefore established, while the source-derived
theorem is not. No untyped scalar equality or inverse-Fourier identity can
remove this residual.

## Conditional abstract connection witness

The missing tuple is algebraically realizable without claiming that the source
constructs it. Let \(\mathcal H_X=\mathbb C^{m_X}\) with its standard Hermitian
pairing, choose any finite matrix \(B_{+,X}\), and set
\[
 B_{-,X}:=B_{+,X}^{*}.
\]
Then the adjoint residual vanishes identically. Define the control inclusion
by \(\mathcal R_N(e_0)=N^{-1}\Omega\), extend it linearly from the control
basis. Define a linear current readout on the control line by
\(\kappa_X(\Omega)=N J_{\rm cl}\), so that
\(\kappa_X(\mathcal R_N e_0)=J_{\rm cl}\) follows rather than being separately
assigned. Finally impose the single coherence equation
\[
\kappa_X(\mathcal R_N e_0)(q_1)-
\kappa_X(\mathcal R_N e_0)(q_0)=0.
\]
This produces a consistent finite-cutoff connection cell, and therefore the
conditional Green-identity proof applies. In the minimal case \(m_X=1\), take
\(B_{+,X}=[b]\) and \(B_{-,X}=[\overline b]\). Then
\(B_{-,X}-B_{+,X}^{*}=[0]\), while the reconstruction and coherence equations
are exactly \(\mathcal R_N(e_0)=N^{-1}\Omega\) and \(J_{\rm cl}(q_1)-J_{\rm cl}(q_0)=0\).
Thus all four required cell identities are simultaneously satisfiable.
The independence can be made fully explicit on \(\mathcal H_X=\mathbb C\): set
\(\Omega=1\) and \(\mathcal R_N(e_0)=1/N\). The readout
\(\kappa_0(x)(q)=NxJ\) has zero endpoint jump, whereas
\(\kappa_1(x)(q_0)=NxJ\) and \(\kappa_1(x)(q_1)=Nx(J+1)\) have endpoint jump
\(1\) on the same reconstructed input. Both are linear readouts and leave
\(B_{\pm,X}\) and \(\mathcal R_N\) unchanged. Hence reconstruction cannot
determine endpoint sewing.
It is not a source derivation:
choosing the pairing, \(B_{+,X}\), \(\kappa_X\), and the coherence equation is
new model data. The construction proves realizability and isolates exactly
which axioms must be supplied by a future Fourier–Tate theorem. For a concrete
specialization, take \(N=c=r=J_{\rm cl}=1\), \(\Omega=1\), and any scalar
\(z\), with \(f=-z/2\), \(u=1/2\), and \(v=-1/2\). Then
\(u'=v'=0\), \(w=0\), \(C=zr+2cf=0\), every prolongation vanishes, and
\(\int(u^2+v^2)=\frac12(q_1-q_0)>0\). With the constant readout
\(\kappa(1)=1\), endpoint sewing also holds. The conditional Green identity
then forces the chosen scalar \(z\) to vanish; this is a model check, not a
source derivation. In particular, the algebraic equations before applying the
Green identity admit a formal nonzero \(z\), but the complete theorem
hypotheses cannot all hold for that nonzero value. The witness therefore checks
consistency of the implication; it is not a counterexample to confinement.

## Implication audit

The constructed tuple proves the implication
\[
\{C=0,\ C^{(n)}=0,\ \text{zero flux},\ J_{\rm cl}(q_1)=J_{\rm cl}(q_0),\ \text{positive bulk}\}
\Longrightarrow z=0.
\]
It does not prove any reverse implication, does not derive the hypotheses from
Fourier–Tate sewing, and does not show that the base model preserves the
constrained sector. The two-readout countermodel shows specifically that
reconstruction and adjointness cannot replace endpoint-current sewing.

## Corrected weakest joint promotion theorem

Let \(z\) be the real centered scalar used by the declared base flow. A source
theorem suffices if it constructs one nonzero selected state \(\Omega_X\) and
maps satisfying
\[
\widetilde A_X(\Omega_X,1)=0,
\qquad
\widetilde D_X=\widetilde Q_X\widetilde A_X,
\qquad
\mathcal R_N(e_0)=N^{-1}\Omega_X,
\]
with completed, filtration-compatible versions of these identities. It must
also derive
\[
L_X\Omega_X=(u,v),
\qquad
u'=-zu-cf,
\qquad
v'=zv-cf,
\qquad
\|L_X\Omega_X\|^2=\int_I(u^2+v^2)\,dq>0,
\]
and a faithful observer
\[
\mathcal B_X:\mathcal H_X\to C(I,\mathcal O_X),
\qquad
j_X:\mathcal O_X\to\mathbb R,
\]
where \(\mathcal O_X\) contains all arithmetic, seam, and two-sign moment
ports. For \(J_{\rm cl}=j_X\mathcal B_X\Omega_X\), require \(w(q_0)=0\),
zero endpoint flux, equal endpoint values of \(J_{\rm cl}\), and the
source-derived Green identity. The affine factorization gives \(C=0\) and its
jet, hence \(w\equiv0\); the boundary conditions reduce the Green identity to
\[
2z\|L_X\Omega_X\|^2=0.
\]
Positive bulk then gives \(z=0\).

This theorem is weakest relative to the recorded independence tests. It does
not require formal adjointness once the Green identity is supplied, does not
replace the nonlinear current by a linear readout, and does not treat the
homogeneous Gaussian equalizer as compatible with a nonzero forcing anomaly.
No current artifact constructs the full interface, so the theorem remains
conditional rather than source-derived.

## Disposition

As a conditional model, the extension is usable: taking the minimal promotion
interface as an axiom yields scalar-null confinement by the Green identity.
Only the stronger claim that Fourier–Tate sewing derives those axioms remains
unestablished. The cheapest falsifier of preservation by the unextended model is explicit. Set \(c=f=0\),
\(z(t)=1+t\), and initial data \(u(0)=1\), \(v(0)=-1\). The base flow gives
\[
u(t)=e^{-t-t^2/2},\qquad v(t)=-e^{t+t^2/2},\qquad w(0)=0,
\]
but \(w(t)=e^{-t-t^2/2}-e^{t+t^2/2}\not\equiv0\). Moreover
\(z'r+2cf'=r\neq0\), so the required prolongation fails. This demonstrates
that the constraint is imposed rather than preserved by the unextended
equations. No claim of source-derived null confinement is made.
