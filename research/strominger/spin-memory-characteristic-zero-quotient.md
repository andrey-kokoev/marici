# Characteristic-zero spin-memory quotient

## Fourier-block explanation

After the nine-longitude Fourier transform, two dark latitude rings act
independently in each azimuthal character. For \(|m|=0,1,2,3,4\), the ranks
of the two-latitude evaluation blocks are

\[
(2,2,2,2,1).
\]

The multiplicity convention doubles every \(|m|>0\) block, giving

\[
2+2(2+2+2+1)=16.
\]

The corresponding nullities are

\[
(1,1,1,0,0).
\]

Therefore the five-dimensional quotient is canonically carried by

\[
m=-2,-1,0,1,2.
\]

It is not an accidental modular basis. It is the complete set of low
azimuthal characters left after two independent radial conditions consume
two of the three degree coordinates available for \(|m|\leq2\).

## Source of the two redundancies

For \(|m|=4\), only degree \(l=4\) is admitted. Its radial coefficient space
is one-dimensional. Two latitude observations of that same coefficient have
rank one, not two. The duplicated loss occurs once for \(m=4\) and once for
\(m=-4\).

Thus the two redundant observations have a precise representation-theoretic
source:

\[
18\text{ nominal rows}-2\text{ repeated }m=\pm4\text{ observations}
=16\text{ independent constraints}.
\]

## Canonical quotient generators

For a dark pair \(x_a,x_b\) and \(|m|\leq2\), define

\[
Q_m^{a,b}(z)=
\det\begin{pmatrix}
P_2^m(z)&P_3^m(z)&P_4^m(z)\\
P_2^m(x_a)&P_3^m(x_a)&P_4^m(x_a)\\
P_2^m(x_b)&P_3^m(x_b)&P_4^m(x_b)
\end{pmatrix}.
\]

Then the quotient is spanned by

\[
Q_{|m|}^{a,b}(z)e^{im\phi},
\qquad -2\leq m\leq2.
\]

This gives a characteristic-zero constructor for the five coordinates. The
finite-field computation is needed only for the exact continuation-distance
certificate, not for the quotient's existence or interpretation.

Every generator further factorizes as

\[
Q_m^{a,b}(z)=
(z-x_a)(z-x_b)(1-z^2)^{|m|/2}R_m^{a,b}(z),
\]

where

\[
\deg R_m^{a,b}=2-|m|,
\qquad |m|=0,1,2.
\]

The residual radial degrees are therefore \(2,1,0\). This is the usual
spin-two degree staircase. The quotient is not five unrelated coordinates:
it is one effective spin-two packet after the two prescribed radial zeros
have been factored out. Its three remaining latitude readouts are diagonal
transports of the same five azimuthal coordinates.

After normalizing one surviving ring, every other ring acts diagonally on
\(|m|=0,1,2\). Its three multipliers interpolate a unique quadratic

\[
T_{a,b;r}(m^2),
\qquad m^2\in\{0,1,4\}.
\]

Thus the continuation is a polynomial transfer law in the spin Casimir, not
an arbitrary five-by-five matrix. Distance 16 occurs exactly when one such
transfer is singular at \(m^2=1\). The surviving \(m=\pm1\) packet then makes
the corresponding third ring completely dark. This happens precisely when
the original pair extends to \(\{0,2,4\}\) or \(\{1,2,3\}\).

## Exact distance law

The pairwise characteristic-zero continuation distances are

\[
d_{a,b}=
\begin{cases}
16,&\{a,b\}\subseteq\{0,2,4\}\text{ or }\{a,b\}\subseteq\{1,2,3\},\\
22,&\text{otherwise}.
\end{cases}
\]

The six singular-transfer pairs attain 16 through the three-dark-ring
\(m=\pm1\) packet. For each nonsingular reflection orbit, three consecutive
longitudes on one ring together with the middle longitude on both other
rings give five zeros. The corresponding five-by-five Laurent determinant
vanishes identically in the longitude parameter. This is stronger than the
original observation that it vanishes modulo
\(\Phi_9(t)=t^6+t^3+1\): the witness is geometric rather than a ninth-root
accident. Hence those words have support 22 at \(N=9\). Exact reduction at
the good prime 991 excludes six zeros, so the upper witnesses are optimal.

The identity has a coordinate-free explanation. Center the three consecutive
longitudes at \(j\). The sum of the two outer observation rows multiplies the
\(m\)-th quotient character, relative to the middle row, by

\[
u^m+u^{-m}.
\]

This multiplier depends only on \(|m|\). The three surviving ring rows at
longitude \(j\) span all functions on
\(|m|\in\{0,1,2\}\), because the regular radial transfer is nonsingular.
Consequently the symmetric outer-row sum lies in their span. The five rows
are dependent for every nonzero longitude parameter \(u\). Reflection and
three-point radial interpolation, rather than cyclotomy, force the cocircuit.

## Odd-longitude counterfactual

Keep the five latitude transports and the effective spin-two quotient fixed,
and replace nine longitudes by an odd number \(N\). The universal five-zero
dependence gives

\[
d_{\mathrm{regular}}(N)\leq 3N-5.
\]

On a singular transfer pair, the pure \(m=\pm1\) packet kills a third ring
and has one zero on each of the two live rings when \(N\) is odd. Therefore

\[
d_{\mathrm{singular}}(N)=2N-2.
\]

Exhaustive maximal-row-subset searches for every latitude pair at
\(N=11,13\), together with representative searches at \(N=9,15\), find

\[
d_{\mathrm{regular}}(N)=3N-5,
\qquad
d_{\mathrm{singular}}(N)=2N-2.
\]

Only the singular equality and the regular upper bound are presently proved
uniformly in odd \(N\). The regular lower bound remains bounded evidence: an
unbounded proof must exclude a sixth root-of-unity zero without assuming the
finite-field certificate at \(N=9\).

## Hidden antipodal boundary

Factoring the canonical five-zero word reveals more continuous zeros than
the discrete count reports. If its three consecutive first-ring roots are
\(1,u,u^2\), then its first-ring polynomial is proportional to

\[
(x-1)(x-u)(x-u^2)(x+u).
\]

Both other ring polynomials are divisible by

\[
x^2-u^2.
\]

Thus \(x=-u\) is a zero on all three rings. An odd longitude grid excludes
this antipode, while an even grid admits it. The parity hypothesis is
therefore an anti-aliasing condition, not bookkeeping.

The residual quadratic roots also fail to add sampled zeros for odd \(N\).
In the first regular reflection orbit, one residual equation has the form

\[
9(y+y^{-1})=2\sqrt2\,(u+u^{-1}).
\]

If \(u\) and \(y\) both have odd order, their cyclotomic field cannot contain
\(\sqrt2\), whose conductor is \(8\); the zero-trace alternative would force
order four. The other residual equation is excluded at a prime above \(3\):
it would make the reduction of an odd-order root satisfy \(u^2=-1\).

For the second regular orbit, write

\[
s=u+u^{-1},\qquad t=y+y^{-1}.
\]

Separating the rational and \(\sqrt2\) components of either residual
quadratic and eliminating \(t\) gives

\[
s(7417s^2+24740s+18844)=0.
\]

The first branch again forces order four. The quadratic has one root outside
\([-2,2]\); its other root is an irrational element of
\(\mathbb Q(\sqrt2)\), which cannot lie in an odd cyclotomic field. Hence the
canonical cocircuit has exactly five sampled zeros for every odd \(N\).

This does not yet prove the full regular lower bound: a hypothetical
six-zero word need not contain the canonical three-one-one incidence
pattern. The remaining theorem is to classify all six-row incidence
partitions and reduce each to the same odd-cyclotomic obstruction.

## Congruence-controlled competing cocircuits

The antipodal factor predicts a different upper witness on even grids. The
canonical word has eight sampled zeros there: four on its first ring and two
on each other ring. Independently, a pure \(m=\pm2\) word has
\(\gcd(4,N)\) zeros on each of the three live rings. On a singular transfer,
a pure \(m=\pm1\) word kills one ring and has \(\gcd(2,N)\) zeros on each
remaining ring.

These mechanisms predict

\[
d_{\mathrm{regular}}(N)\leq
\begin{cases}
3N-5,&N\text{ odd},\\
3N-8,&N\equiv2\pmod4,\\
3N-12,&4\mid N,
\end{cases}
\]

and

\[
d_{\mathrm{singular}}(N)
=2\bigl(N-\gcd(2,N)\bigr).
\]

Exhaustive searches at \(N=8,10,12,14\) attain these bounds exactly. Combined
with the odd searches through \(N=21\), the evidence says that minimum
distance is selected by the largest admissible cocircuit among:

- the reflection-generated five-zero word;
- its even-grid antipodal completion;
- the pure-character torsion words.

The modulus of \(N\) controls which continuous zeros become executable
sample points. This is a finite-group constructor effect, not a change in
the transported spin-two object.

## Odd-grid circuit atlas

The reflection construction is not limited to adjacent longitudes. Fix a
center \(j\) and nonzero displacement \(d\) in \(\mathbb Z/N\mathbb Z\).
Three observations on one ring at

\[
j-d,\quad j,\quad j+d
\]

together with the observation at \(j\) on each other ring form a dependent
five-row set. Indeed, relative to the center, the sum of the outer rows
multiplies character \(m\) by

\[
u^{dm}+u^{-dm},
\]

which depends only on \(|m|\) and is therefore reconstructed by the three
centered radial observations.

When \(N\) is odd, \(d\) and \(-d\) describe the same circuit and every
unordered outer pair has a unique center. The predicted circuit count is

\[
3N\frac{N-1}{2}.
\]

Complete numerical row-matroid enumeration in both regular reflection
orbits gives:

\[
\begin{array}{c|c|c}
N&\text{dependent five-row sets}&\text{predicted count}\\
\hline
9&108&108\\
11&165&165\\
13&234&234
\end{array}
\]

Every dependency has incidence \((3,1,1)\), every triple is
reflection-centered, and every rank-four circuit has closure of size exactly
five. Thus no enumerated circuit admits a sixth observation.

This suggests the invariant formulation of the remaining theorem:

> On a regular odd grid, the rank-four circuits of the observation matroid
> are exactly the reflection-centered \((3,1,1)\) circuits, and each is a
> closed flat.

The construction and closure of the displayed circuits now have uniform
proofs. Exhaustiveness remains to be proved. In coding language, the
three-block spin-two evaluation code is maximally recoverable after
quotienting by precisely these source-forced local reflection parities.

## Torsion-point reduction

The generic five-row determinant over unconstrained complex longitude
variables does not vanish only on the reflection-centered family. It defines
a larger algebraic hypersurface. Therefore ordinary determinant
factorization or real total positivity cannot prove circuit exhaustiveness.

The sampling constructor imposes the missing condition: every longitude is
a torsion point of \(\mathbb G_m\). For each incidence partition, normalize
one longitude by global rotation and form the corresponding maximal minor
as a Laurent polynomial over

\[
K=\mathbb Q(\sqrt2,\sqrt5).
\]

The unbounded problem is then:

1. classify the torsion cosets contained in each minor hypersurface;
2. intersect the coset lists for all minors required by a rank-four
   six-row set;
3. retain only odd-order torsion points;
4. prove that the surviving positive-dimensional cosets are exactly
   \[
   (j-d,j,j+d;\,j;\,j);
   \]
5. exclude sporadic odd-torsion intersections.

This separates three levels that a raw determinant census conflates:

\[
\text{continuous algebraic dependency}
\supset
\text{torsion dependency}
\supset
\text{odd-grid executable dependency}.
\]

The hidden antipodal zero belongs to the torsion dependency but drops out of
the odd executable locus. The \(\sqrt2\)-field separation and the
prime-above-\(3\) argument are the first local exclusions of sporadic
odd-torsion points.

A practical exact proof can proceed incidence type by incidence type. After
global-rotation normalization, compute the Laurent supports, enumerate
vanishing subsums under root-of-unity specialization, and use the exponent
difference lattice to recover maximal torsion cosets. Any residual
zero-dimensional solutions must then be checked through their cyclotomic
minimal polynomials. This is finite for the fixed five-column spin-two
packet, even though \(N\) is unbounded.

There is a useful conductor split before any torsion-coset enumeration. For
odd \(N\), the longitude field cannot contain \(\sqrt2\), whose conductor is
\(8\). Writing a minor as

\[
\Delta=A+\sqrt2\,B
\]

over the odd cyclotomic field enlarged, when necessary, by \(\sqrt5\),
odd-torsion vanishing forces

\[
A=B=0.
\]

Thus one continuous determinant hypersurface becomes a codimension-two
intersection on the executable locus. When \(5\nmid N\), \(\sqrt5\) is also
disjoint and the determinant splits into four rational component equations.
The case \(5\mid N\) is the only odd-conductor sector in which the
\(\sqrt5\) coefficient field can be internal to the longitude field; it
must be audited separately rather than treated as generic.

This field-disjointness supplies a plausible source for the observed
rigidity. It also yields a finite proof architecture:

- generic odd conductor, split both quadratic generators;
- conductor divisible by \(5\), split only \(\sqrt2\);
- enumerate torsion cosets in the resulting simultaneous component ideals;
- check the finite residual conductor list exactly.

## First incidence elimination: four plus one

Five observations on one ring are independent whenever their longitudes are
distinct: after nonzero row and column scalings, their minor is the ordinary
five-point Vandermonde determinant.

For four observations on a base ring and one on a target ring, divide every
base longitude by the target longitude and let \(E_k\) be the elementary
symmetric functions of the four resulting roots. The dependency equation is

\[
t_2(1+E_4)-t_1(E_1+E_3)+t_0E_2=0,
\]

where \(t_0,t_1,t_2\) are the target-to-base transfer multipliers for
\(|m|=0,1,2\).

Whenever the radical in \(t_1\) is disjoint from the odd cyclotomic field,
its component vanishes separately:

\[
E_1+E_3=0.
\]

The remaining rational component is

\[
1+E_4+\frac{t_0}{t_2}E_2=0.
\]

Across all directed ring pairs in the two regular reflection orbits, the
reduced ratios \(t_0/t_2\) are

\[
\frac{39}{28},\quad\frac{39}{55},\quad
\frac{28}{39},\quad\frac{28}{55},\quad
\frac{55}{39},\quad\frac{55}{28}.
\]

For each ratio, an odd prime among \(7,11,13\) divides its numerator but not
its denominator. Reduction at that prime forces

\[
1+E_4=0.
\]

But \(E_4\) is a product of odd-order roots of unity. Its reduction away from
the chosen coefficient denominator still has odd order, so it cannot equal
\(-1\). This excludes the four-plus-one circuit.

Of the twelve directed ring pairs, eight have a \(\sqrt2\)-bearing middle
transfer and close by field separation. Two \(\sqrt5\)-internal reverse
directions close immediately at the prime above \(5\). Clearing denominators
in the remaining two forward directions gives

\[
495A+121\sqrt5\,B+351C=0
\]

and

\[
165A-121\sqrt5\,B+117C=0,
\]

where

\[
A=1+E_4,\qquad B=E_1+E_3,\qquad C=E_2.
\]

Both equations imply

\[
C\in11\mathcal O_K.
\]

This uses divisibility by the full integer ideal \(11\mathcal O_K\), so no
unramified-conductor assumption is needed. If \(C\neq0\), then with
\(d=[K:\mathbb Q]\),

\[
11^d\leq |\operatorname{Norm}(C)|\leq6^d,
\]

because every conjugate of \(C\) is a sum of six unit-modulus terms. This is
impossible, hence \(C=0\).

In the first equation, the remaining coefficients force

\[
B\in9\mathcal O_K.
\]

Every conjugate of \(B\) has magnitude at most \(8\), so the same norm
argument gives \(B=0\). The equation then gives \(A=0\).

In the second equation, after \(C=0\), division by \(11\) gives

\[
15A=11\sqrt5\,B.
\]

Since \(15\) is coprime to \(11\), this forces
\(A\in11\mathcal O_K\). But every conjugate of \(A\) has magnitude at most
\(2\), so \(A=0\).

Both residual directions therefore imply

\[
1+E_4=0.
\]

The product \(E_4\) has odd order and cannot equal \(-1\). Thus no
four-plus-one dependency exists for any odd \(N\). The earlier bounded
search through \(N=65\) is retained only as discovery evidence; the
full-ideal norm argument supplies the unbounded exclusion.

## Second incidence reduction: three plus two

Let the three base-ring roots have elementary symmetric functions

\[
A=a+b+c,\qquad B=ab+ac+bc,\qquad C=abc.
\]

They leave the polynomial pencil

\[
F(x)(\alpha x+\beta),
\qquad
F(x)=x^3-Ax^2+Bx-C.
\]

After a target transfer with multipliers \(t_0,t_1,t_2\), a basis for the
transferred pencil is

\[
Q_0(x)=-t_2C+t_1Bx-t_0Ax^2+t_1x^3,
\]

\[
Q_1(x)=-t_1Cx+t_0Bx^2-t_1Ax^3+t_2x^4.
\]

For distinct target roots \(p,q\), dependency is equivalent to

\[
\mathcal R_{3,2}
=\frac{Q_0(p)Q_1(q)-Q_0(q)Q_1(p)}{p-q}=0.
\]

This formula is quadratic in the middle transfer \(t_1\). Its terms of even
\(t_1\)-degree are divisible by \(p+q\); the odd component is nonzero. Since
\(p+q=0\) would make \(p/q=-1\), the even antipodal branch is unavailable on
an odd grid.

For transfers whose \(t_1\) carries a quadratic radical disjoint from the
longitude field, the equation therefore splits into simultaneous even and
odd residual equations. Unlike the four-plus-one case, the radical also
appears through \(t_1^2\), so the even equation retains a genuine rational
term. This is the first coupled torsion ideal rather than a single
full-ideal norm obstruction.

The next exact task is to normalize \(pq=1\) using the unique odd-grid square
root of the target product, impose the unit-circle identities

\[
B=C\overline A,\qquad p+q\in\mathbb R,
\]

and eliminate the odd component from the even one. The desired output is
either the reflection-centered \((3,1,1)\) coset or an explicit weighted
vanishing sum whose coefficient norm exceeds its conjugate bound.

After setting

\[
r=\frac{t_0}{t_2},
\qquad
s=\left(\frac{t_1}{t_2}\right)^2,
\]

the twelve directed transfers collapse to ten rational \((r,s)\) classes.
Direction reversal sends

\[
(r,s)\longmapsto(r^{-1},s^{-1}),
\]

so only five undirected classes remain.

Let \(W=(p+q)^2\) after normalizing \(pq=1\). The odd and even equations are
linear in \(W\). Eliminating it gives the target-independent trace
resultant

\[
\mathcal H_{r,s}
=(AC+B)\bigl((1+s-r)C-sAB\bigr)
+(C^2+1)(C-rAB).
\]

Using \(B=C\overline A\) and dividing by \(C^2\), this becomes

\[
(A+\overline A)\bigl(1+s-r-s|A|^2\bigr)
+(C+\overline C)\bigl(1-r|A|^2\bigr)=0.
\]

Thus any three-plus-two circuit must first place its base triple on one of
five rational trace hypersurfaces; only then can the eliminated target
separation be reconstructed. Random continuous triples meet every
hypersurface, so no fixed-sign argument is available. The outstanding
statement is again torsion-specific: prove that none of these five trace
hypersurfaces contains an executable odd-torsion base triple compatible
with the reconstructed target pair.

The reconstructed separation is

\[
W
=2-\frac{r(A+BC)+s(AB-C)}{C}.
\]

Continuous solutions of the trace resultant occur with \(0\leq W\leq4\) in
every transfer class, so the unit-circle interval supplies no analytic
exclusion. A direct determinant search, retaining the unsplit quadratic
radicals, finds no three-plus-two circuit on the tested odd grids through
\(N=121\). Near-collisions reach approximately \(5\times10^{-9}\), and
high-precision replay confirms that they are nonzero. As in the previous
stratum, numerical separation deteriorates while exact torsion
nonintersection persists.

## Deutsch counterfactual: a constructible bad transfer

Invert the normalized residual equations rather than testing only the
physical transfer points. Every torsion base triple and target pair proposes
the transfer

\[
r=-\frac{Y}{X},
\qquad
s=-\frac{rP+Q}{R},
\]

provided the displayed denominators are nonzero. Searching for simple
rational images produces an exact counterexample at

\[
(r,s)=(1,2).
\]

Let \(\zeta=\zeta_7\) and take the base triple

\[
\zeta,\quad\zeta^2,\quad\zeta^4.
\]

Its elementary data satisfy the quadratic-period identities

\[
A+\overline A=-1,\qquad
A\overline A=2,\qquad
C=1.
\]

Take the target pair to be the two nontrivial cube roots

\[
\omega,\quad\omega^2.
\]

Then

\[
U=\omega+\omega^2=-1,\qquad W=U^2=1.
\]

For \(r=1,s=2\), the normalized odd and even residuals both vanish:

\[
rX+Y=0,
\qquad
rP+Q+sR=0.
\]

Embedding the seventh and third roots into the twenty-first roots gives the
explicit incidence

\[
\text{base exponents }(3,6,12),
\qquad
\text{target exponents }(7,14)
\pmod {21}.
\]

Equivalently, the transfer

\[
t_0=t_2,\qquad t_1^2=2t_2^2
\]

has a genuine three-plus-two circuit. Therefore odd sampling and the
spin-two character set do not by themselves forbid interior circuits. The
physical theorem must use the source-derived radial transfer coefficients.

Among simple rational bad transfers found on odd grids through \(N=41\),
\((1,2)\) is closest in logarithmic \((r,s)\)-distance to the physical class

\[
\left(\frac{39}{55},\frac{121}{45}\right).
\]

This supplies Deutsch's requested nearby world: moving the radial transfer
to the period-compatible relation \(t_0=t_2\), \(t_1^2=2t_2^2\) activates
an otherwise absent circuit. The next explanatory task is to derive a
source invariant separating every physical transfer class from the torsion
discriminant containing \((1,2)\).

## Source-curve audit

For a fixed dark pair, a surviving latitude does not choose \(R\) and \(S\)
independently. Define

\[
R(z)=\frac{Q_0(z)}{Q_2(z)},
\qquad
S(z)=\left(\frac{Q_1(z)}{Q_2(z)}\right)^2.
\]

For the two regular reflection orbits these are

\[
R_1(z)
=-\frac{375z^2-180z-77}{4500(z^2-1)},
\qquad
S_1(z)
=-\frac{(19z-9)^2}{3249(z^2-1)},
\]

and

\[
R_2(z)
=-\frac{15z^2+60z-77}{180(z^2-1)},
\qquad
S_2(z)
=-\frac{(z+3)^2}{9(z^2-1)}.
\]

Eliminating \(z\) gives two explicit rational conics. Thus a directed
transfer is a multiplicative chord of a source-derived curve, not a free
point of the \((r,s)\)-plane.

The conics do not exclude the bad transfer. Solving

\[
R(y)=R(x),
\qquad
S(y)=2S(x)
\]

gives the nontrivial equal-\(R\) involutions

\[
90xy-149x-149y+90=0,
\]

\[
30xy-31x-31y+30=0.
\]

Their admissible bad-chord latitudes satisfy

\[
6096481x^2-8153586x+2148201=0
\]

or

\[
14519x^2-30498x+14031=0.
\]

Both quadratics have nonsquare discriminant. They possess roots in the
physical interval, so reflection-compatible real Legendre transport can
activate the Deutsch circuit. It cannot do so at rational latitudes through
this chord.

The protection hierarchy is therefore sharper:

\[
\text{spin two}
\;+\;
\text{odd sampling}
\;+\;
\text{reflection}
\;+\;
\text{Legendre source curve}
\]

still does not forbid the circuit. The current apparatus additionally uses
the rational latitude lattice

\[
\left\{-\frac23,-\frac13,0,\frac13,\frac23\right\}.
\]

Replacing two surviving rational latitudes by the displayed quadratic
conjugate chord is the smallest constructor-level extension presently known
to activate the \((1,2)\) circuit. Rational-lattice protection for all
torsion discriminants remains a conjecture; only this nearest bad chord has
been classified.

A wider inverse search through odd \(N\leq75\), accepting rational
reconstructions with denominator at most \(500\) and replaying near matches
at high precision, finds only two nondegenerate simple rational bad
transfers:

\[
(r,s)=(1,2),\qquad(r,s)=(3,4).
\]

For \((3,4)\), eliminating the source latitudes gives the quartics

\[
1272256551x^4+1498218768x^3-8613013086x^2
+9246225744x-3148996777
\]

and

\[
59049x^4+711504x^3+1848510x^2-325104x-2231687.
\]

Both are irreducible over \(\mathbb Q\). Hence neither known rational
torsion discriminant is realized by a rational chord of either radial source
conic. A putative \(N=69\) transfer \(r=50/347,s=1\) fails high-precision
replay by approximately \(2.22\times10^{-11}\); it is a near-rational
continuous approximation, not an exact discriminant point.

The strengthened conjecture is:

> Rational chords of the two physical radial source conics avoid every
> nondegenerate odd-torsion three-plus-two discriminant.

This is stronger than the finite five-latitude theorem and now has two exact
hostile algebraic extensions. It still requires an unbounded argument:
bounded reconstruction cannot exclude rational bad transfers of larger
height or conductor.

## Exact closure of the symmetric near-rational family

The rejected (N=69) reconstruction belongs to a family that can be closed
without a conductor bound.  Take the base triple

\[
\{1,v,v^{-1}\}
\]

and the target pair \(\{v,v^{-1}\}\), and put

\[
t=v+v^{-1}.
\]

Substitution in the two residual equations gives

\[
X=-2t(t+1),\qquad
Y=-2t(t^2+t-1),
\]

and the unique nondegenerate transfer

\[
s=1,qquad
r=-\frac{t^2+t-1}{t+1}.
\]

This formula explains why high-conductor examples can approach simple
rationals extremely closely.  It also proves that none is exactly a positive
rational bad transfer.  Indeed, if \(r=q\in\mathbb Q\), then

\[
t^2+(1+q)t+(q-1)=0.
\]

Hence \([\mathbb Q(t):\mathbb Q]\leq2\).  If \(v\) has odd order \(n>2\),
the real cyclotomic trace has degree \(\varphi(n)/2\), so
\(\varphi(n)\leq4\).  The odd possibilities are only \(n=1,3,5\).  At
order one, \(t=2\) gives \(r=-5/3\).  At order three, \(t=-1\) is the pole
of the pencil.  At order five, \(t^2+t-1=0\) gives \(r=0\).  These are,
respectively, inadmissible, degenerate, and degenerate.

Thus the entire reflection-symmetric family contains no positive,
nondegenerate rational bad transfer.  The (N=69) value is not an isolated
numerical accident: it is an irrational cyclotomic value shadowed by a nearby
rational.  This is the first unbounded subfamily of the inverse torsion
problem to close exactly.  It does not yet settle nonsymmetric base triples.

## Two-trace closure of every reflection-centered family

The target pair need not coincide with the nontrivial base pair.  Let

\[
\{1,u,u^{-1}\}
\]

be the base triple, let \(\{v,v^{-1}\}\) be an independent target pair, and
write

\[
x=u+u^{-1},\qquad W=(v+v^{-1})^2.
\]

The two residual equations simplify exactly to

\[
r=\frac{x-(x+1)W}{x(x+1)},
\qquad
s=\frac{W}{x^2}.
\]

Consequently, rational \(r,s\) imply

\[
s x^2+(s+r)x+(r-1)=0.
\]

The base trace again has degree at most two, so an odd-order base root has
order only \(1,3,5\).  These cases close as follows.

- At order one, \(x=2\).  Rationality of \(s\) forces the odd-torsion target
  square \(W\) to be rational.  The rational root-of-unity trace theorem
  leaves \(W=1\) or \(W=4\), and both give \(r\leq0\).
- At order three, \(x=-1\), where the transfer pencil degenerates.
- At order five, reducing the rationality equation modulo
  \(x^2+x-1\) gives

  \[
  rx+(r+s-1)=0.
  \]

  Irrationality of \(x\) therefore forces \(r=0\) and \(s=1\).

Hence no reflection-centered odd-torsion base triple and inverse target pair
supports a positive, nondegenerate rational bad transfer.  This strictly
contains the diagonal family and removes the target-identification
assumption.  Any remaining rational circuit must break reflection centering
of the base triple itself.

## Off-center compression and the defect seven point

There is a larger product-one family in which the base triple need not be
reflection-centered.  Let its elementary symmetric functions be

\[
A,\qquad B=\overline A,\qquad C=1,
\]

and retain an inverse target pair with squared trace \(W\).  Introduce the
real base invariants

\[
U=A+B,qquad V=AB=|A|^2.
\]

The two residual equations become

\[
r(2V-U^2+U)+(1-W)U-2=0,
\]

\[
rU+W-2+s(V-1)=0.
\]

Eliminating \(W\) produces the unexpectedly small incidence law

\[
r(2V+U)+sU(V-1)-U-2=0.
\]

Thus the target separation is not part of the first obstruction.  For fixed
rational transfer \((r,s)\), every admissible product-one base triple must
lie on a rational Möbius curve in the \((U,V)\)-plane.  The target pair is
reconstructed only afterward from

\[
W=2-rU-s(V-1).
\]

Reflection-centered triples form the discriminant locus

\[
\Delta=4V-U^2=0.
\]

The exact \(N=21\) circuit instead has

\[
(U,V)=(-1,2),\qquad (r,s)=(1,2),
\]

and therefore

\[
\Delta=4\cdot2-(-1)^2=7.
\]

This identifies the first exception as a genuinely off-center torsion point,
not a failure of the centered proof.  Its prime seven is already encoded in
the base-triple centering defect.  The remaining classification problem is
now precise: determine the torsion points on these rational incidence curves
and then impose that the reconstructed \(W\) is an inverse-pair torsion
trace square.  This is a cyclotomic unlikely-intersection problem rather than
an unconstrained five-point determinant search.

## Reducible incidence and the complete heptagon

The product-one incidence polynomial is bilinear:

\[
E_{r,s}(U,V)
=sUV+2rV+(r-s-1)U-2.
\]

Its coefficient matrix has determinant

\[
-2(r-1)(r-s).
\]

It therefore factors precisely on the two rational transfer strata

\[
r=1\qquad\text{or}\qquad r=s.
\]

The factorizations are

\[
E_{1,s}=(sU+2)(V-1),
\]

\[
E_{r,r}=(U+2)(rV-1).
\]

The first known bad transfer lies on the first reducible stratum:

\[
E_{1,2}=2(U+1)(V-1).
\]

Its \(N=21\) base triple uses seventh-root exponents \(\{1,2,4\}\).
Their inverses have exponents \(\{6,5,3\}\), and the two sets partition all
nonzero residues modulo seven.  Consequently

\[
1+U=1+\sum_{j=1}^{6}\zeta_7^j=0.
\]

So the exceptional branch \(U=-1\) is exactly the complete heptagon
cyclotomic relation.  The circuit exists because three selected roots plus
their reflected partners close a full prime polygon; the transfer
factorization exposes that polygon as an entire component of the incidence
curve.  The value \(V=2\), and hence the centering defect seven, is the norm
data of the same quadratic-period split.

This separates the two rational bad transfers found by the inverse search.
The \((1,2)\) transfer belongs to a reducible incidence stratum and admits the
prime-seven polygon mechanism.  The \((3,4)\) transfer is off both reducible
strata, so any realization of it must be an isolated torsion intersection
with an irreducible bilinear curve.  Its mechanism cannot be another copy of
the complete-heptagon branch.

### Exact classification of the \(U=-1\) branch

The heptagon explanation is exhaustive, not merely an example.  On the
\(U=-1\) branch,

\[
1+\alpha+\beta+\gamma
+\alpha^{-1}+\beta^{-1}+\gamma^{-1}=0,
\qquad \alpha\beta\gamma=1.
\]

This seven-term vanishing sum is minimal.  A proper vanishing subsum cannot
have weight two because all roots have odd order.  If it had weight three,
the complement would have weight four, which is excluded by the odd-prime
weight theorem for vanishing sums.  Weights four, five, and six similarly
leave or contain an impossible complement of weight four, two, or one.

Mann's theorem therefore says that every ratio of roots in the sum has order
dividing the product of primes at most seven.  Removing the factor two because
all ratios have odd order leaves

\[
3\cdot5\cdot7=105.
\]

The exact quotient-ring enumeration in
\(\mathbb Q[x]/(\Phi_{105}(x))\), with distinct base exponents and
\(a+b+c=0\pmod{105}\), has precisely two solutions:

\[
(a,b,c)=(15,30,60),qquad(45,75,90).
\]

After division by 15 these are the two conjugate orientations

\[
\{1,2,4\},\qquad\{3,5,6\}\pmod 7.
\]

Thus every odd-torsion realization of the \(U=-1\) component is the
quadratic-residue heptagon, up to the normalizations already imposed.  In
particular, the \((1,2)\) exceptional mechanism is conductor-seven rigid.

## Endogenous authority plane for the heptagon perturbation

The question "why not perturb \(r\)?" is ill-typed until four distinct facts
are separated.

1. **Algebraic state.** The formulas represent \(r=1+\varepsilon\), and the
   heptagon response is

   \[
   E_{r,s}(-1,2)=3r-s-1.
   \]

   The null class therefore persists on the compensation line

   \[
   s=3r-1.
   \]

   Holding \(s=2\) fixed gives the transverse response \(3(r-1)\), but a
   coordinated change of \(s\) can preserve the kernel.

2. **Physical feasibility.** The first Legendre source conic has two real
   bad-chord latitudes in \((-1,1)\), and the second has one.  Thus each
   continuous source orbit can realize \((r,s)=(1,2)\) at a physical
   latitude.

3. **Constructor capability.** The bad-chord latitude polynomials have
   nonsquare discriminants.  The original rational-latitude constructor
   cannot instantiate their roots.

4. **Authority.** Existence of those real source points does not authorize an
   extension of the constructor grammar.  Such an extension requires its own
   source-derived grant and evidence packet.

Therefore \(r=1\) is not presently a dynamical law: the continuous dynamics
admits it.  Nor is the heptagon circuit part of the original constructible
state space: its required radial chord lies outside the rational latitude
lattice.  The current protection is a constructor boundary.  Whether that
boundary is immutable or may be crossed is an endogenous authority question,
not a consequence of the conic's geometric support.

A fully typed counterfactual must consequently carry an authority-bearing
constructor

\[
G_{\delta r,\delta s}:
(r,s)=(1,2)\longmapsto(1+\delta r,2+\delta s),
\]

together with its domain, source basis, consumption rule, and evidence state.
Without such a grant, the affine response is an algebraic prediction, not an
executable intervention.  With an admitted algebraic-latitude extension, the
prediction becomes testable.  A deformation \((\delta r,\delta s)\) gives

\[
\delta E=3\delta r-\delta s.
\]

The null class is lifted transversely and survives for authorized deformations
tangent to \(\delta s=3\delta r\).

### Source pullback of the compensation line

Pull the compensation law back through each radial chord map

\[
r=\frac{R(y)}{R(x)},\qquad s=\frac{S(y)}{S(x)}.
\]

The equation

\[
\frac{S(y)}{S(x)}-3\frac{R(y)}{R(x)}+1=0
\]

is quadratic in the target latitude \(y\).  For the first Legendre orbit its
discriminant in \(y\) is

\[
-8(19x-9)^2 f_1(x),
\]

where

\[
\begin{aligned}
f_1(x)={}&2511675x^6-14405580x^5+22402983x^4+13747572x^3\\
&-58129525x^2+45092772x-11916097.
\end{aligned}
\]

For the second orbit the discriminant is

\[
8(x+3)^2 f_2(x),
\]

where

\[
\begin{aligned}
f_2(x)={}&3645x^6+18180x^5+31497x^4-27564x^3\\
&-72323x^2-5484x+52081.
\end{aligned}
\]

Both sextics are squarefree.  After removing the displayed square factors,
rational compensation chords are governed by two genus-two hyperelliptic
curves.  The original five rational latitudes produce no chord on either
pullback.  An additional exact search over reduced rational latitudes of
denominator at most 20 also finds no positive transfer, but that wider result
remains bounded evidence.

The authority question now has a precise arithmetic capability gate.
Authorizing arbitrary real algebraic latitudes activates a continuous
source-supported compensation family.  Restricting to rational latitudes may
exclude the entire family, not just \((r,s)=(1,2)\).  Proving that requires
determining the rational points on the two displayed genus-two curves;
geometric support alone supplies no constructor authority.

### Rational boundary-only conjecture

There is no immediate local obstruction: both genus-two curves have points
over every tested good residue field below 300.  Rational protection, if
true, is therefore global rather than a congruence veto.

An exact homogeneous search gives a sharper pattern.  For \(x=a/b\), the
lift condition is tested by asking whether

\[
c\,b^6f(a/b)
\]

is an integer square, with \(c=-8\) or \(8\).  Through denominator 500,
neither curve has a rational point with \(|x|<1\).  Each curve does have the
two rational base coordinates

\[
x=-1,qquad x=1,
\]

with both signs of the hyperelliptic coordinate.  These are exactly the
excluded latitude boundaries where the original radial functions have poles.
The leading coefficients also exclude rational points at infinity.

The resulting unbounded target is:

> Every rational point on either compensation curve lies above
> \(x=\pm1\), hence no rational point defines an executable physical chord.

This is stronger and better typed than claiming that the curves have no
rational points.  The curves retain boundary states, but the source-domain
contract excludes them.  A proof should compute the Jacobian ranks and
2-Selmer information, then apply Chabauty--Coleman or a Mordell--Weil sieve if
the rank permits.  Until that calculation is supplied, boundary-only remains
a bounded conjecture rather than a theorem.

### Jacobian torsion and the rank-one frontier

The first exact Jacobian invariant can be computed without a dedicated
arithmetic-geometry package.  For a genus-two curve, point counts over
\(\mathbb F_p\) and \(\mathbb F_{p^2}\) determine
\(\#J(\mathbb F_p)\).  The verified reduction orders are

\[
\begin{array}{c|ccc}
&p=11&p=13&p=19\\
\hline
J_1&222&165&419
\end{array}
\]

and

\[
\begin{array}{c|cc}
&p=7&p=11\\
\hline
J_2&117&107.
\end{array}
\]

All listed primes are primes of good reduction.  In both rows the gcd of the
orders is one.  Since rational torsion injects into every good reduction,

\[
J_1(\mathbb Q)_{\mathrm{tors}}=0,
\qquad
J_2(\mathbb Q)_{\mathrm{tors}}=0.
\]

The distinct rational boundary points therefore produce non-torsion divisor
classes, so each Jacobian has positive rank.  Rank zero is excluded.  The
most favorable remaining possibility is rank one, which is below the genus
and would permit Chabauty--Coleman.  What remains missing is an upper bound
from 2-descent or an equivalent certified Mordell--Weil computation.  The
finite-field calculation establishes torsion-freeness; it does not by itself
establish rank one or completeness of the boundary point list.

### No elliptic-factor shortcut

Both compensation sextics are irreducible over \(\mathbb Q\).  Their Galois
groups have order

\[
720=|S_6|,
\]

and are the full symmetric group \(S_6\).  Thus the rational branch locus does
not split into lower-degree factors, and the obvious route through a product
of elliptic descents is unavailable.  The rank frontier is a genuine
degree-six genus-two 2-descent problem.

No Sage, Magma, or PARI runtime is available in the current workspace; the
PowerShell command named `gp` is an unrelated alias, and the lightweight
Python PARI binding cannot build without a PARI installation.  The smallest
missing constructor is therefore:

```text
GenusTwoJacobianRankBounds
  input: squarefree sextic over Q, known rational divisor classes
  output: certified lower and upper Mordell--Weil rank bounds
  required evidence: 2-Selmer computation and local images
```

At that stage, the requested output was an upper bound of one for each
Jacobian.  Subsequent canonical-height calculations below falsify that target.
An asserted rank based only on the height census or finite-field orders would
still exceed the authority of those calculations.

The exact rational input points for that constructor are

\[
C_1(\mathbb Q)_{\mathrm{known}}
=\{(-1,\pm26768),(1,\pm2360)\},
\]

\[
C_2(\mathbb Q)_{\mathrm{known}}
=\{(-1,\pm488),(1,\pm16)\}.
\]

Each point has been replayed against the integral hyperelliptic model.  The
machine-readable result now carries these points, the trivial-torsion
certificates, proved rank lower bounds \([2,2]\), requested upper bounds
\([2,2]\), and the required 2-Selmer local-image evidence.  This is the
complete descent request; no inferred rank or executable capability is
encoded in it.

### Conditional descent falsifies the immediate Chabauty route

The exact models were submitted to the official Magma V2.29-9 calculator.
For the first curve, both `RankBounds(J)` and the direct
`RankBound(f,2)` exceeded the online time limit during unconditional class
group work.  Magma reported that unconditional class-group proof was
infeasible in that environment and suggested its GRH mode.

With

```text
SetClassGroupBounds("GRH");
RankBound(f,2);
```

the two curves returned the conditional upper bounds

\[
\operatorname{rank}J_1(\mathbb Q)\leq4,
\qquad
\operatorname{rank}J_2(\mathbb Q)\leq6.
\]

These are GRH-conditional 2-Selmer bounds, not actual ranks and not
unconditional certificates.  More importantly, both are at least the genus,
so they do not unlock classical Chabauty.  The earlier rank-one hope is now a
failed strategy rather than the active theorem path.

The boundary-only conjecture may still be true, but it requires stronger
information: improved Mordell--Weil bounds, elliptic or number-field Chabauty,
quadratic Chabauty, a Mordell--Weil sieve with additional generators, or a
direct source-specific argument on the original bidegree compensation curve.
The conditional probe is retained as discovery evidence with its assumption
and failure status explicit.

### Curve-level two-cover frontier

The official Magma handbook supplies a stronger route when the Jacobian rank
is too large for classical Chabauty: compute the fake two-Selmer set of the
curve itself, realize each surviving two-cover over a factor field, and apply
elliptic Chabauty to points whose image on the \(x\)-line is rational.

The GRH-conditional online probes give:

- For \(C_1\), the full descent exceeded the time limit.  With
  `PrimeBound:=30`, Magma returned three classes.  The handbook explicitly
  states that restricting good primes can return a strict superset of the
  true two-Selmer set, so three is an upper candidate count, not a certified
  complete set.
- For \(C_2\), the full call returned 18 classes.  This is complete relative
  to the GRH class-group assumption used by the calculation, but it is not an
  unconditional result.

The immediate compiler target is now one cover packet per returned class:

```text
TwoCoverEllipticChabautyPacket
  curve_id
  selmer_class
  class_group_assumption
  factor_field
  elliptic_cover
  rational_x_map
  Mordell-Weil finite-index certificate
  Chabauty output
  reconstructed rational curve points
```

For \(C_1\), omitted good-prime local tests must first remove the
`PrimeBound` incompleteness.  For \(C_2\), all 18 conditional classes must be
discharged.  Only after every cover reconstructs points above \(x=\pm1\) may
the boundary-only conjecture be promoted, and unconditional promotion still
requires unconditional class-group evidence.

### Boundary points force rank at least two

The four known boundary points contain more Mordell--Weil information than
the initial torsion argument detected.  For each curve, choose one boundary
point as origin and form the three differences to the other boundary points.
Magma V2.29-9 `ReducedBasis`, using unconditional canonical-height
computations, returns two generators.  In both cases the input differences
have coordinate matrix

\[
\begin{pmatrix}
1&1\\
1&0\\
0&1
\end{pmatrix}.
\]

The height-pairing matrices are nonsingular.  Consequently

\[
\operatorname{rank}J_1(\mathbb Q)\geq2,
\qquad
\operatorname{rank}J_2(\mathbb Q)\geq2.
\]

There is a stronger support statement.  All four returned reduced generators
have Mumford (u)-polynomial

\[
u(x)=x^2-1.
\]

Thus the two independent classes are not generic interior points discovered
by a height search.  They are boundary-supported divisor contrasts carried by
the two fibres (x=-1) and (x=1).  The coordinate relation above removes
one redundant presentation among the three contrasts, while the nonsingular
height pairing shows that the remaining two contrasts survive globally and
are non-torsion.  In particular, the completion obstruction manufactures its
own rank-two arithmetic witness at the endpoint divisor.

The redundancy is source-derived.  Write the two points above (x=-1) as
(P_-^+,P_-^-), and those above (x=1) as (P_+^+,P_+^-).  Fibres of the
hyperelliptic degree-two map are linearly equivalent, so

\[
P_-^+ + P_-^- \sim P_+^+ + P_+^-.
\]

Choosing (P_-^+) as origin and setting

\[
D_1=[P_-^- - P_-^+],\quad
D_2=[P_+^+ - P_-^+],\quad
D_3=[P_+^- - P_-^+]
\]

gives the universal identity (D_1=D_2+D_3).  Thus the boundary packet has
rank at most two for geometric reasons on every such hyperelliptic fibre
pair.  The height determinants do only the remaining job: they show that the
universal upper bound is attained on both compensation curves.

Magma's exact (p)-saturation routine returns the same two-element basis for
both curves at all (54) primes

\[
p\leq251.
\]

Hence the boundary subgroup is (p)-saturated at each of these primes.  This
is deliberately a bounded index theorem, not a proof of global saturation:
if the subgroup has finite index in a larger rational subgroup, every prime
divisor of that index is at least (257).  In particular, an unseen rational
half-class cannot explain the gap between the visible rank-two subgroup and
the conditional two-descent upper bounds.  Closing global saturation now
requires an independent upper bound on the saturation index, or a complete
Mordell--Weil computation; extending the prime census alone cannot supply that
logical step.

There is no local representability loophole.  Exact deficient-place checks
over the real place and every bad finite prime return no deficient places for
either curve.  Equivalently, both curves have index one everywhere locally.
Thus every rational Jacobian class is representable by a rational divisor,
and the descent rank bounds concern the full Jacobian rather than only a
representable submodule.  The unresolved quotient is therefore a genuinely
global closure defect: it cannot be attributed to failure of a local divisor
constructor.

Both curves also return `HasSquareSha = true`.  Under the documented
finiteness hypothesis for the Tate--Shafarevich group, this says its order is
a square.  It is not, by itself, a rank-parity theorem.

The common boundary behavior is not inherited from a common bad-reduction
tail.  The finite bad-prime supports intersect exactly in

\[
\{2,3,5\}.
\]

Outside those universal small primes the supports are disjoint, even though
both curves have the same boundary support polynomial, the same rank-two
relation matrix, and unchanged saturation bases through (251).  This is
evidence that the shared rank-two packet is natural in the endpoint
constructor rather than an accidental consequence of matching arithmetic
fault spectra.

This rules out classical Chabauty unconditionally because the rank is already
at least the genus.  The earlier rank-one target is not merely unproved; it is
false.  The revised rank request asks whether both ranks equal two, but point
classification must proceed through curve-level two-cover descent and
elliptic Chabauty, or another higher-rank method, regardless of that answer.
