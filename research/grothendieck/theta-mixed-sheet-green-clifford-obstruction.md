# Mixed right--left Green terms have a Clifford denominator obstruction

Status: exact mixed identity and no-go for a constant local two-sheet metric;
no RH claim

Use the sheared positive-tail features

\[
 A(q,z)=K_a^+(q,z),
 \qquad
 B(q,w)=K_{-a}^+(q,-w),                               \tag{1}
\]

with flows

\[
 A_q=-s_zA+g_a,
 \qquad
 B_q=-s_{-w}B+g_{-a},                                 \tag{2}
\]

where

\[
 s_z=1/2+iz,
 \qquad s_{-w}=1/2-iw.                               \tag{3}
\]

## Exact scalar mixed Green identity

For `P=A(q,z)overline{B(q,w)}`, differentiation gives

\[
 P_q=-[1+i(z+\bar w)]P
 +g_a\overline B+A g_{-a}.                            \tag{4}
\]

Assuming tail decay and integrating from zero to infinity yields

\[
 \boxed{
 \begin{aligned}
 i(z+\bar w)\int_0^\infty A\overline B\,dq
 ={}&A(0,z)\overline{B(0,w)}\\
 &-\int_0^\infty(A-g_a)
 \overline{(B-g_{-a})}\,dq\\
 &+\int_0^\infty g_ag_{-a}\,dq.
 \end{aligned}
 }                                                     \tag{5}
\]

This classifies the natural mixed flow exactly.  Its spectral denominator is
`z+bar(w)`, not the de Branges denominator `bar(w)-z`, and its bulk is a cross
pairing rather than a norm square.

## Two-sheet Clifford form

Place the right and left features in

\[
 \Psi(q,z)=\binom{K_a^+(q,z)}{K_{-a}^+(q,-z)}.         \tag{6}
\]

Ignoring the declared forcing for the spectral typing, the homogeneous flow
is

\[
 \Psi_q=left(-\frac12I-iz\sigma_3\right)\Psi,
 \qquad
 \sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.     \tag{7}
\]

Let `M` be a constant Hermitian Green metric.  Its spectral contribution is

\[
 i\bar w\,\sigma_3M-iz\,M\sigma_3.                   \tag{8}
\]

Decompose `M` into the part commuting with `sigma_3` and the part
anticommuting with it:

\[
 M=M_{\parallel}+M_{\perp},
 \quad[\sigma_3,M_{\parallel}]=0,
 \quad\{\sigma_3,M_{\perp}\}=0.                     \tag{9}
\]

Then (8) becomes

\[
 \boxed{
 i(\bar w-z)\sigma_3M_{\parallel}
 +i(\bar w+z)\sigma_3M_{\perp}.
 }                                                     \tag{10}
\]

The commuting metrics are sheet-diagonal and produce the required de Branges
difference denominator.  Every right--left cross metric is off-diagonal,
belongs to `M_perp`, and necessarily produces the sum denominator.

Therefore

\[
 \boxed{
 \text{no constant local two-sheet Green metric can turn the mixed
 cross terms into a }(\bar w-z)\text{ positive bulk.}
 }                                                     \tag{11}
\]

This is a spectral-typing obstruction, not a missing inequality.

## Consequence for modular sewing

The cross terms in

\[
 E_a(z)=H_a^+(z)+H_{-a}^+(-z)                         \tag{12}
\]

cannot be controlled by simply adding the two independent one-chart Green
energies.  One of three stronger mechanisms is necessary:

1. **Exact cancellation:** modular sewing cancels the off-diagonal
   polarization before division by `bar(w)-z`.
2. **Seam localization:** the mixed bulk in (5) transfers entirely to a
   source-fixed boundary form at `q=0`.
3. **Coupled evolution:** the completed source supplies an off-diagonal
   connection between the two sheets, changing the spectral generator so
   that a positive metric can produce the correct denominator.

An invented constant coupling chosen to repair (10) is inadmissible.  It must
be derived from the bilateral modular incidence and must preserve the exact
Clark outputs.

## Sharp next falsifier

Compute the genuine bilateral sewing map at the scale seam.  If its pullback
leaves a nonzero `M_perp` bulk while the spectral generator remains diagonal
as in (7), the arithmetic-shear mechanism cannot close through a local
positive Green identity.  If the pullback annihilates `M_perp` or converts it
to the primitive seam form, the architecture reduces to the single declared
defect.

## The physical cross polarization is a reflection coboundary

The individual mixed products in (5) are not the physical cross object.
Write

\[
 P(z)=H_a^+(z),\qquad Q(z)=H_{-a}^+(z),
\]

and retain the full alternating polarization produced by the two Clark
sheets:

\[
\begin{aligned}
 \mathcal X_a(z,w)={}&
 P(z)\overline{Q(-w)}+Q(-z)\overline{P(w)}\\
 &-Q(z)\overline{P(-w)}-P(-z)\overline{Q(w)}.
                                                               \tag{13}
\end{aligned}
\]

The source functions are real, so
`overline(P(bar(z)))=P(z)` and similarly for `Q`.  Consequently, on the
reflected diagonal `w=-bar(z)`, the first term cancels the fourth and the
second cancels the third:

\[
 \boxed{\mathcal X_a(z,-\bar z)=0.}                  \tag{14}
\]

To state divisibility precisely, regard `zeta=bar(w)` as the independent
antiholomorphic coordinate.  The numerator in (13) is analytic in
`(z,zeta)` and vanishes on `zeta=-z`; hence

\[
 \boxed{
 \mathcal X_a(z,w)=(z+\bar w)\mathcal R_a(z,w)
 }
                                                               \tag{15}
\]

for an analytic kernel `mathcal R_a`.  Thus the denominator produced by the
mixed Green identity is not a false pole: it is exactly the factor already
carried by the physical alternating cross polarization.

This removes one obstruction but does not prove positivity.  In the de
Branges quotient the same contribution is

\[
 \frac{\mathcal X_a(z,w)}{\bar w-z}
 =\frac{z+\bar w}{\bar w-z}\mathcal R_a(z,w).        \tag{16}
\]

The Cayley factor in (16) is not positive by itself.  The correct conclusion
is therefore structural:

\[
 \boxed{
 \text{the mixed term is a reflection coboundary, not an independent
 positive channel.}
 }
                                                               \tag{17}
\]

It vanishes on the reflection-fixed relation and, on the kernel diagonal,
vanishes along `Re(z)=0`.  Hence the cross obstruction is purely horizontal:
it begins only when one moves away from the sheet-reflection axis.

The revised target is to combine `mathcal R_a` with the sheet-diagonal Green
energies *before* division by `bar(w)-z`.  Trying to prove positivity of each
mixed product separately discards the source-forced cancellation (14).

## Transverse-jet reduction

Equation (15) turns the entire mixed sector into a first-order transverse
question.  With `zeta=bar(w)`, analytic division gives on the reflected
diagonal

\[
 \mathcal R_a(z,-\bar z)
 =\left.\partial_\zeta\mathcal X_a(z,\zeta)
   \right|_{\zeta=-z}.                              \tag{18}
\]

Thus no infinite collection of independent mixed inequalities remains.  The
source must control one oriented normal derivative of its reflection
coboundary.

On the ordinary kernel diagonal, write `z=x+iy`.  Then

\[
 z+\bar z=2x,\qquad \bar z-z=-2iy,
\]

so the mixed de Branges contribution has the exact form

\[
 \boxed{
 \frac{\mathcal X_a(z,z)}{\bar z-z}
 = i\frac{x}{y}\mathcal R_a(z,z).
 }                                                     \tag{19}
\]

This explains two geometric facts at once:

* the cross channel is invisible on the sheet-reflection axis `x=0`;
* away from that axis its sign is governed by an oriented transverse jet,
  amplified only by the explicit geometric ratio `x/y`.

The smallest hostile test is now exact rather than numerical: determine
whether `i mathcal R_a(z,z)` has the sign opposite to `x`, or whether its
negative part is dominated by the already-positive sheet-diagonal energy.
One counterexample suffices to rule out termwise transverse positivity; it
does not rule out domination by the diagonal bulk.

This gives the next source-derived theorem candidate:

\[
 \boxed{
 \text{diagonal sheet energy}
 +i(x/y)\,\text{reflection-transverse jet}>0
 \quad (0<y<1/2).
 }                                                     \tag{20}
\]

Unlike a free positivity ansatz, every term in (20) is forced by the completed
two-sheet theta source and its reflection incidence.

## Symplectic factorization of the transverse jet

The jet in (18) has a stronger closed form.  Introduce the even and odd parts
of the two Clark sheets,

\[
 P=P_e+P_o,\qquad Q=Q_e+Q_o,
\]

and the symplectic bracket `det`.  Direct expansion of (13), with
`zeta=bar(w)` treated independently, gives

\[
 \mathcal X_a(z,\zeta)
 =-2\{\det(U(\zeta),V(z))+\det(U(z),V(\zeta))\},    \tag{21}
\]

where

\[
 U=(P_e,Q_e),\qquad V=(P_o,Q_o).
\]

The factor `z+zeta` is therefore the algebraic consequence of pairing an
even sheet vector with an odd sheet vector.  It is not an accidental zero of
the final scalar readout.

More directly, differentiating (13) at `zeta=-z` yields

\[
 \boxed{
 \mathcal R_a(z,-\bar z)=W_a(z)+W_a(-z),
 \qquad
 W_a=QP'-PQ'.
 }                                                     \tag{22}
\]

Thus the transverse datum is precisely the even part of the Wronskian of the
two Clark sheets.

Now write both sheets in terms of their common one-sided source transform
`F`:

\[
 P=F+iaF',\qquad Q=F-iaF'.                           \tag{23}
\]

Their Wronskian is elementary:

\[
 \boxed{
 W_a(z)=2ia\bigl(F(z)F''(z)-F'(z)^2\bigr).
 }                                                     \tag{24}
\]

Consequently

\[
 \boxed{
 \mathcal R_a(z,-\bar z)
 =2ia\,[L_F(z)+L_F(-z)],
 \qquad L_F=FF''-(F')^2.
 }                                                     \tag{25}
\]

The mixed-sheet obstruction has therefore collapsed to the even logarithmic
curvature numerator of the primitive theta transform.  Away from zeros of
`F`,

\[
 L_F=F^2(\log F)''.
\]

This is the same curvature object that appears in Laguerre inequalities,
Hankel two-minors, and the earlier Schwarzian reduction.  The Green and
moment approaches were probing the same source invariant in different
coordinates.

The next falsifier is correspondingly sharp: test whether the completed
bilateral combination of `L_F(z)+L_F(-z)` has the orientation required by
(20).  Failure disproves standalone transverse-jet positivity but leaves the
weaker diagonal-energy domination theorem intact.

## Identification with the Clark derivative and order-two tower

There are two equivalent readings of (24).  First,

\[
 \boxed{
 \left(\frac{P}{Q}\right)'=\frac{W_a}{Q^2}.
 }                                                     \tag{26}
\]

Thus the Wronskian is the numerator of the derivative of the Clark Cayley
ratio.  The missing transverse orientation is exactly the infinitesimal
orientation of that ratio; it is not an additional positivity structure.

Second,

\[
 \boxed{
 \frac{L_F}{F^2}=(\log F)''.
 }                                                     \tag{27}
\]

Whenever the canonical product of `F` has only a linear exponential factor,
logarithmic differentiation gives formally, and locally normally away from
the zeros,

\[
 (\log F)''(z)=-\sum_\rho\frac{m_\rho}{(z-\rho)^2}.  \tag{28}
\]

Any polynomial contribution must be audited for the precise completed
one-sided transform before using (28).  Subject to that audit, (28) is the
same order-two resolvent kernel that generated the proposed Stieltjes/Hankel
tower.

Therefore the current three approaches coincide at their nontrivial core:

\[
 \boxed{
 \text{mixed Green transverse jet}
 \equiv
 \text{Clark-ratio derivative}
 \equiv
 \text{order-two logarithmic curvature}.
 }                                                     \tag{29}
\]

This equivalence prevents a false multiplication of evidence.  Proving any
one of these presentations positive by assuming another would be circular.
Its value is instead that it identifies the one source invariant for which a
noncircular theta identity must be found.

## Direct source formula and reflection-axis sign theorem

Let the primitive one-sided transform be

\[
 F(z)=\int_0^\infty f(u)e^{izu}\,du,
 \qquad f(u)>0,
\]

with sufficient decay to differentiate twice.  Direct differentiation and
symmetrization give the exact identity

\[
 \boxed{
 \mathscr C_F(z):=F(z)F''(z)-F'(z)^2
 =-\frac12\iint_{(0,\infty)^2}
 (u-v)^2f(u)f(v)e^{iz(u+v)}\,du\,dv.
 }                                                     \tag{30}
\]

The squared separation is source-derived: it is the second centered minor of
the two-copy transport, not an inserted comparison weight.

On the reflection-fixed imaginary axis `z=iy`, `y>0`, the phase becomes a
positive Laplace weight.  Therefore

\[
 \boxed{
 \mathscr C_F(iy)<0
 }
                                                               \tag{31}
\]

unless the source is supported at a single point.  Equivalently,

\[
 (\log F)''(iy)<0,
\]

because `F(iy)>0`.  This is a genuine universal coupled-positivity theorem:
every nondegenerate positive source has strictly log-concave Laplace
transform along the reflection-fixed axis.

Combining (25) and (31), for `a>0`,

\[
 i\mathcal R_a(iy,iy)>0,                              \tag{32}
\]

with the argument interpreted through the reflected-diagonal coordinates of
(25).  The mixed sheet therefore has a definite infinitesimal orientation on
the sheet-reflection axis.  The unresolved problem is extension away from
that axis, not selection of its orientation there.

This axis must not be confused with the RH locus.  In the spectral convention

\[
 X(z)=\xi\!\left(\frac12+iz\right),\qquad z=x+iy,
\]

the RH critical line is `y=0`, whereas the fixed set `z=-bar(z)` used above is
`x=0`.  The theorem (31) is therefore a source boundary condition transverse
to the spectral direction, not a zero-free neighborhood of the RH line.

## Canonical sum--difference pushforward

Put

\[
 S=u+v,\qquad D=u-v.
\]

Then (30) becomes

\[
 \mathscr C_F(z)=-\int_0^\infty e^{izS}\,d\mu_2(S),  \tag{33}
\]

where the positive order-two separation measure is

\[
 \boxed{
 d\mu_2(S)=\frac14
 \int_{-S}^{S}D^2
 f\!\left(\frac{S+D}{2}\right)
 f\!\left(\frac{S-D}{2}\right)dD\,dS\ge0.
 }                                                     \tag{34}
\]

Thus all oscillation has been pushed into the single faithful quotient
coordinate `S`; the fiber coordinate `D` has already been integrated with a
nonnegative weight.  This is exactly the durable finite-to-one rule: the
claim is made against the faithful sum coordinate, not against an arbitrary
scalar projection of the two-copy source.

For `z=x+iy`,

\[
 \mathscr C_F(x+iy)
 =-\int_0^\infty e^{-yS}e^{ixS}\,d\mu_2(S).          \tag{35}
\]

The remaining RH obstruction is now sharply isolated: modular completion
must orient the Fourier transform of the positive measure `mu_2` throughout
`0<y<1/2`.  Positivity of `mu_2` alone cannot do this; a positive measure may
have an oscillatory Fourier transform.  The missing input must therefore be
a modular variation-diminishing or boundary-repair theorem for this exact
order-two pushforward.

## Theta-label separation and the quadratic arithmetic repair

The exact theta scaling law

\[
 \phi_n(u)=n^{-1/2}\phi_1(u+\log n)                  \tag{36}
\]

adds more structure to `mu_2` than positivity alone.  In the contribution of
the ordered label pair `(m,n)`, change variables

\[
 r=u+\log m,\qquad t=v+\log n.
\]

Then

\[
 u-v=(r-t)+\log(n/m),                                \tag{37}
\]

and

\[
 u+v=r+t-\log(mn).                                   \tag{38}
\]

Consequently the separation square is

\[
 (u-v)^2=(r-t)^2+2(r-t)\log(n/m)+\log^2(n/m).        \tag{39}
\]

The completed two-copy source contains both ordered pairs `(m,n)` and
`(n,m)`.  After simultaneously exchanging `r` and `t`, their linear terms
cancel.  The symmetrized separation weight is therefore

\[
 \boxed{
 2\bigl[(r-t)^2+\log^2(n/m)\bigr]\ge0.
 }                                                     \tag{40}
\]

The second summand is a source-forced **quadratic arithmetic repair**.  It
vanishes precisely on equal labels and measures squared distance in the
multiplicative label lattice.  For adjacent prime transport `n=pm`, it is
exactly

\[
 \log^2(n/m)=\log^2p.                                \tag{41}
\]

This is the order-two descendant of the first-order commutator cocycle
`[M_a,S_p]=a log(p)S_p`: the Clark fold sees oriented displacement `log p`,
while curvature sees its positive square.

The transformed domain for `(m,n)` is

\[
 r\ge\log m,\qquad t\ge\log n,                       \tag{42}
\]

and the domain for `(n,m)` becomes exactly (42) after simultaneously
exchanging `r` and `t`.  Therefore the cancellation of the linear term and
the positive repair (40) hold on the entire pair domain, with no unmatched
strip.  The exact faithful-label architecture is

\[
 \boxed{
 \text{positive geometric separation}
 +\text{positive }\log^2(n/m)\text{ repair}.
 }                                                     \tag{43}
\]

Finite sewing strips appear only after compressing the faithful label sum
into a prime-recursive presentation; they are coordinate-boundary terms, not
defects of the full two-copy source.  The label lattice cannot generate an
indefinite separation weight after ordered-pair symmetrization.  The next
theorem is therefore to determine whether its additional multiplicative
distance structure forces orientation of the cosine transform, or whether a
hostile positive label lattice still produces a negative lobe.

## Smallest hostile label-pair falsifier

The quadratic arithmetic repair does not by itself orient the cosine
transform.  Take an idealized positive primitive carrier concentrated at
`r=R` and retain two labels `m\ne n`, with `R>max(log(m),log(n))`.  Their
physical source points are

\[
 u_m=R-\log m,\qquad u_n=R-\log n.
\]

The equal-label pairs have zero separation weight.  The two cross-label pairs
produce the single positive separation atom

\[
 (u_m-u_n)^2=\log^2(n/m),
 \qquad
 S_0=u_m+u_n=2R-\log(mn)>0.                           \tag{44}
\]

Hence, up to a positive coefficient,

\[
 -\mathscr C_F(x)=\log^2(n/m)\cos(xS_0),             \tag{45}
\]

which changes sign.  Smooth narrow positive carriers preserve a negative
lobe, so this is not an artifact of using point masses.

Therefore

\[
 \boxed{
 \text{positive multiplicative separation, even with exact label-pair
 symmetry, does not imply oscillatory orientation.}
 }                                                     \tag{46}
\]

The missing hypothesis cannot be a finite-label inequality.  It must use the
infinite completed theta organization: reciprocal-scale sewing, its precise
weights, or a variation-diminishing property that is destroyed by finite
label truncation.  This falsifier also forbids interpreting the arithmetic
`log^2` repair as an RH mechanism on its own.

## Continuum orientation system suggested by the Pluecker lane

The appropriate analogue of signed total positivity is not an
`x`-independent sign attached to the quotient coordinate `S`.  No such gauge
can orient `cos(xS)` for all `x`: for every fixed `S>0`, its sign changes as
`x` varies.

For each `x>0`, instead partition the faithful quotient ray into its canonical
consecutive cosine bands

\[
 I_k(x)=\left[
 \frac{(k-1/2)\pi}{x},
 \frac{(k+1/2)\pi}{x}
 \right]\cap[0,\infty),                              \tag{47}
\]

on which the kernel has alternating orientation `(-1)^k`.  A modular
orientation theorem would have to transport the restricted measures

\[
 \mu_{2,k}^{(x)}=\mu_2|_{I_k(x)}                     \tag{48}
\]

through source-derived adjacent-band correspondences so that every negative
band is dominated by its coherently paired positive band.

The essential word is **coherently**.  Pairings chosen separately for each
`x` merely restate the desired inequality.  The transport must commute with

* motion of the band walls as `x` varies;
* reciprocal-scale reflection;
* prime-label refinement and regrouping;
* creation of a new terminal band at infinity.

These compatibilities form a sign-incidence graph whose vertices are band
charts and modular refinements.  Each transport supplies a relative sign.
As in the finite Pluecker problem, the first exact falsifier is a cycle whose
sign product is negative.  A positive result is a source-derived orientation
local system with trivial holonomy.

Thus the shared cross-sector principle becomes

\[
 \boxed{
 \text{positivity after oscillatory projection}
 =\text{positive source weight}
 +\text{coherent transported orientation}.
 }                                                     \tag{49}
\]

For theta, the orientation system must be parameter-covariant rather than a
fixed gauge.  This distinction is forced by the moving zeros of the cosine
kernel and prevents importing the finite matrix statement too literally.

## Sign-local-system no-go and the faithful phase bundle

Prime transport exposes a stronger obstruction to (49).  Translation of the
faithful quotient coordinate by `c` acts on the oscillatory feature as

\[
 e^{ix(S-c)}=e^{-ixc}e^{ixS}.                        \tag{50}
\]

On real and imaginary components this is the rotation

\[
 \binom{\cos x(S-c)}{\sin x(S-c)}
 =
 \begin{pmatrix}
 \cos xc&\sin xc\\
 -\sin xc&\cos xc
 \end{pmatrix}
 \binom{\cos xS}{\sin xS}.                          \tag{51}
\]

For a prime shift `c=log(p)` (and for the two-copy sum shift built from
`log(mn)`), the angle `xc` is generically not an integral multiple of `pi`.
Therefore prime transport does not preserve the cosine line even up to sign.
It mixes cosine and sine continuously.

Hence

\[
 \boxed{
 \text{no }\{\pm1\}\text{-valued band orientation can be covariant under
 all prime-scale transports.}
 }                                                     \tag{52}
\]

The faithful orientation carrier is instead the rank-two real phase bundle,
or equivalently a complex line, with prime holonomy

\[
 \rho_x(p)=e^{-ix\log p}=p^{-ix}.                    \tag{53}
\]

This representation is multiplicatively flat:

\[
 \rho_x(mn)=\rho_x(m)\rho_x(n).                      \tag{54}
\]

Thus the full arithmetic transport is coherent before scalar readout.  The
apparent sign incoherence is created only when one projects the rotating
two-component feature onto its cosine coordinate.

The corrected architecture is

\[
 \boxed{
 \text{positive separation source}
 \to\text{flat arithmetic }SO(2)\text{ transport}
 \to\text{source-selected cone}
 \to\text{cosine readout}.
 }                                                     \tag{55}
\]

This replaces the proposed sign-local-system theorem.  What must be proved is
that modular completion selects a covariant cone in the rank-two phase
bundle whose scalar cosine projection has the required orientation.  A cone
chosen after projection is not source-derived.

The smallest falsifier is now representation-theoretic: if the prime
rotations generated by (53) admit no nontrivial source-fixed proper cone after
bilateral sewing, then pointwise cone preservation cannot prove RH.  One must
instead use a quadratic/Gram form invariant under the rotations.

## Dense-prime-rotation theorem: the cone route is closed

The preceding falsifier can be decided without computation.  Fix `x ne 0`.
If both rotation angles

\[
 \frac{x\log2}{2\pi},\qquad \frac{x\log3}{2\pi}
\]

were rational, their ratio `log(2)/log(3)` would be rational.  That would give
positive integers `r,s` with

\[
 r\log2=s\log3,
\]

hence `2^r=3^s`, contradicting unique factorization.  At least one of the two
prime rotations is therefore irrational, and its powers are dense in
`SO(2)`.

Any closed convex cone in `R^2` invariant under every prime transport is then
invariant under all rotations.  Its only possibilities are

\[
 \{0\}\quad\text{or}\quad\mathbb R^2.               \tag{56}
\]

In particular there is no nontrivial proper positive cone preserved by the
faithful arithmetic phase representation.

Therefore

\[
 \boxed{
 \text{prime-covariant linear cone orientation cannot be the RH mechanism.}
 }                                                     \tag{57}
\]

This is a useful hard no-go, not a failure of modular coherence.  The prime
phase connection is perfectly flat; it is simply too irreducible over the
real plane to preserve an order cone.  The first faithful positive invariant
is quadratic:

\[
 \cos^2(xS)+\sin^2(xS)=1.                            \tag{58}
\]

Accordingly the only surviving route in this architecture is a
rotation-invariant Hermitian/Gram energy, with modular sewing controlling the
finite defect channels.  This returns, noncircularly, to the Green identity:
its quadratic bulk is not an optional reformulation but the minimal positive
object compatible with all prime transports.

## Quadratic classification: invariant trace versus spin two

Dense rotational covariance also makes the local positive metric unique.  If
`M` is a real symmetric two-by-two matrix satisfying

\[
 R_\theta^TMR_\theta=M
\]

for every prime rotation, density and continuity imply the same identity for
all `R_theta in SO(2)`.  Hence

\[
 \boxed{M=cI.}                                      \tag{59}
\]

For `c>0` this is the unique invariant positive quadratic form, up to scale.
There is no hidden alternative metric that modular arithmetic might select.

But the curvature readout is not this invariant norm.  Define the two-copy
amplitude

\[
 \psi_z(u,v)=(u-v)\sqrt{f(u)f(v)}
 e^{iz(u+v)/2}.                                      \tag{60}
\]

Then

\[
 -\mathscr C_F(z)=\frac12\iint\psi_z(u,v)^2\,du\,dv,
                                                               \tag{61}
\]

whereas the invariant Gram energy is

\[
 \frac12\iint|\psi_z(u,v)|^2\,du\,dv\ge0.          \tag{62}
\]

Writing `psi=A+iB`, these are respectively

\[
 \operatorname{Re}(\psi^2)=A^2-B^2,
 \qquad
 |\psi|^2=A^2+B^2.                                  \tag{63}
\]

Thus curvature is the traceless, spin-two component of the quadratic tensor,
while Gram positivity is its rotationally invariant trace.  Under a prime
phase rotation by `theta`, the curvature component rotates by `2theta`.
Dense prime phases therefore destroy any invariant sign for it just as they
did at linear order.

This yields a second hard boundary:

\[
 \boxed{
 \text{Gram positivity alone cannot orient the logarithmic curvature.}
 }                                                     \tag{64}
\]

The missing modular identity must do something more precise: express the
spin-two curvature readout as an invariant trace energy minus explicit
source-fixed seam terms, and then repair or cancel those terms.  This is
exactly the shape already exposed by the Green calculation,

\[
 \text{positive bulk}-\text{primitive line}-\text{seam line},
\]

now derived from representation type rather than guessed from integration by
parts.

The minimal live theorem is therefore:

\[
 \boxed{
 \text{completed modular sewing converts the spin-two theta curvature into
 the unique invariant Gram trace plus controlled finite-rank defects.}
 }                                                     \tag{65}
\]

If the completed sewing leaves any uncontrolled spin-two bulk, no
prime-covariant positive-energy proof of this form can close.

## Localization of all orienting information

The dense-rotation argument applies to the translation-covariant interior of
the label flow.  That interior can carry the invariant trace energy but cannot
choose an orientation for the spin-two component.  Therefore every possible
orientation of `mathscr C_F` must be supported where covariance ceases to be
an honest two-sided unitary action:

* the primitive lower endpoint of the label semigroup;
* the finite currents created by stopping a prime translation;
* the reciprocal-scale modular seam;
* their Clark-differentiated logarithmic repair terms.

Consequently

\[
 \boxed{
 \text{all RH-relevant orientation data are boundary/seam data;
 the arithmetic bulk supplies only universal positive energy.}
 }                                                     \tag{66}
\]

This reverses the tempting interpretation of the Green defects.  They are not
errors to be bounded after constructing the bulk proof.  They are the only
source locations capable of breaking rotational symmetry and selecting the
curvature direction.  A proof that discards them necessarily discards the RH
content.

The analogy with the level-44 theorem is now exact at the architectural level:
a symmetric positive bulk has no directional information, while a small
source-fixed boundary channel repairs and orients the unique near-critical
mode.  No numerical inference from level 44 is being made; the shared claim
is the typed role of the defect channel.

## Exact bilateral curvature decomposition

The reciprocal seam channel can be computed explicitly.  Let the completed
even transform be

\[
 X(z)=F(z)+F(-z).                                    \tag{67}
\]

Expanding `mathscr C_X=XX''-(X')^2` gives

\[
 \boxed{
 \mathscr C_X(z)=\mathscr C_F(z)+\mathscr C_F(-z)
 +\mathscr S_F(z),
 }                                                     \tag{68}
\]

where the opposite-sheet seam is

\[
 \mathscr S_F(z)=
 F(z)F''(-z)+F(-z)F''(z)+2F'(z)F'(-z).               \tag{69}
\]

Using the positive half-source directly,

\[
 \boxed{
 \mathscr S_F(z)=
 -\iint_{(0,\infty)^2}(u+v)^2f(u)f(v)e^{iz(u-v)}\,du\,dv.
 }                                                     \tag{70}
\]

The same-sheet curvature measures squared **difference** `(u-v)^2` and
oscillates in the sum coordinate.  The modular seam measures squared
**sum** `(u+v)^2` and oscillates in the difference coordinate.  Reciprocal
reflection exchanges the roles of the two faithful quotient coordinates.

Although (70) is an infinite integral, its two-variable kernel has algebraic
rank at most three:

\[
 (u+v)^2=u^2\cdot1+2u\cdot v+1\cdot v^2.            \tag{71}
\]

Thus the entire opposite-sheet curvature channel is determined by the three
source moments `F,F',F''`.  This is the explicit finite-rank defect promised
by the representation argument.

On the RH spectral locus `z=x in R`, reality of the source gives

\[
 \boxed{
 \mathscr S_F(x)
 =2\operatorname{Re}\!\bigl(F''(x)\overline{F(x)}\bigr)
 +2|F'(x)|^2
 =\frac{d^2}{dx^2}|F(x)|^2.
 }                                                     \tag{72}
\]

Therefore the completed curvature problem on the RH line is exactly

\[
 \boxed{
 \mathscr C_X(x)=2\operatorname{Re}\mathscr C_F(x)
 +\bigl(|F(x)|^2\bigr)''.
 }                                                     \tag{73}
\]

This is a concrete theorem-sized reduction: the infinite positive separation
bulk is corrected by one rank-three horizontal seam jet.  No unspecified
modular boundary term remains at this level.

The sharp falsifier is now whether (73) has the orientation required by the
de Branges kernel after the precise Clark normalization.  If not, further
prime sampling must alter the bulk decomposition; it cannot alter the exact
bilateral identity itself.

## Rank-two moment determinant on the RH spectral axis

For real `x`, define the half-source moments

\[
 C_0(x)=\int_0^\infty f(u)\cos(xu)\,du,
 \quad
 S_1(x)=\int_0^\infty u f(u)\sin(xu)\,du,
 \quad
 C_2(x)=\int_0^\infty u^2 f(u)\cos(xu)\,du.          \tag{74}
\]

The completed even transform and its first two derivatives are

\[
 X(x)=2C_0(x),\qquad X'(x)=-2S_1(x),qquad
 X''(x)=-2C_2(x).                                    \tag{75}
\]

Hence the full bilateral curvature reduces to

\[
 \boxed{
 -\frac14\mathscr C_X(x)=C_0(x)C_2(x)+S_1(x)^2.
 }                                                     \tag{76}
\]

The positive square `S_1^2` is the exact coupled repair of the potentially
negative product `C_0C_2`.  Failure can occur only where `C_0` and `C_2` have
opposite signs and

\[
 |C_0C_2|>S_1^2.                                     \tag{77}
\]

Thus the infinite two-copy question has compressed, on the RH locus, to one
scalar hostile inequality.

There is also a canonical geometric form.  Put

\[
 V(x)=\binom{C_0(x)}{S_1(x)}.
\]

Since `C_0'=-S_1` and `S_1'=C_2`,

\[
 \boxed{
 \det(V,V')=C_0C_2+S_1^2=-\frac14\mathscr C_X.
 }                                                     \tag{78}
\]

The first Laguerre curvature inequality is therefore exactly positive
orientation of the source-derived planar moment curve `V`.  Away from zeros
of `C_0`, it is equivalently

\[
 \left(\frac{S_1}{C_0}\right)'
 =\frac{C_0C_2+S_1^2}{C_0^2}\ge0.                   \tag{79}
\]

This is the real-axis Clark-ratio monotonicity in elementary source
coordinates.  At a simple zero of `C_0`, (76) is automatically strict unless
`S_1` also vanishes; the dangerous regions lie between zeros, where the
curvature product can oppose the square repair.

Equation (78) supplies a more faithful Carrier statement than positivity of
an isolated scalar: modular completion must make the moment curve wind with
one orientation.  A reversal of its oriented area velocity is the smallest
exact falsifier.

Scope: (76)--(79) express the first Laguerre inequality.  They do not by
themselves establish RH; sufficiency requires the full Laguerre--Pólya/de
Branges conditions rather than one curvature inequality.

## Exact hostile entire-function falsifier for first curvature

The scope warning is essential, not merely formal.  For `a,b>0`, consider

\[
 Y_{a,b}(z)=e^{-az^2}(z^2+b^2).                      \tag{80}
\]

It has the nonreal zeros `z=plus-or-minus ib`.  Yet on the real axis

\[
 (\log Y_{a,b})''(x)
 =-2a+\frac{2(b^2-x^2)}{(x^2+b^2)^2}.               \tag{81}
\]

The rational term is at most `2/b^2`, with equality at `x=0`.  Therefore, if

\[
 a>1/b^2,
\]

then

\[
 (\log Y_{a,b})''(x)<0
 \quad\text{for every real }x.                       \tag{82}
\]

Equivalently,

\[
 (Y'_{a,b})^2-Y_{a,b}Y''_{a,b}>0
 \quad\text{on }\mathbb R,                           \tag{83}
\]

despite the off-real zero pair.

Thus

\[
 \boxed{
 \text{strict one-oriented winding of }(Y,-Y')
 \text{ on the real axis does not force real-rootedness.}
 }                                                     \tag{84}
\]

The first curvature theorem remains a necessary boundary shadow and a useful
local falsifier, but it cannot be the Deutsch--Popperian RH conjecture.  The
long-horizon target must retain either the full upper-half-plane de Branges
kernel or an equivalent complete hierarchy of generalized Laguerre/Hankel
conditions.  Any proof architecture that ends at (76) is now decisively
closed.

## Full generalized-Laguerre separation tower

For an entire transform `Y`, define the `n`th generalized Laguerre form by

\[
 \mathcal L_n[Y](z)=
 \frac1{(2n)!}\sum_{j=0}^{2n}
 (-1)^{j+n}\binom{2n}{j}
 Y^{(j)}(z)Y^{(2n-j)}(z).                            \tag{85}
\]

For `n=1`, this is `(Y')^2-YY''`.  If

\[
 Y(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du
\]

with a positive rapidly decreasing completed source, substitution of the
derivatives into (85) and the binomial theorem give

\[
 \boxed{
 \mathcal L_n[Y](z)=
 \frac1{(2n)!}\iint_{\mathbb R^2}
 (u-v)^{2n}\Phi(u)\Phi(v)e^{iz(u+v)}\,du\,dv.
 }                                                     \tag{86}
\]

Thus every member of the complete hierarchy is source-positive before the
oscillatory quotient readout.  Pushing forward by `S=u+v` defines a canonical
positive measure

\[
 d\mu_{2n}(S)=\frac12\int_{mathbb R}
 D^{2n}\Phi\!\left(\frac{S+D}{2}\right)
 \Phi\!\left(\frac{S-D}{2}\right)dD\,dS,            \tag{87}
\]

up to the fixed Jacobian convention, and

\[
 \mathcal L_n[Y](z)=\frac1{(2n)!}
 \int_{\mathbb R}e^{izS}\,d\mu_{2n}(S).             \tag{88}
\]

For the even completed theta source, `mu_{2n}` is even, so on the RH spectral
axis

\[
 \boxed{
 \mathcal L_n[X](x)=\frac{2}{(2n)!}
 \int_0^\infty\cos(xS)\,d\mu_{2n}(S).
 }                                                     \tag{89}
\]

The first-curvature falsifier (80) shows why the index `n` cannot be thrown
away.  The complete source object is the entire family of even separation
measures

\[
 \{\mu_0,\mu_2,\mu_4,\ldots\},                       \tag{90}
\]

not `mu_2` alone.  Subject to the standard growth/genus hypotheses that must
be checked for the completed theta transform, nonnegativity of the full
generalized Laguerre hierarchy is the appropriate Laguerre--Polya target.

The sharpened Deutsch--Popperian conjecture is therefore

\[
 \boxed{
 \text{modular completion coherently orients every even-distance
 pushforward }\mu_{2n}\text{, uniformly in }n.
 }                                                     \tag{91}
\]

Its smallest falsifier is a pair `(n,x)` with
`mathcal L_n[X](x)<0`.  Unlike accumulating finite disks, this hierarchy is
structurally complete: an off-line zero must eventually violate an exact
member once the equivalence hypotheses are established.

## Exact generating function: the tower is vertical modulus geometry

Summing (86) over all orders gives

\[
\begin{aligned}
 \sum_{n=0}^\infty \mathcal L_n[X](z)t^{2n}
 &={}
 \iint \Phi(u)\Phi(v)e^{iz(u+v)}
 \cosh\!\bigl(t(u-v)\bigr)\,du\,dv\\
 &=X(z-it)X(z+it).                                   \tag{92}
\end{aligned}
\]

For real `x`, the real structure of `X` yields

\[
 \boxed{
 \sum_{n=0}^\infty \mathcal L_n[X](x)t^{2n}
 =|X(x+it)|^2.
 }                                                     \tag{93}
\]

Therefore the generalized Laguerre tower is not an auxiliary moment
construction.  Its entries are exactly the even vertical Taylor coefficients
of the completed modulus about the RH spectral axis.

Pointwise positivity of the right side is automatic and says almost nothing:
every modulus square is nonnegative.  The nontrivial condition is
**coefficientwise** positivity in `t^2`:

\[
 \mathcal L_n[X](x)\ge0
 \quad\text{for all }n\ge0, x\in\mathbb R.          \tag{94}
\]

Equivalently, for each real `x`, the function

\[
 r\longmapsto |X(x+i\sqrt r)|^2                     \tag{95}
\]

must be absolutely monotone at `r=0` to all orders, with the appropriate
global analytic continuation.  This explains how every finite probe can be
strictly positive while the complete infinite tower still carries the exact
support constraint.

When all zeros are real, the canonical product heuristically displays the
mechanism:

\[
 |X(x+it)|^2
 \sim \prod_\gamma\bigl((x-\gamma)^2+t^2\bigr),      \tag{96}
\]

whose finite product coefficients in `t^2` are nonnegative.  Turning this
heuristic into an equivalence requires the already-declared canonical-product
and limiting audits.

The research target can now be stated without choosing among Green, Clark,
or moment language:

\[
 \boxed{
 \text{derive coefficientwise vertical-modulus positivity (93) directly
 from modular theta sewing.}
 }                                                     \tag{97}
\]

This is strictly stronger than positivity of the modulus itself and retains
the full hierarchy discarded by the first-curvature reduction.

## Stopped label-pair expansion of the vertical generator

A critical typing restriction comes first.  The formal factor

\[
 \sum_{n\ge1}n^{-1/2-iz}
\]

does not converge on the spectral boundary, so it cannot be inserted into
(93) as a global Dirichlet series.  Work first with the faithful stopped
packet

\[
 P_N(z)=\sum_{n\le N}\chi_n(z),
 \qquad \chi_n(z)=n^{-1/2-iz}.                       \tag{98}
\]

Its vertical self-comparison is an exact finite identity:

\[
 P_N(x-it)P_N(x+it)
 =\sum_{m,n\le N}(mn)^{-1/2-ix}(n/m)^t.             \tag{99}
\]

Pairing `(m,n)` with `(n,m)` gives

\[
 \boxed{
 (mn)^{-1/2-ix}
 \bigl[(n/m)^t+(m/n)^t\bigr]
 =2(mn)^{-1/2-ix}\cosh\!\bigl(t\log(n/m)\bigr).
 }                                                     \tag{100}
\]

Hence every even vertical coefficient contributed by the label **ratio** is
nonnegative before the remaining scalar projection:

\[
 [t^{2k}]\cosh\!\bigl(t\log(n/m)\bigr)
 =\frac{\log^{2k}(n/m)}{(2k)!}\ge0.                 \tag{101}
\]

This is the all-orders extension of the quadratic arithmetic repair
`log^2(n/m)`.  Odd powers cancel solely because the faithful two-copy packet
contains both ordered label pairs.

But (100) also isolates the independent product-coordinate character

\[
 (mn)^{-ix}=e^{-ix\log(mn)}.                         \tag{102}
\]

After the real completed projection it contributes a cosine in
`x log(mn)`, whose sign is not controlled by (101).  Thus the arithmetic
two-copy coordinates separate cleanly:

\[
 \boxed{
 \log(n/m)\text{ controls vertical coefficient magnitude,}
 \qquad
 \log(mn)\text{ controls oscillatory orientation.}
 }                                                     \tag{103}
\]

This is the discrete label analogue of the source coordinates
`D=u-v` and `S=u+v` in (86).  Positivity lives on the ratio/difference fiber;
the RH difficulty lives entirely on the product/sum quotient.

No conclusion about the completed transform follows by sending `N` to
infinity in (99).  The primitive theta tail and reciprocal modular seam must
be restored before that limit.  Their task is now precise: orient the product
character (102) without disturbing the coefficientwise-positive ratio
factor (101).

## Multiplicative divisor fibers over the product quotient

Group the ordered pairs in (99) by their product `q=mn`.  The complete fiber
over `q` has vertical character

\[
 \boxed{
 A_q(t)=\sum_{mn=q}(n/m)^t
 =\sum_{d\mid q}(q/d^2)^t
 =q^t\sigma_{-2t}(q).
 }                                                     \tag{104}
\]

The involution `d mapsto q/d` proves `A_q(-t)=A_q(t)`, and

\[
 \boxed{
 [t^{2k}]A_q(t)
 =\frac1{(2k)!}\sum_{d\mid q}
 \log^{2k}(q/d^2)\ge0.
 }                                                     \tag{105}
\]

Thus each product label carries a canonical positive divisor-separation
moment tower.  This is a faithful fiber statement: finite-to-one is not being
mistaken for one-to-one; all divisor pairs over `q` are retained.

The fibers are multiplicative.  For coprime `q_1,q_2`,

\[
 A_{q_1q_2}(t)=A_{q_1}(t)A_{q_2}(t).                 \tag{106}
\]

At a prime-power component,

\[
 A_{p^a}(t)=\sum_{j=0}^{a}p^{(a-2j)t}
 =\frac{\sinh((a+1)t\log p)}{\sinh(t\log p)},       \tag{107}
\]

with the removable value `a+1` at `t=0`.  Equivalently it is the Chebyshev
polynomial `U_a(cosh(t log p))`.  Every local vertical coefficient is
therefore nonnegative.

The stopped generator can now be written as a quotient sum

\[
 \sum_q q^{-1/2-ix}A_q(t),                           \tag{108}
\]

with the cutoff incidence inherited from `(m,n)`, not replaced by an
unjustified rectangular `q` cutoff.  Formally, in a half-plane of absolute
convergence, (108) is the Dirichlet convolution identity behind

\[
 \zeta(s-t)\zeta(s+t).                               \tag{109}
\]

Equation (105) proves that no negative vertical coefficient is created
inside a divisor fiber or a prime-power local factor.  Any failure of the
completed Laguerre hierarchy must occur when the positive fibers are summed
against the oscillatory quotient character `q^{-ix}`, or in the archimedean
completion/sewing required to continue that sum.

This is the exact coefficientwise version of the paired coefficient--Betti
principle: positive multiplicative fiber data descend to an oscillatory
quotient readout, and the theorem must be proved at the faithful fiber level
before scalar projection.

## Bochner reformulation: positivity versus positive definiteness

For the even completed source, write the separation pushforward in (87) as

\[
 d\mu_{2n}(S)=w_{2n}(S)\,dS,
\]

where `w_{2n}` is even, nonnegative, and rapidly decreasing.  Equation (89)
says, up to the fixed positive normalization,

\[
 \mathcal L_n[X](x)=\widehat{w_{2n}}(x).             \tag{110}
\]

Bochner's theorem therefore gives the exact equivalence

\[
 \boxed{
 \mathcal L_n[X](x)\ge0\ \text{for every real }x
 \quad\Longleftrightarrow\quad
 w_{2n}\ \text{is positive-definite on }\mathbb R.
 }                                                     \tag{111}
\]

Here positive-definite means that for every finite set `S_1,...,S_r` and
complex coefficients `c_1,...,c_r`,

\[
 \sum_{j,k}c_j\overline{c_k}\,
 w_{2n}(S_j-S_k)\ge0.                                \tag{112}
\]

This exposes the missing property precisely.  Pointwise positivity
`w_{2n}(S)>=0` comes for free from the squared separation fiber, but it does
not imply (112).  The hostile two-atom example fails exactly at this step.

Thus the complete RH target becomes

\[
 \boxed{
 \text{every modularly completed even-separation density }w_{2n}
 \text{ is positive-definite.}
 }                                                     \tag{113}
\]

This is stronger and more testable than saying that modular sewing
"orients" the quotient.  It asks for an explicit autocorrelation/Gram
factorization

\[
 w_{2n}=g_n*\widetilde g_n                            \tag{114}
\]

or an equivalent positive representation.  If such a factorization is
source-derived uniformly in `n`, coefficientwise vertical positivity
follows immediately.  Conversely, one finite Gram matrix violating (112) is
a local exact falsifier for the proposed factorization at that order.

The distinction now reads

\[
 \boxed{
 \text{positive fibers}
 \not\Rightarrow
 \text{positive-definite quotient};
 \quad
 \text{modular sewing must supply the missing correlations.}
 }                                                     \tag{115}
\]

## Exact Krein signature of the order-`n` correlation carrier

Source evenness converts the sum convolution into an autocorrelation.  Put
`v=u-S`; then `Phi(S-u)=Phi(v)` and `D=2u-S=u+v`.  Therefore

\[
 w_{2n}(S)=
 \int_{\mathbb R}(u+v)^{2n}\Phi(u)\Phi(v)
 \big|_{v=u-S}\,du.                                  \tag{116}
\]

Expand the polynomial and introduce the moment-feature vector

\[
 H_n(u)=
 \left(
 \sqrt{\binom{2n}{0}}\Phi(u),
 \sqrt{\binom{2n}{1}}u\Phi(u),
 \ldots,
 \sqrt{\binom{2n}{2n}}u^{2n}\Phi(u)
 \right)^T.                                          \tag{117}
\]

If `J_n` reverses the `2n+1` coordinates, then

\[
 \boxed{
 w_{2n}(S)=
 \int_{\mathbb R}H_n(u)^TJ_nH_n(u-S)\,du.
 }                                                     \tag{118}
\]

The reversal involution has a fixed central coordinate and `n` exchanged
pairs.  Hence its exact signature is

\[
 \boxed{
 \operatorname{sig}(J_n)=(n+1,n).
 }                                                     \tag{119}
\]

Thus the order-`n` separation density is naturally a Krein
autocorrelation—not yet a Hilbert autocorrelation.  It contains exactly `n`
negative correlation channels.  At `n=1`, this is the rank-three carrier
with signature `(2,1)` already exposed by the kernel `(u+v)^2`.

This corrects any hope that one fixed finite-rank seam repair automatically
proves the full hierarchy.  The defect count grows with `n`.  A uniform proof
must either

1. construct `n` source-derived repairs at order `n`, or
2. embed all moment features in one completed Fock/symmetric-power object
   whose positive metric simultaneously resolves every `J_n`.

The second is the hard-to-vary option.  The matrices `J_n` are not arbitrary:
they are the degree-`2n` symmetric-power polarizations of the same rank-two
right--left carrier.  Therefore a successful bilateral Green identity at the
rank-two generating-function level could repair the entire tower at once.
Treating each generalized Laguerre inequality separately would discard that
common origin.

The strengthened falsifier is now representation-theoretic: if the completed
rank-two sewing map does not turn the symmetric-power reversal forms `J_n`
into positive correlation metrics for all `n`, then no order-by-order seam
estimate can supply a uniform RH explanation.

## Sylvester no-go: sewing cannot be only a change of frame

The preceding target requires a crucial correction.  Let `T_n` be any
invertible sewing map on the degree-`2n` feature space.  The transported form
is

\[
 T_n^TJ_nT_n.                                        \tag{120}
\]

By Sylvester's law of inertia it has the same signature `(n+1,n)` as `J_n`.
Therefore

\[
 \boxed{
 \text{no invertible rank-two sewing map, nor any of its symmetric powers,
 can convert }J_n\text{ into a positive metric.}
 }                                                     \tag{121}
\]

This closes the interpretation of modular sewing as a clever coordinate
change.  Positivity requires an operation that changes the typed object:

1. **compression** to a source-selected positive subspace;
2. **quotient/localization** by a differential-stable negative sector;
3. **dilation** into a larger Hilbert space with boundary repair channels; or
4. an exact cancellation showing that the physical feature image never
   reaches the negative directions.

Only the fourth possibility could occur without adding or removing states,
and it is a statement about the image of the theta moment map, not about the
ambient form.

This makes the fixed-sector localization question exact.  Let

\[
 E_n^- =\ker(J_n+I),\qquad \dim E_n^-=n.             \tag{122}
\]

The desired source theorem must construct a canonical subobject `K_n`
containing every physically realized negative component, stable under the
relevant scale/differential operations, such that the quotient correlation
form on

\[
 \operatorname{im}(H_n)/K_n                         \tag{123}
\]

is positive.  Merely projecting orthogonally onto `E_n^+` is circular because
that projection is defined from the desired sign form rather than from theta
incidence.

The corrected uniform theorem is consequently

\[
 \boxed{
 \text{the completed theta Carrier supplies a source-defined localization
 whose symmetric-power quotients eliminate exactly the }n
 \text{ negative reversal channels.}
 }                                                     \tag{124}
\]

If no such source-stable subobject exists already at `n=1`, the localization
route is falsified and only a genuine Hilbert dilation with modular boundary
states remains.

## Negative-channel classification: one common fold at every order

The negative eigenspace in (122) is explicit.  For `0<=j<n`, the reversal
eigenvector is

\[
 e_j-e_{2n-j}.
\]

Because the paired binomial coefficients agree, its realized source feature
is, up to a positive normalization,

\[
 \boxed{
 h_{n,j}^-(u)
 =\bigl(u^j-u^{2n-j}\bigr)\Phi(u)
 =u^j\bigl(1-u^{2(n-j)}\bigr)\Phi(u).
 }                                                     \tag{125}
\]

On the positive half-line, every one of the `n` negative channels changes
sign at exactly the same point:

\[
 \boxed{u=1.}                                        \tag{126}
\]

For `n=1`, the sole channel is

\[
 h_{1,0}^-(u)=(1-u^2)\Phi(u),                        \tag{127}
\]

while the two positive channels are represented by `(1+u^2)Phi` and
`u Phi`.

Thus the growing negative index does not correspond to `n` unrelated
geometric defects.  It is the jet tower of one common fold.  Higher orders
increase the polynomial multiplicity attached to that fold but do not create
new positive-half-line sign boundaries.

This recovers, from the complete Laguerre hierarchy, the one-fold Clark
geometry encountered earlier.  The relationship is now precise:

\[
 \boxed{
 \text{Clark one-fold defect}
 \longrightarrow
 \text{all antisymmetric reversal channels in its symmetric powers.}
 }                                                     \tag{128}
\]

The numerical location `u=1` depends on the canonical normalization of the
vertical parameter `t`; rescaling that parameter transports the common fold
accordingly.  What is invariant is that all negative channels share one fold,
not its untyped coordinate value.

This makes a uniform boundary repair conceivable despite the signature
growth: a single fold-localized boundary object could carry an infinite jet
fiber and repair all `h_{n,j}^-` simultaneously.  The next falsifier is
whether the theta scale flow preserves the ideal of features vanishing at the
fold.  If it does not, the common zero is only algebraic coincidence and does
not define a localization subobject.

## Fixed-fold localization falsified; moving divisor survives

Let

\[
 \mathcal I_c=\{h:h(c)=0\}
\]

be the evaluation ideal at a fold position `c`, and let prime transport act
by

\[
 (S_ph)(u)=p^{-1/2}h(u+\log p).                      \tag{129}
\]

Then

\[
 (S_ph)(c)=p^{-1/2}h(c+\log p),
\]

so, generically,

\[
 \boxed{S_p\mathcal I_c\not\subseteq\mathcal I_c.} \tag{130}
\]

Instead the exact covariance is

\[
 \boxed{S_p\mathcal I_c=\mathcal I_{c-\log p}}      \tag{131}
\]

on the transported function class.  Therefore the common fold in (126) does
not define a fixed differential/scale-stable subobject analogous to a fixed
Cut kernel.

This falsifies the simplest localization theorem.  The surviving object is a
**moving fold divisor** over the multiplicative label Carrier.  Its connection
records the displacement `log p`; differentiating the moving evaluation
condition is exactly the origin of the previously derived commutator repair

\[
 [M_a,S_p]=a\log p\,S_p.                             \tag{132}
\]

Thus localization and arithmetic repair are not competing mechanisms.  The
repair cocycle is the connection term required to compare the moving fold
fibers.

The corrected theorem target is consequently relative rather than absolute:

\[
 \boxed{
 \text{the bundle of fold-jet quotients }
 \{\mathcal H/\mathcal I_{c-\log n}^{(\infty)}\}_{n\ge1}
 \text{ carries a positive flat modular connection.}
 }                                                     \tag{133}
\]

Here the infinite jet notation records that the full symmetric-power tower
requires all polynomial orders at the same moving divisor.  A connection
with nontrivial negative holonomy would falsify uniform repair; a flat
connection whose seam monodromy is positive would repair the hierarchy at
the generating-function level.

## Exact affine holonomy and jet parity at the modular seam

Write `T_ell` for translation of the fold coordinate by `-ell`.  Prime
transport has `ell=log p`, and

\[
 T_{\log p}T_{\log q}=T_{\log(pq)}
 =T_{\log q}T_{\log p}.                              \tag{134}
\]

Hence every multiplicative square has trivial bulk holonomy.  The connection
one-form is the exact additive cocycle `d log n`; there is no curvature in
the prime-translation interior.

Let `R` be reciprocal reflection of oriented scale.  On fold positions it
acts by `c mapsto -c` and obeys the dihedral relation

\[
 RT_\ell R=T_{-\ell}.                                \tag{135}
\]

Therefore the affine translation--reflection connection itself is flat.  Its
only nontrivial action on the fold fiber is the reflection involution.

On the jet at the reflected fold,

\[
 j_k(h)=h^{(k)}(c),
\]

the seam acts as

\[
 \boxed{Rj_k=(-1)^k j_k.}                           \tag{136}
\]

Thus the infinite seam monodromy is the parity operator

\[
 \operatorname{diag}(1,-1,1,-1,\ldots).             \tag{137}
\]

This is not positive on any faithful linear order cone, but it is unitary for
the canonical jet Gram norm.  Consequently the earlier phrase "positive
flat modular connection" must be read quadratically:

\[
 \boxed{
 \text{the fold connection is flat and Gram-unitary, not cone-positive.}
 }                                                     \tag{138}
\]

Odd jet channels are sheet-odd and can cancel only after genuine bilateral
sewing; even jet channels survive.  This recovers the already observed
cancellation of the sheet-odd first-moment line and explains why separate
one-sided Green identities could not see it.

Flatness alone still does not prove the Laguerre hierarchy.  It says that no
additional obstruction is hidden in prime-path dependence.  The sole live
question is whether the bilateral parity projection plus its boundary
forcing converts the surviving even-jet Gram form into the positive-definite
quotient densities (113).

## Parity projection removes only half the negative tower

Because the completed source is even, the negative feature (125) has parity

\[
 h_{n,j}^-(-u)=(-1)^j h_{n,j}^-(u).                  \tag{139}
\]

Consequently bilateral reflection cancels the negative channels with odd
`j`, but preserves those with even `j`.  Among `j=0,...,n-1`, the surviving
negative count is

\[
 \boxed{
 \#\{j<n:j\text{ even}\}=\left\lceil\frac n2\right\rceil.
 }                                                     \tag{140}
\]

In particular, the sole order-one negative channel `(1-u^2)Phi` is even and
survives modular reflection.  This is consistent with the fact that the first
Laguerre inequality remains nontrivial after completing the source.

Therefore

\[
 \boxed{
 \text{bilateral parity sewing cancels the sheet-odd defects but cannot
 make the full symmetric-power carrier positive.}
 }                                                     \tag{141}
\]

The remaining repair burden grows as `ceil(n/2)`.  A uniform proof must
explain these even fold jets through the inhomogeneous boundary forcing or a
larger Hilbert dilation.  Pure reflection, even with exact flat holonomy, is
now ruled out as a complete mechanism.

## Functorial rank-one repair at the base carrier

The growing negative count nevertheless has a rank-one origin.  On the base
right--left sheet carrier, the reciprocal pairing is

\[
 J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.            \tag{142}
\]

Let

\[
 e_- =\frac1{\sqrt2}\binom{1}{-1},
 \qquad P_-=e_-e_-^T.
\]

Then the unique minimal correction that flips the negative sheet line while
leaving the positive line unchanged is

\[
 \boxed{J+2P_-=I.}                                  \tag{143}
\]

The reversal metric `J_n` is exactly the action induced by `J` on the
degree-`2n` symmetric power, in the binomial-normalized monomial basis.
Likewise, the repaired base metric `I` induces the positive identity metric
on every symmetric power.

At order `n`, the net correction is

\[
 I-J_n=2P_n^-,                                      \tag{144}
\]

where `P_n^-` is the projection onto the full `n`-dimensional negative
reversal space.  Thus all growing repair channels are functorial descendants
of the single base antisymmetric line `e_-`; they are not independent data.

The correction `2P_-` is the canonical isometric repair, because it restores
the identity metric.  More generally,

\[
 J+\lambda P_-\ge0
 \quad\Longleftrightarrow\quad \lambda\ge1.          \tag{143a}
\]

Thus positivity needs only the threshold `lambda>=1`; the value `lambda=2`
is forced only by the stronger demand that sewing restore the canonical
identity norm exactly.

This produces the smallest possible uniform theorem:

\[
 \boxed{
 \text{the modular boundary forcing realizes }\lambda P_-
 \text{ with }\lambda\ge1\text{ before symmetric-power formation.}
 }                                                     \tag{145}
\]

If (145) holds as a source-derived Green/Gram identity, positivity of every
symmetric-power metric follows automatically.  The antisymmetric line and
the threshold are forced; the actual coefficient must be computed from the
source and may not be fitted after inspecting the Laguerre inequalities.

This is the direct infinite-tower analogue of the prime-two architecture:
one source-fixed boundary channel repairs the unique base defect, and
functorial propagation repairs every higher composite channel.

The sharp falsifier is correspondingly small.  Compute the completed
rank-two seam form before taking any moments.  If its boundary contribution
has `lambda<1`, or if it introduces an additional indefinite cross term,
then the functorial repair theorem fails already at the base carrier.  The
special value `lambda=2` would establish the stronger canonical-isometry
statement.

## The repair line is the antisymmetric sine channel

For the sheet vector

\[
 v(z)=\binom{F(z)}{F(-z)},
\]

the required correction has the scalar form

\[
 \boxed{
 v^*(2P_-)v=|F(z)-F(-z)|^2.
 }                                                     \tag{146}
\]

On the real spectral axis,

\[
 F(x)-F(-x)
 =2i\int_0^\infty f(u)\sin(xu)\,du.                 \tag{147}
\]

Thus the unique base repair is the Gram energy of the antisymmetric sine
channel.  It is selected by reciprocal-sheet incidence itself, not invented
from the target inequality.

After one spectral differentiation, the same channel produces

\[
 S_1(x)^2=
 \left(\int_0^\infty u f(u)\sin(xu)\,du\right)^2,   \tag{148}
\]

which is exactly the positive square repairing `C_0C_2` in (76).  Therefore
the first coupled positivity formula is the order-one shadow of the base
metric repair (143).

This identifies the prospective uniform mechanism:

\[
 \boxed{
 \text{retain the antisymmetric sine Gram line through modular sewing,
 then form symmetric powers; do not discard it when projecting to }X.
 }                                                     \tag{149}
\]

The even completed scalar `X=F(z)+F(-z)` alone forgets this line.  Its
derivative remembers the first descendant, but higher Laguerre orders require
the whole antisymmetric jet/Fock channel.  This explains why a proof based
only on the final scalar repeatedly regenerates an expanding list of defect
terms.

The next calculation is now unambiguous: rewrite the completed rank-two
Green identity in the symmetric/antisymmetric sheet basis, compute the
operator carried by the positive norm (146), and test it against the base
threshold, with no residual mixed polarization.

## Reflection reduces the seam audit to one antisymmetric operator

The completed seam form acts both on sheet indices and on the spectral/source
feature space.  Represent it in the right--left basis by a two-by-two block
Hermitian operator `B`.  Reciprocal reflection exchanges the sheets, so a
reflection-covariant seam satisfies

\[
 JBJ=B.                                               \tag{150}
\]

Consequently

\[
 B=\begin{pmatrix}A&C\\C&A\end{pmatrix},             \tag{151}
\]

where the displayed simplification uses the real structure; more generally
the off-diagonal blocks are adjoints.  It is already diagonal in the
symmetric/antisymmetric basis:

\[
 B=P_+\otimes(A+C)+P_-\otimes(A-C).                  \tag{152}
\]

Thus bilateral reflection automatically removes every residual mixed
polarization.  If physical normalization says the seam must leave the
completed symmetric scalar unchanged, then

\[
 A+C=0,                                              \tag{153}
\]

and the entire boundary form reduces to

\[
 \boxed{B=P_-\otimes\Lambda,
 \qquad \Lambda=A-C=2A.}                            \tag{154}
\]

The full infinite-tower question has therefore reduced to one source
Hermitian operator:

\[
 \boxed{\Lambda\ge Q?}                              \tag{155}
\]

Here `Q` is the primitive source-derived Gram metric on the antisymmetric
feature space.  Writing an unqualified identity operator would silently
choose a basis-dependent normalization.  Equality gives a semidefinite
quotient with null base modes; strict operator inequality gives a positive
base metric; `Lambda=2Q` gives the canonical identity repair relative to that
Gram structure.  A scalar `lambda` occurs only if the boundary form
factorizes as `Lambda=lambda Q`.  That factorization must be proved, not
assumed.

## Absolute Green identity cannot determine `Lambda`

The existing aggregate flow has seam value

\[
 \mathscr G(0,z)=F(z),                               \tag{156}
\]

and its absolute Green identity contains the boundary term

\[
 -F(z)\overline{F(w)}.                               \tag{157}
\]

Applying the same identity to the reflected sheet and then changing basis
produces the symmetric and antisymmetric seam norms, but their coefficients
are simply the boundary presentation of the Clark/de Branges current being
studied.  No new arithmetic comparison has entered.

Therefore reading `Lambda` from the absolute identity would be circular.  It
would amount to assuming the seam repair in order to prove the seam repair.

The operator in (154) can arise only from the **relative** Green identity
between

\[
 \mathscr G(q,z)=\sum_{n\ge1}G(q+\log n,z)           \tag{158}
\]

and the faithful family of shifted primitive flows.  The relative identity
must retain their overlaps; treating the label features as orthogonal would
delete the interference term that can contribute to `Lambda`.

The exact remaining computation is now

\[
 \boxed{
 \Lambda
 =\text{antisymmetric component of the aggregate--primitive
 relative boundary form}.
 }                                                     \tag{159}
\]

It succeeds if source calculation gives `Lambda>=Q`, with all other relative
terms positive or cancelling by reflection.  It fails if `Lambda-Q` has a
negative direction or if an independent indefinite overlap survives.  The
generic one-source Green identity cannot decide either outcome.

## Canonically normalized relative-frame formulation

Let `mathcal A` denote the antisymmetric primitive feature map and define its
Gram operator

\[
 Q=\mathcal A^*\mathcal A\ge0.                      \tag{160}
\]

Null vectors of `Q` are physically invisible and must be quotiented before
normalization.  On `overline{ran Q}`, define

\[
 \widehat\Lambda
 =Q^{-1/2}\Lambda Q^{-1/2}.                          \tag{161}
\]

Then the invariant repair condition is

\[
 \boxed{
 \inf\sigma(\widehat\Lambda)\ge1.
 }                                                     \tag{162}
\]

This is a lower-frame/coercivity bound for the completed antisymmetric feature
family relative to the primitive source norm.  It is unchanged by rescaling
or changing coordinates in the feature space.

For a finite spectral packet, (162) becomes the smallest generalized
eigenvalue of the pair `(Lambda,Q)`.  Raw determinants or unnormalized
eigenvalues are not meaningful measures of the repair margin.  The sharp
finite falsifier is instead

\[
 \exists c\notin\ker Q:
 \quad \langle c,\Lambda c\rangle
 <\langle c,Qc\rangle.                              \tag{163}
\]

The infinite theorem must additionally control closure, domains, and the
possible approach of the normalized reserve to zero.  This is the same
invariant coercivity notion previously identified for the Stieltjes tower,
now derived at the base modular seam rather than imposed on its moment
shadows.

## Full label-frame lower bound is impossible

The relative-frame language must not authorize arbitrary variations of theta
labels.  To see why, consider the shifted tail features

\[
 \mathcal A_n(q,z)=\mathcal A(q+\log n,z).           \tag{164}
\]

Their adjacent displacement is

\[
 \delta_n=\log(n+1)-\log n=\log(1+1/n)\longrightarrow0.  \tag{165}
\]

For a regular nonzero tail feature, translation continuity implies that the
normalized adjacent features become arbitrarily close:

\[
 \left\|
 \frac{\mathcal A_{n+1}}{\|\mathcal A_{n+1}\|}
 -
 \frac{\mathcal A_n}{\|\mathcal A_n\|}
 \right\|\longrightarrow0.                          \tag{166}
\]

Therefore coefficient vectors supported on `(n,n+1)` with opposite signs
have nonzero diagonal reference norm but arbitrarily small synthesized norm.
No positive uniform lower-frame bound can hold on the free `ell^2` label
space.

Hence

\[
 \boxed{
 \text{the repair inequality cannot quantify over arbitrary label
 coefficients.}
 }                                                     \tag{167}
\]

Such coefficients are not physical degrees of freedom: the completed theta
source fixes their weights and incidence.  Allowing them independently would
replace the source object by a larger unfaithful carrier and manufacture
spurious near-null directions.

The operators `Q` and `Lambda` in (160)--(163) must instead act on the
source-generated **spectral/cyclic subspace**, after the label family has been
assembled with its fixed coefficients but before scalar sheet projection.
Labels remain internal coordinates for deriving the relative identity; they
are not freely variable test directions.

This distinction leaves the normalized coercivity target intact while
closing a tempting but false proof route through a Riesz bound for shifted
tails.  The next construction must specify the cyclic spectral packet first,
then pull the relative boundary form back to that packet and test the
generalized eigenvalue there.

## Exact symmetric--antisymmetric forced Dirac system

The rank-two flow can be written without guessing the relative operator.
For one completed half-source tail, put

\[
 P(q,z)=G(q,z),\qquad Q(q,z)=G(q,-z),                \tag{168a}
\]

and

\[
 S=\frac{P+Q}{\sqrt2},\qquad
 A=\frac{P-Q}{\sqrt2}.                              \tag{168b}
\]

Since

\[
 P_q=-(1/2+iz)P-f,qquad
 Q_q=-(1/2-iz)Q-f,
\]

the sheet system is

\[
 \left(\binom SA\right)_q
 =-\frac12\binom SA-iz\sigma_x\binom SA
 -\sqrt2 f(q)e_+,
 \qquad e_+=\binom10.                               \tag{168c}
\]

Remove the universal damping by defining

\[
 Y(q,z)=e^{q/2}\binom{S(q,z)}{A(q,z)},
 \qquad h(q)=\sqrt2e^{q/2}f(q)=\sqrt2\phi(q).
\]

Then

\[
 \boxed{
 Y_q=-iz\sigma_xY-h(q)e_+.
 }                                                     \tag{168d}
\]

This is a forced Dirac system with positive Euclidean bulk metric.  The
forcing lies entirely in the symmetric sheet channel; the antisymmetric
channel is generated only through spectral coupling by `sigma_x`.

For two spectral parameters, its exact Lagrange identity is

\[
\begin{aligned}
 i(\bar w-z)\int_0^\infty Y(q,w)^*Y(q,z)\,dq
 ={}&-Y(0,w)^*\sigma_xY(0,z)\\
 &+\int_0^\infty h(q)
 \bigl(A(q,z)+\overline{A(q,w)}\bigr)dq.
                                                               \tag{168e}
\end{aligned}
\]

The first term is the mixed symmetric--antisymmetric seam polarization,

\[
 -\overline{S(0,w)}A(0,z)
 -\overline{A(0,w)}S(0,z),                           \tag{168f}
\]

and the remaining obstruction is one affine forcing channel.  Thus the base
Green carrier has the exact architecture

\[
 \boxed{
 \text{positive Dirac bulk}
 -\text{mixed seam line}
 +\text{one symmetric-forcing current}.
 }                                                     \tag{168g}
\]

This corrects an overly simple reading of the antisymmetric norm repair.  The
positive sine norm is the required Schur-complement channel, but the raw
Lagrange boundary form is mixed, not already `P_- tensor Lambda`.  The
aggregate--primitive relative identity must eliminate the affine forcing and
take the Schur complement before `Lambda` is defined.

Because the forcing in (168d) is source-fixed and one-dimensional, the affine
flow can be homogenized projectively with one constant coordinate, producing
a three-state linear system.  This does **not** yet imply a conservative or
positive dilation.  The next theorem is whether that exact three-state system
admits a source-derived Green metric whose Schur complement on the
antisymmetric channel is positive and dominates the primitive seam form.

## Minimal three-state dilation has a spectral-typing obstruction

The projectively homogenized state is

\[
 Z=\begin{pmatrix}Y_+\\Y_-\\1\end{pmatrix},
 \qquad
 Z_q=M_z(q)Z,
\]

with

\[
 M_z=-izK-hE_{13},
 \qquad
 K=E_{12}+E_{21}.                                   \tag{168h}
\]

The natural Green metric for the unforced Dirac part is `K`, because

\[
 K^2=E_{11}+E_{22},                                  \tag{168i}
\]

the positive norm on the two physical sheet channels.

To cancel the affine forcing in the metric evolution, any minimal Hermitian
correction has the form

\[
 H(q)=K+b(q)(E_{23}+E_{32}).                         \tag{168j}
\]

The zero-spectral-parameter Lyapunov equation forces

\[
 b'(q)=h(q),
 \qquad
 b(q)=-\int_q^\infty h(r)\,dr                       \tag{168k}
\]

under the terminal normalization `b(infinity)=0`.

But the spectral contribution then becomes

\[
\begin{aligned}
 i\bar w K H-izH K
 ={}&i(\bar w-z)(E_{11}+E_{22})\\
 &+ib(q)\bigl(\bar w E_{13}-zE_{31}\bigr).          \tag{168l}
\end{aligned}
\]

The second line is not divisible by the de Branges denominator
`bar(w)-z` as a Hermitian positive bulk.  It is a new mixed spectral coupling
between the projective constant and the symmetric sheet channel.

Therefore

\[
 \boxed{
 \text{the minimal three-state affine homogenization cannot by itself
 provide the required conservative positive Green identity.}
 }                                                     \tag{168m}
\]

This reproduces, in the smallest matrix calculation, the earlier terminal
defect no-go.  Cancelling the forcing moves the obstruction into spectral
typing; it does not remove it.  The next admissible possibilities are a
fourth dynamical boundary state that pairs with the constant channel, or the
full aggregate--primitive relative construction whose arithmetic overlaps
supply that state nonlocally.

## Exact minimal four-state conservative dilation

The fourth state can be constructed canonically.  Let

\[
 L=E_{12}+E_{21},
 \qquad
 \mathbb J=E_{12}+E_{21}+E_{34}+E_{43},             \tag{168n}
\]

and define the four-state generator

\[
 \mathbb M_z(q)=-izL+N(q),
 \qquad
 N(q)=-h(q)E_{13}+h(q)E_{42}.                       \tag{168o}
\]

In coordinates `Z=(S,A,C,R)^T`, the system is

\[
\begin{aligned}
 S_q&=-izA-hC,\\
 A_q&=-izS,\\
 C_q&=0,\\
 R_q&=hA.                                            \tag{168p}
\end{aligned}
\]

Taking `C=1` recovers the forced physical Dirac system exactly.  With terminal
condition `R(infinity)=0`, the fourth state is the nonlocal accumulator

\[
 R(q,z)=-\int_q^\infty h(r)A(r,z)\,dr.              \tag{168q}
\]

The construction is conservative in the constant Krein metric `mathbb J`:

\[
 \boxed{N^*\mathbb J+\mathbb JN=0.}                \tag{168r}
\]

Moreover,

\[
 L\mathbb J=\mathbb JL=E_{11}+E_{22}.              \tag{168s}
\]

Therefore the exact Lagrange identity has correctly typed positive spectral
bulk:

\[
 \boxed{
 \frac d{dq}\bigl(Z(q,w)^*\mathbb JZ(q,z)\bigr)
 =i(\bar w-z)
 \bigl(\overline{S(q,w)}S(q,z)
 +\overline{A(q,w)}A(q,z)\bigr).
 }                                                     \tag{168t}
\]

Because `S,A` decay, `C=1`, and `R(infinity)=0`, the terminal Krein boundary
pairing vanishes.  Integration gives

\[
 \boxed{
 i(\bar w-z)\int_0^\infty
 \bigl(\overline S_wS_z+\overline A_wA_z\bigr)dq
 =-Z(0,w)^*\mathbb JZ(0,z).
 }                                                     \tag{168u}
\]

Expanding the boundary form reproduces exactly the mixed sheet seam plus the
affine forcing accumulator:

\[
 Z_w^*\mathbb JZ_z
 =\overline S_wA_z+\overline A_wS_z
 +\overline C_wR_z+\overline R_wC_z.                \tag{168v}
\]

Thus four states are sufficient, and the fourth is not arbitrary: it is the
integrated antisymmetric response to the symmetric source forcing.  This is
the continuous counterpart of the missing relative arithmetic boundary
channel.

Scope remains decisive.  Identity (168u) is valid for generic decaying
sources and therefore does not prove RH.  It solves the local spectral-typing
problem and identifies the exact boundary form whose completed arithmetic
sewing must make positive.  The remaining theorem is no longer construction
of an operator; it is positivity of the source-specific four-state boundary
Krein form after aggregate--primitive comparison.

## Exact aggregate--primitive accumulator difference

Work first with a stopped finite label set `mathcal N`.  Let `h_n(q)` be the
positive forcing attached to label `n`, and let `(S_n,A_n)` be the physical
Dirac response to `h_n`.  Linearity gives

\[
 h_{\mathcal N}=\sum_{n\in\mathcal N}h_n,
 \qquad
 S_{\mathcal N}=\sum_nS_n,
 \qquad
 A_{\mathcal N}=\sum_nA_n.                           \tag{168w}
\]

The fourth state is quadratic in the forcing and response.  At the seam,

\[
 R_{\mathcal N}(0,z)
 =-\int_0^\infty h_{\mathcal N}(q)
 A_{\mathcal N}(q,z)dq
 =-\sum_{m,n\in\mathcal N}
 \int_0^\infty h_m(q)A_n(q,z)dq.                    \tag{168x}
\]

Subtract the sum of the individual primitive accumulators.  The diagonal
label terms cancel exactly, leaving

\[
 \boxed{
 R_{\rm rel}^{\mathcal N}(z)
 =-\sum_{\substack{m,n\in\mathcal N\\m\ne n}}
 \int_0^\infty h_m(q)A_n(q,z)dq.
 }                                                     \tag{168y}
\]

This is the previously abstract aggregate--primitive interference channel.
No orthogonality assumption and no infinite rearrangement has entered.

The antisymmetric response has an explicit Volterra formula.  From

\[
 A_n''+z^2A_n=iz h_n
\]

with terminal tail conditions,

\[
 \boxed{
 A_n(q,z)=i\int_q^\infty
 \sin\!\bigl(z(r-q)\bigr)h_n(r)dr.
 }                                                     \tag{168z}
\]

Therefore

\[
 \boxed{
 R_{\rm rel}^{\mathcal N}(z)
 =-i\sum_{m\ne n}
 \int_{0<q<r<\infty}
 h_m(q)h_n(r)
 \sin\!\bigl(z(r-q)\bigr)dqdr.
 }                                                     \tag{168aa}
\]

Pairing `(m,n)` with `(n,m)` shows that each unordered pair carries the
positive source amplitude

\[
 h_m(q)h_n(r)+h_n(q)h_m(r),                          \tag{168ab}
\]

multiplied by the sole oscillatory factor `sin(z(r-q))`.

Thus the relative operator `Lambda` is no longer unnamed: it is the
polarized boundary kernel induced by the Volterra interference current
(168aa), together with the mixed seam term fixed by (168v).  Its positivity
is not automatic—the sine kernel can change sign—but every possible failure
is now localized to a faithful ordered-label, ordered-scale integral.

The next source theorem must use modular reflection or prime-scale recursion
to orient this Volterra sine transform.  A two-label concentrated forcing is
the smallest analytic falsifier; if it produces the wrong boundary sign even
after the exact reflected seam is included, then cross-label interference
alone cannot supply `Lambda>=Q`.

## Two-label test: the accumulator alone is not positive

For real `x`, the forcings `h_n` are real and (168aa) shows that
`R_rel(x)` is purely imaginary.  Hence

\[
 R_{\rm rel}(x)+\overline{R_{\rm rel}(x)}=0.         \tag{168ac}
\]

This is required rather than helpful: on the real spectral diagonal the
Green denominator also vanishes.  The relevant kernel is the removable
divided difference, not the undivided boundary numerator.

Take two positive point forcings at `q_1<q_2`, with weights `alpha,beta` and
`Delta=q_2-q_1`.  Then

\[
 R_{\rm rel}(z)=-i\alpha\beta\sin(z\Delta).          \tag{168ad}
\]

The real-diagonal divided-difference limit of its boundary polarization is,
up to the fixed overall Green-sign convention,

\[
 \alpha\beta\Delta\cos(x\Delta).                    \tag{168ae}
\]

It changes sign.  Smooth narrow positive forcings retain the negative lobe.
Therefore

\[
 \boxed{
 \text{the relative accumulator current alone is not a positive kernel.}
 }                                                     \tag{168af}
\]

The operator `Lambda` must denote the Schur complement of the **complete**
boundary form: mixed symmetric--antisymmetric seam, accumulator, and the
positive Dirac bulk pulled back through the aggregate--primitive comparison.
Identifying `Lambda` with (168aa) alone would be another false shortcut.

The hostile example does not falsify the completed theta mechanism, because
it lacks reciprocal modular sewing and the exact theta forcing.  It does
falsify every generic-source claim that four-state conservativity by itself
implies the required de Branges positivity.

## Meaning gate: the physical Clark channel is differentiated

The universal positivity in (168u) proves that its boundary quotient cannot
already be the RH kernel.  At the seam,

\[
 S(0,z)=\frac{F(z)+F(-z)}{\sqrt2}
 =\frac{X(z)}{\sqrt2},                              \tag{168ag}
\]

but

\[
 A(0,z)=\frac{F(z)-F(-z)}{\sqrt2}                   \tag{168ah}
\]

is the undifferentiated sine channel.  The physical Clark/de Branges partner
is instead

\[
 \frac{X'(z)}{\sqrt2}
 =\partial_zS(0,z)
 =\frac{F'(z)-F'(-z)}{\sqrt2}.                      \tag{168ai}
\]

Therefore identifying `A` with `X'` would confuse a source sheet coordinate
with its spectral jet.  The four-state construction solves the carrier
typing only before the Clark differential.

Differentiate the homogeneous four-state equation

\[
 Z_q=(-izL+N)Z
\]

with respect to `z`.  The jet `dot Z=partial_z Z` obeys

\[
 (\dot Z)_q=(-izL+N)\dot Z-iLZ.                     \tag{168aj}
\]

This is a Jordan extension forced by the original carrier.  The natural
spectral shear

\[
 W=\dot Z+iqLZ                                      \tag{168ak}
\]

removes the explicit `-iLZ` term, but because the source forcing does not
commute with spectral sheet exchange, it leaves

\[
 \boxed{
 W_q=(-izL+N)W+iq[L,N]Z,
 }                                                     \tag{168al}
\]

with

\[
 \boxed{
 [L,N]=-h(q)(E_{23}+E_{41}).
 }                                                     \tag{168am}
\]

The residual is source-fixed, proportional to the oriented scale `q`, and
couples the physical carrier to both boundary states.  It is the four-state
version of the earlier Clark arithmetic shear: after sampling at
`q=log n`, its coefficient becomes `log n`.

Thus the logarithmic repair has now been derived inside the minimal
conservative dilation rather than appended afterward.  The corrected live
object is the eight-state carrier `(Z,W)`, or an equivalent rank-four Jordan
module, with source forcing (168am).

The next theorem is whether the all-label sum of these `q h(q)` boundary
currents supplies the positive Schur complement required for the
differentiated physical seam `(X,X')`.  A proof at the undifferentiated
four-state level cannot establish RH, because that positivity is universal.

## Relative Jordan shear produces the logarithmic repair exactly

For label `n`, the native tail coordinate is

\[
 r_n=q+\log n.                                      \tag{168an}
\]

Its natural differentiated shear is therefore

\[
 W_n=\dot Z_n+i(q+\log n)LZ_n,                      \tag{168ao}
\]

whereas the aggregate carrier uses the common coordinate

\[
 W_{\rm agg}=\dot Z_{\rm agg}+iqLZ_{\rm agg}.       \tag{168ap}
\]

Since `Z_agg=sum_n Z_n` on the physical response coordinates, subtraction
gives the exact relative shear

\[
 \boxed{
 W_{\rm agg}-\sum_nW_n
 =-i\sum_n(\log n)LZ_n.
 }                                                     \tag{168aq}
\]

Likewise, the source term in the native primitive Jordan equation contains
`(q+log n)h_n`, while the aggregate equation contains `q sum_n h_n`.  Their
difference is

\[
 \boxed{
 \sum_n(q+\log n)h_n-q\sum_nh_n
 =\sum_n(\log n)h_n\ge0.
 }                                                     \tag{168ar}
\]

Thus the logarithmic arithmetic repair is exactly the mismatch between local
label coordinates and the global aggregate coordinate.  It is simultaneously

* the commutator `[M_a,S_n]`;
* displacement of the moving fold divisor;
* the relative Jordan shear current in the conservative dilation.

These are three coordinate descriptions of one source invariant, not three
independent positivity effects.

The repair current is pointwise nonnegative before its matrix coupling, but
that alone does not prove that its Schur complement is positive.  The final
base theorem is now sharply formulated: insert (168ar) into the relative
eight-state Green identity and determine whether its boundary contribution
dominates the differentiated antisymmetric seam Gram form.  No further
source term remains unclassified.

## Global null-mode cancellation and the theta remainder curvature

The saturation at `x=0` is the local shadow of an exact global cancellation.
For

\[
 K_0(u)=\frac12e^{-|u|/2},
\]

the Fourier transform is

\[
 \widehat K_0(x)=\frac{1/2}{x^2+1/4}.               \tag{168dv}
\]

Hence the completion factor annihilates its pole and leaves a constant:

\[
 \boxed{
 \left(x^2+\frac14\right)\widehat K_0(x)=\frac12
 \quad\text{for every real }x.
 }                                                     \tag{168dw}
\]

Write the even theta correction as `R_theta` and set

\[
 H(z)=\left(z^2+\frac14\right)\widehat R_\theta(z).
                                                               \tag{168dx}
\]

Since `K=K_0-R_theta`, the completed transform is exactly

\[
 \boxed{X(z)=\frac12-H(z).}                         \tag{168dy}
\]

Therefore its first Laguerre curvature is

\[
 \boxed{
 \mathcal L_1[X](x)
 =(H'(x))^2+\left(\frac12-H(x)\right)H''(x).
 }                                                     \tag{168dz}
\]

The archimedean null mode contributes zero curvature everywhere.  It supplies
the globally constant carrier, while every nontrivial sign decision belongs
to the completed theta remainder `H`.

This explains why the central threshold was exactly `8` and why the
Schwarzian numerator earlier became quadratic in one logarithm: after exact
pole cancellation, only one remainder function and its first two derivatives
survive.

At the origin, evenness gives `H'(0)=0`, and the theorem (168du) says

\[
 \left(\frac12-H(0)\right)H''(0)>0.                 \tag{168ea}
\]

Away from the origin the positive square `(H')^2` becomes the canonical
coupled repair of the potentially negative product `(1/2-H)H''`.  The global
first-order theorem is thus the scalar inequality

\[
 \boxed{
 (H')^2+\left(\frac12-H\right)H''\ge0
 \quad(x\in\mathbb R).
 }                                                     \tag{168eb}
\]

This remains only the first Laguerre shadow, not RH.  Its value is that the
archimedean and arithmetic roles are now separated without approximation:
the null mode fixes the constant baseline, the full theta remainder creates
all curvature, and prime-power decompositions are coordinate resolutions of
that same remainder.

## Complete hierarchy after null-mode cancellation

The same reduction holds at every vertical order.  From

\[
 X(z-it)X(z+it)
 =\left(\frac12-H(z-it)\right)
  \left(\frac12-H(z+it)\right),                     \tag{168ec}
\]

the constant square contributes only at order zero.  For every `n>=1`, the
two constant--remainder cross terms contribute

\[
 -\frac{(-1)^n}{(2n)!}H^{(2n)}(z).
\]

Therefore

\[
 \boxed{
 \mathcal L_n[X](z)
 =\mathcal L_n[H](z)
 -\frac{(-1)^n}{(2n)!}H^{(2n)}(z),
 \qquad n\ge1.
 }                                                     \tag{168ed}
\]

For `n=1`, this is

\[
 \mathcal L_1[H]+\frac12H''
 =(H')^2+\left(\frac12-H\right)H'',
\]

recovering (168dz).

Thus the complete RH hierarchy has only two typed pieces at each order:

\[
 \boxed{
 \text{theta-remainder self-comparison}
 +\text{one constant--remainder even-jet channel}.
 }                                                     \tag{168ee}
\]

The archimedean null mode generates no higher curvature tower after pole
cancellation.  It survives solely as the constant `1/2` that polarizes one
even derivative of `H`.  This is the all-orders version of the finite-rank
seam principle.

The sharpened source theorem is now

\[
 \boxed{
 \mathcal L_n[H](x)
 \ge\frac{(-1)^n}{(2n)!}H^{(2n)}(x)
 \quad\text{for all }n\ge1, x\in\mathbb R.
 }                                                     \tag{168ef}
\]

Unlike the earlier growing Krein presentation, (168ef) has one declared
interference channel at every order and a single common generating function
`H`.  Any uniform modular Green proof should act on this remainder carrier
before expanding in `n`.

## Meaning audit: the constant carrier is the reflected arithmetic seam

The affine identity (168dy) does not by itself reduce the RH problem.  Source
typing shows both why the constant is canonical and why its apparent residual
channel must not be counted as an independent repair mechanism.

Extend `R_theta` evenly from the positive scale chamber.  It is smooth away
from the modular seam, while

\[
 K=K_0-R_\theta,
 \qquad K_0(u)=\frac12e^{-|u|/2},
\]

is smooth and even at the origin.  Hence `K'(0+)=0`, whereas
`K_0'(0+)=-1/4`, so

\[
 \boxed{R_\theta'(0+)=-\frac14.}                  \tag{168eg}
\]

For an even piecewise-smooth function, distributional differentiation gives

\[
 D^2R_\theta=(R_\theta'')_{\rm cl}
              +2R_\theta'(0+)\delta_0.
\]

Away from zero, `Phi=(1/4-D^2)K` and
`(1/4-D^2)K_0=0`.  Combining this with (168eg) yields the global
distributional identity

\[
 \boxed{
 \left(\frac14-D^2\right)R_\theta
 =\frac12\delta_0-\Phi.
 }                                                    \tag{168eh}
\]

Fourier transformation of (168eh) is exactly `H=1/2-X`.  Thus the constant
carrier is not extra physical data: it is the boundary current created when
the positive-chamber arithmetic remainder is sewn to its reflected chamber.
The proposed interpretation

\[
 \text{carrier interference}
 =\text{boundary of arithmetic self-comparison}
\]

is therefore exact at the source level.

There is a further cancellation hidden by the affine presentation.  Put

\[
 \eta:=\frac12\delta_0-\Phi,
 \qquad H=\widehat\eta.
\]

For every `n>=1`, the source formula gives

\[
 \mathcal L_n[H](x)
 =\frac1{(2n)!}\iint
 (u-v)^{2n}e^{ix(u+v)}\,d\eta(u)d\eta(v).          \tag{168ei}
\]

Expanding `eta=(1/2)delta_0-Phi`, its delta--delta term vanishes and its two
delta--bulk edges contribute

\[
 -\frac1{(2n)!}\int u^{2n}e^{ixu}\Phi(u)du.        \tag{168ej}
\]

Meanwhile

\[
 -\frac{(-1)^n}{(2n)!}H^{(2n)}(x)
 =-\frac1{(2n)!}\int u^{2n}e^{ixu}d\eta(u)
 =\frac1{(2n)!}\int u^{2n}e^{ixu}\Phi(u)du.        \tag{168ek}
\]

Thus (168ej) and (168ek) cancel identically, leaving

\[
 \boxed{
 \mathcal L_n[H](x)
 -\frac{(-1)^n}{(2n)!}H^{(2n)}(x)
 =\frac1{(2n)!}\iint
 (u-v)^{2n}\Phi(u)\Phi(v)e^{ix(u+v)}dudv.
 }                                                    \tag{168el}
\]

This supersedes the interpretation following (168ee): after faithful source
typing, there are not two independent residual mechanisms.  The even-jet
channel removes precisely the seam--bulk edges already present in the
remainder self-comparison.  What survives is the original positive
two-copy separation measure, with exactly one unresolved obstruction: the
orientation of its oscillatory sum-coordinate transform.

Consequently an order-by-order Schur-complement proof in the affine `H`
coordinate would merely re-prove this cancellation.  The next genuine
reduction must retain the theta label pairs and explain how modular sewing
orients

\[
 \sum_{m,n}\iint
 (u-v)^{2k}\Phi_m(u)\Phi_n(v)e^{ix(u+v)}dudv
\]

uniformly in `k` and `x`.  The smallest completed modular orbit with a
negative oriented coefficient is the local falsifier.

## Generating refinement of the earlier Bochner reduction

Identity (168el) returns exactly to the positive-definiteness target
(110)--(115) and its Krein obstruction (116)--(128); it does not constitute
a second route around them.  It does, however, package every fixed-order
Bochner question into one curve.  Set

\[
 W_t(S):=\frac12\int_{\mathbb R}
 \cosh(tD)
 \Phi\!\left(\frac{S+D}{2}\right)
 \Phi\!\left(\frac{S-D}{2}\right)dD.              \tag{168em}
\]

Then

\[
 W_t(S)=\sum_{n\ge0}\frac{t^{2n}}{(2n)!}w_{2n}(S),
 \qquad
 \widehat W_t(x)=|X(x+it)|^2.                      \tag{168en}
\]

For each fixed real `t`, `W_t` is automatically positive definite because
its Fourier transform is nonnegative.  The missing property is strictly
stronger: `t -> W_t` must be coefficientwise positive in the Bochner cone at
`t=0`.  Equivalently, the vertical self-comparison must be absolutely
monotone as a curve in that cone.  This is the precise single-operation form
of the complete Laguerre hierarchy.

## Product--ratio label reduction and the divisor character

The tilted two-copy source reveals a further exact combinatorial separation.
On the positive chamber use

\[
 \phi_m(u)=m^{-1/2}\phi_1(u+\log m),
 \qquad
 \phi_n(v)=n^{-1/2}\phi_1(v+\log n),
\]

and put

\[
 r=u+\log m,qquad s=v+\log n.
\]

The Fourier phase and vertical tilt then split as

\[
 e^{ix(u+v)}e^{t(u-v)}
 =(mn)^{-ix}\left(\frac nm\right)^t
 e^{ix(r+s)}e^{t(r-s)}.                             \tag{168eo}
\]

Thus the faithful arithmetic coordinates of an ordered label pair are

\[
 \boxed{
 q=mn\quad\text{for the oscillatory phase},
 \qquad
 n/m\quad\text{for the vertical jet}.
 }                                                    \tag{168ep}
\]

Fix `q` and sum over its complete ordered-factorization fiber `mn=q`.  On
any region common to all corresponding shifted rectangles, the label factor
is

\[
 \boxed{
 A_q(t):=\sum_{m\mid q}\left(\frac{q}{m^2}\right)^t.
 }                                                    \tag{168eq}
\]

The involution `m -> q/m` sends the exponent to its negative.  Consequently
`A_q` is even and

\[
 [t^{2k}]A_q(t)
 =\frac1{(2k)!}\sum_{m\mid q}
 \log^{2k}\!\left(\frac q{m^2}\right)\ge0,         \tag{168er}
\]

while every odd coefficient vanishes.  This is the all-orders version of the
quadratic `log^2(n/m)` repair in (40).

The character is multiplicative.  If `q=prod_p p^{a_p}`, then

\[
 \boxed{
 A_q(t)=\prod_{p^{a_p}\parallel q}
 \sum_{j=0}^{a_p}e^{(a_p-2j)t\log p}
 =\prod_{p^{a_p}\parallel q}
 \frac{\sinh((a_p+1)t\log p)}{\sinh(t\log p)}.
 }                                                    \tag{168es}
\]

Accordingly its Dirichlet generating series has the exact factorization

\[
 \boxed{
 \sum_{q\ge1}\frac{A_q(t)}{q^\sigma}
 =\zeta(\sigma+t)\zeta(\sigma-t)
 }                                                    \tag{168et}
\]

in the half-plane of absolute convergence.  No zero information enters this
identity: it is simply the product--ratio decomposition of the ordered pair
lattice.

This is not yet a positivity proof.  Two obstructions remain visibly typed.
First, every product fiber still carries the rotating scalar `q^{-ix}`;
positive Taylor coefficients in `t` do not orient the Fourier sum over `q`.
Second, the transformed pair `(m,n)` occupies

\[
 r\ge\log m,qquad s\ge\log n,                     \tag{168eu}
\]

so different divisors of the same `q` do not initially share a common
rectangle.  On the deep common chamber `r,s>=log q`, the divisor character
(168eq) is exact without residuals.  Everything outside that chamber is a
finite union of divisor-indexed boundary strips.

Hence the pair-label combinatorics has reduced to

\[
 \boxed{
 \text{multiplicative divisor-character bulk}
 +\text{finite factorization-fiber seams}.
 }                                                    \tag{168ev}
\]

The bulk already has coefficientwise-positive vertical characters.  The
next nontrivial question is whether reciprocal modular sewing turns the
boundary-strip complex into an exact positive-definite correction after the
remaining product phase `q^{-ix}` is included.  The smallest product `q` and
order `k` whose fully sewn strip Gram form has a negative direction is the
sharp combinatorial falsifier.  Unlike a free finite-label scout, this test
is forced by the canonical factorization fiber and its incidence boundary.

## Primitive curvature orients every adjacent divisor transport

The factorization-fiber seams are not governed by an unknown density.  The
primitive theta label on the positive chamber is

\[
 \phi_1(u)=2\pi e^{5u/2}
 (2\pi e^{2u}-3)e^{-\pi e^{2u}},
 \qquad u\ge0.                                      \tag{168ew}
\]

It is strictly positive because `2pi e^{2u}>3`.  With `y=e^{2u}`, direct
differentiation gives

\[
 \boxed{
 (\log\phi_1)''(u)
 =-4\pi y-\frac{24\pi y}{(2\pi y-3)^2}
 <-4\pi.
 }                                                    \tag{168ex}
\]

Thus the primitive label is uniformly strongly log-concave.  This fact is
not being used as a black-box certificate for the already-summed theta
source.  It supplies a canonical orientation for the adjacent edges of the
divisor lattice before label compression.

Indeed, fix a product `q`, a transformed sum `T=r+s`, and an adjacent prime
move transferring `p` from the second label to the first.  Put `L=log p`.
On the common part of the two rectangles, the density ratio is

\[
 \rho_{p,T}(r)
 =\frac{\phi_1(r+L)\phi_1(T-r-L)}
        {\phi_1(r)\phi_1(T-r)}.                    \tag{168ey}
\]

Writing `ell=log(phi_1)`, its logarithmic derivative is

\[
 \frac d{dr}\log\rho_{p,T}(r)
 =\ell'(r+L)-\ell'(r)
  -\ell'(T-r-L)+\ell'(T-r)<0,                      \tag{168ez}
\]

because `ell'` is strictly decreasing.  Hence

\[
 \boxed{
 \rho_{p,T}\text{ is strictly decreasing on every admissible edge chart.}
 }                                                    \tag{168fa}
\]

Every adjacent divisor transport therefore has the monotone-likelihood-ratio
property requested by the earlier band-pairing programme.  Moreover, for

\[
 q=\prod_p p^{a_p},
\]

the ordered-factorization fiber is the finite box

\[
 \mathcal B_q=\prod_{p^{a_p}\parallel q}\{0,1,\ldots,a_p\}. \tag{168fb}
\]

Prime moves are translations in distinct box coordinates and commute.  The
geometric transport has trivial holonomy around every square; any remaining
failure of global orientation must therefore come from the boundary-strip
readout or from incompatibility of the MLR orders with the oscillatory
sum-coordinate kernel, not from incoherence of the divisor incidence graph.

This is the first source-derived adjacent-transport theorem in the current
RH lane:

\[
 \boxed{
 \text{fixed-product divisor fibers carry a coherent cubical transport,}
 \quad
 \text{and every prime edge is strictly MLR-oriented.}
 }                                                    \tag{168fc}
\]

Its scope is deliberately limited.  MLR orientation controls single-crossing
comparisons of neighboring label densities; it does not by itself imply that
their cosine transforms are nonnegative.  The next exact gate is whether
reflection-paired paths across `B_q` make each even separation moment a
positive-definite boundary-corrected correlation.  Failure must appear as a
specific box face whose MLR-oriented strip form retains a negative Gram
direction.

## First higher-coherence gate: the infinitesimal TP3 minor also passes

Strict MLR is only an order-two sign-regularity statement.  To determine
whether the primitive transport may extend beyond pairwise ordering, test the
first local order-three invariant.  For a positive function `f=e^ell`, the
Wronskian of its first three derivative columns is

\[
 \det
 \begin{pmatrix}
 f&f'&f''\\
 f'&f''&f'''\\
 f''&f'''&f''''
 \end{pmatrix}
 =f^3\left(2b^3+bd-c^2\right),                    \tag{168fd}
\]

where

\[
 b=\ell'',\qquad c=\ell''',\qquad d=\ell''''.
\]

This controls the leading confluent `3 by 3` translation minor.  The sign
required by the standard Gaussian/strictly-totally-positive orientation is
negative.

For `f=phi_1`, put

\[
 x=2\pi e^{2u},\qquad z=x-3.
\]

Here `x>6` and `z>3`.  Exact differentiation of (168ew) gives

\[
\begin{aligned}
 b&=-2x\left(1+\frac6{z^2}\right),\\
 c&=-4x\left(1-\frac6{z^2}-\frac{36}{z^3}\right),\\
 d&=-8x\left(1+\frac6{z^2}
 +\frac{108}{z^3}+\frac{324}{z^4}\right).
\end{aligned}                                      \tag{168fe}
\]

Writing the three parenthesized factors as `B,C,D`, respectively, one finds

\[
 2b^3+bd-c^2
 =-16x^2\left[xB^3-(BD-C^2)\right],               \tag{168ff}
\]

and the bracket reduces to

\[
 xB^3-(BD-C^2)
 =z+3+\frac{18}{z}+\frac{30}{z^2}-\frac{72}{z^3}.
                                                               \tag{168fg}
\]

Multiplying by `z^3`, its numerator is

\[
 z^4+3z^3+18z^2+30z-72>0\qquad(z>3),              \tag{168fh}
\]

since it is already positive at `z=3` and has positive derivative there and
beyond.  Therefore

\[
 \boxed{
 2(\ell'')^3+\ell''\ell''''-(\ell''')^2<0
 \quad\text{for every }u\ge0.
 }                                                    \tag{168fi}
\]

Thus the primitive theta translation kernel passes both the TP2/MLR gate and
the first confluent TP3 gate everywhere on the physical chamber.  This is
strictly stronger evidence than log-concavity, but its demonstrated strength
is local: it does not prove that every separated `3 by 3` minor is oriented,
much less that `phi_1` is a Polya-frequency function of infinite order.

The sharpened conjecture is now finitely falsifiable without spectral
scouting:

\[
 \boxed{
 K(r,s)=\phi_1(r-s)
 \text{ is sign-regular of all orders on its admitted translation domain.}
 }                                                    \tag{168fj}
\]

The next hostile test is symbolic: derive a closed form for a separated
`3 by 3` minor, factor out its forced positive exponentials, and determine
whether the residual polynomial/exponential expression keeps the confluent
sign.  One exact negative instance would kill the total-positivity route
while preserving the proven cubical MLR theorem.

## Separated-minor attack: global TP3 holds on the admitted chamber

The proposed hostile test can be completed symbolically.  Remove the
positive row and column factors from (168ew) by putting

\[
 A=\pi e^{2r},\qquad Y=e^{-2s},qquad
 k(AY)=(2AY-3)e^{-AY}.                              \tag{168fk}
\]

The physical translation chamber `r-s>=0` is exactly

\[
 AY=\pi e^{2(r-s)}\ge\pi>3.                        \tag{168fl}
\]

For three fixed positive values `Y_j`, the first three derivative rows of
`k(AY_j)` with respect to `A`, after removing the positive exponentials, are

\[
 \begin{pmatrix}
 2AY_j-3\\
 -Y_j(2AY_j-5)\\
 Y_j^2(2AY_j-7)
 \end{pmatrix}.                                    \tag{168fm}
\]

Let `V(Y)=prod_{i<j}(Y_j-Y_i)`.  Expansion in the monomial degrees
`(0,1,2,3)` gives the exact Wronskian factorization

\[
 \boxed{
 \mathcal W_3
 =e^{-A(Y_1+Y_2+Y_3)}V(Y)
 \left(105-30e_1+12e_2-8e_3\right),
 }                                                    \tag{168fn}
\]

where `e_j` is the degree-`j` elementary symmetric polynomial in

\[
 t_i=AY_i.
\]

On the admitted chamber every `t_i>=pi>3`.  The residual polynomial

\[
 P_3(t_1,t_2,t_3)=105-30e_1+12e_2-8e_3             \tag{168fo}
\]

is strictly decreasing in each variable there, because

\[
 \frac{\partial P_3}{\partial t_1}
 =-30+12(t_2+t_3)-8t_2t_3<0                        \tag{168fp}
\]

for `t_2,t_3>=3`, and cyclically.  At the lower comparison corner,

\[
 P_3(3,3,3)=-57<0.                                 \tag{168fq}
\]

Hence `P_3<0` throughout the full physical chamber.

The order-two Wronskian has the parallel exact factorization

\[
 \mathcal W_2
 =e^{-A(Y_1+Y_2)}(Y_2-Y_1)
 \left[-15+6(t_1+t_2)-4t_1t_2\right],             \tag{168fr}
\]

and its bracket is also strictly negative for `t_i>=3`.  Together with
`k(t)>0`, the first three Wronskians never vanish and have the canonical
sign-regular orientation.  The extended-Chebyshev determinant criterion
therefore transports the confluent signs to every separated set of row
coordinates.

Finally, increasing physical column coordinates `s_j` makes
`Y_j=e^{-2s_j}` decrease.  Reversing the column order contributes precisely
the alternating sign of the `A,Y` kernel.  Restoring the discarded positive
row/column factors yields

\[
 \boxed{
 \det\bigl[\phi_1(r_i-s_j)\bigr]_{i,j=1}^m>0,
 \qquad m=1,2,3,
 }                                                    \tag{168fs}
\]

whenever `r_1<...<r_m`, `s_1<...<s_m`, and every `r_i-s_j>=0`.

Thus the primitive positive-chamber translation kernel is globally strictly
totally positive of order three on its admitted domain.  The separated test
does not merely fail to falsify the route; it proves a new finite-order
theorem.  No claim of TP-infinity follows.  The next discriminator is order
four, where the residual symmetric polynomial is no longer fixed by MLR and
one cubic Wronskian.

## Exact order-seven obstruction to primitive total positivity

The order-four suggestion above can be replaced by a complete local
classification.  The derivatives of the reduced kernel in (168fk) satisfy

\[
 \frac{d^j}{dt^j}\bigl[(2t-3)e^{-t}\bigr]
 =(-1)^j\bigl(2t-(2j+3)\bigr)e^{-t}.               \tag{168ft}
\]

In the order-`m` Wronskian, row `j` therefore contains only the adjacent
monomial degrees `j` and `j+1`.  A nonzero alternant can switch from the
lower to the upper degree only once.  Factoring the Vandermonde gives the
general residual

\[
 \boxed{
 P_m(t_1,\ldots,t_m)
 =(-1)^{m(m+1)/2}
 \sum_{j=0}^m(-2)^j(2(m-j)+1)!!\,e_j(t_1,\ldots,t_m).
 }                                                    \tag{168fu}
\]

Let `Z` be a standard real Gaussian and `Y=Z^2`.  Since

\[
 \mathbb E[Y^{k+1}]=(2k+1)!!,
\]

the sum in (168fu) is exactly

\[
 \boxed{
 R_m(t_1,\ldots,t_m)
 :=\mathbb E\!\left[Y\prod_{i=1}^m(Y-2t_i)\right].
 }                                                    \tag{168fv}
\]

For the translation kernel to retain its canonical sign at order `m`, the
diagonal seam limit requires

\[
 \operatorname{sgn}R_m(t,\ldots,t)=(-1)^m,
 \qquad t\ge\pi.                                    \tag{168fw}
\]

At the rational comparison point `t=3`, exact Gaussian moments give

\[
\begin{array}{c|rrrrrrrr}
 m&0&1&2&3&4&5&6&7\\ \hline
 R_m(3,\ldots,3)
 &1&-3&15&-57&369&-891&15903&78975.
\end{array}                                         \tag{168fx}
\]

Thus the required alternating sign first fails at `m=7`.  The failure
persists at the physical seam `t=pi`.  Along the diagonal write

\[
 a_m(t)=\mathbb E[Y(Y-2t)^m].
\]

Then

\[
 a_m'(t)=-2m a_{m-1}(t).                            \tag{168fy}
\]

Starting from `a_1(t)=3-2t<0`, this recurrence and the signs in (168fx)
show successively on `3<=t<=22/7` that

\[
 a_2>0, a_3<0, a_4>0, a_5<0, a_6>0,
\]

so `a_7` is strictly decreasing there.  Direct exact evaluation at the upper
rational endpoint gives

\[
 \boxed{
 7^7a_7(22/7)=37\,328\,273\,323>0.
 }                                                    \tag{168fz}
\]

Because `3<pi<22/7`, it follows that

\[
 \boxed{a_7(\pi)>a_7(22/7)>0,}                     \tag{168ga}
\]

opposite to the required odd-order sign.  Continuity turns this wrong
confluent sign into a wrong genuinely separated `7 by 7` minor arbitrarily
near the modular boundary.  After restoring the physical column ordering,
that minor is negative.

Therefore

\[
 \boxed{
 \phi_1(r-s)\text{ is not totally positive of infinite order;
 the first seam-local Wronskian obstruction occurs at order }7.
 }                                                    \tag{168gb}
\]

This supersedes conjecture (168fj).  The proven TP3 and cubical MLR results
remain intact, but no primitive TP-infinity theorem can orient the complete
Laguerre tower.  Any all-orders variation-diminishing mechanism on this route
must use the completed multi-label modular sewing to repair, quotient, or
bypass a defect that is already present in one primitive label at order
seven.  This is precisely the kind of finite typed defect the
boundary-complex programme was meant to expose.  The Wronskian order `7` is
not itself a generalized-Laguerre order and supplies no counterexample to RH.

## Why seven appears: a size-biased gamma fold

The Gaussian representation (168fv) identifies the source of the reversal.
If `Y=Z^2`, then size-biasing by the leading factor `Y` changes the
`chi^2_1` law into a Gamma law of shape `3/2` and scale `2`.  Therefore, on
the diagonal,

\[
 a_m(t)=\mathbb E_{\Gamma(3/2,2)}[(Y-2t)^m].        \tag{168gc}
\]

The determinant sign is controlled by a single source-fixed fold at

\[
 \boxed{Y=2t.}                                      \tag{168gd}
\]

For odd `m`, the region below the fold contributes negatively and the gamma
tail above it contributes positively.  At the physical seam `t=pi`, orders
`1,3,5` are still interior-dominated; at order `7` the tail wins for the first
time.  Thus seven is the first orientation reversal of this exact
archimedean fold, not an unexplained fitted integer.

The same moment polynomial has the closed form

\[
 \boxed{
 a_m(t)=2^m(-1)^m m!\,
 L_m^{(-m-3/2)}(-t),
 }                                                    \tag{168ge}
\]

where `L_m^(alpha)` is the generalized Laguerre polynomial.  This identity
follows by expanding both sides:

\[
 a_m(t)=2^m\sum_{k=0}^m
 \binom mk(3/2)_{m-k}(-t)^k.                        \tag{168gf}
\]

The primitive TP question has therefore collapsed from arbitrary determinant
combinatorics to the sign pattern of one explicit moving-parameter Laguerre
family.  Formula (168ge) is explanatory rather than RH-equivalent: these are
Wronskian-order polynomials arising from the primitive transport kernel, not
the generalized Laguerre inequalities of `X`.

This also types the modular burden more sharply.  The exponential kernel
`e^{-AY}` is the universal totally-positive carrier.  The completion factor

\[
 (2AY-3)e^{-AY}
 =\left(-2A\partial_A-3\right)e^{-AY}              \tag{168gg}
\]

is its Euler--Darboux transform.  The transform preserves low-order
orientation but creates the gamma-fold reversal at order seven.  Any
completed modular repair on the TP route must therefore act on this explicit
Euler--Darboux defect; generic positivity of the underlying exponential
carrier cannot repair it.

## Modular response to the order-seven defect: parity block localization

For the pure label `n`, the same reduced Wronskian calculation is evaluated
at

\[
 t=\pi n^2e^{2u}.                                   \tag{168gh}
\]

At its positive-chamber endpoint `u=0`, the primitive label has `t=pi` and
the wrong order-seven sign.  Every higher label has

\[
 t=\pi n^2\ge4\pi>4.
\]

The recurrence (168fy) shows `a_6(t)>0` for all `t>=3`, so `a_7` is strictly
decreasing there; direct evaluation gives

\[
 a_7(4)=-365\,303<0.                                \tag{168gi}
\]

Hence

\[
 \boxed{
 n=1\text{ is the unique wrong-sign pure label at the order-seven seam;}
 \quad n\ge2\text{ have the canonical sign.}
 }                                                    \tag{168gj}
\]

This does not prove that the sum over labels repairs the defect, because a
Wronskian determinant is nonlinear and contains mixed-label columns.  It
does identify the minimal architecture: one primitive defect faces an
infinite family of source-fixed correctly oriented label channels.

The aggregate modular source supplies an additional exact operation absent
from every individual label.  On the positive chamber,

\[
 \sqrt2\,\Phi(u)
 =\sum_{n\ge1}n^{-1/2}\phi_1(u+\log n),
\]

while completed reciprocal reflection makes `Phi` smooth and even.  Thus

\[
 \boxed{
 \sum_{n\ge1}n^{-1/2}
 \phi_1^{(2j+1)}(\log n)=0
 \qquad(j\ge0).
 }                                                    \tag{168gk}
\]

These are exact all-label seam-repair identities.  Exponential suppression
of higher labels cannot be assessed before differentiation: the derivative
polynomials contain growing powers of `n`, and (168gk) says their aggregate
cancellation is exact.

At confluent order seven, the translation-kernel jet matrix, before its
fixed column-orientation signs, is

\[
 \mathcal J_7=\bigl[\Phi^{(i+j)}(0)\bigr]_{i,j=0}^6. \tag{168gl}
\]

Every entry with `i+j` odd vanishes by (168gk).  Reordering the indices by
parity therefore gives the canonical localization

\[
 \boxed{
 \mathcal J_7\cong E_4\oplus O_3,
 }                                                    \tag{168gm}
\]

where

\[
 E_4=\bigl[\Phi^{(2a+2b)}(0)\bigr]_{a,b=0}^3,
 \qquad
 O_3=\bigl[\Phi^{(2a+2b+2)}(0)\bigr]_{a,b=0}^2.    \tag{168gn}
\]

Consequently

\[
 \boxed{
 \det\mathcal J_7=\det E_4\,\det O_3.
 }                                                    \tag{168go}
\]

This is the smallest completed-seam test forced by the primitive falsifier.
Instead of asking whether infinitely many labels vaguely improve TP7, one
must determine the two exact modular jet determinants in (168go).  If their
oriented product is negative, the completed translation-total-positivity
route is finitely falsified.  If it is positive, modular reflection has
repaired the first primitive obstruction through a parity-localized
`4 plus 3` mechanism.  Either result concerns this sufficient TP route, not
RH itself.

## Programme correction: completed PF-infinity was already impossible

The parity-localized determinant (168go) is a legitimate finite-latency
diagnostic, but it is not the next RH obligation.  The earlier Schoenberg
audit in `theta-polya-frequency-no-go.md` already proves unconditionally that
the completed translation kernel `Phi(r-s)` cannot be totally positive of
all orders.

Indeed, if `Phi` were a Polya-frequency function of infinite order, its
bilateral Laplace transform would have Schoenberg form

\[
 \mathcal L\Phi(s)=\frac1{\Psi(s)}
\]

on a strip, with `Psi` entire Laguerre--Polya.  Superexponential decay makes
`L Phi` entire, and here it is the completed Xi transform up to convention.
The identity theorem would force that transform to be zero-free, contradicting
the unconditionally known critical-line zeros.

Therefore modular summation may move the first failing minor, and (168go)
could identify how, but it cannot restore TP-infinity.  The order-seven
primitive theorem should be retained as an analytic explanation of finite
total-positivity latency:

\[
 \boxed{
 \text{low-order variation diminution survives,}
 \quad
 \text{the Euler--Darboux fold eventually exposes a forbidden sign.}
 }                                                    \tag{168gp}
\]

The live RH-compatible positive object is instead the denominator-free
Loewner kernel

\[
 L_C(x,y)=
 \frac{(x-1/4)C'(x)C(y)-(y-1/4)C'(y)C(x)}{x-y}.    \tag{168gq}
\]

Unlike translation TP, positivity of `L_C` does not erase transform zeros.
An allowed real squared-zero coordinate contributes a positive rank-one
Loewner atom.  The programme distinction is thus

\[
 \boxed{
 \text{translation TP forbids the desired zeros;}
 \qquad
 \text{centered Loewner positivity carries them spectrally.}
 }                                                    \tag{168gr}
\]

Consequently no further primitive or aggregate TP census should be treated
as evidence for RH.  The next explanatory attack returns to the exact mixed
Green Bezoutian of `K` and `Phi`, seeking a source-derived order-two
Stieltjes/Loewner Gram factorization.  The order-seven fold may still inform
the necessary boundary channel, but it is not itself that factorization.

## Exact affine-regression law of the Green pair

The mixed pair has a source identity stronger than generic positivity.  In
the convergent precursor strip `0<x<1/4`, set

\[
 I(x)=\int_0^\infty K(u)\phi_x(u)du,
 \qquad
 d\mu_x(u)=\frac{K(u)\phi_x(u)}{I(x)}du,             \tag{168gs}
\]

with

\[
 \phi_x(u)=\cosh(\sqrt x\,u),
 \qquad
 q_x(u)=\partial_x\log\phi_x(u),
 \qquad
 r(u)=\frac{\Phi(u)}{K(u)}.                         \tag{168gt}
\]

The transferred Green identity

\[
 \int_0^\infty\Phi(u)\phi_x(u)du
 =\left(\frac14-x\right)I(x)
\]

is exactly the affine-regression law

\[
 \boxed{
 \mathbb E_x[r]=\frac14-x.
 }                                                    \tag{168gu}
\]

The tilt derivative of any fixed observable `f` is

\[
 \partial_x\mathbb E_x[f]
 =\operatorname{Cov}_x(f,q_x).
\]

Differentiating (168gu) therefore gives the calibrated source covariance

\[
 \boxed{
 \operatorname{Cov}_x(r,q_x)=-1
 \qquad(0<x<1/4).
 }                                                    \tag{168gv}
\]

All higher derivatives of (168gu) vanish, producing a hierarchy of exact
connected-response cancellations.  This is the statistical form of the
Green operator: modular completion forces one unit of anticorrelation
between the source potential `Phi/K` and the vertical response coordinate.

The mixed response ratio in the Loewner Bezoutian is

\[
 R(x)=\frac{P(x)}{I(x)}
 =\mathbb E_x[rq_x]
 =\left(\frac14-x\right)\mathbb E_x[q_x]-1.         \tag{168gw}
\]

The final equality is precisely (168gv).  Consequently diagonal Loewner
positivity is

\[
 \boxed{
 R'(x)le0,
 \qquad
 R'(x)=\mathbb E_x[r\,\partial_xq_x]
       +\operatorname{Cov}_x(rq_x,q_x).
 }                                                    \tag{168gx}
\]

This reduction isolates the first unforced connected response.  The
zeroth-order expectation and first covariance are fixed exactly by the
source operator; only the derivative of the mixed product remains to be
oriented.

The calibration is structural but not theta-specific.  Given any admissible
positive-even source `Phi`, its Green resolvent
`K=(1/4-D^2)^{-1}Phi` satisfies (168gu)--(168gv).  Thus the earlier four-atom
Loewner falsifier can be equipped with the same Green pair and shows that
affine regression plus covariance `-1` is insufficient.  These identities
type the universal carrier correctly; the missing inequality must still
spend modular/arithmetic information beyond the Green operator.

The identity is not yet a proof: a fixed negative covariance does not control
the sign of the higher mixed response in (168gx).  The sharp next theorem is
a second-order regression inequality for this particular pair `(r,q_x)`, or
an exact decomposition of `-R'` as its squared regression norm plus a
modular boundary current.  That is narrower than another raw moment or minor
certificate.

## Uniform regression-slope shortcut is impossible

The covariance calibration suggests a tempting deterministic comparison.
For independent `U,V` with law `mu_x`,

\[
 -\operatorname{Cov}_x(r,q_x)
 =\frac12\mathbb E_x
 \left[-(r(U)-r(V))(q_x(U)-q_x(V))\right]=1,       \tag{168gy}
\]

and

\[
 \operatorname{Var}_x(q_x)
 =\frac12\mathbb E_x[(q_x(U)-q_x(V))^2].           \tag{168gz}
\]

Hence a uniform secant estimate

\[
 -(r(u)-r(v))(q_x(u)-q_x(v))
 \ge\lambda_x(q_x(u)-q_x(v))^2                    \tag{168ha}
\]

would give `Var_x(q_x)<=1/lambda_x` and could close the diagonal Loewner
gate for a sufficiently large `lambda_x`.

But no positive uniform `lambda_x` exists.  The theta and precursor tails
satisfy

\[
 r(u)=\frac{\Phi(u)}{K(u)}\longrightarrow0
 \quad\text{superexponentially},
 \qquad
 q_x(u)\sim\frac{u}{2\sqrt x}\longrightarrow\infty. \tag{168hb}
\]

Fixing `v` and sending `u` to infinity makes

\[
 \frac{-(r(u)-r(v))}{q_x(u)-q_x(v)}\longrightarrow0. \tag{168hc}
\]

Therefore the strongest unweighted MLR/Sturm slope comparison is
analytically falsified.  This does not falsify the variance inequality:
`mu_x` suppresses the remote tail exponentially, and (168gy) is an integrated
identity.  It proves that the missing theorem must be a weighted covariance
or transport inequality retaining the actual precursor law, not a global
pointwise ordering of `r` against `q_x`.

## Canonical weighted Sturm transport

The required weight is already contained in the Green pair.  Put

\[
 p_x(u)=K(u)\phi_x(u),
 \qquad
 g_x(u)=\frac{K'(u)}{K(u)}
       -\frac{\phi_x'(u)}{\phi_x(u)}.               \tag{168hd}
\]

The numerator `p_x g_x` is the Wronskian

\[
 p_xg_x=K'\phi_x-K\phi_x'.
\]

Using

\[
 K''=\left(\frac14-r\right)K,
 \qquad
 \phi_x''=x\phi_x,
\]

its derivative is

\[
 \partial_u(p_xg_x)
 =\left(\frac14-x-r(u)\right)p_x(u).               \tag{168he}
\]

Equivalently,

\[
 \boxed{
 r(u)-\left(\frac14-x\right)
 =-\frac1{p_x(u)}\partial_u\bigl(p_x(u)g_x(u)\bigr).
 }                                                    \tag{168hf}
\]

The boundary current vanishes at zero by evenness and at infinity by the
precursor decay in `x<1/4`.  Hence for every admissible differentiable test
function `f`, integration by parts gives

\[
 \boxed{
 \operatorname{Cov}_x(r,f)
 =\mathbb E_x[g_x f'].
 }                                                    \tag{168hg}
\]

Taking `f=q_x` recovers the calibrated identity in differential form,

\[
 \boxed{\mathbb E_x[g_x q_x']=-1.}                 \tag{168hh}
\]

This is the faithful weighted transport that the uniform-slope shortcut was
missing.  Its weight is the source Wronskian itself, not a fitted Poincare or
Brascamp--Lieb coefficient.

There is a useful conditional orientation statement.  If

\[
 r(u)=\Phi(u)/K(u)
\]

is strictly decreasing on the positive chamber, then it crosses its mean
`1/4-x` exactly once.  Equation (168he), together with
`p_xg_x=0` at both endpoints, then forces

\[
 g_x(u)<0\qquad(u>0).                               \tag{168hi}
\]

Consequently `-g_x p_x du` is a canonical positive transport current and
(168hg) gives the expected opposite ordering of `r` against every increasing
observable.

The monotonicity of `Phi/K` is therefore the next smallest analytic gate for
this Sturm route.  Even if it holds, it proves only first-order covariance
orientation; the Loewner derivative still requires a second connected
inequality.  If `Phi/K` has a turning point, the proposed one-current Sturm
mechanism is falsified and the modular repair must retain more than one
boundary channel.

## Theta theorem: the weighted Sturm current is strictly positive

The conditional monotonicity assumption on `Phi/K` is unnecessary for
orienting the first Sturm current.  Write on `u>=0`

\[
 K(u)=K_0(u)(1-\rho(u)),
 \qquad
 K_0(u)=\frac12e^{-u/2},
 \qquad
 \rho(u)=2e^u\sum_{n\ge1}e^{-\pi n^2e^{2u}}.        \tag{168hj}
\]

Positivity of `K` gives `0<rho<1`.  Put `y=e^{2u}` and

\[
 \mathcal F(y)
 :=8y^{3/2}\sum_{n\ge1}\pi n^2e^{-\pi n^2y}
   -2\sqrt y\sum_{n\ge1}e^{-\pi n^2y}.             \tag{168hk}
\]

The inequality `K'(u)<0` is equivalent to

\[
 -\rho'(u)<\frac12(1-\rho(u)),
\]

which in turn is exactly `mathcal F(y)<1`.  The `n`th summand of
`mathcal F` is

\[
 h_n(y)=2\sqrt y\,(4a_ny-1)e^{-a_ny},
 \qquad a_n=\pi n^2.                               \tag{168hl}
\]

Its derivative has the sign of

\[
 7a_ny-\frac12-4a_n^2y^2<0,                        \tag{168hm}
\]

because `a_ny>=pi>3`.  Hence every label contribution, and therefore
`mathcal F`, is strictly decreasing for `y>=1`.  Smooth even modular sewing
gives `K'(0)=0`, equivalently

\[
 \mathcal F(1)=1.                                  \tag{168hn}
\]

It follows that

\[
 \boxed{K'(u)<0\qquad(u>0).}                       \tag{168ho}
\]

For `0<=x<1/4`,

\[
 \frac{\phi_x'(u)}{\phi_x(u)}
 =\sqrt x\tanh(\sqrt x\,u)\ge0,
\]

strictly for `x,u>0`.  Combining this with (168ho) proves

\[
 \boxed{
 g_x(u)=\frac{K'}K-\frac{\phi_x'}{\phi_x}<0
 \qquad(u>0).
 }                                                    \tag{168hp}
\]

Thus

\[
 d\tau_x(u):=-g_x(u)d\mu_x(u)                      \tag{168hq}
\]

is a canonical positive transport current, and (168hg) becomes

\[
 \boxed{
 -\operatorname{Cov}_x(r,f)
 =\int_0^\infty f'(u)d\tau_x(u)ge0
 }                                                    \tag{168hr}
\]

for every increasing differentiable `f`.  In particular its mass against
the response gradient is normalized exactly:

\[
 \int_0^\infty q_x'(u)d\tau_x(u)=1.                \tag{168hs}
\]

This supersedes the conditional first-order orientation following (168hi).
Theta label structure proves positivity of the weighted Sturm current
directly, even without pointwise monotonicity of `Phi/K`.

The remaining diagonal Loewner obstruction is genuinely second order, but a
typing caution is essential: (168hr) transfers covariances whose first
argument is `r`; it cannot be applied directly to
`Cov_x(rq_x,q_x)`.  Put `a=1/4-x` and `m=E_x[q_x]`.  Correct expansion gives

\[
\begin{aligned}
 \operatorname{Cov}_x(rq_x,q_x)
 &=a\operatorname{Var}_x(q_x)
   +\operatorname{Cov}_x(r,q_x^2)
   -m\operatorname{Cov}_x(r,q_x)\\
 &=a\operatorname{Var}_x(q_x)
   -2\int q_xq_x'\,d\tau_x+m,                     \tag{168ht}
\end{aligned}
\]

while

\[
 \mathbb E_x[r\,\partial_xq_x]
 =a\mathbb E_x[\partial_xq_x]
  -\int\partial_u\partial_xq_x\,d\tau_x.          \tag{168hu}
\]

The kernel differential equation supplies the resulting normalization

\[
 \int\left(2q_xq_x'
 +\partial_u\partial_xq_x\right)d\tau_x=2m.        \tag{168hv}
\]

Substitution reduces exactly to

\[
 \boxed{
 R'(x)=-m+a\left(
 \mathbb E_x[\partial_xq_x]
 +\operatorname{Var}_x(q_x)
 \right).
 }                                                    \tag{168hw}
\]

Thus the positive Sturm current faithfully reproduces, rather than bypasses,
the earlier response-versus-variance gate.  Its value is that every
first-order sign and boundary normalization is now source-derived.  The
remaining theorem must be a weighted second-order concentration inequality
for `mu_x`, or a genuinely coupled Loewner factorization; another covariance
integration by parts with no new theta input will be circular.

## Null-mode normalization of the second-order gate

The response--variance inequality has an exact critical baseline.  Let

\[
 K_0(u)=\frac12e^{-u/2},
 \qquad
 R_\theta(u)=K_0(u)-K(u)>0,
 \qquad
 a=\frac14-x.                                      \tag{168hx}
\]

For `0<=x<1/4`, direct integration gives

\[
 I_0(x):=\int_0^\infty K_0(u)\phi_x(u)du
 =\frac1{4a}.                                      \tag{168hy}
\]

The null-mode logarithmic response is therefore

\[
 m_0=(\log I_0)'=\frac1a,
 \qquad
 m_0'=\frac1{a^2},
\]

and it saturates the diagonal Loewner gate exactly:

\[
 m_0-a m_0'=0.                                     \tag{168hz}
\]

Put

\[
 J(x)=\int_0^\infty R_\theta(u)\phi_x(u)du,
 \qquad
 \eta(x)=\frac{J(x)}{I_0(x)}=4aJ(x).               \tag{168ia}
\]

Since `0<R_theta<K_0`, one has `0<eta<1`, and

\[
 I(x)=I_0(x)(1-\eta(x)).                            \tag{168ib}
\]

Thus, with `m=(log I)'`,

\[
 m(x)=\frac1a-\frac{\eta'(x)}{1-\eta(x)}.         \tag{168ic}
\]

For the centered response

\[
 H(x)=1+(x-1/4)m(x)=1-a m(x),
\]

the null contribution cancels identically and leaves

\[
 \boxed{
 H(x)=a\frac{\eta'(x)}{1-\eta(x)}.
 }                                                    \tag{168id}
\]

Consequently the complete diagonal Loewner condition is the single remainder
curvature inequality

\[
 \boxed{
 H'(x)=
 \frac{
 a\eta''(1-\eta)+a(\eta')^2-\eta'(1-\eta)
 }{(1-\eta)^2}
 \ge0.
 }                                                    \tag{168ie}
\]

Equivalently, if

\[
 U(x)=\frac1{1-\eta(x)}=\frac{I_0(x)}{I(x)},
\]

then

\[
 \boxed{
 H=a(\log U)',
 \qquad
 H'=(a\partial_x-1)(\log U)'.
 }                                                    \tag{168if}
\]

This is the correct meaning of the variance gate: the universal exponential
carrier lies exactly on its boundary, and the entire strict sign must be
created by the normalized theta subtraction `eta`.  No generic concentration
inequality should be expected to see this near-critical cancellation unless
it retains that subtraction.

There is also a probability interpretation requiring no new measure.  Under
the explicit null-mode tilted law

\[
 d\nu_{0,x}(u)=\frac{K_0(u)\phi_x(u)}{I_0(x)}du,
\]

one has

\[
 \boxed{
 \eta(x)=\mathbb E_{0,x}[\rho(U)],
 \qquad
 \rho(u)=\frac{R_\theta(u)}{K_0(u)}.
 }                                                    \tag{168ig}
\]

The earlier labelwise theorem proves that `rho` is strictly decreasing.  The
next theta-specific task is therefore not to bound the variance of an
arbitrary law, but to orient the curvature (168ie) of the expectation of one
explicit decreasing modular observable under an exactly solvable two-rate
exponential tilt.

## One-measure reduction of the normalized theta subtraction

Put

\[
 s=\sqrt x,
 \qquad
 \lambda_-=\frac12-s,
 \qquad
 \lambda_+=\frac12+s,
 \qquad
 a=\lambda_-\lambda_+.                             \tag{168ih}
\]

The null tilted density is explicitly

\[
 d\nu_{0,x}(u)
 =a\left(e^{-\lambda_-u}+e^{-\lambda_+u}\right)du. \tag{168ii}
\]

Thus, for the Laplace transform

\[
 L_\rho(\lambda)=\int_0^\infty e^{-\lambda u}\rho(u)du,
\]

formula (168ig) becomes

\[
 \boxed{
 \eta(x)=a\left[
 L_\rho(\lambda_-)+L_\rho(\lambda_+)
 \right].
 }                                                    \tag{168ij}
\]

The theta label formula in (168hj) proves directly that `rho'(u)<0`: every
term has logarithmic derivative `1-2pi n^2e^{2u}<0`.  Therefore

\[
 d\sigma(u):=-d\rho(u)\ge0,
 \qquad
 \sigma([0,\infty))=\rho(0).                       \tag{168ik}
\]

Integration by parts gives, for every `lambda>0`,

\[
 \lambda L_\rho(\lambda)
 =\int_0^\infty(1-e^{-\lambda u})d\sigma(u).        \tag{168il}
\]

Consequently the normalized subtraction is the single-measure integral

\[
 \boxed{
 \eta(x)=\int_0^\infty
 \left[
 \lambda_+(1-e^{-\lambda_-u})
 +\lambda_-(1-e^{-\lambda_+u})
 \right]d\sigma(u).
 }                                                    \tag{168im}
\]

All theta arithmetic is now contained in the positive seam measure `sigma`;
the dependence on the spectral coordinate is the explicit two-rate kernel
in brackets.  This is a genuine reduction, but not yet a universal positivity
theorem: the Loewner curvature (168ie) is nonlinear in the integral, so
pointwise positivity of the bracket does not orient it.

The next hostile question is exact.  Determine whether (168ie) holds for
every positive `sigma`, or whether a one- or two-atom `sigma` falsifies that
universal claim.  If an atomic falsifier exists, the proof must use an
additional shape property of the actual theta seam measure.  If every atom
and every two-atom mixture passes and the kernel is closed under positive
mixture in the required nonlinear sense, the diagonal Loewner theorem would
follow from the monotone theta ratio alone.

## One-atom falsifier: monotone seam mass is insufficient

The universal claim in the preceding paragraph is false already for one
atom.  Take

\[
 d\sigma=M\delta_U,
 \qquad 0<M<1,
\]

so `eta(x)=M k_U(x)` with

\[
 k_U(x)=1-e^{-U/2}
 \left[
 \cosh(U\sqrt x)+2\sqrt x\sinh(U\sqrt x)
 \right].                                          \tag{168in}
\]

At `x=0`, exact expansion in `x` gives

\[
\begin{aligned}
 k_U'(0)&=-e^{-U/2}\left(2U+\frac{U^2}{2}\right),\\
 k_U''(0)&=-e^{-U/2}\left(\frac{2U^3}{3}
                              +\frac{U^4}{12}\right).
\end{aligned}                                      \tag{168io}
\]

The numerator of (168ie), to first order in `M`, is

\[
 M\left[\frac14k_U''(0)-k_U'(0)\right]+O(M^2).
\]

Its exact coefficient factors as

\[
 \boxed{
 \frac14k_U''(0)-k_U'(0)
 =-\frac{U(U-4)(U^2+12U+24)}{48}e^{-U/2}.
 }                                                    \tag{168ip}
\]

Thus every `U>4` gives a negative linear coefficient.  By continuity, for
all sufficiently small positive `M`, the full nonlinear curvature numerator
is negative while `0<eta<1`.  Smooth decreasing approximations to the step
ratio preserve the strict failure.

Therefore

\[
 \boxed{
 d\sigma\ge0\text{ and }\rho'\le0
 \not\Longrightarrow H'(0)\ge0.
 }                                                    \tag{168iq}
\]

The exact threshold `U=4` identifies the missing theta information.  Seam
mass within four logarithmic-scale units contributes with the desired sign
at first order, whereas sufficiently remote mass contributes with the wrong
sign.  The actual theta measure decays superexponentially, so it may satisfy
the required weighted balance, but that balance must be proved from its
labelled tail rather than inferred from monotonicity.

The smallest faithful scalar target at the central point is now a signed
moment of the actual seam measure with weight (168ip), together with the
explicit quadratic-in-mass correction from (168ie).  This is an analytic
near-seam/tail theorem, not a generic concentration principle.

## Rank-uniform lift: one-seam plus two-seam Loewner kernel

The seam-measure reduction extends before taking a diagonal.  Write

\[
 a_x=\frac14-x,
 \qquad
 H(x)=\frac{a_x\eta'(x)}{1-\eta(x)},
\]

and orient the Loewner divided difference as

\[
 K_H(x,y)=\frac{H(y)-H(x)}{y-x}.                   \tag{168ir}
\]

Clearing the positive central-strip denominators gives the faithful kernel

\[
 \mathscr L_\eta(x,y)
 :=(1-\eta(x))(1-\eta(y))K_H(x,y).                 \tag{168is}
\]

Using

\[
 \eta(x)=\int k_u(x)d\sigma(u),
 \qquad
 h_u(x):=a_x\partial_xk_u(x),                      \tag{168it}
\]

direct expansion yields

\[
 \boxed{
 \mathscr L_\eta(x,y)
 =\int \mathscr E_u(x,y)d\sigma(u)
 +\iint \mathscr Q_{u,v}(x,y)d\sigma(u)d\sigma(v).
 }                                                    \tag{168iu}
\]

The linear one-seam kernel is

\[
 \boxed{
 \mathscr E_u(x,y)
 =\frac{h_u(y)-h_u(x)}{y-x},
 }                                                    \tag{168iv}
\]

and a symmetric two-seam representative is

\[
 \boxed{
 \mathscr Q_{u,v}(x,y)
 =\frac{
 h_u(x)k_v(y)+h_v(x)k_u(y)
 -h_u(y)k_v(x)-h_v(y)k_u(x)
 }{2(y-x)}.
 }                                                    \tag{168iw}
\]

Formula (168iu) is exact and rank-uniform: every finite Loewner matrix is the
same one-copy plus two-copy seam integral.  No higher seam powers occur;
they were artifacts of leaving the scalar denominators uncleared.

The one-atom falsifier (168ip) shows that `mathscr E_u` is not positive for
all seam locations.  Nor may the quadratic block be discarded: it is the
canonical interaction generated by denominator clearing and can repair or
worsen the linear tail defect.  The legitimate theorem is positivity of the
completed sum in (168iu), not separate positivity of either presentation
block.

This is the coupled analogue of the null-mode cancellation found earlier:

\[
 \boxed{
 \text{critical carrier removed}
 \longrightarrow
 \text{one-seam response}
 +\text{two-seam interaction}.
 }                                                    \tag{168ix}
\]

The next combinatorial gate is now finite in source-copy number.  Substitute
the labelled theta density

\[
 d\sigma=\sum_{n\ge1}d\sigma_n
\]

into (168iu), group `(m,n)` under exchange and prime-scale transport, and
test whether each completed label orbit has a Gram factorization.  A negative
finite Loewner matrix for one fully completed orbit is the sharp falsifier;
entrywise signs of `mathscr E` or `mathscr Q` alone are not.

## Arithmetic transport of the seam measure

The seam measure in (168iu) retains the theta labels exactly.  From

\[
 \rho_n(u)=2e^u e^{-\pi n^2e^{2u}},
 \qquad
 d\sigma_n(u)=-\rho_n'(u)du,
\]

one obtains

\[
 \boxed{
 \rho_n(u)=n^{-1}\rho_1(u+\log n),
 \qquad
 d\sigma_n(u)=n^{-1}d\sigma_1(u+\log n).
 }                                                    \tag{168iy}
\]

In particular prime transport is

\[
 \boxed{
 d\sigma_{pn}(u)=p^{-1}d\sigma_n(u+\log p).
 }                                                    \tag{168iz}
\]

The completed seam measure is the positive label sum

\[
 d\sigma=\sum_{n\ge1}d\sigma_n.                    \tag{168ja}
\]

Therefore the quadratic part of (168iu) is indexed by ordered label pairs
`(m,n)`.  For a fixed product `q=mn`, every pair carries the common arithmetic
weight `q^{-1}`.  Exchange `(m,n)<->(n,m)` is already a symmetry of
`mathscr Q`, while adjacent prime transfer moves one `log p` displacement
between the two seam coordinates.  The factorization fiber is again the
divisor box

\[
 \mathcal B_q=\prod_{p^a\parallel q}\{0,\ldots,a\},
\]

but the spectral matrix rank no longer raises its source-copy degree.

This is a substantial compression relative to the generalized-Laguerre
Krein tower:

\[
 \boxed{
 \text{all Loewner ranks}
 \longleftarrow
 \text{one labelled seam copy}
 +\text{two labelled seam copies}.
 }                                                    \tag{168jb}
\]

The live arithmetic theorem is now source-finite: prove that prime-translated
divisor boxes orient the completed kernels `mathscr E+mathscr Q` as positive
Loewner matrices for arbitrary spectral tuples.  Infinite matrix rank remains,
but no growing source-copy or negative-channel tower is required.

## Canonical Dirichlet blocks include the carrier--seam edge

The preceding statement requires one refinement: the linear and quadratic
terms must be grouped together before assigning divisor boxes.  Remove the
common arithmetic weight by writing

\[
 d\sigma_n=n^{-1}d\tau_n,
 \qquad
 d\tau_n(u)=d\sigma_1(u+\log n).                   \tag{168jc}
\]

Let `mathscr E[tau]` denote the linear integral of `mathscr E_u`, and let
`mathscr Q[tau_m,tau_n]` denote the bilinear integral of
`mathscr Q_{u,v}`.  Then (168iu) has the exact Dirichlet decomposition

\[
 \boxed{
 \mathscr L_\eta
 =\sum_{q\ge1}\frac1q\,\mathscr B_q,
 }                                                    \tag{168jd}
\]

where

\[
 \boxed{
 \mathscr B_q
 =\mathscr E[\tau_q]
 +\sum_{mn=q}\mathscr Q[\tau_m,\tau_n].
 }                                                    \tag{168je}
\]

Thus block `q` contains exactly:

* the carrier--seam edge with seam label `q`; and
* every ordered two-seam factorization `(m,n)` with `mn=q`.

The common coefficient `q^{-1}` is forced simultaneously by the one-label
scaling and by multiplication of the two pair weights.  No fitted
normalization is involved.

For example,

\[
\begin{aligned}
 \mathscr B_1&=\mathscr E[\tau_1]
              +\mathscr Q[\tau_1,\tau_1],\\
 \mathscr B_p&=\mathscr E[\tau_p]
              +\mathscr Q[\tau_1,\tau_p]
              +\mathscr Q[\tau_p,\tau_1],          \tag{168jf}
\end{aligned}
\]

for a prime `p`.  The second line is the first nontrivial completed
factorization interval: one transported carrier edge plus the reflection
pair `(1,p),(p,1)`.

This is the faithful meaning of a completed divisor box.  Testing
`mathscr E[tau_q]` alone or a quadratic factor pair alone breaks Dirichlet
incidence.  Positivity of every `mathscr B_q` would be a sufficient
rank-uniform theorem, but it is not assumed necessary: distinct `q` blocks
may still repair one another in the full sum.  Accordingly a negative block
falsifies only the blockwise explanation, while a negative matrix of the full
kernel falsifies the RH-equivalent Loewner conjecture.

The smallest analytic attack is now unambiguous:

\[
 \boxed{
 \mathscr B_1\ \text{first},
 \qquad
 \mathscr B_p\ \text{second}.
 }                                                    \tag{168jg}
\]

Both use the fixed primitive seam measure and exact source shifts; neither is
a freely chosen finite-label scout.

## First block theorem: `B_1` passes the central diagonal gate

For the primitive block, let `eta_1` be generated by `d sigma_1`.  At `x=0`
the linear part of the curvature numerator (168ie) is

\[
 \mathcal C_1
 =\int_0^\infty W(u)d\sigma_1(u),                  \tag{168jh}
\]

where

\[
 \boxed{
 W(u)=e^{-u/2}
 \frac{u(4-u)(u^2+12u+24)}{48}.
 }                                                    \tag{168ji}
\]

The weight is positive on `(0,4)` and negative beyond `4`.  The primitive
seam density is

\[
 \frac{d\sigma_1}{du}
 =2e^u(2\pi e^{2u}-1)e^{-\pi e^{2u}}.              \tag{168jj}
\]

The sign can be proved with deliberately crude elementary bounds.  On
`0<=u<=1/10`, use

\[
 e^{-u/2}>\frac{19}{20},
 \quad 4-u\ge\frac{39}{10},
 \quad u^2+12u+24\ge24,
\]

and `pi>3`, `pi e^(1/5)<4`, `e^4<55`.  Then

\[
 W(u)>\frac{741}{400}u,
 \qquad
 \frac{d\sigma_1}{du}>\frac2{11},
\]

so

\[
 \int_0^{1/10}W(u)d\sigma_1(u)
 >\frac{1482}{880000}>\frac1{1000}.                \tag{168jk}
\]

On the hostile tail `u=4+t`, use

\[
 |W(u)|\frac{d\sigma_1}{du}
 \le\frac\pi2u^4e^{5u/2}e^{-\pi e^{2u}}.
\]

Since `pi e^8>768`, `e^(2t)>=1+2t`, and
`(4+t)^4<=256e^t`, the entire tail satisfies

\[
 \int_4^\infty|W(u)|d\sigma_1(u)<e^{-750}<2^{-750}. \tag{168jl}
\]

The omitted interval `[1/10,4]` contributes nonnegatively.  Therefore

\[
 \boxed{\mathcal C_1>0.}                            \tag{168jm}
\]

For one seam measure the full diagonal numerator is

\[
 (1-\eta_1(0))\mathcal C_1
 +\frac14\left(int_0^\infty
 e^{-u/2}\left(2u+\frac{u^2}{2}\right)d\sigma_1(u)
 \right)^2.                                        \tag{168jn}
\]

Both terms are strictly positive.  Hence

\[
 \boxed{
 \mathscr B_1(0,0)>0.
 }                                                    \tag{168jo}
\]

This is a source theorem for the smallest completed Dirichlet block, not a
global block-positivity theorem.  Separated spectral points and the full
central interval remain open.  Its explanatory content is the exact balance:
the primitive seam lies overwhelmingly inside the universal favorable
distance `u=4`, and its superexponential hostile tail cannot reverse the
carrier--seam orientation.

## Diagonal Dirichlet blocks reduce to three seam moments

The central diagonal of every block has a closed arithmetic convolution
formula.  For the unweighted shifted measure `tau_n`, define

\[
\begin{aligned}
 E_n&=\int_0^\infty(1-e^{-u/2})d\tau_n(u),\\
 A_n&=\int_0^\infty e^{-u/2}
 \left(2u+\frac{u^2}{2}\right)d\tau_n(u),\\
 C_n&=\int_0^\infty W(u)d\tau_n(u),                \tag{168jp}
\end{aligned}
\]

with `W` from (168ji).  Expanding

\[
 (1-\eta(0))\mathcal C+\frac14\mathcal A^2
\]

by Dirichlet convolution shows that the `q`th block diagonal is, up to its
positive common factor `q^{-1}`,

\[
 \boxed{
 D_q
 =C_q-\sum_{mn=q}E_mC_n
 +\frac14\sum_{mn=q}A_mA_n.
 }                                                    \tag{168jq}
\]

For `q=1`, this is exactly (168jn).  For a prime `p`, only the ordered
factorizations `(1,p)` and `(p,1)` occur, so

\[
 \boxed{
 D_p=(1-E_1)C_p-E_pC_1+\frac12A_1A_p.
 }                                                    \tag{168jr}
\]

Every coefficient is source-derived.  The middle term is the sole negative
transported carrier interaction; the last term is the canonical reflection-
pair repair.  No matrix determinant or fitted constant remains at the
diagonal prime-block level.

This is the smallest prime theorem now worth proving:

\[
 \boxed{D_p>0\qquad\text{for every prime }p.}       \tag{168js}
\]

It has a direct falsifier and a plausible uniform mechanism.  Translation by
`log p` makes `tau_p` increasingly concentrated at the seam, where

\[
 A(u)\sim2u,
 \qquad E(u)\sim\frac u2,
 \qquad C(u)\sim2u.
\]

Thus `A_p/E_p` and `C_p/E_p` approach `4`, while the hostile region
`u>4` is suppressed still more strongly than for `p=1`.  Turning these
asymptotics into monotone ratio bounds would prove all prime diagonal blocks
at once.  Passing (168js) would still not establish separated-point or
composite-block positivity, but it would identify the first arithmetic
repair theorem beyond the primitive block.

## Uniform theorem for every prime diagonal block

The ratio estimate proposed above can be proved without asymptotics.  The
total mass of `tau_n` is

\[
 \tau_n([0,\infty))=2n e^{-\pi n^2}.
\]

After normalization, its survival function is exactly

\[
 \boxed{
 S_a(u)=e^u\exp[-a(e^{2u}-1)],
 \qquad a=\pi n^2.
 }                                                    \tag{168jt}
\]

Let `G(u)=C(u)-E(u)` denote the difference of the two scalar kernels in
(168jp).  Since `G(0)=0`, survival integration gives

\[
 \frac{C_n-E_n}{\tau_n([0,\infty))}
 =\int_0^\infty G'(u)S_a(u)du.                     \tag{168ju}
\]

Direct differentiation yields

\[
 G'(u)=e^{-u/2}
 \left(\frac32-\frac{3u^2}{4}+\frac{u^4}{96}\right). \tag{168jv}
\]

For every `n>=1`, one has `a=pi n^2>3`.  On
`0<=u<=1/(4a)<1/12`,

\[
 G'(u)>1,
 \qquad
 e^{2u}-1\le3u,
\]

so the positive initial contribution obeys

\[
 \int_0^{1/(4a)}G'(u)S_a(u)du
 >\int_0^{1/(4a)}e^{-3au}du
 >\frac1{6a}.                                      \tag{168jw}
\]

Every negative contribution lies in `u>=1`.  Using
`e^{2u}-1>=2u` and the elementary polynomial bound

\[
 |G'(u)|<4e^u\qquad(u\ge1),
\]

gives

\[
 \int_1^\infty |G'(u)|S_a(u)du
 <\frac{4e^{-(2a-2)}}{2a-2}
 <\frac1{6a}\qquad(a\ge3).                         \tag{168jx}
\]

Consequently

\[
 \boxed{C_n>E_n>0\qquad(n\ge1).}                   \tag{168jy}
\]

The primitive constants require only coarse upper bounds.  Since

\[
 \tau_1([0,\infty))=2e^{-\pi}<\frac1{10},
\]

and `0<E(u)<1`,

\[
 E_1<\frac1{10}.                                   \tag{168jz}
\]

Moreover `W(u)<3` on its positive interval `0<u<4`: on `[0,1]` this
is immediate, on `[1,2]` it follows from
`e^{-u/2}(2u+u^2/2)<=6/e<3`, and on `[2,4]` the exact derivative of
`W` is negative.  Its tail is negative, so

\[
 0<C_1<3\tau_1([0,\infty))<\frac3{10}.             \tag{168ka}
\]

For every prime `p`, combine (168jy), (168jz), and (168ka):

\[
\begin{aligned}
 (1-E_1)C_p-E_pC_1
 &>E_p\left(\frac9{10}-\frac3{10}\right)\\
 &=\frac35E_p>0.
\end{aligned}                                      \tag{168kb}
\]

The remaining reflection-pair repair is itself positive.  Therefore

\[
 \boxed{
 D_p>\frac35E_p+\frac12A_1A_p>0
 \qquad\text{for every prime }p.
 }                                                    \tag{168kc}
\]

This proves (168js), and actually proves the same inequality for every
single-label block formula with `n>=2`.  The mechanism is uniform:
prime translation concentrates the transported seam strongly enough that
its linear reserve already dominates the primitive carrier defect; the
quadratic reflection pair supplies additional, not merely compensating,
positivity.

## Composite blocks are governed by one moment cone

The prime proof does not have to be repeated along the divisor lattice.
Regroup the ordered factorizations in (168jq).  For a nonsquare `q`, this
gives

\[
 D_q=C_q+
 \sum_{\substack{m<n\\mn=q}}
 \left(
 \frac12A_mA_n-E_mC_n-E_nC_m
 \right),                                           \tag{168kd}
\]

while every square factorization contributes the additional diagonal term

\[
 \frac14A_m^2-E_mC_m.                               \tag{168ke}
\]

Thus the entire composite problem is controlled by the normalized moment
coordinates

\[
 \alpha_n=\frac{A_n}{E_n},
 \qquad
 \gamma_n=\frac{C_n}{E_n}.                         \tag{168kf}
\]

Indeed, a pair `m,n` is oriented precisely when

\[
 \boxed{
 \frac12\alpha_m\alpha_n\ge\gamma_m+\gamma_n,
 }                                                    \tag{168kg}
\]

and a repeated factor is oriented precisely when

\[
 \boxed{
 \alpha_m^2\ge4\gamma_m.
 }                                                    \tag{168kh}
\]

There is a particularly simple sufficient cone:

\[
 \boxed{
 0<\alpha_n\le4,
 \qquad
 0<\gamma_n\le2\alpha_n-4.
 }                                                    \tag{168ki}
\]

For two points in this cone,

\[
\begin{aligned}
 \frac12\alpha_m\alpha_n-\gamma_m-\gamma_n
 &\ge
 \frac12\alpha_m\alpha_n-2\alpha_m-2\alpha_n+8\\
 &=\frac12(4-\alpha_m)(4-\alpha_n)\ge0,            \tag{168kj}
\end{aligned}
\]

and setting `m=n` gives (168kh).  Consequently:

\[
 \boxed{
 \text{if every theta seam label lies in (168ki), then }
 D_q>0\text{ for every }q\ge1.
 }                                                    \tag{168kk}
\]

The strictness comes from the leading term `C_q>0`; for `q>=2` this was
proved in (168jy), and for `q=1` in (168jm).

The upper face `alpha<=4` is already source-free at the kernel level.  If

\[
 E(u)=1-e^{-u/2},
 \qquad
 A(u)=e^{-u/2}\left(2u+\frac{u^2}{2}\right),
\]

then

\[
 4E(u)-A(u)
 =4e^{-u/2}
 \left(e^{u/2}-1-\frac u2-\frac{u^2}{8}\right)
 \ge0                                               \tag{168kl}
\]

by the Taylor series of the exponential.  Hence

\[
 \boxed{\alpha_n\le4\quad\text{for every }n.}      \tag{168km}
\]

What remains is exactly one label-uniform source inequality,

\[
 \boxed{
 C_n+4E_n\le2A_n
 \qquad(n\ge1).
 }                                                    \tag{168kn}
\]

It cannot be asserted pointwise: the scalar kernel
`2A(u)-4E(u)-C(u)` eventually becomes negative.  Thus (168kn), if true, is
genuinely a theorem about the translated theta seam law rather than an
algebraic accident of the readout kernels.  Conversely, its first failure is
the canonical composite-block falsifier; no choice of factor pairing or
post-hoc regrouping is available.

This is the desired combinatorial reduction:

\[
 \boxed{
 \text{all diagonal Dirichlet blocks}
 \longleftarrow
 \text{one two-dimensional seam-moment cone}.
 }                                                    \tag{168ko}
\]

It also explains why finite block scouting is now low-value.  The theorem is
not indexed by the number of divisors of `q`; divisor combinatorics merely
forms pairwise sums inside a cone.  The only live issue is whether the exact
theta transport places every label on the correct side of the single face
(168kn).

## The theta seam lies in the moment cone

The remaining face has a one-fold derivative.  Put

\[
 F(u)=2A(u)-4E(u)-C(u).
\]

Using the three kernels in (168jp), direct differentiation gives the exact
cancellation

\[
 \boxed{
 F'(u)=e^{-u/2}\frac{u^2(24-u^2)}{96}.
 }                                                    \tag{168kp}
\]

Thus `F(0)=0`, the current is positive up to `sqrt(24)`, and all possible
failure is confined to one remote tail.  Normalize `tau_n` and use its exact
survival function (168jt).  Survival integration gives

\[
 \frac{2A_n-4E_n-C_n}{\tau_n([0,\infty))}
 =\int_0^\infty F'(u)S_a(u)du,
 \qquad a=\pi n^2.                                  \tag{168kq}
\]

This integral is strictly positive uniformly for `a>=3`.  Here is a coarse
fully analytic comparison.  On `0<=u<=1/(4a)`, use

\[
 F'(u)>\frac{u^2}{9},
 \qquad
 S_a(u)>e^{-3au}>\frac13.
\]

Therefore its positive part is larger than

\[
 \frac1{5184a^3}.                                   \tag{168kr}
\]

The negative part begins only beyond `sqrt(24)>4`.  On that ray,

\[
 |F'(u)|S_a(u)
 <\frac{u^4}{96}e^{-(2a-1/2)u}
 <\frac5{96}e^{-(2a-3/2)u},                         \tag{168ks}
\]

where `u^4<5e^u` for `u>=4`.  Hence its absolute mass is less than

\[
 \frac5{96(2a-3/2)}e^{-4(2a-3/2)}.                 \tag{168kt}
\]

At `a=3`, the last expression is below
`5/(432\,2^{18})`, whereas (168kr) is
`1/(5184\cdot27)`; the former is smaller.  Their ratio continues to decrease
for `a>=3`, since the exponential decay dominates the cubic factor.
Consequently (168kq) is positive.  As `a=pi n^2>3` for every theta label,

\[
 \boxed{
 C_n+4E_n<2A_n
 \qquad(n\ge1).
 }                                                    \tag{168ku}
\]

Together with (168km), positivity of `C_n`, and hence
`gamma_n>0`, this places every seam label strictly inside the cone (168ki).
Equations (168kd)--(168kj) now prove the uniform diagonal theorem

\[
 \boxed{
 D_q>0
 \qquad\text{for every integer }q\ge1.
 }                                                    \tag{168kv}
\]

This is the first all-arithmetic result in the Loewner-block program.  Every
completed Dirichlet block is positively oriented at the central diagonal,
independently of its number of divisors.  The mechanism is not an accumulation
of prime cases: modular translation puts every label in a common moment cone,
and multiplicative convolution preserves that cone through the pair identity
(168kj).

The scope remains exact.  Equation (168kv) proves the central diagonal of
each arithmetic block.  It does not yet prove the separated-point Loewner
kernel, positivity throughout `0<x<1/4`, or RH.  The next obstruction is no
longer arithmetic multiplicity; it is propagation of this cone orientation
away from the maximally symmetric diagonal.

## The separated blocks are symplectic divisor chords

There is a canonical two-component object before confluence.  For each
label define

\[
 K_n(x)=\int k_u(x)d\tau_n(u),
 \qquad
 H_n(x)=\int h_u(x)d\tau_n(u),
 \qquad
 v_n(x)=\binom{K_n(x)}{H_n(x)}.                    \tag{168kw}
\]

Equip these columns with the fixed alternating form

\[
 \omega\!\left(\binom{k}{h},\binom{\tilde k}{\tilde h}\right)
 =h\tilde k-k\tilde h.                             \tag{168kx}
\]

Then the integrated two-seam kernel is exactly

\[
 \mathscr Q[\tau_m,\tau_n](x,y)
 =\frac{
 \omega(v_m(x),v_n(y))+
 \omega(v_n(x),v_m(y))
 }{2(y-x)}.                                        \tag{168ky}
\]

The linear carrier edge has the same form.  Introduce the fixed null-mode
column

\[
 v_0(x)=\binom{-1}{0}.
\]

Then

\[
 \mathscr E[\tau_q](x,y)
 =\frac{
 \omega(v_0(x),v_q(y))+
 \omega(v_q(x),v_0(y))
 }{y-x}.                                           \tag{168kz}
\]

Consequently every completed block is one oriented symplectic chord sum:

\[
 \boxed{
 \mathscr B_q(x,y)=\frac1{y-x}
 \left[
 \omega(v_0(x),v_q(y))+
 \omega(v_q(x),v_0(y))
 +\frac12\sum_{mn=q}
 \bigl(
 \omega(v_m(x),v_n(y))+
 \omega(v_n(x),v_m(y))
 \bigr)
 \right].
 }                                                    \tag{168la}
\]

This identifies the faithful separated-point generalization of the moment
cone.  It is not a collection of scalar inequalities in `x` and `y`; it is
coherent orientation of the transported two-plane columns `v_n(x)` under the
single alternating form (168kx).  The carrier is not an exceptional extra
term: it is the distinguished boundary column `v_0` completing the divisor
incidence.

Taking `y->x` turns each chord into a Wronskian.  At `x=0`, those Wronskians
reduce exactly to the three moments `E_n,A_n,C_n`; hence (168kv) is the
confluent shadow of (168la), not an unrelated diagonal estimate.  The
remaining theorem can now be stated without coordinates:

\[
 \boxed{
 \text{theta scale transport must preserve the symplectic orientation of
 every completed divisor chord.}
 }                                                    \tag{168lb}
\]

This supplies a sharper falsifier than a generic Loewner determinant.  The
first failure must be either:

1. a label column `v_n(x)` crossing the oriented carrier cone;
2. a factor-pair chord reversing orientation under `x<y`; or
3. individually coherent chords whose completed divisor sum loses matrix
   positivity.

Only the third is genuinely higher-rank.  The first two are two-dimensional
transport questions and should be attacked before any further spectral
matrix census.

## Theta labels have a globally coherent column orientation

The first two-dimensional transport question admits an exact answer.  The
atomic response kernel has the integral representation

\[
 \boxed{
 k_u(x)=2a_x\int_0^u e^{-t/2}\cosh(\sqrt{x}\,t)dt,
 \qquad a_x=\frac14-x.
 }                                                    \tag{168lc}
\]

Indeed, differentiating (168in) with respect to `u` gives

\[
 \partial_uk_u(x)=2a_xe^{-u/2}\cosh(\sqrt{x}\,u),
 \qquad k_0(x)=0.                                   \tag{168ld}
\]

The kernel `cosh(st)` is strictly TP2 for `s,t>0`: its logarithmic
cross-derivative is

\[
 \partial_s\partial_t\log\cosh(st)
 =\tanh(st)+st\operatorname{sech}^2(st)>0.          \tag{168le}
\]

Positive integration over the nested interval `[0,u]` preserves TP2, and
the monotone change `s=sqrt(x)` together with multiplication by `2a_x`
does not change its minors.  Therefore

\[
 \boxed{k_u(x)\text{ is strictly TP2 in }(x,u).}    \tag{168lf}
\]

The theta transport has the opposite order.  Normalize `tau_n` and write
`a=pi n^2`.  Its density, up to an `a`-dependent positive factor, is

\[
 p_a(u)\propto
 e^u(2ae^{2u}-1)e^{-a(e^{2u}-1)}.                  \tag{168lg}
\]

For `y=e^{2u}`,

\[
 \frac{d}{dy}\partial_a\log p_a
 =-1-\frac2{(2ay-1)^2}<0.                          \tag{168lh}
\]

Thus the family is strictly reverse-MLR ordered: increasing the label
parameter `a` moves the seam law toward smaller `u`.  Composing this
reverse-TP2 family with the TP2 kernel (168lf) reverses the spectral minors.
Equivalently, a direct two-copy determinant integral proves that for
`m<n` and `0<=x<y<1/4`,

\[
 \boxed{
 K_m(x)K_n(y)-K_m(y)K_n(x)<0.
 }                                                    \tag{168li}
\]

In ratio form,

\[
 \boxed{
 \frac{K_m(y)}{K_m(x)}>\frac{K_n(y)}{K_n(x)}
 \qquad(m<n,\ x<y).
 }                                                    \tag{168lj}
\]

Confluence at `y=x` gives

\[
 \partial_x\log K_m(x)>partial_x\log K_n(x)
 \qquad(m<n).                                      \tag{168lk}
\]

Since `H_n=a_xK_n'`, the same-point symplectic orientation is therefore

\[
\begin{aligned}
 \omega(v_m(x),v_n(x))
 &=a_xK_m(x)K_n(x)
 \left(partial_x\log K_m-partial_x\log K_n\right)\\
 &>0
 \qquad(m<n).                                      \tag{168ll}
\end{aligned}
\]

This eliminates the first failure mode following (168lb): no pair of theta
label columns crosses anywhere in the central spectral interval.  Their
orientation is fixed by the opposition between spectral TP2 and arithmetic
reverse MLR, not by a finite label census.

The result is stronger than the central moment cone in one direction and
weaker in another.  It holds for every `x` in the full interval and every
label pair, but it controls columns at a common spectral point.  The live
two-point question is the polarization of (168ll): whether the completed
combination in (168la), with columns evaluated at `x` and `y`, retains the
same orientation.  That is now the only remaining two-dimensional defect;
after it, any failure must be genuinely higher-rank.

## Polarization is contraction in the logarithmic spectral coordinate

The coefficient `a_x` in the response selects the correct coordinate.  Put

\[
 \xi=-\log a_x,
 \qquad
 x=\frac14-e^{-\xi}.
\]

Then

\[
 \boxed{H_n(x)=a_xK_n'(x)=\partial_\xi K_n(\xi).}   \tag{168lm}
\]

For a factor pair define the symmetric product

\[
 P_{m,n}(\xi,\zeta)
 =K_m(\xi)K_n(\zeta)+K_n(\xi)K_m(\zeta).           \tag{168ln}
\]

Formula (168ky) becomes

\[
 \boxed{
 \mathscr Q[\tau_m,\tau_n](x,y)
 =\frac{(\partial_\xi-\partial_\zeta)
 P_{m,n}(\xi,\zeta)}{2(y-x)}.
 }                                                    \tag{168lo}
\]

Now write

\[
 c=\frac{\xi+\zeta}{2},
 \qquad
 d=\frac{\zeta-\xi}{2}>0.
\]

Since `partial_xi-partial_zeta=-partial_d`,

\[
 \boxed{
 \mathscr Q[\tau_m,\tau_n](x,y)
 =-\frac{\partial_dP_{m,n}(c-d,c+d)}{2(y-x)}.
 }                                                    \tag{168lp}
\]

Thus a two-seam factor pair is positively oriented exactly when its
symmetric response product contracts as the logarithmic spectral gap opens.
For a repeated label this reduces further:

\[
 P_{n,n}(c-d,c+d)=2K_n(c-d)K_n(c+d),                \tag{168lq}
\]

so log-concavity of `K_n` in `xi` is sufficient and, infinitesimally,
necessary for self-pair orientation.

For distinct labels, the reverse-TP2 theorem (168lj) supplies the ordered
logarithmic slopes.  The remaining pair theorem is therefore sharply
factored into:

\[
 \boxed{
 \begin{array}{c}
 \log K_n(\xi)\text{ concave for every }n,\\[2mm]
 \text{the reverse-TP2 slope order is preserved under symmetric
 polarization.}
 \end{array}
 }                                                    \tag{168lr}
\]

This is the correct successor to the central moment cone.  The diagonal
inequalities (168ku)--(168kv) are precisely the first confluent tests of this
gap-contraction law.  A failure of log-concavity for one exact theta label
would immediately falsify positive orientation of its self-pair block; a
proof of (168lr) would orient every quadratic divisor chord before any
higher-rank Loewner argument.

## Self-pair contraction is an exact coefficient-variance bound

The first line of (168lr) has a discrete source formulation.  Expanding
(168lc) gives

\[
 K_n(x)=2a_xF_n(x),
 \qquad
 F_n(x)=\sum_{j\ge0}b_{j,n}x^j,                    \tag{168ls}
\]

with strictly positive coefficients

\[
 \boxed{
 b_{j,n}=\frac1{(2j)!}
 \int_0^\infty e^{-t/2}t^{2j}
 \tau_n([t,\infty))dt.
 }                                                    \tag{168lt}
\]

For fixed `x>0`, define the canonical probability law

\[
 \mathbb P_{n,x}(J=j)=\frac{b_{j,n}x^j}{F_n(x)}.
                                                               \tag{168lu}
\]

Writing `L_n=log F_n`, the standard power-series identities are

\[
 xL_n'(x)=\mathbb E[J],
 \qquad
 x^2L_n''(x)=\operatorname{Var}(J)-\mathbb E[J].    \tag{168lv}
\]

Because `x=1/4-a` and `partial_xi=a partial_x`, while `log(2a)` is affine
in `xi`, one obtains

\[
 \partial_\xi^2\log K_n
 =a^2L_n''-aL_n'.                                   \tag{168lw}
\]

Substitution of (168lv), using `a+x=1/4`, yields the exact equivalence

\[
 \boxed{
 \log K_n(\xi)\text{ is concave}
 \quad\Longleftrightarrow\quad
 4a_x\operatorname{Var}_{n,x}(J)
 \le\mathbb E_{n,x}[J].
 }                                                    \tag{168lx}
\]

This is not a normalization-dependent Hankel determinant.  `J` is the
actual even-factorial mode selected by the source tail (168lt), and the
factor `4a_x` is the remaining distance to the critical boundary.  The
three regimes have direct meanings:

\[
 \begin{array}{c|c}
 4a\operatorname{Var}(J)<\mathbb E[J]&
 \text{strict self-pair contraction},\\
 4a\operatorname{Var}(J)=\mathbb E[J]&
 \text{a null symplectic direction},\\
 4a\operatorname{Var}(J)>\mathbb E[J]&
 \text{an exact self-pair orientation failure}.
 \end{array}                                        \tag{168ly}
\]

The boundary behavior is structurally consistent.  As `x->1/4`, `a->0`,
so every finite variance automatically lies on the contracting side.  At
`x->0`, the law concentrates at `J=0` and the leading inequality is
critical because `4a->1` and `Var(J)~E[J]`; the first nontrivial correction
is exactly the central moment-cone reserve already proved in (168ku).

A familiar sufficient condition is under-dispersion,

\[
 \operatorname{Var}(J)\le\mathbb E[J],             \tag{168lz}
\]

because `4a<=1`.  For a single fixed tail coordinate, the even-factorial
weights come from an even-Poisson law and have precisely this repulsive
shape.  But (168lt) is a theta mixture over tail coordinates, and arbitrary
mixtures can create over-dispersion.  Therefore the remaining self-pair
theorem is sharply arithmetic: prove that the superexponentially ordered
theta tail preserves enough under-dispersion to satisfy (168lx), or exhibit
the first exact `(n,x)` where it fails.

This variance criterion is the coefficient-level form of the same
symplectic orientation, not a new independent RH route.

## A Gaussian moment-ratio criterion for the whole self-pair theorem

The exact survival function removes the last abstraction from (168lt).  Up
to the positive label factor `2n`, put

\[
 M_{r}(a)=\int_0^\infty
 t^r e^{t/2-ae^{2t}}dt,
 \qquad a=\pi n^2.                                  \tag{168ma}
\]

Then

\[
 b_{j,n}=\frac{2n}{(2j)!}M_{2j}(a).                \tag{168mb}
\]

A positive power-series distribution is ultra-log-concave relative to the
Poisson law if

\[
 j b_j^2\ge(j+1)b_{j-1}b_{j+1}qquad(j\ge1).       \tag{168mc}
\]

Ultra-log-concavity implies `Var(J)<=E[J]`, and therefore proves (168lx)
for every `x` at once.  Substituting (168mb) into (168mc) cancels all
factorials and yields the remarkably simple source condition

\[
 \boxed{
 \frac{M_{2j-2}(a)M_{2j+2}(a)}{M_{2j}(a)^2}
 \le\frac{2j+1}{2j-1}
 \qquad(a\ge\pi,\ j\ge1).
 }                                                    \tag{168md}
\]

The right side is exactly the adjacent even-moment ratio of a centered
Gaussian.  Thus the proposed theorem has a hard-to-vary meaning:

\[
 \boxed{
 \text{the completed theta tail is no more moment-dispersed than a
 Gaussian at every even order.}
 }                                                    \tag{168me}
\]

The source density has the correct rigidity:

\[
 \frac{d^2}{dt^2}\log\left(e^{t/2-ae^{2t}}\right)
 =-4ae^{2t}\le-4a.                                  \tag{168mf}
\]

So it is uniformly more strongly log-concave than a Gaussian of curvature
`4a`, with an additional boundary tilt toward `t=0`.  Mere log-concavity
would not imply (168md), but (168mf) identifies the exact comparison
principle to seek: a one-sided strong-log-concavity moment-ratio theorem.

This creates a decisive analytic fork.  Proving (168md) closes every
self-pair chord and all `x` simultaneously.  Falsifying it at one `(a,j)`
does not yet falsify (168lx), because ultra-log-concavity is sufficient rather
than necessary; it would instead show that the direct Gaussian-comparison
explanation is too strong.  The faithful fallback would remain the weighted
variance inequality (168lx), not numerical block scouting.

## The Gaussian comparison is analytically false: the seam is exponential

The fork can be decided without computation.  Fix `r` and let the label
parameter `a` tend to infinity.  Put

\[
 \lambda_a=2a-\frac12.
\]

After the boundary scaling `t=z/lambda_a`,

\[
 \frac t2-ae^{2t}
 =-a-z+O_a\!\left(\frac{z^2}{a}\right).            \tag{168mg}
\]

Dominated convergence on bounded `z`, followed by the elementary
superexponential tail bound, gives

\[
 \boxed{
 M_r(a)\sim e^{-a}\frac{\Gamma(r+1)}{\lambda_a^{r+1}}
 \qquad(a\to\infty).
 }                                                    \tag{168mh}
\]

Consequently

\[
 \frac{M_{2j-2}M_{2j+2}}{M_{2j}^2}
 \longrightarrow
 \frac{(2j+2)(2j+1)}{(2j)(2j-1)},                  \tag{168mi}
\]

which is strictly larger than the Gaussian target
`(2j+1)/(2j-1)`.  Hence, for every fixed `j`, (168md) fails for all
sufficiently large theta labels.

This is a useful falsification, not a setback to (168lx).  The seam density
is concentrated at the boundary `t=0`; its local model is exponential, not
Gaussian.  Under (168mh), the factorial cancellation in (168mb) gives

\[
 b_{j,n}\asymp\lambda_a^{-2j-1}.                   \tag{168mj}
\]

Thus the coefficient law tends to a geometric distribution with parameter

\[
 r_a=\frac{x}{\lambda_a^2}.
\]

For that law,

\[
 \frac{\operatorname{Var}(J)}{\mathbb E[J]}
 =\frac1{1-r_a}.                                   \tag{168mk}
\]

The faithful condition (168lx) becomes

\[
 \frac{4a_x}{1-r_a}\le1
 \quad\Longleftrightarrow\quad
 r_a\le4x,                                         \tag{168ml}
\]

which holds with a large reserve because `lambda_a^2>1/4`.  Therefore the
labels that falsify Gaussian ultra-log-concavity are driven deeper into the
true contracting cone.

The correct comparison is source-exponential.  In fact the likelihood ratio
against the exponential density of rate `lambda_a` is

\[
 \frac{e^{t/2-ae^{2t}}}{e^{-a}e^{-\lambda_at}}
 =\exp[-a(e^{2t}-1-2t)],                            \tag{168mm}
\]

and is strictly decreasing.  After `r`th size biasing, stochastic domination
by `Gamma(r+1,lambda_a)` yields the exact adjacent bound

\[
 \boxed{
 \frac{M_{r+2}(a)}{M_r(a)}
 \le\frac{(r+1)(r+2)}{\lambda_a^2}.
 }                                                    \tag{168mn}
\]

Equivalently, the coefficient ratios obey

\[
 \boxed{
 \frac{b_{j+1,n}}{b_{j,n}}
 \le\frac1{\lambda_a^2}.
 }                                                    \tag{168mo}
\]

This is the faithful replacement for (168md).  The remaining purely discrete
step is to transfer the uniform ratio envelope (168mo) into the weighted
variance bound (168lx).  The extremal candidate is now geometric, exactly as
the boundary scaling predicts.  Any proof must retain the spectral factor
`4a_x`; discarding it was precisely what made the Gaussian conjecture too
strong.

## Geometric domination proves every self-pair chord

The discrete step uses the log-concavity that survived the failed Gaussian
comparison.  We use two elementary one-dimensional facts.

First, if `w` is log-concave on the positive ray, then its factorially
normalized Mellin moments

\[
 p\longmapsto
 \frac1{\Gamma(p+1)}\int_0^\infty t^p w(t)dt       \tag{168mp}
\]

form a log-concave function of `p>=0`.  This is the normalized-moment lemma;
in one dimension it follows by applying the layer-cake representation to the
nested interval superlevel sets of `w` and Holder interpolation.  Applied at
the even integers to

\[
 w_a(t)=e^{t/2-ae^{2t}},
\]

whose logarithm has negative second derivative by (168mf), it shows that

\[
 \boxed{
 \frac{b_{j+1,n}}{b_{j,n}}
 \text{ is nonincreasing in }j.
 }                                                    \tag{168mq}
\]

Second, let a probability law on the nonnegative integers have successive
mass ratios bounded by `r<1` and nonincreasing.  Its conditional residual
tails are then dominated by those of the geometric law of ratio `r`.
Summation by parts gives the sharp dispersion bound

\[
 \boxed{
 \frac{\operatorname{Var}(J)}{\mathbb E[J]}
 \le\frac1{1-r}.
 }                                                    \tag{168mr}
\]

Equality is attained by the geometric law; finite support or a strict drop
in one ratio makes the inequality strict.

For the coefficient law (168lu), (168mo) and (168mq) give

\[
 \frac{\mathbb P(J=j+1)}{\mathbb P(J=j)}
 =x\frac{b_{j+1,n}}{b_{j,n}}
 \le r_{n,x}:=\frac{x}{\lambda_a^2}.               \tag{168ms}
\]

Therefore

\[
 4a_x\frac{\operatorname{Var}(J)}{\mathbb E[J]}
 \le\frac{4a_x}{1-x/\lambda_a^2}.                  \tag{168mt}
\]

Since `a_x=1/4-x`, the right side is at most one exactly when

\[
 \lambda_a^2\ge\frac14.                            \tag{168mu}
\]

But `lambda_a=2pi n^2-1/2>1/2` for every theta label.  The inequality is
strict for `x>0`; its confluent endpoint reserve at `x=0` was established
directly in the central moment theorem.  Combining with (168lx) proves

\[
 \boxed{
 \partial_\xi^2\log K_n(\xi)<0
 \qquad
 (n\ge1,\ 0<x<1/4).
 }                                                    \tag{168mv}
\]

Equivalently, by (168lp)--(168lq),

\[
 \boxed{
 \mathscr Q[\tau_n,\tau_n](x,y)>0
 \qquad(n\ge1,\ 0<x<y<1/4).
 }                                                    \tag{168mw}
\]

This closes every self-pair divisor chord on the full central interval.
The proof also explains the earlier surprise: Gaussian ultra-log-concavity
was false because it erased the boundary geometry, while geometric
domination is exactly adapted to a seam-supported source.  Strong continuous
log-concavity supplies decreasing coefficient ratios; the arithmetic
exponential envelope supplies their scale; the critical spectral factor
`4a_x` converts that scale into contraction.

The remaining two-dimensional problem is now only the mixed pair `m!=n`.
Its two summands couple different decreasing-ratio towers.  Reverse TP2
orders their logarithmic slopes, while (168mv) makes each slope decrease in
`xi`; the next question is whether these two monotonicities imply contraction
of their symmetric cross product in (168ln).

## Mixed labels form synchronously ordered coefficient towers

The coefficient representation retains the arithmetic order.  Let `m<n`,
and normalize away the positive label masses.  The reverse-MLR calculation
(168lh) says that the `n`th tail density divided by the `m`th tail density is
strictly decreasing in `t`.  Size biasing by `t^{2j}` therefore gives

\[
 \frac{M_{2j}(\pi n^2)}{M_{2j}(\pi m^2)}
 \text{ strictly decreasing in }j.                 \tag{168mx}
\]

The common factorial in (168mb) does not affect the comparison, so

\[
 \boxed{
 \frac{b_{j,n}}{b_{j,m}}
 \text{ is strictly decreasing in }j
 \qquad(m<n).
 }                                                    \tag{168my}
\]

Equivalently, every adjacent coefficient minor has the fixed sign

\[
 \boxed{
 b_{j,m}b_{j+1,n}-b_{j+1,m}b_{j,n}<0.
 }                                                    \tag{168mz}
\]

Together, (168mq) and (168mz) say that the theta towers are synchronously
log-concave and reverse-TP2 in `(j,n)`.  This is stronger than either of the
continuous statements used separately:

* (168mq) prevents a single label tower from developing a late factorial
  burst;
* (168mz) prevents two label towers from exchanging their mode order;
* (168mo) gives the common geometric envelope.

At a fixed spectral point, the induced laws

\[
 P_{n,x}(j)=\frac{b_{j,n}x^j}{F_n(x)}              \tag{168na}
\]

are therefore reverse-MLR ordered in `n`.  In particular every increasing
function of `J` has smaller expectation at larger theta label.  The first
moment recovers the ordered logarithmic slopes in (168lk); all higher mode
responses are ordered simultaneously.

This identifies the exact discrete theorem needed for mixed contraction.
It is no longer permissible to treat `K_m` and `K_n` as arbitrary concave
functions.  They arise from two log-concave coefficient laws with decreasing
successive ratios, a fixed MLR order, and the common activity bound

\[
 x\frac{b_{j+1,n}}{b_{j,n}}
 \le\frac{x}{(2\pi n^2-1/2)^2}.                    \tag{168nb}
\]

The remaining polarization lemma is purely discrete:

\[
 \boxed{
 \begin{array}{c}
 \text{Do synchronized reverse-TP2 geometric towers force}\\
 F_m(x_-)F_n(x_+)+F_n(x_-)F_m(x_+)\\
 \text{to contract under the canonical symmetric }\xi\text{-separation?}
 \end{array}
 }                                                    \tag{168nc}
\]

For unrestricted log-concave functions the answer need not be yes.  The
coefficient synchronization (168mz) is the additional theta datum that must
do the work.  A proof of (168nc) closes all mixed quadratic chords; a
counterexample satisfying (168mq), (168mz), and (168nb) would show that even
this discrete source order is insufficient and that positivity occurs only
after completed divisor summation.

## The first mixed obstruction is a curvature-versus-shear inequality

The infinitesimal form of (168nc) reveals why separate concavity and label
ordering are not enough.  Put

\[
 \ell_n(\xi)=\log K_n(\xi)
\]

and expand the symmetric product (168ln) about zero gap.  The odd terms
cancel, and direct differentiation gives

\[
\begin{aligned}
 &\left.\partial_dP_{m,n}(c-d,c+d)\right|_{d=0}=0,\\
 &\frac{
 \left.\partial_d^2P_{m,n}(c-d,c+d)\right|_{d=0}
 }{2K_m(c)K_n(c)}\\
 &\hspace{20mm}=
 \ell_m''(c)+\ell_n''(c)
 +\bigl(\ell_m'(c)-\ell_n'(c)\bigr)^2.             \tag{168nd}
\end{aligned}
\]

Therefore local mixed contraction requires

\[
 \boxed{
 -\ell_m''(\xi)-\ell_n''(\xi)
 \ge
 \bigl(\ell_m'(\xi)-\ell_n'(\xi)\bigr)^2.
 }                                                    \tag{168ne}
\]

The left side is the sum of the two self-pair coercivity reserves proved
positive in (168mv).  The right side is the square of the arithmetic shear
between the label columns.  This is the first genuinely coupled positivity
condition: neither self-pair theorem alone can imply it.

In the coefficient laws (168na), write

\[
 \mu_n=\mathbb E_{n,x}[J],
 \qquad
 v_n=\operatorname{Var}_{n,x}(J).
\]

Since

\[
 \ell_n'=-1+\frac{a_x}{x}\mu_n,                    \tag{168nf}
\]

and (168lw) gives

\[
 -\ell_n''
 =\frac{a_x}{4x^2}\bigl(\mu_n-4a_xv_n\bigr),      \tag{168ng}
\]

condition (168ne) becomes the exact probability inequality

\[
 \boxed{
 \frac{a_x}{4x^2}
 \left[
 \mu_m+\mu_n-4a_x(v_m+v_n)
 \right]
 \ge
 \frac{a_x^2}{x^2}(\mu_m-\mu_n)^2.
 }                                                    \tag{168nh}
\]

After cancelling the positive common factor, the coupled reserve is

\[
 \boxed{
 \mu_m+\mu_n-4a_x(v_m+v_n)
 \ge4a_x(\mu_m-\mu_n)^2.
 }                                                    \tag{168ni}
\]

This is now the smallest faithful mixed-label theorem.  The geometric
envelope controls each variance term, while reverse MLR controls the mean
difference.  Their reserves must be compared rather than proved separately.
The sharp local falsifier is any exact `(m,n,x)` violating (168ni); such a
failure would show that individual factor-pair orientation is too strong,
without yet falsifying positivity of the completed divisor block.

Conceptually, the identity is the same architecture seen at level 44:

\[
 \boxed{
 \text{two positive self reserves}
 -\text{one rank-one arithmetic shear square}.
 }                                                    \tag{168nj}
\]

The mixed problem has therefore ceased to be a vague polarization question.
It is one scalar secular inequality at every source-derived pair and spectral
coordinate.

## The coupled secular inequality is uniformly positive

The same geometric envelope that proved the self-pair theorem also controls
the shear.  Put

\[
 r_n=\frac{x}{\lambda_n^2},
 \qquad
 \lambda_n=2\pi n^2-\frac12.
\]

From (168mr)--(168ms),

\[
 v_n\le\frac{\mu_n}{1-r_n},
 \qquad
 \mu_n\le\frac{r_n}{1-r_n}.                        \tag{168nk}
\]

The first inequality gives the individual reserve bound

\[
 \mu_n-4a_xv_n
 \ge
 \mu_n\frac{4x-r_n}{1-r_n}.                        \tag{168nl}
\]

But

\[
\begin{aligned}
 \frac{4x-r_n}{1-r_n}-4a_x\mu_n
 &\ge
 \frac{4x-r_n-4a_xr_n}{1-r_n}\\
 &=\frac{4x-(1+4a_x)r_n}{1-r_n}\\
 &\ge
 \frac{x(4-2/\lambda_n^2)}{1-r_n}>0,               \tag{168nm}
\end{aligned}
\]

because `1+4a_x=2-4x<=2` and `lambda_n^2>1/2`.  Hence every label satisfies
the stronger nonlinear estimate

\[
 \boxed{
 \mu_n-4a_xv_n>4a_x\mu_n^2.
 }                                                    \tag{168nn}
\]

For `m<n`, reverse MLR gives `mu_m>mu_n>=0`.  Therefore the `m`th reserve
alone controls the full arithmetic shear:

\[
\begin{aligned}
 &\mu_m+\mu_n-4a_x(v_m+v_n)\\
 &\quad>4a_x(\mu_m^2+\mu_n^2)\\
 &\quad\ge4a_x(\mu_m-\mu_n)^2.                    \tag{168no}
\end{aligned}
\]

This proves (168ni), strictly, for every pair of theta labels and every
`0<x<1/4`.  Equivalently,

\[
 \boxed{
 \ell_m''+\ell_n''+(\ell_m'-\ell_n')^2<0.
 }                                                    \tag{168np}
\]

Thus every mixed symmetric product begins by contracting when a spectral
gap opens.  The result is uniform in the labels; no divisor census enters.
It is also stronger than a balanced two-channel repair: each self reserve
already dominates its own squared mean, so their sum controls the difference
square automatically.

The remaining distinction is global in the gap.  Equation (168np) proves
strict contraction at `d=0` for every center.  To deduce
`partial_dP_{m,n}<0` for arbitrary `d>0`, the coupled inequality must be
transported along the opening gap.  The natural target is preservation of
(168np) under the synchronized coefficient flow, or an integrated Jacobi-
field identity whose derivative is the negative secular reserve (168no).

## Exact integrated secular criterion for arbitrary gaps

The global propagation problem has a scalar closed form.  Let

\[
 A=\ell_m',
 \qquad B=\ell_n',
 \qquad u=A-B>0,
 \qquad v=-(A'+B')>0,                              \tag{168nq}
\]

and write the two endpoints as `xi_-<xi_+`.  Set

\[
 \mathcal H=\int_{\xi_-}^{\xi_+}u(s)ds,
 \qquad
 \mathcal V=\frac12\int_{\xi_-}^{\xi_+}v(s)ds,
 \qquad
 \mathcal U=\frac{u(\xi_-)+u(\xi_+)}2.             \tag{168nr}
\]

The two cross products in (168ln) have ratio

\[
 \frac{K_n(\xi_-)K_m(\xi_+)}
 {K_m(\xi_-)K_n(\xi_+)}=e^{\mathcal H}.             \tag{168ns}
\]

Moreover

\[
\begin{aligned}
 A(\xi_-)-B(\xi_+)&=\mathcal V+\mathcal U,\\
 A(\xi_+)-B(\xi_-)&=\mathcal U-\mathcal V.         \tag{168nt}
\end{aligned}
\]

Substitution into the exact gap derivative gives

\[
 \partial_dP_{m,n}
 =T_-\left[
 e^{\mathcal H}(\mathcal U-\mathcal V)
 -(\mathcal U+\mathcal V)
 \right],                                          \tag{168nu}
\]

where `T_->0` is the first cross product.  Hence arbitrary-gap contraction
is equivalent to

\[
 \boxed{
 \frac{\mathcal V}{\mathcal U}
 \ge\tanh\left(\frac{\mathcal H}{2}\right).
 }                                                    \tag{168nv}
\]

If `mathcal V>=mathcal U`, contraction is automatic; the formula remains
valid and its content is only needed in the near-shear regime
`mathcal V<mathcal U`.

The infinitesimal limit recovers the coupled theorem exactly.  On an interval
of length `2d`,

\[
 \mathcal H\sim2du,
 \qquad
 \mathcal V\sim dv,
 \qquad
 \mathcal U\sim u,
\]

so (168nv) reduces to `v>=u^2`, which is (168np).

This is the desired integrated Jacobi-field identity.  It separates the
three relevant quantities without coordinates:

\[
 \boxed{
 \text{accumulated self curvature }\mathcal V,
 \quad
 \text{endpoint shear }\mathcal U,
 \quad
 \text{holonomy }\mathcal H.
 }                                                    \tag{168nw}
\]

The remaining theorem is no longer “extend a local inequality somehow.”
It is the precise transport bound (168nv).  Since `tanh z<=z`, a sufficient
but stronger form is

\[
 \boxed{
 \int_{\xi_-}^{\xi_+}v(s)ds
 \ge
 \frac{u(\xi_-)+u(\xi_+)}2
 \int_{\xi_-}^{\xi_+}u(s)ds.
 }                                                    \tag{168nx}
\]

This says that the `u`-weighted mean shear does not fall below its endpoint
mean.  The synchronized coefficient flow must now be tested against this
single integral inequality.  Unlike a separated Loewner census, either its
proof or its first analytic counterexample explains the fate of every mixed
factor-pair chord.

## Riccati comparison closes arbitrary mixed gaps

The transport bound follows from the nonlinear reserve already proved.
Define the positive activity slopes

\[
 \alpha=\ell_m'+1=\frac{a_x}{x}\mu_m,
 \qquad
 \beta=\ell_n'+1=\frac{a_x}{x}\mu_n.               \tag{168ny}
\]

For `m<n`, reverse MLR gives `0<beta<alpha`.  Both decrease by the self-pair
theorem.  More strongly, (168nn) and (168ng) imply

\[
 \boxed{
 -\alpha'(\xi)>\alpha(\xi)^2,
 \qquad
 -\beta'(\xi)>\beta(\xi)^2.
 }                                                    \tag{168nz}
\]

Let subscripts `-` and `+` denote the two endpoints.  From (168nt),

\[
 \mathcal U-\mathcal V=\alpha_+-\beta_-.
                                                               \tag{168oa}
\]

If `alpha_+<=beta_-`, then `mathcal V>=mathcal U` and contraction is
automatic.  Suppose instead that `alpha_+>beta_-`.  Integrating the first
Riccati inequality gives

\[
\begin{aligned}
 \mathcal H
 &=\int_{\xi_-}^{\xi_+}(\alpha-\beta)d\xi\\
 &<\int_{\xi_-}^{\xi_+}\alpha d\xi\\
 &<\log\frac{\alpha_-}{\alpha_+}.                  \tag{168ob}
\end{aligned}
\]

Since both activities are positive and decreasing,
`alpha_- beta_->alpha_+ beta_+`, and therefore

\[
 \frac{\alpha_-}{\alpha_+}
 \le
 \frac{\alpha_- -\beta_+}{\alpha_+-\beta_-}.      \tag{168oc}
\]

Combining (168ob)--(168oc) yields

\[
 e^{\mathcal H}(\alpha_+-\beta_-)
 <\alpha_- -\beta_+.                               \tag{168od}
\]

By (168nt), this is exactly the strict form of (168nu).  Hence

\[
 \boxed{
 \partial_dP_{m,n}(c-d,c+d)<0
 \qquad(m\ne n,\ d>0).
 }                                                    \tag{168oe}
\]

Together with (168mw), this proves the full chord theorem

\[
 \boxed{
 \mathscr Q[\tau_m,\tau_n](x,y)>0
 \qquad(m,n\ge1,\ 0<x<y<1/4).
 }                                                    \tag{168of}
\]

The mechanism is source-rigid: geometric domination produces a Riccati
barrier for each activity slope, and ordered positive slopes cannot acquire
enough holonomy to reverse their endpoint chord.

This closes both two-dimensional failure modes following (168lb).  Every
label column is coherently oriented, and every self or mixed factor-pair
chord is positive at arbitrary separation.  The remaining blockwise burden
is the carrier edge `mathscr E[tau_q]` and genuinely higher-rank positive-
semidefiniteness; entrywise positivity of all quadratic chords alone implies
neither.

## Every carrier edge is positive at separated points

The remaining entrywise carrier question also follows from the geometric
envelope.  From `K_n=2a_xF_n` and `H_n=partial_xi K_n`, direct differentiation
gives

\[
 \boxed{
 H_n'(x)=2F_n(x)
 \left[
 1-\frac{3a_x}{x}\mu_n
 +\frac{a_x^2}{x^2}\mathbb E[J(J-1)]
 \right].
 }                                                    \tag{168og}
\]

The factorial-moment term is nonnegative.  From geometric domination,

\[
 \frac{\mu_n}{x}
 \le\frac1{\lambda_n^2-x}.                         \tag{168oh}
\]

Therefore

\[
 \frac{H_n'(x)}{2F_n(x)}
 \ge1-\frac{3a_x}{\lambda_n^2-x}.                  \tag{168oi}
\]

For every label, `lambda_n>=2pi-1/2>11/2`; hence

\[
 \frac{3a_x}{\lambda_n^2-x}
 <\frac{3/4}{30}<1.                                \tag{168oj}
\]

Thus

\[
 \boxed{H_n'(x)>0\qquad(n\ge1,\ 0<x<1/4).}        \tag{168ok}
\]

Taking divided differences proves

\[
 \boxed{
 \mathscr E[\tau_n](x,y)>0
 \qquad(n\ge1,\ 0<x<y<1/4).
 }                                                    \tag{168ol}

Combining (168of) and (168ol), every completed arithmetic block is strictly
positive entrywise throughout the central interval:

\[
 \boxed{
 \mathscr B_q(x,y)>0
 \qquad(q\ge1,\ 0<x<y<1/4).
 }                                                    \tag{168om}

This extends the all-`q` diagonal theorem (168kv) to arbitrary pairs of
spectral points.  It is still not Loewner-matrix positivity: a kernel may be
positive entrywise while possessing a negative higher-rank direction.  The
two-dimensional source geometry is now completely oriented, so any remaining
failure must be a genuinely collective spectral-packet effect.

## The first collective obstruction is exactly the Schwarzian numerator

For the full kernel, multiplication by the positive factors
`1-eta(x_i)` is a diagonal congruence.  Hence positive semidefiniteness of
`mathscr L_eta` is equivalent to that of the ordinary Loewner kernel

\[
 L_H(x,y)=\frac{H(y)-H(x)}{y-x}.                    \tag{168on}
\]

After entrywise orientation, the smallest genuinely collective packet has
two nearby spectral points `x` and `x+epsilon`.  Its determinant expands as

\[
\begin{aligned}
 &\det
 \begin{pmatrix}
 H'(x)&L_H(x,x+\varepsilon)\\
 L_H(x,x+\varepsilon)&H'(x+\varepsilon)
 \end{pmatrix}\\
 &\qquad=
 \frac{\varepsilon^2}{12}
 \left(2H'H'''-3(H'')^2\right)(x)
 +O(\varepsilon^3).                                \tag{168oo}
\end{aligned}
\]

Thus the first surviving higher-rank condition is

\[
 \boxed{
 2H'(x)H'''(x)-3H''(x)^2\ge0.
 }                                                    \tag{168op}
\]

When `H'>0`, this is exactly nonnegativity of the Schwarzian derivative,

\[
 S(H)=\frac{H'''}{H'}-\frac32\left(\frac{H''}{H'}\right)^2.
                                                               \tag{168oq}
\]

This identifies the status of the earlier Schwarzian lane.  It was not an
independent analytic coincidence: it is the confluent rank-two obstruction
that necessarily remains after every one-point and pair-chord source
orientation has been removed.  Agreement between the two formulations is
therefore one structural identity, not two pieces of evidence.

The research frontier is correspondingly sharp:

\[
 \boxed{
 \text{source-oriented one- and two-chord geometry}
 \longrightarrow
 \text{rank-two Schwarzian positivity}
 \longrightarrow
 \text{higher Loewner packets}.
 }                                                    \tag{168or}
\]

The next attack should expand (168op) in the same coefficient laws
`P_{n,x}`.  The aim is a coupled third-cumulant inequality with the already
proved geometric envelope supplying its comparison scale.  Rechecking
finite spectral matrices before deriving that identity would discard the
source reduction just obtained.

## Schwarzian positivity is shape-two dispersion

Put

\[
 Y(x)=H'(x)>0.
\]

The Schwarzian numerator has the elementary square-root form

\[
 \boxed{
 \left(Y^{-1/2}\right)''
 =-\frac{2YY''-3(Y')^2}{4Y^{5/2}}.
 }                                                    \tag{168os}
\]

Thus the first collective Loewner condition is exactly

\[
 \boxed{Y^{-1/2}\text{ is concave}.}               \tag{168ot}
\]

This explains the distinguished exponent two in the proposed Stieltjes
representation.  A single order-two resolvent atom has

\[
 Y(x)=\frac{c}{(r+x)^2},
\]

so `Y^{-1/2}` is affine and (168op) is saturated.  For a positive mixture,

\[
 Y=M_2,
 \qquad
 Y'=-2M_3,
 \qquad
 Y''=6M_4,
\]

where `M_k=int c(r+x)^{-k}dnu(r)`.  Therefore

\[
 2YY''-3(Y')^2
 =12(M_2M_4-M_3^2)\ge0                             \tag{168ou}
\]

by Cauchy--Schwarz.  Schwarzian positivity is precisely the first variance
shadow of an order-two positive resolvent measure.

There is an equivalent coefficient statement in the coordinate oriented
toward the negative Stieltjes cut.  Put `z=-x` (or translate this coordinate
at another base point), and suppose the source expansion

\[
 \widetilde Y(z)=Y(-z)=\sum_{j\ge0}c_jz^j,
 \qquad c_j\ge0,                                   \tag{168ov}
\]

is available, and define

\[
 \mathbb P_z(J=j)=\frac{c_jz^j}{\widetilde Y(z)}.
\]

Writing `mu=E[J]` and `v=Var(J)`, logarithmic differentiation gives

\[
 \frac{2\widetilde Y\widetilde Y''-3(\widetilde Y')^2}
 {\widetilde Y^2}
 =\frac{2v-\mu^2-2\mu}{z^2}.                       \tag{168ow}
\]

Hence

\[
 \boxed{
 2\operatorname{Var}(J)
 \ge\mathbb E[J]^2+2\mathbb E[J].
 }                                                    \tag{168ox}
\]

Equality is the negative-binomial law of shape two, whose generating
function is `(1-rx)^{-2}`.  Positive mixtures of order-two atoms create the
additional variance in (168ou).

This reverses the role played by dispersion in the one-label chord theorem:

\[
 \begin{array}{c|c}
 K_n\text{ self chord}&
 \text{geometric upper envelope prevents excessive dispersion},\\
 H'\text{ collective rank two}&
 \text{shape-two lower envelope requires sufficient dispersion}.
 \end{array}                                        \tag{168oy}
\]

There is no contradiction.  The first law concerns one transported seam
channel; the second concerns the completed response after carrier and all
pair interactions.  Their coupling must create exactly the extra
negative-binomial dispersion.  This is the coefficient meaning of
“positive self reserves plus a source-fixed repair.”

The sharp next theorem is therefore not an untyped third-cumulant estimate.
It is:

\[
 \boxed{
 \text{derive a nonnegative coefficient expansion for }H'
 \text{ whose mode law dominates the shape-two dispersion floor.}
 }                                                    \tag{168oz}
\]

Failure of coefficient positivity would not by itself falsify Schwarzian
positivity, because (168ov) is a chosen coordinate.  Failure of the invariant
concavity (168ot), however, is the exact rank-two falsifier.

## Shape-two normalization exposes the Stieltjes tower

For an order-two resolvent mixture in the cut-oriented coordinate,

\[
 \widetilde Y(z)
 =\int_0^\infty\frac{d\nu(r)}{(r-z)^2}
 =\sum_{j\ge0}(j+1)
 \left(\int_0^\infty r^{-j-2}d\nu(r)\right)z^j.    \tag{168pa}
\]

Therefore the canonical normalization is

\[
 \boxed{d_j=\frac{c_j}{j+1}.}                      \tag{168pb}
\]

The desired order-two representation says precisely that `d_j` is a
Stieltjes moment sequence.  At the first nontrivial order,

\[
 d_0d_2-d_1^2\ge0
 \quad\Longleftrightarrow\quad
 \boxed{4c_0c_2-3c_1^2\ge0}.                       \tag{168pc}
\]

But the right side is exactly the Schwarzian numerator at `z=0`, since

\[
 2\widetilde Y(0)\widetilde Y''(0)
 -3\widetilde Y'(0)^2
 =4c_0c_2-3c_1^2.                                  \tag{168pd}
\]

Thus the Schwarzian condition is literally the first Hankel minor of the
shape-two-normalized response tower.  Higher Loewner packet conditions are
not unrelated inequalities; they are the higher Hankel and localizing
constraints of the same normalized sequence.

This gives the cleanest current formulation of the RH lane:

\[
 \boxed{
 \text{derive the coefficients }c_j\text{ from the completed theta source,}
 \quad
 \text{then prove }\left\{\frac{c_j}{j+1}\right\}_{j\ge0}
 \text{ is a Stieltjes moment sequence.}
 }                                                    \tag{168pe}
\]

The division by `j+1` is not fitted normalization.  It is forced by the
order-two resolvent kernel, just as the factor `4a_x` was forced by the
critical spectral coordinate in the chord theorem.  This also specifies the
necessary support audit: Hankel positivity controls existence of a positive
measure, while the shifted/localizing tower must place that measure on the
correct negative quotient ray.

## Exact source formula for the shape-two coefficients

The coefficients in (168pe) can be derived without invoking zeros.  Work at
the central base point and use the cut-oriented variable `z=-x`.  Put

\[
 Z(z)=1-\eta(-z),
 \qquad
 L(z)=\log Z(z)=\sum_{k\ge0}\ell_kz^k.              \tag{168pf}
\]

Since `a_x=1/4-x=1/4+z`, the centered response satisfies

\[
 H(-z)=\left(\frac14+z\right)\partial_zL(z),
 \qquad
 \widetilde Y(z)=H'(-z)
 =-\partial_z\left[left(\frac14+z\right)L'(z)\right].
                                                               \tag{168pg}
\]

Consequently, if `widetilde Y=sum c_jz^j`, then

\[
 \boxed{
 c_j=-(j+1)^2\ell_{j+1}
 -\frac14(j+1)(j+2)\ell_{j+2},
 }                                                    \tag{168ph}
\]

and the shape-two-normalized tower is

\[
 \boxed{
 d_j=\frac{c_j}{j+1}
 =-(j+1)\ell_{j+1}-\frac14(j+2)\ell_{j+2}.
 }                                                    \tag{168pi}
\]

The input coefficients of `Z` are themselves direct seam moments.  From
(168in), analytic continuation `x=-z` gives

\[
 k_u(-z)=1-e^{-u/2}
 \left[
 \cos(u\sqrt z)-2\sqrt z\sin(u\sqrt z)
 \right].                                          \tag{168pj}
\]

For `j>=1`, the coefficient of `z^j` in `eta(-z)` is

\[
 \boxed{
 [z^j]\eta(-z)
 =(-1)^{j+1}\int_0^\infty e^{-u/2}
 \left[
 \frac{u^{2j}}{(2j)!}
 +\frac{2u^{2j-1}}{(2j-1)!}
 \right]d\sigma(u).
 }                                                    \tag{168pk}
\]

Together with

\[
 Z(0)=1-\int_0^\infty(1-e^{-u/2})d\sigma(u)>0,      \tag{168pl}
\]

equations (168pf), (168pi), and (168pk) are a complete source-only
construction of every candidate Stieltjes moment `d_j`.  The logarithm in
(168pf) packages connected seam cumulants; the adjacent operator in (168pi)
is the archimedean shape-two completion.

The theorem target is now entirely explicit:

\[
 \boxed{
 \left{
 -(j+1)[z^{j+1}]\log Z
 -\frac14(j+2)[z^{j+2}]\log Z
 \right}_{j\ge0}
 \text{ is a Stieltjes moment sequence.}
 }                                                    \tag{168pm}

No zero ordinates, fitted atoms, or numerical reconstruction occur in this
formulation.  Its first Hankel minor is the Schwarzian condition; the entire
tower is the order-two Loewner target.

## The null carrier cancels and leaves an even-cumulant tower

The completed denominator has a simpler undecomposed expression.  Since
`I(x)=int K(u)cosh(sqrt(x)u)du` and `Z=4a_xI`, continuation to `x=-z` gives

\[
 \boxed{
 Z(z)=(1+4z)C(z),
 \qquad
 C(z)=\int_0^\infty K(u)\cos(\sqrt z\,u)du.
 }                                                    \tag{168pn}
\]

Write

\[
 \log C(z)=\sum_{k\ge0}q_kz^k.
\]

The contribution of `log(1+4z)` to (168pi) cancels identically:

\[
 -(j+1)[z^{j+1}]\log(1+4z)
 -\frac14(j+2)[z^{j+2}]\log(1+4z)=0.               \tag{168po}
\]

Therefore

\[
 \boxed{
 d_j=-(j+1)q_{j+1}-\frac14(j+2)q_{j+2}.
 }                                                    \tag{168pp}

This is the all-orders form of the curvature-neutral-carrier observation.
The archimedean factor is essential for typing the completed response, but
it contributes no shape-two moment after the adjacent logarithmic operator
is applied.

Normalize `K(u)du` to a probability law and symmetrize it by assigning signs
`+/-` with equal probability.  Let `kappa_{2k}` be the even cumulants of the
resulting real symmetric variable `U`.  Then

\[
 q_k=(-1)^k\frac{\kappa_{2k}}{(2k)!}.               \tag{168pq}
\]

Substitution into (168pp) yields the exact cumulant formula

\[
 \boxed{
 d_j=(-1)^j
 \left[
 \frac{(j+1)\kappa_{2j+2}}{(2j+2)!}
 -\frac{(j+2)\kappa_{2j+4}}{4(2j+4)!}
 \right].
 }                                                    \tag{168pr}
\]

Thus the RH-relevant moment candidate is an adjacent finite difference of
connected even source cumulants.  The theorem (168pm) can be restated as

\[
 \boxed{
 \left\{
 (-1)^j\left[
 \frac{(j+1)\kappa_{2j+2}}{(2j+2)!}
 -\frac{(j+2)\kappa_{2j+4}}{4(2j+4)!}
 \right]
 \right\}_{j\ge0}
 \text{ is a Stieltjes moment sequence.}
 }                                                    \tag{168ps}

This is a substantial semantic compression.  The proposed spectral measure
is not hidden in arbitrary theta derivatives: it is the shape-two adjacent
transform of the connected separation statistics of one fixed positive
source.  The first possible failure is a sign error in one `d_j`; the first
collective failure is a negative Hankel or shifted-localizing minor.

## The central Schwarzian gate is an eighth-cumulant inequality

The first three normalized coefficients from (168pr) are

\[
\begin{aligned}
 d_0&=\frac{\kappa_2}{2}-\frac{\kappa_4}{48},\\
 d_1&=-\frac{\kappa_4}{12}+\frac{\kappa_6}{960},\\
 d_2&=\frac{\kappa_6}{240}-\frac{\kappa_8}{40320}. \tag{168pt}
\end{aligned}
\]

Consequently the central rank-two Loewner condition is exactly

\[
 \boxed{
 \left(\frac{\kappa_2}{2}-\frac{\kappa_4}{48}\right)
 \left(\frac{\kappa_6}{240}-\frac{\kappa_8}{40320}\right)
 \ge
 \left(-\frac{\kappa_4}{12}+\frac{\kappa_6}{960}\right)^2.
 }                                                    \tag{168pu}
\]

Every cumulant here belongs to the single symmetrized probability law
proportional to `K(u)du`.  Thus (168pu) is the smallest source-only
collective theorem remaining after the complete chord analysis.  It is also
a sharp analytic falsifier: violation disproves the proposed order-two
Stieltjes mechanism already at the central Schwarzian gate, whereas success
opens the next Hankel and shifted-support minors.

The hierarchy is now visibly typed:

\[
 \begin{array}{c|c}
 d_j\ge0&\text{one normalized source mode},\\
 d_0d_2-d_1^2\ge0&\text{first collective curvature packet},\\
 \det(d_{i+j})_{i,j<r}\ge0&\text{higher coherent packets},\\
 \det(d_{i+j+1})_{i,j<r}\ge0&\text{support on the Stieltjes ray}.
 \end{array}                                        \tag{168pv}
\]

This is the point at which an analytic cumulant identity, rather than any
further finite spectral scout, is required.

## Exponential sources saturate curvature but expose the support problem

The carrier family gives an exact hostile comparison.  Take

\[
 K_\lambda(u)=c e^{-\lambda u},
 \qquad \lambda>0.
\]

Then

\[
 I_\lambda(x)=\frac{c\lambda}{\lambda^2-x},
\]

and the centered response has

\[
 \boxed{
 H_\lambda'(x)
 =\frac{\lambda^2-1/4}{(\lambda^2-x)^2}.
 }                                                    \tag{168pw}
\]

Every noncritical exponential therefore has an order-two rank-one
resolvent.  Its Schwarzian numerator vanishes identically, and every
unshifted Hankel determinant beyond rank one is zero.  Curvature alone cannot
distinguish the correct support ray.

In the cut-oriented coordinate `z=-x`,

\[
 \widetilde Y_\lambda(z)
 =\frac{\lambda^2-1/4}{(\lambda^2+z)^2},            \tag{168px}
\]

so

\[
 \boxed{
 d_j^{(\lambda)}
 =(-1)^j\frac{\lambda^2-1/4}{\lambda^{2j+4}}.
 }                                                    \tag{168py}
\]

For `lambda>1/2`, the response is positive but the normalized coefficients
alternate: the rank-one atom lies on the wrong quotient ray.  For
`lambda<1/2`, the coefficient orientation reverses together with the response
weight.  At

\[
 \lambda=\frac12,
\]

the entire tower vanishes.  This is exactly the critical archimedean null
carrier.

The example separates the two remaining obligations:

\[
 \boxed{
 \begin{array}{c|c}
 \text{unshifted Hankel/Schwarzian positivity}&
 \text{order-two curvature},\\
 \text{shifted/localizing positivity}&
 \text{selection of the negative quotient ray}.
 \end{array}
 }                                                    \tag{168pz}
\]

The theta correction cannot merely make a curvature determinant positive;
pure exponentials already saturate all such determinants.  It must relocate
the effective shape-two spectral measure across the critical carrier
threshold while preserving positive weight.  This is the precise support-
selection content absent from generic positive-source arguments.

It also explains why the central carrier cancellation (168po) matters.  The
`lambda=1/2` mode is the fold itself, not an atom of the physical measure.
Only connected arithmetic deviations from that null mode can populate the
admissible Stieltjes ray.

## Support positivity is alternation around the critical Laplace recurrence

Formula (168pr) simplifies to

\[
 \boxed{
 d_j=(-1)^j
 \left[
 \frac{\kappa_{2j+2}}{2(2j+1)!}
 -\frac{\kappa_{2j+4}}{8(2j+3)!}
 \right].
 }                                                    \tag{168qa}
\]

Whenever the consecutive cumulants are positive, define

\[
 R_j=\frac{\kappa_{2j+4}}{\kappa_{2j+2}},
 \qquad
 T_j=4(2j+2)(2j+3).                                 \tag{168qb}
\]

Then the one-mode Stieltjes condition `d_j>=0` is exactly

\[
 \boxed{
 R_j\le T_j\quad(j\text{ even}),
 \qquad
 R_j\ge T_j\quad(j\text{ odd}).
 }                                                    \tag{168qc}
\]

For the Laplace source of rate `lambda`,

\[
 R_j=\frac{2(j+1)(2j+3)}{\lambda^2}.                \tag{168qd}
\]

At the critical rate `lambda=1/2`, this equals `T_j` for every `j`.
Therefore the null carrier is not merely annihilated after summation: it is
the exact recurrence wall at every cumulant order.

The first conditions read

\[
 \kappa_4\le24\kappa_2,
 \qquad
 \kappa_6\ge80\kappa_4,
 \qquad
 \kappa_8\le168\kappa_6.                           \tag{168qe}
\]

Thus admissible support requires a coherent alternating displacement of the
theta cumulant ratios around the critical Laplace recurrence.  Uniformly
faster or uniformly slower exponential decay cannot work: it remains on one
side of the wall and produces the alternating wrong-ray sequence (168py).

This supplies a concrete modular target.  Reciprocal-scale completion must
force the connected cumulant recurrence to cross the carrier wall at every
successive parity while the Hankel minors keep those crossings coherent.
That is substantially more specific than “theta positivity should orient
the transform.”

If some even cumulant changes sign, the ratio language must be replaced by
the linear inequalities (168qa); those remain the authoritative statement.
No sign of an unproved cumulant is assumed here.

## The normalized tower is one central Loewner chord

The division by `j+1` has a direct geometric meaning.  Define its generating
function

\[
 D(z)=\sum_{j\ge0}d_jz^j.
\]

Since `d_j=c_j/(j+1)` and `widetilde Y(z)=H'(-z)`, termwise integration gives

\[
\begin{aligned}
 D(z)
 &=\frac1z\int_0^z\widetilde Y(t)dt\\
 &=\boxed{\frac{H(0)-H(-z)}{z}}.                   \tag{168qf}
\end{aligned}
\]

Thus `D` is exactly the Loewner divided difference between the central point
and the cut-oriented point `-z`.  Shape-two normalization is spectral chord
integration, not a fitted coefficient operation.

Using (168pg), the same function is source-explicit:

\[
 \boxed{
 D(z)=\frac{
 \frac14L'(0)-(\frac14+z)L'(z)
 }{z},
 \qquad L=\log Z.
 }                                                    \tag{168qg}
\]

The apparent singularity at `z=0` is removable and equals `d_0=H'(0)`.
Because the null factor `log(1+4z)` cancels in the numerator, (168qg) depends
only on the completed theta remainder.

For an order-two Stieltjes representation,

\[
 \widetilde Y(z)=\int\frac{d\nu(r)}{(r-z)^2},
\]

integration yields

\[
 \boxed{
 D(z)=\int\frac{d\nu(r)}{r(r-z)}.
 }                                                    \tag{168qh}
\]

Therefore the moment sequence `d_j` and the central Loewner chord `D(z)` are
the same object in coefficient and function coordinates.  The remaining RH
target can be stated without reference to Taylor coefficients:

\[
 \boxed{
 \frac{H(0)-H(-z)}{z}
 \text{ is a Stieltjes function with the required support threshold.}
 }                                                    \tag{168qi}

This also clarifies the scope of the chord theorem already proved.  That
theorem orients points inside `0<x<1/4`; (168qi) continues from `x=0` in the
opposite direction, toward the quotient cut.  Analytic continuation across
the center, not another normalization, is where the support-selection burden
enters.

## Higher packets are connected seam clusters

The same formula explains why the all-orders problem survives the two-copy
kernel reduction.  Put

\[
 P(z)=\eta(-z),
 \qquad Z(z)=1-P(z).
\]

Then

\[
 \boxed{
 L(z)=\log Z(z)
 =-\sum_{k\ge1}\frac{P(z)^k}{k}.
 }                                                    \tag{168qj}
\]

Thus the logarithmic coefficients `ell_j` are connected-cluster
combinations of `k` seam copies.  Substitution into (168qg) gives the exact
source formula

\[
 \boxed{
 D(z)=\frac1z\left[
 -\frac14\frac{P'(0)}{1-P(0)}
 +\left(\frac14+z\right)
 \frac{P'(z)}{1-P(z)}
 \right].
 }                                                    \tag{168qk}

There is no contradiction with (168iu).  Clearing the two scalar
denominators of one evaluated Loewner entry leaves at most two seam copies.
Taking a logarithmic response and requiring coherent positivity for packets
of every rank reconstructs the connected powers in (168qj).

The hierarchy now has a precise source-copy interpretation:

\[
 \begin{array}{c|c}
 \text{one Loewner entry after denominator clearing}&
 \text{one- and two-seam chords},\\
 \text{one logarithmic coefficient }d_j&
 \text{connected seam clusters of unbounded size},\\
 \text{rank-}r\text{ Hankel minor}&
 \text{coherence among }r\text{ connected responses}.
 \end{array}                                        \tag{168ql}
\]

This identifies the next possible combinatorial reduction.  The factors
`1/k` in (168qj) are the standard connected-cycle weights.  Rather than
expanding cumulants separately at every order, one should seek a renewal or
Schur-complement realization of

\[
 \frac{P'}{1-P}                                    \tag{168qm}
\]

whose states are source-labelled seam excursions and whose return kernel is
positive after modular reflection.  Such a realization would generate the
entire Stieltjes tower at once.  Without it, proving (168pu) alone would be
only the first connected-cluster check.

## Deutsch--Popper target: a modular renewal resolvent

The connected-cluster formula suggests a single hard-to-vary conjecture.
There should exist a Hilbert space of completed, source-labelled seam
excursions, a cyclic boundary vector `Omega`, and a self-adjoint return
operator `A` with the required support floor such that

\[
 \boxed{
 D(z)=\left\langle\Omega,(A-z)^{-1}\Omega\right\rangle.
 }                                                    \tag{168qn}
\]

The construction must satisfy four typing requirements:

1. one primitive excursion produces `P'(z)`;
2. repeated returns produce the geometric sewing factor `(1-P(z))^{-1}`;
3. reciprocal modular reflection supplies the adjoint, rather than an
   independently chosen inner product;
4. the archimedean boundary column supplies the `1/4` support threshold and
   cancels the null `lambda=1/2` carrier.

If these hold, (168qk) becomes a Schur-complement identity and

\[
 d_j=\langle\Omega,A^{-j-1}\Omega\rangle           \tag{168qo}
\]

is automatically a Stieltjes moment sequence.  All Hankel and localizing
conditions then follow from one positive return geometry.

This conjecture is stronger than fitting a Jacobi matrix to the already
computed moments.  Both `A` and `Omega` must be derived before moment
reconstruction from the theta label transport and its modular seam.  A
generic moment sequence always admits finite tridiagonal presentations when
its tested minors pass; that is coordinate manufacture, not explanation.

The sharp falsifier is finite and source-typed:

\[
 \boxed{
 \text{find the first completed reflected excursion cluster whose return
 quadratic form is negative or whose boundary incidence misses }P'/(1-P).
 }                                                    \tag{168qp}
\]

If such a cluster exists, the renewal explanation fails even if several
central Hankel minors happen to be positive.  If every finite cluster is a
positive compression of one fixed return operator, the infinite closure and
support floor become the only remaining analytic obligations.

## The primitive excursion is a fixed half-line wave response

The numerator of the renewal system already has a canonical linearization.
Since

\[
 K'(u)=-\Phi(u),
 \qquad K(\infty)=0,
\]

integration by parts in (168pn) gives

\[
 \boxed{
 C(z)=\int_0^\infty
 \Phi(u)\frac{\sin(\sqrt z\,u)}{\sqrt z}du.
 }                                                    \tag{168qq}

The kernel

\[
 G_z(u)=\frac{\sin(\sqrt z\,u)}{\sqrt z}
\]

is the solution of the fixed initial-value problem

\[
 -G_z''=zG_z,
 \qquad G_z(0)=0,
 \qquad G_z'(0)=1.                                  \tag{168qr}
\]

Thus `C(z)` is the source readout of one half-line Dirichlet wave channel.
No spectral atoms or moment-fitted Jacobi coefficients are required to
produce the primitive excursion.

The operator problem is consequently narrower than (168qn) initially
suggests.  One must add a source-derived boundary feedback to the fixed wave
system (168qr) so that:

\[
 \boxed{
 \text{primitive wave excursion}
 +\text{modular reflected return}
 \longrightarrow
 \frac{P'}{1-P}
 \longrightarrow
 \text{positive Weyl/Stieltjes function}.
 }                                                    \tag{168qs}

This points toward a Krein-string or canonical-system realization.  But the
mass distribution and boundary condition must be read from `Phi` and the
reciprocal seam; invoking the abstract inverse theorem after establishing
moments would again manufacture the operator from the desired answer.

The next concrete calculation is the Green identity for two solutions of
(168qr) after applying the theta source functional.  Its boundary form must
be compared with (168qk).  If the difference is exactly the modular seam
current, the renewal conjecture has a canonical operator candidate.  If an
additional indefinite bulk term remains, the fixed-wave realization does
not close the Stieltjes mechanism.

## Green identity: positive wave bulk plus a rank-two forcing defect

Introduce the terminal tail field

\[
 F_z(q)=\int_q^\infty
 \Phi(u)\frac{\sin(\sqrt z\,(u-q))}{\sqrt z}du.     \tag{168qt}
\]

It obeys

\[
 F_z(0)=C(z),
 \qquad
 F_z(\infty)=F_z'(\infty)=0,                       \tag{168qu}
\]

and direct differentiation gives the forced wave equation

\[
 \boxed{F_z''+zF_z=\Phi.}                          \tag{168qv}
\]

For two spectral parameters `z,w`, subtract the two forced equations after
pairing.  Integration over the half-line yields

\[
\boxed{
\begin{aligned}
 (z-\bar w)\int_0^\infty F_z(q)\overline{F_w(q)}dq
 ={}&F_z'(0)\overline{C(w)}
 -C(z)\overline{F_w'(0)}\\
 &+\int_0^\infty\Phi(q)
 \left(\overline{F_w(q)}-F_z(q)\right)dq.
\end{aligned}
}                                                     \tag{168qw}
\]

The first line is the ordinary boundary Wronskian.  The left side is the
positive wave Gram kernel with the expected spectral denominator.  The last
line is the obstruction created by the common inhomogeneous theta forcing.

On any finite spectral packet the forcing term has rank at most two: it is
the difference of the column `z mapsto <Phi,F_z>` and its adjoint.  Thus the
fixed-wave realization has exactly the familiar architecture

\[
 \boxed{
 \text{positive wave bulk}
 +\text{boundary Wronskian}
 +\text{rank-two primitive-source defect}.
 }                                                    \tag{168qx}
\]

This answers the proposed Green-identity test.  The bare wave channel does
not close directly to the Stieltjes response; it is forced rather than
homogeneous.  But the failure is finite-channel, not an uncontrolled
indefinite bulk.

There are now only two faithful ways to close it:

1. enlarge the state space by one source coordinate so that `Phi` becomes a
   boundary vector and the forced equation becomes a homogeneous block
   system;
2. prove that reciprocal modular sewing supplies the adjoint source sheet
   whose forcing line cancels the last line of (168qw).

The second option is stronger and more source-specific.  The first supplies
the minimal hostile construction: if the homogeneous one-coordinate
extension still has an indefinite boundary metric, modular arithmetic is
genuinely necessary rather than representational.

## No-go for the naive one-coordinate self-adjoint extension

The minimal homogeneous extension can be tested by source degree.  A
self-adjoint Friedrichs-type block operator would have the form

\[
 \mathcal A=
 \begin{pmatrix}
 A_0&|\Phi\rangle\\
 \langle\Phi|&c
 \end{pmatrix},                                    \tag{168qy}
\]

where `A_0` is the half-line wave operator.  Eliminating the wave channel
produces the scalar Schur complement

\[
 c-z-\langle\Phi,(A_0-z)^{-1}\Phi\rangle.          \tag{168qz}
\]

Its source dependence is quadratic in `Phi`.  By contrast, the actual
primitive response is

\[
 C(z)=\int_0^\infty\Phi(u)G_z(u)du,                \tag{168ra}
\]

which is linear in `Phi`.  No choice of the scalar constant `c` repairs this
degree mismatch.

Therefore

\[
 \boxed{
 \text{one scalar coordinate coupled self-adjointly through }\Phi
 \text{ cannot realize the theta renewal denominator.}
 }                                                    \tag{168rb}

Replacing `Phi` by `sqrt(Phi)` fixes formal source degree only if the
propagator acts diagonally by `G_z(u)`.  But the family

\[
 u\longmapsto\frac{\sin(\sqrt z\,u)}{\sqrt z}
\]

does not satisfy the pointwise resolvent identity and hence is not the
resolvent of a fixed multiplication operator.  That shortcut is unavailable
as well.

This is a useful structural no-go.  A faithful homogeneous realization needs
at least two typed ports:

\[
 \boxed{
 \text{source injection}
 \longrightarrow\text{wave transport}
 \longrightarrow\text{distinct boundary readout},
 }                                                    \tag{168rc}
\]

with modular reflection providing the adjoint identification only after the
transport.  Forcing injection and physical readout cannot be identified at
the outset without squaring the theta source.

The next operator candidate is therefore a conservative two-port colligation
or canonical system, not a rank-one self-adjoint perturbation.  Its transfer
function must be `P(z)`, and closing the two ports by the modular seam must
produce `(1-P)^{-1}`.  Positivity of the closed-loop energy is precisely the
missing Stieltjes theorem.

## The Carrier fold is the symmetric sector of a two-port transfer

The primitive response has the correct off-diagonal form.  Let `b` denote
the generalized boundary-control vector that imposes
`G_z(0)=0, G_z'(0)=1`, and let the observation port be the distributed source
functional `c=<Phi|`.  Then, schematically,

\[
 C(z)=c(A_0-z)^{-1}b.                               \tag{168rd}
\]

The two ports are distinct, so this scalar transfer need not be a Weyl
function.  Reciprocal modular reflection supplies the reverse path

\[
 C^\sharp(z)=b^*(A_0-z)^{-1}c^*.                   \tag{168re}
\]

and the faithful open transfer is the off-diagonal matrix

\[
 \boxed{
 \mathbb T(z)=
 \begin{pmatrix}
 0&P^\sharp(z)\\
 P(z)&0
 \end{pmatrix}.
 }                                                    \tag{168rf}

The modular sewing theorem required here is

\[
 \boxed{P^\sharp(z)=P(z)}                           \tag{168rg}
\]

on the completed Real reciprocal-scale Carrier, with equality understood
after the correct boundary normalizations.  When (168rg) holds, the fixed
and anti-fixed port combinations

\[
 e_+=\frac1{\sqrt2}\binom11,
 \qquad
 e_-=\frac1{\sqrt2}\binom1{-1}                    \tag{168rh}
\]

diagonalize the transfer:

\[
 \mathbb T(z)e_+=P(z)e_+,
 \qquad
 \mathbb T(z)e_-=-P(z)e_-.                         \tag{168ri}

Closing the positive fixed sector therefore produces

\[
 (1-\mathbb T)^{-1}e_+
 =\frac1{1-P(z)}e_+,                               \tag{168rj}
\]

while the anti-fixed sector carries `(1+P)^{-1}`.  This recovers the exact
renewal denominator without squaring the source.

This is the first operator architecture that simultaneously explains:

* why the primitive theta response is linear in `Phi`;
* why an adjoint return path is nevertheless required for positivity;
* why the physical denominator is `1-P` rather than `1-|P|^2`;
* why the functional-equation fold selects one sector and rejects its
  anti-fixed partner.

The remaining positivity theorem is now localized.  One must show that the
open two-port colligation is conservative or passive in a source-derived
metric and that modular reflection really identifies its ports as in
(168rg).  If so, the fixed-sector closed-loop Weyl function is (168qk), and
the Stieltjes tower follows.  If the port metrics have opposite signs or a
nontrivial seam cocycle survives, the proposed Carrier realization fails at
that explicit boundary channel.

## Scope correction: the two-port fold is Krein-signed, not automatically passive

The preceding architecture gets the source degree and renewal denominator
right, but it does not yet supply positivity.  If reciprocity gives
`P^sharp=P`, then

\[
 \operatorname{Im}\mathbb T(z)
 =\begin{pmatrix}
 0&\operatorname{Im}P(z)\\
 \operatorname{Im}P(z)&0
 \end{pmatrix}.                                    \tag{168rk}
\]

In the fixed/anti-fixed basis its eigenvalues are

\[
 \boxed{+\operatorname{Im}P(z),
 \qquad-\operatorname{Im}P(z).}                    \tag{168rl}
\]

Therefore the full two-port transfer cannot be Herglotz in a positive metric
unless `Im P=0`.  Its natural port geometry is Krein-signed: the two Carrier
sectors have opposite orientation.

This corrects a possible overreading of (168rj).  Modular folding explains
why the physical denominator is `1-P` and why there is an anti-fixed partner
`1+P`; it does not prove that the fixed sector is the positive one.  Showing

\[
 \boxed{
 \text{the source-selected fixed sector has the required Pick/Stieltjes
 orientation}
 }                                                    \tag{168rm}

is exactly the remaining theorem.

Nor can ordinary open-system passivity be invoked for free.  A scattering
formulation would require a Schur bound on `P`; a Weyl formulation would
require a Herglotz sign for a Cayley transform of `P`.  Either condition is a
substantial analytic statement about the completed theta source and cannot
be deduced merely from the symmetric off-diagonal presentation.

The operator gain is therefore architectural but real:

\[
 \boxed{
 \text{reciprocity determines the fold and its two signatures;}
 \quad
 \text{theta arithmetic must select the positive signature.}
 }                                                    \tag{168rn}

This is the operator form of the support-selection problem exposed by the
exponential hostile family.  Symmetry creates the two candidate rays;
source-derived positivity must decide which ray is physical.

## Central signature selection is an upper secular bound

The two Carrier signatures can be compared at the central point using the
three seam moments in (168jp).  For the physical fixed denominator `1-eta`,
the cleared diagonal response is

\[
 N_+=(1-E)C+\frac14A^2.                             \tag{168ro}
\]

For the anti-fixed denominator `1+eta`, the same differentiation gives

\[
 \boxed{
 N_-=-(1+E)C+\frac14A^2.
 }                                                    \tag{168rp}
\]

The all-arithmetic theorem proved `N_+>0`.  The two sectors have opposite
central signatures exactly when

\[
 \boxed{
 \frac{A^2}{4}<(1+E)C.
 }                                                    \tag{168rq}

This complements the lower repair inequalities used in the chord theorem.
For a self-pair contribution, positivity required

\[
 \frac{A^2}{4}\ge EC.                              \tag{168rr}
\]

Thus the ideal source-selected window is

\[
 \boxed{
 EC\le\frac{A^2}{4}<(1+E)C.
 }                                                    \tag{168rs}

Inside this window, the reflection-pair repair is large enough to orient the
physical fixed sector but not large enough to orient its anti-fixed partner.
The fold genuinely selects one positive signature rather than duplicating
positivity on both sheets.

Equation (168rq) is the smallest analytic signature-selection test for the
completed source.  It is distinct from RH: it checks only the central first
response.  But failure would falsify the proposed two-port interpretation
immediately, because both sectors would then have the same local sign or the
physical sector would be the wrong one.

The required source estimate is already contained in the moment-cone proof,
once its range is sharpened.  The comparison (168ju)--(168jx) works for every
`a>=3`, not merely `a>=12`; at `a=3` the negative-tail bound is already below
`1/(6a)`, and its ratio to that bound decreases thereafter.  Since
`pi n^2>3`, this proves

\[
 C_n>E_n>0\qquad(n\ge1).                            \tag{168rt}
\]

Summing labels gives `C>E`.  The pointwise exponential inequality (168kl)
gives `A<=4E`.  Finally

\[
 E<\sum_{n\ge1}\tau_n([0,\infty))
 =\sum_{n\ge1}2ne^{-\pi n^2}<\frac1{10};           \tag{168ru}
\]

the first term is below `2/23`, and the tail from `n=2` is bounded by a
geometric series below `1/1000`.

Therefore

\[
 \frac{A^2}{4C}
 \le\frac{16E^2}{4E}
 =4E
 <1+E.                                             \tag{168rv}
\]

This proves (168rq), strictly.  Combining with the previously proved lower
bound yields

\[
 \boxed{
 EC\le\frac{A^2}{4}<(1+E)C.
 }                                                    \tag{168rw}

Hence the completed theta source selects opposite Carrier signatures at the
central response:

\[
 \boxed{N_+>0,
 \qquad N_-<0.}                                     \tag{168rx}

This is the first proved signature-selection theorem for the proposed
two-port realization.  It remains local at the central spectral point, but
it shows that the fixed-sector choice is source-determined rather than a
convention imposed after diagonalization.

## Signature selection propagates through the full central interval

The central theorem extends uniformly in `x`.  Write

\[
 \widehat K_n=n^{-1}K_n,
 \qquad
 \widehat H_n=n^{-1}H_n,
\]

and

\[
 \mathcal E(x)=\eta(x)=\sum_n\widehat K_n(x),
 \qquad
 \mathcal A(x)=-\eta'(x)=\sum_n[-\widehat K_n'(x)],
 \qquad
 \mathcal C(x)=a_x\eta''(x)-\eta'(x)=\sum_n\widehat H_n'(x).
                                                               \tag{168ry}
\]

For a single label, (168og) and (168oi) give

\[
 \widehat H_n'(x)\ge\frac{\widehat K_n(x)}{a_x}
 \left(1-\frac{3a_x}{\lambda_n^2-x}\right).        \tag{168rz}
\]

Moreover `-widehat K_n'/widehat K_n=(1-alpha_n)/a_x<1/a_x`.  Since
`lambda_n^2-x>30` and `3a_x<=3/4`,

\[
 \boxed{
 \frac{a_x[-\widehat K_n'(x)]^2}
 {\widehat K_n(x)\widehat H_n'(x)}
 <\frac{40}{39}.
 }                                                    \tag{168sa}

Cauchy--Schwarz across the labels yields

\[
 \mathcal A(x)^2
 \le\mathcal E(x)
 \sum_n\frac{[-\widehat K_n'(x)]^2}{\widehat K_n(x)}.
                                                               \tag{168sb}

Combining with (168sa),

\[
 a_x\mathcal A(x)^2
 <\frac{40}{39}\mathcal E(x)\mathcal C(x).         \tag{168sc}

Since every `widehat K_n'(x)<0`, the total seam mass decreases with `x`;
hence

\[
 \mathcal E(x)\le\mathcal E(0)<\frac1{10}.         \tag{168sd}

Therefore

\[
 \boxed{
 a_x\mathcal A(x)^2
 <\frac4{39}\mathcal C(x)
 <(1+\mathcal E(x))\mathcal C(x).
 }                                                    \tag{168se}

For the fixed and anti-fixed denominators, the cleared diagonal responses
are respectively

\[
\begin{aligned}
 N_+(x)&=(1-\mathcal E)\mathcal C+a_x\mathcal A^2,\\
 N_-(x)&=-(1+\mathcal E)\mathcal C+a_x\mathcal A^2. \tag{168sf}
\end{aligned}
\]

Since `mathcal C>0`, (168se) proves

\[
 \boxed{
 N_+(x)>0,
 \qquad
 N_-(x)<0
 \qquad(0\le x<1/4).
 }                                                    \tag{168sg}

Thus the source-derived Carrier signature does not switch anywhere in the
central interval.  The fixed sector has positive scalar response and the
anti-fixed sector has negative scalar response uniformly.  This still does
not prove higher-rank Pick positivity of the fixed sector, but it removes a
possible local signature crossing from the operator program.

Since the positive denominators are `(1-mathcal E)^2` and
`(1+mathcal E)^2`, respectively, (168sg) also gives

\[
 H_+'(x)>0,
 \qquad H_-'(x)<0.                                  \tag{168sh}
\]

Therefore every separated scalar chord has the same fixed signature:

\[
 \boxed{
 \frac{H_+(y)-H_+(x)}{y-x}>0,
 \qquad
 \frac{H_-(y)-H_-(x)}{y-x}<0
 \quad(0\le x<y<1/4).
 }                                                    \tag{168si}

The Carrier fold is thus globally signature-stable at rank one.  Any
remaining failure of the fixed sector must arise from collective packet
geometry, while the anti-fixed sector is already rejected by every scalar
probe in the interval.

## The open two-port transfer is Schur on the natural quotient disk

The alternating source coefficients in (168pk) give a complex-domain result.
Write

\[
 P(z)=\eta(-z)=E+sum_{j\ge1}(-1)^{j+1}M_jz^j,
 \qquad M_j>0.                                     \tag{168sj}
\]

For `0<=r<1/4`, evaluation on the physical ray gives

\[
 \eta(r)=P(-r)=E-\sum_{j\ge1}M_jr^j>0.             \tag{168sk}
\]

Therefore, for every `|z|<=r`,

\[
\begin{aligned}
 |P(z)|
 &\le E+\sum_{j\ge1}M_jr^j\\
 &=2E-\eta(r)\\
 &<2E<\frac15.                                     \tag{168sl}
\end{aligned}
\]

Consequently

\[
 \boxed{
 |P(z)|<\frac15
 \qquad(|z|<1/4).
 }                                                    \tag{168sm}
\]

The two-port transfer (168rf) is thus a strict Schur contraction throughout
the natural quotient disk, and both feedback denominators obey

\[
 \boxed{
 |1\mp P(z)|>\frac45.
 }                                                    \tag{168sn}

This proves a source-derived complex zero-free neighborhood and stable
feedback, not merely real-axis monotonicity.  Its radius is set by the
archimedean carrier singularity before cancellation.  It does not reach the
distant negative quotient ray containing the RH ordinates, so it is not a
substitute for the Stieltjes support theorem.

The result nevertheless fixes the analytic starting domain for any
continuation argument.  The fixed sector begins as a uniformly contractive
closed loop with the correct scalar signature.  A failure farther toward the
cut must occur through loss of Pick/Stieltjes orientation after continuation,
not through a local pole, port instability, or ambiguity at the fold.

## Global RH target: the primitive return is Schur in the upper half-plane

The local contraction theorem should not be continued as `|P|<1` through
the positive real spectral ray.  The desired spectral events satisfy

\[
 Z(z)=1-P(z)=0,
 \qquad P(z)=1.                                    \tag{168so}
\]

They are boundary contacts of the feedback transfer, not points to be
excluded.  The correct global statement is

\[
 \boxed{
 |P(z)|<1
 \qquad(\operatorname{Im}z>0).
 }                                                    \tag{168sp}

Reality gives the conjugate statement in the lower half-plane.  Under the
already required product/continuation hypotheses, (168sp) confines every
solution of `P(z)=1` to the real quotient axis.

Recall that the cut coordinate is `z=-x`, where

\[
 x=(s-1/2)^2.
\]

Thus a positive real contact `z=gamma^2` pulls back to

\[
 s=\frac12\pm i\gamma.                             \tag{168sq}
\]

A negative real contact would pull back to a nontrivial real zero.  Combining
the Schur theorem with the independently established absence of such real
zeros therefore leaves only the critical-line contacts.

Accordingly, the conditional theorem-shaped endpoint is

\[
 \boxed{
 \text{global upper-half-plane Schur contractivity of }P
 +\text{real-zero exclusion}
 \Longrightarrow\mathrm{RH}.
 }                                                    \tag{168sr}

This formulation is weaker in local shape than the full Stieltjes theorem
but already has the correct zero-localization force.  The Stieltjes tower
adds positive contact weights, support orientation, and order-two resolvent
structure.

The Cayley transform makes the operator meaning explicit:

\[
 \mathcal W(z)=\frac{1+P(z)}{1-P(z)}.              \tag{168ss}
\]

Condition (168sp) is equivalent to `Re mathcal W(z)>0` in the upper half-
plane.  Hence the immediate global target for the two-port construction is a
positive-real scattering theorem for the fixed-sector Cayley response.
Poles of `mathcal W` are exactly the fixed-sector spectral contacts.

The disk theorem (168sm) supplies a nonempty source-derived germ of this
Schur domain.  What remains is to prove that modularly reflected wave
transport preserves contractivity throughout the upper half-plane, allowing
unit-circle contact only on its real boundary.

## Immediate falsification of the global Schur target

The proposed continuation (168sp) is too strong.  On the real quotient axis,
`Z=1-P` is real.  At a simple spectral event `r`,

\[
 Z(r)=0,
 \qquad Z'(r)\ne0.                                  \tag{168st}
\]

Hence `Z` changes sign and `P=1-Z` crosses transversely through the value
one.  On one adjacent real interval,

\[
 P(t)>1.                                            \tag{168su}
\]

But a scalar Schur function in the upper half-plane has nontangential
boundary values of modulus at most one almost everywhere.  It cannot have a
real analytic boundary trace that crosses transversely from below one to
above one.  Therefore

\[
 \boxed{
 P\text{ cannot be globally Schur if the desired spectral zeros are simple.}
 }                                                    \tag{168sv}

This falsifies (168sp)--(168sr) as the RH mechanism.  The local disk theorem
(168sm) remains valid; it proves only a contractive germ before the first
lossless spectral excursion.

The error was instructive.  A passive scattering variable should meet the
unit circle through phase rotation, while `P` is a real feedback coordinate
that crosses the real value one.  The correct global positive object must be
one of:

1. a de Branges phase ratio with unimodular real boundary values; or
2. the meromorphic Weyl/Stieltjes response `D`, whose positive real poles are
   allowed and carry spectral mass.

Thus the two-port representation of `1-P` remains useful for incidence and
signature selection, but `P` itself is not the passive transfer coordinate.
The Cayley transform (168ss) likewise has alternating real-axis pole signs
unless additional phase data are retained, so it cannot be declared
positive-real from the scalar feedback presentation alone.

The corrected operator target returns to (168qn): construct the meromorphic
resolvent `D` or a phase-valued de Branges transfer from the full two-port
state before projecting to the real scalar `P`.  Projection to `P` preserves
the zero equation but discards the phase orientation needed for passivity.

## The missing phase is the boundary normal derivative

The Green identity (168qw) already contains the correct two-component
boundary observable.  Define

\[
 C(z)=F_z(0),
 \qquad
 B(z)=-F_z'(0)=\int_0^\infty\Phi(u)\cos(\sqrt z\,u)du.  \tag{168sw}
\]

For real `z`, both functions are real.  Hence

\[
 E(z)=C(z)-iB(z),
 \qquad
 E^\#(z)=C(z)+iB(z)                                \tag{168sx}
\]

have the boundary ratio

\[
 \Theta(z)=\frac{E^\#(z)}{E(z)},
 \qquad
 |\Theta(t)|=1\quad(t\in\mathbb R).                \tag{168sy}

Unlike the real scalar `P`, `Theta` can pass through a spectral contact by
phase rotation while remaining unimodular.  It has the correct kinematics
for an inner/de Branges transfer.

Moreover, the boundary Wronskian in (168qw) is exactly

\[
 F_z'(0)\overline{C(w)}-C(z)\overline{F_w'(0)}
 =C(z)\overline{B(w)}-B(z)\overline{C(w)},          \tag{168sz}
\]

the alternating numerator associated with the pair `(C,B)`.  Thus the wave
Green identity was already producing a de Branges boundary form; projecting
to `C` or `P` alone discarded its phase coordinate.

After inserting the exact archimedean normalization that converts `C` into
the completed quotient function, the corrected global target is

\[
 \boxed{
 E\text{ is Hermite--Biehler}
 \quad\Longleftrightarrow\quad
 \Theta=E^\#/E\text{ is inner in the upper half-plane}.
 }                                                    \tag{168ta}

The remaining obstruction is still the rank-two forcing line in (168qw).
If bilateral modular sewing converts that line into a nonnegative boundary
channel, the Wronskian becomes a Gram kernel and (168ta) follows.  If it
retains an indefinite sign, the wave-phase realization fails even though its
boundary kinematics are correct.

This recovers the de Branges lane with a sharper source meaning: `C` is the
Dirichlet boundary value, `B` is its normal derivative, and modular sewing
must orient their symplectic Wronskian.  The phase was not an auxiliary
analytic trick; it was the boundary datum lost in the scalar feedback
projection.

## The forcing defect is the canonical separation channel

The last line of (168qw) is not an arbitrary source functional.  Define

\[
 J(z)=\langle\Phi,F_z\rangle
 =\int_0^\infty\Phi(q)F_z(q)dq.                    \tag{168tb}
\]

Substitution of (168qt) and symmetrization of the ordered region `q<=u`
give

\[
 \boxed{
 J(z)=\frac12\iint_{[0,\infty)^2}
 \Phi(u)\Phi(v)
 \frac{\sin(\sqrt z\,|u-v|)}{\sqrt z},du,dv.
 }                                                    \tag{168tc}

Therefore the forcing line in the Green identity is exactly

\[
 \boxed{\overline{J(w)}-J(z).}                     \tag{168td}

After division by `z-bar w`, it is the Loewner divided-difference kernel of
one canonical two-source separation response.  The apparent rank-two packet
defect is thus a scalar shadow of the positive product measure

\[
 \frac12\Phi(u)\Phi(v)dudv                         \tag{168te}

pushed forward by the separation coordinate `|u-v|`.

This reunifies the Green and curvature lanes.  The earlier measure carrying
the squared-separation curvature and the present sine-propagated forcing
defect are different readouts of the same two-copy source geometry.  The
remaining sign problem is entirely oscillatory: positivity of the underlying
separation measure does not orient its sine or cosine transform.

The de Branges theorem can now be targeted precisely:

\[
 \boxed{
 \text{modular sewing must absorb the divided difference of }J
 \text{ into a nonnegative boundary channel.}
 }                                                    \tag{168tf}

If it does, (168qw) becomes a positive Gram identity for the completed
boundary phase pair `(C,B)`.  If it does not, the exact residual obstruction
is the oscillatory transform (168tc), not an unspecified failure of wave
passivity.

## The separation defect is a cosine transform of an autocorrelation tail

Push the product source in (168tc) to the separation coordinate.  For
`d>=0`, define the one-sided autocorrelation

\[
 A(d)=\int_0^\infty\Phi(u)\Phi(u+d)du.              \tag{168tg}
\]

The factor `1/2` in (168tc) exactly cancels the two orientations of an
off-diagonal pair, so

\[
 J(z)=\int_0^\infty
 A(d)\frac{\sin(\sqrt z\,d)}{\sqrt z}dd.           \tag{168th}
\]

Let

\[
 M(t)=\int_t^\infty A(d)dd.                        \tag{168ti}
\]

Using `sin(sd)/s=int_0^d cos(st)dt` and Tonelli on the nonoscillatory
majorant gives

\[
 \boxed{
 J(z)=\int_0^\infty M(t)\cos(\sqrt z\,t)dt.
 }                                                    \tag{168tj}

This exposes a classical sufficient orientation mechanism.  If

\[
 \boxed{A'(d)\le0\qquad(d\ge0),}                   \tag{168tk}

then `M` is positive, decreasing, and convex:

\[
 M'=-A<0,
 \qquad M''=-A'\ge0.                               \tag{168tl}

Pólya's convexity criterion then implies

\[
 \boxed{J(t)\ge0\qquad(t\ge0).}                   \tag{168tm}

The representation has a direct adjacent-band interpretation: convex decay
of `M` pairs successive negative cosine lobes with larger preceding positive
lobes.  This is precisely the source-normalized variation-diminishing
mechanism proposed earlier, now attached to the exact Green-identity defect.

Condition (168tk) is not assumed.  The primitive theta density is not
pointwise monotone at the seam, so monotonicity of `A` must come from the
integrated two-copy source rather than from a labelwise shortcut.  The sharp
falsifier is

\[
 \boxed{\exists d>0:\ A'(d)>0.}                    \tag{168tn}

If this occurs, the simple Pólya pairing fails and no regrouping of cosine
bands should be used to conceal it.  A larger modular block or a different
oriented boundary channel would then be necessary.

Even (168tm) would orient only the scalar defect on the real ray.  The full
de Branges theorem requires positivity of its divided-difference kernel in
the upper half-plane.  Nevertheless (168tk) is the smallest analytic test of
whether the exact separation channel possesses the anticipated
variation-diminishing geometry.

## Autocorrelation monotonicity reduces to theta-mixture log-concavity

Extend `Phi` by zero to the negative half-line.  If this extended density is
log-concave, then its full autocorrelation

\[
 \widetilde A(d)=\int_{\mathbb R}\Phi(u)\Phi(u+d)du  \tag{168to}
\]

is log-concave by the Prekopa convolution theorem.  It is also even.  Hence
it is decreasing for `d>0`.  For positive `d`, the zero extension makes
`widetilde A(d)=A(d)`, proving (168tk).

The source condition can be written exactly at the label level.  Decompose

\[
 \Phi(u)=\sum_{n\ge1}\phi_n(u),
 \qquad
 p_n(u)=\frac{\phi_n(u)}{\Phi(u)},                  \tag{168tp}
\]

and define the label score and curvature

\[
 s_n(u)=\partial_u\log\phi_n(u),
 \qquad
 \kappa_n(u)=\partial_u^2\log\phi_n(u).            \tag{168tq}
\]

Differentiating the logarithm of the mixture gives the exact identity

\[
 \boxed{
 (\log\Phi)''
 =\mathbb E_{p(u)}[\kappa_n]
 +\operatorname{Var}_{p(u)}(s_n).
 }                                                    \tag{168tr}

Each primitive label is strongly log-concave.  With
`y=e^{2u}` and `q=n^2y`,

\[
 \boxed{
 \kappa_n(u)
 =-4\pi q-
 \frac{24\pi q}{(2\pi q-3)^2}
 <-4\pi q.
 }                                                    \tag{168ts}

Therefore full theta log-concavity is equivalent to the coupled label bound

\[
 \boxed{
 \operatorname{Var}_{p(u)}(s_n)
 \le-\mathbb E_{p(u)}[\kappa_n]
 \qquad(u\ge0).
 }                                                    \tag{168tt}

This is the same structural competition encountered in the mixed chord
theorem: positive individual curvature must dominate the square of the
between-label shear.  Here the arithmetic weights are even more favorable,
because

\[
 \frac{\phi_n(u)}{\phi_1(u)}
 =n^2\frac{2\pi n^2e^{2u}-3}{2\pi e^{2u}-3}
 e^{-\pi(n^2-1)e^{2u}}                              \tag{168tu}

is superexponentially small for `n>=2` and decreases with `u` after the
seam.  The curvature reserve grows like `n^2e^{2u}`, while the competing
label mass decays like `exp[-pi n^2e^{2u}]`.

The next analytic task is now a uniform tail estimate proving (168tt).  Its
failure has a sharp source-only witness: the first `u` where the exact score
variance exceeds the mean primitive curvature.  Success would prove

\[
 \boxed{
 \Phi\text{ log-concave}
 \Longrightarrow A'(d)\le0
 \Longrightarrow J(t)\ge0\text{ on the real spectral ray}.
 }                                                    \tag{168tv}

This still stops short of the full de Branges kernel, but it would orient the
entire scalar separation defect by one source theorem rather than by
oscillatory-band bookkeeping.

## Uniform theorem: the completed theta source is log-concave

The score-variance gate (168tt) admits a coarse uniform proof.  Put
`y=e^{2u}>=1`.  Since `2pi y-3>pi y` and the label ratio is (168tu),

\[
 \boxed{
 \frac{\phi_n(u)}{\phi_1(u)}
 <2n^4e^{-\pi(n^2-1)y}
 \qquad(n\ge2).
 }                                                    \tag{168tw}

The score has the simplified form

\[
 s(q)=\frac92-2\pi q+\frac6{2\pi q-3},
 \qquad q=n^2y.                                     \tag{168tx}

Using `pi<22/7`, `2pi y-3>3`, and `(n^2-1)y>=3`,

\[
 \boxed{
 |s(n^2y)-s(y)|<7(n^2-1)y.
 }                                                    \tag{168ty}

Variance is no larger than the mean squared displacement from the primitive
score.  Combining (168tw)--(168ty) gives

\[
\begin{aligned}
 \operatorname{Var}_{p(u)}(s_n)
 &\le\sum_{n\ge2}p_n|s_n-s_1|^2\\
 &<98\sum_{n\ge2}
 n^4(n^2-1)^2y^2e^{-\pi(n^2-1)y}.                  \tag{168tz}
\end{aligned}
\]

Every summand decreases for `y>=1`.  With `pi>3`, its value at `y=1` is
bounded by

\[
 98\sum_{n\ge2}n^4(n^2-1)^2e^{-3(n^2-1)}<2;        \tag{168ua}
\]

the `n=2` term is below `1.9`, and the tail from `n=3` is below `1/1000` by
geometric comparison.

On the other hand, (168ts) and `q>=1` imply

\[
 -\mathbb E_{p(u)}[\kappa_n]>4\pi>12.              \tag{168ub}

Therefore the curvature dominates the score shear with a factor greater
than six:

\[
 \boxed{
 (\log\Phi(u))''<-10<0
 \qquad(u\ge0).
 }                                                    \tag{168uc}

The zero extension of `Phi` is log-concave on the real line.  Prekopa's
theorem now proves that its autocorrelation is even and log-concave, hence
strictly decreasing on the positive ray:

\[
 \boxed{A'(d)<0\qquad(d>0).}                       \tag{168ud}

Consequently `M` in (168ti) is positive, decreasing, and strictly convex.
Pólya's criterion yields the global scalar orientation theorem

\[
 \boxed{J(t)\ge0\qquad(t\ge0).}                   \tag{168ue}

This proves the source-normalized adjacent-band mechanism for the exact
Green-identity separation defect.  No band endpoints were chosen to fit the
answer: convexity of the autocorrelation tail supplies the canonical pairing
uniformly over the entire real spectral ray.

The scope remains important.  Scalar nonnegativity of `J(t)` does not yet
orient its two-parameter divided-difference kernel in the upper half-plane.
But the last uncontrolled scalar oscillation in the Green identity is now
removed; any remaining failure is genuinely kernel-valued.

## Pólya convexity does not orient the divided-difference kernel

The scalar theorem (168ue) cannot be promoted formally to the de Branges
kernel.  A positive decreasing convex tail is a positive mixture of tent
functions.  For a single tent of width `a`, the cosine transform is, up to a
positive constant,

\[
 J_a(z)=\frac{1-\cos(a\sqrt z)}{z}.                 \tag{168uf}

It is nonnegative for every real `z>=0`, exactly as Pólya's theorem predicts.
But its derivative has the sign of

\[
 r\sin r-2(1-\cos r),
 \qquad r=a\sqrt z.                                 \tag{168ug}

Near `r=0` this expression is negative:

\[
 r\sin r-2(1-\cos r)=-\frac{r^4}{12}+O(r^6).
\]

Immediately to the right of `r=2pi`, it is positive.  Hence `J_a'` changes
sign, and its divided differences have no global scalar orientation.

Therefore

\[
 \boxed{
 M\text{ positive, decreasing, and convex}
 \not\Longrightarrow
 \frac{J(z)-J(w)}{z-w}\text{ has a fixed sign or is a positive kernel}.
 }                                                    \tag{168uh}

This is the sharp scope boundary of the adjacent-band theorem.  It proves
the scalar separation transform is nonnegative, but a single canonical band
block already falsifies the universal kernel lift.

The remaining opportunity is source-specific coupling among tent scales.
The actual theta autocorrelation tail is not one arbitrary convex function:
its curvature measure inherits prime-scale translations and reciprocal
modular reflection.  A de Branges proof must show that those labelled scales
repair the derivative reversals in (168ug), or absorb them into the boundary
phase channel.  Convexity alone has now been exhausted.

## Arithmetic decomposition of the autocorrelation curvature

The actual tent-scale measure retains the theta labels.  Use the exact
translation law

\[
 \phi_n(u)=n^{-1/2}\phi_1(u+\log n).                \tag{168ui}
\]

The `(m,n)` contribution to (168tg) is

\[
\begin{aligned}
 A_{m,n}(d)
 &=\int_0^\infty\phi_m(u)\phi_n(u+d)du\\
 &=(mn)^{-1/2}\int_{\log m}^\infty
 \phi_1(t)
 \phi_1\!\left(t+d+\log\frac nm\right)dt.         \tag{168uj}
\end{aligned}
\]

For fixed product `q=mn`, this becomes

\[
 \boxed{
 A_{m,q/m}(d)=q^{-1/2}\int_{\log m}^\infty
 \phi_1(t)
 \phi_1\!\left(t+d+\log q-2\log m\right)dt.
 }                                                    \tag{168uk}

Thus the autocorrelation inherits exactly the product--ratio coordinates:

\[
 q=mn,
 \qquad
 \delta_m=\log\frac{q}{m^2}.                       \tag{168ul}
\]

The divisor reflection `m mapsto q/m` sends

\[
 \delta_m\longmapsto-\delta_m                       \tag{168um}
\]

and moves the lower endpoint from `log m` to `log(q/m)`.  Hence reciprocal
pairing reverses the separation shift while changing the primitive integral
only by the finite interval between those two seam endpoints.

This identifies the source of the repair missing from the generic convex-
tail model.  A lone tent scale has an unpaired derivative reversal.  A theta
divisor box contains:

\[
 \boxed{
 \text{shift }+\delta_m
 +\text{reflected shift }-\delta_m
 +\text{finite modular seam current}.
 }                                                    \tag{168un}

The full separation channel therefore has the Dirichlet decomposition

\[
 \boxed{
 A(d)=\sum_{q\ge1}q^{-1/2}
 \sum_{m\mid q}
 \int_{\log m}^\infty
 \phi_1(t)\phi_1(t+d+\delta_m)dt.
 }                                                    \tag{168uo}

This is the faithful arithmetic object on which to test kernel orientation.
The next theorem should not ask whether every tent transform is monotone—it
is not.  It should ask whether each completed reciprocal divisor pair,
including its finite endpoint current, has a nonnegative de Branges
divided-difference kernel, or whether positivity appears only after summing
the whole divisor box.

The sharp falsifier is now canonical: the smallest `q`, reciprocal divisor
pair, and spectral pair `(z,w)` for which the fully endpoint-completed block
has negative orientation.  No post-hoc regrouping of separation bands is
allowed.

## Reciprocal divisor pairs are exact MLR endpoint averages

Let `m<=n` and put

\[
 \delta=\log\frac nm\ge0.
\]

In the reflected term `A_{n,m}`, translate the integration variable by
`-delta`.  The two lower endpoints then agree, and (168uj) becomes

\[
\boxed{
\begin{aligned}
 A_{m,n}(d)+A_{n,m}(d)
 =(mn)^{-1/2}\int_{\log m}^\infty
 \big[&\phi_1(t)\phi_1(t+d+\delta)\\
 &+\phi_1(t+\delta)\phi_1(t+d)\big]dt.
\end{aligned}
}                                                     \tag{168up}
\]

Define the translation likelihood ratio

\[
 r_\delta(t)=\frac{\phi_1(t+\delta)}{\phi_1(t)}.     \tag{168uq}
\]

Then the paired integrand factors as

\[
 \boxed{
 \phi_1(t)\phi_1(t+d)
 \left[r_\delta(t)+r_\delta(t+d)\right].
 }                                                    \tag{168ur}

The primitive strong-log-concavity theorem gives

\[
 \partial_t\log r_\delta(t)
 =s_1(t+\delta)-s_1(t)<0,                           \tag{168us}
\]

so `r_delta` is strictly decreasing.  Reciprocal modular reflection has
therefore converted the raw shifted pair into an exact MLR-oriented average
of the likelihood ratio at the two endpoints of the separation interval.

This is stronger than the unlabelled autocorrelation theorem.  It shows how
the arithmetic involution acts locally on every divisor chord:

\[
 \boxed{
 \text{reciprocal label exchange}
 \longrightarrow
 \text{endpoint average of one decreasing likelihood ratio}.
 }                                                    \tag{168ut}

The remaining kernel calculation should now be performed on (168ur).  The
candidate repair is the difference

\[
 r_\delta(t)-r_\delta(t+d)>0,                       \tag{168uu}

which measures the exact MLR reserve transported across the separation.
If the oscillatory divided difference can be integrated by parts into this
reserve with a nonnegative wave Gram factor, each reciprocal pair closes.
If a residual term depends on the sum rather than the difference of the two
endpoint ratios, divisor-pair positivity is still too strong and the whole
box must participate.

## Exact kernel criterion and a complete-monotonicity no-go

The divided difference of the sine propagator has a convolution identity.
For `G_z(d)=sin(sqrt(z)d)/sqrt(z)`, Laplace transformation in `d` gives

\[
 \boxed{
 \frac{G_{\bar w}(d)-G_z(d)}{z-\bar w}
 =\int_0^dG_z(t)G_{\bar w}(d-t)dt.
 }                                                    \tag{168uv}

Substituting into (168th) and putting `p=t`, `q=d-t` yields

\[
\boxed{
 \frac{\overline{J(w)}-J(z)}{z-\bar w}
 =\iint_{[0,\infty)^2}
 A(p+q)G_z(p)\overline{G_w(q)}dpdq.
}                                                     \tag{168uw}
\]

Thus the forcing divided difference is the pullback of the Hankel kernel

\[
 \mathcal A(p,q)=A(p+q).                            \tag{168ux}

By the Bernstein--Widder theorem, this Hankel kernel is positive
semidefinite for all finite packets exactly when `A` is completely monotone:

\[
 (-1)^kA^{(k)}(d)\ge0
 \qquad(k\ge0,d\ge0).                              \tag{168uy}

The theta autocorrelation fails this criterion at the first even derivative.
Modular completion makes the bilateral source even, so the positive-chamber
derivative satisfies

\[
 \Phi'(0)=0.                                       \tag{168uz}

Twice differentiating (168tg) at zero and integrating by parts gives

\[
\begin{aligned}
 A''(0)
 &=\int_0^\infty\Phi(u)\Phi''(u)du\\
 &=-\Phi(0)\Phi'(0)-\int_0^\infty(\Phi'(u))^2du\\
 &=-\int_0^\infty(\Phi'(u))^2du<0.                \tag{168va}
\end{aligned}
\]

Complete monotonicity would require `A''(0)>=0`.  Therefore

\[
 \boxed{
 A(p+q)\text{ is not a positive Hankel kernel, and the separation defect
 cannot be a standalone Gram channel.}
 }                                                    \tag{168vb}

This is stronger than the tent counterexample (168uh): it falsifies the
positive-kernel lift for the actual completed theta autocorrelation, not just
for the generic convex class.

The consequence for the Green program is decisive.  The defect in (168qw)
must combine with the boundary Wronskian before positivity is tested.
Attempting to prove either term positive separately is impossible.  The live
object is the completed Schur complement

\[
 \boxed{
 \text{boundary phase Wronskian}
 +\text{indefinite autocorrelation Hankel channel}.
 }                                                    \tag{168vc}

Modular arithmetic is required to repair a concrete negative curvature
direction of `A(p+q)`; it is not merely needed to improve a weak scalar
estimate.

## Bilateral reflection gives the canonical Hankel-to-Toeplitz repair

The required repair exists canonically before spectral readout.  Let `f` be
the zero extension of `Phi` to the full real scale line, and let `T_p` denote
translation by `p`.  Its translation Gram kernel is

\[
 \langle T_pf,T_qf\rangle=A(|p-q|).                 \tag{168vd}
\]

Translations in opposite chambers have cross Gram

\[
 \langle T_pf,T_{-q}f\rangle=A(p+q).                \tag{168ve}
\]

Therefore the full reflected two-chamber kernel is

\[
 \boxed{
 \mathbb A(p,q)=
 \begin{pmatrix}
 A(|p-q|)&A(p+q)\\
 A(p+q)&A(|p-q|)
 \end{pmatrix}\succeq0.
 }                                                    \tag{168vf}

Diagonalizing chamber reflection gives the fixed and anti-fixed kernels

\[
 \boxed{
 A(|p-q|)+A(p+q)\succeq0,
 \qquad
 A(|p-q|)-A(p+q)\succeq0.
 }                                                    \tag{168vg}

These are simply the Gram kernels of the even and odd translation features

\[
 T_pf\pm T_{-p}f.                                   \tag{168vh}

This is the exact Hankel-to-Toeplitz completion suggested by the Carrier
geometry.  The one-sided Green calculation sees only the cross-chamber
Hankel block `A(p+q)`, which is indefinite when mis-typed as a same-space
kernel.  Bilateral modular sewing restores the same-chamber Toeplitz block
`A(|p-q|)`, making both reflection sectors genuine Gram spaces.

The remaining identity is now exceptionally sharp:

\[
 \boxed{
 \text{Does the completed boundary Wronskian in (168qw) pull back to
 }A(|p-q|)\text{ with the normalization required by (168vf)?}
 }                                                    \tag{168vi}

If yes, the forcing defect and boundary phase combine into the positive
fixed/anti Gram kernels (168vg), closing the de Branges energy identity.  If
the coefficient differs, or an endpoint delta remains, the mismatch is a
finite boundary secular defect analogous to the level-44 repair scalar.

This is no longer a conjecture that “reflection should help.”  Reflection
has a unique source-derived positive completion, and (168vi) is an exact
identity-or-falsifier test.

## Boundary-Wronskian audit: exact coefficient, one missing seam kernel

The test (168vi) can be evaluated directly.  Rewrite the tail feature as

\[
 F_z(q)=\int_0^\infty\Phi(q+p)G_z(p)dp.             \tag{168vj}
\]

Its positive wave bulk is therefore the pullback of

\[
 B(p,r)=\int_0^\infty\Phi(q+p)\Phi(q+r)dq.          \tag{168vk}

If `p>=r`, translating by `r` gives

\[
 B(p,r)=\int_r^\infty\Phi(t+p-r)\Phi(t)dt.
\]

Hence, symmetrically,

\[
 \boxed{
 B(p,r)=A(|p-r|)-S(p,r),
 }                                                    \tag{168vl}
\]

where the finite seam kernel is

\[
 \boxed{
 S(p,r)=\int_0^{\min(p,r)}
 \Phi(t)\Phi(t+|p-r|)dt.
 }                                                    \tag{168vm}

Now divide the Green identity (168qw) by `z-bar w`.  By (168uw), the forcing
term pulls back to the Hankel kernel `A(p+r)`.  Therefore the boundary
Wronskian divided difference pulls back exactly to

\[
\boxed{
 B(p,r)-A(p+r)
 =\underbrace{A(|p-r|)-A(p+r)}_{\text{positive odd-reflection Gram}}
 -S(p,r).
}                                                     \tag{168vn}

This answers (168vi):

* the Toeplitz coefficient is exactly one;
* the reflection sign is the odd/Dirichlet sign;
* the one-sided chart omits precisely the finite initial seam `S`.

There is no diffuse normalization error and no additional bulk defect.  The
one-sided boundary phase is the correct odd bilateral Gram kernel minus one
explicit seam channel.

The modular sewing theorem is now an equality target:

\[
 \boxed{
 \text{reflected chamber boundary current}=S(p,r).
 }                                                    \tag{168vo}

If bilateral completion supplies (168vo), then (168vn) becomes the positive
kernel `A(|p-r|)-A(p+r)`, closing the Dirichlet de Branges energy identity.
If it supplies a different coefficient or orientation, the difference is
the final finite boundary secular defect.

This is the closest point yet to a complete source-derived Gram theorem: all
continuous bulk terms are already typed and positive after reflection; only
the finite seam incidence remains to be matched.

## Bilateral extension supplies the seam exactly

The equality target (168vo) is forced by the reflected integration domain.
Extend the positive-chamber source as a separate reflected copy and extend
the bulk coordinate from `q>=0` to the full bilateral line.  The additional
crossing interval is

\[
 -\min(p,r)\le q<0.
\]

On that interval both translated source arguments remain in the admitted
positive chart.  If `p>=r`, put `t=q+r`; then

\[
\begin{aligned}
 \int_{-r}^0\Phi(q+p)\Phi(q+r)dq
 &=\int_0^r\Phi(t+p-r)\Phi(t)dt\\
 &=S(p,r).                                          \tag{168vp}
\end{aligned}
\]

The case `r>=p` is symmetric.  Therefore

\[
 \boxed{
 \text{reflected chamber boundary current}=S(p,r)
 }                                                    \tag{168vq}

with coefficient exactly one and no sign choice.

Adding (168vq) to the one-sided boundary form (168vn) proves the raw
bilateral Dirichlet Gram theorem

\[
 \boxed{
 \mathcal K_{\rm raw}(p,r)
 =A(|p-r|)-A(p+r)\succeq0.
 }                                                    \tag{168vr}

Equivalently, it is the Gram kernel of the odd reflected source features

\[
 T_pf-T_{-p}f.                                      \tag{168vs}

This is the first complete coupled positivity theorem in the wave lane:

\[
 \boxed{
 \text{positive one-sided bulk}
 +\text{indefinite forcing Hankel block}
 +\text{reflected finite seam}
 =\text{positive odd bilateral Gram kernel}.
 }                                                    \tag{168vt}

The scope boundary is now crucial.  The theorem applies to the raw boundary
phase pair `(C,B)` generated by the forced Dirichlet wave.  The physical
completed quotient includes the archimedean factor and the Clark/logarithmic
differential used to form `H` and `D`.  Those operations are not yet proved
to preserve (168vr).  They may introduce the finite Jordan channels already
seen in the differentiated scale-flow identity.

Accordingly, (168vr) is not an RH proof.  It proves that modular reflection
repairs the entire continuous wave/separation obstruction before physical
completion.  The remaining calculation is finite-channel: apply the exact
completion operator to the raw Gram identity and classify every new boundary
and Jordan term.  No uncontrolled continuous bulk remains.

## Physical completion is a rank-two spectral Jordan extension

The raw phase pair in (168sx) is not yet the physical de Branges pair.  The
completed quotient readout is

\[
 X(z)=(1+4z)C(z)=(1+4z)F_z(0).                     \tag{168vu}
\]

Its spectral derivative is

\[
 \boxed{
 X'(z)=4F_z(0)+(1+4z)U_z(0),
 \qquad U_z=\partial_zF_z.
 }                                                    \tag{168vv}

Differentiating the forced wave equation (168qv) gives

\[
 \boxed{
 U_z''+zU_z=-F_z,
 \qquad U_z(\infty)=U_z'(\infty)=0.
 }                                                    \tag{168vw}

Thus physical completion replaces the one-channel forced wave by the Jordan
system

\[
 \boxed{
 \begin{pmatrix}F\\U\end{pmatrix}''
 +z\begin{pmatrix}F\\U\end{pmatrix}
 =\begin{pmatrix}\Phi\\-F\end{pmatrix}.
 }                                                    \tag{168vx}

This sharpens the scope statement following (168vt).  The completion is not
merely a finite matrix acting on the raw boundary pair: it introduces one
spectral tangent channel `U`.  But it is still finite in channel number and
source-derived; no growing derivative tower is required for the first
de Branges kernel.

The physical phase is now

\[
 E_{\rm phys}(z)=X(z)-iX'(z),                       \tag{168vy}

so the exact remaining calculation is the coupled Green identity for
`(F,U)`.  The raw `(F,F)` continuous bulk is already the positive reflected
Gram kernel (168vr).  The only new terms arise from:

1. the Jordan forcing `-F` in (168vw);
2. the finite boundary combination `4F+(1+4z)U`;
3. possible cross terms between the raw and tangent channels.

This is the faithful final finite-channel obstruction.  If the coupled
identity diagonalizes into positive reflected Gram channels plus a
source-fixed boundary repair, the Hermite--Biehler theorem closes.  If one
negative Jordan polarization survives, it is the exact obstruction—matching
the earlier scale-flow analysis rather than contradicting it.

## Exact Jordan Green identity

Apply Green's formula to the tangent equations (168vw) at `z` and `w`.
The terminal boundary vanishes, leaving

\[
\boxed{
\begin{aligned}
 (z-\bar w)\int_0^\infty U_z\overline{U_w}dq
 ={}&U_z'(0)\overline{U_w(0)}
 -U_z(0)\overline{U_w'(0)}\\
 &+\int_0^\infty
 \left(U_z\overline{F_w}-F_z\overline{U_w}\right)dq.
\end{aligned}
}                                                     \tag{168vz}
\]

The new bulk term is a single antisymmetric polarization between the raw and
tangent channels.  No new theta forcing appears: differentiation killed the
source derivative because `Phi` is spectral-parameter independent.

The mixed Green identities are similarly

\[
\boxed{
\begin{aligned}
 (z-\bar w)\int F_z\overline{U_w}
 ={}&W_{F,U}(0)
 +\int\Phi\overline{U_w}
 +\int F_z\overline{F_w},\\
 (z-\bar w)\int U_z\overline{F_w}
 ={}&W_{U,F}(0)
 -\int F_z\overline{F_w}
 -\int U_z\Phi.
\end{aligned}
}                                                     \tag{168wa}
\]

Here each `W` is the corresponding spatial boundary Wronskian at zero; all
integrals are over the positive scale chamber.

After the raw reflected repair (168vt), the physical completion therefore
has exactly one live continuum polarization:

\[
 \boxed{
 \langle U_z,F_w\rangle-\langle F_z,U_w\rangle.
 }                                                    \tag{168wb}

It is skew under exchange of the two channels and cannot be declared
positive separately.  The archimedean boundary combination in (168vv) must
convert it into either an exact boundary term or a positive symplectic Gram
pair.

This is the same Jordan obstruction previously found in Mellin-scale flow,
now derived from the fixed wave realization.  The agreement is structural,
not independent evidence: spectral differentiation of any forced resolvent
creates precisely this tangent coupling.

The next calculation is finite and explicit: substitute
`X=(1+4z)F(0)` and `X'=4F(0)+(1+4z)U(0)` into the physical Bezoutian, then use
(168vz)--(168wa) to eliminate every boundary product.  The surviving bulk
matrix will decide whether the completion is Hilbert-positive, Krein-signed,
or repaired by one additional modular seam line.

## Physical Bezoutian equals one rank-one repair plus one mixed channel

The boundary substitution can be performed before any further Green
manipulation.  Put

\[
 a(z)=1+4z,
 \qquad f_z=F_z(0),
 \qquad u_z=U_z(0).
\]

Then

\[
 X(z)=a(z)f_z,
 \qquad X'(z)=4f_z+a(z)u_z.                         \tag{168wc}
\]

Direct expansion gives

\[
\boxed{
\begin{aligned}
 &\frac{
 X(z)\overline{X'(w)}-X'(z)\overline{X(w)}
 }{z-\bar w}\\
 &\qquad=
 16f_z\overline{f_w}
 +a(z)a(\bar w)
 \frac{f_z\overline{u_w}-u_z\overline{f_w}}
 {z-\bar w}.
\end{aligned}
}                                                     \tag{168wd}

The coefficient `16` is forced by

\[
 \frac{4(a(z)-a(\bar w))}{z-\bar w}=16.            \tag{168we}

Thus archimedean completion supplies exactly one positive rank-one boundary
channel

\[
 16|f\rangle\langle f|,                             \tag{168wf}

and all remaining delicacy is concentrated in the mixed raw--tangent
Bezoutian

\[
 \boxed{
 \frac{f_z\overline{u_w}-u_z\overline{f_w}}
 {z-\bar w}.
 }                                                    \tag{168wg}

This is the physical counterpart of the level-44 mechanism:

\[
 \boxed{
 \text{one mixed defect channel}
 +\text{one source-fixed rank-one completion repair}.
 }                                                    \tag{168wh}

No coefficient is fitted, and no higher boundary rank appears.  The next
step is now a secular theorem: use (168vz)--(168wa) and the reflected raw Gram
identity to determine whether the negative index of (168wg) is at most one
and whether the exact coefficient `16` repairs it.  A second negative
direction would falsify the proposed completion mechanism immediately.

## Scope correction: the bilateral Gram space includes the seam coordinate

Equation (168vr) proves positivity after adjoining the reflected seam current
`S`.  It does not prove that the original scalar boundary pair `(C,B)` alone
is Hermite--Biehler.  The equality is

\[
 \frac{W_{C,B}(z,w)}{z-\bar w}
 +\mathcal S(z,w)
 =\mathcal G_{\rm odd}(z,w)\succeq0,               \tag{168wi}
\]

where `mathcal S` is the spectral pullback of (168vm).  The seam is an actual
boundary coordinate, not a zero term.  Discarding it before projecting to a
scalar phase would repeat the same typing error as discarding the finite
modular sewing current in the prime recursion.

Therefore the enlarged raw Gram theorem cannot by itself imply real zeros of
`C` or a zero-index logarithmic derivative.

## The mixed channel is the logarithmic-derivative kernel of `C`

Away from zeros of `C`, put

\[
 r(z)=\frac{U_z(0)}{F_z(0)}=\frac{C'(z)}{C(z)}.      \tag{168wj}
\]

Then the mixed channel (168wg) factors exactly as

\[
\boxed{
 \frac{f_z\overline{u_w}-u_z\overline{f_w}}
 {z-\bar w}
 =-f_z\overline{f_w}
 \frac{r(z)-\overline{r(w)}}{z-\bar w}.
}                                                     \tag{168wk}

Define the Nevanlinna kernel

\[
 K_r(z,w)=\frac{r(z)-\overline{r(w)}}{z-\bar w}.    \tag{168wl}
\]

After the diagonal congruence by `a(z)f_z`, the physical Bezoutian (168wd)
is therefore governed by

\[
 \boxed{
 16\left|\frac1{a(z)}\right\rangle
 \left\langle\frac1{a(w)}\right|
 -K_r(z,w).
 }                                                    \tag{168wm}

Thus the proposed one-defect theorem is exactly a generalized-Nevanlinna
index statement for the logarithmic derivative `C'/C`.  If `C` had only real
zeros, `r` would be anti-Herglotz and `-K_r` positive; but establishing that
is already a real-zero theorem and cannot be inferred from the enlarged
seam Gram space.

The correct secular target is

\[
 \boxed{
 \operatorname{ind}_-(-K_r)\le1
 \quad\text{and the unique negative direction is the vector }1/a.
 }                                                    \tag{168wn}

This is now a precise conjecture, not a conclusion.  A packet on which
`-K_r` has two independent negative directions is the sharp falsifier; one
such direction orthogonal to `1/a` already defeats the rank-one repair of
strength `16`.

## The rank-one term is exactly the real carrier zero

The secular presentation has a final exact simplification.  Since

\[
 X(z)=a(z)C(z),
 \qquad a(z)=1+4z,
\]

its logarithmic derivative is

\[
 \frac{X'}X=r(z)+\frac4{a(z)}.                     \tag{168wo}

The divided-difference kernel of the carrier term is

\[
 \frac{
 4/a(z)-4/a(\bar w)
 }{z-\bar w}
 =-\frac{16}{a(z)a(\bar w)}.                       \tag{168wp}

Therefore

\[
 \boxed{
 -K_{X'/X}(z,w)
 =\frac{16}{a(z)a(\bar w)}-K_r(z,w).
 }                                                    \tag{168wq}

This is exactly the kernel in (168wm).  The positive rank-one channel is the
canonical logarithmic-derivative contribution of the real carrier zero

\[
 a(z)=0
 \quad\Longleftrightarrow\quad
 z=-\frac14.                                        \tag{168wr}

Thus the coefficient `16` is fully explained, but the interpretation as an
independent repair mechanism was too optimistic.  Multiplication by one real
linear factor adds one positive rank-one zero kernel; it does not supply new
arithmetic control over the remaining zeros of `C`.

For a real entire function with the required canonical-product convergence,
each real zero contributes a positive rank-one term to `-K_{X'/X}`, while a
nonreal conjugate packet contributes an indefinite block.  Hence

\[
 \boxed{
 -K_{X'/X}\succeq0
 \quad\Longleftrightarrow\quad
 X\text{ has only real zeros}
 }                                                    \tag{168ws}

under the standard growth and polynomial-factor audit.

This closes the secular loop honestly.  The physical Bezoutian has not
reduced RH to a new rank-one inequality; it has recovered the classical
logarithmic-derivative real-zero kernel, with the carrier contribution typed
correctly.  The genuine source advance remains earlier: the continuous raw
wave/separation obstruction admits an exact bilateral Gram completion.  What
is still missing is a proof that the physical projection from that enlarged
Gram space to `X` preserves positivity rather than discarding the seam
coordinate.

The next useful attack must therefore target that projection map itself.  A
claim that the carrier rank-one term repairs an otherwise arbitrary
logarithmic-derivative kernel would merely restate the desired conclusion.

## Scope correction: finite seam interval does not mean finite-rank seam

The kernel `S` in (168vm) is supported on a finite initial interval for each
pair `(p,r)`, but it is not a finite-dimensional boundary channel.  Near the
corner `p=r=0`, smoothness and positivity of `Phi` give

\[
 \boxed{
 S(p,r)=\Phi(0)^2\min(p,r)+O((p+r)\min(p,r)).
 }                                                    \tag{168wt}

The leading kernel `min(p,r)` is the Brownian covariance kernel and has
infinite rank on every nontrivial interval.  Equivalently, increments on
arbitrarily many disjoint seam subintervals give linearly independent Gram
directions.  The lower-order perturbation cannot collapse all of them.

Therefore

\[
 \boxed{\operatorname{rank}S=\infty.}              \tag{168wu}

This corrects every description of `S` as a “finite boundary secular line.”
It is finite in geometric extent and canonical in incidence, but infinite in
Hilbert-space rank.

The consequence is decisive.  The rank-one carrier contribution (168wf)
cannot repair the loss of the entire seam coordinate by itself.  A valid
operator proof must retain the seam Hilbert space in the physical state and
show that the scalar completed function `X` is obtained by a positivity-
preserving Schur complement, compression, or boundary determinant.

The viable architecture is therefore

\[
 \boxed{
 \text{bilateral odd Gram space}
 =\text{one-sided wave space}\oplus\text{seam space}
 \longrightarrow
 \text{physical scalar transfer by a typed Schur complement}.
 }                                                    \tag{168wv}

Simply projecting away the seam subtracts the infinite-rank kernel `S` and
need not preserve positivity.  This is now the central operator obstruction.
The next theorem must construct the actual block map and prove its Schur
complement equals the physical Bezoutian; no scalar rank-one argument can
substitute for it.

## Exact seam feature and the cut decomposition of translation

The seam kernel has a canonical Gram realization.  For `p>=0`, define the
future-tail and boundary-crossing features

\[
 g_p(t)=\Phi(t+p),
 \qquad
 h_p(t)=\mathbf 1_{0\le t\le p}\Phi(p-t),
 \qquad t\ge0.                                     \tag{168ww}
\]

Their Gram kernels are

\[
 \langle g_p,g_r\rangle=B(p,r)                     \tag{168wx}
\]

and, if `p>=r`,

\[
\begin{aligned}
 \langle h_p,h_r\rangle
 &=\int_0^r\Phi(p-t)\Phi(r-t)dt\\
 &=\int_0^r\Phi(s+p-r)\Phi(s)ds\\
 &=S(p,r).                                          \tag{168wy}
\end{aligned}
\]

Thus

\[
 \boxed{S(p,r)=\langle h_p,h_r\rangle.}            \tag{168wz}
\]

Combining with (168vl),

\[
 \boxed{
 A(|p-r|)
 =\langle g_p,g_r\rangle+\langle h_p,h_r\rangle.
 }                                                    \tag{168xa}
\]

This is the cut decomposition of one bilateral translation feature: `g_p`
is the part remaining in the positive chamber after translation, while
`h_p` is the part that crossed the seam.  The map

\[
 T_pf\longmapsto g_p\oplus h_p                     \tag{168xb}

is an isometry from the translated source orbit into

\[
 \mathcal H_{\rm tail}\oplus\mathcal H_{\rm seam},
 \qquad
 \mathcal H_{\rm tail}=\mathcal H_{\rm seam}=L^2(\mathbb R_+).
\]

For a compactly supported translation packet `c(p)`, the spectral seam
feature is

\[
 \boxed{
 s_c(t)=\int_t^\infty\Phi(p-t)c(p)dp.
 }                                                    \tag{168xc}
\]

Accordingly, on the packet space the pulled-back seam kernel is

\[
 \iint S(p,r)c(p)\overline{d(r)}dpdr
 =\langle s_c,s_d\rangle.                          \tag{168xd}
\]

This identity does **not** automatically extend to the bare spectral wave
`c(p)=G_z(p)`: that wave is not in the translation-packet Hilbert space.
Thus the former formal notation `s_z` requires a cutoff, a genuine resolvent
domain, or a source-derived renormalized boundary pairing.  It is not an
ordinary `L^2` seam vector.

On admissible packets, the raw completed energy can be written without
unnamed terms:

\[
 \boxed{
 \mathcal G_{\rm odd}[c,d]
 =\mathcal W_{C,B}[c,d]+\langle s_c,s_d\rangle.
 }                                                    \tag{168xe}
\]

Here `mathcal W_{C,B}` is the scalar boundary Wronskian kernel.  Therefore
passing from the positive bilateral energy to the scalar phase subtracts the
Gram norm of the explicit seam feature `s_c`.  It is a Krein-type quotient,
not a Hilbert compression.

The required Schur-complement theorem is now concrete but must first be
posed on the packet completion: find a source-derived constraint or coupling
operator `Gamma` such that

\[
 s_c=\Gamma\,v_c                                  \tag{168xf}
\]

for the retained physical bulk feature `v_z`, and show the block energy has
positive Schur complement after imposing that constraint.  If no bounded
contractive `Gamma` exists, scalar phase projection necessarily loses
positivity.

## Exact prime-power expansion of the logarithmic current

Let

\[
 \mathcal H_{\log}(q)=\sum_{n\ge1}(\log n)h_n(q).   \tag{168as}
\]

Use

\[
 \log n=\sum_p v_p(n)\log p
\]

and expand the valuation as `v_p(n)=sum_{k>=1}1_{p^k divides n}`.  The exact
theta scaling law gives

\[
 \sum_{p^k\mid n}h_n(q)
 =p^{-k/2}h_{\rm agg}(q+k\log p),                    \tag{168at}
\]

with the common fixed normalization of the forcing.  Therefore

\[
 \boxed{
 \mathcal H_{\log}(q)
 =\sum_p(\log p)\sum_{k\ge1}
 p^{-k/2}h_{\rm agg}(q+k\log p).
 }                                                     \tag{168au}
\]

Equivalently, summing over prime powers `d=p^k`,

\[
 \boxed{
 \mathcal H_{\log}(q)
 =\sum_{d\text{ prime power}}
 \Lambda_{\rm vM}(d)d^{-1/2}
 h_{\rm agg}(q+\log d),
 }                                                     \tag{168av}
\]

where `Lambda_vM(p^k)=log p` is the von Mangoldt weight.

Every coefficient and every shifted forcing in (168au) is nonnegative.  This
is substantially more structure than the bare statement
`mathcal H_log>=0`: the repair is an exact prime-power transfer operator

\[
 \mathcal V
 =\sum_{d\text{ prime power}}
 \Lambda_{\rm vM}(d)d^{-1/2}T_{\log d}.             \tag{168aw}
\]

It is the real-scale source counterpart of `-zeta'/zeta`.  Completion poles
and analytic continuation have not been invoked; (168av) is an identity of
positive shifted source tails.

The final Schur-complement question can now be attacked as an operator
comparison between the primitive seam Gram form and the Volterra response to
`mathcal V h_agg`.  If positivity fails, the falsifier must identify the
first prime-power shift or coherent combination whose matrix coupling
overcomes the positive weights.  If it succeeds, prime powers are the
source-derived repair channels rather than a posteriori spectral data.

## Prime shifts are coisometries with positive seam defects

Positive coefficients in (168aw) do not make `mathcal V` a positive
operator.  On `L^2(0,infinity)`, let

\[
 (T_af)(q)=f(q+a),\qquad a>0.                       \tag{168ax}
\]

Its adjoint is

\[
 (T_a^*g)(r)=\mathbf1_{[a,\infty)}(r)g(r-a).        \tag{168ay}
\]

Hence

\[
 T_aT_a^*=I,
 \qquad
 T_a^*T_a=I-P_{[0,a)},                              \tag{168az}
\]

where `P_[0,a)` is restriction to the initial seam interval.  Equivalently,

\[
 \boxed{
 \|f\|^2-\|T_af\|^2
 =\int_0^a|f(q)|^2dq\ge0.
 }                                                     \tag{168ba}
\]

Thus a prime-power shift is a coisometry, and its only canonical positive
operator contribution is the finite defect projection

\[
 \boxed{
 D_d=I-T_{\log d}^*T_{\log d}
 =P_{[0,\log d)}.
 }                                                     \tag{168bb}
\]

This is precisely the finite modular sewing current that cancels the false
singularities of a divided prime multiplier.  It is not optional endpoint
bookkeeping; it is the defect operator of the one-sided arithmetic shift.

One might try to sum these defects into

\[
 \boxed{
 \mathcal D_{\rm naive}
 =\sum_{d\text{ prime power}}
 \Lambda_{\rm vM}(d)d^{-1/2}P_{[0,\log d)}.
 }                                                     \tag{168bc}
\]

but the convergence audit rejects this as an operator on a common unrestricted
`L^2` feature.  Indeed, at every fixed `q`, all sufficiently large prime
intervals contain `q`, while

\[
 \sum_p\frac{\log p}{\sqrt p}=\infty.               \tag{168bd}
\]

Thus `mathcal D_naive` is infinite on every nonzero feature supported near
the seam.  Termwise positivity does not authorize forgetting which shifted
theta tail each defect acts upon.

The faithful positive object must retain the payload:

\[
 \boxed{
 \left\{
 \Lambda_{\rm vM}(d)d^{-1/2},
 \ P_{[0,\log d)},
 \ T_{\log d}h_{\rm agg}
 \right\}_{d=p^k}.
 }                                                     \tag{168be}
\]

The superexponential theta decay occurs in the last component and can make
the resulting source quadratic form convergent.  Removing that component
before summation creates the divergence (168bd).

The distinction is now exact:

\[
 \text{shift bulk }T_{\log d}
 \text{ carries transport but no sign,}
\]

\[
 \text{defect }P_{[0,\log d)}
 \text{ carries positive boundary energy.}
\]

Accordingly the next inequality is not positivity of `mathcal V` or of the
divergent `mathcal D_naive`.  It is whether the differentiated antisymmetric
seam Gram form is dominated by the convergent **payload-retaining defect
quadratic form** obtained from (168be) through the four-state Volterra
response.  This is the first correctly typed positive candidate produced by
the prime recursion.

## Valuation-depth defect form is positive and convergent

Fix a prime `p`, put `ell_p=log p`, and retain its valuation filtration.  The
depth-`k` payload is

\[
 h_{p,k}=T_{k\ell_p}h_{\rm agg}.                    \tag{168bf}
\]

Applying one further prime shift gives the exact defect energy

\[
\begin{aligned}
 \|h_{p,k}\|_2^2-\|T_{\ell_p}h_{p,k}\|_2^2
 &=\|T_{k\ell_p}h_{\rm agg}\|_2^2
   -\|T_{(k+1)\ell_p}h_{\rm agg}\|_2^2\\
 &=\int_{k\ell_p}^{(k+1)\ell_p}
 |h_{\rm agg}(r)|^2dr\ge0.                          \tag{168bg}
\end{aligned}
\]

The faithful arithmetic defect quadratic form is therefore

\[
 \boxed{
 \mathfrak D_\theta
 =\sum_p(\log p)\sum_{k\ge1}p^{-k/2}
 \int_{k\log p}^{(k+1)\log p}|h_{\rm agg}(r)|^2dr.
 }                                                     \tag{168bh}
\]

Every summand is positive.  Unlike (168bc), each projection remains attached
to its valuation-depth payload.

The standard theta-tail bound has the form

\[
 |h_{\rm agg}(r)|
 \le C\exp(Ar-c e^{2r})
 \qquad(r\ge0)                                      \tag{168bi}
\]

for fixed positive constants `A,c,C`.  On the interval in (168bg),
`e^{2r}>=p^{2k}`.  Hence its contribution is bounded by a polynomial in
`p^k` times

\[
 (\log p)p^{-k/2}e^{-2c p^{2k}}.                    \tag{168bj}
\]

The double sum over primes and depths converges absolutely.  Thus

\[
 \boxed{0\le\mathfrak D_\theta<\infty.}             \tag{168bk}
\]

No analytic continuation or cancellation is used in this convergence proof;
it is a real-source theorem.

The form `mathfrak D_theta` is the first fully constructed positive arithmetic
boundary energy in the RH lane.  It is not yet the desired Schur complement:
the differentiated four-state response must be inserted before comparing it
with the seam Gram form.  But positivity, source typing, and convergence of
the repair reservoir are now established independently of RH.

## Spectral lift of the valuation-defect reservoir

The Volterra response commutes exactly with right translation.  If `A_h`
denotes (168z) for forcing `h`, then

\[
\begin{aligned}
 A_{T_ah}(q,z)
 &=i\int_q^\infty\sin(z(r-q))h(r+a)dr\\
 &=A_h(q+a,z)
 =(T_aA_h)(q,z).                                    \tag{168bl}
\end{aligned}
\]

Thus the prime valuation defects lift from the forcing to the physical
antisymmetric response without an error term.

Define the kernel

\[
 \boxed{
 \Lambda_{\rm def}(z,w)
 =\sum_p(\log p)\sum_{k\ge1}p^{-k/2}
 \int_{k\log p}^{(k+1)\log p}
 \overline{A(r,w)}A(r,z)dr.
 }                                                     \tag{168bm}
\]

For every finite spectral packet `(z_i,c_i)`,

\[
 \sum_{i,j}\overline{c_i}
 \Lambda_{\rm def}(z_i,z_j)c_j
 =\sum_p(\log p)\sum_{k\ge1}p^{-k/2}
 \int_{k\log p}^{(k+1)\log p}
 \left|\sum_jc_jA(r,z_j)\right|^2dr\ge0.           \tag{168bn}
\]

Hence `Lambda_def` is a positive-definite kernel.  The theta-tail estimates
used in (168bi)--(168bj), together with local uniformity in bounded spectral
sets, give convergence and analyticity on finite packets.

This is the first explicit candidate for the positive comparison operator in
(170).  The sharp inequality is now

\[
 \boxed{
 \Lambda_{\rm def}(z,w)
 -a(z)\overline{a(w)}\ge0,
 \qquad a(z)=F(z)-F(-z).
 }                                                     \tag{168bo}
\]

Equivalently, packetwise,

\[
 a^*\Lambda_{\rm def}^\dagger a\le1.               \tag{168bp}
\]

Two audits remain before treating (168bo) as the RH theorem.  First, the
relative differentiated Green identity must show that `Lambda_def` is
exactly its Schur-complement operator rather than merely a positive
suboperator.  Second, the normalization of `a` must be matched to the Clark
derivative, not the undifferentiated sine seam.  These are algebraic/source
identification problems; positivity and convergence of the candidate kernel
itself are already proved.

## Small-`z` scalar falsifier for the defect kernel

Let

\[
 B(r)=\int_r^\infty(s-r)h_{\rm agg}(s)ds.           \tag{168bq}
\]

The Volterra formula gives, locally uniformly as `z` tends to zero,

\[
 A(r,z)=izB(r)+O(z^3).                               \tag{168br}
\]

At the seam,

\[
 a(z)=F(z)-F(-z)=\sqrt2A(0,z)
 =i\sqrt2zB(0)+O(z^3).                              \tag{168bs}
\]

Define the locally finite arithmetic step weight

\[
 W(r)=\sum_{\substack{p,\ k\ge1\\
 k\log p\le r<(k+1)\log p}}
 (\log p)p^{-k/2}.                                  \tag{168bt}
\]

Then the quadratic coefficient of `Lambda_def(z,w)` at `(0,0)` is

\[
 C_\theta=\int_0^\infty W(r)B(r)^2dr.               \tag{168bu}
\]

Consequently the proposed kernel domination (168bo) has the exact necessary
condition

\[
 \boxed{
 C_\theta\ge2B(0)^2.
 }                                                     \tag{168bv}
\]

In terms of the half-source first moment

\[
 m_1=\int_0^\infty s\phi(s)ds,
\]

and `h_agg=sqrt(2)phi`, this is equivalently

\[
 C_\theta\ge4m_1^2.                                 \tag{168bw}
\]

This is the smallest analytic falsifier for `Lambda_def`: it uses only one
spectral jet at the origin and no zero data.  If (168bv) fails, the
valuation-defect reservoir cannot dominate even the undifferentiated seam,
so it cannot be the complete Schur complement.

The inequality is not universal for positive sources.  Since `W(r)=0` on
`0<=r<log 2`, a forcing supported in that interval has `C_theta=0` but
`B(0)>0`.  Therefore any proof of (168bv) for theta must use its completed
tail beyond the first prime seam; positivity and decay alone are insufficient.

This also identifies the first genuinely arithmetic balance: can the
prime-power-weighted remote tail energy control the primitive first moment at
the modular seam?

## Pole-subtracted theta formula for the small-`z` tail moment

The raw modular profile

\[
 \mathcal A(r)=\frac12e^{r/2}\Theta(e^{2r})
\]

obeys `Phi=(partial_r^2-1/4)mathcal A`, but it grows like
`e^{r/2}/2`.  Therefore integrating it by parts on the half-line and dropping
the endpoint is invalid.  The faithful decaying precursor is

\[
 K(r)=\cosh(r/2)-\mathcal A(r),                      \tag{168bx}
\]

for which

\[
 \Phi(r)=\left(\frac14-\partial_r^2\right)K(r).     \tag{168by}
\]

Now the endpoint terms vanish honestly.  Since `h_agg=sqrt(2)Phi`, two
integrations by parts in (168bq) give

\[
 \boxed{
 B(r)=\sqrt2\left[
 \frac14\int_r^\infty(s-r)K(s)ds-K(r)
 \right].
 }                                                     \tag{168bz}
\]

The sign of the bracket is fixed by the original positive-source integral,
not inferred from the two displayed terms separately.

This correction is important for meaning: the local archimedean channel is
the pole-subtracted null-mode boundary carried by `K`, not the growing raw
theta precursor `mathcal A`.  The direct `Phi` estimates below do not use the
invalid raw integration by parts, so the analytic falsification of
`Lambda_def` remains unchanged.

## Archimedean completion has one explicit central negative coefficient

Let

\[
 \widehat K(z)=\int_{\mathbb R}K(u)e^{izu}du.
\]

The pole-subtracted source identity gives, in the Fourier spectral convention,

\[
 \boxed{
 X(z)=\left(z^2+\frac14\right)\widehat K(z).
 }                                                     \tag{168da}
\]

Therefore its vertical self-comparison factors as

\[
 X(x-it)X(x+it)=P_x(t^2)
 \widehat K(x-it)\widehat K(x+it),                  \tag{168db}
\]

where

\[
\begin{aligned}
 P_x(t^2)
 &=\left|\left(x+it\right)^2+\frac14\right|^2\\
 &=\boxed{
 \left(x^2+\frac14\right)^2
 +\left(2x^2-\frac12\right)t^2+t^4.
 }                                                     \tag{168dc}
\end{aligned}
\]

Thus the archimedean completion polynomial has exactly one potentially
negative vertical coefficient:

\[
 2x^2-\frac12<0
 \quad\Longleftrightarrow\quad |x|<\frac12.          \tag{168dd}
\]

It is not a uniformly positive local counterterm.  It creates a central
order-one defect and is automatically coefficientwise positive outside the
quarter-centered spectral interval.

If

\[
 \widehat K(x-it)\widehat K(x+it)
 =\sum_{n\ge0}\kappa_n(x)t^{2n},                    \tag{168de}
\]

then the completed Laguerre coefficients obey the exact three-term coupling

\[
 \boxed{
 \mathcal L_n[X](x)
 =\left(x^2+\frac14\right)^2\kappa_n(x)
 +\left(2x^2-\frac12\right)\kappa_{n-1}(x)
 +\kappa_{n-2}(x),
 }                                                     \tag{168df}
\]

with negative-index terms omitted.

This is a major simplification of the archimedean audit.  Completion couples
only three adjacent vertical orders; it does not introduce an uncontrolled
infinite defect tower.  The central negative coefficient must be repaired by
the pole-subtracted theta precursor coefficients `kappa_n`, with prime-power
defects supplying only the already-proved subleading remote correction.

The smallest archimedean gate is

\[
 \left(x^2+\frac14\right)^2\kappa_1(x)
 +\left(2x^2-\frac12\right)\kappa_0(x)\ge0.          \tag{168dg}
\]

At `x=0`, this requires

\[
 \boxed{
 \kappa_1(0)\ge8\kappa_0(0).
 }                                                     \tag{168dh}

This is the corrected primitive/archimedean scalar test.  Unlike the remote
prime-defect candidate, it retains the pole-cancellation data that generate
the quarter center.

## The null mode saturates the central gate exactly

Because `K` is even,

\[
 \kappa_0(0)=\widehat K(0)^2,
 \qquad
 \kappa_1(0)
 =\widehat K(0)\int_{\mathbb R}u^2K(u)du.           \tag{168di}
\]

Assuming the already-established positivity of the decaying precursor, the
gate (168dh) is equivalent to

\[
 \boxed{
 \int_{\mathbb R}(u^2-8)K(u)du\ge0.
 }                                                     \tag{168dj}
\]

On the positive half-line, modular expansion gives

\[
 K(u)=K_0(u)-R_\theta(u),
 \qquad
 K_0(u)=\frac12e^{-u/2},
 \qquad
 R_\theta(u)=e^{u/2}\sum_{n\ge1}e^{-\pi n^2e^{2u}}.
                                                               \tag{168dk}
\]

The null mode satisfies

\[
 \frac{\int_0^\infty u^2K_0(u)du}
 {\int_0^\infty K_0(u)du}=8,                        \tag{168dl}
\]

so

\[
 \int_0^\infty(u^2-8)K_0(u)du=0.                   \tag{168dm}
\]

The precursor is strictly positive.  Indeed,

\[
 \frac{R_\theta(u)}{K_0(u)}
 =2e^u\sum_{n\ge1}e^{-\pi n^2e^{2u}}               \tag{168dm1}
\]

is decreasing for `u>=0`, since every summand has logarithmic derivative
`1-2pi n^2e^{2u}<0`.  At the origin, using `pi>3`, `e^3>20`, and
`n^2>=1+3(n-1)`,

\[
 2\sum_{n\ge1}e^{-\pi n^2}
 <\frac{2/20}{1-e^{-3\pi}}<1.                       \tag{168dm2}
\]

Hence `0<R_theta(u)<K_0(u)` and `K(u)>0` on the positive half-line; evenness
gives positivity on all of `R`.

Therefore the central completed gate reduces exactly to

\[
 \boxed{
 \int_0^\infty(u^2-8)R_\theta(u)du\le0.
 }                                                     \tag{168dn}
\]

This is the first place where the architecture becomes genuinely critical:
the archimedean null mode supplies neither positive nor negative reserve.  It
saturates the required coefficient ratio exactly.  The nonzero theta labels
alone select the sign.

Since `R_theta` is positive and superexponentially concentrated near the
origin, the integrand in (168dn) is negative on `0<u<sqrt(8)` and positive
only in the extremely small far tail.  The next proof is a direct
negative-core versus positive-tail comparison.  Success certifies the first
central Laguerre coefficient from the theta source; failure would falsify the
archimedean repair already at `(x,n)=(0,1)`.

## First central archimedean gate is strictly proved

Split the theta correction into positive labels

\[
 R_\theta(u)=\sum_{n\ge1}R_n(u),
 \qquad
 R_n(u)=e^{u/2}e^{-\pi n^2e^{2u}}.                  \tag{168do}
\]

Put

\[
 \lambda_n=2\pi n^2-\frac12.
\]

Relative to the exponential density `e^{-lambda_n u}`, the likelihood ratio
is, up to a positive constant,

\[
 \frac{R_n(u)}{e^{-\lambda_nu}}
 =\exp\!\left[-\pi n^2
 \bigl(e^{2u}-1-2u\bigr)\right].                    \tag{168dp}
\]

Because `e^{2u}-1-2u` is increasing and nonnegative on `u>=0`, this ratio is
decreasing.  The normalized probability measure proportional to `R_n(u)du`
is therefore smaller than the exponential law of rate `lambda_n` in monotone
likelihood-ratio order, hence in stochastic order.

Applying this to the increasing function `u^2` gives

\[
 \frac{\int_0^\infty u^2R_n(u)du}
 {\int_0^\infty R_n(u)du}
 \le\frac2{\lambda_n^2}.                            \tag{168dq}
\]

Since `pi>3`,

\[
 \lambda_n\ge2\pi-\frac12>\frac{11}{2},
 \qquad
 \frac2{\lambda_n^2}<\frac8{121}<8.                \tag{168dr}
\]

Therefore every theta label satisfies

\[
 \int_0^\infty(u^2-8)R_n(u)du<0.                   \tag{168ds}
\]

Absolute convergence permits summation over `n`, yielding

\[
 \boxed{
 \int_0^\infty(u^2-8)R_\theta(u)du<0.
 }                                                     \tag{168dt}
\]

Combining with (168dn) proves

\[
 \boxed{
 \kappa_1(0)>8\kappa_0(0),
 \qquad
 \mathcal L_1[X](0)>0.
 }                                                     \tag{168du}

This is a genuine source theorem.  The archimedean null mode is exactly
critical, and every nonzero theta label shifts the completed first vertical
coefficient in the positive direction.  Prime-power repair is not needed at
the central origin; its role begins away from this maximally symmetric point.

The proof uses only modular source decomposition and stochastic domination,
not zero locations or numerical evaluation.

## Analytic falsification of the bare valuation-defect candidate

The small-`z` gate (168bv) can be decided by elementary bounds.

### Lower bound at the primitive seam

For the first theta label,

\[
 \phi_1(u)=
 \left(4\pi^2e^{9u/2}-6\pi e^{5u/2}\right)
 e^{-\pi e^{2u}}.                                   \tag{168ca}
\]

On `0<=u<=1/10`, the elementary estimates

\[
 \pi>3.14,\quad \pi<22/7,
 \quad e^{1/4}<4/3,
 \quad \pi e^{1/5}<4,
 \quad e^4<55
\]

give

\[
 \phi_1(u)>\frac{14}{55}.                           \tag{168cb}
\]

Since `h_agg=sqrt(2)Phi>phi_1`,

\[
 \boxed{
 B(0)=\int_0^\infty u h_{\rm agg}(u)du
 >\int_0^{1/10}u\frac{14}{55}du
 =\frac7{5500}.
 }                                                     \tag{168cc}
\]

Therefore

\[
 2B(0)^2>\frac{98}{30\,250\,000}.                   \tag{168cd}
\]

### Upper bound on the remote repair reservoir

For `r>=log 2`, discard the negative term in each theta summand and use
`pi>3`, `pi^2<10`.  The elementary Gaussian tail bound

\[
 \sum_{n\ge1}n^4e^{-3n^2e^{2r}}
 \le2e^{-3e^{2r}}                                   \tag{168ce}
\]

then yields

\[
 h_{\rm agg}(r)
 \le120e^{9r/2}e^{-3e^{2r}}.                        \tag{168cf}
\]

For `s=r+t`, use `e^{2t}>=1+2t` and `e^{2r}>=4`.  Integrating the resulting
exponential majorant gives

\[
 \boxed{
 B(r)\le\frac13e^{9r/2}e^{-3e^{2r}}
 \qquad(r\ge\log2).
 }                                                     \tag{168cg}
\]

At any fixed `r`, at most one valuation depth contributes for each prime in
`W(r)`, and every contributing prime satisfies `p<=e^r`.  Hence the crude
counting bound

\[
 W(r)\le re^r                                      \tag{168ch}
\]

is sufficient.  Consequently

\[
\begin{aligned}
 C_\theta
 &\le\frac19\int_{\log2}^\infty
 r e^{10r}e^{-6e^{2r}}dr\\
 &=\frac1{36}\int_4^\infty
 (\log x)x^4e^{-6x}dx\\
 &<\frac1{36}\int_4^\infty x^5e^{-6x}dx
 <\frac6{2^{24}}.                                   \tag{168ci}
\end{aligned}
\]

The last bound follows from the exact repeated-integration formula for the
degree-five exponential tail, whose bracket is below `216`, together with
`e^{24}>2^{24}`.

Finally,

\[
 \frac6{2^{24}}
 <\frac{98}{30\,250\,000}
 <2B(0)^2.                                          \tag{168cj}
\]

Thus

\[
 \boxed{C_\theta<2B(0)^2.}                          \tag{168ck}
\]

The necessary condition (168bv) fails.  Therefore `Lambda_def` is
analytically falsified as the complete Schur-complement repair operator,
already in the first spectral jet at the origin.

This does not falsify the differentiated modular Green program.  It proves
that the positive valuation defect reservoir supplies only a subleading
remote-tail contribution.  The missing dominant term must come from the
primitive interval `0<=q<log2`, the archimedean completion, or their mixed
cross term with the prime-power reservoir.  Any theorem that retains only
the positive shift defects necessarily loses the main seam energy.

## Finite spectral packets reduce to one secular inequality

Choose spectral points `z_1,...,z_r` and coefficients `c_1,...,c_r`.  The
primitive antisymmetric seam feature on this packet is

\[
 a_i=F(z_i)-F(-z_i).                                 \tag{168}
\]

Because the seam evaluation has one complex output channel, its packet Gram
matrix is

\[
 \boxed{Q_r=aa^*.}                                  \tag{169}
\]

It has rank at most one, independently of packet size.  Let `Lambda_r` be the
pullback of the aggregate--primitive relative boundary operator to the same
packet.  The repair condition is exactly

\[
 \boxed{\Lambda_r-aa^*\ge0.}                        \tag{170}
\]

This separates into three typed requirements:

1. `Lambda_r>=0`;
2. `a in ran(Lambda_r^{1/2})`;
3. the rank-one secular bound

\[
 \boxed{
 a^*\Lambda_r^\dagger a\le1,
 }                                                     \tag{171}
\]

where `dagger` denotes the Moore--Penrose inverse on the support.  If
`Lambda_r` is strictly positive, this is simply

\[
 a^*\Lambda_r^{-1}a\le1.                             \tag{172}
\]

Therefore the base theta repair has the exact same abstract shape as the
level-44 proof:

\[
 \boxed{
 \text{positive comparison operator}
 -\text{one source-fixed seam line}
 \ge0
 \quad\Longleftrightarrow\quad
 \text{one secular inequality}.
 }                                                     \tag{173}
\]

The analogy concerns rank-one operator structure only.  It supplies no
numerical evidence for RH.

This also sharpens the falsifier.  On the smallest packet where either
`Lambda_r` has a negative direction, `a` misses its support, or the scalar in
(171) exceeds one, the functorial boundary-repair mechanism fails.  If every
finite packet passes, the remaining work is the infinite-kernel closure and
nonuniform-coercivity limit—not higher symmetric-power algebra.

## Sine addition exposes the spectral seam as an undamped boundary wave

The typing correction after (168xc) can be made exact.  Write

\[
 G_z(t)=\frac{\sin(\sqrt z\,t)}{\sqrt z},
 \qquad
 C(z)=\int_0^\infty\Phi(u)G_z(u)du,
 \qquad
 B(z)=\int_0^\infty\Phi(u)\cos(\sqrt z\,u)du.
                                                               \tag{174}
\]

If one formally inserts the bare spectral wave into the seam transform,
sine addition gives

\[
\begin{aligned}
 \widetilde s_z(t)
 &=\int_0^\infty\Phi(u)G_z(u+t)du\\
 &=C(z)\cos(\sqrt z\,t)+B(z)G_z(t).
                                                               \tag{175}
\end{aligned}
\]

Thus the seam is controlled by the two boundary coordinates `(C,B)`, but it
is not an `L^2(R_+)` vector.  For positive real `z` it is an undamped
oscillation; at `z=0` it is the affine wave

\[
 \widetilde s_0(t)=C(0)+B(0)t;                    \tag{176}
\]

and off the real axis one of the exponential modes generally grows.  Except
at exceptional simultaneous boundary zeros, its ordinary seam norm diverges.

This distinguishes three statements that had been conflated:

1. the spatial seam kernel `S(p,r)` is a genuine positive, infinite-rank
   Gram kernel on compact translation packets;
2. its spectral image has **boundary channel width two**, by (175);
3. that image is not a Hilbert-space Gram vector without a cutoff or a
   boundary renormalization.

Finite channel width therefore does not imply finite operator rank, and it
does not justify replacing the seam by the rank-one carrier term.  Likewise,
the later rank-one packet `aa^*` records a particular primitive boundary
evaluation; it is not the full spatial seam Gram.

The correct next object is a renormalized Green boundary form.  With a cutoff
`T`, define

\[
 \mathcal S_T(z,w)
 =\int_0^T\widetilde s_z(t)
       \overline{\widetilde s_w(t)}dt.             \tag{177}
\]

Equation (175) makes every divergent term an explicit quadratic expression
in `(C(z),B(z))`.  The theorem-shaped target is now:

\[
 \boxed{
 \text{the bilateral modular boundary current cancels the universal
 cutoff divergence of }\mathcal S_T,
 \text{ leaving a positive finite part.}
 }                                                   \tag{178}
\]

This is sharper than seeking an unspecified contraction `Gamma`.  The
candidate repair is forced to be a two-port boundary counterform, and its
coefficients are determined by the sine propagator rather than fitted.  A
decisive falsifier is equally sharp: after subtracting the unique Green
boundary divergence, the finite part has a negative finite spectral packet.

## The seam is the free propagation of the physical boundary pair

Equation (175) has a stronger interpretation.  The formal seam wave is the
unique solution of

\[
 \widetilde s_z''+z\widetilde s_z=0,
 \qquad
 \widetilde s_z(0)=C(z),
 \qquad
 \widetilde s_z'(0)=B(z).                          \tag{179}
\]

Thus the source dependence of the entire seam is concentrated in the
physical boundary pair `(C,B)`; propagation away from the seam is universal.
This is channel width two in the precise state-space sense.

For two spectral parameters define the remote Wronskian

\[
 W_{z,w}(t)
 =\widetilde s_z'(t)\overline{\widetilde s_w(t)}
  -\widetilde s_z(t)\overline{\widetilde s_w'(t)}.
                                                               \tag{180}
\]

The free equations give the exact Lagrange identity

\[
 W_{z,w}'(t)
 =(\bar w-z)\widetilde s_z(t)
             \overline{\widetilde s_w(t)},          \tag{181}
\]

and hence

\[
 (\bar w-z)\mathcal S_T(z,w)
 =W_{z,w}(T)
  -\bigl(B(z)\overline{C(w)}
         -C(z)\overline{B(w)}\bigr).               \tag{182}
\]

The scalar boundary Wronskian and the seam Gram are therefore not unrelated
terms awaiting a guessed coupling.  They are the two endpoints of one free
Green current.  The sole missing datum is the disposition of `W_{z,w}(T)` as
`T` tends to infinity.

For real positive spectral parameters the seam is a standing wave, so the
remote current does not vanish pointwise.  An outgoing prescription, Abel
limit, or bilateral modular pairing is indispensable.  Consequently the
next RH-relevant theorem is no longer “find a positive seam contraction.” It
is

\[
 \boxed{
 \text{derive from completed modular sewing the canonical remote boundary
 condition for the free seam wave, and prove that its induced boundary
 form has the de Branges orientation.}
 }                                                    \tag{183}
\]

This also supplies the immediate hostile test.  Any proposed sewing rule
must be applied to the elementary two-mode solution (175).  If it does not
dispose of `W(T)` covariantly for every finite spectral packet, it cannot
orient the completed theta Bezoutian, regardless of how positive the spatial
translation Gram was before spectral projection.

## Reflection or free outgoingness cannot select the theta Weyl ratio

The hostile test closes the simplest remote-boundary proposals immediately.
Put `z=k^2`.  In the half-plane `Im k>0`, the unique decaying solution of the
free equation in (179) is proportional to `e^{ikt}`.  Its Cauchy data obey

\[
 \boxed{B(z)=ik\,C(z).}                             \tag{184}
\]

Thus a free outgoing condition selects the universal Weyl function

\[
 m_0(z)=\frac{B(z)}{C(z)}=i\sqrt z,                 \tag{185}
\]

not the source-dependent theta ratio `m_theta=B/C`.

Bare bilateral reflection is no better.  Under `t\mapsto -t`, the Cauchy
state transforms as

\[
 (C,B)\longmapsto(C,-B).                            \tag{186}
\]

Its fixed and anti-fixed sectors impose respectively

\[
 B=0
 \qquad\hbox{or}\qquad
 C=0.                                               \tag{187}
\]

Neither is the physical theta boundary state.  Already at `z=0`, positivity
of the source gives

\[
 B(0)=\int_0^\infty\Phi(u)du>0,
 \qquad
 C(0)=\int_0^\infty u\Phi(u)du>0.                  \tag{188}
\]

So reflection parity and free outgoingness are analytically falsified as
the missing sewing law.  Reciprocal modular symmetry can identify the two
charts, but it cannot by itself manufacture the nontrivial theta Weyl ratio.

The consequence is structural:

\[
 \boxed{
 \text{the missing positive object cannot be the free seam with a boundary
 condition; it must be a source-loaded canonical system whose Weyl function
 is }m_\theta(z)=B(z)/C(z).
 }                                                    \tag{189}
\]

Equivalently, the theta source must enter the *propagator*, not merely its
initial boundary vector.  The next construction problem is to recover a
Hamiltonian `H(t)>=0` (or to find the first obstruction to one) for which the
canonical-system transfer has Weyl function `B/C`.  If such a source-derived
Hamiltonian exists with the required endpoint typing, its standard Green
identity supplies the desired positive bulk and kills the remote current by
limit-point theory.  If it does not, the seam/Green route cannot prove the
de Branges orientation.

## Autocorrelation is positive but phase-blind

The positive reflected kernel from (168xe) is the obvious candidate
accelerant, but its information content can be audited exactly.  Let `f` be
the zero extension of `Phi` to the line and choose

\[
 \widehat f(k)=\int_0^\infty\Phi(u)e^{iku}du
 =B(k^2)+ikC(k^2).                                  \tag{190}
\]

Wiener--Khinchin gives

\[
 \widehat{A} (k)=|\widehat f(k)|^2.                \tag{191}
\]

Consequently the odd-reflection Gram has the sine representation

\[
 A(|p-r|)-A(p+r)
 =\frac2\pi\int_0^\infty
 |\widehat f(k)|^2\sin(kp)\sin(kr)dk.              \tag{192}
\]

This proves its positivity again, but also reveals what it forgets.  It
retains only

\[
 |B(k^2)+ikC(k^2)|^2,                               \tag{193}
\]

whereas the physical Weyl coordinate requires the relative phase, or
equivalently the ratio `B/C`.

Multiplication of `widehat f` by any admissible inner factor leaves (191)
and every autocorrelation Gram unchanged while changing its zeros and phase.
Therefore no construction functorial only in `A` can distinguish those
phase alternatives.  In particular, positivity of the odd autocorrelation
kernel cannot by itself prove the zero-location statement.

For a one-sided Hardy transform, modulus determines phase only after an
outer-factor assertion.  But excluding a nontrivial inner factor is already
a zero-free theorem in the relevant half-plane.  Invoking outer
factorization here would therefore import the missing conclusion rather than
explain it.

We obtain a second structural no-go:

\[
 \boxed{
 \text{the canonical system cannot be reconstructed from the symmetric
 autocorrelation alone; it must retain an oriented triangular factor of the
 original theta source.}
 }                                                    \tag{194}
\]

The distinction matches the Carrier rule developed elsewhere.  The Gram
kernel is the positive scalar readout; the causal half-line factor `Phi` is
the faithful source coordinate.  Squaring to the autocorrelation before
constructing transport destroys precisely the phase that controls the
critical-line question.

The next viable attack is consequently a triangular factorization theorem,
not another positivity estimate for `A`: construct the finite-cut operators

\[
 (\mathsf T_T c)(t)
 =\int_t^T\Phi(p-t)c(p)dp,                          \tag{195}
\]

retain their orientation as `T` varies, and derive the two-dimensional
boundary evolution of their source-fixed factors.  A successful evolution
must produce `B/C` before taking the modulus-square Gram.  Failure of nested
factor covariance at the first pair `T_1<T_2` would finitely falsify this
specific canonical-system route.

## The missing orientation is the source scattering ratio

The phase discarded in (191) has a canonical expression.  In the square-root
spectral coordinate define

\[
 E(k)=\widehat f(k)=B(k^2)+ikC(k^2),
 \qquad
 E^\#(k)=\overline{E(\bar k)}=B(k^2)-ikC(k^2).      \tag{196}
\]

Their quotient

\[
 \boxed{
 \Theta(k)=\frac{E^\#(k)}{E(k)}
 =\frac{B(k^2)-ikC(k^2)}{B(k^2)+ikC(k^2)}
 }                                                    \tag{197}
\]

is unimodular on the real `k` axis wherever defined.  It retains exactly the
oriented phase absent from `|E|^2`.  Moreover the theta Weyl ratio is its
Cayley coordinate:

\[
 \boxed{
 \frac{B(k^2)}{C(k^2)}
 =ik\frac{1+\Theta(k)}{1-\Theta(k)}.
 }                                                    \tag{198}
\]

Thus the canonical-system existence question has an exact analytic gate:
`Theta` must be a Schur/inner function in the chosen half-plane, with poles,
boundary points, and the square-root sheet typed correctly.  Equivalently,
`E` must have the corresponding Hermite--Biehler orientation

\[
 |E^\#(k)|<|E(k)|.                                  \tag{199}
\]

This is not yet a proof: establishing (199) is another form of the missing
zero-location theorem.  Its value is explanatory compression.  The objects
now line up as

\[
 \boxed{
 \begin{array}{c}
 \text{causal theta factor }E
 \longrightarrow \text{reflection quotient }\Theta=E^\#/E\\
 \longrightarrow \text{Weyl coordinate }B/C
 \longrightarrow \text{canonical-system Green positivity},
 \end{array}
 }                                                    \tag{200}
\]

whereas autocorrelation stops at `|E|^2` before the first arrow.

This also gives the correct finite falsifier for any proposed triangular
transport law.  It must imply the Pick-kernel inequality

\[
 \frac{1-\Theta(k)\overline{\Theta(\ell)}}
      {-i(k-\bar\ell)}\succeq0                     \tag{201}
\]

on every finite packet in its asserted half-plane.  A negative two-point
minor disproves that transport law.  Passing all sampled packets would still
be discovery evidence only; the desired theorem must derive (201) from the
source-fixed nested Volterra factors, without assuming outerness or zero
locations.

## Scope correction: the upper-half-plane scattering orientation is inverse

The first hostile point `k=iy`, `y>0`, falsifies (199)--(201) with the stated
upper-half-plane convention.  Directly from (196),

\[
 E(iy)=\int_0^\infty\Phi(u)e^{-yu}du,
 \qquad
 E^\#(iy)=\int_0^\infty\Phi(u)e^{yu}du.             \tag{202}
\]

Since `Phi>0`,

\[
 |E^\#(iy)|>|E(iy)|,
 \qquad
 |\Theta(iy)|>1.                                   \tag{203}
\]

Thus `Theta=E^#/E` is not Schur in the upper half-plane.  The formal Pick
target (201) has the wrong orientation there.  One may instead consider

\[
 S(k)=\Theta(k)^{-1}=\frac{E(k)}{E^\#(k)},          \tag{204}
\]

or retain `Theta` and work in the opposite half-plane, but analyticity of
the denominator must be proved before either reformulation is meaningful.
Changing the quotient alone does not solve the zero problem.

The attack nevertheless yields a genuine source theorem.  Earlier strict
log-concavity and modular evenness gave

\[
 \Phi'(0)=0,
 \qquad
 (\log\Phi)''<0,
\]

so `Phi'(u)<0` for every `u>0`.  Define the positive finite measure

\[
 d\mu(t)=-\Phi'(t)dt,
 \qquad
 \mu(\mathbb R_+)=\Phi(0).                          \tag{205}
\]

Because

\[
 \Phi(u)=\int_u^\infty d\mu(t),
\]

Fubini gives the exact Levy--Khintchine-type factorization

\[
 \boxed{
 ikE(k)=\int_0^\infty\bigl(e^{ikt}-1\bigr)d\mu(t).
 }                                                    \tag{206}
\]

If `Im k>0`, then

\[
 \left|\int_0^\infty e^{ikt}d\mu(t)\right|
 \le\int_0^\infty e^{-t\,\operatorname{Im}k}d\mu(t)
 <\mu(\mathbb R_+),                                 \tag{207}
\]

where strictness uses that `\mu` has positive mass away from zero.  Therefore
the right side of (206) cannot vanish.  Since `E(0)>0`, we obtain

\[
 \boxed{
 E(k)\ne0\qquad(\operatorname{Im}k>0).
 }                                                    \tag{208}
\]

This zero-free half-plane is not RH.  `E=B+ikC` is the causal source factor,
whereas the physical zeros of `C` are sheet-coincidence points

\[
 C(k^2)=0
 \quad\Longleftrightarrow\quad
 E(k)=E^\#(k).                                      \tag{209}
\]

The result precisely relocates the difficulty.  The causal sheet is already
minimum-phase by monotone source transport; what remains is to control its
comparison with the reflected, anti-causal sheet.  In upper-half-plane
language the corrected conjectural gate is

\[
 \boxed{
 S(k)=E(k)/E^\#(k)\text{ extends analytically and contractively,}
 }                                                    \tag{210}
\]

with the explicit warning that analyticity of `S` requires zero-freeness of
`E^#` in that half-plane.  That denominator condition is not supplied by
(208) and may carry the full hard content.

Deutsch's question is consequently sharper than before: what modular
operation transfers the elementary causal zero-free theorem (208) across
the fold without losing its orientation?  The sought explanation must act
between the two sheets; no further one-sided positivity estimate can do it.

## The reflected-sheet gap is exactly the original two-copy transport

The contractivity condition in (210) is

\[
 \Delta(k):=|E^\#(k)|^2-|E(k)|^2\ge0,
 \qquad \operatorname{Im}k>0.                       \tag{211}
\]

Writing `k=x+iy` and expanding the two source integrals gives

\[
 \boxed{
 \Delta(x+iy)
 =2\iint_{\mathbb R_+^2}
 \Phi(u)\Phi(v)
 \sinh\bigl(y(u+v)\bigr)
 \cos\bigl(x(u-v)\bigr)dudv.
 }                                                    \tag{212}
\]

Thus reflected-sheet contractivity is precisely a sum/difference transport:
the positive radial weight depends on `U=u+v`, while the oscillatory sign
depends on `D=u-v`.  This is the same invariant previously encountered in
the theta quadrant inequality, Clark transport, and the vertical-modulus
derivative.  The scattering formulation compresses those routes but does
not supply independent evidence for them.

The monotonicity theorem (206) nevertheless changes the explanatory burden.
Put

\[
 \psi(k)=ikE(k)
 =\int_0^\infty(e^{ikt}-1)d\mu(t).                 \tag{213}
\]

Then the forward exponent `psi` is automatically nonzero in the upper
half-plane, and the entire missing theorem becomes

\[
 \boxed{
 |\psi(k)|\le|\psi(-k)|
 \qquad(\operatorname{Im}k>0).
 }                                                    \tag{214}
\]

This suggests the strongest current Deutsch--Popper conjecture:

\[
 \boxed{
 \begin{minipage}{0.84\linewidth}
 The Levy measure `dmu=-Phi'(t)dt` generated by the completed theta source
 belongs to a modularly oriented subclass of positive half-line measures
 whose compound-Poisson exponent satisfies the reflection dominance
 (214).  Modular prime-scale sewing, not positivity alone, characterizes
 that subclass.
 \end{minipage}
 }                                                    \tag{215}
\]

It is hard to vary in the required sense.  Removing modular sewing leaves
an arbitrary positive decreasing source; such sources still satisfy the
causal zero-free theorem (208) but need not satisfy reflection dominance.
The smallest valid falsifier is therefore a positive decreasing source—or a
single canonical modular truncation—for which (214) reverses at one point.
The constructive proof target is an exact prime-scale decomposition of

\[
 |\psi(-k)|^2-|\psi(k)|^2                           \tag{216}
\]

into a positive primitive term, transported valuation terms, and the finite
modular seam current.  Unlike an autocorrelation proof, this expansion must
retain the orientation of each factor before taking its modulus square.

## Prime transport places the half-offset in the multiplier norm

The exact prime recursion can be differentiated without losing positivity.
For a prime `p`, put `L=log p` and split

\[
 \Phi(u)=\Phi_{p\nmid}(u)+p^{-1/2}\Phi(u+L).        \tag{217}
\]

Every label is decreasing on the positive chamber, so

\[
 d\mu=-\Phi'(u)du,
 \qquad
 d\mu_{p\nmid}=-\Phi_{p\nmid}'(u)du               \tag{218}
\]

are positive measures.  Define their Levy exponents and the finite seam
current

\[
\begin{aligned}
 \psi(k)&=\int_0^\infty(e^{iku}-1)d\mu(u),\\
 \psi_{p\nmid}(k)&=\int_0^\infty(e^{iku}-1)d\mu_{p\nmid}(u),\\
 \eta_{p}(k)&=\int_0^L(e^{iku}-1)d\mu(u).
                                                               \tag{219}
\end{aligned}
\]

Changing variables in the shifted tail gives

\[
\begin{aligned}
 &\int_0^\infty(e^{iku}-1)d\mu(u+L)\\
 &\qquad=e^{-ikL}\bigl(\psi(k)-\eta_p(k)\bigr)
 +(e^{-ikL}-1)\Phi(L).                              \tag{220}
\end{aligned}
\]

Therefore

\[
 \boxed{
 \bigl(1-p^{-1/2-ik}\bigr)\psi(k)
 =\psi_{p\nmid}(k)
 -p^{-1/2-ik}\eta_p(k)
 +p^{-1/2}(e^{-ikL}-1)\Phi(L).
 }                                                    \tag{221}
\]

This is the oriented Levy version of the earlier transform sewing identity.
The final two terms are forced by the finite interval `0<=u<L`; deleting
them creates false arithmetic singularities.

Now write `k=x+iy`.  The transport multiplier has modulus

\[
 \left|p^{-1/2-ik}\right|=p^{y-1/2}.               \tag{222}
\]

Hence its neutral locus is exactly

\[
 \boxed{y=\frac12.}                                \tag{223}
\]

Below that line the prime shift is contractive; above it the same shift is
expansive.  On the line, the multiplier `1-p^{-1/2-ik}` vanishes at

\[
 k=\frac{2\pi m}{\log p}+\frac i2,
 \qquad m\in\mathbb Z,                              \tag{224}
\]

and the right side of (221) must cancel there exactly because `psi` is
entire.

This gives a source-derived explanation of the otherwise mysterious
half-offset: it is the unique balance point between the coefficient weight
`p^{-1/2}` and the Laplace gain `p^y` generated by translation through one
prime scale.  It is not yet RH—the cancellation lattice (224) consists of
false multiplier singularities, not zeta zeros—but it explains why every
prime transport changes orientation at the same displaced line.

The reflected-sheet problem has therefore acquired a canonical local form.
For each prime, one must prove that the numerator in (221), including its
finite seam current, transports the contractive side through the neutral
line without generating a negative Pick direction.  The smallest falsifier
is one prime, two spectral points, and its exact seam term.  Any argument
that omits `eta_p` or the endpoint mass `Phi(L)` is structurally incapable of
crossing (223).

## All prime seams meet at one universal neutral point

Although the nonzero points of the cancellation lattice (224) depend on
`p`, its central point does not:

\[
 \boxed{k_*=\frac i2.}                              \tag{225}
\]

At `k_*`, one has

\[
 p^{-1/2-ik_*}=1,
 \qquad
 e^{-ik_*L}=p^{1/2}.                                \tag{226}
\]

Substitution into (221) gives, for every prime separately, the exact seam
sum rule

\[
 \boxed{
 \psi_{p\nmid}(k_*)-\eta_p(k_*)
 +(1-p^{-1/2})\Phi(\log p)=0.
 }                                                    \tag{227}
\]

This is not a consequence of numerical coincidence.  It is forced by
entirety together with the normalized prime translation weight.  Primitive
transport, the finite seam current, and the endpoint mass meet in exactly
the combination needed to remove the false pole at the common neutral
point.

The first derivative contains the surviving finite value.  If `N_p(k)`
denotes the right side of (221), then

\[
 1-p^{-1/2-ik}=iL(k-k_*)+O((k-k_*)^2),              \tag{228}
\]

and hence

\[
 \boxed{N_p'(k_*)=i(\log p)\psi(k_*).}             \tag{229}
\]

Expanding the derivative gives the explicit Ward-type identity

\[
\boxed{
 \psi_{p\nmid}'(k_*)
 +iL\eta_p(k_*)-\eta_p'(k_*)-iL\Phi(L)
 =iL\psi(k_*).
}                                                     \tag{230}
\]

The right side is independent of `p`.  Thus every prime chart reconstructs
the same global source value from a different primitive/seam decomposition.
This is the first exact all-prime compatibility law in the reflected-sheet
attack.

Its explanatory meaning is precise: the half-offset is the common fixed
balance of all prime dilation charts, while arithmetic enters through the
different ways those charts resolve the same germ.  The remaining problem
is whether the compatibility extends from the common germ to a positive
kernel along the whole neutral line.  A mismatch between the second divided
differences derived from two primes would falsify that extension before any
global RH claim is made.

## Centering turns every prime chart into an inner-exponential cocycle

Introduce the neutral coordinate

\[
 q=k-\frac i2
 \qquad\text{and}\qquad
 b_p(q)=e^{iq\log p}=p^{iq}.                        \tag{231}
\]

For `Im q>0`,

\[
 |b_p(q)|=e^{-(\log p)\operatorname{Im}q}<1,        \tag{232}
\]

and `b_p` is inner on the real boundary.  Rewriting (221) at
`k=q+i/2` and multiplying by `b_p(q)` gives

\[
 \boxed{
 (1-b_p(q))\widetilde\psi(q)=J_p(q),
 }                                                    \tag{233}
\]

where

\[
\begin{aligned}
 \widetilde\psi(q)&=\psi(q+i/2),\\
 J_p(q)&=\widetilde\eta_p(q)
 -b_p(q)\widetilde\psi_{p\nmid}(q)
 -\bigl(1-p^{-1/2}b_p(q)\bigr)\Phi(\log p).        \tag{234}
\end{aligned}
\]

Thus the primitive transform, finite seam, and endpoint mass form an exact
Hardy cocycle divisible by the canonical inner defect `1-b_p`.  The common
neutral point is simply `q=0`, where every `b_p` equals one.

Different prime charts satisfy the exact overlap relation

\[
 \boxed{
 J_p(q)\bigl(1-b_r(q)\bigr)
 =J_r(q)\bigl(1-b_p(q)\bigr)
 \qquad(p,r\text{ prime}).
 }                                                    \tag{235}
\]

This is the sought all-prime compatibility, now valid as an entire identity
rather than only at the common germ.  The quotients

\[
 \frac{J_p}{1-b_p}=\widetilde\psi                 \tag{236}
\]

are the same global section in every prime chart.

Each chart also carries the canonical positive Pick kernel

\[
\begin{aligned}
 K_p(q,r)
 &=\frac{1-b_p(q)\overline{b_p(r)}}{-i(q-\bar r)}\\
 &=\int_0^{\log p}e^{iqt}\overline{e^{irt}}dt
 \succeq0.                                          \tag{237}
\end{aligned}
\]

This identifies the finite modular seam geometrically: it is precisely the
model space of the inner translation `b_p`, with interval length `log p`.
The seam current in (234) is therefore typed in the correct positive carrier
space rather than added as an ad hoc correction.

There is, however, a crucial scope boundary.  Positivity of `K_p` is
universal for every translation length and says nothing about the sign of
the source section `widetilde psi`.  Indeed

\[
 \widetilde\psi(q)\overline{\widetilde\psi(r)}K_p(q,r)
 \succeq0                                            \tag{238}
\]

for any scalar function on a finite packet.  Therefore (237) supplies the
positive carrier geometry but not reflected-sheet dominance.  Treating it
as the missing RH positivity would repeat the error “positive source Gram
implies oriented scalar readout.”

The remaining theorem must involve how the cocycles `J_p` act on these model
spaces.  A noncircular target is: prove that the source-derived multiplier or
compression induced by `J_p` is contractive, and that the contractions agree
under the overlap law (235).  The smallest falsifier is a two-prime overlap
and a two-point packet on which one compressed cocycle has norm greater than
one.

## Compatibility alone is a tautological carrier law

The overlap identity (235) is exact, but by itself it has no selective power.
For an arbitrary entire function `h(q)`, setting

\[
 J_p^{(h)}(q)=(1-b_p(q))h(q)                      \tag{239}
\]

produces the same vanishing lattices and satisfies every two-prime overlap
identity automatically.  Consequently

\[
 \boxed{
 \text{prime-chart divisibility and Cech compatibility do not constrain the
 global section.}
 }                                                    \tag{240}
\]

This is another instance of the distinction between a Carrier law and a
physical selector.  The inner exponentials `b_p`, their model-space kernels,
and their overlap maps describe the universal geometry of prime translations.
They do not select the theta section among all compatible sections.

The arithmetic content of (233) lies only in the *typed decomposition*

\[
 J_p
 =\underbrace{\widetilde\eta_p}_{\text{finite seam}}
 -\underbrace{b_p\widetilde\psi_{p\nmid}}_{\text{primitive transport}}
 -\underbrace{(1-p^{-1/2}b_p)\Phi(\log p)}_{
                 \text{endpoint current}}.         \tag{241}
\]

Any positivity theorem must use relations among these three summands before
they are collapsed to `J_p`.  After collapse, the compatibility data cannot
distinguish theta from a hostile section.

This gives a sharper attack direction.  On the model space

\[
 \mathcal K_p=H^2\ominus b_pH^2
 \cong L^2(0,\log p),                               \tag{242}
\]

the finite seam is native, while primitive transport enters through the
boundary value at the far endpoint.  The theorem to seek is a Green or
Schur-complement identity on `K_p` in which the endpoint current in (241)
is exactly the boundary repair for the primitive term.  It must be derived
before forming the scalar quotient (236).

This formulation supplies a stronger falsifier than an arbitrary Pick
minor: compute the exact two-channel boundary form of (241).  If its negative
index exceeds the number of source-fixed endpoint channels, no compatible
rank-finite repair can make the prime chart contractive.  If the index is
one and the endpoint current repairs precisely that direction, the
level-44 mechanism has reappeared at each prime scale for structural rather
than numerical reasons.

## Integration by parts reveals an orthogonal two-chamber identity

The three-term presentation (241) is useful for tracking Levy boundary
mass, but the endpoint current is not an independent channel.  For
`k=q+i/2`, integration by parts gives

\[
\begin{aligned}
 \widetilde\eta_p(q)
 &=\int_0^L(e^{iku}-1)(-\Phi'(u))du\\
 &=\bigl(1-p^{-1/2}b_p(q)\bigr)\Phi(L)
   +ik\int_0^L\Phi(u)e^{iku}du.                    \tag{243}
\end{aligned}
\]

The first term cancels the endpoint current in (234) exactly.  Since
`psi=ikE`, the cocycle becomes

\[
 \boxed{
 (1-b_p(q))\widetilde E(q)
 =F_{p}(q)-b_p(q)\widetilde E_{p\nmid}(q),
 }                                                    \tag{244}
\]

where

\[
\begin{aligned}
 \widetilde E(q)
 &=E(q+i/2)
 =\int_0^\infty e^{-u/2}\Phi(u)e^{iqu}du,\\
 F_p(q)
 &=\int_0^{\log p}e^{-u/2}\Phi(u)e^{iqu}du,\\
 \widetilde E_{p\nmid}(q)
 &=\int_0^\infty e^{-u/2}\Phi_{p\nmid}(u)e^{iqu}du.
                                                               \tag{245}
\end{aligned}
\]

Now the model-space typing becomes exact.  Under the Paley--Wiener
identification of upper-half-plane `H^2` with `L^2(R_+)`,

\[
 F_p\in L^2(0,L),
 \qquad
 b_p\widetilde E_{p\nmid}\in L^2(L,\infty).        \tag{246}
\]

These two terms are orthogonal.  Therefore (244) yields the source-derived
positive-energy identity

\[
 \boxed{
 \|(1-b_p)\widetilde E\|_{H^2}^2
 =\|F_p\|_{H^2}^2
  +\|\widetilde E_{p\nmid}\|_{H^2}^2.
 }                                                    \tag{247}
\]

This is the first non-tautological payoff of the prime cocycle.  The finite
seam and translated primitive chamber do not require a fitted repair: after
the critical half-shift they are literally disjoint pieces of the causal
source on the scale line.

It also corrects the speculative negative-index formulation following
(242).  At the causal `H^2` level there is no negative direction to repair;
the apparent endpoint defect was an integration-by-parts artifact.  The
indefiniteness enters only when this orthogonal causal decomposition is
compared with its reflected anti-causal copy.

The remaining gap is consequently very precise:

\[
 \boxed{
 \text{upgrade the global orthogonal energy identity (247) to a coherent
 reflected-sheet Pick inequality.}
 }                                                    \tag{248}
\]

Norm equality alone cannot perform that upgrade.  Evaluation at a spectral
point is not an orthogonal projection onto the two time chambers, and cross
terms reappear after reflection.  The required modular theorem must show
that the nested decompositions (244), simultaneously over all primes,
orient those reflected cross terms.

## The arithmetic selector is mixed-prime complete monotonicity

There is one further scope correction to (247).  Orthogonality of an initial
interval and its shifted tail is universal one-prime Carrier geometry.  By
itself it does not distinguish theta from an arbitrary half-line source.
The selective arithmetic content first appears when several prime cuts are
required to coexist.

Define the critically weighted source and primitive seed

\[
 f(u)=e^{-u/2}\Phi(u),
 \qquad
 f_1(u)=e^{-u/2}\phi_1(u).                          \tag{249}
\]

The exact label translation

\[
 \phi_n(u)=n^{-1/2}\phi_1(u+\log n)
\]

becomes, after multiplication by `e^{-u/2}`,

\[
 \boxed{
 e^{-u/2}\phi_n(u)=f_1(u+\log n).
 }                                                    \tag{250}
\]

Thus the half-weight removes every label coefficient and turns the completed
source into the unweighted arithmetic orbit sum

\[
 \boxed{
 f(u)=\sum_{n\ge1}f_1(u+\log n).
 }                                                    \tag{251}
\]

This is a stronger explanation of the half-offset than multiplier neutrality
alone: at weight `1/2`, multiplicative label transport becomes literal
translation with unit coefficient.

Let

\[
 (T_p h)(u)=h(u+\log p),
 \qquad
 D_p=I-T_p.                                         \tag{252}
\]

Equation (251) gives

\[
 D_pf(u)
 =\sum_{p\nmid n}f_1(u+\log n)ge0.                \tag{253}
\]

Because the prime shifts commute, for every finite set of primes `S`,

\[
 \boxed{
 \left(\prod_{p\in S}D_p\right)f(u)
 =\sum_{\gcd(n,\prod_{p\in S}p)=1}
 f_1(u+\log n)ge0.
 }                                                    \tag{254}
\]

This is mixed-prime complete monotonicity on the multiplicative translation
semigroup.  An arbitrary positive decreasing source has the one-shift
inequalities `D_pf>=0`, but need not have all mixed differences positive.
Theta has them because every difference retains a faithful positive label
payload: it is exact arithmetic exclusion, not an alternating sum whose sign
must be estimated afterward.

The all-prime Deutsch--Popper conjecture can now be made substantially less
vague:

\[
 \boxed{
 \begin{minipage}{0.84\linewidth}
 Mixed-prime complete monotonicity (254), together with reciprocal modular
 sewing of the primitive seed across `u=0`, forces the reflected scattering
 section `S=E/E#` to be Schur in the correctly oriented half-plane.
 \end{minipage}
 }                                                    \tag{255}
\]

Both hypotheses are necessary candidates.  The mixed differences encode
arithmetic coherence but only on the positive chamber; modular sewing
relates that chamber to its reflected copy.  Dropping the first permits
incompatible prime charts, while dropping the second leaves the phase-blind
one-sided theorem (208).

This conjecture has a finite hostile program that is analytical rather than
numerical.  First ask whether (254) alone implies even the two-point
reflection inequality.  A finite positive orbit sum with two multiplicative
generators and a primitive seed provides the smallest counterexample class.
If a counterexample exists, impose the exact reciprocal-seed relation and
repeat.  Survival at that level would identify a genuinely source-derived
route from arithmetic exclusion coherence to Pick positivity.

## Hostile two-atom source falsifies mixed-prime positivity alone

The first stage of the hostile program fails in the smallest possible way.
Choose `0<b<a<log 2`, put `d=a-b`, and take the positive source measure

\[
 df(t)=A\,\delta_b+B\,\delta_a,
 \qquad A>B>0.                                     \tag{256}
\]

Every prime shift moves its support beyond the positive chamber.  Hence, for
every nonempty finite prime set `S`,

\[
 \left(\prod_{p\in S}(I-T_{\log p})\right)f=f\ge0. \tag{257}
\]

Thus the source satisfies the entire mixed-prime difference hierarchy in
the strongest but vacuous way.

Its centered oriented transform is

\[
 \widetilde E(q)=e^{iqb}\bigl(A+B e^{iqd}\bigr),
 \qquad
 \widetilde E^\#(q)=e^{-iqb}\bigl(A+B e^{-iqd}\bigr).
                                                               \tag{258}
\]

At

\[
 q_0=\frac\pi d+\frac i d\log\frac AB              \tag{259}
\]

one has `Im q_0>0` and

\[
 \widetilde E^\#(q_0)=0,                           \tag{260}
\]

while

\[
 \widetilde E(q_0)
 =e^{iq_0b}\left(A-\frac{B^2}{A}\right)\ne0.      \tag{261}
\]

Therefore `widetilde E/widetilde E#` has an upper-half-plane pole and cannot
be Schur.  The
counterexample is stable: replacing the atoms by sufficiently narrow
positive bumps preserves a nearby reflected zero, while support remains
inside `(0,log 2)` and (257) remains automatic.

We have proved the sharp no-go

\[
 \boxed{
 \text{mixed-prime complete monotonicity alone does not orient the
 reflected scattering section.}
 }                                                    \tag{262}
\]

This identifies why the modular clause in (255) is indispensable.
Arithmetic exclusion tests only forward prime translations.  A source
hidden entirely before the first prime seam passes all of them.  Reciprocal
modular sewing is the nonlocal condition that must prevent such a compact
primitive source from choosing its reflected phase arbitrarily.

For the actual completed theta source, evenness of `Phi` gives the bilateral
critical-weight relation

\[
 \boxed{
 f(-u)=e^u f(u),
 \qquad f(u)=e^{-u/2}\Phi(u).
 }                                                    \tag{263}
\]

The next hostile class must satisfy both (254) and (263).  The two-atom
construction does not.  The live question is whether their combination
still admits a finite reflected zero, or whether the reciprocal tail forced
by (263) converts the prime-difference hierarchy into genuine reflection
dominance.

## Reciprocal evenness alone does not repair the counterexample

The second hostile stage also fails if “modular sewing” means only (263).
Given any positive-chamber measure `f_+`, define its negative-chamber copy by

\[
 df(-u)=e^u df(u),
 \qquad u>0.                                        \tag{264}
\]

Then `Phi(u)=e^{u/2}f(u)` is even.  Applying this construction to the two
atoms in (256) produces mirrored atoms at `-b` and `-a` with the exact
reciprocal weights.  It satisfies (263) identically but does not alter the
positive-chamber transform (258), so the pole (260) survives.

The same construction works with the smooth hostile bumps already described.
Consequently

\[
 \boxed{
 \text{mixed-prime differences plus reciprocal evenness still do not imply
 reflected-sheet contractivity.}
 }                                                    \tag{265}
\]

This falsifies conjecture (255) as stated.  The phrase “reciprocal modular
sewing” was under-typed: bilateral symmetry is only a rule for extending a
chosen chamber, and places no restriction on what was chosen there.

The actual theta source contains a stronger, nonlocal law.  Its primitive
seed has the rigid Gaussian-exponential form

\[
 \phi_1(u)
 =\left(4\pi^2e^{9u/2}-6\pi e^{5u/2}\right)
   e^{-\pi e^{2u}},                                 \tag{266}
\]

and all arithmetic labels are its exact logarithmic translates.  The
bilateral completion relates the resulting *whole orbit sum* across the
fold; it is not an arbitrary even extension of a compact seed.

The corrected conjecture must therefore retain the heat/Gaussian orbit law:

\[
 \boxed{
 \begin{minipage}{0.84\linewidth}
 The unweighted multiplicative orbit (251) of the theta Gaussian seed,
 together with its completed bilateral identity, forces reflected-sheet
 dominance.  Neither mixed-prime positivity nor reciprocal symmetry after
 forgetting the seed is sufficient.
 \end{minipage}
 }                                                    \tag{267}
\]

This is harder to vary and more falsifiable.  The next admissible hostile
source must deform the primitive seed while preserving its heat equation,
translation orbit, and bilateral completion.  If those conditions leave no
deformation except scale normalization, we have found rigidity rather than
another positivity hierarchy.  If they admit a deformation with a reflected
zero, the proposed explanation fails.

## Gaussian scale deformation has one modular fixed point

The simplest admissible deformation can be classified exactly.  For `c>0`,
let

\[
 \Theta_c(u)=\sum_{n\in\mathbb Z}e^{-c n^2e^{2u}}.  \tag{268}
\]

Poisson summation gives

\[
 \Theta_c(u)
 =\sqrt{\frac\pi c}\,e^{-u}
   \Theta_{\pi^2/c}(-u).                            \tag{269}
\]

Introduce the normalized completed carrier

\[
 \mathcal F_c(u)
 =\left(\frac c\pi\right)^{1/4}e^{u/2}\Theta_c(u).
                                                               \tag{270}
\]

Then (269) becomes the exact sheet exchange

\[
 \boxed{
 \mathcal F_c(u)=\mathcal F_{\pi^2/c}(-u).
 }                                                    \tag{271}
\]

Thus modular reflection does not preserve an arbitrary Gaussian scale.  It
exchanges `c` with its dual `pi^2/c`.  A single source lies on the fixed
sheet precisely when

\[
 c=\frac{\pi^2}{c},
 \qquad\text{hence}\qquad
 \boxed{c=\pi.}                                     \tag{272}
\]

This proves a genuine rigidity statement: within the heat-kernel scale
family, the coefficient `pi` in the theta seed is selected uniquely by the
reciprocal fold.  It is not a fitted normalization.

The completed theta source itself is obtained from this carrier by the
reflection-invariant differential operator

\[
 \mathcal D=\partial_u^2-\frac14.                   \tag{273}
\]

Indeed, for `x=cn^2e^{2u}`,

\[
 \mathcal D\left(e^{u/2}e^{-cn^2e^{2u}}\right)
 =\left(4c^2n^4e^{9u/2}-6cn^2e^{5u/2}\right)
   e^{-cn^2e^{2u}}.                                 \tag{274}
\]

The `n=0` carrier mode is annihilated automatically.  At the fixed scale
`c=pi`, summing (274) over `n in Z` gives twice the positive-label convention
for the theta source `Phi`; the harmless factor two comes from `n` and `-n`.
Equation (271) then implies bilateral evenness of `Phi`.

The architecture is therefore forced:

\[
 \boxed{
 \text{Gaussian heat carrier}
 \xrightarrow{\text{Poisson duality}}
 c\leftrightarrow\pi^2/c
 \xrightarrow{c=\pi}
 \text{one reciprocal sheet}
 \xrightarrow{\partial_u^2-1/4}
 \Phi.
 }                                                    \tag{275}
\]

This explains the Gaussian scale, the reciprocal fold, the null carrier,
and the specific polynomial prefactor simultaneously.  It still does not
orient the reflected scattering quotient: a reflection-invariant
differential operator need not preserve total positivity or the Schur class.
The remaining question is now narrower—what positivity property of the
Gaussian heat carrier survives application of `D` and the arithmetic orbit
sum strongly enough to imply (214)?

## The completion polynomial is the Fourier shadow of the null carrier cusp

At the self-dual scale, write

\[
 \mathcal F(u)=e^{u/2}\Theta_\pi(u).
\]

By (271), `mathcal F` is even.  Its `n=0` asymptotic on the positive side is
`e^{u/2}`, so bilateral evenness identifies the global null carrier as

\[
 N(u)=e^{|u|/2}.                                    \tag{276}
\]

The renormalized carrier

\[
 R(u)=\mathcal F(u)-N(u)                            \tag{277}
\]

decays at both ends.  Away from the seam,

\[
 (\partial_u^2-1/4)N=0,
\]

but `N'` has jump one at `u=0`.  Therefore, distributionally,

\[
 \boxed{
 (\partial_u^2-1/4)N=\delta_0.
 }                                                    \tag{278}
\]

On the other hand, (274) and the `plus/minus n` pairing give

\[
 (\partial_u^2-1/4)\mathcal F=2\Phi.               \tag{279}
\]

Subtracting (278),

\[
 \boxed{
 (\partial_u^2-1/4)R=2\Phi-\delta_0.
 }                                                    \tag{280}
\]

With Fourier convention

\[
 \widehat R(k)=\int_{\mathbb R}R(u)e^{iku}du,
\]

equation (280) becomes

\[
 \boxed{
 2\widehat\Phi(k)-1
 =-(k^2+1/4)\widehat R(k).
 }                                                    \tag{281}
\]

This derives, from one geometric cusp, three features that previously looked
independent:

1. the constant carrier `1/2` in the physical transform;
2. the completion factor `1+4k^2`;
3. the source-fixed rank-one seam channel represented by `delta_0`.

The coincidence is exact.  The real carrier zero at `k^2=-1/4` is the
Fourier image of the null exponential `e^{|u|/2}`, while the constant term is
its derivative jump at the reciprocal fold.

This also removes a false avenue.  The operator `D` cannot be the missing
orientation mechanism: after renormalization it acts spectrally only by the
real polynomial `-(k^2+1/4)`.  It creates the known carrier zero and seam
term but cannot control the nontrivial zero geometry.  The RH-relevant phase
must be selected by the renormalized self-dual carrier `R`—equivalently by
how the Gaussian arithmetic orbit approaches and is sewn to its null
asymptote—not by the completion polynomial itself.

## The renormalized carrier is an exact positive tent mixture

On `u>0`, the carrier remainder is explicitly

\[
 R(u)=2e^{u/2}\sum_{n\ge1}e^{-\pi n^2e^{2u}}>0.     \tag{282}
\]

Every summand is strictly decreasing there because

\[
 \partial_u\left(e^{u/2}e^{-\pi n^2e^{2u}}\right)
 =\left(\frac12-2\pi n^2e^{2u}\right)
   e^{u/2}e^{-\pi n^2e^{2u}}<0.                    \tag{283}
\]

Away from the seam, (280) gives

\[
 R''(u)=\frac14R(u)+2\Phi(u)>0.                    \tag{284}
\]

Hence `R` is positive, strictly decreasing, and strictly convex on the
positive chamber, with `R` and `R'` tending to zero at infinity.  It has the
canonical tent decomposition

\[
 \boxed{
 R(u)=\int_u^\infty(t-u)R''(t)dt.
 }                                                    \tag{285}
\]

Taking the even Fourier transform and interchanging positive integrals,

\[
\begin{aligned}
 \widehat R(k)
 &=2\int_0^\infty R(u)\cos(ku)du\\
 &=\frac2{k^2}\int_0^\infty
 R''(t)\bigl(1-\cos(kt)\bigr)dt.                  \tag{286}
\end{aligned}
\]

Therefore

\[
 \boxed{
 \widehat R(k)>0\qquad(k\in\mathbb R),
 }                                                    \tag{287}
\]

with the value at `k=0` understood by continuity.  Strictness for nonzero
`k` follows because `R''(t)>0` on an interval while `1-cos(kt)` cannot vanish
there identically.

Combining (281) and (287) gives the exact real-axis orientation

\[
 1-2\widehat\Phi(k)
 =(k^2+1/4)\widehat R(k)>0.                         \tag{288}
\]

This is a universal coupled positivity theorem for the completed carrier:
the seam delta, completion polynomial, and convex theta remainder form one
positive real-axis object.  It uses the full source and no zero data.

Its limitation is equally exact.  Tent-mixture positivity controls the
Fourier transform only on the real axis.  The de Branges/Pick target compares
two complex sheets, where the cosine factor is replaced by an exponentially
weighted oscillatory polarization.  As shown earlier by the tent
counterexample, convexity does not orient that divided-difference kernel.
Thus (287) is a boundary theorem, not RH; the missing step remains coherent
complexification of this positive tent decomposition.

## Physical zeros are carrier-level crossings of the positive remainder

The convention must be typed carefully.  The decaying function `R` in
(277) is twice the positive theta remainder used earlier, while the physical
completed transform is `X=widehat Phi`.  Rearranging (281) gives

\[
 \boxed{
 X(k)=\frac12-H(k),
 \qquad
 H(k)=\frac12(k^2+1/4)\widehat R(k).
 }                                                    \tag{289}
\]

This is exactly the earlier null-mode decomposition (168dy), now derived
from the modular Gaussian carrier and its cusp.  By (287),

\[
 H(k)>0\qquad(k\in\mathbb R).                       \tag{290}
\]

Consequently real physical zeros are positive level crossings

\[
 \boxed{X(k)=0\quad\Longleftrightarrow\quad H(k)=1/2.} \tag{291}
\]

The tent representation makes the remainder explicit:

\[
 \boxed{
 H(k)=\frac{k^2+1/4}{k^2}
 \int_0^\infty R''(t)(1-\cos(kt))dt.
 }                                                    \tag{292}
\]

Since `H` is even, write `H(k)=h(k^2)`.  The RH-bearing question in this
coordinate is not positivity of `widehat R`; that is already proved.  It is
the level-set confinement statement

\[
 \boxed{
 h(z)=\frac12
 \quad\Longrightarrow\quad
 z\text{ lies on the physical real quotient ray}.
 }                                                    \tag{293}
\]

A sufficient explanation would make `h` a Pick/Stieltjes-type function with
the correct orientation and support, because a nonconstant Pick function
cannot take an interior real value away from its real boundary.  But (292)
is only a positive mixture of the atomic functions

\[
 h_t(z)=\frac{z+1/4}{z}
        \bigl(1-\cos(t\sqrt z)\bigr).               \tag{294}
\]

Earlier single-tent calculations already showed that these atoms are not
individually Pick or Loewner-positive.  Therefore positive mixing cannot be
invoked termwise.  The special theta density

\[
 R''(t)=\frac14R(t)+2\Phi(t)                        \tag{295}
\]

must provide a coupled cancellation among the hostile atomic directions.

This is the cleanest current statement of the missing theorem:

\[
 \boxed{
 \text{prove that the modular Gaussian mixing law (295) orients the
 complete tent mixture (292) as a quotient-ray Pick function.}
 }                                                    \tag{296}
\]

It is also the correct falsifier.  One off-ray solution of `h(z)=1/2`, or one
negative two-point Pick minor for `h`, defeats this proposed mechanism.  No
amount of real-axis positivity for `Rhat` can substitute for that test.

## Scope correction: the entire remainder cannot itself be Pick

The proposed sufficient mechanism in (296) is impossible as stated.  Since
`H(k)` is even entire, `h(z)` is entire.  Every entire function mapping the
upper half-plane to itself is affine,

\[
 h(z)=az+b,
 \qquad a\ge0,\quad b\in\mathbb R,                \tag{297}
\]

whereas the theta remainder in (292) is non-affine.  Therefore `h` cannot be
a global Pick function.  This closes the direct Loewner orientation of the
tent mixture independently of any numerical test.

The correct meromorphic object is the logarithmic derivative of the physical
level difference

\[
 X_\square(z)=\frac12-h(z),
 \qquad
 m(z)=-\frac{X_\square'(z)}{X_\square(z)}
 =\frac{h'(z)}{1/2-h(z)}.                           \tag{298}
\]

Its poles are exactly the level crossings (293).  Under the canonical-product
and growth audit, confinement of those poles to the physical real ray with
the sign-correct residues (equivalently positive spectral masses) is
equivalent to a Herglotz/Stieltjes representation of `m`, not of `h`.

The tent formula now supplies explicit numerator and denominator data:

\[
 m(z)=
 \frac{\partial_z\left[
  \dfrac{z+1/4}{z}
  \int_0^\infty R''(t)(1-\cos(t\sqrt z))dt
 \right]}
 {\dfrac12-
  \dfrac{z+1/4}{z}
  \int_0^\infty R''(t)(1-\cos(t\sqrt z))dt}.       \tag{299}
\]

Thus the corrected target is

\[
 \boxed{
 \text{derive the Herglotz orientation of the nonlinear ratio (299) from
 the modular Gaussian mixing law.}
 }                                                    \tag{300}
\]

This returns, with its typing now explicit, to the Stieltjes/logarithmic-
derivative frontier identified earlier.  The new contribution is not a
shortcut around that frontier: it derives both entries of the ratio from one
positive tent measure and identifies exactly why linear mixture positivity
was insufficient.

## Exact coupled-tent Bezoutian for the logarithmic derivative

Let

\[
 d\rho(t)=R''(t)dt,
 \qquad
 a_t(z)=\frac{z+1/4}{z}\bigl(1-\cos(t\sqrt z)\bigr),
                                                               \tag{301}
\]

so that

\[
 h(z)=\int_0^\infty a_t(z)d\rho(t),
 \qquad
 X_\square(z)=\frac12-h(z).                         \tag{302}
\]

The Pick kernel of `m=h'/X_square` is congruent, away from zeros of
`X_square`, to

\[
 \mathcal B(z,w)
 =\frac{h'(z)\overline{X_\square(w)}
       -X_\square(z)\overline{h'(w)}}
      {z-\bar w},                                   \tag{303}
\]

because

\[
 \frac{m(z)-\overline{m(w)}}{z-\bar w}
 =\frac{\mathcal B(z,w)}
 {X_\square(z)\overline{X_\square(w)}}.            \tag{304}
\]

Substituting (302) gives the exact source expansion

\[
\begin{aligned}
 \mathcal B(z,w)
={}&\frac1{2(z-\bar w)}
 \int\left(a_t'(z)-\overline{a_t'(w)}\right)d\rho(t)\\
 &+\frac1{z-\bar w}\iint
 \left[
 a_t(z)\overline{a_s'(w)}
 -a_t'(z)\overline{a_s(w)}
 \right]d\rho(t)d\rho(s).                         \tag{305}
\end{aligned}
\]

The first line is the constant-carrier interference.  The second is an
antisymmetric two-copy determinant.  Neither is positive term by term; their
coupling is the whole theorem.

On the real diagonal, (303) has the limit

\[
 \boxed{
 \mathcal B(x,x)
 =(h'(x))^2+\left(\frac12-h(x)\right)h''(x).
 }                                                    \tag{306}
\]

Thus the earlier “first universal coupled positivity theorem” is exactly the
diagonal of the full logarithmic-derivative Pick kernel.  Higher packet
positivity is not a separate hierarchy invented afterward; it is the
polarization of the same carrier-plus-two-copy determinant.

Equation (305) provides the sharp modular target.  The Gaussian theta law
must pair the negative orientations of the atomic determinants against the
linear carrier interference so that `mathcal B` is positive on every finite
packet.  A single negative `2 by 2` Gram determinant of (305) is the smallest
falsifier; diagonal positivity alone cannot close the argument.

## The infinitesimal two-point obstruction is one Schwarzian

Let `m` be real analytic at a real point `x` away from a physical zero and
consider the two-point Pick matrix at `x` and `x+epsilon`.  Its entries are

\[
 K_m(s,t)=\frac{m(s)-m(t)}{s-t},
 \qquad K_m(s,s)=m'(s).                             \tag{307}
\]

A direct Taylor expansion gives

\[
\begin{aligned}
 \det
 \begin{pmatrix}
 K_m(x,x)&K_m(x,x+\varepsilon)\\
 K_m(x+\varepsilon,x)&K_m(x+\varepsilon,x+\varepsilon)
 \end{pmatrix}
 =\frac{\varepsilon^2}{12}
 \left(2m'm'''-3(m'')^2\right)+O(\varepsilon^3).
                                                               \tag{308}
\end{aligned}
\]

Equivalently,

\[
 \boxed{
 \det K_m[x,x+\varepsilon]
 =\frac{\varepsilon^2}{6}(m'(x))^2
   \mathcal S m(x)+O(\varepsilon^3),
 }                                                    \tag{309}
\]

where

\[
 \mathcal S m
 =\frac{m'''}{m'}-\frac32\left(\frac{m''}{m'}\right)^2
                                                               \tag{310}
\]

is the Schwarzian derivative.  Therefore the first genuinely off-diagonal
necessary conditions are

\[
 m'(x)\ge0,
 \qquad
 \mathcal S m(x)\ge0.                               \tag{311}
\]

The first is exactly diagonal coupled positivity (306).  The second is the
infinitesimal rank-two obstruction.  This explains why the independent
Schwarzian lane repeatedly appeared: it is not another conjectural route,
but the collision limit of the smallest nontrivial Pick packet.

The carrier decomposition simplifies its numerator.  Put

\[
 X=\frac12-h,
 \qquad
 L=(h')^2+Xh'',
 \qquad
 m'=\frac{L}{X^2}.                                  \tag{312}
\]

Then two cancellations give

\[
 L'=h'h''+Xh''',
 \qquad
 L''=(h'')^2+Xh''''.                                \tag{313}
\]

Writing `q=m''/m'=(log L)'+2m` and using
`S m=q'-q^2/2`, one obtains the exact formula

\[
\boxed{
\begin{aligned}
 \mathcal S m
={}&\frac{(h'')^2+Xh''''}{L}
 -\frac32\left(\frac{h'h''+Xh'''}{L}\right)^2\\
 &-2\frac{h'}X\frac{h'h''+Xh'''}L
 +2\frac{h''}X.
\end{aligned}
}                                                     \tag{314}
\]

Every quantity in (314) is an explicit moment of the single positive tent
measure `rho` through (301).  The next analytical gate is therefore finite:
prove (or symbolically falsify) `S m>=0` before attempting arbitrary packet
size.  Success would establish local rank-two Pick positivity everywhere;
failure at one real point would rule out the entire Herglotz mechanism even
if the diagonal theorem survives.

## At the central point rank two is one cumulant Turan inequality

Normalize the even source to a probability measure

\[
 d\mathbb P(u)=\frac{\Phi(u)du}{X(0)},
 \qquad
 M_{2j}=\mathbb E[U^{2j}].                          \tag{315}
\]

In the quotient coordinate,

\[
 \frac{X_\square(z)}{X(0)}
 =\mathbb E\!\left[\cos(\sqrt z\,U)\right].        \tag{316}
\]

Put `ell(z)=log X_square(z)`.  Direct differentiation at the origin gives

\[
\begin{aligned}
 \ell''(0)&=\frac{A}{12},\\
 \ell'''(0)&=\frac{B}{120},\\
 \ell''''(0)&=\frac{C}{1680},                      \tag{317}
\end{aligned}
\]

where

\[
\begin{aligned}
 A={}&M_4-3M_2^2,\\
 B={}&-M_6+15M_2M_4-30M_2^3,\\
 C={}&M_8-28M_2M_6-35M_4^2
       +420M_2^2M_4-630M_2^4.                     \tag{318}
\end{aligned}
\]

These are precisely

\[
 A=\kappa_4,
 \qquad B=-\kappa_6,
 \qquad C=\kappa_8,                                \tag{319}
\]

the fourth, negative sixth, and eighth cumulants of the normalized theta
source.

Since `m=-ell'`,

\[
 m'(0)=-\ell''(0)=-\frac{\kappa_4}{12}.            \tag{320}
\]

Thus central diagonal positivity is exactly negative fourth cumulant:

\[
 \boxed{\kappa_4\le0.}                              \tag{321}
\]

Moreover

\[
 \mathcal S m(0)
 =\frac{\ell''(0)\ell''''(0)
       -\frac32(\ell'''(0))^2}
      {(\ell''(0))^2}.                             \tag{322}
\]

After clearing the positive denominators, the infinitesimal rank-two gate is

\[
 \boxed{
 10\,\kappa_4\kappa_8-21\,\kappa_6^2\ge0.
 }                                                    \tag{323}
\]

This is a cumulant Turan inequality.  In the nondegenerate positive regime
`kappa_4<0`, it forces `kappa_8<0` with enough magnitude to dominate the
sixth-cumulant square.  A Gaussian has all three higher cumulants zero and
sits at the completely degenerate boundary; rank-two reserve measures the
specific non-Gaussian organization of the theta source.

Equation (323) is the smallest exact symbolic falsifier now available.  It
uses only four even source moments and no zero data.  Ordinary positivity or
log-concavity does not automatically imply this higher cumulant relation;
the next proof attempt must use the modular Gaussian orbit to control the
joint signs and magnitude, rather than bounding each moment independently.

## Cusp-normalized exponentials have the opposite Stieltjes orientation

The carrier identity (280) has a solvable comparison family.  For
`a>1/2`, define

\[
 R_a(u)=\frac1{2a}e^{-a|u|}.                        \tag{324}
\]

Its derivative jump at the seam is `-1`, exactly like the theta remainder.
Therefore

\[
 (\partial_u^2-1/4)R_a
 =\frac{a^2-1/4}{2a}e^{-a|u|}-\delta_0.            \tag{325}
\]

The associated positive source is

\[
 \Phi_a(u)=\frac{a^2-1/4}{4a}e^{-a|u|}.            \tag{326}
\]

Since

\[
 \widehat R_a(k)=\frac1{a^2+k^2},                  \tag{327}
\]

the physical quotient transform is

\[
 \boxed{
 X_a(z)=\frac{a^2-1/4}{2(a^2+z)},
 \qquad z=k^2.
 }                                                    \tag{328}
\]

Its logarithmic derivative is the one-atom resolvent

\[
 \boxed{
 m_a(z)=-\frac{X_a'(z)}{X_a(z)}
 =\frac1{a^2+z}.
 }                                                    \tag{329}
\]

Thus the same null carrier, cusp coefficient, completion operator, and
positive source lead exactly to a one-atom Stieltjes function.  But its pole
is at `z=-a^2`, and

\[
 m_a'(x)=-\frac1{(a^2+x)^2}<0.                     \tag{329a}
\]

So `m_a` has the **opposite** half-plane orientation from the RH-bearing
logarithmic derivative with poles on the positive quotient ray.  Its Pick
matrices are negative semidefinite in the convention (307), and all higher
local determinants vanish after rank one.

This model clarifies the cumulant gate by contrast.  A single exponential
carrier is rank one and has no rank-two reserve, but it selects the carrier
ray rather than the physical zero ray.  The theta source must both generate
strict rank growth and reverse this naive decay-scale orientation.

More generally, if the theta remainder admitted a positive Laplace mixture

\[
 R(u)=\int_{1/2}^\infty\frac{e^{-a|u|}}{2a}d\sigma(a),
 \qquad d\sigma\ge0,
 \qquad \sigma([1/2,\infty))=1,                    \tag{330}
\]

then its physical transform would be

\[
 X(z)=\frac12\int_{1/2}^\infty
 \frac{a^2-1/4}{a^2+z}d\sigma(a),                 \tag{331}
\]

a Stieltjes function supported on the negative carrier ray.  It is zero-free
off that ray, but its logarithmic derivative has the anti-Herglotz
orientation and does not model positive physical zero locations.

However, (330) is equivalent to complete monotonicity of `R` on the positive
chamber, and the superexponential theta tail cannot be a nonzero positive
Laplace mixture of fixed exponentials.  So this condition is both too strong
for theta and oriented toward the wrong ray.  It supplies a useful no-go
comparison:

\[
 \boxed{
 \text{modular arithmetic sewing must produce physical-ray Herglotz
 orientation by a mechanism unavailable to positive exponential mixtures.}
 }                                                    \tag{332}
\]

In other words, theta cannot merely behave like a positive decay-scale
spectrum.  Such a spectrum naturally places singular support on the negative
resolvent ray.  The modular fold must convert causal decay geometry into
positive-ray level-crossing geometry.  That orientation reversal is now an
explicit part of the missing explanation.

## The central cumulant polynomial is exactly an inverse-zero Hankel minor

The unusual coefficients in (323) have a precise conditional explanation.
Suppose, only for this audit, that the physical quotient has a canonical
product with positive real zero locations `lambda_j` and no unaccounted
polynomial contribution:

\[
 \frac{X_\square(z)}{X_\square(0)}
 =\prod_j\left(1-\frac z{\lambda_j}\right).        \tag{333}
\]

Put

\[
 S_r=\sum_j\lambda_j^{-r}.                          \tag{334}
\]

Then

\[
 \ell^{(r)}(0)=-(r-1)!S_r.                         \tag{335}
\]

Comparing (335) with (317)--(319) gives

\[
 \kappa_4=-12S_2,
 \qquad
 \kappa_6=240S_3,
 \qquad
 \kappa_8=-10080S_4.                               \tag{336}
\]

Therefore

\[
 \boxed{
 10\kappa_4\kappa_8-21\kappa_6^2
 =1\,209\,600\left(S_2S_4-S_3^2\right).
 }                                                    \tag{337}
\]

The right side is the Hankel determinant

\[
 \det
 \begin{pmatrix}
 S_2&S_3\\
 S_3&S_4
 \end{pmatrix}
 \ge0                                               \tag{338}
\]

by Cauchy--Schwarz for the vectors
`(lambda_j^{-1})_j` and `(lambda_j^{-2})_j`.  Equality means that the
positive spectral measure has rank one.

This calculation is not a proof of (323), because (333) is the desired
zero-location representation.  Its role is diagnostic.  It shows that the
central source cumulant inequality is exactly the shadow of a positive
inverse-zero Gram matrix; the coefficients `10` and `21` are forced by the
factorials relating Fourier cumulants to logarithmic zero moments.

The source-side objective is now extremely concrete:

\[
 \boxed{
 \text{construct directly from the modular Gaussian carrier two source
 vectors whose Gram determinant equals the left side of (337).}
 }                                                    \tag{339}
\]

Such a construction would prove central rank-two positivity without zero
input and would reveal the finite-dimensional prototype of the full
Stieltjes tower.  Conversely, failure to realize this one determinant as a
source Gram form would make an all-orders Gram construction implausible.

## On the negative quotient ray the target is ordinary susceptibility

The cumulants in (315)--(323) arise from a familiar positive object before
analytic continuation.  Let

\[
 K(t)=\log\mathbb E[e^{tU}]                        \tag{340}
\]

be the cumulant-generating function of the normalized even theta source.
Near the origin,

\[
 \ell(z)=\log\frac{X_\square(z)}{X_\square(0)}
 =K(i\sqrt z).                                     \tag{341}
\]

Consequently

\[
 m(z)=-\ell'(z)
 =-\frac{i}{2\sqrt z}K'(i\sqrt z).                \tag{342}
\]

On the negative quotient ray, put `z=-s^2` with `s>0`.  Evenness of `K`
then gives

\[
 \boxed{
 m(-s^2)=\frac{K'(s)}{2s}.
 }                                                    \tag{343}
\]

Here `K'(s)` is the mean of `U` under the honest tilted probability measure

\[
 d\mathbb P_s(u)
 =\frac{e^{su}d\mathbb P(u)}{\mathbb E[e^{sU}]}.   \tag{344}
\]

Thus `m(-s^2)` is mean response per unit field.  It is positive for `s>0`
because convexity and evenness of `K` imply `K'(s)>0`.  Its derivatives are
controlled by the tilted variance and higher connected responses:

\[
 K''(s)=\operatorname{Var}_{\mathbb P_s}(U)>0.      \tag{345}
\]

This locates the conceptual gap exactly.  On the negative carrier ray, the
candidate Stieltjes object is an ordinary probabilistic susceptibility and
its basic positivity costs nothing.  Passing to positive `z` performs the
Wick rotation, turning a positive exponential tilt into an oscillatory
Fourier comparison.  Probability positivity does not survive that rotation
automatically.  In symbols, the continuation is

\[
 s\mapsto i\sqrt z.
\]

The RH mechanism must therefore explain

\[
 \boxed{
 \text{why the Euclidean susceptibility }K'(s)/(2s)
 \text{ has a positive spectral continuation whose poles occur only on the
 physical quotient ray.}
 }                                                    \tag{346}
\]

This recasts the desired source Gram construction (339): it should be a
reflection-positive or modular-sewing theorem that transports covariance
positivity of the real tilted measures (344) through the Wick rotation.
Without such a theorem, cumulant inequalities at the origin are only finite
Taylor shadows of ordinary Euclidean convexity.

## RH becomes a Stieltjes law for Euclidean susceptibility versus field squared

Set

\[
 r=s^2,
 \qquad
 g(r)=m(-r)=\frac{K'(\sqrt r)}{2\sqrt r}.           \tag{347}
\]

If the desired positive spectral representation holds, then for a positive
measure `nu` on the physical zero coordinate,

\[
 \boxed{
 g(r)=\int_0^\infty\frac{d\nu(\lambda)}
 {\lambda+r}.
 }                                                    \tag{348}
\]

Conversely, subject to the canonical-product, continuation, support, and
polynomial-term audit, a source-derived representation (348) analytically
continues to

\[
 m(z)=\int_0^\infty\frac{d\nu(\lambda)}
 {\lambda-z},                                      \tag{349}
\]

placing its poles on the physical positive quotient ray.

This removes the rhetorical mystery from “transport positivity through Wick
rotation.”  The concrete Euclidean theorem is:

\[
 \boxed{
 \text{the mean susceptibility per field of the tilted theta source is a
 Stieltjes function of field squared.}
 }                                                    \tag{350}
\]

There is an exact variance formula.  Since `K'(0)=0`,

\[
\begin{aligned}
 g(s^2)
 &=\frac1{2s}\int_0^sK''(t)dt\\
 &=\frac12\int_0^1
 \operatorname{Var}_{\mathbb P_{qs}}(U)dq.         \tag{351}
\end{aligned}
\]

Thus `g` is half the average variance encountered while the external field
is increased from zero to `s`.  Its positivity is automatic.  The missing
content is the much stronger Stieltjes organization of that response.

For example,

\[
 g'(s^2)
 =\frac{sK''(s)-K'(s)}{4s^3}.                      \tag{352}
\]

The first complete-monotonicity inequality `g'<=0` is therefore

\[
 \boxed{
 K'(s)\ge sK''(s),
 }                                                    \tag{353}
\]

meaning that the average variance along the tilt is at least the terminal
variance.  A sufficient local mechanism is monotone decrease of tilted
variance with field.  At `s=0`, (353) reduces to `kappa_4<=0`, exactly the
central diagonal gate (321).

The Taylor series is

\[
 \boxed{
 g(r)=\frac{\kappa_2}{2}
 +\frac{\kappa_4}{12}r
 +\frac{\kappa_6}{240}r^2
 +\frac{\kappa_8}{10080}r^3+\cdots.
 }                                                    \tag{354}
\]

Hence alternating cumulant signs are the derivative shadows of complete
monotonicity, while the Turan inequality (323) is the first Hankel constraint
distinguishing a genuine Stieltjes response from an arbitrary completely
monotone Taylor series.

This formulation suggests a source operator target with no spectral zeros
inserted:

\[
 \boxed{
 \frac{K'(s)}{2s}
 =\langle\Omega,(A+s^2)^{-1}\Omega\rangle,
 \qquad A=A^*>0,
 }                                                    \tag{355}
\]

where `A` and `Omega` must be constructed from the Gaussian orbit and modular
sewing.  This is the Euclidean version of the proposed Hilbert--Polya object.
It would generate every cumulant Hankel inequality simultaneously and make
the Wick continuation automatic.

## Scope correction: the spectral measure has infinite total mass

The ordinary Hilbert-vector formulation in (355) fails a far-field growth
audit.  Up to normalization,

\[
 \mathbb E[e^{sU}]
 =\frac{\xi(1/2+s)}{\xi(1/2)}.                     \tag{356}
\]

Stirling's formula and the absolutely convergent Euler product on the far
right give

\[
 K'(s)
 =\frac12\log\frac{s}{2\pi}+O(1/s),
 \qquad s\to+\infty.                               \tag{357}
\]

Therefore

\[
 \boxed{
 g(s^2)=\frac{K'(s)}{2s}
 =\frac1{4s}\log\frac{s}{2\pi}+O(s^{-2}).
 }                                                    \tag{358}
\]

If `Omega` were an ordinary Hilbert vector and `A>=0`, then

\[
 0\le
 \langle\Omega,(A+s^2)^{-1}\Omega\rangle
 \le\frac{\|\Omega\|^2}{s^2},                     \tag{359}
\]

contradicting (358).  Hence (355) is impossible with `Omega in H`.

This is exactly what the expected zero counting predicts.  The candidate
measure is locally finite and obeys

\[
 \int_0^\infty\frac{d\nu(\lambda)}{1+\lambda}<\infty,
\]

so its Stieltjes transform exists, but

\[
 \nu([0,\infty))=\infty.                            \tag{360}
\]

It cannot be the spectral measure of an ordinary vector.  The faithful
operator statement must use a boundary distribution in a rigged Hilbert
space, or equivalently define the convergent resolvent form directly.  Its
derivative has the positive squared-resolvent form

\[
 \boxed{
 -g'(r)=\int_0^\infty\frac{d\nu(\lambda)}
 {(\lambda+r)^2},
 }                                                    \tag{361}
\]

but the generating boundary vector remains generalized rather than
square-summable.

This correction preserves the Stieltjes target (348) while sharpening the
operator typing:

\[
 \boxed{
 \text{source-derived positive self-adjoint operator}
 +\text{ generalized boundary functional}
 +\text{ resolvent-admissibility},
 }                                                    \tag{362}
\]

not an ordinary cyclic vector.  Any proposed Hilbert--Polya construction
that assigns finite norm to the unit-weight zero channel is inconsistent
with the completed theta asymptotics before zero locations are considered.

## RH is the Lee--Yang property of the completed theta-source measure

The Euclidean formulation has a standard statistical-mechanical name.  From
(356), the moment-generating function of the normalized theta source is

\[
 \boxed{
 Z(s)=\mathbb E[e^{sU}]
 =\frac{\xi(1/2+s)}{\xi(1/2)}.
 }                                                    \tag{363}
\]

The Riemann hypothesis is therefore exactly the statement

\[
 \boxed{
 Z(s)=0\quad\Longrightarrow\quad\operatorname{Re}s=0.
 }                                                    \tag{364}
\]

In other words, the completed theta-source distribution has the Lee--Yang
property: all zeros of its external-field partition function lie on the
imaginary field axis.

This identification organizes the finite inequalities already found:

\[
\begin{array}{c|c}
 \text{theta-source quantity}&\text{statistical-mechanical meaning}\\
 \hline
 K'(s)&\text{magnetization}\\
 K''(s)&\text{susceptibility}\\
 K'''(s)&\text{field derivative of susceptibility}\\
 \kappa_{2n}&\text{connected zero-field responses}\\
 g(s^2)=K'(s)/(2s)&\text{susceptibility per field, averaged from zero}
\end{array}                                          \tag{365}
\]

The inequality

\[
 K'(s)\ge sK''(s)                                   \tag{366}
\]

is a GHS-type decreasing-susceptibility statement.  The signs
`kappa_4<=0`, `kappa_6>=0`, `kappa_8<=0`, and the Hankel constraint (323) are
successive connected-response shadows of the full Lee--Yang property.

This is explanatory progress but not a proof.  An arbitrary positive,
log-concave, or reflection-symmetric single-site measure need not be
Lee--Yang.  The missing source theorem must place the very specific theta
measure in a known stability-preserving class, or derive an analogous class
from modular arithmetic transport.

The strongest current Deutsch--Popper conjecture can now be stated without
metaphor:

\[
 \boxed{
 \begin{minipage}{0.84\linewidth}
 The completed modular Gaussian orbit is the magnetization marginal of a
 source-derived ferromagnetic/stable system.  Its finite approximants have
 the Lee--Yang property, and their partition functions converge in a
 zero-preserving topology to `xi(1/2+s)/xi(1/2)`.
 \end{minipage}
 }                                                    \tag{367}
\]

If such approximants exist, the imaginary-axis zero theorem would be
inherited by the limit after the usual nontriviality and local-uniform
convergence audit.  If the smallest faithful theta truncation cannot be
represented by a stable ferromagnetic partition function, this particular
explanation is finitely falsified.

The representation must be source-faithful.  Matching finitely many
cumulants or fitting an Ising model after seeing the answer would not count.
The couplings, boundary condition, and external-field observable must be
derived from the Gaussian label transport, prime-scale exclusion law, and
modular fold already present in the carrier.

## Euclidean reflection positivity alone is universally too weak

For every positive source measure, regardless of its zero geometry, the
Euclidean kernel

\[
 Z(s+\bar t)
 =\mathbb E[e^{sU}\overline{e^{tU}}]               \tag{368}
\]

is positive semidefinite.  It is simply the Gram kernel of the features
`e^{sU}`.  Thus ordinary Osterwalder--Schrader-style reflection positivity of
the scalar source is automatic and cannot select the Lee--Yang class.

The smallest hostile example is an even three-atom measure with partition
function

\[
 Z_{A,B}(s)=A+B\cosh(as),
 \qquad A>B>0.                                     \tag{369}
\]

It has a positive Euclidean Gram kernel (368), but its zeros satisfy

\[
 \cosh(as)=-A/B.                                   \tag{370}
\]

Since `A/B>1`, these include

\[
 \boxed{
 s=\frac1a\left(
 \mathop{\rm arcosh}(A/B)+i(2j+1)\pi
 \right),
 \qquad j\in\mathbb Z,
 }                                                    \tag{371}
\]

and their reflected partners.  Their real parts are nonzero.  Smooth positive
even approximations preserve nearby zeros by local-uniform perturbation.

Therefore

\[
 \boxed{
 \text{positivity of the Euclidean source Gram plus reflection symmetry does
 not imply the Lee--Yang property.}
 }                                                    \tag{372}
\]

The missing finite approximation theorem must preserve a stronger notion:
multivariate stability, ferromagnetic Lee--Yang contraction, or an equivalent
zero-preserving operation at every source step.  Only after establishing
that local stability may one pass to the modular/infinite limit.  A proof
that merely constructs positive transfer matrices or reflection-positive
Euclidean kernels has not crossed the decisive gate.

## The discrete Gaussian carrier is Lee--Yang in the label field

There is nevertheless a source-level stability object already present.  For
`0<q<1`, introduce the bilateral discrete-Gaussian fugacity partition

\[
 \vartheta(q,z)=\sum_{n\in\mathbb Z}q^{n^2}z^{2n}.  \tag{373}
\]

Jacobi's triple product gives

\[
 \boxed{
 \vartheta(q,z)
 =\prod_{m\ge1}(1-q^{2m})
  (1+q^{2m-1}z^2)
  (1+q^{2m-1}z^{-2}).
 }                                                    \tag{374}
\]

For positive `q`, every zero in the label-fugacity coordinate `z^2` lies on
the negative real ray.  Thus the Gaussian label carrier has an exact
Lee--Yang factorization before any scale integration.

This does not prove (364), because the physical external field is conjugate
to the logarithmic scale `u`, not to the integer label `n`.  The theta source
is obtained by setting

\[
 q=e^{-\pi e^{2u}},                                 \tag{375}
\]

applying the completion/energy differential operator in `u`, specializing
the label fugacity, and finally taking the bilateral Laplace transform in
`u`.  Schematically,

\[
 \boxed{
 \text{label-field stable theta product}
 \xrightarrow{\text{heat/energy insertion}}
 \Phi(u)
 \xrightarrow{\text{Mellin--Laplace pushforward}}
 Z(s).
 }                                                    \tag{376}
\]

Neither arrow is automatically stability preserving.  Differentiation in
`u` acts through the heat parameter `q`, not through the stable fugacity
variable, and positive integration over `u` is a mixture operation; the
three-atom falsifier shows that such mixtures can create off-axis zeros.

This isolates a concrete theorem candidate:

\[
 \boxed{
 \text{the self-dual theta heat flow and completed Mellin pushforward form a
 stability-preserving composite, even though neither operation is stable in
 isolation.}
 }                                                    \tag{377}
\]

That composite would be a hard-to-vary explanation: the triple product
supplies local Lee--Yang factors, the heat equation transports them through
scale, and modular self-duality supplies the missing boundary condition at
the fold.  The smallest falsifier is to apply the exact completed differential
operator and Mellin pushforward to a finite self-dual Gaussian approximation
and find an off-axis zero.  A non-self-dual label truncation is not faithful
enough to test (377), because it breaks the boundary mechanism before the
stability question is asked.

## Mellin audit: prime valuation chains are Lee--Yang on the wrong line

The critically weighted primitive seed in (249) has an elementary bilateral
Mellin transform.  From (266),

\[
 f_1(u)=e^{-u/2}\phi_1(u)
 =\left(4\pi^2e^{4u}-6\pi e^{2u}\right)
   e^{-\pi e^{2u}}.                                 \tag{378}
\]

With `x=pi e^{2u}` one obtains

\[
\begin{aligned}
 \mathcal M f_1(s)
 &=\int_{\mathbb R}f_1(u)e^{su}du\\
 &=(s-1)\pi^{-s/2}\Gamma(1+s/2)\\
 &=\frac{s(s-1)}2\pi^{-s/2}\Gamma(s/2).           \tag{379}
\end{aligned}
\]

This factor has no nontrivial zeros; it is exactly the archimedean completion
factor before multiplication by the arithmetic orbit.

Using (251), translation by `log n` contributes `n^{-s}`.  In the initial
half-plane of absolute convergence,

\[
\begin{aligned}
 \mathcal M f(s)
 &=\mathcal M f_1(s)\sum_{n\ge1}n^{-s}\\
 &=\frac{s(s-1)}2\pi^{-s/2}\Gamma(s/2)\zeta(s)\\
 &=\boxed{\xi(s)}.                                  \tag{380}
\end{aligned}
\]

Thus the Gaussian seed, unweighted translation orbit, and completed zeta
function are not analogous objects; they are literally related by Mellin
factorization.

Now truncate one prime valuation chain faithfully:

\[
 P_{p,N}(s)=\sum_{j=0}^Np^{-js}
 =\frac{1-p^{-(N+1)s}}{1-p^{-s}}.                  \tag{381}
\]

Its zeros obey

\[
 p^{-s}=e^{2\pi i m/(N+1)},
 \qquad m=1,\ldots,N,
\]

and therefore

\[
 \boxed{\operatorname{Re}s=0.}                    \tag{382}
\]

Products of finite independent valuation chains preserve this natural
Lee--Yang line.  But it is the wrong line for RH:

\[
 \operatorname{Re}s=0
 \qquad\text{versus}\qquad
 \operatorname{Re}s=\frac12.                       \tag{383}
\]

This closes another shortcut.  Independent Euler/valuation stability cannot
prove RH, even though each finite factor is perfectly Lee--Yang.  The
half-offset is created only when the right-hand Mellin factorization is sewn
to its reflected continuation by

\[
 \xi(s)=\xi(1-s),                                   \tag{384}
\]

whose fixed locus is `Re s=1/2`.

The operator's “last-moment bi-split” intuition can now be stated exactly:

\[
 \boxed{
 \text{unfolded multiplicative transport selects }\operatorname{Re}s=0;
 \quad
 \text{completed reciprocal folding replaces it by the fixed line }
 \operatorname{Re}s=1/2.
 }                                                    \tag{385}
\]

What remains unexplained is why the fold *confines every zero* to its fixed
line rather than merely making the zero set symmetric about it.  Symmetry
alone permits off-line quartets.  The missing stability theorem must couple
the two Mellin sheets before the infinite Euler limit, not append the
functional equation after independent prime factors have already been
formed.

## The smallest symmetric prime fold produces an off-line quartet

Take the first nontrivial valuation chain

\[
 P_p(s)=1+p^{-s}.                                   \tag{386}
\]

Its zeros lie on the unfolded line `Re s=0`.  The most direct additive fold

\[
 Q_p(s)=P_p(s)+P_p(1-s)                            \tag{387}
\]

obeys `Q_p(s)=Q_p(1-s)` exactly.  Center the coordinate by

\[
 z=(s-1/2)\log p.                                  \tag{388}
\]

Then

\[
 \boxed{
 Q_p(s)=2+2p^{-1/2}\cosh z.
 }                                                    \tag{389}
\]

Its zeros satisfy

\[
 \cosh z=-\sqrt p.                                 \tag{390}
\]

Since `sqrt p>1`, they are

\[
 \boxed{
 z=\mathord\pm\mathop{\rm arcosh}(\sqrt p)
   +(2j+1)\pi i,
 \qquad j\in\mathbb Z.
 }                                                    \tag{391}
\]

Thus the smallest exactly reflection-symmetric prime model already has an
off-fixed-line quartet.  Multiplicative symmetrization is no better:
`P_p(s)P_p(1-s)` retains the two original zero lines `Re s=0` and `Re s=1`.

This proves

\[
 \boxed{
 \text{prime-factor Lee--Yang stability plus exact functional-equation
 symmetry does not imply fixed-line stability.}
 }                                                    \tag{392}
\]

The repair threshold is explicit.  Add a source-fixed scalar seam current
`c_p`:

\[
 Q_{p,c}(s)=2+c_p+2p^{-1/2}\cosh z.                \tag{393}
\]

All zeros lie on the fixed line `Re z=0` precisely when

\[
 \boxed{
 \left|1+\frac{c_p}{2}\right|\le p^{-1/2}.
 }                                                    \tag{394}
\]

For the uncorrected fold `c_p=0`, the inequality fails by the factor
`sqrt p`.  A positive scalar addition makes it worse; the minimal real repair
must be negative and satisfy

\[
 -2(1+p^{-1/2})le c_p
 \le-2(1-p^{-1/2}).                                \tag{395}
\]

This is the one-prime Lee--Yang analogue of the level-44 secular repair.
The functional equation supplies symmetry, but a quantitatively typed seam
channel must overcome one unstable even direction.  Its sign here is fixed:
it subtracts excess carrier mass rather than adding positive bulk.

The next source audit is now finite and exact.  Extract the actual seam term
from the completed theta Mellin identity at one prime scale and compare its
centered coefficient with (394).  If it misses the interval (395), no
prime-local additive repair can explain RH; the stabilization must be
collective across primes or infinite-dimensional in the modular seam.

## The divided antisymmetric fold repairs one prime step canonically

The additive fold (387) is not the only canonical way to obtain a symmetric
readout.  Define the divided antisymmetric fold

\[
 \boxed{
 (\mathfrak D P)(s)
 =\frac{P(s)-P(1-s)}{2s-1}.
 }                                                    \tag{396}
\]

Both numerator and denominator change sign under `s\mapsto1-s`, so
`mathfrak D P` is symmetric and the apparent singularity at `s=1/2` is
removable.

For the one-step prime chain `P_p(s)=1+p^{-s}`, use the centered coordinate
`z=(s-1/2)log p`.  Then

\[
 P_p(s)-P_p(1-s)=-2p^{-1/2}\sinh z,                \tag{397}
\]

and hence, up to a nonzero constant,

\[
 \boxed{
 (\mathfrak D P_p)(s)
 \sim\frac{\sinh z}{z}.
 }                                                    \tag{398}
\]

Every nontrivial zero is

\[
 z=j\pi i,
 \qquad j\in\mathbb Z\setminus\{0\},             \tag{399}
\]

exactly on the fixed line.  No fitted scalar repair is needed.  The
order-one odd numerator and the order-one fold coordinate cancel at the
center, leaving an order-two symmetric readout.

This is the first explicit finite model in which the *fold operation itself*
creates Lee--Yang confinement.  It matches the recurring Carrier pattern

\[
 \boxed{
 \text{sheet-odd transport current}
 \longrightarrow
 \text{division by the fold coordinate}
 \longrightarrow
 \text{sheet-even physical readout}.
 }                                                    \tag{400}
\]

The mechanism is not automatically stable at finite valuation depth.  For

\[
 P_{p,2}(s)=1+p^{-s}+p^{-2s},
\]

put `r=p^{-1/2}`.  Its odd numerator is

\[
 -2\left(r\sinh z+r^2\sinh2z\right)
 =-2r\sinh z\left(1+2r\cosh z\right).              \tag{401}
\]

Besides the fixed-line zeros of `sinh z`, it has

\[
 \cosh z=-\frac1{2r}=-\frac{\sqrt p}{2}.           \tag{402}
\]

For primes `p>=5`, these are off the fixed line.  Thus even the correct fold
can fail at a finite valuation cutoff.

The infinite valuation chain behaves differently:

\[
 P_{p,\infty}(s)=\frac1{1-p^{-s}}.
\]

Its odd difference is

\[
 \boxed{
 P_{p,\infty}(s)-P_{p,\infty}(1-s)
 =\frac{-2r\sinh z}
 {1-2r\cosh z+r^2}.
 }                                                    \tag{403}
\]

The numerator has only fixed-line zeros.  The additional off-line events are
poles of the local Euler factor, not zeros; their disposition belongs to
global completion and analytic continuation.

This gives a much sharper candidate architecture:

\[
 \boxed{
 \text{complete each valuation tower}
 \to\text{form its sheet-odd current}
 \to\text{divide by the common fold coordinate}
 \to\text{perform collective pole cancellation}.
 }                                                    \tag{404}
\]

Two hard gates remain.  The odd difference of a product is not the product
of the odd differences, so cross-prime coupling must be derived rather than
assumed.  And local Euler poles must cancel through the archimedean/modular
seam without reintroducing off-line zeros.  Nevertheless, (398)--(403) show
that the order-two quotient is not cosmetic: it is the first operation in
the chain that actually converts unfolded prime transport into fixed-line
zero geometry.

## The completed theta partition is a positive mixture of divided odd currents

The order-two quotient has an exact source realization, not merely a prime
toy model.  Center the external field:

\[
 Z(t)=\frac{\xi(1/2+t)}{\xi(1/2)}
 =\frac1{X(0)}\int_{\mathbb R}\Phi(u)e^{tu}du.      \tag{405}
\]

The completed source is even, and the earlier log-concavity theorem implies

\[
 \Phi'(u)<0\qquad(u>0).                             \tag{406}
\]

Define the oriented source current

\[
 J(u)=-\Phi'(u).                                    \tag{407}
\]

Then `J` is odd and `J(u)>0` on the positive chamber.  Integration by parts
on the full line gives

\[
 tX(0)Z(t)
 =\int_{\mathbb R}J(u)e^{tu}du
 =2\int_0^\infty J(u)\sinh(tu)du.                  \tag{408}
\]

Therefore

\[
 \boxed{
 Z(t)=\frac2{X(0)}\int_0^\infty
 J(u)\frac{\sinh(tu)}tdu,
 \qquad J(u)>0.
 }                                                    \tag{409}
\]

Each atomic divided current

\[
 \frac{\sinh(tu)}t                                  \tag{410}
\]

is even in `t` and has all nontrivial zeros on the imaginary field axis.
Thus the actual completed theta partition is a positive mixture of
elementary Lee--Yang functions generated by the sheet-odd source current.

This is substantially closer to the desired explanation than the positive
cosh mixture.  The fold coordinate has already been divided out, and the
mixing density is not arbitrary: it is the derivative current of the modular
Gaussian source.

But positive mixtures of the atoms (410) do not preserve their zero line in
general.  The depth-two calculation (401)--(402) is exactly such a failure.
Hence (409) reduces RH to a classical-looking but source-specific mixture
problem:

\[
 \boxed{
 \text{why does the modular current }J=-\Phi'
 \text{ make its positive }\sinh(tu)/t\text{ mixture Lee--Yang?}
 }                                                    \tag{411}
\]

The candidate answer must be a variation-diminishing or total-positivity
property of `J` stronger than positivity.  This reconnects directly to the
adjacent-band transport program: on `t=ix`, the atoms become

\[
 \frac{\sin(xu)}x,                                  \tag{412}
\]

and zero confinement depends on how the positive current weights consecutive
sine bands.  The source-derived current, rather than `Phi` or its
autocorrelation, is now the faithful object whose sign-regularity must be
tested.

## The faithful current sequence is a Jensen-hyperbolicity target

Pass from the centered field to its square:

\[
 F(y)=Z(\sqrt y).                                   \tag{413}
\]

Because the source is even,

\[
 F(y)=\sum_{n\ge0}a_ny^n,
 \qquad
 a_n=\frac{\mathbb E[U^{2n}]}{(2n)!}>0.            \tag{414}
\]

Using the odd current and integrating by parts,

\[
 \boxed{
 a_n=\frac2{X(0)(2n+1)!}
 \int_0^\infty u^{2n+1}J(u)du.
 }                                                    \tag{415}
\]

The Lee--Yang/RH statement is

\[
 \boxed{
 F(y)=0\quad\Longrightarrow\quad y<0.
 }                                                    \tag{416}
\]

Under the standard reality, order, and local-uniform approximation audit,
this is membership of `F` in the type-I Laguerre--Polya class.  Equivalently,
all Jensen polynomials built from

\[
 \gamma_n=n!a_n
 =\frac{2n!}{X(0)(2n+1)!}
  \int_0^\infty u^{2n+1}J(u)du                    \tag{417}
\]

must be hyperbolic with the correct negative-root orientation.

For degree `d` and shift `r`, the source-derived Jensen polynomial is

\[
 \boxed{
 \mathcal J_d^{(r)}(x)
 =\sum_{j=0}^d\binom dj\gamma_{r+j}x^j.
 }                                                    \tag{418}
\]

This gives an exact meaning to “variation diminution of the current.”  It is
not merely monotonicity of `J` in `u`; it is simultaneous hyperbolicity of
every factorially normalized moment projection (418).

The first nontrivial polynomial is

\[
 \mathcal J_2^{(0)}(x)
 =1+2\frac{M_2}{2}x
 +2\frac{M_4}{24}x^2.                              \tag{419}
\]

Its discriminant condition is

\[
 M_2^2-\frac{M_4}{3}\ge0
 \quad\Longleftrightarrow\quad
 \kappa_4\le0,                                     \tag{420}
\]

exactly the central diagonal gate.  Higher Jensen discriminants polarize
into the cumulant/Hankel conditions already found; the Schwarzian rank-two
test is their logarithmic-derivative form.

Thus the adjacent-band and moment programs have finally met on one faithful
object:

\[
 \boxed{
 J=-\Phi'
 \longrightarrow
 \text{factorially normalized odd-current moments}
 \longrightarrow
 \text{Jensen hyperbolicity}
 \longrightarrow
 \text{Lee--Yang/RH}.
 }                                                    \tag{421}
\]

This remains a characterization until a source operation is shown to
preserve (418).  The best constructive target is now to derive a recurrence
or cone-preserving transfer for the Jensen polynomials directly from the
Gaussian prime-translation orbit.  One nonhyperbolic polynomial is a finite
falsifier; accumulating positive scalar moments is not.

## All quadratic Jensen gates reduce to outward score stiffening

Write the normalized even source density as

\[
 d\mathbb P(u)=c e^{-V(u)}du,
 \qquad V(-u)=V(u).                                 \tag{422}
\]

Define the Gaussian-normalized even moments

\[
 b_n=\frac{M_{2n}}{(2n-1)!!}.                      \tag{423}
\]

Since

\[
 \gamma_n
 =\frac{n!M_{2n}}{(2n)!}
 =2^{-n}b_n,                                       \tag{424}
\]

hyperbolicity of every quadratic Jensen polynomial `J_2^{(r)}` is exactly
log-concavity of `(b_n)`:

\[
 \boxed{b_{n+1}^2\ge b_nb_{n+2}\qquad(n\ge0).}     \tag{425}
\]

Integration by parts gives, for `n>=1`,

\[
 (2n-1)M_{2n-2}
 =\mathbb E[U^{2n-1}V'(U)].                        \tag{426}
\]

Put

\[
 W(u)=\frac{V'(u)}u,
 \qquad u>0.                                       \tag{427}
\]

Then

\[
 \frac{b_n}{b_{n-1}}
 =\frac{M_{2n}}{(2n-1)M_{2n-2}}
 =\frac1{\mathbb E_{\mathbb Q_n}[W(U)]},          \tag{428}
\]

where `Q_n` is the positive probability tilt

\[
 d\mathbb Q_n(u)
 =\frac{u^{2n}d\mathbb P(u)}{M_{2n}}.              \tag{429}
\]

As `n` increases, the measures `Q_n` move outward in monotone-likelihood-
ratio order with respect to `|u|`.  Therefore, if

\[
 \boxed{
 W'(u)=\frac{uV''(u)-V'(u)}{u^2}\ge0
 \qquad(u>0),
 }                                                    \tag{430}
\]

then `E_{Q_n}[W]` increases with `n`, the ratios `b_n/b_{n-1}` decrease, and
(425) follows for every shift.

We have proved the source theorem

\[
 \boxed{
 \frac{V'(u)}u\text{ increasing}
 \quad\Longrightarrow\quad
 \mathcal J_2^{(r)}\text{ hyperbolic for every }r\ge0.
 }                                                    \tag{431}
\]

The condition has a direct physical meaning: restoring force per unit
displacement stiffens as one moves away from the modular seam.  A Gaussian
has constant `W` and saturates every inequality; strict outward stiffening
produces strict quadratic Jensen reserve.

For theta, `V(u)=-log Phi(u)`, so the remaining degree-two gate is the
pointwise source inequality

\[
 \boxed{
 -u(\log\Phi)''(u)+(\log\Phi)'(u)\ge0
 \qquad(u>0).
 }                                                    \tag{432}
\]

This is stronger than the already proved strict log-concavity
`(log Phi)''<0`; strong curvature alone does not say that curvature stiffens
outward.  Equation (432) is now the smallest analytical target capable of
proving an infinite family of Jensen gates at once.  Its failure would not
falsify RH, but it would falsify outward-score stiffening as the explanation
of the complete quadratic hierarchy.

## Outward score stiffening is strictly true at the modular seam

Because `Phi` is even,

\[
 (\log\Phi)'(0)=(\log\Phi)'''(0)=0.                \tag{433}
\]

The first nonzero jet of the stiffening numerator in (432) is

\[
 -u(\log\Phi)''(u)+(\log\Phi)'(u)
 =-\frac13(\log\Phi)''''(0)u^3+O(u^5).             \tag{434}
\]

Its sign can be decided directly from the theta source.  Put

\[
 x_n=\pi n^2
\]

and define polynomials by

\[
 P_0(x)=4x^2-6x,
 \qquad
 P_{r+1}(x)=2xP_r'(x)+(1/2-2x)P_r(x).              \tag{435}
\]

Then

\[
 \Phi^{(r)}(0)=\sum_{n\ge1}P_r(x_n)e^{-x_n}.       \tag{436}
\]

The needed even polynomials are

\[
\begin{aligned}
 P_2(x)={}&-\frac{75}{2}x+165x^2-112x^3+16x^4,\\
 P_4(x)={}&-\frac{1875}{8}x+\frac{15465}{4}x^2
 -8512x^3+5176x^4-1056x^5+64x^6.                 \tag{437}
\end{aligned}
\]

Since the odd sums vanish by modular evenness,

\[
 (\log\Phi)''''(0)
 =\frac{\Phi''''(0)}{\Phi(0)}
 -3\left(\frac{\Phi''(0)}{\Phi(0)}\right)^2.      \tag{438}
\]

Elementary rational bounds `3.14159<pi<3.14160`, Taylor bounds for the
exponential, and a geometric majorant for `n>=3` give

\[
\begin{aligned}
 0&<\Phi(0)<0.9,\\
 \Phi''(0)&<-16.70,\\
 0&<\Phi''''(0)<813.                               \tag{439}
\end{aligned}
\]

For transparency, the only material tail estimates are

\[
 P_2(\pi)e^{-\pi}<-17.43,
 \qquad
 \sum_{n\ge2}|P_2(\pi n^2)|e^{-\pi n^2}<0.73,
\]

and

\[
 \sum_{n\ge1}|P_4(\pi n^2)|e^{-\pi n^2}<813;
\]

after `n=3`, the ratio is dominated by a polynomial factor times
`e^{-pi(2n+1)}` and is below a geometric series with ratio `1/1000`.

The coarse bounds already have ample margin:

\[
 \Phi''''(0)\Phi(0)
 <813(0.9)=731.7
 <3(16.70)^2
 <3(\Phi''(0))^2.                                  \tag{440}
\]

Therefore

\[
 \boxed{(\log\Phi)''''(0)<0.}                      \tag{441}
\]

Combining (434) and (441), there exists `epsilon>0` such that

\[
 \boxed{
 -u(\log\Phi)''(u)+(\log\Phi)'(u)>0
 \qquad(0<u<\varepsilon).
 }                                                    \tag{442}
\]

Thus the degree-two Jensen mechanism is strictly valid near the modular
seam.  The remaining obstruction is global: the stiffening numerator could
still reverse sign on an intermediate interval before the superexponential
tail makes the primitive Gaussian curvature dominant again.

## Outward score stiffening is also strict on the far chamber

The far region can be handled labelwise.  Put

\[
 x_n=\pi n^2e^{2u},
 \qquad
 \phi_n(u)=e^{u/2}(4x_n^2-6x_n)e^{-x_n},
 \qquad
 V_n=-\log\phi_n.                                  \tag{443}
\]

Direct differentiation gives

\[
\begin{aligned}
 V_n'&=2x_n-\frac52-\frac{4x_n}{2x_n-3},\\
 V_n''&=4x_n+\frac{24x_n}{(2x_n-3)^2}.             \tag{444}
\end{aligned}
\]

Hence

\[
\begin{aligned}
 uV_n''-V_n'
={}&x_n(4u-2)+\frac52
 +\frac{4x_n}{2x_n-3}
 +\frac{24ux_n}{(2x_n-3)^2}.                      \tag{445}
\end{aligned}
\]

Every term is nonnegative and the constant term is strict when `u>=1/2`.
Thus every individual theta label stiffens outward on the far chamber.

For the aggregate `Phi=sum phi_n`, let

\[
 w_n(u)=\frac{\phi_n(u)}{\Phi(u)}.
\]

Mixture differentiation gives the exact identity

\[
 \boxed{
 uV''-V'
 =\sum_nw_n(u)\bigl(uV_n''-V_n'\bigr)
 -u\operatorname{Var}_{w(u)}(V_n').
 }                                                    \tag{446}
\]

The variance is the only possible loss of stiffening.  It is exponentially
small.  With `x=pi e^{2u}` and `u>=1/2`,

\[
 \frac{\phi_n(u)}{\phi_1(u)}
 =n^2\frac{2n^2x-3}{2x-3}e^{-(n^2-1)x}
 \le2n^4e^{-(n^2-1)x}.                             \tag{447}
\]

Also `|V_n'-V_1'|<=3n^2x`.  Consequently

\[
 u\operatorname{Var}_{w}(V_n')
 \le18ux^2\sum_{n\ge2}n^8e^{-(n^2-1)x}.           \tag{448}
\]

Since `x>=pi e>8`, the right side is dominated by its `n=2` term and a
geometric tail; using `u<=x` gives the coarse uniform bound

\[
 u\operatorname{Var}_{w}(V_n')<10^{-3}.            \tag{449}
\]

Meanwhile (445) gives `uV_1''-V_1'>5/2`, and (447) gives `w_1>0.999`.
Substitution in (446) proves

\[
 \boxed{
 -u(\log\Phi)''(u)+(\log\Phi)'(u)>0
 \qquad(u\ge1/2).
 }                                                    \tag{450}
\]

Combining (442) and (450), outward score stiffening is now proved near the
modular seam and throughout the far chamber.  Only a compact intermediate
interval

\[
 \varepsilon\le u<1/2                              \tag{451}
\]

remains.  Closing it requires a structural comparison of the first few
overlapping labels, not asymptotic certification or higher Jensen algebra.

## The global quadratic theorem is monotone curvature of the theta potential

Let

\[
 Q(u)=uV''(u)-V'(u).                                \tag{452}
\]

Since `V'(0)=0`, one has `Q(0)=0`, and differentiation gives the exact
cancellation

\[
 \boxed{Q'(u)=uV'''(u).}                            \tag{453}
\]

Therefore the source condition

\[
 \boxed{
 V'''(u)\ge0\qquad(u>0)
 }                                                    \tag{454}
\]

implies outward score stiffening globally and hence every quadratic Jensen
gate through (431).  In source language,

\[
 \boxed{
 (\log\Phi)'''(u)\le0qquad(u>0).
 }                                                    \tag{455}
\]

This says that the already negative logarithmic curvature of `Phi` becomes
more negative as one moves away from the modular fold.

The endpoint results fit this statement exactly.  Equation (441) says

\[
 V''''(0)=-(\log\Phi)''''(0)>0,                    \tag{456}
\]

so `V'''` leaves the seam in the positive direction.  In the far chamber,
the primitive Gaussian label has positive curvature derivative; equation
(450) already proves the required weaker conclusion `Q>0` there without
assuming global curvature monotonicity.

For reference, an individual label has

\[
 V_n'''(u)
 =8x_n-\frac{48x_n(2x_n+3)}{(2x_n-3)^3}.           \tag{457}
\]

It is positive as soon as

\[
 (2x_n-3)^3>6(2x_n+3).                             \tag{458}
\]

All labels `n>=2` satisfy this already at the seam; only the first label has
a short initial transition.  Modular mixing is therefore needed only to
bridge that single primitive transition while enforcing `V'''(0)=0`.

The remaining analytical problem has become a small structural lemma:

\[
 \boxed{
 \text{prove that the aggregate modular correction keeps }V'''\ge0
 \text{ until the }n=1\text{ curvature derivative turns positive.}
 }                                                    \tag{459}
\]

If (459) closes, then (454), (431), and (425) prove hyperbolicity of every
degree-two Jensen polynomial in one chain.  This would be the first infinite
Jensen family derived directly from source geometry rather than from zeros
or asymptotic hyperbolicity.

## The modular repair is one explicit scalar tail, not an uncontrolled mixture

The mixture correction in (459) admits two exact descriptions.  Write

\[
 a_n=V_n',\qquad b_n=V_n'',\qquad c_n=V_n''',
 \qquad \bar a=\sum_nw_na_n.                       \tag{460}
\]

Differentiating an expectation with moving Gibbs weights gives

\[
 \frac d{du}\sum_nw_nh_n
 =\sum_nw_nh_n'-\operatorname{Cov}_w(h,a).         \tag{461}
\]

Applying this twice to `V=-log sum exp(-V_n)` yields

\[
 \boxed{
 V'''=\mathbb E_w[c]
       -3\operatorname{Cov}_w(a,b)
       +\mathbb E_w[(a-\bar a)^3].
 }                                                    \tag{462}
\]

This identity types the repair which was invisible in the labelwise audit.
The positive-label average is not the whole answer: increasing score and
curvature produce a covariance loss, while the right-skewed distribution of
label scores produces a cubic repair.  At the modular seam these three terms
cancel exactly because `V'''(0)=0`.  Thus the exceptional first label is not
repaired by a pointwise positive summand; it is repaired, if at all, by the
oriented third cumulant of the complete label ensemble.

For proving the sign, however, there is an even sharper coordinate.  Factor
out the primitive label:

\[
 \Phi(u)=\phi_1(u)(1+R(u)),
 \qquad
 R(u)=\sum_{n\ge2}r_n(u),
 \qquad r_n=\frac{\phi_n}{\phi_1}.                 \tag{463}
\]

With `x=pi e^{2u}`, every tail ratio is explicit:

\[
 \boxed{
 r_n(x)=n^2\frac{2n^2x-3}{2x-3}
          e^{-(n^2-1)x}.
 }                                                    \tag{464}
\]

Consequently

\[
 \boxed{
 V'''(u)=V_1'''(u)-\bigl(\log(1+R(u))\bigr)'''.
 }                                                    \tag{465}
\]

Equations (462) and (465) are the same modular correction in ensemble and
primitive-tail coordinates.  The latter removes all moving-weight
combinatorics.  If

\[
 u_*:=\frac12\log\frac{x_*}{\pi},
 \qquad (2x_*-3)^3=6(2x_*+3),                      \tag{466}
\]

then `V_1'''<0` only for `0<u<u_*`.  The entire primitive transition is
therefore equivalent to the scalar inequality

\[
 \boxed{
 -\bigl(\log(1+R)\bigr)'''\ge -V_1'''
 \qquad(0<u<u_*).
 }                                                    \tag{467}
\]

There is no numerical parameter and no fitted repair in (467): `R` is the
source-prescribed sum (464).  Moreover, writing

\[
 D:=2x\frac d{dx}=\frac d{du},                     \tag{468}
\]

turns (467) into the explicit one-variable inequality

\[
 \boxed{
 -D^3\log\!\left(
 1+\sum_{n\ge2}n^2\frac{2n^2x-3}{2x-3}
 e^{-(n^2-1)x}
 \right)
 \ge
 \frac{48x(2x+3)}{(2x-3)^3}-8x
 }                                                    \tag{469}
\]

for `pi<x<x_*`.  This is the smallest faithful analytic form of the seam
problem found so far.  It also explains why replacing the theta ensemble by
the primitive Gaussian fails: the entire left side of (469), including the
exact seam cancellation, would be deleted.

The next proof step is now bounded and source-typed.  Separate

\[
 R=r_2+T_3,
 \qquad T_3=\sum_{n\ge3}r_n,                       \tag{470}
\]

retain `r_2` exactly, and bound `D^jT_3` for `0<=j<=3` by the first omitted
exponential times a geometric majorant.  A successful comparison proves
(467) analytically; failure identifies the first derivative order at which
the two-label modular repair is insufficient.  No finite grid or
zero-location input is relevant to this test.

The logarithm introduces no further hierarchy.  For any positive `1+R`,

\[
 -D^3\log(1+R)
 =\frac{
 -(1+R)^2D^3R
 +3(1+R)(DR)(D^2R)
 -2(DR)^3
 }{(1+R)^3}.                                      \tag{471}
\]

Thus (469) is equivalent, after multiplication by the positive denominator,
to one polynomial inequality in the four source jets

\[
 R,\quad DR,\quad D^2R,\quad D^3R.                \tag{472}
\]

Each jet is a termwise sum of an explicit rational function of `x` times
`e^{-(n^2-1)x}`.  In particular, if

\[
 R=r_2+T_3,
\]

then substitution into the numerator of (471) separates it into the exact
two-label contribution plus terms containing at least one of

\[
 T_3,\quad DT_3,\quad D^2T_3,\quad D^3T_3.         \tag{473}
\]

There are no hidden products of infinitely many labels: every remainder
monomial contains a typed tail jet which can be majorized directly.  The
faithful certificate therefore has the form

\[
 \boxed{
 \mathcal P_2(x)-\mathcal E_3(x)
 \ge (1+r_2+T_3)^3
 \left(\frac{48x(2x+3)}{(2x-3)^3}-8x\right),
 }                                                    \tag{474}
\]

where `mathcal P_2` is obtained from (471) using `R=r_2` exactly and
`mathcal E_3` is an explicit absolute majorant for all monomials meeting
(473).  This is a finite symbolic certificate with an analytic tail, not a
finite sampling certificate.

One subtlety must be preserved.  At `u=0`, the equality `V'''(0)=0` is a
property of the completed modular source, so the full tail participates in
the exact seam balance.  The `n=2` truncation must not be required to satisfy
that equality by itself.  The useful comparison is therefore either strict
on `0<u<u_*` with a seam-compatible first-order factor removed, or performed
after writing

\[
 V'''(u)=u\int_0^1V''''(tu)\,dt.                  \tag{475}
\]

Equation (475) converts the vanishing endpoint into a regular fourth-
derivative comparison.  It prevents interval or tail estimates from wasting
their entire margin on reproducing an exact cancellation at a single point.

## The infinite tail has a closed exponential jet envelope

The transition interval in (466) is itself elementary.  The left side of
the defining equation is smaller than the right side at `x=pi`, while at
`x=7/2` they are respectively `64` and `60`.  Monotonicity of their ratio
therefore gives

\[
 \pi<x_*<\frac72.                                  \tag{476}
\]

Thus every estimate needed for the primitive transition lives in the narrow
fixed strip `pi<=x<=7/2`.

For each label put `lambda_n=n^2-1`.  The logarithmic `D`-derivative of
(464) is exactly

\[
 L_n:=D\log r_n
 =\frac{4n^2x}{2n^2x-3}
  -\frac{4x}{2x-3}
  -2\lambda_nx.                                   \tag{477}
\]

Define rational functions recursively by

\[
 P_{n,0}=1,
 \qquad P_{n,j+1}=DP_{n,j}+L_nP_{n,j}.            \tag{478}
\]

Then no differentiation of an infinite series is left implicit:

\[
 \boxed{D^jr_n=r_nP_{n,j}\qquad(0\le j\le4).}     \tag{479}
\]

On `x>=pi` and `n>=2`, the two rational denominators in (477) are bounded
away from zero.  A direct induction in (478), using `Dx=2x`, gives the coarse
but uniform estimate

\[
 |P_{n,j}(x)|\le(8n^2x)^j
 \qquad(0\le j\le4).                              \tag{480}
\]

Together with (447), this yields for the omitted tail

\[
 \boxed{
 |D^jT_3(x)|
 \le2(8x)^je^{-8x}C_j,
 \quad
 C_j:=\sum_{n\ge3}n^{4+2j}e^{-(n^2-9)\pi},
 \quad0\le j\le4.
 }                                                    \tag{481}
\]

The constants `C_j` are source-independent numerical series with positive
terms.  They require no theta evaluation and have a geometric majorant:
for `n>=3`, successive exponential factors gain at least `e^{-7pi}`, so
splitting off `n=3` and bounding the polynomial ratio gives an elementary
rational function of `e^{-7pi}`.  In particular, every tail jet carries the
common scale `e^{-8x}`.

This changes the logical shape of the remaining theorem.  The exact
two-label expression carries scale `e^{-3x}`, whereas every omitted-label
error carries `e^{-8x}`.  After the modular seam zero is removed using (475),
the repair margin and the error are separated by the source-forced gap

\[
 e^{-8x}/e^{-3x}=e^{-5x}\le e^{-5\pi}.             \tag{482}
\]

Therefore the infinite-label problem away from the exact modular seam has
been reduced to an analytic error envelope.  What remains is to expand the
exact `r_2` contribution to `V''''`, prove its post-seam lower bound on
`pi<=x<=x_*`, and compare that bound with (481) at `j=0,...,4`.  The seam
itself requires the separate coherence audit below.

## Modular completion creates an exponentially thin boundary layer

The exact two-label algebra is best written as a two-state Gibbs system, not
as an expanded numerator.  Put

\[
 r=r_2,
 \qquad \ell=\log r,
 \qquad p=\frac r{1+r}.                            \tag{483}
\]

Repeated differentiation of `log(1+exp ell)` gives the exact fourth-order
identity

\[
\begin{aligned}
 D^4\log(1+r)={}&pD^4\ell
 +4p(1-p)(D\ell)(D^3\ell)
 +3p(1-p)(D^2\ell)^2\\
 &+6p(1-p)(1-2p)(D\ell)^2D^2\ell\\
 &+p(1-p)(1-6p+6p^2)(D\ell)^4.                  \tag{484}
\end{aligned}
\]

Here every derivative of `ell` is rational because

\[
 \ell=\log4+\log(8x-3)-\log(2x-3)-3x.            \tag{485}
\]

Thus the exact two-label fourth derivative is

\[
 \boxed{
 V_{\{1,2\}}''''=V_1''''-D^4\log(1+r_2),
 }                                                    \tag{486}
\]

with the second term given by the five factored channels in (484).  This is
the useful finite expression: its signs can be bounded channelwise without
destroying the cancellation through expansion.

There is, however, an important nonuniformity.  The complete modular source
obeys

\[
 V'''(0)=0,                                        \tag{487}
\]

whereas a finite label truncation has no reason to obey (487).  From (481),
the discrepancy between the complete and two-label third derivatives at the
seam is of order `e^{-8pi}`.  On the other hand the first nonzero outward
growth supplied by (486) is of order

\[
 u e^{-3\pi}.                                     \tag{488}
\]

Balancing (487)--(488) identifies the natural seam scale

\[
 \boxed{u_{\mathrm{mod}}\asymp e^{-5\pi}.}         \tag{489}
\]

This is not a fitted cutoff.  It is the ratio between the first omitted
modular label scale and the first repairing label scale.  It exposes a
singular-perturbation structure:

\[
\begin{array}{c|c}
 0\le u\lesssim e^{-5\pi}
   & \text{all-label modular sewing enforces the seam orientation},\\
 e^{-5\pi}\ll u\le u_*
   & \text{the exact two-label repair dominates the analytic tail}.
\end{array}                                        \tag{490}
\]

Therefore `retain n=2 and bound the rest` is valid only after leaving the
modular boundary layer.  At the seam itself, the tiny tail is qualitatively
decisive despite being quantitatively negligible.  This is the same
source-versus-readout lesson encountered earlier: a small coefficient may
carry an exact coherence condition which cannot be deleted by norm size.

The global proof now has two compatible local certificates:

1. use `V''''(0)>0` together with explicit fifth-derivative bounds for the
   complete theta series on `0<=u<=C e^{-5pi}`;
2. use the factored two-label identity (484), plus (481), from
   `C e^{-5pi}` through `u_*`.

The overlap constant `C` must be chosen from the two analytic bounds before
either estimate is evaluated.  If their admissible intervals overlap, (459)
closes.  If they do not, the uncovered interval is the exact falsifier of
this curvature route.

## The two-label certificate has exactly one internal repair channel

The derivatives in (484) have a transparent rational coordinate.  Set

\[
 \alpha=\frac3{8x-3},
 \qquad
 \beta=\frac3{2x-3}.                              \tag{491}
\]

For `z=3/(ax-3)` one has

\[
\begin{aligned}
 D\log(ax-3)&=2(1+z),\\
 D^2\log(ax-3)&=-4z(1+z),\\
 D^3\log(ax-3)&=8z(1+z)(1+2z),\\
 D^4\log(ax-3)&=-16z(1+z)(1+6z+6z^2).           \tag{492}
\end{aligned}
\]

Since

\[
 0<\alpha<\beta<1
 \qquad(\pi\le x\le7/2),                         \tag{493}
\]

equations (485) and (492) give

\[
 D\ell<0,qquad D^2\ell<0,qquad D^3\ell<0.       \tag{494}
\]

The fourth derivative is

\[
 D^4\ell
 =16\{h(\beta)-h(\alpha)\}-48x,
 \qquad h(z)=z(1+z)(1+6z+6z^2).                  \tag{495}
\]

This retains a one-variable rational sign test rather than hiding it in an
expanded polynomial.

That last sign test is elementary on the transition strip.  From
`pi<x<=7/2` and `pi>3`,

\[
 \beta\ge\frac34,
 \qquad
 0<\alpha<\frac17.                                \tag{495a}
\]

The polynomial `h` in (495) is strictly increasing for positive arguments.
Consequently

\[
\begin{aligned}
 h(\beta)-h(\alpha)
 &>h\!\left(\frac34\right)-h\!\left(\frac17\right)\\
 &=\frac{1491}{128}-\frac{776}{2401}
 >\frac{21}{2}
 \ge3x.                                           \tag{495b}
\end{aligned}
\]

Substitution in (495) proves

\[
 \boxed{D^4\ell>0\qquad(\pi<x\le x_*).}           \tag{495c}
\]

The Gibbs weight is uniformly tiny.  The rational prefactor of `r_2` is
decreasing in `x`, and at `x>=pi`

\[
 4\frac{8x-3}{2x-3}<28,
 \qquad e^{3x}>e^{3\pi}>23^3>12000.
\]

Therefore

\[
 0<p<r_2<\frac7{3000}<\frac1{400}.                \tag{496}
\]

In particular,

\[
 1-2p>0,
 \qquad 1-6p+6p^2>0.                              \tag{497}
\]

Substitution of (494) and (497) into (484) classifies its channels:

\[
\begin{array}{c|c}
 pD^4\ell & >0,\\
 4p(1-p)(D\ell)(D^3\ell) & >0,\\
 3p(1-p)(D^2\ell)^2 & >0,\\
 6p(1-p)(1-2p)(D\ell)^2D^2\ell & <0,\\
 p(1-p)(1-6p+6p^2)(D\ell)^4 & >0.
\end{array}                                        \tag{498}
\]

Because the target is `V_1''''-D^4 log(1+r_2)`, the orientation of this table
must be read with a minus sign.  Four channels consume primitive reserve.
The unique negative channel is the internal repair:

\[
 \boxed{
 6p(1-p)(1-2p)(D\ell)^2D^2\ell<0.
 }                                                    \tag{499}
\]

The primitive reserve is also explicitly positive:

\[
 \boxed{
 V_1''''(u)
 =16x+\frac{96x(4x^2+24x+9)}{(2x-3)^4}>0.
 }                                                    \tag{500}
\]

Consequently the post-seam theorem no longer requires estimating (484) by
absolute values.  One should retain the negative channel (499) exactly and
compare the four reserve-consuming channels jointly with (500).  Discarding
(499) would lose precisely the internal cancellation which makes the
two-label repair work.

The next exact inequality is therefore

\[
 \boxed{
 V_1''''
 -pD^4\ell
 -4p(1-p)(D\ell)(D^3\ell)
 -3p(1-p)(D^2\ell)^2
 -p(1-p)(1-6p+6p^2)(D\ell)^4
 \ge
 6p(1-p)(1-2p)(D\ell)^2D^2\ell,
 }                                                    \tag{501}
\]

with the right side negative.  If the left side is nonnegative, (501) is
automatic.  If it is negative, its magnitude must be no larger than the
repair supplied by the negative cubic channel; the `n>=3` envelope is then
added with its correct worst-case orientation.  This is the smallest
sign-resolved form of the two-label curvature certificate.

## Exponential dilution beats growth of the dangerous score channel

Introduce positive magnitudes

\[
 A=-D\ell,
 \qquad B=-D^2\ell,
 \qquad C=-D^3\ell,
 \qquad E=D^4\ell.                                \tag{502}
\]

Equations (494) and (495c) prove `A,B,C,E>0`.  They also give the differential
chain

\[
 DA=B,
 \qquad DB=C,
 \qquad DC=-E,                                   \tag{503}
\]

while the logistic weight satisfies

\[
 Dp=-p(1-p)A.                                    \tag{504}
\]

In these variables the exact two-label cost is

\[
\begin{aligned}
 D^4\log(1+r_2)={}&pE+4p(1-p)AC+3p(1-p)B^2\\
 &+p(1-p)A^2
 \left[(1-6p+6p^2)A^2-6(1-2p)B\right].          \tag{505}
\end{aligned}
\]

Thus the internal repair is already combined with the nominally largest
quartic consumer in the final bracket.

The pure quartic envelope decreases strictly.  Indeed, from the explicit
formulas,

\[
 A>6x,
 \qquad B<12x.                                   \tag{506}
\]

Therefore, using `x>pi>3` and (496),

\[
 \frac{4B}{A^2}<\frac4{3x}<\frac49<1-p.          \tag{507}
\]

Equations (503)--(504) now give

\[
\begin{aligned}
 D\log(pA^4)
 &=-(1-p)A+\frac{4B}{A}\\
 &=A\left[-(1-p)+\frac{4B}{A^2}\right]<0.        \tag{508}
\end{aligned}
\]

Hence

\[
 \boxed{p(x)A(x)^4\text{ is strictly decreasing on }[\pi,x_*].} \tag{509}
\]

This is the first global budget inequality on the full primitive-transition
strip.  It says that the channel with fourth-power score growth is largest
at the modular seam; moving outward cannot create a new quartic instability.
The remaining terms in (505) are lower-order mixed channels.  Their useful
structure is already visible in (503): `AC` benefits from `DC=-E<0`, while
the only outward growth in `B^2` is controlled by `DB=C`.  The next bounded
task is to prove monotonicity of their ratios to the primitive reserve (500),
not to expand (505).

## Every reserve-consuming envelope is seam-maximal

Put

\[
 q=p(1-p),
 \qquad d=1-2p.                                  \tag{510}
\]

Then

\[
 D\log q=-dA.                                    \tag{511}
\]

The `AC` channel decreases immediately:

\[
 D\log(qAC)
 =-dA+\frac BA-\frac EC
 <-dA+2<0,                                       \tag{512}
\]

where `B/A<2` follows from (506).  For the `B^2` channel, (492)--(493) give

\[
 B>12x-8>28,
 \qquad C<24x+48<132.                            \tag{513}
\]

Hence

\[
 D\log(qB^2)
 =-dA+\frac{2C}{B}
 <-\frac{199}{200}18+\frac{264}{28}<0.           \tag{514}
\]

Finally, (495) can be differentiated without expansion.  Since
`Dz=-2z(1+z)` and the function `z(1+z)h'(z)` is increasing for `z>0`,

\[
 DE
 =-32\{\beta(1+\beta)h'(\beta)
       -\alpha(1+\alpha)h'(\alpha)\}-96x<0.      \tag{515}
\]

Together with `Dp<0`, this proves

\[
 \boxed{pE,\quad qAC,\quad qB^2
 \text{ are strictly decreasing on }[\pi,x_*].}  \tag{516}
\]

The quartic consumer and cubic repair must be kept paired.  Since
`1-6p+6p^2<1`, their bracket in (505) is bounded above by

\[
 K:=A^2-6dB.                                     \tag{517}
\]

This envelope is positive because

\[
 K>A^2-6B>36x^2-72x=36x(x-2)>0.                 \tag{518}
\]

Moreover,

\[
 DK=2AB(1-6q)-6dC<2AB.                          \tag{519}
\]

Using (506), (518), and `x>3`,

\[
 \frac{DK}{K}
 <\frac{24xA}{36x(x-2)}
 =\frac{2A}{3(x-2)}<\frac{2A}{3}.                \tag{520}
\]

Therefore

\[
\begin{aligned}
 D\log(qA^2K)
 &=-dA+\frac{2B}{A}+\frac{DK}{K}\\
 &<-\frac{199}{200}A+4+\frac{2A}{3}<0,           \tag{521}
\end{aligned}
\]

because `A>18`.  Thus the paired quartic-cubic envelope also decreases.

Define the complete seam-majorant

\[
 \boxed{
 \mathcal U(x)
 :=pE+4qAC+3qB^2+qA^2(A^2-6dB).
 }                                                    \tag{522}
\]

Equations (505) and (517) give

\[
 D^4\log(1+r_2)\le\mathcal U(x),                 \tag{523}
\]

while (512), (514), (515), and (521) prove

\[
 \boxed{D\mathcal U(x)<0.}                       \tag{524}
\]

The primitive reserve (500) is also decreasing on this strip.  Direct
differentiation gives

\[
 \frac d{dx}V_1''''
 =16-\frac{96(8x^3+132x^2+198x+27)}{(2x-3)^5}<0,
                                                               \tag{525}
\]

the last inequality following already from `3<x<=7/2` after clearing the
positive denominator.  Consequently

\[
 V_1''''(x)\ge V_1''''(7/2)=\frac{1939}{8}.       \tag{526}
\]

The entire exact two-label theorem has therefore reduced to the single seam
estimate

\[
 \boxed{\mathcal U(\pi)<\frac{1939}{8}.}          \tag{527}
\]

Unlike a sampled endpoint test, (527) contains only rational functions of
`pi` and the single exponential `e^{-3pi}`.  Elementary rational bounds for
`pi` and the exponential decide it.  Once (527) is proved with reserve, the
`e^{-8x}` tail envelope (481) can be subtracted, and only the exponentially
thin all-label seam layer (490) remains.

## The seam endpoint has a strict rational reserve

The endpoint inequality (527) can be closed without decimal evaluation.  Use
the classical rational enclosure

\[
 \frac{333}{106}<\pi<\frac{355}{113}.             \tag{528}
\]

The functions `A` and `B` are increasing by (503), whereas `C` and `E` are
decreasing.  Substitution of the appropriate endpoint from (528) into their
rational formulas gives, by integer cross-multiplication,

\[
 \boxed{
 A(\pi)<\frac{2041}{100},\quad
 \frac{313}{10}<B(\pi)<\frac{3133}{100},\quad
 C(\pi)<\frac{567}{5},\quad
 E(\pi)<167.
 }                                                    \tag{529}
\]

For the Gibbs weight, the rational prefactor is decreasing and

\[
 4\frac{8\pi-3}{2\pi-3}
 <4\frac{8(333/106)-3}{2(333/106)-3}
 =\frac{782}{29}<\frac{2697}{100}.                \tag{530}
\]

The positive Taylor polynomial through degree `20` gives the exact lower
bound

\[
 e^{3\pi}>e^{999/106}
 >\sum_{k=0}^{20}\frac{(999/106)^k}{k!}>12372.    \tag{531}
\]

Therefore

\[
 p(\pi)<r_2(\pi)
 <\frac{2697}{100\cdot12372}
 =\frac{899}{412400}<\frac{109}{50000}.           \tag{532}
\]

To bound (522), use `q<p`, `d>1-2(109/50000)`, the upper bounds for positive
factors in (529), and the lower bound for the subtracted factor `B`.  This
gives

\[
 K(\pi)<
 \left(\frac{2041}{100}\right)^2
 -6\left(1-\frac{218}{50000}\right)\frac{313}{10}
 =\frac{57396727}{250000}.                        \tag{533}
\]

Consequently

\[
\begin{aligned}
 \mathcal U(\pi)
 <\frac{109}{50000}\Bigg[&167
 +4\frac{2041}{100}\frac{567}{5}
 +3\left(\frac{3133}{100}\right)^2\\
 &+\left(\frac{2041}{100}\right)^2
   \frac{57396727}{250000}\Bigg]
 =\frac{29432252144493483}{125000000000000}.     \tag{534}
\end{aligned}
\]

The comparison with (526) has the exact positive residual

\[
 \boxed{
 \frac{1939}{8}-\mathcal U(\pi)
 >\frac{864622855506517}{125000000000000}>0.
 }                                                    \tag{535}
\]

Equations (523)--(535) prove the strict two-label curvature theorem

\[
 \boxed{
 V_{\{1,2\}}''''(u)>0
 \qquad(0\le u\le u_*).
 }                                                    \tag{536}
\]

This is an analytic theorem, not a grid certificate: monotonicity transports
one exact rational seam estimate across the entire primitive-transition
strip.  The reserve in (535) is deliberately coarse and remains large enough
to absorb the explicit `n>=3` jet envelope outside the modular boundary
layer.  The sole unresolved point is now to make that absorption and the
all-label seam Taylor neighborhood overlap with declared constants.

## The complete modular tail fits inside the two-label reserve

Factor the full source relative to the two-label source:

\[
 \Phi=\phi_1(1+r_2)(1+S),
 \qquad
 S:=\frac{T_3}{1+r_2}.                            \tag{537}
\]

Then

\[
 V''''=V_{\{1,2\}}''''-D^4\log(1+S).             \tag{538}
\]

The constants in (481) admit very small integer majorants:

\[
 C_0<82,\quad C_1<730,\quad C_2<6562,\quad
 C_3<59050,\quad C_4<531442.                      \tag{539}
\]

Indeed, the `n=3` terms are respectively
`81,729,6561,59049,531441`, and the complete `n>=4` remainder is less than
one in every case.  This follows by splitting off `n=4`; successive terms
then lose at least `e^{-9pi}` while gaining only a fixed polynomial ratio.

The positive Taylor polynomial through degree `35`, together with (528),
gives

\[
 e^{8\pi}>e^{1332/53}
 >\sum_{k=0}^{35}\frac{(1332/53)^k}{k!}
 >80000000000.                                    \tag{540}
\]

Since `x^je^{-8x}` decreases for `x>=pi` and `0<=j<=4`, equations
(481), (539), and (540) imply

\[
 |D^jT_3|
 <\frac{2C_j}{80000000000}\left(\frac{176}{7}\right)^j
 =:\tau_j.                                       \tag{541}
\]

It remains only to account for the harmless denominator in (537).  Put
`g=(1+r_2)^{-1}=1-p`.  Direct differentiation of the logistic equation,
using `p<109/50000`, `A<23`, `B<38`, `C<114`, and `E<167`, yields

\[
 |D^jg|<m_j,\qquad
 (m_0,m_1,m_2,m_3,m_4)=\left(1,\frac1{20},2,33,910\right). \tag{542}
\]

Leibniz's rule therefore gives the explicit tail-quotient bounds

\[
 |D^jS|
 <\sigma_j:=\sum_{k=0}^j{j\choose k}\tau_km_{j-k}. \tag{543}
\]

For reference, integer cross-multiplication in (541)--(543) gives the coarse
upper bounds

\[
\begin{aligned}
 \sigma_0&<3\cdot10^{-9},&
 \sigma_1&<5\cdot10^{-7},\\
 \sigma_2&<2\cdot10^{-4},&
 \sigma_3&<\frac3{100},&
 \sigma_4&<\frac{5316}{1000}.                    \tag{544}
\end{aligned}
\]

The exact fourth logarithmic derivative is

\[
\begin{aligned}
 D^4\log(1+S)={}&\frac{D^4S}{1+S}
 -\frac{4(DS)(D^3S)+3(D^2S)^2}{(1+S)^2}\\
 &+\frac{12(DS)^2D^2S}{(1+S)^3}
 -\frac{6(DS)^4}{(1+S)^4}.                       \tag{545}
\end{aligned}
\]

Because `S>=0`, substitution of the unrounded rational values from
(541)--(543), followed by integer cross-multiplication, gives

\[
 \boxed{
 |D^4\log(1+S)|<\frac{1329}{250}=5.316.
 }                                                    \tag{546}
\]

Combining (535), (538), and (546) leaves the exact reserve

\[
\begin{aligned}
 V''''
 &>\frac{864622855506517}{125000000000000}
   -\frac{1329}{250}\\
 &=\frac{200122855506517}{125000000000000}
 >\frac85.                                        \tag{547}
\end{aligned}
\]

Thus the modular boundary layer is no longer unresolved at curvature order:

\[
 \boxed{
 V''''(u)>\frac85
 \qquad(0\le u\le u_*).
 }                                                    \tag{548}
\]

Since `V'''(0)=0`, integration proves

\[
 \boxed{
 V'''(u)>\frac85u>0
 \qquad(0<u\le u_*).
 }                                                    \tag{549}
\]

For `u>=u_*`, every individual label has `V_n'''>=0`; the aggregate still
contains the covariance and cubic terms in (462), so this fact alone does
not yet prove global `V'''>=0`.  What has closed is the only chamber where
the primitive label itself has the wrong curvature orientation.  The next
attack must control the aggregate mixture after all labelwise curvature
derivatives have become nonnegative, without silently discarding the
covariance term.

## After the crossover, the first tail label can only repair curvature

For the two-label system, the third logarithmic derivative has the exact
form

\[
 D^3\log(1+r_2)
 =-pC+3qAB-qdA^3
 =-pC-qA(dA^2-3B).                               \tag{550}
\]

On `x>=pi`, equations (496), (506), and `B<12x` give

\[
 dA^2-3B
 >\frac{199}{200}36x^2-36x
 =36x\left(\frac{199}{200}x-1\right)>0.          \tag{551}
\]

Hence

\[
 \boxed{D^3\log(1+r_2)<0.}                       \tag{552}
\]

Once `x>=x_*`, the primitive term itself satisfies `V_1'''>=0`.  Therefore

\[
 V_{\{1,2\}}'''
 =V_1'''-D^3\log(1+r_2)>0.                       \tag{553}
\]

More importantly, the repair has a uniform source-scaled lower bound.  Since
`r_2<1/400`,

\[
 q=\frac{r_2}{(1+r_2)^2}
 >\left(\frac{399}{400}\right)^2r_2,
 \qquad
 r_2>16e^{-3x}.                                  \tag{554}
\]

Also, for `x>3`,

\[
 dA^2-3B
 >\frac{3573}{50}x.                              \tag{555}
\]

Dropping the additional positive `pC` term in (550) gives

\[
 \boxed{
 -D^3\log(1+r_2)
 >6800x^2e^{-3x}.
 }                                                    \tag{556}
\]

The complete remaining tail is much smaller.  Continue to write
`S=T_3/(1+r_2)`.  On `x>=pi`, direct differentiation of `g=(1+r_2)^{-1}`
and the bounds `A<7x`, `B<4x^2`, `C<40x` give

\[
 |D^jg|<(8x)^j
 \qquad(0\le j\le3).                             \tag{557}
\]

Combining (481), (539), (543), and (557), then using

\[
 D^3\log(1+S)
 =\frac{D^3S}{1+S}
 -\frac{3(DS)(D^2S)}{(1+S)^2}
 +\frac{2(DS)^3}{(1+S)^3},                       \tag{558}
\]

gives the uniform analytic envelope

\[
 \boxed{
 |D^3\log(1+S)|
 <125000000x^3e^{-8x}.
 }                                                    \tag{559}
\]

The ratio of (559) to (556) is less than

\[
 18400xe^{-5x}.                                   \tag{560}
\]

This decreases for `x>=pi`.  Using `pi<22/7`, `pi>3`, and the positive
Taylor bound `e^{15}>3000000`,

\[
 18400xe^{-5x}
 <\frac{18400(22/7)}{3000000}<\frac1{50}.         \tag{561}
\]

Thus the omitted modular labels consume less than one fiftieth of the
two-label repair.  From (553), (556), and (559),

\[
 \boxed{
 V'''(u)>0
 \qquad(u_*\le u\le1/2).
 }                                                    \tag{562}
\]

Together with (549), this proves

\[
 \boxed{V'''(u)>0\qquad(0<u\le1/2).}              \tag{563}
\]

Finally, `Q'=uV'''` and `Q(0)=0` imply

\[
 Q(u)>0\qquad(0<u\le1/2),                        \tag{564}
\]

while (450) already proves `Q(u)>0` for `u>=1/2`.  Therefore outward score
stiffening is global:

\[
 \boxed{
 -u(\log\Phi)''(u)+(\log\Phi)'(u)>0
 \qquad(u>0).
 }                                                    \tag{565}
\]

By (431), the normalized Gaussian moment sequence `b_n` is strictly
log-concave.  Equivalently, every quadratic Jensen polynomial of the
completed theta source has real roots with the required orientation.  This
is the first complete infinite Jensen layer obtained here directly from the
theta labels and modular seam, without using any zeta zero.

Scope: (565) proves the degree-two Jensen family, not the higher-degree
Jensen hierarchy and not RH.  The next obstruction begins at degree three,
where pairwise ratio monotonicity is no longer enough and a genuinely
higher-order orientation law is required.

## Degree three is coherence between adjacent quadratic deficits

Let

\[
 \mathcal J_3^{(r)}(z)
 =\gamma_r+3\gamma_{r+1}z
  +3\gamma_{r+2}z^2+\gamma_{r+3}z^3.             \tag{566}
\]

For brevity put

\[
 a=\gamma_r,quad b=\gamma_{r+1},quad
 c=\gamma_{r+2},quad d=\gamma_{r+3}.             \tag{567}
\]

Its discriminant is

\[
 \Delta_3
 =162abcd-108ac^3+81b^2c^2-108db^3-27a^2d^2.   \tag{568}
\]

Introduce the two adjacent quadratic ratios

\[
 x=\frac{ac}{b^2},
 \qquad
 y=\frac{bd}{c^2}.                               \tag{569}
\]

The degree-two theorem gives `0<x,y<=1`.  Substitution in (568) removes all
moment scales:

\[
 \boxed{
 \frac{\Delta_3}{27b^2c^2}
 =3-4x-4y+6xy-x^2y^2.
 }                                                    \tag{570}
\]

Now write the quadratic deficits

\[
 u=1-x,
 \qquad v=1-y.                                    \tag{571}
\]

An exact factor rearrangement gives

\[
 \boxed{
 \frac{\Delta_3}{27b^2c^2}
 =uv(2u+2v-uv)-(u-v)^2.
 }                                                    \tag{572}
\]

Therefore the cubic Jensen polynomial is hyperbolic exactly when

\[
 \boxed{
 (u-v)^2\le uv(2u+2v-uv).
 }                                                    \tag{573}

This is the first genuinely coupled positivity law.  Degree two merely says
`u,v>=0`; degree three says their mismatch cannot exceed their joint reserve.
In particular, pairwise log-concavity alone is insufficient.  If `u=0` and
`v>0`, the right side of (573) vanishes while the left side does not.

The score-tilt meaning is exact.  Recall

\[
 \rho_n:=\frac{b_n}{b_{n-1}}
 =\frac1{\mathbb E_{Q_n}[W]},                    \tag{574}
\]

where `Q_n` is the `u^{2n}` tilt and `W=V'/u`.  Since the powers of two in
`gamma_n=2^{-n}b_n` cancel from cross-ratios,

\[
 x=\frac{\rho_{r+2}}{\rho_{r+1}},
 \qquad
 y=\frac{\rho_{r+3}}{\rho_{r+2}}.                \tag{575}
\]

Thus `u` and `v` measure two consecutive relative drops in the reciprocal
mean outward score.  The degree-three theorem sought from the source is not
another pointwise curvature sign.  It is the discrete transport law

\[
\boxed{
 \left(
 \frac{\rho_{r+2}}{\rho_{r+1}}
 -\frac{\rho_{r+3}}{\rho_{r+2}}
 \right)^2
 \le
 (1-x)(1-y)\{2(1-x)+2(1-y)-(1-x)(1-y)\}.
}                                                   \tag{576}
\]

This identifies what “higher-order orientation” means operationally: the
source-induced loss of Gaussian coercivity must vary slowly and coherently
between consecutive polynomial tilts.

The sharp hostile falsifier is now only two numbers.  Any positive even
source with increasing outward score but adjacent deficits violating (573)
shows that global score stiffening cannot by itself prove the cubic layer.
For theta, the next attack is to differentiate the tilt means in (574) and
seek a source-derived bound on the discrete curvature of `log rho_n` strong
enough to imply (573).

## Cubic deficits are normalized adjacent score covariances

Put

\[
 m_n:=\mathbb E_{Q_n}[W]=\rho_n^{-1}.             \tag{577}
\]

Since `Q_{n+1}` is obtained from `Q_n` by reweighting with `U^2`,

\[
 m_{n+1}
 =\frac{\mathbb E_{Q_n}[U^2W]}{\mathbb E_{Q_n}[U^2]}.
                                                               \tag{578}
\]

Consequently

\[
 m_{n+1}-m_n
 =\frac{\operatorname{Cov}_{Q_n}(U^2,W)}
        {\mathbb E_{Q_n}[U^2]}.                  \tag{579}
\]

The outward-score theorem says `W` is increasing, so (579) is strictly
positive.  More importantly, the deficits in (571) are exactly

\[
\boxed{
 u=rac{\operatorname{Cov}_{Q_{r+1}}(U^2,W)}
          {\mathbb E_{Q_{r+1}}[U^2],m_{r+2}},
 \qquad
 v=rac{\operatorname{Cov}_{Q_{r+2}}(U^2,W)}
          {\mathbb E_{Q_{r+2}}[U^2],m_{r+3}}.
}                                                   \tag{580}
\]

Thus degree two proves positivity of each normalized covariance separately;
degree three requires the adjacent covariance transports to fit inside the
cone (573).

A slightly stronger but simpler sufficient condition follows from
`0<=u,v<=1`:

\[
 2u+2v-uv\ge u+v.
\]

Hence

\[
 \boxed{
 (u-v)^2\le uv(u+v)
 \quad\Longrightarrow\quad
 \mathcal J_3^{(r)}\text{ is hyperbolic}.
 }                                                    \tag{581}
\]

Near the Gaussian boundary, where `u` and `v` are small, this exposes the
required scale sharply:

\[
 |u-v|=O\!\left((u+v)^{3/2}\right).               \tag{582}
\]

Ordinary comparability `u asymp v` is not enough.  Their consecutive change
must be one half-order smaller than their common size.  This explains why a
degree-two proof cannot be iterated mechanically.

The kernel

\[
 K(n,U)=U^{2n}                                    \tag{583}
\]

is totally positive in the ordered variables `n` and `log U`; it already
supplies the monotone-likelihood transport behind (579).  The missing theta
input is therefore a third-order compatibility between this TP kernel and
the particular score `W`.  A natural theorem-shaped target is:

\[
 \boxed{
 \text{the normalized covariance sequence in (580) obeys (581).}
 }                                                    \tag{584}
\]

Its falsifier is local in `r`: the first adjacent covariance pair outside
the cone.  Its proof, if true, should come from a signed `3x3` minor or a
three-copy transport of the theta current, not from separately sharpening
the two covariance inequalities.
