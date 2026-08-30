# The route packet separates absence from interference

Factor the observation system as

\[
\mathcal S\xrightarrow{T}
\mathcal P_L\oplus\mathcal P_R
\xrightarrow{\sigma=[1\;1]}\mathcal O.
\]

The intermediate route packet is `T(s)=(A(s),B(s))`; the exposed readout is
`A+B`.  Invisible source information fits into

\[
0\longrightarrow\ker T
\longrightarrow\ker(\sigma T)
\longrightarrow\operatorname{im}T\cap\ker\sigma
\longrightarrow0.
\]

The two terms distinguish mechanisms:

- `ker T`: route loss, with packet `(0,0)`;
- `im(T) intersect ker(sigma)`: destructive interference, with nonzero packet
  `(A,-A)`.

The anti-diagonal `ker(sigma)` exists architecturally for every parameter.  It
becomes realized hidden information only when the transported source image
meets it.

For the admissible magnetic exception `(g,d)=(2,5)`, both carriers vanish, so
the circuit belongs to the route-loss term.

The analytically continued **local residual coordinate** contains the other
mechanism.  At the exact rational point

\[
(g,d)=\left(6,\frac{17}{3}\right),
\]

both routes are nonzero, while the weighted amplitudes are

\[
A=-\frac{113228379953561600000}{729},
\qquad
B=\frac{113228379953561600000}{729}.
\]

Thus `A+B=0` with `(A,B) != (0,0)`: a literal coherence residue in the local
two-route packet.  This witness shows that route loss and destructive
interference are not merely two verbal descriptions of the same residual
determinant zero.

It is not yet a kernel vector of a fractional magnetic source system.  Direct
construction of the three corresponding full path columns gives no
three-column null vector: the integer-tail Schur reduction used to obtain the
local coordinate does not automatically extend to fractional collision
depths.  Promoting this local coherence residue to a source state requires a
new, explicitly specified tail lattice and elimination grammar.

## Integrality as interference protection

At grade six the obstruction polynomial factors as

\[
P(6,d)=4(3d-17)(3d-37).
\]

Hence the two exact balance points are

\[
d=\frac{17}{3},\qquad d=\frac{37}{3}.
\]

Both lie off the admitted integer depth lattice.  The Diophantine theorem
shows that this is the only higher-grade rational-square opportunity for the
local residual coordinate.  Its two interference fibers are excluded by
depth quantization.  The sole integral zero is the grade-two residual-carrier
loss point.  At the later full-sheet level, its magnetic kernel vector has
nonzero equal sheets; see `magnetic-two-level-interference.md`.

In system terms, the continuous transport law permits a finely tuned
anti-diagonal packet, but the discrete configuration protocol cannot encode
the required tuning.  Integrality acts as an error-detecting constraint:

\[
\text{continuous system permits interference; discrete admissibility rejects
its balance ratio.}
\]

For a multi-sector augmentation such as the cosmological star, the analogous
factorization retains all labelled adapted sector outputs before applying the
weighted sum.  The meaningful coherence residue is then

\[
\operatorname{im}T\cap\ker\sigma,
\]

not the generically large `ker(sigma)` by itself.

## Cubic-cover preflight

The substitution `z=w^3` makes the fractional monomial exponents integral,
but it does not by itself transport the source grammar.  A spin-two component
pulls back as

\[
C_{ww}=\left(\frac{dz}{dw}\right)^2C_{zz}=9w^4C_{zz}(w^3,\bar w^3),
\]

and the round metric becomes

\[
\gamma_{w\bar w}=\frac{18w^2\bar w^2}{(1+w^3\bar w^3)^2}.
\]

The two readout routes land in different tensor components
`K^(g+2) tensor Kbar` and `K tensor Kbar^(g+2)`.  Their direct-sum packet
pulls back naturally; their subtraction requires a declared lifted frame or
pairing.  Moreover, the lifted sources do not belong to the original
nonnegative even-pole grammar.  Therefore the cubic cover is presently
ill-typed as an extension of the classified source system.  A valid test must
first specify:

1. the lifted source lattice, including its tail columns;
2. the pulled-back spin/tensor trivialization;
3. the lifted readout pairing;
4. branch-point admissibility at `w=0`.

Without these data, substitution into the residual formula transports a
presentation but not the authority to claim a new kernel state.

There is also an exact descent obstruction.  Under the cubic deck action

\[
w\mapsto\omega w,
\qquad
\bar w\mapsto\omega^{-1}\bar w,
\qquad \omega^3=1,
\]

a Laurent coefficient `w^p wb^r` has raw character `p-r mod 3`.  Including
tensor indices, the invariant charge of

\[
w^p\bar w^r(dw)^n(d\bar w)^m
\]

is

\[
\chi=p-r+n-m\pmod3.
\]

A genuine
pullback

\[
C_{ww}=9w^4C_{zz}(w^3,\bar w^3)
\]

has raw coefficient character `1 mod 3`, which combines with its two `dw`
indices to give total charge zero.  The three candidate coefficients instead
have

\[
\begin{array}{c|c}
(p,r)&p-r\pmod3\\
\hline
(4,-50)&0\\
(-10,6)&2\\
(-16,0)&2
\end{array}
\]

After the two spin indices are included, their intrinsic charges are

\[
(2,1,1).
\]

None has descended charge zero, and the proposed three-term relation is not
even deck-homogeneous.  Deck-equivariant transport
preserves these sectors, so a descended readout cannot coherently cancel the
charge-2 source against the charge-1 sources.

This supplies a source-derived type checker for the cover:

\[
\text{integer Laurent representation on the cover}
\not\Rightarrow
\text{deck-equivariant descent data}.
\]

Activating the local interference packet would require breaking or twisting
deck equivariance, not merely adjoining cube roots.

## Constructor conservation law

The charge formula makes naturality elementary.  A covariant `w` derivative
lowers `p` by one and adds one `dw` index:

\[
(p,n)\mapsto(p-1,n+1),
\]

so `chi` is unchanged.  A covariant `wb` derivative similarly sends
`(r,m)` to `(r-1,m+1)` and also preserves `chi`.  The pulled connection terms
have exactly the same charge shifts.  Therefore every fold composition
preserves deck charge.  Reflection exchanges barred and unbarred data and
sends `chi` to `-chi`; it pairs conjugate sectors without identifying them.

To combine the candidate charge-2 source with the two charge-1 sources, a new
adapter must carry charge 2.  Multiplication by `w^2` is the smallest local
example, since `2+2=1 mod 3`, but it is not deck-invariant and changes the
source grammar.  A lawful activation must therefore name a charged defect,
twisted line bundle, or explicit symmetry-breaking morphism that supplies
this charge.

## The parameter-type obstruction

There is a still earlier issue.  The excess `d=q-g` is a discrete type derived
from exponent labels, not a scalar coefficient in a fixed source module.
Analytically continuing `P(g,d)` moves the labels of the residual columns:

\[
(0,d-1,d+1)
\quad\longrightarrow\quad
\left(0,\frac{14}{3},\frac{20}{3}\right)
\]

at `d=17/3`.  These lie in depth cosets

\[
0,\frac23,\frac23\pmod2,
\]

whereas the classified source grammar uses the single even-depth coset.
Therefore `P(g,d)=0` is an analytic continuation of a relabelled residual
presentation, not automatically the Fitting locus of one fixed family of
source modules.

The cubic cover makes the coefficient exponents integral.  With cover pole
depth `A=-p`, the candidates have

\[
A=(-4,10,16),
\qquad
A\pmod6=(2,4,4),
\]

and barred exponents modulo three `(1,0,0)`.  The essential pullback image of
the original grammar instead satisfies both

\[
A=2\pmod6,
\qquad
r=0\pmod3.
\]

No candidate satisfies both conditions.  A cover extension must consequently
authorize three logically separate changes:

1. enlarge the source lattice to new congruence classes;
2. supply charged adapters so the desired sum is deck-homogeneous;
3. define the fractional/cover tail whose elimination produces the residual
   block.

Passing the first gate does not imply either of the others.  This explains why
integer Laurent representability alone failed to produce a full kernel.

## No cyclic cover can repair the branch mismatch

The cubic obstruction is a special case of an arbitrary-cover law.  Under
`z=w^N`, the total spin-two deck charge of a lifted monomial is

\[
\chi_N=N(2-a-m)\pmod N.
\]

The two reflected branches have

\[
a+m=1-g-q,
\qquad
a+m=1-g+q.
\]

Their charge difference is therefore

\[
\Delta\chi_N=2Nq\pmod N.
\]

After `N` clears the denominator of `q`, the branches align only if

\[
2q\in\mathbb Z.
\]

For the two grade-six rational residual roots,

\[
q=\frac{35}{3},\qquad q=\frac{55}{3},
\]

and neither has integral `2q`.  Consequently no cyclic cover of any degree
that clears thirds can place the reflected branches in one deck sector.  A
uniform twist shifts every charge equally and also cannot change their
difference.

Thus the obstruction is not peculiar to choosing a cubic cover:

\[
\text{no finite cyclic cover alone activates either rational interference
pattern.}
\]

Only a sector-specific charged adapter, a defect absorbing the charge
difference, or explicit deck-symmetry breaking can do so.

## Rational-cover classification

The odd-core discriminant theorem and the cover criterion join cleanly.  For
integer grade `g>=2`, the complete list of rational zeros of the continued
residual obstruction is

\[
(g,d)=(2,5),
\quad
\left(6,\frac{17}{3}\right),
\quad
\left(6,\frac{37}{3}\right).
\]

The first has `q=7` and is the original integral route-loss exception.  The
two grade-six points have `q=35/3,55/3`, so neither satisfies `2q in Z`.
Therefore:

\[
\text{No rational destructive-interference zero of the odd residual block
is compatible with descent through any finite cyclic cover.}
\]

This is stronger than integer-lattice protection.  Clearing denominators by
an arbitrarily large cyclic cover never suffices.  The only rational zero that
passes the descent type checker is the already constructible grade-two
route-loss class.
