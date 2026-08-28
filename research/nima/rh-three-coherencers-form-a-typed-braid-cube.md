# The Three RH Coherencers Form a Typed Braid Cube

## Question

What categorical object compares the reciprocal, adelic, and boundary
coherencers without reducing any of them to the completed scalar section?

## Claim boundary

Let the three partial constructors be:

- $F$, reciprocal Fourier comparison;
- $A$, finite-to-archimedean valuation comparison and restricted-product
  completion;
- $G$, moving-endpoint Green construction and boundary Schur incidence.

These are not assumed to be total endofunctors. Each composite below is
defined only on the common source domain on which all intermediate traces,
boundary values, and completions exist.

Suppose the source supplies pairwise comparison cells

\[
\alpha:AF\Rightarrow FA,
\qquad
\beta:GF\Rightarrow FG,
\qquad
\gamma:GA\Rightarrow AG.
\]

There are then two typed routes from $GAF$ to $FAG$:

\[
GAF
\xRightarrow{G\alpha}
GFA
\xRightarrow{\beta A}
FGA
\xRightarrow{F\gamma}
FAG,
\]

and

\[
GAF
\xRightarrow{\gamma F}
AGF
\xRightarrow{A\beta}
AFG
\xRightarrow{\alpha G}
FAG.
\]

The required higher coherencer is a modification comparing the two composite
cells. In an additive realization its residual is

\[
\mathfrak U=
(F\gamma)\circ(\beta A)\circ(G\alpha)
-(\alpha G)\circ(A\beta)\circ(\gamma F).
\]

Pairwise commutative faces do not imply $\mathfrak U=0$. This is the same
logical gap as a system with valid swap diamonds but a nonzero braid
residual. The RH application must derive the comparison from the labelled
theta/Tate source; it cannot declare the modification from equality of scalar
outputs.

## Current face audit

### Reciprocal--adelic face

The normalized local response

\[
\rho_q(s)=\frac{q^s-q^{1-s}}{1-q}
\]

is odd under $s\leftrightarrow1-s$, and its algebraic degeneration is

\[
\lim_{q\to1}\rho_q(s)=1-2s.
\]

This supplies a source-derived local candidate for $\alpha$. It fixes the
relative normalization and orientation of finite and infinite response
columns. It does not yet prove compatibility with restricted-product
completion.

### Reciprocal--Green face

For one labelled moving endpoint, the reciprocal tails give

\[
m=\frac{T_++T_-}{2},
\qquad
n=\frac{T_+-T_-}{2},
\]

and satisfy

\[
\partial_xm=-\frac12m-zn-f,
\qquad
\partial_xn=-zm-\frac12n.
\]

The same endpoint current $f$ occurs in both channels. Reciprocal exchange
preserves the symmetric forcing and reverses the antisymmetric coordinate.
This supplies the local source content of (eta). It has not yet been
transported through the completed Green domain.

### Adelic--Green face

No source-derived comparison cell $\gamma$ currently exists. The missing
map must take the finite and archimedean response columns into the actual
Green boundary packet, including its seam component, endpoint lift, graph
norm, and Schur blocks $B,C,E$. Equality after Mellin summation or scalar
determinant evaluation does not construct this cell.

Therefore the braid cube is presently open on one face. The higher residual
$\mathfrak U$ is not yet a computable RH invariant. Declaring it zero would
hide the missing adelic-to-boundary incidence inside a fitted coherencer.

## Finite DPC

At a finite labelled cutoff $X$, construct source matrices

\[
F_X,qquad A_X,qquad G_X
\]

and the three pairwise comparison cells on one declared common domain. Then
compute

\[
\mathfrak U_X=
(F_X\gamma_X)(\beta_XA_X)(G_X\alpha_X)
-(\alpha_XG_X)(A_X\beta_X)(\gamma_XF_X).
\]

The test must be performed on the labelled odd source directions, not only on
the scalar determinant. Three verdicts are admitted:

1. $\mathfrak U_X\ne0$: the proposed higher coherencer fails at finite
   source level.
2. $\mathfrak U_X=0$ for every cutoff, but the residual reappears under
   completion: the obstruction is a genuine asymptotic completion class.
3. The cells extend and $\mathfrak U=0$: the three constructions form one
   coherent source object, after which zero confinement remains a separate
   boundary nondegeneracy question.

The smallest hostile witness is a deformation that preserves all three
scalar projections and every pairwise comparison while changing one
labelled endpoint current or one boundary incidence row. Such a witness has
zero scalar image and nonzero $\mathfrak U_X$.

## Disposition

Progressive typing result, not an RH theorem. The required object is a
higher comparison cell over a typed braid cube, rather than a fourth scalar
observer. Two local faces now have source-derived candidates. The
adelic--Green face is missing, so the higher cell cannot yet be asserted or
tested globally.

The immediate construction target is the map from the normalized valuation
response family into the moving-endpoint Green boundary packet. It must carry
the common endpoint current, not merely reproduce the completed scalar
section.

## The homogeneous adelic--Green face is exact

Let

\[
a=\frac12+z,
\qquad
b=\frac12-z,
\qquad
D_\ell(z)=
\begin{pmatrix}
e^{-a\ell}&0\\
0&e^{-b\ell}
\end{pmatrix}.
\]

This is the homogeneous transport of the two moving-endpoint Green channels
over a logarithmic interval of length $\ell$. Apply its normalized odd
codiagonal to the common source vector:

\[
\frac{(1,-1)}{1-e^{-\ell}}
D_\ell(z)
\begin{pmatrix}1\\1\end{pmatrix}
=
\frac{e^{-(1/2+z)\ell}-e^{-(1/2-z)\ell}}
{1-e^{-\ell}}
=
-\frac{\sinh(\ell z)}{\sinh(\ell/2)}.
\]

For $\ell=\log p$, the right side is exactly the normalized finite-place
odd response. Its degeneration at $\ell=0$ is the archimedean response:

\[
\lim_{\ell\to0}
\frac{(1,-1)D_\ell(z)(1,1)^T}{1-e^{-\ell}}
=-2z.
\]

Thus the valuation response is not merely analogous to the Green transport.
It is a source-normalized boundary readout of its homogeneous two-channel
propagator. This constructs the adelic--Green comparison on the homogeneous
rank-two carrier.

## The forcing requires an affine lift

The actual labelled tails are not homogeneous. Put

\[
\mathbf T(x)=
\begin{pmatrix}T_+(x)\\T_-(x)\end{pmatrix},
\qquad
\mathbf 1=
\begin{pmatrix}1\\1\end{pmatrix}.
\]

Their exact interval transport is

\[
\mathbf T(x+\ell)
=D_\ell\mathbf T(x)-\mathbf r_f(x,\ell),
\]

where

\[
\mathbf r_f(x,\ell)
=\int_0^\ell D_{\ell-u}\mathbf 1 f(x+u)\,du.
\]

The forcing reservoir obeys the cocycle law

\[
\mathbf r_f(x,\ell_1+\ell_2)
=D_{\ell_2}\mathbf r_f(x,\ell_1)
+\mathbf r_f(x+\ell_1,\ell_2).
\]

Consequently the affine matrices

\[
\widehat D_f(x,\ell)=
\begin{pmatrix}
D_\ell&-\mathbf r_f(x,\ell)\\
0&1
\end{pmatrix}
\]

compose exactly under interval subdivision. For two prime lengths
$\ell_p=\log p$ and $\ell_q=\log q$, the two subdivisions give the identity

\[
D_{\ell_q}\mathbf r_f(x,\ell_p)
+\mathbf r_f(x+\ell_p,\ell_q)
=
D_{\ell_p}\mathbf r_f(x,\ell_q)
+\mathbf r_f(x+\ell_q,\ell_p).
\]

This is a source-derived finite coherence diamond. Its extra coordinate is
the common endpoint forcing reservoir. Removing that coordinate leaves the
correct local response symbol but destroys composition of the full Green
transport.

## Revised frontier

The adelic--Green face is no longer wholly missing. It is exact on the
homogeneous two-channel carrier and has a canonical affine lift on every
finite moving-endpoint interval. What remains unconstructed is its descent to
the arithmetic sampling module and its extension through restricted-product
completion into the full seam and Schur boundary object.

The higher cube should therefore be tested first on the affine three-port
carrier. If its braid residual vanishes there, any later residual is localized
to sampling, arithmetic aggregation, or completion rather than to local
reciprocal transport.

## Descent to the labelled divisibility category

Let the objects be positive integers and let a prime-labelled generating arrow
be

\[
n\xrightarrow{p}np.
\]

Set $x=\log n$ and $\ell_p=\log p$. Assign to this arrow the affine Green
transport

\[
\mathcal T_{n,p}=\widehat D_f(\log n,\log p).
\]

For two primes, the forcing cocycle gives

\[
\mathcal T_{np,q}\mathcal T_{n,p}
=
\widehat D_f(\log n,\log p+\log q)
=
\mathcal T_{nq,p}\mathcal T_{n,q}.
\]

Therefore arithmetic sampling itself creates no braid residual. The affine
transport descends to a functor from the prime-generated divisibility category
into affine two-channel Green transports at every finite label.

This descent is coherent but not faithful on factorization paths. The two
orders through $npq$ have the same affine image. Moreover, if arbitrary
composite-labelled arrows were admitted, the map for one step labelled $pq$
would equal the composite of the $p$ and $q$ steps. The analytic transport
cannot decide whether that composite edge was primitive.

Prime typing must consequently remain in the source category. Unique
factorization determines the admitted generating arrows and their powers;
the affine Green functor transports them but does not reconstruct their types
from its image. This reproduces the earlier type-erasure boundary in a more
exact form:

- the Green image preserves coherent arithmetic action;
- the source labels preserve which actions are primitive;
- neither component can replace the other.

The remaining obstruction is now downstream of finite arithmetic sampling.
It can enter when the labelled direct sum is aggregated, when the forcing
reservoir is compressed, or when the finite functor is completed. A finite
prime-order residual is no longer available as the missing RH mechanism.

## The affine port reproduces the coefficients behind the Schatten-three boundary

For the translated theta atom used by the moving-endpoint construction,

\[
\rho_1(x)=2e^{x/2}e^{-\pi e^{2x}},
\]

the common forcing simplifies to

\[
f(x)=e^{-x/2}\rho_1(x)=2e^{-\pi e^{2x}}.
\]

At the central parameter $z=0$, both Green rates equal $1/2$. On the prime
step from $1$ to $p$, either component of the forcing reservoir is

\[
R_p
=p^{-1/2}
\int_0^{\log p}e^{u/2}f(u)\,du.
\]

The integral converges monotonically to the finite positive constant

\[
C_infty
=2\int_0^\infty e^{u/2}e^{-\pi e^{2u}}\,du.
\]

Consequently

\[
R_p\sim C_\infty p^{-1/2}.
\]

For a prime-power interval of length $k\log p$, the same calculation gives

\[
R_{p^k}\sim C_\infty p^{-k/2}
\]

as $p$ increases with $k$ fixed. The three completion levels follow:

- $k=1$: the prime reservoir is not square summable;
- $k=2$: the square reservoir is square summable but not absolutely
  summable;
- $k\ge3$: the remaining reservoir is absolutely summable.

Thus the affine coherencer port independently reproduces the coefficient
summability thresholds encountered in the local Tate sewing. If these
coefficients are realized as singular values of a diagonal prime-edge
operator, they give the corresponding Schatten-three filtration. The present
calculation does not itself construct that operator or prove that the Green
synthesis has those singular values.

The coefficient hierarchy is not an external regularization convention. It
is present in the source-derived Duhamel coordinate required for
compositional Green transport.

## Ordinary determinants erase the coherencer port

The affine lift is triangular, so

\[
\det\widehat D_f(x,\ell)
=\det D_\ell
=e^{-\ell}.
\]

Its determinant is independent of $z$ and of the forcing reservoir. Hence the
third port is essential for composition and carries the completion anomaly,
while the ordinary determinant of the local affine transport cannot see its
coefficient-level completion obstruction.

This identifies the remaining required constructor more precisely. The seam
or Schur boundary object must couple the forcing coordinate back into the
characteristic readout. A triangular affine augmentation alone has no divisor
and cannot confine zeros. Conversely, deleting the forcing coordinate before
completion destroys exactly the primitive and square currents that obstruct
that deletion.

The candidate higher coherencer is therefore not the affine port by itself.
It is the still-missing incidence from that port into the completed boundary
Schur system.

## Determinant visibility requires a return incidence

The minimum nontriangular extension has the block form

\[
M=
\begin{pmatrix}
D&-\mathbf r\\
\mathbf c^T&e
\end{pmatrix}.
\]

Because $D$ is invertible at every finite local step, Schur reduction gives

\[
\det M
=
\det D
\left(e+\mathbf c^TD^{-1}\mathbf r\right).
\]

The affine forcing port becomes determinant-visible only through the closed
pairing

\[
\mathbf c^TD^{-1}\mathbf r.
\]

The existing affine construction supplies the outgoing column
$-\mathbf r$. It does not supply the return row $\mathbf c^T$. Therefore the
minimum missing datum is not another state coordinate; it is a source-derived
return incidence from the boundary port into the two Green channels.

## Reciprocal covariance does not select the return map

Let

\[
S=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

The local data obey

\[
D(-z)=SD(z)S,
\qquad
\mathbf r(-z)=S\mathbf r(z).
\]

Reciprocal covariance of the completed block requires only

\[
\mathbf c(-z)=S\mathbf c(z).
\]

It admits the entire family

\[
\mathbf c_\kappa(z)=\kappa\mathbf r(z),
\qquad
\kappa\in\mathbb C.
\]

Every member has the same reciprocal typing, but its Schur readout is

\[
e+\kappa\mathbf r^TD^{-1}\mathbf r.
\]

The case $\kappa=0$ is determinant-blind. Nonzero values change the
characteristic section whenever the quadratic response is nonzero. Thus
reciprocity, finite affine coherence, and determinant normalization leave a
free complex return gain. They cannot orient or normalize the missing
incidence.

This is the finite falsifier for any claim that the higher coherencer follows
from symmetry alone: compare two values of $\kappa$. They preserve every
currently derived local transport and reciprocal relation while changing the
Schur characteristic readout.

The next source question is now singular. Which theta/Tate boundary operation
constructs $\mathbf c$ and fixes its normalization relative to
$\mathbf r$? Without that operation, the completed determinant connection is
underdetermined by one return-incidence family.

## A metric law fixes the return row only relative to the metric

There is a precise conditional compiler for the proposed relationship energy.
At a fixed real slice, regard the coupled block as a boundary generator

\[
K=
\begin{pmatrix}
A&-\mathbf r\\
\mathbf c^T&e
\end{pmatrix}
\]

with positive metric

\[
H=
\begin{pmatrix}
G&0\\
0&h
\end{pmatrix},
\qquad
G>0,
\qquad
h>0.
\]

If the source supplies the conservation law

\[
K^TH=HK,
\]

then its off-diagonal block forces

\[
h\mathbf c=-G\mathbf r,
\qquad
\mathbf c=-h^{-1}G\mathbf r.
\]

The diagonal block separately requires $A^TG=GA$. The return-row conclusion
uses only the off-diagonal block; existence of the complete conservation law
also requires this metric compatibility of the bulk generator.

The skew form of the conservation law reverses the sign but has the same
typing consequence. Once $G$, $h$, and the conservation convention are fixed,
the return incidence is no longer free.

This is only a conditional result. It does not prove that the analytic Schur
block is a self-adjoint boundary generator, nor does it construct its metric.
Those are additional source obligations.

## Positivity and reciprocity still leave metric moduli

Reciprocal invariance requires

\[
S^TGS=G.
\]

For a real symmetric two-channel metric, the general solution is

\[
G=
\begin{pmatrix}
g&u\\
u&g
\end{pmatrix},
\qquad
g>|u|.
\]

The boundary weight $h$ is also positive and otherwise free. Hence positive
reciprocal metrics determine a family of return rows, not one row. Even in the
scalar subfamily $G=gI$, the effective return gain is proportional to $g/h$.

On the central scalar bulk $A=a_0I$, the smallest hostile pair is

\[
(G,h)=(I,1),
\qquad
(G,h)=(2I,1).
\]

Both are positive and reciprocal. Each makes its associated central generator
metric-self-adjoint, but they produce respectively

\[
\mathbf c=-\mathbf r,
\qquad
\mathbf c=-2\mathbf r,
\]

and therefore different Schur characteristic sections.

Relationship energy can close the return-incidence problem only if the source
fixes the relative normalization of the Green-channel metric and the boundary
metric. Positivity of an unspecified metric merely reparameterizes the free
gain.

The frontier is consequently the construction of one common theta/Tate energy
object whose restrictions yield both $G$ and $h$. Importing a convenient
Hilbert norm after the fact would fit the missing coherencer rather than derive
it.

## The native tail metric is Lorentzian, not positive

The moving-endpoint system in symmetric and antisymmetric coordinates is

\[
\partial_x
\begin{pmatrix}m\\n\end{pmatrix}
=
\left(
-\frac12I-z\sigma_x
\right)
\begin{pmatrix}m\\n\end{pmatrix}
-f
\begin{pmatrix}1\\0\end{pmatrix},
\qquad
\sigma_x=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Remove the scalar damping and write $A_0=-z\sigma_x$. A constant symmetric
form $L$ cancels the full $z$-dependent bulk coupling exactly when

\[
A_0^TL+LA_0=0.
\]

For all $z$, this is equivalent to

\[
\sigma_xL+L\sigma_x=0.
\]

The nonzero symmetric solutions are

\[
L=\lambda
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Hence the source flow selects the Lorentz form uniquely up to scale. Restoring
the damping and forcing gives

\[
(\partial_x+1)(m^2-n^2)=-2fm.
\]

The coordinate identity $m^2-n^2=T_+T_-$ fixes the natural scale in the
labelled tail frame. But this form is indefinite: every nonzero solution has
negative determinant. It cannot be the positive metric assumed by the
conditional boundary-generator compiler above.

## The Clark Gram is a different typed object

The native Clark construction supplies the positive feature energy

\[
2|G+f|^2+2a^2|\partial_zG|^2.
\]

This is a Gram form on the feature packet

\[
(G+f,a\partial_zG),
\]

not on the tail-state packet $(m,n)$. Existing work has not proved that the
state-to-feature map is injective or that pulling the Clark Gram back produces
a completed positive metric on the tail domain.

Therefore the programme currently has two source-derived forms:

- an indefinite Lorentz balance on labelled reciprocal tails;
- a positive Euclidean Gram form on Clark features.

No source-derived isometry, Wick comparison, or common boundary object has
yet identified them. The de Rham concomitant cannot select such an
identification because it transports every supplied constant symmetric form.

This changes the metric frontier. The missing higher coherencer must compare
the Lorentz tail relation with the positive Clark feature relation while
retaining the forcing and endpoint ports. Asking directly for one positive
metric on the tail carrier imposes a structure the current source does not
supply.

The finite falsifier is immediate. Any proposed positive tail metric that
cancels the full $z\sigma_x$ coupling must solve the anticommutation equation
above, but every nonzero solution is indefinite. Positivity can emerge only
after passage to the doubled Clark feature object or another independently
derived enlargement.

## The missing comparison changes the real structure

A complex quarter-turn does convert the Lorentz bilinear form into a Euclidean
bilinear presentation. Put

\[
W=
\begin{pmatrix}
1&0\\
0&i
\end{pmatrix},
\qquad
J=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Then

\[
W^TW=J.
\]

But

\[
W^\dagger W=I.
\]

The quarter-turn changes the complex bilinear presentation; it does not pull
a positive Hermitian form back to an indefinite one. Hermitian inertia cannot
change under an invertible complex congruence. Therefore no complex-linear
isometry identifies the Lorentz tail energy with the positive Clark energy.

The missing datum is an antilinear real structure. Let

\[
\mathcal C(v)=J\overline v.
\]

It is an involution:

\[
\mathcal C^2=I.
\]

If the Lorentz bilinear pairing is

\[
B(v,w)=v^TJw,
\]

then

\[
B(v,\mathcal C v)=v^T\overline v=|m|^2+|n|^2.
\]

Thus the same labelled two-channel carrier supports an indefinite analytic
bilinear relation and a positive Hermitian relation once reciprocal
conjugation is supplied. The positive form is not obtained by forgetting the
Lorentz relation; it is obtained by composing it with the antilinear sector
comparison.

## The critical seam is the fixed locus of the real structure

For the homogeneous tail generator

\[
A(z)=-\frac12I-z\sigma_x,
\]

the antilinear comparison obeys

\[
J\overline{A(z)}J=A(-\overline z).
\]

Hence it transports the fiber at $z$ to the fiber at $-\overline z$. It is
internal to one parameter fiber exactly when

\[
z=-\overline z,
\]

which is the critical seam in centered coordinates.

This gives a source-level explanation of why the seam is special: only there
does reciprocal conjugation become an internal dagger structure on the tail
fiber. Off seam it compares two distinct fibers.

This is not zero confinement. The positive Hermitian norm exists for every
vector and the antilinear transport exists between off-seam paired fibers.
Hostile reciprocal source deformations may preserve both structures while
changing the scalar divisor. The remaining theorem must show that the
forcing-to-boundary return incidence is compatible with this dagger structure
and that its completed characteristic pairing cannot vanish off the fixed
locus.

The higher coherencer now has a more exact type: it is not merely a linear
comparison cell. It is a dagger-compatible modification joining the analytic
Lorentz relation, reciprocal conjugation, the affine forcing cocycle, and the
positive Clark feature relation.

## Dagger compatibility reduces but does not remove the return freedom

Give the scalar boundary port ordinary conjugation and the tail port the real
structure $\mathcal C$. The full block involution is generated by

\[
\widehat J=
\begin{pmatrix}
J&0\\
0&1
\end{pmatrix}.
\]

Assume the forcing column obeys its source-derived reciprocal law

\[
\mathbf r(-\overline z)=J\overline{\mathbf r(z)}.
\]

For the return family $\mathbf c_\kappa=\kappa\mathbf r$, covariance of the
full block requires

\[
\kappa(-\overline z)=\overline{\kappa(z)}.
\]

A constant return gain must therefore be real. The dagger structure reduces
the free complex line to a free real line, but it does not fix magnitude or
sign. Two distinct nonzero real gains preserve the same dagger covariance and
change the characteristic section.

The seam makes the Schur readout real under the declared involution; reality
does not imply nonvanishing. Dagger coherence explains the fixed locus but
does not supply zero confinement.

## The native boundary object is an additive current

The Lorentz balance has a stronger typing consequence. Put

\[
Q=m^2-n^2.
\]

Then

\[
\partial_x(e^xQ)=-2e^xfm.
\]

Define the accumulated endpoint current

\[
Y(x)=2\int_{x_0}^x e^u f(u)m(u)\,du.
\]

The exact conservation law is

\[
e^xQ(x)+Y(x)=e^{x_0}Q(x_0).
\]

Thus the source naturally produces an additive current ledger. It does not
produce a third Hilbert amplitude with a quadratic norm. Treating $Y$ as an
ordinary state coordinate in a determinant block is therefore not yet typed.

To affect a determinant line, the additive current must be sent to a
multiplicative transition. A holomorphic character has the form

\[
\chi_\kappa(Y)=e^{\kappa Y},
\]

and obeys

\[
\chi_\kappa(Y_1+Y_2)
=
\chi_\kappa(Y_1)\chi_\kappa(Y_2).
\]

The scale $\kappa$ remains free. Its first derivative at the identity is

\[
\chi_\kappa'(0)=\kappa.
\]

This is exactly the return gain found by linear Schur analysis. The apparent
one-parameter family of return rows is the infinitesimal shadow of the family
of characters from the additive current effect to the multiplicative
determinant-line effect.

The missing constructor has therefore changed type again. It is not primarily
a metric-selected matrix row. It is a source-authorized effect conversion

\[
(\mathbb C,+)\longrightarrow(\mathbb C^\times,\cdot)
\]

with a fixed unit relating endpoint current to determinant-line holonomy.
Neither additivity, dagger covariance, nor positivity fixes that unit.

This identifies the common core of the metric and Schur obstructions. Choosing
the boundary weight $h$, choosing the return gain $\kappa$, and choosing the
current-to-line character are three presentations of the same missing source
normalization. A successful theta/Tate construction must derive the character
before scalar determinant evaluation.

## The co-moving odd row fixes the frozen-source normalization

There is a canonical local candidate for the return incidence. Let

\[
q^T=(1,-1)
\]

be the primitive odd codiagonal and define

\[
C_\ell=q^TD_\ell.
\]

With outgoing column $B_\ell=-\mathbf r_\ell$, the Schur complement becomes

\[
S_\ell
=e-C_\ell D_\ell^{-1}B_\ell
=e+q^T\mathbf r_\ell.
\]

This row is co-moving with the Green frame and inherits its normalization from
the same odd codiagonal that produces the valuation response. No independent
gain is inserted. Differentiating the complete Schur expression cancels the
return-row and retained-transport derivatives, leaving

\[
S_\ell'=q^T\mathbf r_\ell'.
\]

This exactly fixes the return presentation. It does not yet prove that the
remaining derivative equals the moving theta endpoint current.

## Variable forcing produces a new first-jet residual

The frozen-source model takes the forcing to be constant across the interval.
Then

\[
\mathbf r_\ell
=
\int_0^\ell D_{\ell-u}\mathbf 1 f_0\,du
\]

and the co-moving Schur derivative equals the expected endpoint current.

The actual theta forcing varies with the moving endpoint. For

\[
f(u)=f_0+gu
\]

define

\[
\mathbf r_\ell
=
\int_0^\ell D_{\ell-u}\mathbf 1 f(u)\,du
\]

and compare the Schur derivative with

\[
Q_\ell=2f(\ell)e^{-\ell/2}\sinh(z\ell).
\]

The exact local expansion gives

\[
q^T\mathbf r_\ell'+Q_\ell
=zg\ell^2+O(\ell^3).
\]

Thus constant forcing closes the first jet, while the first forcing derivative
creates a nonzero quadratic residual. For the theta source,

\[
f'(x)=-4\pi e^{2x}e^{-\pi e^{2x}},
\]

so this correction is generically present.

The co-moving odd row therefore repairs the arbitrary return gain but does not
complete the source-varying theta current. The next required port is the
forcing jet, or an equivalent covariant connection that differentiates the
source while the endpoint moves. Treating $f$ as frozen removes precisely this
port.

This local residual is a sharper finite falsifier than a completed scalar
comparison. Any proposed determinant character must reproduce the
$zf'(x)\ell^2$ term before prime sampling and completion. If it does not, its
apparent normalization is an artifact of freezing the source along the
transport interval.

## The theta forcing has an exact source connection

The forcing is not an arbitrary function. Introduce

\[
y=e^{2x},
\qquad
f=2e^{-\pi y}.
\]

It obeys the closed nonlinear system

\[
\partial_xy=2y,
\qquad
\partial_xf=-2\pi yf.
\]

Equivalently, the forcing is horizontal for the source-derived scalar
connection

\[
\nabla_xf=
(\partial_x+2\pi y)f=0.
\]

Its exact interval transport is

\[
f(x+\ell)
=
f(x)
\exp\left[-\pi y(x)(e^{2\ell}-1)\right].
\]

Thus the forcing-jet correction is not a free counterterm. It is generated by
the same moving Gaussian endpoint source.

## Finite nonlinear closure becomes an infinite linear tower

The pair $(y,f)$ closes nonlinearly. A linear operator realization behaves
differently. Define the graded observables

\[
h_k=y^kf,
\qquad
k\ge0.
\]

Their derivatives satisfy

\[
\partial_xh_k
=2kh_k-2\pi h_{k+1}.
\]

Every finite truncation leaks at its top grade. In particular,

\[
\partial_xh_N
=2Nh_N-2\pi h_{N+1}
\]

contains a nonzero direction outside the span of
$h_0,\ldots,h_N$.

Therefore the exact forcing connection has two lawful presentations:

- a finite nonlinear source system on $(y,f)$;
- an infinite upper-shift linear system on the graded forcing jets.

It has no finite transport-complete linear realization on these natural
observables. The variable-forcing residual is the first leaked grade of that
linear tower.

This recovers the earlier infinite-closure lesson in a source-local form.
Finite determinant blocks can model the frozen forcing or a bounded jet
truncation, but exact moving-endpoint transport requires either the nonlinear
source object or the full graded tower.

The categorical choice is now explicit. A determinant-line functor must be
defined on the nonlinear source connection or on a completion of the infinite
linear jet module. Applying a finite matrix determinant before making that
choice necessarily loses the forcing coherencer.

This still does not establish horizontality of the completed characteristic
section. It constructs the previously missing forcing connection and proves
that a finite linear Schur closure cannot carry it exactly.
