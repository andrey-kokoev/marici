# String road/contact Z/3 carrier class and its physical-polarity no-go

## Authoritative scope correction

The \(\mathbb Z/3\) class constructed below is an exact invariant of the
unloaded road-orientation mapping problem.  It is not a physical phase of the
frozen once-relatively-polarity-loaded butterfly.

The established physical polarity line has the same reflection character as
the road-orientation line.  Loading it exactly once changes the coefficient
module and therefore the obstruction theory:

\[
\begin{array}{c|cc}
&H^1&H^2\\
\hline
\mathbb Z_{\rm or}&\mathbb Z/2&\mathbb Z/3\\
\mathbb Z_{\chi_N}=\mathbb Z_{\rm triv}&0&\mathbb Z/2.
\end{array}
\]

There is no coefficient map carrying the old \(\mathbb Z/3\) class into the
loaded \(\mathbb Z/2\) group.  Consequently the primitive rotation-linking
holonomy derived below is a carrier/coefficient diagnostic and a negative
control for physical typing.  It does not survive the declared physical
lens.

The actual frozen physical gate is the reflection-square class

\[
\omega_{\rm load}(f_3,f_3)\pmod2.
\]

If it is even, the once-loaded path component exists uniquely because loaded
\(H^1=0\).  If it is odd, the proposed loaded synthesis is obstructed.
Symmetric loading of both mapping endpoints would cancel the polarity line in
internal Hom and retain the old coefficient theory, but that is a distinct,
currently unconstructed variance and cannot be substituted for the physical
one-sided loading.

### Explicit once-loaded binary cocycle

Let \(\varepsilon(g)\in\{0,1\}\) record whether \(g\in D_3\) is a
reflection.  For the trivial loaded coefficient, put

\[
\omega_2(g,h)
=
\frac{\varepsilon(g)+\varepsilon(h)-\varepsilon(gh)}{2}.
\]

This is an integral normalized two-cocycle.  It vanishes on the rotation
subgroup and obeys

\[
\omega_2(f_3,f_3)=1.
\]

For a normalized integral one-cochain \(u\),

\[
(\delta u)(f_3,f_3)=2u(f_3),
\]

so reflection-square parity is representative-independent and the displayed
generator is not an integral coboundary.  Its double is exact:

\[
2\omega_2=\delta\varepsilon.
\]

Therefore the physical loaded comparison has exactly two possibilities:

\[
\begin{array}{c|c}
\omega_{\rm load}(f_3,f_3)\pmod2 & \text{conclusion}\\
\hline
0 & \text{unique loaded realization exists}\\
1 & \text{loaded realization is obstructed}.
\end{array}
\]

The formula constructs the universal generator, not the actual geometric
defect.  Computing which row applies still requires the paired
\(x_3/x_4\) endpoint connector with both Tor grades and lower Cousin terms.

### Present data cannot select the binary class

The target-side \(x_3/x_4\) purity packet is already strict under physical
reflection.  Its reflection square is the identity after the one retained
polarity sign cancels road orientation.  This includes both repeated-normal
Tor grades, the graph Bockstein, all lower Koszul--Čech terms, and endpoint
exchange.  Hence it contributes zero to the global binary class:

\[
\omega_{\rm global}=\omega_{\rm source}.
\]

On the source side, the primitive hemisphere \(Q\)-row has Smith factor one,
but adjoining the endpoint reflection row leaves Smith factors

\[
(1,2).
\]

Thus saturated \(Q\)-normalization does not select connector parity.  The two
formal cocycles

\[
\omega^{(0)}=0,\qquad \omega^{(1)}=\omega_2
\]

agree on every rotation restriction and all currently exported
\(Q\)-normalization data.  They differ precisely at

\[
\omega^{(0)}(f_3,f_3)=0,\qquad
\omega^{(1)}(f_3,f_3)=1.
\]

This is an identifiability theorem for the frozen artifacts: no additional
rank census, target-purity check, or rotation-sector calculation can decide
existence.  The source connector two-cell itself carries the missing bit.

### Bockstein pipeline localizes the bit to the wall correction

The shifted corridor is not parity-neutral.  Reflection exchanges its
ordinary and suspended branches, forcing the odd sign-valued one-cocycle

\[
a_{\rm susp}=1
\in H^1(C_2;\mathbb Z_{\rm sign})\simeq\mathbb Z/2.
\]

Inflation along the parity quotient \(D_3\twoheadrightarrow C_2\) sends this
to the unique generator of

\[
H^1(D_3;\mathbb Z_{\rm or})\simeq\mathbb Z/2.
\]

The normalization--conductor sequence has an isomorphic polarity Bockstein

\[
\partial_{\rm pol}:
H^1(D_3;\mathbb Z_{\rm or})
\xrightarrow{\ \simeq\ }
H^2(D_3;\mathbb Z_{\rm triv}),
\]

and at cochain level

\[
\partial_{\rm pol}(a_{\rm susp})(g,h)
=
\frac{\varepsilon(g)+\varepsilon(h)-\varepsilon(gh)}2
=\omega_2(g,h).
\]

Therefore the shifted corridor alone gives the obstructed class.  The same
source analysis requires a wall-supported excess triangle and forbids
deleting its lower Čech/endpoint term.

The later literal wall construction fixes the local correction.  The six
oriented common triangulation vertices realize the full three-axis Boolean
packet with one uniform Gysin shift.  In that packet, the odd two-boundary
suspension cocycle is precisely the truncation shadow of changing which
vertex axis is omitted.  Restoring the third axis and the physical
reflection \(v\mapsto3-v\) therefore supplies

\[
a_{\rm wall}=1\pmod2.
\]

The oriented Kato--Nakayama augmented interval independently constructs the
third wall term: reflection reverses both the interval and anti-diagonal wall
orientations, while the uniform odd Gysin shift retains the required graded
correction.  Thus at the local wall stage

\[
\boxed{
\omega_{\rm local}
=1+a_{\rm wall}
=1+1
=0\pmod2.
}
\]

This closes the local coefficient obstruction: the corridor and its
source-required wall cannot be separated, and their binary classes cancel.
It does **not** yet prove the global loaded synthesis.  The later finite
exit-path calculation does construct the KN-to-literal pushforward at every
vertex and edge grade, and the oriented \(dP_6\) boundary derives three
endpoint and three centre connector cells.  Moreover, the resulting finite
endpoint mapping-fibre candidate predicts

\[
p_{\partial,Q}=0,
\qquad
\partial_{\rm pol}p_{\partial,Q}=0.
\]

But these columns have not been identified with the actual
normalization-provenanced support/nearby-cycle restriction into the literal
endpoint costalks.  The endpoint \(Q\)-mapping fibre is therefore still
uninstantiated as a physical object.  The smallest remaining test is one
provenance square: construct \(r_{\partial,Q}\) from the full source kernel
and show that its endpoint, centre, and generic \(q_\Sigma\) columns are the
already certified primitive finite columns.

There is no remaining parity freedom inside that square.  The complete
27-state endpoint-star sign-naturality graph is connected, and its anchored
solution is unique.  Positive normalization fixes the anchor.  Consequently
any admissible spatial comparison is forced to equal the finite comparison,
including its zero endpoint class and zero Bockstein.  The final dichotomy is
therefore

\[
\boxed{
\begin{array}{c|c}
r_{\partial,Q}\text{ exists}
  &\text{unique global loaded realization}\\
r_{\partial,Q}\text{ does not exist}
  &\text{the proposed source-to-literal synthesis is mistyped}.
\end{array}}
\]

A different nonzero endpoint parity is not a third outcome: it would violate
the already-proved anchored naturality equations.

### The normalization connector closes the binary gate

The remaining existence branch was subsequently realized.  The two labelled
positive exceptional rays have boundary \(r_1-r_{D03}\), while the two
normalization costalks have oriented difference \(e_+-e_-\).  A
reflection-equivariant integral comparison necessarily has the form

\[
M(a,b)=\begin{pmatrix}a&b\\b&a\end{pmatrix}.
\]

Boundary compatibility and the normalized endpoint counit impose

\[
b-a=1,
\qquad
a+b=1.
\]

Their unique integral solution is

\[
\boxed{
M=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad \det M=-1.
}
\]

Thus the comparison is unimodular and source-selected, with
\(r_{D03}\mapsto e_-\) and \(r_1\mapsto e_+\).  It instantiates the complete
three-road endpoint/\(Q\) mapping fibre and promotes the formerly conditional
calculation to

\[
\boxed{
p_{\partial,Q}=0,
\qquad
\partial_{\rm pol}p_{\partial,Q}=0.
}
\]

Together with the local corridor--wall cancellation and loaded \(H^1=0\),
this proves the unique once-polarity-loaded endpoint/\(Q\) realization in the
frozen source problem.  The selected zero class is also fixed by the full
endpoint \(D_8\) transport and has zero scalar Jordan obstruction.  This does
not identify the higher matrix-valued octagonal coherence with the full
Jordan differential; that is a downstream, non-scalar question rather than
a reopening of endpoint parity.

### Zero obstruction still retains primitive holonomy

The downstream octagonal audits close the apparent non-scalar loophole but
leave a more informative object.  The four occurrence-resolved PC square
faces and four Jordan square faces are canonically identical; their chain
comparison is unimodular and \(D_8\)-equivariant, and every square curvature
vanishes.  Globally, however, the Möbius carrier has primitive core
\(\gamma\) and dual class \(\omega\) with

\[
\langle\omega,\gamma\rangle=1,
\qquad
[\partial O]=2[\gamma].
\]

Thus the zero mod-two endpoint class is the shadow of a nonzero integral
crosscap class:

\[
2\bmod2=0.
\]

For the occurrence road lattice

\[
0\longrightarrow A_2
\longrightarrow P_D=\mathbb Z^3
\xrightarrow{\epsilon_D}\mathbf1
\longrightarrow0,
\]

the failure of any road section to invert \(\epsilon_D\) has image exactly
in the genuine two-dimensional contact sector \(A_2\).  In the primitive
Verdier quotient by the thick contact subcategory, all three road roofs
become the same canonical inverse and the orientation line has

\[
\boxed{
\operatorname{Hol}(\gamma)=-1,
\qquad
\operatorname{Hol}(\partial O)=+1.
}
\]

This is not permission to discard \(A_2\): it is physical QTDS contact data.
The required recollement/filtered enhancement has now been constructed.  The
occurrence permutation lattice sits in the nonsplit integral sequence

\[
0\longrightarrow A_2\longrightarrow \mathbb Z[C_3]
\xrightarrow{\epsilon}\mathbf 1\longrightarrow0,
\]

whose extension class generates
\(\operatorname{Ext}^1_{\mathbb Z[C_3]}(\mathbf1,A_2)\cong\mathbb Z/3\).
The resulting filtered Jordan atlas exists and is rigid, and the global
mixed-variance fs/Kato transform lands on the unique framed connector.  Its
physical six-point pullback has

\[
H_1\cong\mathbb Z,
\qquad H_i=0\quad(i\ne1),
\]

with primitive road augmentation \(+1\).  Thus the obstruction has not been
erased: it has been reorganized into a rigid filtered object whose supported
physical realization is a primitive line.

### Eight-point descent fixes the variance of overlap maps

The next multiplicity test also closes.  The eight loaded Cut charts contain
\(8\cdot1075=8600\) generators and their twelve pair overlaps contain
\(12\cdot125=1500\).  The naive audit found 7,320 radial arrows leaving a
retained overlap and initially mistook them for a chain-map obstruction.  The
correct variance reverses the diagnosis: the overlap is the coordinate
**quotient** by the discarded subcomplex.  Escaping arrows are therefore
killed on both sides.  The actual obstruction would be an arrow from a
discarded source into a retained target, and the exhaustive count is

\[
\boxed{\text{entering arrows}=0}.
\]

Together with 7,200 agreeing internal arrows and the native odd Thom line,
this gives a cellwise total differential with

\[
D_{\rm tot}^2=0
\]

and a primitive global section.  Hence full eight-point Thom-twisted Cut
descent exists in the cellular fs/Kato sector.

The conceptual consequence is sharper than existence alone.  A common
support locus does not determine a restriction map by set inclusion.  Its
source-derived variance determines whether the legal operation is a
pullback, an exceptional restriction, or a quotient.  Here the difference
between a false obstruction and exact descent is precisely the difference
between treating the overlap as a subobject and treating it as a supported
quotient.

### General Cut-localization quotient theorem

The directional zero is a multiplicity-independent statement.  For a
loaded Cut chart \(C_D\) and a second compatible Cut \(D'\), let
\(K_{D'}\subset C_D\) be generated by faces incompatible with \(D'\).  Then
one has

\[
dK_{D'}\subseteq K_{D'},
\qquad
C_D/K_{D'}\cong C_{DD'}.
\]

Indeed, a normal differential changes only the marking subset and leaves the
face fixed, while a radial differential enlarges the face.  Hence an existing
diagonal crossing cannot disappear under either move.  Every pairwise Cut
restriction is therefore the canonical localization
quotient

\[
r^!_{D,D'}:C_D\twoheadrightarrow C_D/K_{D'},
\]

and “no entering arrows” follows from source combinatorics rather than a
multiplicity-eight rank accident.  An exhaustive trap-check over every
diagonal Cut and compatible ordered Cut pair for polygon sizes \(5\) through
\(8\) tests 116,580 radial-arrow incidences and finds no entering arrow.

The same proof applies to any compatible Cut family \(S\).  If \(K_S\) is
generated by faces incompatible with at least one member of \(S\), then

\[
dK_S\subseteq K_S,
\qquad
C_D/K_S\cong C_{D\cup S}.
\]

Thus the construction supplies every higher Čech restriction whenever the
physical Cut nerve has higher intersections.  The remaining global datum is
cleanly separated: the carrier supplies a cosimplicial system of localization
quotients, while the
native Thom-normal local system decides whether their Čech nerve has a
primitive global section.

The cosimplicial identities are strict rather than merely coherent.  For Cut
families \(S\subseteq T\), the discarded kernels are nested,

\[
K_S\subseteq K_T,
\]

so the direct quotient to the \(T\)-overlap equals the successive quotient
through the \(S\)-overlap.  In particular, on every compatible Cut triple,

\[
r^!_{D,D',D''}
=r^!_{DD',D''}\,r^!_{D,D'}
=r^!_{DD'',D'}\,r^!_{D,D''}.
\]

No fitted overlap homotopy is needed at the cellular carrier level.  Any
higher coherence still required by the physical theory must therefore enter
through coefficient, Thom, or relative-chain data rather than through an
ambiguity of the Cut localization maps themselves.

The theorem is scoped to the declared loaded differential.  A future
differential operation that can remove a crossing diagonal would fall outside
its hypotheses and must be audited afresh; one arrow from \(K_S\) into its
complement would falsify localization for that enlarged calculus.

## Source problem

The paired endpoint packet has a legal compositional target: construct the
loaded normalization--conductor morphism and two endpoint connector cells so
that the correspondence homotopy limit satisfies

\[
d_{\rm sp,sc}^2=0
\]

and the Cousin chain equation.  At coefficient/carrier level, the
endpoint-fixed mapping fibre has tangent

\[
R\!\operatorname{Hom}_{\mathbb Z[D_3]}
(\mathbb Z,\mathbb Z_{\rm or})[1],
\]

with component torsor \(\mathbb Z/2\) and next obstruction

\[
\operatorname{Ext}^2_{\mathbb Z[D_3]}
(\mathbb Z,\mathbb Z_{\rm or})
\cong\mathbb Z/3.
\]

This is structurally different from the cosmology candidates.  The torsion
class is already the obstruction group of a predeclared legal *unloaded*
composition; it is not being imported to explain a rank anomaly.  Physical
polarity subsequently replaces this obstruction theory rather than promoting
its three-primary class.

## Why the order-three obstruction survives reflection

Write

\[
D_3=C_3\rtimes C_2.
\]

Rotation acts trivially on the orientation coefficient
\(\mathbb Z_{\rm or}\), while reflection acts by \(-1\).  Restriction to
\(C_3\) gives

\[
H^2(C_3;\mathbb Z)\cong\mathbb Z/3.
\]

Reflection contributes two signs:

1. conjugation \(g\mapsto g^{-1}\) acts by \(-1\) on the degree-two cyclic
   class;
2. the orientation coefficient contributes another \(-1\).

Their product is \(+1\).  Therefore the full \(D_3\)-invariant obstruction
survives:

\[
(-1)_{\rm cyclic}\,(-1)_{\rm orientation}=+1,
\qquad
H^2(D_3;\mathbb Z_{\rm or})\cong\mathbb Z/3.
\]

This is the same signed/Real distinction exposed by the corrected \(A_2\)
audit: bare occurrence reflection and orientation-loaded reflection are not
the same operation.

## Deutsch--Popperian prediction

The coupling-necessity conjecture makes a nontrivial prediction at the
unloaded carrier stage.  If an unloaded string correspondence is pointed, its
source-derived comparison and connector cells must
either:

1. trivialize the \(\mathbb Z/3\) obstruction coherently; or
2. retain it as a flat order-three differential character/holonomy record.

The second outcome gives a carrier-level realization of

\[
\boxed{
\text{composition obstruction}
\longrightarrow
\text{flat }\mu_3\text{ record}.
}
\]

It becomes a physical realization only under a separately source-derived
readout that retains \(\mathbb Z_{\rm or}\).  The declared one-sided physical
polarity loading does not.  The conjecture is falsified here if the relevant
composition closes while the
connector cells neither account for the obstruction nor produce a coherent
nullhomotopy, or if an arbitrary connector choice changes the physical result.

## Explicit cocycle and connector acceptance contract

Write an element of \(D_3\) as \((a,e)\), with \(a\in\mathbb Z/3\),
\(e\in\mathbb Z/2\), and

\[
(a,e)(b,d)=(a+(-1)^e b,e+d).
\]

The exact checker constructs a normalized integral two-cocycle \(f\) for the
orientation action.  On the rotation subgroup it is the carry cocycle

\[
f((a,0),(b,0))=\left\lfloor\frac{a+b}{3}\right\rfloor,
\qquad a,b\in\{1,2\}.
\]

It satisfies the full twisted \(D_3\) cocycle equation.  It is not an
integral coboundary: restriction to \(C_3\) would force

\[
u(2)=2u(1),\qquad 3u(1)=1.
\]

But \(3f\) is an integral coboundary.  One normalized trivializing cochain,
ordered on

\[
(1,0),(2,0),(0,1),(1,1),(2,1),
\]

is

\[
u_3=(1,2,-2,-1,0),\qquad \delta u_3=3f.
\]

This yields a strictification acceptance contract, but its variance matters.
Let \(c_{\rm add}\) be the degree-two correction derived from the loaded sheet
morphism \(\alpha_{\rm sh}^{!,\check C}\) together with the fixed road
inclusion.  An integral pointed strictification is legal only if

\[
\boxed{
[c_{\rm add}]=-[f]
\quad\text{in}\quad
H^2(D_3;\mathbb Z_{\rm or}),
}
\]

equivalently, if the two endpoint connector cells assemble to an integral
one-cochain \(u\) with

\[
f+c_{\rm add}=\delta u.
\]

Cancellation after tensoring with a field, cancellation of one scalar
evaluation, or the identity \(3f=\delta u_3\) does not pass this gate.  The
loaded sheet/road comparison must supply the opposite cohomology class if a
strict integral pointing is claimed.  The
endpoint connector cells cannot do so by themselves: as one-cochains, their
coboundaries have zero cohomology class.  Their role is to witness the
integral nullhomotopy after the degree-two obstruction has cancelled and to
select the remaining \(\mathbb Z/2\) component.  If instead the totalization
retains the unsplit class as a flat record, no cancellation is required, but
its readout must factor through the
resulting \(\mu_3\) differential character and be independent of the chosen
cocycle representative.

### Minimal rotation-sector test

The Lyndon--Hochschild--Serre calculation shows that restriction detects this
three-primary class:

\[
H^2(D_3;\mathbb Z_{\rm or})
\longrightarrow
H^2(C_3;\mathbb Z)
\simeq\mathbb Z/3.
\]

Consequently the loaded comparison need not initially export a full
\(D_3\) two-cochain.  For a normalized rotation-restricted cocycle \(c\), put

\[
\kappa(c)=c(r,r)+c(r^2,r)\pmod 3.
\]

If \(c\) changes by the integral coboundary of \(u\), then

\[
\kappa(c+\delta u)-\kappa(c)=3u(r)=0\pmod 3.
\]

Thus \(\kappa\) is an integral-gauge invariant.  The explicit generator has

\[
\kappa(f)=1.
\]

The smallest decisive export from the loaded sheet/road geometry is therefore
\(\kappa(c_{\rm add})\), interpreted branchwise:

\[
\boxed{
\begin{array}{c|c}
\kappa(c_{\rm add}) & \text{typed consequence}\\
\hline
2 & \text{integral strictification may exist}\\
0 & \text{original unsplit obstruction is retained}\\
1 & \text{nonzero inverse residual; neither branch closes}
\end{array}}
\]

Value \(2\) opens the connector-cell nullhomotopy test.  Value \(0\) is legal
only if the physical object and its readout remain genuinely unsplit.  Value
\(1\) leaves total class \(2\) and supports neither interpretation,
independent of all endpoint connector choices.

## Identification with the older endpoint obstruction

The unsplit endpoint skeleton had already found that a strict equivariant
representative of the primitive unit would require

\[
3c=1
\]

in the rotation sector and \(2a=1\) in the reflection sector.  The first
equation is exactly the class \(\kappa(f)=1\); the explicit cocycle identifies
the source of the previously observed denominator three.  The second equation
belongs to the independent component torsor \(\mathbb Z/2\).

The primitive hemisphere \(Q\)-row has Smith factor one, while the endpoint
reflection row retains Smith factor two.  Consequently neither saturated
\(Q\)-normalization nor a choice of endpoint parity changes the
three-primary class.  The loaded geometry must report two independent data:

\[
\bigl(\kappa(c_{\rm add}),p_{\partial,Q}\bigr)
\in\mathbb Z/3\oplus\mathbb Z/2.
\]

This direct-sum notation records independent finite diagnostics; it does not
assert that the completed mapping space splits canonically.

### Primary-separation theorem at the obstruction truncation

The independence can be strengthened at the one-truncated coefficient level.
Cross-primary maps and extensions vanish:

\[
\operatorname{Hom}(\mathbb Z/2,\mathbb Z/3)
=
\operatorname{Hom}(\mathbb Z/3,\mathbb Z/2)
=0,
\]

\[
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/2,\mathbb Z/3)
=
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/3,\mathbb Z/2)
=0.
\]

The reflection action on the three-primary obstruction is trivial because
cyclic inversion and the orientation coefficient contribute two cancelling
signs.  Also,

\[
H^{n>0}(C_2;\mathbb Z/3)=0,
\]

since averaging by \(1/2=2\pmod 3\) is available.  Therefore no hidden
Postnikov extension at this truncation lets the endpoint
\(\mathbb Z/2\)-component alter the \(\mathbb Z/3\) obstruction.

This is still not a claim that the full geometric mapping space is a literal
product.  Higher support, filtration, and six-functor data remain capable of
coupling the sectors.  It proves only the decisive negative statement:
choosing endpoint parity cannot repair the cyclic obstruction.

## What can read a retained class

On the rotation subgroup the class is Ext-derived:

\[
H^2(C_3;\mathbb Z)
\simeq
\operatorname{Ext}^1_{\mathbb Z}
\bigl(H_1(C_3;\mathbb Z),\mathbb Z\bigr),
\qquad
H_1(C_3;\mathbb Z)\simeq\mathbb Z/3.
\]

Therefore the natural readout is not evaluation on an ordinary two-cycle.
It is the torsion-linking pairing with the rotation one-cycle.  The exact
rational trivializer of \(f\) has

\[
u(r)=\frac13,\qquad u(r^2)=\frac23,
\]

and hence gives the primitive flat holonomy

\[
\operatorname{hol}_f(r)
=
\exp(2\pi i/3).
\]

Signed reflection preserves it:

\[
-u(r^2)=-\frac23\equiv\frac13=u(r)\pmod1.
\]

This makes the physical-readout gate precise.  In the unsplit-retention
branch, the loaded correspondence must transport the labelled road-rotation
torsion loop to a source-admissible physical relative loop or current, and
the readout must reproduce this linking value.  Without that transport, the
primitive \(\mu_3\) holonomy is a coefficient record only.  In the
strictification branch the total class vanishes and this holonomy is removed.

### The road packet already contains the torsion loop

The augmented road triangle is the standard cyclic packet with maps

\[
N=1+r+r^2,\qquad 1-r,\qquad \epsilon.
\]

After derived \(C_3\)-coinvariants these become

\[
N\longmapsto 3,\qquad 1-r\longmapsto0.
\]

Hence the relevant coinvariant portion is

\[
\mathbb Z\xrightarrow{3}\mathbb Z\xrightarrow{0}\mathbb Z,
\]

and its torsion homology is canonically \(\mathbb Z/3\).  Thus the rotation
loop needed by the linking character is already source-labelled on the
coefficient side; it was not introduced by the cocycle checker.

The remaining physical map is correspondingly narrow.  The loaded
normalization--conductor correspondence must induce a map from this derived
coinvariant generator to a physical relative loop/current, and that image
must be nonzero for the retained \(\mu_3\) phase to be observable.  A zero
image makes the class physically silent without trivializing it
mathematically.

## Current boundary

Carrier curvature vanishes, so the abstract torsor is nonempty.  But the
loaded normalization--conductor morphism and endpoint connector cells remain
unconstructed.  Hence no physical \(\mu_3\) phase is claimed.  This document
identifies the string packet as the first correctly typed positive test—not
as a completed activation theorem.

## Evidence

- `research/voevodsky/context.md`, current endpoint packet frontier;
- `research/nima/checkers/check_string_road_contact_z3_obstruction.py`;
- `research/nima/results/string-road-contact-z3-obstruction.json`;
- `research/nima/checkers/check_string_road_contact_z3_cocycle.py`;
- `research/nima/results/string-road-contact-z3-cocycle.json`;
- `research/nima/checkers/check_string_loaded_polarity_z2_cocycle.py`;
- `research/nima/results/string-loaded-polarity-z2-cocycle.json`;
- epistemic event `ev-000000002621-4f383534-5ce7-4329-a202-e9b1d140cf39`;
- typing correction and supersession event
  `ev-000000002622-9c7af70c-14d4-40d1-84b0-ad4992fceb52`;
- minimal rotation-sector gate event
  `ev-000000002624-685abcb1-6726-4922-ba09-848ad8fcd9fc`;
- strictification/retention correction and linking interface event
  `ev-000000002626-348d984a-4f32-4aaa-868a-186e3a204c56`;
- canonical road derived-coinvariant generator event
  `ev-000000002627-38440880-293c-4bea-95f0-2825a21c569f`;
- physical-polarity no-go, binary successor problem, and explicit loaded
  cocycle event `ev-000000002628-2572b91f-320a-40dd-8ae7-54b6b79a6e19`;
- one-bit source-connector identifiability boundary event
  `ev-000000002629-d666149d-b693-4063-a4ff-314388130979`.
