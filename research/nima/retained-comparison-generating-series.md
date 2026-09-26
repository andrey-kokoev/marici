# A generating operator from actual retained comparisons

## Starting point, not a repeated construction

The prior whole-package and native-table results already retain comparisons,
higher witnesses and their histories. This experiment consumes them. It neither
re-proves fiber recovery nor inserts a desired scalar potential into a toy lift.

Active SCC obligations: forward realization of an existing comparison as an
operator, compatibility with composition and higher paths, then scalar readout.

Source: `BoundaryGeneratedQuestions.fourQ`, whose values are pairs of Booleans and
whose selected value is (false,false). Its existing `identity fourQ` and
`swap-filler` are different pointed equivalences of the SAME complete boundary.
The existing `truth-identifies-fillers` theorem shows that their Boolean question
answers agree. `NativeTableRegression.actual-filler-equivalence` already transfers
these actual witnesses unchanged to native packages.

## The constructed operator and series

For an actual filler f, define its pullback on functions on the source values:

\[
(T_fv)(x)=v(f(x)).
\]

This does not assign a fitted number to a witness. It evaluates the equivalence
already stored in that witness. In particular it preserves all pointwise operations;
on rational-valued functions it is linear. Its variance is explicit:

\[
T_{g\circ f}=T_fT_g,\qquad T_{f^{-1}}T_f=1.
\]

Agda proves identity, composition, inverse and compatibility with paths between
fillers. Reification and the native-package transfer preserve this readout.
This representation is not asserted faithful on complete resolution histories;
finite pointed equivalences are the tested source sector.

Now form the ordinary generating series of repeated application of that same
comparison:

\[
G_f(z)=\sum_{n\geq0}z^nT_f^n=(1-zT_f)^{-1}.
\]

The inverse is a formal power-series inverse, since the constant coefficient is
identity. z records the number of comparison applications. It is not physical time,
a field variable or a source-selected geometric deformation. Choosing an ordinary
rather than exponential generating series is part of this construction, not a
uniqueness claim about generating functionals.

The precise derivative-of-difference identity is

\[
\left.\frac{d}{dz}(G_f-G_g)\right|_{z=0}=T_f-T_g.
\]

Thus an operator-valued version of the proposed mechanism can be constructed from
retained comparison data. It does not yet identify that derivative with a physical
force, action variation, or curvature of the input/output fibration.

## Actual source calculation

Order the values as 00,01,10,11. The imported identity has images (0,1,2,3), while
the imported coordinate swap has images (0,2,1,3). Both image tuples are checked by
Agda reflexivity against the actual source maps, and the Python checker parses
those proof statements rather than supplying an unrelated permutation fixture.

Write P for the swap operator. Since P squared is identity,

\[
G_{\rm id}(z)=\frac{1}{1-z}1,\qquad
G_{\rm swap}(z)=\frac{1+zP}{1-z^2}.
\]

Their first differential comparison is

\[
P-1=
\begin{pmatrix}
0&0&0&0\\
0&-1&1&0\\
0&1&-1&0\\
0&0&0&0
\end{pmatrix}.
\]

It vanishes at the selected point 00, but not as an operator on the full retained
carrier. The trace series difference is `-2 z/(1-z^2)`: odd repetitions have two
fewer fixed values than identity; even repetitions agree.

`no-truth-factor` proves that even the first operator coefficient cannot be
recovered from the old double-negation truth quotient. The source truth equality
would force false=true under a supposed factorization. The construction therefore
uses precisely a distinction that the retained witness contains and the Boolean
answer forgets.

## The involution makes the response integrable: an actual quadratic action

There is a further positive result connecting the proposed involution to an action.
Use the finite counting pairing on rational functions on the four source values.
The permutation operator P is orthogonal. Because the chosen comparison is an
involution, P is also self-adjoint. Put R=1-P and let phi be a formal assignment of
a scalar to each source value. Then

\[
S_P(\phi)=\tfrac12\langle\phi,(1-P)\phi\rangle,
\qquad \nabla S_P=(1-P)\phi.
\]

Thus the negative of the generating-series differential response has a scalar
primitive. For the actual source swap it is

\[
S_P(\phi)=\tfrac12(\phi_{01}-\phi_{10})^2.
\]

The graph edge and its relative coefficient come from the stored comparison;
no separate graph or desired potential was inserted. The factor one-half is
fixed by integrating the prescribed linear response. An additive constant remains
invisible; this expression sets S(0)=0. This is a dimensionless algebraic action,
not yet a selected physical theory. The probe field phi, linear-response readout
and finite counting pairing are declared; the source does not prove that nature
uses this representation or this pairing.

The residual identities now have an operational realization:

\[
\phi=P\phi+R\phi,\qquad R(P\phi)=-R\phi,\qquad R^2=2R,
\qquad S_P(P\phi)=S_P(\phi).
\]

These equations concern the action of an existing comparison on scalar probe
assignments. They do not subtract differently typed raw and grouped tables.

The Hessian is R, with rank one and a three-dimensional kernel. Its inverse exists
on the anti-invariant sector only:

\[
\Pi_-=\tfrac12(1-P),\qquad K_-^{-1}=\tfrac14(1-P),\qquad
R K_-^{-1}=K_-^{-1}R=\Pi_-.
\]

The checker rejects interpreting this as an inverse on the whole four-dimensional
space. No pole prescription or quantum Gaussian measure is inferred. The fourth
variation is zero: this comparison produces a quadratic action, not the previously
declared quartic scalar interaction.

There is a sharp source-level hostile. A nontrivial three-cycle is also an admitted
pointed comparison, but 1-P is not symmetric, so its prescribed linear response
has no scalar primitive in this pairing. Symmetrizing would change that response.
Among the six pointed source maps, exactly the identity and three transpositions
pass. Involution is therefore doing actual work in the action construction.

## Derived orientation weight; scalarization has a kernel

On the determinant line of the finite function space the induced weights are

\[
\det T_{\rm id}=+1,\qquad \det T_{\rm swap}=-1.
\]

These signs are computed from the existing maps, not supplied as coupling values.
Determinant is unchanged by simultaneous basis relabelling and is multiplicative
under the actual comparison composition. Using the determinant line as the physical
observer, however, is not selected by the source interface.

The whole pointed automorphism group here is S3: it permutes the three nonselected
values. Exact enumeration checks all six maps and all 36 compositions. Their full
operator matrices are distinct. Scalar multiplicative characters have only two
possibilities over the complex numbers: the trivial character and sign.

Written classification: transpositions are conjugate, so a scalar character gives
them one common value c. Their order two forces c squared to be one. Transpositions
generate S3, and a three-cycle is a product of two of them. Thus c=+1 gives the
trivial character, c=-1 gives sign, and every three-cycle has weight +1 in either.
The checker exhausts all sign assignments and obtains exactly these two characters.

Consequences:

- Determinant detects swap versus identity, but loses nonidentity three-cycles.
- Spectral determinants distinguish only three conjugacy classes, not all six maps.
- A real additive action on this finite group must vanish, since every element has
  finite order. A phase character can nevertheless carry the order-two sign.
- Comparison-character weights are not quartic vertex couplings. This construction
  does not identify its -1 with a Feynman vertex or predict the fixture's 3/5.

The quadratic primitive above and the determinant character are different
readouts. Selecting a scalar character neither selects that action physically nor
supplies the missing quartic interaction.

## Control on the original schedule square

The original `ObserverCoherenceCube.Geometry` independently expands two factors.
Its actual `route-homotopy` equates the two composite maps while retaining their
different schedules. The new generic `SquareControl.readout-equal` imports that
homotopy and proves equal map-based observations. An explicit nontrivial expansion
control has operators P tensor 1 and 1 tensor P; they commute on all 16 states.

Therefore this readout gives ZERO defect for that original independent-expansion
square. The identity/swap pair above is a different, already existing comparison
pair; it must not be substituted for the square and advertised as its curvature.
Retained order remains present in the source but is not observed by this particular
function-space representation.

Also, G itself is not a multiplicative comparison weight: even G_id squared is
not G_id. Composition applies to T and its determinant, not to multiplying these
iteration generating series without a new sewing law.

## Verification

New module: `agda/RetainedComparisonSeries.agda`. Fresh safe/cubical compilation
passes, including its 24 local module dependencies. The symbolic checker verifies
formal resolvent identities, the differential response and its quadratic primitive,
Hessian/sector-inverse identities, the three-cycle integrability obstruction, six
pointed bijections, composition/inverses, the two scalar characters, scalarization losses
and the original square control. Series coefficient regressions additionally cover
n=0..12; the rational resolvent identity and Agda two-periodicity are not limited
to that range.

```text
pwsh -NoProfile -File research/nima/checkers/check_retained_comparison_series.ps1 -Fresh
uv run --with sympy python research/nima/checkers/check_retained_comparison_series.py
uv run --with sympy python research/aspect/scc/scc.py check nima-retained-comparison-series
```

Receipts: `results/agda-RetainedComparisonSeries.json` and
`results/retained-comparison-series.json`; current formal import hashes are checked.
The formal module proves the coefficient/operator interface, not a completed
infinite series ring or a continuum path integral. The resolvent, quadratic-action,
sector-inverse and determinant calculations are exact symbolic checks. No arbitrary-boundary finite enumeration,
full-history faithful action, physical selection or independent review is claimed.
New files and evidence remain uncommitted; no existing researcher source was edited.
Report event `ev-000000015611-1f40e1d0-4423-4302-a136-8388e4598c62` at sequence
15611 is admitted but uncommitted. No computation remains active; graph admission
is not truth certification.
