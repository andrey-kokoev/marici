# Open-Path Surface Dictionary and Complete Marked-Handle Leading Singularity

## Record

Date: 2026-08-13

Status: the formula objective posed at the end of entry 50 is achieved for the
marked-theta graph cell.  The literal endpoint-extension rule produces a
homotopy-sensitive surface-\(X_C\) polynomial with all signs and cancellations
retained.  After the resolved closed-circuit substitution

\[
\nu_\gamma-\Delta_\gamma=D,
\]

that polynomial agrees with the complete five-vertex Yang--Mills leading
singularity, including physical longitudinal projector terms, at four
independent exact six-dimensional kinematic points and for all twelve
spanning-tree sewing presentations.

This is an exact finite graph-cell certificate and a combinatorial construction
of the requested dictionary.  It is not yet a symbolic identity over the full
kinematic variety, a mapping-class-summed surface integrand theorem, or an
all-graph proof.

Reproducible certificate:

`research/nima/check_marked_handle_x_dictionary.rs`

## Formula objective

Let

\[
\mathbf s\in\{0,1,2\}^{5}
\]

choose one of the three metric-pairing sectors at each of the five cubic
Yang--Mills vertices.  The resolved state has four open contraction paths
\(\mathcal P(\mathbf s)\) and at most one closed polarization circuit.  For an
open path \(P\), let

\[
C(P;\epsilon_L,\epsilon_R)
\]

be the surface curve obtained by independently extending either endpoint by

\[
\epsilon=0:\quad \text{right once, then left forever},
\qquad
\epsilon=1:\quad \text{left forever}.
\]

The target graph-cell formula is

\[
\boxed{
\operatorname{LS}^{\rm phys}_{\Gamma_3}
=
\frac{1}{2^4}
\sum_{\mathbf s\in\{0,1,2\}^{5}}
D^{c(\mathbf s)}
\prod_{P\in\mathcal P(\mathbf s)}
\left[
\sum_{\epsilon_L,\epsilon_R=0}^{1}
(-1)^{\epsilon_L+\epsilon_R}
\,4X_{C(P;\epsilon_L,\epsilon_R)}
\right].
}
\]

Here \(c(\mathbf s)\in\{0,1\}\) is the number of closed circuits.  The factor
\(2^{-4}\) is fixed locally: at the exact scaffolded kinematics used by the
certificate, every one of the 978 tested open components obeys

\[
\boxed{
\sum_{\epsilon_L,\epsilon_R}
(-1)^{\epsilon_L+\epsilon_R}
\,4X_{C(P;\epsilon_L,\epsilon_R)}
=-2\,H_L\!\cdot H_R.
}
\]

There are \(243\times4=972\) components on the marked handle and six in the
three-point calibration.  Since the marked cell always has four open paths,
the four factors of \(-2\) leave the overall \(2^4\) normalization shown above.

Equivalently, if the polynomial is evaluated directly on ordinary \(X_C\)
rather than the scaled \(4X_C\), then

\[
\operatorname{LS}^{\rm phys}_{\Gamma_3}=2^4 P_{\Gamma_3}(X).
\]

## The curve dictionary

The scalar-scaffolded marked graph has eight trivalent vertices and six
boundary legs.  Its five Yang--Mills vertices contribute

\[
3^5=243
\]

local sector words.  Sewing the metric-paired indices in a sector produces
four red-handle-to-red-handle paths and possibly one closed blue circuit.

A curve is not keyed only by its two boundary labels.  On a handle that would
identify different winding classes.  The certificate uses

\[
C=(i,w,j),
\]

where \(i,j\) are boundary labels and \(w\) is the reduced signed internal-edge
word.  Immediate backtracking is cancelled, and orientation reversal imposes

\[
(i,w,j)\sim(j,w^{-1},i).
\]

This is the smallest graphwise label that both evaluates the surface momentum
rule and keeps homotopically distinct curves separate.

For one open component the four extensions give

\[
\Phi(P)
=
\sum_{\epsilon_L,\epsilon_R=0}^{1}
(-1)^{\epsilon_L+\epsilon_R}
X_{C(P;\epsilon_L,\epsilon_R)}.
\]

In a disk presentation this is exactly the Carrôlo--Figueiredo rule

\[
\Phi(P)=X_{bd}+X_{ac}-X_{bc}-X_{ad}.
\]

The global sign, cyclic orientation, and boundary-label origin are not fitted
on the handle.  They are fixed first by the three-point calibration.

## Three-point calibration

On the scalar-scaffolded cubic gluon graph, the same algorithm has

\[
3\cdot4^2=48
\]

raw extension origins.  After imposing the massless boundary and scaffolding
zero curves, grouping equal \(X\)-monomials gives exactly

\[
\begin{aligned}
A_3^{\rm YM}
={}&X_{14}X_{26}+X_{36}X_{24}+X_{25}X_{46}\\
&-X_{25}X_{36}-X_{14}X_{36}-X_{14}X_{25}.
\end{aligned}
\]

No relabeling, reflection, or overall sign is required:

\[
(\text{shift},\text{orientation},\text{sign})=(0,+1,+1).
\]

At the primary exact point the independent tensor, graphical, and scaled
surface evaluations are

\[
(A_3^{\rm tensor},A_3^{\rm paths},A_3(4X))=(8,8,32),
\]

which is the expected two-path factor \(2^2\).

## Correct on-shell zero locus

An early false start identified curves running along the three scaffold graph
edges with the scaffold zeros.  That destroys \(X_{14},X_{25},X_{36}\), which
must survive in the calibrated cubic polynomial.

The correct zero curves are boundary-parallel representatives:

- the six massless arcs \(X_{i,i+1}\);
- the three short scaffolding chords \(X_{13},X_{35},X_{51}\).

The signed edge word is essential here.  A winding curve may have the same
endpoint pair as one of these arcs without lying on the on-shell zero locus.

## Extension and cancellation census

Every marked-handle sector has four open paths and hence eight independently
chosen endpoints.  The raw extension histogram is therefore exactly

\[
N_k=243\binom{8}{k},
\qquad 0\leq k\leq8,
\]

or

| \(N_e\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| origins | 243 | 1,944 | 6,804 | 13,608 | 17,010 | 13,608 | 6,804 | 1,944 | 243 |

Thus the full expansion contains

\[
243\cdot4^4=62{,}208
\]

signed origins.  The exact reduction is:

| quantity | count |
|---|---:|
| origins removed by the on-shell zero locus | 40,896 |
| distinct homotopy-sensitive \(X_C\) variables | 150 |
| distinct generated monomials before cancellation | 10,317 |
| monomials cancelling completely | 4,701 |
| nonzero surviving monomials | 5,616 |
| surviving monomials with partial cancellation | 72 |
| constant-sector survivors | 5,424 |
| \(D\)-sector survivors | 192 |
| mixed constant-plus-\(D\) survivors | 0 |
| maximum absolute surviving coefficient | 1 |

The last two lines are a strong internal check.  After grouping all coincident
curves, the polynomial is multiplicity-free and the constant and circuit
supports separate completely.  Equality of the final amplitude alone would
not expose these extension cancellations.

## Complete physical five-vertex leading singularity

The direct comparison contracts five ordinary cubic gluon tensors at a
six-dimensional split-signature point.  The metric has nonzero pairs

\[
g_{03}=g_{30}=g_{14}=g_{41}=g_{25}=g_{52}=1.
\]

All internal and external momenta and all external polarizations are exactly
null; momentum conservation and transversality are checked using integer
arithmetic.  The local tensor is independently decomposed into its three
pairing sectors for all

\[
243
\]

sector words and every tensor index assignment.

A two-loop sewing presentation chooses a spanning tree of four of the six
internal graph edges.  On its two closing edges the certificate inserts

\[
\Pi^{\mu\nu}(p;q)
=-\eta^{\mu\nu}
+\frac{p^\mu q^\nu+p^\nu q^\mu}{p\!\cdot q},
\]

while tree edges carry the ordinary metric sewing.  The marked-theta graph has
twelve spanning trees.  All twelve yield the same physical leading
singularity.

At the primary point,

\[
\operatorname{LS}_{\rm metric}=-2056,
\qquad
\boxed{\operatorname{LS}_{\rm physical}=-2048}.
\]

The surface expansion gives

\[
P_{\Gamma_3}(4X)=-32768,
\qquad
\frac{P_{\Gamma_3}(4X)}{2^4}=-2048.
\]

The equality is repeated at three additional nonzero exact points:

| parameters \((a,b,d)\) | \(\operatorname{LS}_{\rm physical}\) | \(P_{\Gamma_3}(4X)\) |
|---:|---:|---:|
| \((1,2,3)\) | \(-2048\) | \(-32768\) |
| \((1,-3,4)\) | \(-512\) | \(-8192\) |
| \((1,3,-2)\) | \(-1536\) | \(-24576\) |
| \((1,4,2)\) | \(-4608\) | \(-73728\) |

These are exact integer identities, not floating-point comparisons.  They
provide a robust finite certificate, but four samples are not a substitute for
a symbolic proof over the entire on-shell kinematic variety.

## The longitudinal correction and the resolved carrier

Entry 50 incorrectly concluded that every longitudinal projector term
vanishes.  Expanding the two closing projectors into metric and longitudinal
parts gives two exact sewing-history classes at the primary point:

| \([\mathrm{M},L_1,L_2,L_1L_2]\) | spanning trees |
|---|---:|
| \([-2056,8,0,0]\) | 8 |
| \([-2056,8,8,-8]\) | 4 |

Both sum to \(-2048\).  In particular, four sewing histories contain a
nonzero nested longitudinal term.  The net correction to the all-metric
network is

\[
\operatorname{LS}_{\rm physical}
-\operatorname{LS}_{\rm metric}=8.
\]

The earlier turn test inspected the completed graph-theoretic fundamental
cycle and counted turns at the two closure endpoints.  The physical criterion
instead inspects the path connecting the legs *before* they are glued.
Endpoint turns are not part of that open path.  Such a path may be all-left
internally even when the completed graph cycle appears mixed.

This correction does not alter the surface formula.  It explains why the
resolved circuit value had to be

\[
\boxed{\nu_\gamma-\Delta_\gamma}
\]

rather than a bare exponent.  For a generic closed curve,

\[
(\nu_\gamma,\Delta_\gamma)=(0,-D),
\]

whereas an internal-boundary curve has

\[
(\nu_\gamma,\Delta_\gamma)=(1,1-D).
\]

Both are sent to

\[
\nu_\gamma-\Delta_\gamma=D.
\]

The resolved carrier therefore forgets precisely the sewing-history
distinction that the physical projector rearranges while retaining the common
state-space trace.  The nonzero correction is evidence for the resolution,
not an extra term that must be appended to it.

## What is established

For this marked maximal graph cell:

- the endpoint-extension construction is explicit and homotopy-sensitive;
- its orientation and signs reproduce the published three-point polynomial;
- all \(62{,}208\) extension origins and their \((-1)^{N_e}\) signs are
  enumerated;
- the on-shell zero locus and all equal-\(X_C\) cancellations are explicit;
- the five-tensor network equals its 243-sector open-path decomposition;
- the complete physical projector is independent of all twelve spanning-tree
  sewing presentations at each tested point;
- the normalized surface polynomial agrees with that physical answer at four
  exact nondegenerate points;
- the prior zero-longitudinal claim is falsified;
- the resolved circuit value \(D=\nu-\Delta\) survives the correction without
  modification.

## What remains open

This entry does not yet provide:

- a symbolic polynomial proof of the complete projector equality for arbitrary
  on-shell momenta and polarizations;
- a comparison with the full mapping-class sum rather than one labelled
  marked-theta cell;
- a proof that the signed edge-word labels descend canonically to the global
  surface curve algebra under all flips;
- a scale-carrying four-point integrated amplitude test;
- an all-topology theorem that every nested physical-projector history is
  absorbed by the same \(\nu-\Delta\) carrier.

The next mathematical target is no longer to find the dictionary.  It is to
promote the finite graph-cell identity above to a symbolic local theorem and
then prove its compatibility with flips, Cuts, and mapping-class summation.

## Primary source

- Carrôlo and Figueiredo, *How gluon leading singularities discover curves on
  surfaces*, especially the cubic graphical rule, endpoint extensions,
  V-rule cancellations, physical polarization projectors, and the all-loop
  closed-curve exponent: <https://arxiv.org/abs/2512.17019>.

## Internal dependencies

- Entry 46: resolved closed-circuit carrier and the target
  \(\nu-\Delta\).
- Entry 49: hostile punctured-torus test of the resolved surface counit.
- Entry 50: marked-handle state carrier and the now-superseded
  zero-projector-correction claim.
