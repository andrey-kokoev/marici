# The Missing Sewing Object Is a Local Recollement and a Global Stratified Boundary

## Correction to the bare cospan

The constant--delta obstruction does not merely request an unspecified common
boundary object. At one local place it has the standard shape of a
recollement.

Let $X_v$ be the additive local field, let $U_v=X_v\setminus\{0\}$, and let
$Z_v=\{0\}$. Write

\[
j_v:U_v\hookrightarrow X_v,
\qquad
i_v:Z_v\hookrightarrow X_v.
\]

The open and closed sectors are connected by the six operations associated
with the two embeddings:

\[
j_{v!},\ j_v^*,\ j_{v*},
\qquad
i_v^*,\ i_{v*},\ i_v^!.
\]

Restriction $j_v^*$ cannot see a distribution supported at zero:

\[
j_v^*\delta_0=0.
\]

This is not loss inside the recollement. The delta distribution belongs to
the closed-stratum image of $i_{v*}$. Endpoint evaluation and endpoint
costalk are carried by $i_v^*$ and $i_v^!$, not by pretending that
$\delta_0$ is an interior trace state.

## Fourier is a cross-stratum constructor

Additive Fourier transform does not preserve the two strata separately. On
the external distributional plane it exchanges

\[
1\longleftrightarrow\delta_0.
\]

The constant has a nonzero open restriction, while the delta is supported on
the closed stratum. Fourier is therefore a constructor on the completed
recollement, not an endomorphism derived from the open restriction functor.

This explains the earlier no-go. Asking for an injective idelic restriction
containing both ports attempts to collapse the recollement into its open
sector. The impossible injective trace was the result of erasing the closed
stratum.

At the real place, Grothendieck's two-sign logarithmic trace is precisely the
open sector. Its Fourier-conjugated Hankel operator carries the effect of the
global Fourier constructor on that open trace. The endpoint moment tower is
the boundary data required to extend this action across the closed stratum.

## Why this is not yet a global adelic recollement

For each local field, the nonzero locus is the complement of one closed
point. Globally, however, the idele group is not simply one open complement
inside the additive adeles. It imposes nonvanishing at every place and the
restricted-product unit condition at almost every finite place. It is
additive-Haar null.

Therefore the global object cannot be obtained by declaring one open idele
stratum and one closed zero stratum. It needs a stratified restricted-product
boundary recording which local conditions fail. Finite-place valuation
strata carry the arithmetic constructor data; the archimedean zero stratum
carries the constant--delta and moment boundary.

This separates the known channels without declaring them independently
positive:

- the archimedean endpoint gives a closed-stratum boundary tower;
- primitive and prime-square incidences occupy typed finite-place strata;
- the connected prime-power tail occupies the summable interior completion;
- reciprocal Fourier--Tate sewing acts across the assembled stratification.

The global sewing object should therefore be a restricted product of local
recollement data, or an equivalent adelic stratified category, rather than a
single Hilbert trace space.

## Relation to the A3 path algebra

The three directed roles previously typed by the $A_3$ path algebra can now
be read more concretely as closed boundary, completed additive source, and
open multiplicative trace. Write these objects as

\[
\mathcal Z\longrightarrow\mathcal X\longrightarrow\mathcal U.
\]

This is a directed stage decomposition. It is not the three-generator
Veronese space. The six recollement operations likewise do not imply a
six-dimensional carrier. They are six typed functorial roles.

The Veronese algebra acts independently on the external endpoint grade. The
$A_3$ stage algebra acts on passage among boundary, source, and trace. A
source theorem is still required to show that grade change commutes with
stage transport.

## Dagger and the first intrinsic loop

Forward restriction alone is acyclic. An authorized pairing supplies adjoint
mates and creates round trips. Locally, the relevant comparisons have the
forms

\[
j_{v!}\dashv j_v^*\dashv j_{v*},
\qquad
i_v^*\dashv i_{v*}\dashv i_v^!.
\]

Units and counits of these adjunctions are the first legitimate coherence
cells joining the strata. They provide the categorical location for the
round-trip curvature found in the dagger-enhanced endpoint tower. An
arbitrary reverse map would not.

This also types the proposed mate construction: its source pairings must
realize the appropriate adjunction on the rigged boundary category. Merely
having a formal transpose matrix is insufficient.

## Exact next gate

At a finite place the first gate already has an explicit two-port form. For
$f\in\mathcal S(\mathbb Q_p)$ define

\[
\epsilon_p(f)=f(0),
\qquad
\mu_p(f)=\int_{\mathbb Q_p}f(x)\,dx.
\]

With self-dual Haar normalization, additive Fourier transform exchanges the
two functionals:

\[
\epsilon_p(\mathcal F_pf)=\mu_p(f),
\qquad
\mu_p(\mathcal F_pf)=\epsilon_p(f).
\]

The restriction $j_p^*f$ on $\mathbb Q_p^\times$ retains an eventual germ as
$x\to0$. Because $f$ is locally constant, that germ is precisely
$\epsilon_p(f)$. Its Fourier mate $\mu_p(f)$ is global rather than germ-local.
Thus the constant--delta exchange plane is more accurately the dual boundary
observer plane

\[
P_{\partial,p}^*=\operatorname{span}\{\epsilon_p,\mu_p\}.
\]

This supplies a canonical local Veronese incidence into symmetric powers of
observer ports. It does not place $1$ and $\delta_0$ inside the open trace as
states. The distinction between carrier and observer is essential.

The smallest exact diagram to test is the Fourier exchange square

\[
\begin{array}{ccc}
\mathcal S(\mathbb Q_p)&\xrightarrow{\mathcal F_p}&
\mathcal S(\mathbb Q_p)\\
\downarrow(\epsilon_p,\mu_p)&&\downarrow(\epsilon_p,\mu_p)\\
\mathbb C^2&\xrightarrow{B}&\mathbb C^2,
\end{array}
\qquad
B=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

This square commutes exactly. What remains nontrivial is compatibility with
valuation shift and with the restricted-product bonding maps.

## Valuation shift produces the local coherencer

For $a\in\mathbb Q_p^\times$, use the unitary additive dilation

\[
(D_af)(x)=|a|_p^{1/2}f(ax).
\]

The two boundary observers transform with reciprocal weights:

\[
\epsilon_p(D_af)=|a|_p^{1/2}\epsilon_p(f),
\qquad
\mu_p(D_af)=|a|_p^{-1/2}\mu_p(f).
\]

On the ordered observer vector $(\epsilon_p,\mu_p)$, dilation therefore has
matrix

\[
A_p(a)=
\begin{pmatrix}
|a|_p^{1/2}&0\\
0&|a|_p^{-1/2}
\end{pmatrix}.
\]

Fourier exchange does not commute with this action. Instead it reverses it:

\[
BA_p(a)B=A_p(a)^{-1}.
\]

For the prime dilation $a=p$, since $|p|_p=p^{-1}$,

\[
A_p(p)=
\begin{pmatrix}
p^{-1/2}&0\\
0&p^{1/2}
\end{pmatrix}.
\]

Thus the local boundary algebra is generated by one valuation translation
and one reflection, with the reflection conjugating the translation to its
inverse. The coherencer is not a commuting square. It is the exact dihedral
relation between valuation transport and Fourier sewing.

On the first even Veronese grade, the induced weights are

\[
p^{-1},\ 1,\ p.
\]

The Fourier involution exchanges the two extremal weights and fixes the mixed
weight. This derives the three grade-one directions from the source ports:
contracting endpoint, neutral relationship, and expanding total-mass mate.

The determinant of $A_p(a)$ is one. Hence local dilation preserves oriented
two-port volume even though neither observer has invariant size separately.
Any scalar compression selecting only one port destroys this reciprocal
conservation law.

## The deeper local object

The diagonal matrices $A_p(a)$ form the split torus of an $SL_2$-type
representation. The Fourier exchange $B$ acts as its Weyl reflection. Their
relation

\[
BA_p(a)B=A_p(a)^{-1}
\]

is the defining torus--Weyl relation. Thus valuation transport and reciprocal
sewing are two parts of one local rank-one representation, not independent
repairs.

The endpoint tower

\[
\bigoplus_{l\ge0}\operatorname{Sym}^{2l}P_{\partial,p}^*
\]

is the even symmetric representation tower of this two-port object. At grade
$l$, the torus weights range from $|a|_p^l$ to $|a|_p^{-l}$ in unit steps of
$|a|_p^{-1}$. The Weyl action reverses that weight string. The celestial conic
and its even Veronese algebra are therefore the projective endpoint shadow of
the same local torus--Weyl mechanism.

There is one typing qualification. The matrix $B$ on the even boundary
functionals is an involution. The full Fourier operator also retains parity,
and its metaplectic lift is generally order four before passage to even
symmetric grades. The even Veronese tower forgets that central sign. It cannot
replace the full signed Fourier boundary packet.

## Prime powers and the arithmetic normalization

Write the prime dilation as an exponential

\[
A_p(p)=\exp\left(-\frac{\log p}{2}Q\right),
\qquad
Q=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Its $k$-fold iterate has logarithmic generator $k\log p$. Raw transport alone
would therefore assign a coefficient proportional to $k\log p$ to the label
$p^k$. That is not the von Mangoldt coefficient.

The connected-cycle expansion supplies the necessary orbit normalization:

\[
-\log(1-p^{-s})
=\sum_{k\ge1}\frac{p^{-ks}}{k}.
\]

Differentiation with respect to $s$ cancels the iterate length:

\[
-\frac{d}{ds}
\left(\frac{p^{-ks}}{k}\right)
=(\log p)p^{-ks}.
\]

Thus the local representation and the positive Fock grammar perform distinct
jobs:

- torus iteration records the valuation length $k$;
- the connected-cycle symmetry factor contributes $1/k$;
- the spectral derivative contributes $k\log p$;
- their product yields $\Lambda(p^k)=\log p$.

No corresponding primitive cycle exists at a mixed label $pq$. This retains
the earlier type distinction: tensoring two different local excitations is
not a new primitive orbit.

This gives an exact compatibility gate for any global assembly. If its
prime-power transport lacks the cycle factor $1/k$, it produces the wrong
arithmetic current. If it freely promotes mixed-prime tensors to primitive
cycles, it erases Euler type.

## Restricted-product vacuum and excitation

For the standard unramified local source $f_p=1_{\mathbb Z_p}$ with self-dual
normalization,

\[
\epsilon_p(f_p)=1,
\qquad
\mu_p(f_p)=1.
\]

The corresponding observer vector is fixed by Fourier exchange. Prime
dilation moves it to

\[
\begin{pmatrix}p^{-1/2}\\p^{1/2}\end{pmatrix},
\]

which is not the unramified vacuum. Consequently a prime constructor is a
typed local excitation, not an alternative choice of the restricted-product
vacuum.

Only finitely many such state excitations belong to an ordinary restricted
product. The completed Euler object packages infinitely many virtual cycle
contributions through a determinant or connected logarithm instead. Treating
that determinant expansion as an infinite tensor product of excited boundary
states would conflate a scalar connected readout with the underlying state
carrier.

## Hostile germ classification

The Weyl reversal law does not uniquely select valuation dilation. Let $X$ be
a real infinitesimal generator and impose

\[
BXB=-X.
\]

For $B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, every solution has the form

\[
X(a,b)=
\begin{pmatrix}
a&b\\
-b&-a
\end{pmatrix}.
\]

Its square is scalar:

\[
X(a,b)^2=(a^2-b^2)I.
\]

The sign of $a^2-b^2$ separates three distinct transport types:

- positive: hyperbolic valuation dilation;
- negative: elliptic rotation;
- zero: nilpotent shear.

All three satisfy the same first-order Fourier reversal law. In particular,
the hostile rotation generator

\[
X(0,1)=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
\]

passes the categorical germ test but is not prime valuation transport.

The arithmetic source supplies the missing selector: $|a|_p$ is a positive
real character, so its boundary action is diagonalizable over the ordered
real observer lines and has $a^2-b^2>0$. This source fact must remain in the
constructor contract. Torus--Weyl coherence without the positive valuation
character is insufficient.

The finite falsifier for a proposed local arithmetic constructor is therefore
the discriminant

\[
\Delta_X=a^2-b^2.
\]

A nonpositive value rejects its interpretation as a nontrivial valuation
dilation even when every Fourier-reversal square commutes.

## The celestial conic is the transport discriminant boundary

The first Veronese grade satisfies

\[
H_1\cong\operatorname{Sym}^2\mathbb C^2\cong\mathfrak{sl}_2(\mathbb C)
\]

as an $SL_2$ representation. On $\mathfrak{sl}_2$, the invariant quadratic
form is proportional to the determinant or Killing form. Its projective zero
locus is the nilpotent conic.

The Fourier-odd generator plane $BXB=-X$ is a real two-dimensional slice of
this adjoint representation. On that slice, the invariant reduces to

\[
\Delta_X=a^2-b^2.
\]

Therefore the three hostile-germ types are the three real orbit regions cut
out by the celestial conic:

- hyperbolic valuation generators lie on one side;
- elliptic rotation generators lie on the other;
- nilpotent shear generators lie on the conic.

This gives the endpoint conic an operational meaning. It is the degeneracy
wall where an infinitesimal transport loses semisimple orientation. The
Veronese tower records symmetric powers of the same two-port representation,
while its quadratic relation records the transport-type boundary.

Over $\mathbb C$, the sign distinction between the two nonzero real regions
is unavailable. Hence the complex algebraic conic alone cannot select
arithmetic valuation transport over hostile elliptic transport. The selector
is the source-derived real form together with the positive valuation
character.

## Global operator-ideal filtration

On the unitary seam, the connected contribution of the $k$-fold prime orbit
has magnitude proportional to

\[
\frac{p^{-k/2}}{k}.
\]

The square-summability test is therefore

\[
\sum_p\frac{p^{-k}}{k^2}.
\]

For $k=1$ this contains the divergent prime harmonic series. For every
$k\ge2$ it converges. Thus the primitive current is not Hilbert, while the
prime-square current and higher currents admit a Hilbert realization.

Absolute summability instead requires

\[
\sum_p\frac{p^{-k/2}}{k}.
\]

This diverges for $k=1$ and $k=2$, and converges for $k\ge3$. Consequently the
global packet has the exact filtration:

1. $k=1$ is a distributional primitive boundary current;
2. $k=2$ is Hilbert--Schmidt but not trace class;
3. $k\ge3$ is trace class.

This reproduces the order-three regularization boundary from the local
torus--Weyl and cycle data. It also explains why the first two currents cannot
be deleted. They are the lower operator-ideal strata required to complete the
same local constructor globally.

The appropriate global object is therefore a filtered extension, not one
ordinary determinant-class operator. Its trace-class quotient begins at
$k=3$; the primitive and square components remain typed relative-boundary
data. A scalar regularized determinant records their combined readout but
does not reconstruct either lower stratum.

## Global hostile test

Local positivity of every discriminant does not imply that the restricted
product exists as a bounded or determinant-class operator. A hostile family
can choose hyperbolic generators $X_p$ with $\Delta_{X_p}>0$ at every prime
while allowing their norms to grow too quickly.

For a proposed assembly, define the cycle-normalized seam amplitudes
$c_{p,k}$. The exact ideal gates are:

\[
\sum_p|c_{p,k}|^2<\infty
\]

for Hilbert--Schmidt admission, and

\[
\sum_p|c_{p,k}|<\infty
\]

for trace-class admission. Passing the local discriminant test without the
appropriate global summability test is insufficient.

The smallest global falsifier is therefore a positive local family for which
one required ideal sum diverges in a grade declared to occupy that ideal.
This separates source orientation from completion stability.

## Spectral coupling and the unitary seam

The real valuation generator must be distinguished from its complex spectral
coupling. Put

\[
z=s-\frac12,
\qquad
A_p(z)=\exp\left(-z(\log p)Q\right).
\]

Weyl reflection and dagger act by

\[
BA_p(z)B=A_p(-z),
\qquad
A_p(z)^\dagger=A_p(\overline z).
\]

Their combined parameter involution is

\[
z\longmapsto-\overline z.
\]

Its fixed locus is $\operatorname{Re}z=0$. On that locus $A_p(z)$ is unitary.
This derives the critical line as the unitary sewing seam of the local
torus--Weyl packet.

The conclusion is geometric, not spectral: it identifies the fixed unitary
locus but does not imply that a scalar matrix coefficient or completed
section is nonzero away from it.

## Cycle normalization still does not confine scalar zeros

Even the first two connected-cycle coefficients admit a positive reciprocal
hostile readout. Consider

\[
F(z)=e^z+e^{-z}
+\frac12\left(e^{2z}+e^{-2z}\right).
\]

The weights $1$ and $1/2$ match the connected-cycle factors $1/k$ for
$k=1,2$. The function is positive-source, conjugation-compatible, and even
under $z\mapsto-z$.

Set $y=e^z+e^{-z}$. Then

\[
F(z)=y+\frac12(y^2-2).
\]

The zero equation is

\[
y^2+2y-2=0.
\]

Its negative root $y=-1-\sqrt3$ is less than $-2$. Hence
$e^z+e^{-z}=y$ has negative real reciprocal solutions of unequal modulus,
giving zeros with nonzero real part.

This does not contradict local Euler-factor nonvanishing. The finite
connected current has been used here as a scalar readout; it has not been
closed under the full exponential constructor that forms an Euler factor.
The example instead proves a typing boundary:

- cycle normalization explains $\Lambda(p^k)$;
- reciprocal sewing explains the unitary seam;
- neither statement makes an arbitrary positive connected-current readout
  zero-free off the seam.

Any zero-confinement argument must use the complete source-authorized
determinant or section and its cross-scale boundary law. It cannot be inferred
from the local representation, its symmetric powers, or finitely many
cycle-normalized currents.

## Candidate determinant coherencer

The order-three filtration suggests a specific higher cell. For a finite
matrix $T$, define

\[
\det_3(I+T)
=\det\left((I+T)\exp\left(-T+\frac12T^2\right)\right).
\]

Its logarithm retains the connected powers beginning at degree three:

\[
\log\det_3(I+T)
=\sum_{k\ge3}\frac{(-1)^{k+1}}{k}\operatorname{tr}(T^k).
\]

Unlike the ordinary determinant, $\det_3$ is not strictly multiplicative. For
commuting finite matrices $A$ and $B$, direct expansion gives

\[
\frac{\det_3((I+A)(I+B))}
{\det_3(I+A)\det_3(I+B)}
=
\exp\operatorname{tr}
\left(
A^2B+AB^2+\frac12A^2B^2
\right).
\]

The right-hand side is not an error term to discard. It is the finite
comparison cell between the one-step product and the two separately
regularized factors.

This gives a precise candidate architecture:

- primitive and square currents choose the relative determinant frame;
- the $k\ge3$ tail defines the order-three determinant;
- the multiplicative anomaly supplies the coherence cell for changing Euler
  factorization paths;
- the archimedean boundary must provide the matching global normalization.

The formula is currently a finite commuting model, not a theta theorem.
Noncommuting operator blocks require their source-ordered anomaly polynomial,
and its traces must be continuous in the declared operator ideals.

The smallest falsifier is immediate. For two source-derived finite prime
blocks, compute both sides of the displayed anomaly formula in the authorized
frame. Any unexplained residual proves that the proposed primitive,
prime-square, and connected-tail packet is not a coherent order-three
determinant system.

## Status correction: both finite shadows already close

The two-prime calculation is already exact in the labelled source square. If
$a$ and $b$ are the two prime increments, their shared corner gives

\[
c=a+b+ab.
\]

The order-three anomaly is

\[
\log D_3(c)-\log D_3(a)-\log D_3(b)
=ab\left(a+b+\frac12ab\right),
\]

and the primitive--square boundary factor supplies the negative of this
quantity. Thus the determinant-line composition gate closes.

The endpoint shadow also closes. Let $S_L$ be the left translation
coisometry on $L^2(0,\infty)$,

\[
(S_Lf)(u)=f(u+L).
\]

Its adjoint inserts a zero prefix, and

\[
S_LS_L^*=I,
\qquad
S_L^*S_L=I-P_L,
\qquad
P_L=M_{\mathbf 1_{[0,L)}}.
\]

The moving-seam window is the source pairing with $P_L$. For two shifts,

\[
P_{L_1+L_2}
=P_{L_1}+S_{L_1}^*P_{L_2}S_{L_1}.
\]

This is exactly the transported-window cocycle. It produces the shared
$pq$ endpoint incidence without fitting a scalar repair.

## The common-refinement obstruction

The two exact shadows live at different operator levels:

- the coisometry and $P_L$ live in the half-line translation/defect algebra;
- the order-three anomaly lives in a regularized determinant line.

The projection $P_L$ has infinite-dimensional range for every $L>0$ and is
not compact. Therefore its exact endpoint colligation does not possess an
ordinary Fredholm determinant. Conversely, determinant-line data forget the
special-linear incidence and cannot reconstruct the coisometry, its adjoint,
or its defect projection.

The common refinement would require a source-derived functor

\[
\mathfrak C_\Phi:
\mathcal W_{\mathrm{seam}}
\longrightarrow
\mathcal I_{\le2}\ltimes\mathcal S_3
\]

from the seam defect algebra to the filtered operator-ideal packet. It must
have two simultaneous shadows:

1. endpoint pairing recovers every transported moving window;
2. regularized determinant recovers the shared-corner anomaly and its
   primitive--square cancellation.

No such functor is presently constructed. Heat sandwiching makes the seam
projection trace class at a positive regulator scale, but the resulting
determinant depends on that scale. Arbitrary Hardy, de Branges, or spectral
compression could manufacture the desired operator ideal and is not source
authority.

This changes the decisive gate. The finite anomaly formula no longer needs
to be rediscovered. The required test is whether one source-selected
compression preserves the projection cocycle, Fourier--Tate transport, and
the order-three determinant anomaly at once.

The finite obstruction is the infinite rank of $P_L$. The completion
obstruction is regulator dependence. A successful construction must remove
both without deriving its compression from the target scalar section.

## Two natural completions fail in complementary ways

The ordinary Hilbert completion admits $P_L$ as a bounded endomorphism, but
$P_L$ is noncompact. Passing to the closed translation orbit of the Gaussian
does not help: the logarithmic Gaussian has a Fourier transform with no real
zeros, so its translates are cyclic and their Hilbert closure is the whole
carrier.

The Fourier-stable Gaussian Gelfand--Shilov rigging has the opposite
properties. It retains quasianalytic source information and makes the full
moment germ faithful. But multiplication by the sharp indicator
$\mathbf 1_{[0,L)}$ creates jumps at the interval endpoints. Therefore

\[
P_L\mathcal G\not\subseteq\mathcal G.
\]

The sharp seam projection is not an endomorphism of the Gaussian analytic
rigging.

Thus:

- the Hilbert category has the exact seam operator but no determinant-class
  defect;
- the Gaussian analytic category has source faithfulness but no internal
  sharp seam operator.

This rules out the two most immediate realizations of $\mathfrak C_\Phi$.

## The seam must remain a correspondence

For the analytic source space $\mathcal G$, factor the sharp cut through a
separately typed interval object:

\[
\mathcal G
\xrightarrow{r_L}
\mathcal G|_{[0,L)}
\xrightarrow{e_L}
\mathcal G'.
\]

Here $r_L$ is restriction and $e_L$ is extension by zero into a distributional
target. Their composite represents $P_L$, but it is not asserted to be an
endomorphism of $\mathcal G$.

For two intervals, the transported decomposition becomes a composition law
among restriction and extension correspondences. This retains the exact
projection cocycle without forcing a discontinuous state back into the
analytic bulk.

The determinant question must consequently be posed for the relative
boundary correspondence or its mapping cone, not for $I+P_L$ on one Hilbert
space. To obtain a determinant line, that relative object must still be shown
to have an authorized nuclear or Fredholm realization. Rephrasing it as a
correspondence removes the false endomorphism requirement but does not by
itself prove determinant admissibility.

The next exact gate is whether the source-derived interval restriction maps
form a nuclear compatible family in the Gaussian inductive topology and
whether their mapping cones reproduce the primitive, square, and connected
operator-ideal grades. Failure of nuclearity closes this refinement; success
would provide the first non-regulator common lift.

## Nuclear restriction is still non-Fredholm

Nuclearity of the restriction map is not sufficient. Consider a Hilbert step
$\mathcal G_h$ of the Gaussian rigging for which

\[
r_L:\mathcal G_h\longrightarrow L^2(0,L)
\]

is compact. Polynomial--Gaussian states belong to the source class, and
their restrictions are dense in $L^2(0,L)$. Hence $r_L$ has dense range.

If that range were closed, it would equal $L^2(0,L)$. After quotienting any
kernel, the inverse on the range would be bounded. The identity on the
infinite-dimensional target would then factor through the compact map
$r_L$, making the identity compact, which is impossible.

Therefore the natural compact restriction has nonclosed range and is not
Fredholm. Its raw mapping cone does not carry a finite determinant line.

This sharpens the common-refinement requirement once more. The missing datum
cannot be only a source-selected topology or a nuclear restriction. It must
include a boundary differential, return incidence, or polarization that
pairs the infinitely many interval modes and produces a Fredholm relative
complex.

The source authority test is strict: that pairing must be derived before
forming the determinant and must reproduce the exact moving-window
functional. Choosing it to close the range after inspecting the desired
section would merely fit the missing Schur block.

## Fourier pairs the interval modes but gives a universal determinant

There is one canonical boundary pairing with no heat parameter. Let

\[
K_L=r_L\mathcal F e_L:
L^2(0,L)\longrightarrow L^2(0,L),
\]

where $e_L$ extends by zero, $\mathcal F$ is additive Fourier transform, and
$r_L$ restricts back to the interval. Its kernel is

\[
K_L(x,y)=e^{-2\pi ixy},
\qquad
0<x,y<L.
\]

Therefore $K_L$ is Hilbert--Schmidt and

\[
\|K_L\|_2^2=L^2.
\]

The positive operator $K_L^*K_L$ is trace class. Moreover, $K_L$ has no
singular value equal to one. Equality would require a nonzero function
supported in $(0,L)$ whose Fourier transform is also supported in $(0,L)$,
which is impossible by analytic continuation.

Consequently

\[
I-K_L^*K_L>0
\]

and its Fredholm determinant exists and is nonzero:

\[
\det(I-K_L^*K_L)>0.
\]

This construction pairs all interval modes and removes the raw non-Fredholm
defect without choosing a heat scale. But it is universal: it depends only on
the interval and additive Fourier transform, not on the labelled theta source
or prime incidence.

Hence it cannot be the completed arithmetic section. It can at most provide
a canonical positive background metric or polarization on the seam
correspondence. To become the common refinement, a separately derived theta
incidence must enter before determinant formation and must reproduce both the
moving-window current and the shared-prime order-three anomaly.

The hostile test is any alternative source placed in the same interval. It
inherits the identical operator $K_L$ and the identical nonvanishing
determinant. Thus the Fourier--interval determinant carries no
source-selective zero information by itself.

## The finite Fourier pairing loses its gap at completion

For every fixed $L$, the operator

\[
A_L=I-K_L^*K_L
\]

is positive and invertible. This makes it a legitimate finite bulk block for
a Schur complement.

The inverse is not uniformly controlled as $L$ grows. Choose a normalized
Gaussian wave packet whose position center and frequency center both lie
deep inside $(0,L)$. As $L\to\infty$, the mass lost by position restriction
and by Fourier restriction tends to zero. Therefore there are unit vectors
$g_L$ such that

\[
\|K_Lg_L\|\longrightarrow1.
\]

It follows that

\[
\langle g_L,A_Lg_L\rangle\longrightarrow0,
\qquad
\|A_L^{-1}\|\longrightarrow\infty.
\]

Thus the canonical finite Fourier pairing has an approximate blindness
direction at completion. A complete Schur expression

\[
E_L-C_LA_L^{-1}B_L
\]

may be well-defined at every finite cutoff while becoming unstable in the
limit.

This is the operator version of escape at infinity. Finite positivity and a
nonzero finite determinant do not supply the uniform observability required
for completed sewing.

A theta-specific admissible packet could avoid these Gaussian phase-space
escapes only if its source constructors exclude them or add a uniformly
controlling boundary row. That exclusion or row must be derived before the
Schur complement is formed. The universal Fourier--interval geometry cannot
provide it.

## Exact Schur-stability gate

Let $B_L$ be a source-derived boundary injection into the finite bulk with
$A_L\ge0$. The feedback term is uniformly controlled precisely when

\[
\sup_L\|A_L^{-1/2}B_L\|<\infty
\]

on the supported range. By the Douglas factorization criterion, this is
equivalent to one cutoff-independent constant $C$ satisfying

\[
B_LB_L^*\le C^2A_L
\]

for every cutoff.

For a scalar boundary row $b_L$, the same condition reads

\[
b_L^*A_L^{-1}b_L\le C^2.
\]

Hence every approximate blind mode $g_L$ with
$\langle g_L,A_Lg_L\rangle\to0$ must obey

\[
\|B_L^*g_L\|^2
\le
C^2\langle g_L,A_Lg_L\rangle
\longrightarrow0.
\]

This is the precise source requirement hidden by finite Schur inversion.
Finite invertibility of $A_L$ is insufficient.

The smallest falsifier is a sequence of normalized admissible states $g_L$
for which the bulk energy tends to zero while one labelled boundary
incidence remains nonzero. Such a sequence proves that the proposed
colligation has no completion-stable Schur return, even if all finite
determinants and first jets agree.

## The moving-window row fails the universal Fourier domination

On the ambient Gaussian rigging, the falsifier can be constructed explicitly.
Fix a negative Mellin height $t$ and put

\[
\xi_0=-\frac{t}{2\pi}>0.
\]

Choose widths $w_L=\sqrt L$ and normalized packets

\[
g_L(u)=c_L
\exp\left(-\frac{(u-L/2)^2}{2w_L^2}\right)e^{-itu}.
\]

Their position mass outside $(0,L)$ tends to zero. Their Fourier transforms
are Gaussian packets centered at $\xi_0$ with width proportional to
$w_L^{-1}$, so their Fourier mass outside $(0,L)$ also tends to zero.
Consequently

\[
\|K_Lg_L\|\longrightarrow1,
\qquad
\langle g_L,A_Lg_L\rangle\longrightarrow0.
\]

The Mellin seam row at the matching height is

\[
B_{L,t}(g)=\int_0^L g(u)e^{itu}\,du.
\]

For the chosen packets the phases cancel, and Gaussian integration gives

\[
|B_{L,t}(g_L)|\asymp w_L^{1/2}=L^{1/4}.
\]

Therefore no cutoff-independent constant can satisfy

\[
|B_{L,t}(g)|^2
\le
C^2\langle g,A_Lg\rangle
\]

on the ambient Gaussian packet class.

This closes the universal truncated-Fourier bulk as the common refinement
for the moving-seam incidence. The conclusion is carrier-specific: a smaller
arithmetic constructor module might exclude the packets $g_L$, but that
exclusion must be proved from its source operations. Declaring the smaller
carrier after seeing this falsifier would not supply authority.

## Dagger closure restores the hostile packets in Hilbert completion

The ordinary arithmetic module does not provide that exclusion once
reciprocal adjoints are admitted. Prime transport supplies translations by
$\log n$. Dagger supplies their inverses. Composition therefore supplies

\[
\log n-\log m=\log\frac nm.
\]

The set $\log\mathbb Q_{>0}$ is dense in $\mathbb R$. Since the translation
representation on logarithmic $L^2$ is strongly continuous, a closed subspace
invariant under these arithmetic translations and their adjoints is invariant
under every real translation.

The logarithmic theta Gaussian has a Fourier transform proportional to a
Gamma function with no real zeros. It is cyclic for the full translation
group. Hence the Hilbert closure of its dagger-closed arithmetic orbit is the
entire logarithmic $L^2$ carrier.

The phase-space packets used in the preceding falsifier therefore belong to
that Hilbert completion. They are not external hostiles once prime transport,
dagger, and ordinary Hilbert closure are all required.

Avoiding them requires a strictly finer constructor topology in which the
dense arithmetic translation group remains continuous but its completion is
not ordinary $L^2$. That topology must also support the sharp seam
correspondence and the primitive, square, and order-three determinant grades.
The Gaussian inductive rigging remains a candidate carrier, but the preceding
non-Fredholm correspondence problem must then be solved there rather than
evaded by a smaller Hilbert subspace.

## The discrete-to-continuous prime intertwiner loses dagger

The source supplies a canonical forward comparison between one discrete
$p$-valuation chain and the continuous tail. Let $L=\log p$, let
$Se_k=e_{k+1}$ on $\ell^2(\mathbb N_0)$, and define

\[
(J_pe_k)(u)=p^{-k/2}\Phi(u+kL).
\]

For the continuous left shift

\[
(C_Lf)(u)=f(u+L),
\]

the source weights give the exact forward intertwining law

\[
p^{-1/2}C_LJ_p=J_pS.
\]

This is the operator-level form of prime-scale recursion along one valuation
chain.

The comparison is not a Hilbert equivalence. Its column norms are

\[
\|J_pe_k\|^2
=
p^{-k}\int_{kL}^{\infty}|\Phi(v)|^2\,dv,
\]

and tend to zero. Thus $J_p$ is not bounded below on the labelled basis. Any
bounded realization has nonclosed range.

Consequently the forward intertwining law cannot be inverted to transport
adjoints. In particular, it does not imply a compatible relation between
$S^*$ and $C_L^*$. The discrete vacuum defect and the continuous interval
defect remain differently typed:

\[
I-SS^*=|e_0\rangle\langle e_0|,
\qquad
I-C_L^*C_L=P_L.
\]

The first has rank one; the second has infinite rank.

This is the exact obstruction to making the arithmetic-to-tail comparison a
dagger functor in ordinary Hilbert topology. Forward compositionality exists,
but source-tied reverse coherence does not descend through the collapsing
intertwiner.

A valid common refinement must therefore retain $J_p$ together with its
range topology and a separately typed boundary mate. Treating $J_p^{-1}$ as
bounded, or identifying the two defect projections after scalar pairing,
would erase the moving-seam modes.

## The source Gram satisfies an exact Stein identity

The collapsing intertwiner also supplies the canonical boundary mate. Put

\[
G_p=J_p^*J_p,
\qquad
A_p=p^{1/2}S,
\]

and let $R_L$ restrict a tail function to $(0,L)$. Define the full seam-window
observation

\[
B_p=R_LJ_p.
\]

Since $C_LJ_p=J_pA_p$, shifting both translated source columns by one
valuation step removes exactly their first interval. Entrywise,

\[
\left(G_p-A_p^*G_pA_p\right)_{k\ell}
=
p^{-(k+\ell)/2}
\int_0^L
\Phi(u+kL)\overline{\Phi(u+\ell L)}\,du.
\]

The right side is $(B_p^*B_p)_{k\ell}$. Hence

\[
G_p-A_p^*G_pA_p=B_p^*B_p.
\]

This is an exact observability Stein identity derived from the source
translation and the physical origin. It says that the failure of the
valuation shift to preserve the source Gram is exactly the moving-seam
energy.

In the $G_p$ topology, $A_p$ is contractive and $B_p$ is its defect
observation. Thus the forward arithmetic shift and its source-tied adjoint
coherence do meet, but only after replacing the standard labelled metric by
the source Gram.

The gain is not yet a Hilbert solution. The Gram is noncoercive on the full
labelled module because the columns of $J_p$ collapse. Completing only in
$G_p$ can erase persistent arithmetic predicates such as divisibility.
Therefore the honest object must retain both:

- the analytic observability Gram and its Stein law;
- the labelled constructor topology that preserves arithmetic type.

Their common completion is necessarily pro-valued or otherwise
multi-topological. A single equivalent Hilbert norm cannot carry both known
requirements.

## Transported windows give exact analytic observability

Iterating the Stein identity gives

\[
G_p-(A_p^*)^NG_pA_p^N
=
\sum_{j=0}^{N-1}
(A_p^*)^jB_p^*B_pA_p^j.
\]

For every finite labelled packet $c$, superexponential decay of the theta
source gives

\[
\|J_pA_p^Nc\|\longrightarrow0.
\]

Therefore

\[
\|J_pc\|^2
=
\sum_{j\ge0}\|B_pA_p^jc\|^2.
\]

The complete transported seam-window family is an exact isometric observer
for the analytic tail state. A fixed-origin window fails because it retains
only the $j=0$ term. Moving the observer with every valuation rung restores
all the energy that otherwise escapes toward infinity.

This is the clean control-theoretic content of the prime seam system:

- $A_p$ propagates the labelled valuation state;
- $B_p$ observes the newly exposed interval;
- the Stein identity is local energy balance;
- the infinite observation tower reconstructs the source Gram.

The theorem solves analytic observability on each prime orbit. It does not
solve arithmetic faithfulness. Two labelled packets can remain close in the
analytic Gram while differing under a non-descending predicate such as prime
divisibility. The constructor-generated pro-Gram topology is still required
to preserve those distinctions.

It also does not yet identify the observation-tower determinant with the
completed Euler--Evans section. That comparison must retain the order-three
anomaly and the archimedean boundary rather than taking the isometric
observability identity as a zero-confinement law.

## Several primes form a permutohedral observer, not a direct sum

For an ordered prime word

\[
w=(p_1,\ldots,p_r),
\qquad
L_j=\log p_j,
\]

put

\[
Q_0=0,
\qquad
Q_j=\sum_{i=1}^jL_i.
\]

Successive Stein defects observe the tagged interval pieces

\[
I_j(w)=[Q_{j-1},Q_j).
\]

Their disjoint union is the total moving seam

\[
\coprod_{j=1}^r I_j(w)=[0,\log n),
\qquad
n=\prod_{j=1}^rp_j.
\]

Changing the prime order changes the intermediate cut points and the tagged
interval decomposition, but not the final interval or composite label.
Adjacent swaps generate comparisons among all orderings. These comparisons
satisfy the involution, distant-commutation, and braid relations because they
are induced by rebracketing and reordering one common interval partition.

Thus the finite global observer has permutohedral coherence:

- vertices are ordered prime factorizations;
- edges are adjacent swaps;
- each vertex carries a transported seam-window decomposition;
- every completed path has the same total interval observer;
- intermediate tagged windows remain distinct and may not be scalar-summed
  before comparison.

This is the analytic counterpart of dependency-aware staged repair. The
shared $pq$ corner is the two-prime face. Its endpoint shadow is interval
concatenation, while its determinant shadow is the order-three anomaly cell.

The construction also explains why prime seam energies cannot be added as
independent positive ports. They are different decompositions of one seam
history. Positivity belongs to the complete partition Gram, with labels and
comparison cells retained.

Passing from ordered words to integer labels requires quotienting by these
permutohedral cells. Unique factorization identifies the terminal labelled
object, but the quotient is authorized only after the cells are shown to
preserve the source Gram, boundary charge, and determinant frame.

## An adjacent swap creates a ratio window

For two unequal primes, the adjacent-swap comparison is not a two-by-two
permutation of interval ports. Assume $L_p<L_q$. The order $(p,q)$ partitions
$[0,L_p+L_q)$ at $L_p$, while the order $(q,p)$ partitions it at $L_q$.
Their minimal common refinement has three pieces:

\[
[0,L_p),
\qquad
[L_p,L_q),
\qquad
[L_q,L_p+L_q).
\]

The two outer pieces have length $L_p$. The middle piece has length

\[
L_q-L_p=\log\frac qp.
\]

Reversing the order reverses the orientation of this middle comparison. Thus
the product label $pq$ controls the total interval, while the ratio $q/p$
controls the swap coherencer.

The ratio window is not a new integer-label state. It is a comparison stratum
created by taking the common refinement of two authorized product paths. This
recovers the earlier typing fact that product transport is internal to
integer labels while product--ratio quarter-turn is not.

A source supported in the middle interval gives the finite falsifier. Both
orders have the same total scalar window, but they assign that source content
to different tagged prime stages. Any comparison implemented only by endpoint
equality or a two-port permutation erases this distinction.

Therefore every nontrivial adjacent swap requires a three-piece refinement:
two transported witnesses and one signed ratio coherencer. Higher
permutohedral cells are assembled from these local refinements, with braid
coherence requiring the induced ratio windows to agree on their common
subdivision.

Construct a finite-place local packet with:

1. an additive source object;
2. its nonzero multiplicative trace;
3. a closed zero/valuation boundary object;
4. the admitted adjoint pairs among their incidence functors;
5. Fourier--Tate transport on the complete packet.

Then verify the two localization triangles and their compatibility with one
prime-valuation constructor. Only after this local gate passes should a
restricted product be formed.

The smallest falsifier is a local constructor that acts continuously on the
open trace but has no compatible action on the boundary unit or counit. Such
a failure proves that the proposed global restricted product has erased a
source distinction.

## Result

The local coherencer is the unit--counit structure of an open--closed
recollement together with the torus--Weyl reversal law. The finite two-prime
endpoint cocycle and determinant anomaly are already known exactly. The
remaining global constructor is a source-derived common refinement from the
noncompact seam defect algebra to the order-three filtered determinant
packet. It must preserve both shadows without regulator fitting and without
losing the finite-place valuation strata or the archimedean moment boundary.
