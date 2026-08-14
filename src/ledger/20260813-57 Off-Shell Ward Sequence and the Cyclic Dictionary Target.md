# Off-Shell Ward Sequence and the Cyclic Dictionary Target

## Record

Date: 2026-08-13

Status: the off-shell cubic Ward identity canonically repairs the first typing
failure of entry 56.  After propagator composition and the physically selected
even endpoint gluing, the local Ward complex has ordinary graph homology as
its closed sector.  On the marked theta this sector has rank two and should be
retained, not killed.  Entry 59 subsequently proves that individual primitive
classes match populated oriented circuit supports, but that an additive,
equivariant transport requires a derived crossing/smoothing resolution.

The scalar-derived cyclic comparison that would perform that transport remains
conjectural.  Its precise target is now a homological-perturbation comparison
between two cyclic deformation retracts of the scalar first-jet/BRST carrier.

Reproducible certificates:

```text
research/nima/check_offshell_ward_contact_complex.rs
research/nima/check_longitudinal_edge_gluing.rs
```

## Exact local Ward identity

For outgoing momenta \(k_0+k_1+k_2=0\), take

\[
V_{\mu\nu\rho}
=
\eta_{\mu\nu}(k_0-k_1)_\rho
+\eta_{\nu\rho}(k_1-k_2)_\mu
+\eta_{\rho\mu}(k_2-k_0)_\nu.
\]

Then

\[
\boxed{
k_0^\mu V_{\mu\nu\rho}
=P_{\nu\rho}(k_1)-P_{\nu\rho}(k_2),}
\qquad
P_{\nu\rho}(k)=k^2\eta_{\nu\rho}-k_\nu k_\rho,
\]

up to the corresponding cyclic sign convention.  The exact Gram-polynomial
certificate verifies 48 cyclic contractions in 21 generic variables.

For the covariant propagator

\[
D_\xi(k)
=
\frac{\eta}{k^2}
+(\xi-1)\frac{k\otimes k}{(k^2)^2},
\]

the transverse inverse kinetic operator annihilates the gauge-dependent
piece, and

\[
P(k)D_\xi(k)
=1-\frac{k\otimes k}{k^2}.
\]

The certificate verifies 96 such compositions without specializing a Gram
determinant or the gauge parameter.

Thus a Ward exit has two canonical outputs:

\[
\text{Ward mark}
\longmapsto
\text{edge contraction/contact state}
-\text{longitudinal exit}.
\]

The identity term changes graph type.  This is why neither the on-shell exit
tensor nor the off-shell contact differential can land solely in the
top-dimensional 243 cubic-origin module.

## The independent-exit audit and its correction

On \(K_{2,3}\), there are nine symmetry-visible local Ward marks and two
local cyclic relations, hence a rank-seven degree-one module.  If the twelve
half-edge exits are kept independent, the contact map has rank five but the
contact-plus-exit map has rank seven.  Each of the 24 fundamental-chord tests
then has zero contact telescope and an eight-exit longitudinal remainder.

That remainder does not yet imply missing ghost or quartic cancellation.
The two exits on one sewn internal edge represent the same rank-two
longitudinal tensor:

\[
Q(k)=\frac{k\otimes k}{k^2},
\qquad Q(-k)=Q(k).
\]

The physically selected edge coequalizer is therefore

\[
Q_{e,\mathrm{tail}}=Q_{e,\mathrm{head}}.
\]

After this even endpoint gluing:

- the contact-plus-longitudinal map again has rank five and kernel rank two;
- all 24 base fundamental cycles telescope;
- all 1,536 orientation-expanded cycle tests telescope;
- all 108 \(S_2\times D_3\) covariance tests pass;
- all 384 momentum-orientation checks confirm projector evenness.

The opposite-sign convention fails all 1,536 cycle tests and contradicts
projector parity in all 384 edge-orientation checks.

This is an exact algebraic result conditional on one physical point: the
scalar-derived propagator/Cut map must realize the even endpoint coequalizer
without an additional sign.

## General flag-incidence theorem

The ranks are instances of a graph-theoretic exact sequence.

For a finite connected graph \(G\) with at least one edge, let

\[
F(G)=\{(v,e):v\in e\}
\]

be its flags and define

\[
\mathsf W_1(G)
=
\left\{
a\in\mathbb Z^{F(G)}
:
\sum_{e\ni v}a_{v,e}=0
\text{ for every }v
\right\}.
\]

This is the direct sum of the reduced star modules at the vertices.  Define

\[
t:\mathsf W_1(G)\longrightarrow\mathbb Z^{E(G)},
\qquad
t(a)_e=a_{v,e}+a_{w,e},
\quad e=\{v,w\}.
\]

Then:

\[
\boxed{
0\longrightarrow H_1(G;\mathbb Z)
\longrightarrow\mathsf W_1(G)
\xrightarrow{t}\mathbb Z^{E(G)}
\xrightarrow{\sum_e}\mathbb Z
\longrightarrow0.}
\]

To see the kernel, orient every edge and write

\[
a_{\mathrm{tail}(e),e}=c_e,
\qquad
a_{\mathrm{head}(e),e}=-c_e.
\]

The vertex equations become \(\partial c=0\), so \(\ker t=H_1(G)\).
The image of \(t\) is the sum-zero edge lattice: differences of incident
edges generate it because the line graph of a connected graph is connected.

For \(K_{2,3}\),

\[
\operatorname{rank}\mathsf W_1=2|E|-|V|=7,
\]

\[
\operatorname{rank}\operatorname{im}t=|E|-1=5,
\]

and

\[
\operatorname{rank}\ker t
=|E|-|V|+1=2.
\]

The exact certificate recovers an integral primitive basis of this rank-two
kernel.  Its smallest nonlocal class uses four Ward marks, the support of a
fundamental four-cycle.

## Interpretation: circuit homology is a state sector

The remaining two classes are not a failure of Ward telescoping.  They are
ordinary graph homology.  The provisional arrow

\[
H_1(K_{2,3};\mathbb Z)
\longrightarrow
\mathsf{Circuits}^{\rm res}(K_{2,3}).
\]

must not be read as a canonical additive section.  The canonical direction is
from an oriented resolved circuit to its homology class.  Entry 59 proves that
the three populated circuit tags surject onto \(H_1\), but that their
\(D_3\)-equivariant additive section has index-three obstruction and requires
a crossing/smoothing chain cell.

A spanning tree contracts the exact transport sector and chooses two
fundamental-cycle representatives.  Changing the tree changes those
representatives but not \(H_1\).  Their wedge belongs to

\[
\det H_1(K_{2,3}),
\]

on which road rotation acts by \(+1\) and ribbon reflection by \(-1\).
This is the natural home of the first antisymmetric two-sewing datum.

Adding a non-bridge edge \(e\) to a connected graph gives the relative
triangle

\[
C_*(G)\longrightarrow C_*(G+e)
\longrightarrow C_*(G+e,G)\xrightarrow{+1}
\]

and

\[
H_1(G+e)/H_1(G)\cong H_1(G+e,G)\cong\mathbb Z.
\]

Thus sewing creates a canonical relative circuit even before a spanning-tree
representative is chosen.

## The cyclic two-retract theorem target

The best candidate common carrier is

\[
\mathcal B_{\rm jet}=J_F^1\mathrm{Scalar}
\]

before gauge cohomology, enriched by the kinetic/contact/ghost strata forced
by its BRST/BV differential.  Seek cyclic contractions

\[
(\mathcal P,d_{\rm P})
\underset{p_{\rm P}}{\overset{i_{\rm P}}{\rightleftarrows}}
(\mathcal B_{\rm jet},Q)
\underset{i_{\rm S}}{\overset{p_{\rm S}}{\rightleftarrows}}
(\mathcal S,d_{\rm S}),
\]

where \(\mathcal P\) is the physical-projector carrier and \(\mathcal S\)
the resolved surface/Ward--Brauer carrier.

Let

\[
\mathbf D=\mathbf Q+\boldsymbol\delta
\]

be the full interaction coderivation on the corresponding bar/cobar or
Feynman-transform complex.  Under the filtered hypotheses of homological
perturbation, the complete dictionary is forced to be

\[
\boxed{
\Phi_{\rm P\to S}
=
p_{\rm S}(1-\boldsymbol\delta h_{\rm S})^{-1}
(1-h_{\rm P}\boldsymbol\delta)^{-1}i_{\rm P}.}
\]

Its expansion is a sum over painted interaction graphs.  At genus zero these
are organized by graph multiplihedra.  With self-sewing they must be organized
by a cyclic/modular Feynman transform.

This formula is a theorem target, not an established scalar construction.  It
reduces the unknown input to:

1. the two contractions \((i,p,h)\);
2. cyclic adjointness with the scalar pairing;
3. Cut compatibility of the contractions;
4. the map from Ward cycle homology to resolved Brauer circuits.

The higher comparison cells would then be generated recursively rather than
fitted graph by graph.

## Lowest coherence equations

If \(F_r\) are the components of the transferred dictionary and
\(m_r^{\rm P},m_r^{\rm S}\) the two transferred interaction structures,
then the first equation is

\[
F_1m_2^{\rm P}
-m_2^{\rm S}(F_1\otimes F_1)
=d_{\operatorname{Hom}}F_2.
\]

This is the correct type of the one-edge realization defect.  A moving Ward
mark contributes to \(F_2\); it is not directly a boundary in the cubic-origin
module.

The arity-three equation contains \(m_3\), the composites of \(m_2\) with
\(F_2\), and \(dF_3\).  Quartic/contact interactions therefore belong in
the first higher morphism equation even though they are not required merely to
kill the graph-cycle kernel.

Cyclicity requires, with graded signs,

\[
p=i^\dagger,
\qquad
\langle hx,y\rangle
+(-1)^{|x|}\langle x,hy\rangle=0.
\]

Cut compatibility requires an Alexander--Whitney-type tensor identity for
\(h\), not merely equality after amplitude augmentation.

## Revised master principle

The data producing a theory is a carrier together with a dictionary:

\[
(\mathcal F_E,V_E)
=
\operatorname{DerivedNormal}_E(\mathrm{Scalar}),
\]

where \(\mathcal F_E\) self-factorizes and \(V_E\) is a cyclic,
homotopy-monoidal valuation into physical states/functions.  Quantum
completion is

\[
\mathsf T_E=\operatorname{Mod}(\mathcal F_E,V_E).
\]

This refines the earlier statement that a theory is merely the modular
completion of a derived normal sector.  The dictionary cannot be suppressed
when distinct chain-level realizations have the same final amplitude.

A candidate global language is a cyclic/modular decomposition space with
dualizable coefficient systems:

- the simplices are flags of compatible scalar Cuts;
- the 2-Segal/decomposition axiom expresses independence of decomposition
  order;
- its incidence coalgebra is the unresolved Cut coaction;
- a physical theory is a coefficient system or module;
- amplitudes arise after linearization, pairing, and valuation.

This language is suggestive, not yet proved to model the scalar surface
formalism.

## Evidence boundary

Proved:

- the generic off-shell cubic Ward identity;
- the propagator contact/longitudinal split;
- the physical evenness test \(Q(-k)=Q(k)\);
- exact telescoping after even endpoint gluing on all marked-theta cycles and
  orientations;
- failure of the opposite-sign endpoint rule;
- the integral flag-incidence exact sequence;
- identification of the remaining rank with graph cycle homology.

Conditional:

- physical realization of endpoint coequalization inside the scalar first-jet
  propagator/Cut complex;
- a homotopy-coherent lift of Ward homology through the oriented resolved
  Brauer circuit carrier.

Conjectural:

- the cyclic two-retract theorem;
- the homological-perturbation formula as the scalar-derived surface
  dictionary;
- the decomposition-space/global modular packaging.

## Next falsifier

Construct one actual scalar-first-jet internal edge and prove that its
propagator/Cut map coequalizes the two endpoint tensors as

\[
Q_{e,\mathrm{tail}}=Q_{e,\mathrm{head}}
\]

with the cyclic pairing signs included.  Then construct the oriented
one-crossing Brauer--skein filler required by entry 59, without applying
\(D\mapsto1\), and verify one nonseparating Cut.  Failure of either step
falsifies the proposed Ward-to-Brauer bridge before higher coherence.

## Primary context

- Nützi and Reiterer, minimal-model amplitudes and propagator homotopy:
  <https://arxiv.org/abs/1812.06454>.
- Reiterer, homotopy BV structure for Yang--Mills:
  <https://arxiv.org/abs/1912.03110>.
- Dyckerhoff and Kapranov, *Higher Segal spaces I*:
  <https://arxiv.org/abs/1212.3563>.
- Gálvez-Carrillo, Kock, and Tonks, decomposition spaces and incidence
  coalgebras:
  <https://arxiv.org/abs/1512.07573>.

## Internal dependencies

- Entry 46: resolved Brauer circuit carrier.
- Entries 49--52: marked-handle circuit and physical-projector tests.
- Entries 53--54: Ward-quotient closure and two-open-pair naturality.
- Entries 55--56: originwise failure and graph-multiplihedral carrier.
- Entries 58--59: general marked-deletion evidence and the precise
  Brauer--skein obstruction.
- Working context: `research/nima/ward_brauer_math_context.md`.
