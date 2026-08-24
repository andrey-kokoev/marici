# The theta canonical-system target requires a typed accumulator defect

Status: exact target identity and no-go for naïve contour truncation; no RH
claim

Let

\[
 X(z)=\xi(1/2+iz),
 \qquad
 \mathcal D(z,w)=
 \frac{X'(z)\overline{X(w)}-X(z)\overline{X'(w)}}
 {\pi(\bar w-z)}.                                    \tag{1}
\]

## What a source canonical system must actually provide

A positive canonical realization must derive a carrier coordinate `r`, a
Hamiltonian

\[
 H(r)=H(r)^*\ge0,                                    \tag{2}
\]

and a two-component solution `Y(r,z)` of a canonical system, with a
`z`-independent admitted initial boundary condition, whose terminal value is

\[
 Y(L,z)=\binom{X(z)}{X'(z)}                            \tag{3}
\]

up to one fixed real symplectic change of basis.  The canonical Lagrange
identity must then read

\[
 \boxed{
 \frac{X'(z)\overline{X(w)}-X(z)\overline{X'(w)}}
 {\bar w-z}
 =\int_0^L Y(r,w)^*H(r)Y(r,z)\,dr.
 }                                                     \tag{4}
\]

Equation (4) is the typed version of “find a de Branges operator.”  It
specifies the source output, the positive bulk energy, and the exact kernel
that must be reproduced.  Abstract inverse realization after assuming
Hermite--Biehler positivity does not satisfy the direction of explanation.

## Naïve contour truncation is not canonical

The most direct attempted carrier is the fixed theta-contour coordinate.
On the half-line define partial transforms

\[
 X_r(z)=\int_0^r\Phi(u)\cos(zu)\,du,
 \qquad
 X'_r(z)=-\int_0^r u\Phi(u)\sin(zu)\,du.             \tag{5}
\]

Their `r`-evolution is exactly

\[
 \partial_rX_r=\Phi(r)\cos(zr),
 \qquad
 \partial_rX'_r=-r\Phi(r)\sin(zr).                  \tag{6}
\]

The right sides are local Fourier modes, not functions of the state
`(X_r,X'_r)`.  Therefore (6) is not a closed two-dimensional first-order
system.  More decisively, its spectral dependence is through `cos(zr)` and
`sin(zr)`, rather than affine multiplication by `z` against a
`z`-independent positive Hamiltonian.

Hence

\[
 \boxed{
 \text{truncating the theta contour does not produce the required
 two-dimensional canonical system.}
 }                                                     \tag{7}
\]

This is a structural typing failure, not a missing estimate.

## Minimal closure exposes the defect sector

The local Fourier modes close only after enlarging the state.  Put

\[
 c_r(z)=\cos(zr),\qquad s_r(z)=\sin(zr).
\]

Then

\[
 c'_r=-z s_r,qquad s'_r=z c_r,
 \qquad X'_r{}^{\!(r)}=-r\Phi(r)s_r,qquad
 X_r^{(r)}=\Phi(r)c_r.                                \tag{8}
\]

Here the superscript `(r)` denotes carrier differentiation, to distinguish
it from spectral differentiation.  This four-component triangular system
contains:

1. a conservative oscillatory transport sector `(c_r,s_r)`;
2. an accumulator sector `(X_r,X'_r)` driven by the theta source; and
3. no reverse coupling from the accumulator to the transport.

It is not yet a positive canonical system.  But it identifies the missing
typed object: the accumulator is a boundary defect sector.  A successful
completion must supply a source-fixed reverse/repair coupling so that the
four-component Green form descends to the positive two-component energy
(4).  Declaring the terminal pair positive after inspecting its zeros would
be an inadmissible spectral repair.

## Relation to the prime-two mechanism

The parallel is now precise rather than metaphorical:

\[
 \begin{array}{c|c}
 \text{prime-two level 44}&\text{theta de Branges target}\\ \hline
 \text{positive comparison bulk}&\text{oscillatory transport sector}\\
 \text{one unstable mode}&\text{driven accumulator defect}\\
 \text{source-fixed rank-one repair}&\text{missing reverse boundary map}.
 \end{array}                                           \tag{9}
\]

Nothing presently proves that the theta defect has finite rank after the
full continuum is included.  Finite-rank language must therefore remain a
conjecture until the Green form of (8) is computed and its negative index is
controlled.

## Next exact attack

Compute the conserved/produced symplectic form of the enlarged system (8).
The desired outcome is an identity

\[
 \text{terminal Bezoutian}
 =\text{positive bulk energy}+\text{boundary defect}. \tag{10}
\]

Then either:

- the defect is source-fixed and admits a positive quotient or finite-rank
  repair, giving a credible route to (4); or
- it has uncontrolled infinite negative index, falsifying the proposed
  transfer of the prime-two mechanism.

This computation, not an abstract canonical-system existence theorem, is
the next informative move.

## The enlarged triangular closure still fails the canonical Green typing

The preceding computation can be done exactly.  Order the state as

\[
 q=(c,s,a,b)^T=(c_r,s_r,X_r,X'_r)^T
\]

and write

\[
 q'=(M_0(r)+zM_1)q,                                   \tag{11}
\]

where

\[
 M_1=
 \begin{pmatrix}
 0&-1&0&0\\1&0&0&0\\0&0&0&0\\0&0&0&0
 \end{pmatrix},
\qquad
 M_0=
 \begin{pmatrix}
 0&0&0&0\\0&0&0&0\\
 \Phi&0&0&0\\0&-r\Phi&0&0
 \end{pmatrix}.                                      \tag{12}
\]

At a finite terminal cutoff `L`, the Bezoutian is selected by the two-form
`da wedge db`.  Transport this form backward through the `z=0` evolution.
Put

\[
 C(r)=\int_r^L\Phi(t)\,dt,
 \qquad
 D(r)=\int_r^L t\Phi(t)\,dt.                          \tag{13}
\]

Since terminal accumulators are `a_L=a_r+C(r)c_r` and
`b_L=b_r-D(r)s_r`, the transported two-form is

\[
 G(r)=d(a+Cc)\wedge d(b-Ds)
 =da\wedge db-D\,da\wedge ds+C\,dc\wedge db-CD\,dc\wedge ds. \tag{14}
\]

It solves the zero-order transport equation

\[
 G'+M_0^TG+GM_0=0.                                   \tag{15}
\]

For a canonical Lagrange identity, the spectral part must additionally obey

\[
 M_1^TG=H,qquad GM_1=-H                              \tag{16}
\]

for one Hermitian positive Hamiltonian `H`.  In particular it is necessary
that

\[
 M_1^TG+GM_1=0.                                      \tag{17}
\]

Direct substitution of (14) gives nonzero cross entries

\[
 (M_1^TG+GM_1)_{ca}=D,qquad
 (M_1^TG+GM_1)_{sb}=-C,                               \tag{18}
\]

with their skew counterparts.  Because `Phi>0`, both `C(r)` and `D(r)` are
strictly positive before the terminal endpoint.  Therefore (17) fails
throughout the bulk.

This proves the stronger no-go

\[
 \boxed{
 \text{the minimal four-state transport--accumulator closure cannot be
 made canonical merely by transporting its terminal Green form.}
 }                                                     \tag{19}
\]

The obstruction is exactly typed by the zeroth and first theta tails `C,D`.
Any repair must add reverse coupling or extra states whose spectral Green
variation cancels both entries in (18).  One scalar rank-one correction is
generically insufficient: there are already two independent tail channels.

The revised constructive question is now finite and explicit: find the
smallest source-derived extension of (12) whose transported two-form is
preserved by its spectral matrix and whose resulting Hamiltonian is
nonnegative.  Failure for every finite extension would force the program
toward an infinite-dimensional boundary quotient rather than a finite-defect
canonical system.

## Rank-four defect forces two repair pairs

The failure in (18) is the two-form

\[
 \Omega_{\rm def}
 =D(r)\,dc\wedge da-C(r)\,ds\wedge db.                \tag{20}
\]

For every interior `r`, positivity of `Phi` gives `C(r),D(r)>0`.  The two
summands occupy disjoint coordinate planes, so

\[
 \operatorname{rank}\Omega_{\rm def}=4.              \tag{21}
\]

A correction supplied by one ordinary auxiliary symplectic pair is a
decomposable two-form `dp wedge dq`, whose rank is at most two after pullback
to the core.  It cannot cancel (20).  Consequently, within the class of
extensions that preserve the four-state transport--accumulator core and add
canonical repair channels,

\[
 \boxed{
 \text{at least two auxiliary symplectic pairs are required.}
 }                                                     \tag{22}
\]

Thus the first admissible finite candidate has dimension eight, not six:

\[
 (c,s,a,b)\oplus(p_0,q_0)\oplus(p_1,q_1).             \tag{23}
\]

The subscripts have a source meaning.  The first pair must cancel the
zeroth-tail channel `C=int Phi`; the second must cancel the first-tail channel
`D=int t Phi`.  Combining them into an untyped rank-one repair would erase
the even/odd distinction that produced the terminal pair `(X,X')`.

This lower bound is conditional only on preserving the core and using
ordinary symplectic repair pairs.  A construction that changes the core
spectral action, uses an indefinite quotient, or introduces a genuinely
infinite-dimensional boundary is outside its scope.

## The two defect weights are coherently related

Although the two-form has rank four, its coefficients are not arbitrary.
Their ratio

\[
 m(r)=\frac{D(r)}{C(r)}                                \tag{24}
\]

is the conditional mean of the remaining theta coordinate under the tail
measure.  Differentiation gives

\[
 m'(r)=
 \frac{\Phi(r)}{C(r)^2}\left(D(r)-rC(r)\right)>0,     \tag{25}
\]

because

\[
 D(r)-rC(r)=\int_r^L(t-r)\Phi(t)\,dt>0.              \tag{26}
\]

Hence the repair geometry is controlled by one positive scale `C(r)` and one
strictly increasing conditional mean `m(r)>r`.  This monotone-likelihood
structure is the first extra source information unavailable in an arbitrary
rank-four defect.

The next construction should exploit this relation: normalize the two repair
pairs by `sqrt(C)` and `sqrt(D)`, compute the connection terms generated by
their `r`-dependence, and test whether monotonicity (25) makes the completed
Hamiltonian positive.  If the connection introduces a new uncancelled moment,
the defect hierarchy continues to `int t^2 Phi`, signaling that no finite
moment closure is possible.

## Crossed repair yields a positive spectral Hamiltonian

The required repair pairs are crossed by parity.  The spectral defect (20)
is cancelled on the source-fixed graph by adjoining pair forms whose pullback
is

\[
 \Omega_{\rm rep}
 =-C\,dc\wedge db-D\,ds\wedge da.                    \tag{27}
\]

Equivalently, use scaled graph coordinates built from
`(sqrt(C)c,sqrt(C)b)` and `(sqrt(D)s,sqrt(D)a)`, with the orientations shown
in (27).  Adding (27) to the transported terminal form (14) cancels its two
cross terms and leaves

\[
 \boxed{
 G_{\rm red}=da\wedge db-CD\,dc\wedge ds.
 }                                                     \tag{28}
\]

Let `R=[[0,-1],[1,0]]` be the spectral rotation on `(c,s)`.  The reduced form
is spectrally invariant,

\[
 R^TG_{\rm red}+G_{\rm red}R=0,                       \tag{29}
\]

and the coefficient of `bar(w)-z` in its Lagrange identity is

\[
 \boxed{
 H_{\rm cand}=CD
 \begin{pmatrix}1&0\\0&1\end{pmatrix}
 }                                                     \tag{30}
\]

on the oscillatory sector.  Since `C,D>0`, this candidate bulk Hamiltonian is
strictly positive.  This is the first point at which the theta-tail repair
produces the correct sign without assuming a zero configuration.

## The repair-frame connection leaves a rank-four obstruction

Spectral typing is not enough.  The reduced Green form must also be preserved
by the zero-order source evolution.  Using

\[
 C'=-\Phi,\qquad D'=-r\Phi                             \tag{31}
\]

and the accumulator equations in (8), direct differentiation gives the
residual connection two-form

\[
 \boxed{
 \Omega_{0}=\Phi\left[
 (Cr+D)\,dc\wedge ds
 +dc\wedge db
 +r\,ds\wedge da
 \right].
 }                                                     \tag{32}
\]

Thus the desired identity currently has the form

\[
 \text{terminal Bezoutian}
 =\int CD\,(c_w^*c_z+s_w^*s_z)\,dr
 +\int\Omega_0(q_w,q_z)\,dr.                          \tag{33}
\]

The first term is a genuine positive bulk energy.  The second is neither a
boundary scalar nor manifestly positive.  For `r>0`, its skew matrix has
Pfaffian proportional to `Phi^2 r`, so

\[
 \operatorname{rank}\Omega_0=4.                      \tag{34}
\]

The eight-state repair therefore does not prove kernel positivity.  It moves
all spectral indefiniteness into an explicit zero-order connection defect.
No second theta moment appears: the defect still closes on `Phi,C,D,r`.

This is a substantially narrower next gate.  Seek a source-fixed reverse
connection whose contribution is `-Omega_0` while leaving the positive
Hamiltonian (30) unchanged.  If such a connection exists and preserves the
terminal accumulator pair, the canonical-system construction closes.  If
every cancellation of (32) destroys (30) or changes `(X,X')`, the finite
repair program is falsified at dimension eight.

## Every eight-state reverse connection is terminal-singular

Because `G_red` is nondegenerate in the interior, a formal correction always
exists.  One canonical choice is

\[
 \Delta M_0=-\frac12G_{\rm red}^{-1}\Omega_0,         \tag{35}
\]

which satisfies

\[
 \Delta M_0^TG_{\rm red}+G_{\rm red}\Delta M_0
 =-\Omega_0.                                         \tag{36}
\]

In the ordered core `(c,s,a,b)`, it is

\[
 \Delta M_0=
 \begin{pmatrix}
 \frac{\Phi(Cr+D)}{2CD}&0&-\frac{\Phi r}{2CD}&0\\
 0&\frac{\Phi(Cr+D)}{2CD}&0&\frac{\Phi}{2CD}\\
 -\frac\Phi2&0&0&0\\
 0&\frac{\Phi r}{2}&0&0
 \end{pmatrix}.                                      \tag{37}
\]

This particular correction already changes the oscillator and accumulator
equations, so it does not preserve the original partial theta transform.
More importantly, its singularity cannot be removed by choosing another
solution of (36).  Any two solutions differ by a `G_red`-skew connection
`K`, satisfying

\[
 K^TG_{\rm red}+G_{\rm red}K=0.
\]

Such a symplectic Lie-algebra element has zero trace.  Hence every solution
of (36) has the invariant trace

\[
 \boxed{
 \operatorname{tr}\Delta M_0
 =\frac{\Phi(Cr+D)}{CD}.
 }                                                     \tag{38}
\]

At a finite terminal cutoff `L`, with `delta=L-r`,

\[
 C(r)=\Phi(L)\delta+O(\delta^2),
 \qquad
 D(r)=L\Phi(L)\delta+O(\delta^2),                    \tag{39}
\]

and therefore

\[
 \boxed{
 \operatorname{tr}\Delta M_0
 =\frac2{L-r}+O(1).
 }                                                     \tag{40}
\]

The logarithmically nonintegrable volume expansion occurs exactly at the
boundary where the auxiliary tail coordinates collapse and the terminal pair
must become `(X,X')`.  It is invariant under all admissible Green-skew gauge
changes.

Consequently

\[
 \boxed{
 \text{the minimal two-pair/eight-state repair has no regular terminal
 canonical connection preserving the theta accumulator boundary.}
 }                                                     \tag{41}
\]

This falsifies the finite repair at its first admissible dimension.  A larger
finite system would have to keep a nondegenerate repair metric at the
terminal boundary rather than scaling every auxiliary channel by vanishing
tails.  The more natural alternative is now an infinite-dimensional relative
boundary space in which the tail is retained as a function, not compressed
to `C` and `D`.

## No-go for every finitely tail-scaled repair

The terminal pole is not special to the first two moments.  Let a finite
repair channel be normalized by any positive tail weight

\[
 h_f(r)=\int_r^L f(t)\Phi(t)\,dt,                     \tag{42}
\]

where `f` is continuous and `f(L)Phi(L)>0`.  Then

\[
 h_f(r)=f(L)\Phi(L)(L-r)+O((L-r)^2),                  \tag{43}
\]

and its normalized frame carries the logarithmic connection

\[
 -\frac12\frac{h_f'(r)}{h_f(r)}
 =\frac1{2(L-r)}+O(1).                                \tag{44}
\]

For finitely many positive repair pairs, these volume contributions add.
A regular bounded change of frame changes the connection trace only by the
derivative of a bounded nonvanishing determinant and cannot remove the
logarithmic pole.  Therefore, in the class where auxiliary positive metrics
are built from finitely many vanishing theta-tail integrals,

\[
 \boxed{
 \text{every finite-dimensional normalized repair is terminal-singular.}
 }                                                     \tag{45}
\]

This statement does not exclude a finite system with a source-derived metric
that remains nondegenerate at the boundary, nor a singular canonical system
whose endpoint is admitted by a separate limit theorem.  It does exclude the
obvious strategy of adding successively more tail moments: each new moment
adds another copy of the same logarithmic collapse.

## Faithful infinite tail Carrier

The noncollapsing source object is the moving Hilbert fiber

\[
 \mathcal H_r=L^2([r,L],\Phi(t)dt).                   \tag{46}
\]

Restriction from `H_r` to `H_s`, `r<s`, is canonical and retains every tail
label.  Its norm loss is the positive shell identity

\[
 \|f\|_{\mathcal H_r}^2-\|f\|_{\mathcal H_s}^2
 =\int_r^s|f(t)|^2\Phi(t)\,dt\ge0.                   \tag{47}
\]

The theta accumulators are continuous readouts of the coherent functions
`cos(zt)` and `-t sin(zt)` from this fiber.  No division by a vanishing tail
mass is needed.  Equation (47) is therefore the correct positive comparison
bulk suggested by the finite calculation.

But multiplication by `t` on this fiber has the continuous source-coordinate
spectrum, not the Riemann-zero spectrum.  The infinite tail Carrier alone is
not a Hilbert--Polya operator.  The remaining nonlinear operation is a
relative boundary quotient whose Weyl function is exactly

\[
 -X'(z)/X(z).                                         \tag{48}
\]

The revised target is consequently precise:

1. construct a boundary trace on the restriction system (46)--(47);
2. prove that its Green quotient has terminal determinant `X` and Weyl
   function (48);
3. show that the quotient energy is positive without extracting zero data.

This is where an infinite-dimensional de Branges or boundary-triple
construction could add content.  Merely using the self-adjoint multiplication
operator on (46) would reproduce the theta coordinate and miss divisor
extraction.
