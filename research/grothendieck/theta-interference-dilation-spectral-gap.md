# Theta interference dilation spectral gap

Author: `marici.Grothendieck`

## 1. Origin

The first Gaussian--Bernstein gate contains the weighted inequality

\[
\int_0^\infty u^3\Phi''(u)^2\,du
\ge
3\int_0^\infty u\Phi'(u)^2\,du.
\]

This packet identifies its exact spectral meaning.

## 2. Logarithmic dilation coordinate

Put

\[
r=\log u,
\qquad
h(r)=-u\Phi'(u),
\qquad u=e^r.
\]

Since `du=u dr`,

\[
\boxed{
\int_0^\infty u\Phi'(u)^2\,du
=\int_{\mathbb R}h(r)^2\,dr.
}
\]

Moreover `Phi'=-h/u`, so

\[
\Phi''(u)=-\frac{h'(r)-h(r)}{u^2}.
\]

Therefore

\[
\boxed{
\int_0^\infty u^3\Phi''(u)^2\,du
=\int_{\mathbb R}(h'(r)-h(r))^2\,dr.
}
\]

The source decay at both logarithmic ends makes the cross term vanish:

\[
\int_{\mathbb R}h'h\,dr=0.
\]

Hence the weighted gap is exactly

\[
\boxed{
\int_{\mathbb R}|h'(r)|^2\,dr
\ge2\int_{\mathbb R}|h(r)|^2\,dr.
}
\]

The mysterious constant three has separated into the universal `+1` from
the logarithmic Jacobian and a genuine dilation-frequency floor `2`.

## 3. Mellin spectral interpretation

Let

\[
\widehat h(k)=\int_{\mathbb R}h(r)e^{-ikr}\,dr.
\]

Plancherel turns the gap into

\[
\boxed{
\frac{\int_{\mathbb R}k^2|\widehat h(k)|^2\,dk}
{\int_{\mathbb R}|\widehat h(k)|^2\,dk}
\ge2.
}
\]

Thus the first global interference gate says:

\[
\boxed{
\text{the dilation spectrum of the completed theta score has mean-square
frequency at least two.}
}
\]

This is not an assertion about zero locations. It is a source bandwidth
theorem before the final Fourier readout.

## 4. Gaussian calibration

For

\[
\Phi_a(u)=e^{-au^2},
\]

the logarithmic score is

\[
h_a(r)=2a e^{2r}e^{-ae^{2r}}.
\]

Translation `r -> r+(1/2)log(a)` changes the Gaussian scale but not its
frequency distribution. Direct gamma integration gives

\[
\frac{\int|h_a'|^2}{\int|h_a|^2}=2.
\]

Every Gaussian scale saturates the dilation-frequency floor. Theta must have
at least the Gaussian bandwidth.

## 5. Arithmetic meaning

The individual theta labels are additive translates in the source coordinate:

\[
\phi_n(u)=n^{-1/2}\phi_1(u+\log n).
\]

But the spectral coordinate above is `r=log u`. Hence prime transport acts as

\[
r\longmapsto\log(e^r+\log n),
\]

not as translation in `r`. It does **not** become multiplication by the phase
`exp(ik log n)` in the Mellin spectrum of `h`.

This is a crucial typing distinction:

\[
\boxed{
\text{Euler transport is additive in }u,
\qquad
\text{the gap is spectral under dilation of }u.
}
\]

Therefore all-prime rigidity does not automatically imply the bandwidth
bound. The missing bridge must convert the affine prime shifts into control
of the dilation generator `u d/du`, including the finite lower-end
sewing caused by the half-line.

This links the two active structures:

\[
\text{all-prime Euler coherence}
\quad\xrightarrow{\text{missing affine--dilation bridge}}\quad
\text{dilation spectral bandwidth}
\quad\longrightarrow\quad
\text{first interference gate}.
\]

The middle arrow is the live theorem.

## 6. Exact affine--dilation commutator

Let

\[
Af(u)=u\partial_uf(u)
\]

be the dilation generator and let

\[
S_af(u)=c_a f(u+a)
\]

be any source translation with constant normalization `c_a`. Direct
differentiation gives

\[
AS_af(u)=c_a u f'(u+a),
\]

whereas

\[
S_aAf(u)=c_a(u+a)f'(u+a).
\]

Hence

\[
\boxed{
[A,S_a]=-aS_a\partial_u.
}
\]

For a prime label, `a=log p` and `c_a=p^(-1/2)`. The failure of additive
prime transport to commute with dilation is therefore a completely typed
arithmetic shear, linear in `log p`.

Since

\[
h=-A\Phi,
\]

the bandwidth numerator and denominator are

\[
\|Ah\|_{L^2(du/u)}^2
=\|A^2\Phi\|_{L^2(du/u)}^2,
\]

and

\[
\|h\|_{L^2(du/u)}^2
=\|A\Phi\|_{L^2(du/u)}^2.
\]

Substitution of the Euler packet generates diagonal translated energies plus
cross-label shear terms from the commutator. The individual translation is
not unitary in `L^2(du/u)` because it moves the half-line boundary. Therefore
neither diagonal label bandwidth nor a phase-only argument is faithful.

The exact live statement is

\[
\boxed{
\|A^2\Phi\|_{du/u}^2-2\|A\Phi\|_{du/u}^2\ge0,
}
\]

with `Phi=prod_p(I-S_p)^(-1)phi_1` and every commutator and boundary current
retained. This is the positive-commutator form of the first global
interference gate.

## 7. Smallest shear falsifier

For any proposed termwise Euler proof, the smallest exact test is a two-label
packet

\[
f+S_af.
\]

Expanding the quadratic form

\[
\mathcal Q(g)=\|A^2g\|^2-2\|Ag\|^2
\]

gives

\[
\mathcal Q(f+S_af)
=\mathcal Q(f)+\mathcal Q(S_af)
+2\mathcal Q(f,S_af).
\]

The mixed polarization `mathcal Q(f,S_af)` contains the entire affine--
dilation interference. If it is negative beyond the diagonal reserve for one
source-derived shift, diagonal Euler positivity is falsified. If all such
mixed terms assemble positively only after modular completion, that assembly
is the required arithmetic theorem.

## 8. Gaussian ground-state completion

The bandwidth form has a second exact reduction. For `a>0`, define the
Gaussian logarithmic-score profile

\[
W_a(r)=2-2ae^{2r}=2-2au^2.
\]

For an arbitrary score `h`, put

\[
\mathcal I_a(h)=
\int_{\mathbb R}|h'(r)-W_a(r)h(r)|^2\,dr\ge0.
\]

Let

\[
M_j=\int_{\mathbb R}e^{2jr}h(r)^2\,dr
=\int_0^\infty u^{2j+1}\Phi'(u)^2\,du.
\]

Integration of the cross term gives the identity

\[
\boxed{
\int|h'|^2-2M_0
=\mathcal I_a(h)-6M_0+12aM_1-4a^2M_2.
}
\]

The right side is optimized at

\[
a_*=\frac{3M_1}{2M_2},
\]

where

\[
\boxed{
\int|h'|^2-2M_0
=\mathcal I_{a_*}(h)
-6M_0+9\frac{M_1^2}{M_2}.
}
\]

Consequently the Gaussian-sharp moment concentration

\[
\boxed{
M_1^2\ge\frac23M_0M_2
}
\]

is sufficient for the dilation spectral gap. In the original source
coordinate this is

\[
\boxed{
\left(\int_0^\infty u^3\Phi'(u)^2\,du\right)^2
\ge\frac23
\left(\int_0^\infty u\Phi'(u)^2\,du\right)
\left(\int_0^\infty u^5\Phi'(u)^2\,du\right).
}
\]

## 9. Probabilistic meaning

Normalize the score-energy measure

\[
d\rho(u)=\frac{u\Phi'(u)^2\,du}{M_0}
\]

and put `R=u^2`. The sufficient condition becomes

\[
\boxed{
\frac{\mathbb E_\rho[R^2]}{\mathbb E_\rho[R]^2}
\le\frac32.
}
\]

Equivalently,

\[
\operatorname{Var}_\rho(R)
\le\frac12\mathbb E_\rho[R]^2.
\]

Thus theta's score-energy radius must be no more dispersed than the gamma
shape-two carrier. For a Gaussian source, `R` under `rho` is exactly gamma of
shape two; the dispersion inequality and the square
`mathcal I_(a_*)` both saturate simultaneously.

This is a hard-to-vary sufficient explanation:

\[
\text{Gaussian-relative radial concentration}
\quad+\quad
\text{nonnegative ground-state square}
\quad\Longrightarrow\quad
\text{dilation bandwidth at least two}.
\]

The concentration inequality is stronger than ordinary moment log-convexity,
which points in the opposite direction and supplies only an upper bound on
`M_1^2/(M_0M_2)`. It must be proved from source concentration, not from the
moment axioms alone.

## 10. Convex-power concentration calibration

For `Phi_p(u)=exp(-u^(2p))`, the score-energy measure is proportional to

\[
u^{4p-1}e^{-2u^{2p}}\,du.
\]

Thus

\[
X=u^{2p}\sim\operatorname{Gamma}(2,2)
\]

under the normalized measure `rho`. Since `R=u^2=X^(1/p)`,

\[
\boxed{
\frac{\mathbb E_\rho[R^2]}{\mathbb E_\rho[R]^2}
=\frac{\Gamma(2+2/p)}{\Gamma(2+1/p)^2}.
}
\]

Put `q=1/p`. The logarithmic derivative of this ratio is

\[
2\psi(2+2q)-2\psi(2+q)>0.
\]

Hence the ratio increases with `q` on `(0,1]` and is maximized at the
Gaussian endpoint `q=1`, where it equals

\[
\frac{\Gamma(4)}{\Gamma(3)^2}=\frac32.
\]

Every stiffer convex power therefore satisfies the Gaussian-relative
concentration condition. Combined with the earlier local calculation, this
shows:

\[
\boxed{
\text{convex powers pass the global ground-state gate, while }p\ge2
\text{ fail the local fourth-curvature gate.}
}
\]

The two halves of the first interference theorem are complementary rather
than redundant.

## 11. Score-energy density in the squared radius

Put

\[
x=u^2.
\]

Since `u du=dx/2`, the score-energy measure becomes

\[
d\rho(x)\propto\Phi'(\sqrt x)^2\,dx.
\]

Evenness gives `Phi'(sqrt x)^2 = x w(x)`, where

\[
\boxed{
w(x)=\left(
\frac{-\Phi'(\sqrt x)}{\sqrt x}
\right)^2.
}
\]

Thus the required gamma-shape-two concentration is exactly a moment theorem
for a density of the form `x w(x)`.

## 12. Log-concave base implies the sharp moment ratio

Let

\[
m_j=\int_0^\infty x^jw(x)\,dx.
\]

Under the normalized density `xw(x)`,

\[
\mathbb E[R]=\frac{m_2}{m_1},
\qquad
\mathbb E[R^2]=\frac{m_3}{m_1}.
\]

For a nonnegative log-concave function on the half-line, the normalized
moments

\[
\frac{m_j}{\Gamma(j+1)}
\]

form a log-concave sequence. At indices `1,2,3`, this gives

\[
\left(\frac{m_2}{2!}\right)^2
\ge
\frac{m_1}{1!}\frac{m_3}{3!}.
\]

Equivalently,

\[
\boxed{
\frac{m_1m_3}{m_2^2}\le\frac32.
}
\]

Therefore:

\[
\boxed{
w\text{ log-concave on }[0,\infty)
\quad\Longrightarrow\quad
\int u^3\Phi''^2\ge3\int u\Phi'^2.
}
\]

This produces the exact constant three through the factorial ratio
`3!/(2!)^2`, rather than through an estimated Poincare constant.

## 13. Reduction to a radial-score theorem

Let

\[
W(u)=\frac{V'(u)}u,
\qquad V=-\log\Phi.
\]

Then

\[
\frac{-\Phi'(u)}u=\Phi(u)W(u),
\]

so

\[
\log w(x)
=2\log\Phi(\sqrt x)+2\log W(\sqrt x).
\]

The first term is already radially concave. Indeed

\[
\frac{d^2}{dx^2}\log\Phi(\sqrt x)
=\frac{u(\log\Phi)''(u)-(\log\Phi)'(u)}{4u^3}
=-\frac{Q(u)}{4u^3}<0,
\]

where

\[
Q(u)=uV''(u)-V'(u)>0
\]

is the proved quadratic curvature theorem.

Thus a clean sufficient source theorem is radial log-concavity of `W`:

\[
\boxed{
\frac{d^2}{dx^2}\log W(\sqrt x)\le0.
}
\]

Writing `W'=Q/u^2`, this condition is exactly

\[
\boxed{
uV'(u)Q'(u)
\le3V'(u)Q(u)+Q(u)^2.
}
\]

Since `Q'=uV'''`, it is a coupled third-curvature inequality using only the
already-typed source quantities `(V',Q,Q')`.

Equivalently, define the dimensionless stiffening elasticity

\[
\mathcal E(u)=\frac{uW'(u)}{W(u)}=\frac{Q(u)}{V'(u)}.
\]

Then radial log-concavity of `W` is

\[
\boxed{
u\mathcal E'(u)\le2\mathcal E(u).
}
\]

Thus the source may stiffen outward, as already proved, but its relative
stiffening may not accelerate faster than quadratically in the radial scale.

The global interference chain is now

\[
\boxed{
\text{radial log-concavity of }W
\Longrightarrow
\text{log-concavity of }w
\Longrightarrow
\text{gamma-shape-two concentration}
\Longrightarrow
\text{dilation spectral gap}.
}
\]

The first arrow is sufficient, not asserted necessary. Its sharp falsifier is
one `u>0` where

\[
uV'Q'>3V'Q+Q^2.
\]

## 14. Modular-seam sixth-jet gate

Write the even potential expansion

\[
V(u)=V(0)
+\frac{v_2}{2}u^2
+\frac{v_4}{24}u^4
+\frac{v_6}{720}u^6
+O(u^8),
\]

where `v_(2j)=V^(2j)(0)` and the proved source curvature gives `v_2>0` and
`v_4>0`.

The radial score has expansion

\[
W(u)=\frac{V'(u)}u
=v_2+\frac{v_4}{6}u^2+\frac{v_6}{120}u^4+O(u^6).
\]

Therefore, in `x=u^2`,

\[
\left.\frac{d^2}{dx^2}\log W(\sqrt x)\right|_{x=0}
=\frac{v_6}{60v_2}-\frac{v_4^2}{36v_2^2}.
\]

The radial-score theorem leaves the modular seam in the correct direction if
and only if

\[
\boxed{
3v_2v_6\le5v_4^2.
}
\]

Equivalently, the first nonlinear coefficient of the elasticity condition
`u E'<=2E` has the required sign. This is the smallest local
falsifier for the global concentration mechanism: one exact sixth-jet
violation kills radial log-concavity immediately.

## 15. Far-tail orientation is automatic

In the primitive far chamber, `x_1=pi exp(2u)` and the first theta label gives

\[
V_1'(u)
=2x_1-\frac52-\frac{4x_1}{2x_1-3}.
\]

Consequently

\[
\log\frac{V_1'(u)}u
=2u-\log u+\log(2\pi)+O(e^{-2u}).
\]

Writing `r=u^2`, the leading radial curvature is

\[
\frac{d^2}{dr^2}\left(2\sqrt r-\frac12\log r\right)
=\frac{1-\sqrt r}{2r^2}<0
\qquad(u>1).
\]

All higher-label corrections are super-exponentially small relative to the
primitive label. Hence radial log-concavity of `W` is eventual; a directed
tail envelope can turn this asymptotic statement into an explicit threshold.

The remaining theorem is compact:

1. prove the sixth-jet seam gate;
2. propagate its sign through the primitive crossover;
3. join it to the automatic far-tail orientation.

No oscillatory variable remains in this sufficient global route.

## 16. Exact spectral falsifier

The gap fails precisely when

\[
\int(k^2-2)|\widehat h(k)|^2\,dk<0.
\]

Thus any candidate arithmetic argument can be rejected by exhibiting excess
completed score energy in the band `|k|<sqrt(2)` that is not compensated by
the outer Mellin frequencies.

A finite sample of frequencies cannot prove the theorem. An admissible proof
must give either:

1. a source-derived spectral factor with a zero of sufficient order in the
   low-frequency band;
2. a positive commutator for the dilation generator;
3. an exact Euler-product identity bounding the low-frequency mass; or
4. a canonical orthogonality removing the dangerous low mode.

## 17. Scope

The logarithmic transformation and spectral equivalence are exact. The
bandwidth inequality has not yet been proved for the completed theta source,
and RH is not proved.

## 18. The compact obstruction is monotone elasticity density

Put `P=V'`.  The denominator-free numerator of radial log-concavity is

\[
\begin{aligned}
\mathcal R_W(u)
&=3P(u)Q(u)+Q(u)^2-uP(u)Q'(u)\\
&=u^2\bigl(P'(u)^2-P(u)P''(u)\bigr)
  +uP(u)P'(u)-2P(u)^2.
\end{aligned}
\]

Indeed the exact curvature identity is

\[
\boxed{
\frac{d^2}{dx^2}\log W(\sqrt x)
=-\frac{\mathcal R_W(u)}{4u^4P(u)^2},
\qquad x=u^2.
}
\]

Thus no division is needed in a source-level proof: it is enough to establish
`R_W(u)>=0` for `u>0`.

There is an even sharper first-order formulation.  Define the normalized
elasticity density

\[
J(u)=\frac{\mathcal E(u)}{u^2}
=\frac{uV''(u)-V'(u)}{u^2V'(u)}.
\]

Then

\[
\boxed{
\mathcal R_W(u)\ge0
\quad\Longleftrightarrow\quad
J'(u)\le0.
}
\]

The seam and the primitive tail have compatible endpoint data.  The jet
expansion gives

\[
J(0^+)=\frac{v_4}{3v_2},
\]

while the primitive asymptotic gives

\[
J(u)=\frac2u+O(u^{-2})
\qquad(u\longrightarrow\infty).
\]

The sixth-jet inequality is exactly `J'(0^+)<=0` in the radial variable;
eventual radial log-concavity is exactly eventual decrease of `J`.  Hence the
previously described compact crossover problem has one intrinsic statement:

\[
\boxed{
\frac{uV''(u)-V'(u)}{u^2V'(u)}
\text{ decreases from the modular seam to the primitive tail.}
}
\]

This formulation suggests the right arithmetic attack.  One should not try
to bound `V'''` independently.  Such bounds discard the correlation forced
by a single completed theta source.  Instead, expand `R_W` after clearing the
common positive theta denominator and seek a four-label, or pair-pair,
polarization whose off-diagonal terms are oriented by reciprocal-scale
sewing.  A negative
coefficient in that exact polarization would finitely falsify this route;
a nonnegative polarization would close the concentration lemma and therefore
the first interference gate.
