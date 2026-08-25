# Typed cancellation and the fixed-family gate

Owner: `marici.Nima`

## 1. When distinct characters cannot interfere

Let a finite deck group `G` act over a characteristic-zero coefficient field,
and decompose a route object into character sectors

\[
E=\bigoplus_\chi E_\chi.
\]

Suppose the physical readout is a `G`-equivariant map

\[
\sigma:E\to Y_\psi
\]

into one character sector.  Then

\[
\sigma|_{E_\chi}=0\qquad(\chi\ne\psi).
\]

Consequently, two nonzero routes of different character cannot both
contribute to one irreducible typed output.  In the direct sum itself,

\[
A_\chi+B_{\chi'}=0,\quad\chi\ne\chi'
\]

implies `A=B=0`, by the character projectors.

For the cubic magnetic cover, the candidate characters `(0,2,2)` do not
match the descended spin-two character `1`.  The proposed circuit therefore
does not define a relation in the descended output sector.

## 2. What would make cross-character cancellation possible

It can occur only after adding structure that changes the theorem's
hypotheses:

- a non-equivariant comparison or evaluation map;
- a twist identifying the characters;
- symmetry breaking that changes the physical target;
- coefficients of characteristic dividing `|G|`, where the representation
  need not split semisimply;
- a derived or ramified operation with explicitly transported inertia data.

Such an operation is new constructor grammar.  It must not be smuggled in as
mere scalar extension.

### Forgetting is not collapsing

The ordinary forgetful functor from graded vector spaces to vector spaces is
faithful.  It retains the underlying direct sum:

\[
U\left(\bigoplus_\chi E_\chi\right)
=\bigoplus_\chi U(E_\chi).
\]

Hence `(A,B)` remains nonzero after merely forgetting the grade label.  False
cancellation requires a further map

\[
\Sigma:\bigoplus_\chi E_\chi\to O,
\qquad
(A,B)\mapsto\phi_\chi(A)+\phi_{\chi'}(B),
\]

which identifies different summands inside one output.  For distinct deck
characters, such comparison maps are not naturally equivariant.  The
magnetic analytic interpolation therefore performs an implicit **type
collapse**, not innocent type erasure.

At a ramification fixed locus, fiberwise values alone are also insufficient:
one must retain stabilizer character and vanishing order.  Evaluation can
erase the very grading that governed descent.

### The naturality gate

After forgetting equivariance, two one-dimensional character lines become
abstractly isomorphic as vector spaces.  Choosing bases can therefore produce
a map `(A,B) -> A+B`.  But the choice is not natural under independent
automorphisms of the two lines.

Let

\[
f:L_1\oplus L_2\to k,
\qquad f(A,B)=c_1A+c_2B.
\]

If `f` is required to be invariant under all independent rescalings
`(A,B)->(alpha A,beta B)`, then

\[
c_1=c_2=0.
\]

Thus there is no nonzero canonical codiagonal from two unrelated lines.  A
nonzero pairing becomes natural only after the source supplies additional
structure, for example:

- a common typed line and diagonal gauge action;
- a specified identification or duality pairing;
- a target character with matching equivariance;
- an orientation, trace, or incidence map fixing the comparison.

This gives a practical hostile test: transform route bases and the proposed
pairing together under every declared gauge transition.  A genuine zero is
preserved.  A fitted scalar cancellation that holds only in one chosen frame
is pseudo-interference.

There is an important qualification.  Independent automorphisms forbid a
canonical nonzero pairing only when the two bare route lines carry no further
structure.  Once the source supplies maps `f_i:L_i -> Y`, their coordinate
covectors transform contragrediently with the route coordinates.  If

\[
e_i'=\alpha_i e_i,
\qquad
x_i'=x_i/\alpha_i,
\qquad
c_i'=\alpha_i c_i,
\]

then `c_i'x_i'=c_ix_i`.  Hence a source-supplied cancellation is invariant
under independent changes of route frame.  The invalid operation is to change
the route coordinates while freezing the pairing coefficients.  Gauge
naturality therefore distinguishes two claims:

- bare route types do not manufacture their own comparison map;
- a source-declared comparison map may relate distinct route types, provided
  that map is transported as part of the structure.

### Interference is a cospan datum

The minimal typed interference object is

\[
E_L\xrightarrow{f_L}Y\xleftarrow{f_R}E_R
\]

together with route states `a in E_L`, `b in E_R`.  The coproduct universal
property forms the unique readout

\[
[f_L,f_R]:E_L\oplus E_R\to Y,
\]

and genuine destructive interference means

\[
f_L(a)+f_R(b)=0,
\qquad
f_L(a)\ne0,
\quad
f_R(b)\ne0.
\]

The routes need not be the same object.  What must exist is the
source-authorized cospan into a common additive target.  The familiar
codiagonal `X+X -> X` is merely the special case where both route objects and
both maps are identical.

This makes interference relational rather than intrinsic to either route.
Neither `a`, nor `b`, nor even the pair `(a,b)` determines a dark output.  The
event belongs to the evaluated cospan

\[
(a,b;f_L,f_R,Y).
\]

Changing the readout legs can remove or create the zero without changing the
route states.  Such a change is physical only when it is itself generated by
an authorized constructor or specialization.

### The coupled-cancellation quotient

The kernel of the combined readout still conflates route loss with genuine
interference.  For

\[
\sigma=[f_L,f_R]:E_L\oplus E_R\to Y,
\]

the coordinate-axis part

\[
K_{\mathrm{loss}}=(\ker f_L\oplus0)+(0\oplus\ker f_R)
\]

consists of routes that were already invisible before aggregation.  The
intrinsic coupled-cancellation object is instead

\[
K_{\mathrm{int}}
=
\frac{\ker\sigma}{K_{\mathrm{loss}}}.
\]

For vector spaces there is a canonical isomorphism

\[
K_{\mathrm{int}}
\simeq
\operatorname{im}f_L\cap\operatorname{im}f_R,
\]

where an element of the intersection records the common output reached with
opposite signs.  This yields an exact trichotomy:

- `ker sigma = 0`: no invisible packet;
- `ker sigma != 0` but `K_int = 0`: route loss only;
- `K_int != 0`: genuine coupled interference.

This quotient is basis-independent and survives replacement of either route
presentation by an isomorphic one.  It also exposes why a scalar determinant
is insufficient: the determinant sees total rank loss, while `K_int`
separates coupled cancellation from dead input channels.

For complexes or sheaves, the same construction must be derived.  The route
pair is the homotopy pullback of `f_L` and `-f_R`, and individual route
costalks must be removed by a cofiber rather than by a fitted vector-space
quotient.  Any residual homology is then supported interference, not merely a
coordinate relation.

### Two different discriminants

In a coherent family, the fiber dimension of coupled cancellation is

\[
\delta_{\mathrm{int}}
=
\operatorname{rank}f_L+
\operatorname{rank}f_R-
\operatorname{rank}[f_L,f_R].
\]

Therefore interference may be born while both individual route ranks remain
constant: their image subspaces simply cease to be transverse.  For example,

\[
f_L(t)=\binom10,
\qquad
f_R(t)=\binom1t.
\]

Both routes have rank one for every `t`, but at `t=0` their images coincide and
`K_int` jumps from zero to rank one.  This is a genuine interference
discriminant.

By contrast,

\[
f_L(t)=\binom t0,
\qquad
f_R(t)=\binom01
\]

loses a route at `t=0` while `K_int` remains zero.  The total determinant
vanishes in both examples, so an unrefined Fitting census cannot distinguish
them.

The program should consequently maintain two loci:

- the **route discriminant**, where an individual `f_i` loses rank;
- the **interference discriminant**, where the images acquire excess
  intersection after individual route loss has been removed.

Their intersection is the derived transition zone where a coupled packet can
degenerate into route loss, exactly the possibility now exposed at the deeper
cosmological ideal `q=y=C=0`.

Thus the route object alone does not determine interference.  Lens and
readout pairing are jointly required structure.  In the magnetic cover,
equivariance kills the necessary legs of the cospan.  In cosmology, the
pre-aggregation construction supplies them.

## 3. The coherent-family gate for determinants

A Fitting determinant has intrinsic meaning only for a morphism

\[
E:M\to R
\]

between coherent finite-type module objects over one parameter base.  They
need not be globally constant or carry one preferred basis.  Vector bundles,
coherent sheaves, and locally free graded modules are allowed when their local
presentations are connected by invertible typed transition maps.

Under basis changes `E -> UEV`, a maximal determinant changes by the unit
`det(U)det(V)`.  Its vanishing locus and Fitting ideal are therefore
unchanged.  A noninvertible or grading-mixing comparison is not a transition
map and may create a false zero.

If varying a parameter changes the source labels or grading sectors without
such descent data, then polynomial interpolation of matrix entries is not
automatically a family of the original source objects.

Therefore, before interpreting `det E(lambda)=0`, certify:

1. coherent source and target module objects over the parameter base;
2. typed invertible transitions between local presentations;
3. compatible grading/deck action and equivariance of `E`;
4. base change compatible with the source grammar;
5. a source-authorized readout pairing.
6. naturality of that pairing under every declared transition/gauge action.

Failure of any gate makes the zero an interpolated algebraic shadow rather
than an event.

In the magnetic continuation, rational `d` changes exponent labels such as
`d+/-1` away from the integral source lattice.  The continued polynomial is
useful for discovering formulas, but its rational fibers are not fibers of a
fixed integral source module.

## 4. Cross-sector contrast

- Magnetic rational roots: different deck characters and no common
  equivariant output; pseudo-interference after implicit type collapse.
- Cosmological contact kernel: both routes inhabit one declared route object
  and the source supplies the codiagonal; its generic coupled-cancellation
  quotient is rank one whenever `C != 0`.
- Topological instruments: equal effects arise through a legitimate
  forgetful map from one instrument space; sequential successors can inspect
  the fiber.

## Deutsch--Popperian conjecture

An algebraic zero is an event only if it is the zero of a source-authorized
morphism in a coherent typed family.  Zeros created only after collapsing
graded summands, changing object labels, or adding an unauthorized comparison
map are virtual presentation shadows.

## Falsifiers

- A nonzero equivariant map exists between distinct simple character sectors
  under the stated semisimple hypotheses.
- The magnetic rational circuit becomes homogeneous after the full pulled-back
  operator and inertia data are retained.
- The cosmological routes fail to share a source-declared codomain.
- A claimed Fitting family lacks coherent module objects and invertible typed
  transitions over its parameter base.
- A claimed interference zero disappears after a legal gauge change with the
  pairing transported naturally.
