# Radiative orientation-twist source gate

## Question

Does the exact radiative/BMS packet independently realize the character-level
candidate

\[
L_{\rm time}\cong L_{\rm pol}\otimes L_{\rm space}
\]

found in the scattering/Carrier comparison?

## What the frozen radiative packet actually supplies

The Strominger convention and source-boundary packets define:

- the celestial antipodal map \(z\mapsto-1/\bar z\), sending
  \(\hat x\mapsto-\hat x\);
- antipodal matching across spatial infinity,
  \(C_{zz}|_{\mathcal I^+_-}=-D_{zz}|_{\mathcal I^-_+}\), with \(f^-=f\);
- the corner magnetic-parity constraint
  \(D_z^2C_{\bar z\bar z}=D_{\bar z}^2C_{zz}\);
- oriented past/future corners of \(\mathcal I^+\) and their mirrors at
  \(\mathcal I^-\).

The same packet explicitly types antipodal matching as external physical
input. It does not provide a source-derived physical spatial-parity operator,
a time-reversal operator exchanging \(\mathcal I^+\) and \(\mathcal I^-\),
or their characters on one named radiative orientation line. Nor does it
compare those actions with Carrier road reflection and core exchange.

## Sharp non-identifications

Three tempting substitutions are mistyped:

1. A map of directions on the celestial sphere is not, by itself, the
   character of the spacetime spatial-orientation line.
2. The phrase *magnetic parity* in the Bondi corner constraint is not a
   time-reversal character.
3. An externally imposed antipodal matching condition is not a derived
   comparison with Carrier involutions.

Consequently the radiative sector neither verifies nor falsifies the twist.
It presently fails the provenance gate.

One component can nevertheless be derived exactly. In real stereographic
coordinates the packet's antipodal map is

\[
(x,y)\longmapsto
\left(-\frac{x}{x^2+y^2},-\frac{y}{x^2+y^2}\right),
\qquad
\det J=-\frac{1}{(x^2+y^2)^2}.
\]

It therefore reverses the celestial \(S^2\) orientation (degree \(-1\)).
This supplies the spatial-orientation character of the *celestial factor*,
not the missing physical time-reversal action or null-infinity
coorientation. Thus the unresolved object has narrowed from an unspecified
``orientation sign'' to the complementary normal/time factor and its
comparison with Carrier core exchange.

## Minimal decisive packet

An independent radiative test must export, before comparison:

1. a named one-dimensional radiative orientation object;
2. the physical \(P\)-action and its sign on it;
3. the physical \(T\)-action exchanging future and past null infinity and
   its sign on it;
4. the orientation sign carried by antipodal matching;
5. typed maps from Carrier road reflection and core exchange to those two
   physical actions.

Only then is the equation

\[
\chi_{\rm time}=\chi_{\rm pol}\chi_{\rm space}
\]

a cross-sector theorem rather than a compatible analogy.

## Meaning for the finite-speed program

Carrier incidence has supplied an unoriented finite reachability filtration.
The scattering comparison found that polarity alone cannot select future
from past under spatial reflection; it needs a spatial-orientation twist.
The radiative sector is therefore the right independent falsifier, but its
current exact packet has not yet typed the required \(P/T\) characters.

This is useful negative information: the causal arrow cannot be imported
from the word *antipodal*, from electric/magnetic sphere parity, or from a
matching convention. It must descend through an actual orientation object
and physical symmetry actions.

## Canonical candidate object from asymptotic geometry

There is a sharper object than an unspecified radiative line: the
determinant orientation line of null infinity. Locally,

\[
\operatorname{Or}(\mathcal I)
\cong
\operatorname{Or}(\text{null generator})
\otimes
\operatorname{Or}(S^2).
\]

With characters ordered as \((P,T)\):

\[
\chi_{\rm generator}=(+1,-1),\qquad
\chi_{S^2}=(-1,+1),
\]

because parity fixes retarded time and acts antipodally on the sphere,
whereas time reversal maps \(\mathcal I^+\) to \(\mathcal I^-\) with
advanced coordinate \(v=-u\) and leaves the spatial direction fixed.
Therefore

\[
\chi_{\operatorname{Or}(\mathcal I)}=(-1,-1).
\]

This is exactly the previously computed Carrier-polarity character. Thus
the unique character-compatible radiative comparison has now become

\[
\boxed{L_{\rm pol}\longrightarrow\operatorname{Or}(\mathcal I)}.
\]

Equivalently,

\[
L_{\rm time}
\cong
L_{\rm pol}\otimes L_{\rm space}
\]

is the determinant-line factorization of null-boundary orientation into
generator orientation and celestial orientation.

This establishes the character table, not the comparison morphism. The
remaining falsifier is now very narrow: construct the map from the Carrier
polarity line to \(\operatorname{Or}(\mathcal I)\) from a source-defined
soft/BMS comparison and test its naturality under antipodal matching.

## Automorphism no-go for the presently disconnected diagram

The existing Carrier and radiative packets do not share a source map. As a
diagram they are therefore a disjoint union. Multiplication by \(-1\) on
\(\operatorname{Or}(\mathcal I)\) is an automorphism of the radiative
character line and commutes with both \(P\) and \(T\). It leaves every
internal radiative character statement unchanged.

A prospective integral bridge is multiplication by some \(a\):

\[
L_{\rm pol}\xrightarrow{a}\operatorname{Or}(\mathcal I).
\]

The independent target sign automorphism sends \(a\mapsto-a\). Canonicity
with respect to all automorphisms of the input diagram therefore requires

\[
a=-a.
\]

Over characteristic zero this forces \(a=0\). In particular, neither of the
two integral isomorphisms \(a=\pm1\) is canonical from the disconnected data.

Thus the current frontier is not normalization by convention. A nonzero
bridge requires a genuinely cross-sector source object that couples the two
independent sign gauges—for example a source-derived soft boundary pairing,
a comparison chain map, or an oriented relative fundamental class whose two
restrictions are the Carrier relation cell and the null-boundary orientation.

This is a useful no-go result:

\[
\boxed{
\text{matching characters} + \text{separate internal naturality}
\not\Rightarrow \text{canonical comparison}.
}
\]

## The apparent Ward shortcut is mistyped

The exact \(m=3\) Carrier certificate does contain a map denoted
\(\Theta\) into a Ward quotient. That target is the marked-theta
graph/circuit Ward complex with a seven-component chain model. It is not the
BMS supertranslation Ward object on null infinity. The two uses of *Ward*
express a common conservation pattern but do not supply an identification.

The \(m=3\) certificate also explicitly retains two relevant defects:

- no scalar-first-jet map identifies the Carrier contact polynomials with
  physical Ward coefficients;
- the physical Cut has not been lifted to the oriented relation complex,
  including the image of its relation generator.

Therefore \(\Theta\) cannot break the sign-gauge no-go above.

## Correct bridge factorization

The source-derived radiative triangle already supplies the right half of a
more physical path:

\[
\text{gravitational amplitude}
\longrightarrow
\text{Weinberg soft residue}
\longleftrightarrow
\text{BMS Ward object}
\longleftrightarrow
\text{memory}.
\]

The first missing arrow is consequently

\[
\boxed{
L_{\rm pol}
\longrightarrow
L_{\rm soft}^{\rm grav},
}
\]

or, at chain level, a source-normalized gravitational soft realization of
the Carrier relation generator. It must retain reflection, polarity/core
exchange, helicity or deck data, and the soft boundary orientation. If this
map exists, composing it with the already verified radiative triangle is the
first legitimate way to produce
\(L_{\rm pol}\to\operatorname{Or}(\mathcal I)\).

Thus the frontier is no longer “compare Carrier directly with spacetime.” It
is the sharper amplitude question:

\[
\boxed{
\text{Does the Carrier relation cell have a canonical gravitational
soft residue?}
}
\]

## The scalar-scaffolded Yang--Mills route

The repository contains a nontrivial intermediate result. The six-point QTDS
transgression is derived from two scalar-scaffolded three-gluon residue
polynomials. Their conductor difference gives the intrinsic polarity-odd
symbol

\[
\sigma_{\rm alt}
=y_2dx_1+y_1dx_3+y_0dx_5-y_1dx_0-y_0dx_2-y_2dx_4,
\]

and one-step rotation preserves its ordered conormal orientation. Thus
polarity and a source-derived coefficient orientation already meet inside a
gauge-theory-flavored packet.

This is not yet a gravitational realization. The exported object is a
scalarized polynomial and its normal symbol. It retains neither a helicity or
polarization line, a BCJ numerator basis, a second gauge copy, a physical
state pairing, nor a soft-leg map compatible with the relation generator.
An unrelated inverse-KLT matrix cannot supply those missing typed maps.

The minimal left-hand construction has therefore sharpened to

\[
L_{\rm pol}
\longrightarrow
L_{\rm YM}^{\rm pol/BCJ}
\xrightarrow{\mathrm{double\ copy}}
L_{\rm soft}^{\rm grav}.
\]

The first arrow must enrich the known conductor symbol by an independently
defined polarization/BCJ coefficient object while retaining its
relative-normal provenance. Only then is the double-copy step typed.

## Helicity double-copy orientation gate

Let the Yang--Mills helicity doublet be

\[
H_{\rm YM}=\langle +,-\rangle,
\]

with parity acting by the swap matrix. Its determinant is \(-1\). On the
unprojected double copy \(H_{\rm YM}\otimes H_{\rm YM}\), parity is
\(P\otimes P\), whose determinant is \(+1\). Thus simply tensoring or
squaring the Yang--Mills coefficient loses the desired orientation
character.

The tensor square splits into two parity-stable doublets:

\[
G_{\rm grav}=\langle ++,--\rangle,
\qquad
G_{\rm mixed}=\langle +-, -+\rangle.
\]

Parity swaps the two basis states in each doublet, so each restricted
determinant line has character \(-1\). The first is the graviton helicity
sector; the second contains the mixed dilaton/two-form sector before its own
physical decomposition.

Therefore the orientation line needed by the Carrier comparison does not
come from double copy alone. It appears only after a typed physical-state
projection:

\[
H_{\rm YM}\otimes H_{\rm YM}
\xrightarrow{\Pi_{\rm grav}}
G_{\rm grav}
\xrightarrow{\det}
\det G_{\rm grav}.
\]

This isolates the next finite object: derive \(\Pi_{\rm grav}\) from the
source state pairing and test whether the polarity-odd conductor maps to
\(\det G_{\rm grav}\). Assigning the two conductor branches directly to the
two helicities would be extra data: the known branch exchange is a label
rotation, not physical parity.

### The graviton projector is fixed by the little group

In four dimensions the projector need not be fitted. Give each Yang--Mills
helicity doublet the operator \(h=\operatorname{diag}(1,-1)\). On the tensor
square define

\[
H_{\rm tot}=h\otimes1+1\otimes h.
\]

Its spectrum on \((++,+-,-+,--)\) is \((2,0,0,-2)\), so

\[
\boxed{
\Pi_{\rm grav}=\frac{H_{\rm tot}^2}{4}
=\operatorname{diag}(1,0,0,1).
}
\]

This operator is idempotent, has rank two, and is parity-natural because
parity sends \(H_{\rm tot}\mapsto-H_{\rm tot}\) while preserving its square.
Thus the physical graviton state sector is selected by little-group weight,
not by a branch convention.

The surviving obstruction is now narrower. The Carrier conductor is a scalar
normal symbol and has no little-group action. We still need a source map that
lifts it into the two-copy helicity complex before applying
\(\Pi_{\rm grav}\). The projector itself is no longer missing.

### Exact moduli of the missing branch-to-helicity lift

Let \(B=\langle F_+,F_-\rangle\) be the two conductor branches and
\(G=\langle ++,--\rangle\) the graviton helicity doublet. On both spaces let
parity act by the swap matrix \(P\). A general linear map \(M:B\to G\) is
parity-equivariant exactly when

\[
MP=PM,
\qquad\Longleftrightarrow\qquad
M=\begin{pmatrix}a&b\\b&a\end{pmatrix}.
\]

Thus parity leaves a two-parameter family, with determinant \(a^2-b^2\).
It does not canonically match branches to helicities and does not even force
the lift to be invertible.

If the branch doublet carries a source-derived little-group grading
\(h_B=\operatorname{diag}(1,-1)\), intertwining it with the graviton grading
forces

\[
Mh_B=h_GM
\qquad\Longrightarrow\qquad b=0,
\]

leaving only \(M=aI\). Primitive integral normalization then leaves the
expected global orientation pair \(M=\pm I\).

This proves that the missing datum is not another parity sign. It is a
little-group action on the conductor branch space, derived from an
unscalarized polarization-dependent three-gluon residue. Once present, it
removes the branch-mixing modulus; the remaining overall sign is precisely
the orientation torsor expected for a determinant-line comparison.

### Little-group weight obstruction of the scalar scaffold

The existing polynomial is genuinely the scalar-scaffolded
\(A_3^{\rm YM}\), but its variables \(X_{ab}\) are Mandelstam-type Lorentz
scalars. Hence every monomial and the complete conductor symbol have
little-group weight

\[
(0,0,0).
\]

By contrast, in standard spinor-helicity conventions,

\[
A_3(1^-,2^-,3^+)
\sim\frac{\langle12\rangle^3}{\langle23\rangle\langle31\rangle}
\]

has weight \((2,2,-2)\), while its parity conjugate has
\((-2,-2,2)\). A nonzero equivariant map between one-dimensional torus
characters exists only when their weights agree. Therefore neither helicity
amplitude can be reconstructed from the scalar-scaffolded polynomial alone.

The required enrichment is now characterized exactly: tensor the scaffolded
conductor with a polarization coefficient doublet carrying the two opposite
little-group characters. This coefficient is not optional bookkeeping; it is
the minimal representation needed for any nonzero helicity lift.

Thus the next admissible object is

\[
\sigma_{\rm alt}\otimes
\left(\mathcal L_{(2,2,-2)}\oplus
      \mathcal L_{(-2,-2,2)}\right),
\]

with its polarization-gauge descent and branch naturality derived before
double copy.

### Correction: the labelled helicity packet has six states

The preceding two-character expression describes one fixed exceptional-leg
choice. It is not closed under the three road/leg relabellings. The complete
labelled three-point packet contains

\[
\{(--+),(-+-),(+--),(++-),(+-+),(-++)\}.
\]

Equivalently, choose a sector—MHV or anti-MHV—and the exceptional-helicity
leg \(k\in\{0,1,2\}\). Hence the state set is

\[
\{\mathrm{MHV},\overline{\mathrm{MHV}}\}\times\{0,1,2\}
\cong S^0\times R_3.
\]

This is canonically the edge set of \(K_{2,3}\): the two vertices on one side
record helicity sector and the three on the other record the exceptional leg.
Parity exchanges the two cores, while label permutations act on the three
roads. The bijection is equivariant for

\[
S_2^{\rm parity}\times S_3^{\rm labels},
\]

the same abstract automorphism group as the six-point Carrier incidence
graph.

This substantially improves the candidate. The polarization coefficient is
not an unrelated doublet to be attached to the Carrier; its complete labelled
configuration space already has the Carrier's \(K_{2,3}\) shape. However,
shape and equivariance still do not identify the physical objects. The
remaining source test is whether the scalar-scaffolding fusion residue sends
each individually supported Carrier edge \((\text{core},\text{road})\) to
the helicity amplitude with the corresponding sector and exceptional leg.
That six-entry residue table would couple the sign gauges and construct the
missing bridge.

In fact full equivariance reduces the required table to one entry. A brute
force census of all \(6!=720\) bijections of the edge set finds that the
centralizer of the natural \(S_2\times S_3\) action contains exactly two
elements:

\[
1,qquad\text{global core/helicity-sector exchange}.
\]

Consequently one source-derived anchor—e.g. the helicity configuration of a
single fixed branch and cyclic sector—determines the other five by parity and
label naturality. The only alternative is global parity conjugation, exactly
the expected orientation torsor.

The next calculation is therefore exceptionally small:

\[
\boxed{
\text{evaluate one fixed scalar-scaffolding fusion residue in 4D
spinor-helicity variables and identify its exceptional leg.}
}
\]

If that anchor is nonzero and has the required little-group weight, the full
\(K_{2,3}\) Carrier-to-helicity bridge follows by symmetry. If the anchor is
weight zero or mixes the two helicity sectors, the proposed bridge fails.

### Superseding correction: scaffold cores are not helicity sectors

The abstract six-state bijection and its centralizer census are correct, but
their proposed physical interpretation used the wrong action. The scaffold
fusion conditions are Mandelstam equations. For a fused pair,

\[
q^2=\langle ab\rangle[ab]=0,
\]

so the fusion locus contains both its holomorphic and antiholomorphic spinor
branches. Physical parity exchanges these two factors while leaving all
Mandelstam variables \(X_{ab}\), the pairing labels, and each fusion stratum
\(F_\pm\) fixed.

Carrier core exchange is different: it is the one-step label rotation

\[
(12)(34)(56)\longleftrightarrow(23)(45)(61),
\]

which exchanges \(F_+\) and \(F_-\). Therefore identifying Carrier core
exchange with MHV/anti-MHV exchange conflates label transport with physical
parity.

There is no parity-equivariant bijection

\[
\{F_+,F_-\}\longrightarrow\{\mathrm{MHV},\overline{\mathrm{MHV}}\},
\]

because parity acts trivially on the source pair and by a swap on the target.
The two equivariant bijections counted previously exist only after *declaring*
Carrier core exchange to be parity—the very comparison that needed proof.

Hence the claimed one-anchor reduction is withdrawn as a physical bridge. The
correct refinement doubles each scaffold branch by its internal spinor branch:

\[
\widetilde F_\pm^{\rm spin}
=F_\pm^{\langle\rangle}\sqcup F_\pm^{[\ ]}.
\]

Physical parity acts within each \(\widetilde F_\pm^{\rm spin}\), while
Carrier core exchange acts between the \(+\) and \(-\) scaffold pairings.
The smallest faithful coefficient carrier therefore has at least four core
states before the three road labels are included. Any bridge must be built on
this refined spinor normalization, not on bare \(K_{2,3}\).

### The refined object is a correspondence between two \(K_{2,3}\) quotients

Let

\[
\widetilde E
=\{F_+,F_-\}
\times\{\langle\rangle,[\ ]\}
\times\{0,1,2\}.
\]

It has twelve states and two canonical projections:

\[
E_{\rm Carrier}
\xleftarrow{\ \pi_C\ }
\widetilde E
\xrightarrow{\ \pi_H\ }
E_{\rm helicity},
\]

where \(\pi_C\) forgets the spinor branch and \(\pi_H\) forgets the scaffold
pairing. Both endpoints have six states and the abstract \(K_{2,3}\) shape;
both projections have fibers of size two.

The two deck involutions commute:

- scaffold exchange acts on \(F_+\leftrightarrow F_-\);
- physical parity acts on
  \(\langle\rangle\leftrightarrow[\ ]\).

There is no spin-deck-equivariant section of \(\pi_C\), because the spin deck
acts trivially downstairs and freely upstairs. Similarly, there is no
scaffold-deck-equivariant section of \(\pi_H\). This gives a structural
explanation of the failed direct identification:

\[
\boxed{
E_{\rm Carrier}\not\cong E_{\rm helicity}\ \text{canonically};
\quad
\widetilde E\ \text{is their source-derived correspondence.}
}
\]

The legitimate bridge must therefore be push--pull through
\(\widetilde E\), with a specified invariant or anti-invariant deck sector,
not a pointwise identification of the two six-state sets. This returns us to
the recurring Marici mechanism: shared carrier incidence, sector-specific
coefficient cover, and a supported trace/Gysin operation.

### The deck character is uniquely forced

Write the scaffold and spin deck signs as \(c,p\in\{\pm1\}\). A
Carrier-polarity-odd class has the form

\[
f(c,k)=c\,a_k.
\]

There are four characters \(c^\alpha p^\beta\) on the commuting deck group.
For each, form the normalized weighted pushforward along the scaffold fiber:

\[
B_{\alpha\beta}(f)(p,k)
=\frac12\sum_{c=\pm1}c^\alpha p^\beta f(c,k).
\]

The complete census gives:

- \(\alpha=0\): the trace vanishes on every scaffold-odd input;
- \((\alpha,\beta)=(1,0)\): the output is spin-parity even;
- \((\alpha,\beta)=(1,1)\): the output is nonzero and spin-parity odd.

Hence exactly one character produces the desired bridge:

\[
\boxed{
\chi_{\rm bridge}=\chi_{\rm scaffold}\chi_{\rm spin},
\qquad
B(f)(p,k)=p\,a_k.
}
\]

This product character couples the two sign gauges and defeats the earlier
disconnected-diagram automorphism no-go. It is also the finite-cover form of
the orientation identity

\[
L_{\rm time}\cong L_{\rm pol}\otimes L_{\rm space}.
\]

What remains physical rather than algebraic is to derive this character local
system and normalized trace from the scalar-scaffolding/spinor residue map.
But there is no longer a choice among deck sectors: all alternatives vanish
or have the wrong parity.

### The normalized sign trace is integral on the typed lattice

The factor \(1/2\) does not introduce a rational ambiguity once the source is
restricted to the scaffold-odd lattice. On one double-cover fiber an integral
odd section is

\[
(f(-),f(+))=(-a,a).
\]

Its weighted trace numerator is

\[
\sum_{c=\pm1}c f(c)=2a,
\]

so the normalized trace returns \(a\in\mathbb Z\). The odd lattice
\(\mathbb Z(1,-1)=\ker[\mathbb Z^2\xrightarrow{(1,1)}\mathbb Z]\) is
primitive and saturated. Therefore the half-trace is an integral isomorphism
on the correctly typed submodule, although it is not an integral operator on
the entire unsplit \(\mathbb Z^2\).

This matters conceptually: the denominator is not fitted physics. It records
the degree-two cover and disappears after the anti-invariant coefficient
condition is imposed. The only residual \(\pm\) is the ordinary choice of
orientation generator.

### Geometry derives the product character

Both binary labels arise from normalization diagrams, not from an arbitrary
finite set. For a two-branch node the conductor sequence on branch values has
the form

\[
\mathbb Z\xrightarrow{\Delta}\mathbb Z^2
\xrightarrow{(-1,1)}Q\longrightarrow0,
\]

where \(Q\) is a primitive rank-one quotient and branch exchange acts on it
by \(-1\).

Apply this once to the alternating scaffold normalization and once to the
spinor factorization

\[
q^2=\langle ab\rangle[ab]=0.
\]

On the four local branches ordered as
\((++),(-+),(+-),(--)\), the two successive conductor differences have mixed
boundary

\[
\delta_p\delta_c
=\begin{pmatrix}1&-1&-1&1\end{pmatrix}.
\]

These coefficients are exactly \(cp\). The mixed quotient line is therefore

\[
Q_c\otimes Q_p,
\]

and both deck involutions act on it by \(-1\). Hence

\[
\boxed{
\chi(Q_c\otimes Q_p)=\chi_{\rm scaffold}\chi_{\rm spin}.
}
\]

So the unique character found by the finite trace census is independently
derived by the tensor product of the two normalization--conductor sequences.
The coefficient local system is no longer conjectural. What remains is the
section-level statement: the scalar-scaffolded amplitude must have a nonzero
mixed conductor grade in this line, compatible with the soft residue.
