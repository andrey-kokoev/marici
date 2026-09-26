# Amplitudes: simple-to-general benchmark programme

## Scope and status

[Native Resolve amplitude bridge](../native-amplitude-resolution.md): all finite
marked sum/product expressions now have actual native and original Resolve
executions with commuting readouts, plus a formal semiring diagram-expansion
proof. The actual six-point fixture reads out 6/25. The general Python DAG
compiler targets this grammar and is checked through twelve points; universal
compiler/enumerator certification remains open.

[Arbitrary-even-n native scalar recursion](../native-scalar-recursion.md)
now implements the tree algorithm with retained partition DAG tables and
memoized readout. Computational checks extend through twelve legs; eight-point
checks compare all 280 individual topology weights. General-n Python
compiler/enumerator certification remains open; the expression-level native
Resolve connection is supplied by the follow-up above.

New: [native weighted-fiber amplitude](../native-scalar-fiber-amplitude.md)
independently constructs and evaluates four/six-point scalar diagram tables.
The actual six-point native table sum is Agda-checked against the existing
fixture; broader exact comparisons include all 720 six-point permutations.
The coupling and propagator laws remain supplied physical inputs.

Current consolidation status: [bounded audit](consolidation-audit.md).
An independent scalar-six census and a fresh Agda check of that fixed sample
pass; corrupted result and propagator proofs are rejected by the compiler.
The external-reference audit and general evaluator/framework bridge remain open.

Goal: progressively reconstruct known amplitudes and then compute further
processes within explicitly specified theories. "All" is an extensible
programme, not a claim of a universal solved amplitude problem. Missing
interactions, parameters or nonperturbative physics are not supplied by
coherence proofs.

The tree calculators use exact rational/complex arithmetic. The massive
one-loop scalar checkpoint additionally uses floating-point logarithms and
quadrature with stated tolerances, not certified interval bounds. Neither is
yet connected to the Agda native-boundary/comparison framework. The earlier
Agda results prove structural properties conditional on typed evaluators;
they neither derive Feynman rules nor establish this calculator's physics.
No new physical discovery is claimed by these benchmarks.

## First completed benchmark: real massless phi^4, tree level

Conventions:

* L = (1/2) partial_mu phi partial^mu phi - lambda phi^4/4!;
* metric (+---), natural units, all external momenta incoming;
* vertex -i lambda, internal propagator i/(q^2+i0);
* amputated connected contribution i M, with momentum delta omitted;
* evaluation only at nonsingular rational on-shell kinematics. No replacement
  of the distributional i0 by a numerical tolerance is made.

The four-point amplitude is M4 = -lambda. The six-point amplitude is

    M6 = -lambda^2 sum_{unordered partitions A|Ac, |A|=3} 1/(sum_A p)^2.

There are ten labelled six-point diagrams. External-leg labels are retained;
no identical-final-particle phase-space symmetry factor belongs in M itself.

Two implementations are compared:

1. direct enumeration of unordered three-versus-three channels;
2. rooted off-shell-current recursion with unordered three-block partitions.

The current recursion uses +lambda/q^2 at internal currents and -lambda at
the amputated root, as follows from the stated vertex and propagator phases.
External root propagators are not included. Full recursive current histories,
channel denominators, input momenta and contributions are retained in JSON.

For lambda=3/5, the included four-point sample gives M4=-3/5. The six-point
2-to-4 sample has incoming energies 2,2 and outgoing energies 1,1,1,1. Its
channel denominators are four copies of 8, two of -4 and four of -6, giving
M6=6/25 in the chosen energy units. These are benchmark-point values, not
kinematics-independent constants or cross sections.

Seven test groups pass using exact fractions:

* four-point contact rule;
* six-point agreement for all six choices of external root;
* all 720 permutations at the reference six-point kinematics;
* unequal-energy, nonuniform-angle rational kinematics;
* coupling and momentum scaling;
* rejection of off-shell or nonconserving inputs;
* rejection of internal propagator poles.

Run:

```
python research/nima/amplitudes/scalar_tree_baseline.py --output research/nima/results/scalar-tree-amplitude-baseline.json
```

These tests do not prove general recursive diagram enumeration or all-
kinematics agreement. The seven groups include many individual cases.

## Eight-point and factorization checkpoint

`scalar_eight_factorization.py` independently enumerates all 280 labelled
three-vertex trees: choose two external legs at the middle vertex, then
partition the remaining six into two unordered triples. Each diagram has
contribution -lambda^3/(s_left s_right).

For every external root, expansion of the recursive histories yields exactly
the same multiset of internal-channel pairs, each once. This is a finite
combinatorial audit beyond comparing amplitude totals. Exact numerical tests
also cover unequal outgoing energies, coupling/momentum scaling, and 16
cyclic/reversed permutations (not all 8! permutations).

At a constructed rational on-shell point with precisely one vanishing
three-leg invariant s_A, the residue is extracted algebraically from the ten
diagrams containing that channel. No divergent amplitude is evaluated:

    lim_{s_A -> 0} s_A M8 = -M4 M6.

The minus sign follows from the stated convention i M: sewing gives
(i M4)(i/s_A)(i M6) = -i M4 M6/s_A. The lower-point amplitudes are evaluated
with the cut momentum incoming on one side and outgoing on the other.
At the supplied cut and lambda=3/5, the residue is 18/125. Eight relabellings
of this cut are checked; this is not a general analytic proof of all cuts.
Overlapping poles and attempts to evaluate a full amplitude at a pole are
explicitly rejected.

Five new test groups pass; the seven earlier groups also pass. The JSON
retains all direct diagrams, a full rooted recursive history, the cut
kinematics and individual residue contributions. At the non-pole eight-point
sample, M8 = 10240196727139/641887958400000 in the chosen energy units.

```
python research/nima/amplitudes/scalar_eight_factorization.py --output research/nima/results/scalar-eight-factorization.json
```

## Massive scalar and cubic-interaction checkpoint

`massive_scalar_trees.py` implements the declared theory

    L = (partial phi)^2/2 - m^2 phi^2/2 - g phi^3/3! - lambda phi^4/4!.

External legs obey p^2=m^2; each active internal propagator uses
1/(q^2-m^2). The generic recursion now assembles both two-child cubic and
three-child quartic vertices, retaining vertex types and couplings in every
history. Zero couplings disable their vertices, including their otherwise
spurious pole checks.

Independent direct references cover:

* four points: one quartic contact plus three cubic exchange diagrams,
  M4 = -lambda - g^2[1/(s-m^2)+1/(t-m^2)+1/(u-m^2)];
* five points: 15 pure-cubic diagrams and 10 mixed cubic/quartic diagrams;
* six points with g=0: ten massive quartic diagrams.

For every external root, expanded recursive histories match the direct
labelled channel/vertex multisets, with no duplicates. Tests also include
all 24 four-point and 120 five-point permutations, pure-coupling limits,
the earlier massless-quartic results, and dimensional scaling. Scaling
p,m,g by a common factor a with lambda fixed scales M_n by a^(4-n).

The included real, on-shell rational examples give:

| legs | m | g | lambda | amplitude in chosen units |
| --- | --- | --- | --- | --- |
| 4 | 1 | 2/5 | 3/5 | -4283/8925 |
| 5 | 1 | 2/5 | 3/5 | 298792/826875 |
| 6 | 1 | 0 | 3/5 | 46914912/182283625 |

A separate algebraic check clears the four-point denominators and extracts
Res_(s=m^2) M4 = -g^2 = -M3 M3 with M3=-g. It uses formal Mandelstam
invariants satisfying s+t+u=4m^2, NOT a real equal-mass on-shell three-point
scattering configuration. No such physical decay configuration is claimed.
The pure-cubic limit is a perturbative benchmark, not a claim of global
vacuum stability for the unbounded cubic potential.

Eight new groups and all twelve previous groups pass. This remains finite
exact computational evidence, not a general proof or an Agda integration.
JSON retains input momenta, each sample's model, diagrams and all rooted
calculation histories.

```
python research/nima/amplitudes/massive_scalar_trees.py --output research/nima/results/massive-scalar-trees.json
python -m unittest discover -s research/nima/amplitudes -p "*.py" -v
```

## First spin/gauge checkpoint: distinct-flavour QED scattering

`qed_fermion_scattering.py` computes tree-level negative-charge Dirac-fermion
elastic scattering, conventionally e- mu- -> e- mu-. These are distinct
flavours, so there is one t-channel photon diagram and no identical-fermion
exchange diagram. The benchmark uses declared rational masses and charge,
NOT the measured electron/muon parameters.

Unlike the scalar all-incoming convention, p1,p2 here are physical incoming
momenta and p3,p4 are outgoing, all with positive energy. With metric +---,
vertex -i e gamma^mu, photon propagator -i g_mu_nu/t and delta-stripped i M:

    M = e^2/t [ubar(p3) gamma^mu u(p1)] [ubar(p4) gamma_mu u(p2)].

A dependency-free exact complex-rational backend constructs Dirac matrices
and canonical spinors normalized by ubar u=2m and u-dagger u=2E. The spin
basis is rest-frame z spin followed by the canonical boost, NOT helicity.
The spinor backend currently requires E+m to have a rational square root;
unsupported algebraic roots raise an explicit error rather than being rounded.

At four scattering directions, three evaluations agree exactly:

1. all 16 individual complex spin amplitudes, then initial-spin averaging;
2. the independent two-Dirac-trace spin sum;
3. the invariant expression

    averaged |M|^2 = 2 e^4/t^2 [(s-me^2-mm^2)^2
                               +(u-me^2-mm^2)^2 + 2t(me^2+mm^2)].

Each external spin combination has both Ward contractions q.J=0. Changing
the covariant gauge parameter among 1, 0, -2 and 7/3 leaves every individual
amplitude unchanged. Deliberately adding longitudinal contamination to BOTH
currents produces gauge dependence, so this is not an identically inert test.
Other tests check the Clifford algebra, gamma adjoints, Dirac equations,
spinor completeness, normalization, azimuth independence of the unpolarized
result, dimensional/coupling scaling and rejection of invalid inputs/poles.
A fixed-spin value M=-17/18 at the first benchmark point checks the overall
sign, which squared amplitudes alone cannot detect.

Eight new groups and all twenty earlier groups pass. JSON retains the
momenta, masses, charge, external spinors, currents, all spin amplitudes,
Ward contractions, trace and invariant results. For the first point,
averaged |M|^2 = 9491089/6718464. This is not a cross section: flux and
phase-space factors have not been applied.

```
python research/nima/amplitudes/qed_fermion_scattering.py --output research/nima/results/qed-fermion-scattering.json
```

## Compton checkpoint: cancellation between diagrams

`qed_compton.py` evaluates tree e- gamma -> e- gamma with both s- and
u-channel electron-exchange diagrams. Physical incoming momenta are p,k;
outgoing momenta are p',k'. The convention is

    M = -e^2 ubar(p') [ eps'*/ (p/+k/+m)/(s-m^2) eps/
                      + eps/ (p/-k'/+m)/(u-m^2) eps'*/ ] u(p).

A slash denotes contraction with gamma matrices. The outgoing photon
polarization is complex-conjugated. The two internal electron momenta,
denominators, diagram amplitudes and external spinors/polarizations are
retained separately in JSON.

Checks cover five directions at one centre-of-momentum energy and two
additional energies at another direction, using exact rational complex
arithmetic. For each spin/polarization combination, replacing either photon
polarization by its momentum makes the SUM vanish. Individual diagrams are
nonzero in witnessed cases; omitting one or reversing the relative sign
fails the Ward test. Simultaneous polarization gauge shifts leave amplitudes
unchanged. Multiplying the incoming polarization by i multiplies M by i;
multiplying the outgoing polarization by i multiplies M by -i, testing the
outgoing conjugation explicitly.

Three unpolarized results agree: explicit physical spin/polarization sums,
a Dirac trace with both covariant polarization sums -g, and the invariant
Klein-Nishina amplitude formula. Writing a=p.k, b=p.k', D=1/a-1/b:

    averaged |M|^2 = 2 e^4 [a/b + b/a + 2m^2 D + m^4 D^2].

This is an amplitude squared, not the differential cross section. Covariant
polarization sums are used on the total gauge-invariant kernel, not on each
diagram separately. The exact forward amplitude is -2e^2 for unchanged
canonical spin and linear polarization, and zero otherwise; this supplies
an amplitude-level sign check. Forward scattering is finite here, unlike
the t-channel photon pole in the distinct-flavour elastic benchmark.

For m=1, e=1/3, incoming photon energy 3/4 in the COM frame and 90-degree
photon scattering, averaged |M|^2 = 317/8100. These are declared benchmark
parameters, not fitted physical constants. Seven new groups and all 28
previous groups pass (35 total). The general analytic Ward theorem and Agda
integration remain unproved by these finite computational tests.

```
python research/nima/amplitudes/qed_compton.py --output research/nima/results/qed-compton.json
```

## Antiparticle annihilation and spin-summed crossing checkpoint

`qed_annihilation.py` adds tree e- e+ -> mu- mu+ with a single s-channel
photon. All external momenta have positive energies: p1,p2 incoming and
p3,p4 outgoing. Masses and charge are rational benchmark parameters, not
measured electron/muon constants.

The antiparticle convention is explicit: with r=sqrt(E+m) and the same fixed
Pauli basis chi used for u, v=(sigma.p chi/r, r chi). Tests verify
(slash(p)+m)v=0, vbar v=-2m, v-dagger v=2E and sum_s v vbar=slash(p)-m.
The phase labels are not presented as helicity or an implicit physical
charge-conjugation spin-label convention.

For delta-stripped i M,

    M = e^2/s [vbar(p2) gamma^mu u(p1)] [ubar(p3) gamma_mu v(p4)].

All 16 spin amplitudes at five massive kinematic points agree, after the
initial-spin average, with both a separate Dirac trace and

    averaged |M|^2 = 2 e^4/s^2 [(t-me^2-mm^2)^2
                               +(u-me^2-mm^2)^2 + 2s(me^2+mm^2)].

Both Ward contractions vanish for every spin combination; changing the
covariant gauge parameter does not change amplitudes. Antiparticle phase
changes act oppositely on incoming barred v and outgoing unbarred v, as
checked at a nonzero amplitude. Additional massless points reproduce
averaged |M|^2=e^4(1+cos(theta)^2), including forward/backward directions.
One fixed spin amplitude checks the chosen overall sign and phase convention.

Crossing is tested at the SPIN-SUMMED analytic-expression level. Substituting
elastic momenta (a1,-a4,-a2,a3) for annihilation momenta (a1,a2,a3,a4) sends
(s_elastic,t_elastic,u_elastic) to (u_annihilation,s_annihilation,t_annihilation).
Each crossed fermion density contributes a minus sign; both signs cancel in
the product of traces. Elastic trace and invariant expressions then equal
the annihilation result at five massive and five massless points. The
physical elastic API still rejects negative-energy inputs. Separately named
algebraic-expression helpers implement the analytic substitution.

This does NOT establish full spin-amplitude crossing, which also requires
analytic spinor continuation and phases. Nor is this a general crossing
proof. Seven new groups and all 35 earlier groups pass (42 total). The JSON
retains spinors, both currents, Ward contractions, all spin amplitudes,
Mandelstam invariants and crossed algebraic momenta/results. The first massive
benchmark has averaged |M|^2=4258/164025, without flux or phase-space factors.

```
python research/nima/amplitudes/qed_annihilation.py --output research/nima/results/qed-annihilation.json
```

## Four-gluon checkpoint: non-Abelian color and gauge cancellation

`yang_mills_four.py` computes the three exchange diagrams and the quartic
contact term in pure SU(3) Yang-Mills theory. An SU(2) calculation supplies a
smaller independent color-normalization check. Momenta are all incoming;
the metric is +--- and the contribution is i M. Cubic vertices use g f V,
internal gluons use -i g_mu_nu/q^2, and the quartic vertex uses -i g^2 times
the declared color/Lorentz tensor.

Color contractions are constructed from explicit Hermitian generators,
not supplied as a table:

    C_ab,cd = -2 Tr([Ta,Tb][Tc,Td]).

To stay in exact complex rational arithmetic, the eighth SU(3) generator is
sqrt(3) times the usual unit-normalized generator. The orthogonal color
metric is therefore diag(1,1,1,1,1,1,1,3). Component amplitudes are labelled
as basis components; squared components and color sums include the inverse
metric for EVERY external leg. A hostile test demonstrates that omitting
these weights gives a wrong color sum. The internal contraction is already
basis-independent through the commutator trace.

The complete color Gram matrix, averaged over the two initial colors, is

    D * [[1, 1/2, -1/2], [1/2, 1, 1/2], [-1/2, 1/2, 1]],

with D=9/8 for SU(3), D=4/3 for SU(2). Jacobi is checked for all 8^4 SU(3)
and 3^4 SU(2) color assignments. The quartic contact coefficient also agrees
with a separate sum of all 24 labelled assignments in the quartic action.

At four rational scattering directions:

* physical polarization/color sums reproduce
  averaged |M|^2 = (9/2) g^4 [3-tu/s^2-su/t^2-st/u^2] for SU(3);
* Ward substitutions in each external leg cancel the sum of diagrams;
  dropping or flipping the contact term fails in explicitly nonzero cases;
* simultaneous polarization gauge shifts leave components unchanged;
* all-plus and single-minus all-outgoing helicity amplitudes, and their
  parity partners, vanish; two-minus amplitudes include nonzero cases;
* normalized circular-polarization sums equal linear-polarization sums;
* Bose relabellings, momentum scaling and coupling scaling pass.

The helicity convention crosses physical incoming helicities and conjugates
physical outgoing polarizations. The four factors of 1/sqrt(2) are applied
as an exact overall 1/4. No spinor-helicity/Parke-Taylor comparison is claimed
at this stage. Forward/backward propagator poles are excluded.

For g=1/3 and the 90-degree benchmark, averaged |M|^2=3/8 for SU(3), and 4/9
for SU(2). These are benchmark amplitude squares, not cross sections or
physical fitted-coupling predictions. Eleven new groups and all 42 earlier
groups pass (53 total). JSON retains generators, color metrics/contractions,
external momenta/polarizations, separate diagrams, Ward substitutions and
helicity components. The Agda bridge and general analytic proofs remain open.

```
python research/nima/amplitudes/yang_mills_four.py --output research/nima/results/yang-mills-four.json
```

## Four-point Parke-Taylor checkpoint: amplitudes, not just squares

`gluon_spinor_helicity.py` factors each all-outgoing null momentum into
independent rational complex spinors, p.sigma=lambda tilde-lambda. This also
handles negative-energy crossed legs without pretending their spinors are
complex conjugates. The bracket convention is <ij>[ji]=2 p_i.p_j.

`gluon_parke_taylor_check.py` compares the ordered Feynman coefficient with

    A(1,2,3,4) = <ij>^4 / (<12><23><34><41>)

for the two negative-helicity legs i,j. The non-MHV helicity sectors vanish
at four points. The common overall i and coupling are stripped. In the
existing generator/color convention the complete amplitude is reconstructed
as -2 g^2 [C_12,34 A(1234) + C_13,24 A(1324)]. This fixes the normalization
rather than fitting a ratio separately at each point.

All 16 helicity assignments and all 24 orders agree at each of four rational
kinematic points: 1536 full complex-amplitude equalities, of which 576 are
nonzero. Further checks include reference-spinor independence, complex
little-group rescaling with weights t_i^(-2h_i), cyclic/reflection identities,
four-point U(1) decoupling and the BCJ relation s12 A(1234)=s13 A(1324).

The rational factorization need not yield unit-Hermitian-norm polarization
vectors. The code therefore retains and checks a per-leg adapter

    epsilon_spinor = alpha * epsilon_circular + beta * p,

including its complex phase/scale and longitudinal gauge term. Reconstructed
SU(3) amplitudes agree with the previous physical circular-basis amplitudes
after multiplying the four alpha factors. Squaring raw spinor-chart values
without these normalization factors is not claimed to be a physical spin
sum. The standard four polarization sqrt(2) factors are applied exactly;
a test that omits their overall 1/4 fails at a nonzero amplitude.

Eight new test groups and all 53 previous groups pass (61 total). JSON keeps
momenta, spinors, reference spinors, bracket matrices, separate ordered
exchange/contact contributions, basis adapters and color reconstruction.
These are exact finite tests, not a proof of Parke-Taylor for all kinematics,
not an on-shell recursion derivation, and not an Agda-certified calculation.

```
python research/nima/amplitudes/gluon_parke_taylor_check.py --output research/nima/results/gluon-parke-taylor-four.json
```

## Five-gluon checkpoint: off-shell ordered recursion

`gluon_ordered_recursion.py` builds ordered off-shell currents from cubic
and quartic Yang-Mills tensors, retaining all child currents, momenta,
propagator denominators, vertex numerators and values. It amputates the final
external leg instead of dividing by its null momentum squared. The engine
does not call a closed helicity formula.

The integer vertex tensors and polarizations with their sqrt(2) factors
omitted require an overall 1/2^(n-1). This follows from V3+2V4=n-2, not
from fitting five-point outputs. Independent nonzero complex three-point
MHV and anti-MHV seeds fix the odd-point signs; the four-point engine also
regresses against the previous explicit Feynman calculation.

`gluon_five_check.py` checks all 32 helicity sectors at four real rational
five-point kinematics: 10 MHV and 10 anti-MHV sectors are nonzero per point,
and the other 12 vanish. Every sector agrees with its independent closed
reference. With the reversed square-bracket determinant convention, the
anti-MHV reference is (-1)^n [ij]^4 / product_cyclic [a,a+1]. Omitting the
odd-point sign fails a nonzero check.

For one MHV and one anti-MHV assignment at the tilted point, all 120 orders
also agree. Expansion of every tested current tree yields exactly the
independently enumerated ten planar diagrams: five purely cubic and five
with one cubic and one quartic vertex, each once. Zero-valued contributions
are retained, not dropped before this audit.

Further checks cover cyclic root changes, odd reflection sign, reference
independence, each external Ward substitution, internal-current
transversality, balanced momentum/spinor scaling, and the five-point BCJ
relation evaluated directly through the Feynman recursion. A deliberately
incomplete sum that omits root quartic terms fails Ward cancellation.
Complex three-point seeds are not presented as real noncollinear scattering.

Ten new groups and all 61 previous groups pass (71 total). JSON retains all
32 ordered amplitude/current records per five-point kinematic point, with
spinors, references and independent values. This is still finite exact
computational evidence. Full five-gluon color reconstruction, on-shell
recursion, general proofs and the Agda integration remain open. The closed
reference explicitly rejects six-point NMHV instead of incorrectly returning
zero for a sector it does not implement.

```
python research/nima/amplitudes/gluon_five_check.py --output research/nima/results/gluon-five-ordered.json
```

## Six-gluon NMHV checkpoint: independent on-shell recursion

`gluon_bcfw.py` implements adjacent BCFW sewing without calling the off-shell
Feynman engine or an n>=4 closed formula. Inputs are the complex three-point
seeds, the all-same-helicity tree zero, and the Yang-Mills large-z boundary
condition for admitted shifts. With tilde_i -> tilde_i-z tilde_j and
lambda_j -> lambda_j+z lambda_i, (-,+), (-,-) and (+,+) shifts are admitted;
(+,-) is rejected. The large-z theorem is physical input, not something the
finite benchmark proves.

Each channel retains its unshifted momentum and propagator, shift
coefficient, pole, internal spinors, opposite internal helicities, complete
left/right subamplitudes and sewn contribution. The explicit convention
-P=(-lambda_P,tilde_P) gives contribution A_L A_R/P^2. Four- and five-point
calibration checks all helicities against the earlier independent formulas.

`gluon_six_check.py` then compares all 20 six-point NMHV helicity assignments
at two generic real rational kinematic points: 40 nonzero complex amplitudes
agree with the off-shell current calculation. No six-point NMHV closed
formula is used. Other checks cover selected MHV/anti-MHV/zero sectors,
different admitted shifts, Ward/reference invariance, and a recursive audit
of on-shell poles, conserved shifted momenta and internal-state sewing.
An independent hexagon-dissection enumeration matches the 38 off-shell
planar diagrams: 14 four-cubic, 21 two-cubic/one-quartic, and 3 two-quartic.

### Exceptional shifts are an explicit domain boundary

The independent comparison caught an actual edge-case bug on symmetric
back-to-back kinematics: skipping a zero shift coefficient returned zero
for a nonzero amplitude. A generic finite pole can move to infinity under
specialization, so the generic large-z argument cannot simply be reused at
that exceptional point.

The corrected engine rejects such a shift and tries another admitted
rotation, recording failures. The original symmetric point is retained in
regressions: one case succeeds by changing charts; another has a finite
nonzero off-shell result but is explicitly refused by this conservative
adjacent-shift backend. It is NOT silently assigned zero. Resolving every
such exceptional input needs additional shift charts or analytic limits.

Nine new groups and all 71 previous groups pass (80 total). JSON retains all
40 NMHV comparison values, complete on/off-shell histories for four examples,
and the original exceptional-input refusal/fallback records. The calculator
still lacks general analytic proofs, full six-gluon color reconstruction and
Agda certification.

```
python research/nima/amplitudes/gluon_six_check.py --output research/nima/results/gluon-six-nmhv.json
```

## Exact pole-residue and positive-soft checkpoint

`gluon_pole_coefficients.py` extracts coefficients directly from the ordered
Feynman trees. A marked zero propagator retains its numerator as a residue
instead of dividing by zero. Multilinear vertices propagate the marked
coefficient separately from diagrams not containing the marked edge. That
second component is NOT the Laurent finite part: derivatives of pole
numerators are deliberately not computed.

`gluon_limits_check.py` checks the three inequivalent planar 3|3 channels
of alternating-helicity six-gluon NMHV at two starting points. BCFW shifts
supply complex on-shell pole locations, but the residue itself is extracted
from the off-shell Feynman tensors. All six nonzero residues agree with the
sum of products of independent four-point Parke-Taylor amplitudes, using
opposite internal helicities and the previously fixed -P spinor convention.
Two additional helicity-forbidden residues vanish although the corresponding
uncut amplitudes are nonzero. Nine of the 38 planar diagrams contain each
tested 3|3 cut. Reference changes, cyclic root changes and all external Ward
substitutions also pass for the residue.

For a positive-helicity soft leg s, the family is lambda_s(tau)=tau lambda_s.
Writing lambda_s=alpha lambda_a+beta lambda_b for its cyclic neighbours,
tilde_a(tau)=tilde_a+(1-tau) alpha tilde_s, and similarly for b. This preserves
nullness and momentum conservation exactly. The external soft polarization
contributes 1/tau. Each adjacent soft propagator contributes another 1/tau,
with its coefficient obtained from the exact nonzero derivative of P^2.
The two marked channels cannot coexist in a planar tree. At six points,
10 diagrams contribute for each attachment, while 18 have neither pole.

The exact tau^-2 coefficients agree with

    <a b> / (<a s><s b>) * A_(n-1)

for all three positive legs of alternating six-point NMHV at both starting
points: six nonzero checks against the five-point anti-MHV reference.
Four five-point MHV families additionally satisfy the special exact finite-tau
identity tau^2 A_5(tau)=S A_4 at three nonzero parameter values each; this
stronger identity is NOT claimed for NMHV. Reference/Ward checks pass, and
omitting either adjacent soft attachment fails at the retained hostile case.

No near-pole numerical fit is used. Zero external momentum is allowed only
as formal boundary data in the coefficient engine, not as a physical input
to ordinary amplitude evaluation. Coincident unmarked poles, zero soft
propagator slopes and compatible marks requiring higher-order Laurent terms
are explicitly rejected. Negative-helicity and subleading soft extraction,
multiple compatible cuts, general proofs and Agda certification remain open.

Nine new groups and all 80 previous groups pass (89 total). JSON retains
complete histories for the six nonzero residues and six NMHV soft coefficients,
including boundary momenta, slopes, reference spinors and independent values.

```
python research/nima/amplitudes/gluon_limits_check.py --output research/nima/results/gluon-pole-soft.json
```

## Negative-soft and two-particle factorization checkpoint

`gluon_pole_coefficients.py` now also constructs the anti-holomorphic soft
family: tilde_s(tau)=tau tilde_s, with conserving shifts of the neighbouring
lambda spinors. Swapping spinor spaces is used only to construct this family;
the negative-helicity coefficient is independently extracted from the actual
Feynman tensors and negative-helicity polarizations, not obtained by assuming
an amplitude parity identity.

In the reverse-determinant square convention, the leading soft factor is

    -[a b] / ([a s][s b]).

The minus sign follows the relative (-1)^n anti-MHV convention and is tested
against nonzero complex coefficients, not squared amplitudes. All three
negative legs of alternating six-point NMHV at both starting points pass:
six coefficients agree with this factor times the five-point MHV reference.
Four five-point anti-MHV families also pass the special exact finite-tau
identity at three parameter values each. Ward and reference checks pass;
calling the negative extractor on a positive-helicity leg is rejected.

`gluon_chiral_limits_check.py` additionally tests 24 nonzero 2|4 residues:
all six adjacent channels at two starting points, using two alternating
helicity assignments and both complex three-point branches. The residue is
extracted from Feynman trees and compared with three-point branch seeds times
five-point MHV/anti-MHV formulas. A wrong three-point branch is zero, not an
evaluation of a 0/0 expression. Ten of the 38 planar diagrams contain each
such cut. Tests also cover non-real internal little-group rescaling,
cyclic root changes and all external Ward substitutions. These complex
branch tests are not presented as simultaneous real collinear limits.

Six new groups and all 89 previous groups pass (95 total). JSON retains all
six negative-soft and 24 residue histories with independent values. Together
with the preceding checkpoint, leading soft coefficients of both helicities
and all types of six-point planar factorization channels now have finite
checks. Subleading soft terms, compatible multiple cuts, exceptional-chart
completion, full higher-point color assembly, general proofs and the Agda
bridge remain open.

```
python research/nima/amplitudes/gluon_chiral_limits_check.py --output research/nima/results/gluon-chiral-limits.json
```

## Four/five-graviton tree checkpoint

`gravity_tree.py` now supplies two computational paths for four-dimensional
pure external gravitons in two-derivative Einstein gravity:

- An unordered BCFW recursion with explicit Einstein three-point bracket
  seeds and ONLY helicities +/-2 in the internal sum. It enumerates every
  subset separating the shifted legs, not only planar ordered partitions.
- Four/five-point KLT using the existing off-shell Yang-Mills Feynman engine
  for both copies. This path does not obtain its Yang-Mills values from the
  gravity recursion or closed Parke-Taylor expressions.

### Phase, coupling and theory scope

The gravity convention strips overall -i and (kappa/2)^(n-2), with positive
three-point bracket-ratio squares. With -P=(-lambda_P,tilde_P), sewing is
+M_L M_R/P^2: two -i M factors and the i transverse spin-two propagator leave
an overall -i. The corresponding KLT kernels are -s AA at four points and
+ss AA+ss AA at five. The first comparison exposed a four-point mismatch
from mixing an i-stripped sewing convention with these kernels; the chosen
-i convention is now explicit and guarded by a nonzero signed regression.
Five-point agreement alone would not have caught that sign.

The Einstein cubic seeds, same-helicity zero, good-shift boundary theorem
and KLT relation are declared physical inputs. There is no Einstein-action
vertex derivation in this checkpoint. The pure external graviton tree sector
of Yang-Mills double copy agrees with Einstein gravity; the unprojected
product theory also contains dilaton/two-form states. This benchmark does
NOT establish pure Einstein gravity for matter amplitudes or loops.

### Checked coverage

`gravity_tree_check.py` compares all 16 four-point helicity assignments at
four rational points and all 32 five-point assignments at two points:
128 exact complex comparisons, 64 nonzero. Tests additionally cover:

- Full four-point Bose permutations and selected five-point transpositions.
- Independent shift choices and independent reference choices in each copy.
- Factorized tensor Ward substitutions in either Yang-Mills copy.
- Spin-two little-group weights and stripped mass dimension two.
- Recursive momentum/pole/internal-state audits and the gravity bonus
  identity sum(z_pole * contribution)=0, consistent with 1/z^2 falloff.
- Hostile sign/kernel changes and omission of a nonzero bonus residue.

Eight new groups and all 95 previous groups pass (103 total). JSON stores all
comparison values and representative full gravity recursion and Yang-Mills
current histories. This is finite exact evidence, not a proof of the boundary
theorem or KLT, not a new physical prediction, and not Agda-certified.

```
python research/nima/amplitudes/gravity_tree_check.py --output research/nima/results/gravity-trees-four-five.json
```

## Massive scalar one-loop bubble checkpoint

`scalar_one_loop.py` implements the four-point amplitude through order
lambda^2 in real massive phi^4 theory, L_int=-lambda phi^4/4!, with
S=1+iT and M_tree=-lambda. Unlike the exact tree modules, this checkpoint
uses floating-point transcendental functions and numerical quadrature.

The regulator is d=4-2 epsilon with unmodified DR integration measure;
Delta=1/epsilon-gamma_E+log(4 pi). The coupling is MSbar-subtracted and m>0
is the pole mass. The momentum-independent one-loop tadpole is assumed
absorbed in the mass counterterm; its LSZ derivative is zero. That tadpole
and its counterterm are not independently evaluated here.

For each of the s,t,u channels, the bubble has symmetry factor 1/2:

    B(s) = - integral_0^1 log((m^2-s x(1-x)-i0)/mu^2) dx,
    M = -lambda + lambda^2/(32 pi^2) * (B(s)+B(t)+B(u)).

The common ultraviolet pole is removed by

    delta_lambda = 3 lambda^2 Delta/(32 pi^2),

whose vertex contribution is -delta_lambda. The amplitude wrapper requires
s+t+u=4m^2; it is not a light-external/heavy-internal model. There is no
massless limit or infrared-divergent calculation in this implementation.

`scalar_one_loop_check.py` compares 36 bubble cases using a piecewise closed
form and independent logarithmic Feynman-parameter integration. At/above
threshold the latter splits at the real roots and uses a quartic endpoint
map to integrate the logarithmic singularities. No finite numerical i0 is
substituted for the boundary prescription. The physical upper rim has
Im B=+pi sqrt(1-4m^2/s), and the lower rim is its conjugate; no second-sheet
continuation is claimed.

Additional checks include:

- Once-subtracted dispersion reconstruction below threshold from the cut.
- Finite-epsilon spacelike Gamma(epsilon) parameter integrals converging to
  Delta+B, separately from the epsilon^0 Laurent subtraction bookkeeping.
- Order-by-order scale cancellation with beta_lambda=3 lambda^2/(16 pi^2),
  without retaining uncontrolled higher powers from a resummed coupling.
- The forward optical theorem, 2 Im M_loop=(1/2!) integral dPhi_2 |M_tree|^2,
  using an independently evaluated on-shell two-body phase-space measure.
  Omitting the identical-state factor or reversing the cut sign fails.
- Scalar crossing permutations, dimensionless scaling and domain guards.

The quadrature target is 1e-11; closed-form comparisons allow 3e-10 absolute
error. Adaptive Simpson error estimates are NOT rigorous bounds. Exhausting
the subdivision depth raises an error rather than returning an unchecked
value. Eight new groups and all 103 previous groups pass (111 total).

JSON retains numerical values, accepted quadrature panels/error estimates,
finite-epsilon records, physical amplitudes and cut comparisons. This is a
numerical one-loop benchmark, not an exact transcendental identity proof,
not an independently complete mass-renormalization calculation, and not an
Agda-certified result.

```
python research/nima/amplitudes/scalar_one_loop_check.py --output research/nima/results/scalar-one-loop-bubble.json
```

## Heavy portal loop: light-scalar EFT and spectral positivity

`scalar_portal_eft.py` declares a DIFFERENT theory from the preceding massive
phi^4 example: external phi has tuned pole mass zero, internal chi has mass
M_chi>0, and L_int=-lambda_phi phi^4/4! - g phi^2 chi^2/4. Only the heavy
one-loop g^2 correction is included. Light lambda_phi^2 loops and other
coupling orders are not calculated, so this is not the unrestricted complete
one-loop portal amplitude. Light mass tuning remains an assumed subtraction.

The amplitude requires s+t+u=0, not 4M_chi^2. The zero-momentum matching is

    lambda_EFT = lambda_phi + 3g^2/(32 pi^2) log(M_chi^2/mu^2).

After subtracting this local quartic, each bubble has the expansion

    B(s)-B(0) = sum_(n>=1) c_n (s/M_chi^2)^n,
    c_n = (n!)^2 / (n (2n+1)!).

The coefficients and invariant sums are exact Fractions. Independent exact
polynomial integration checks c_n through n=12; numerical parameter moments
provide another comparison. The linear term cancels because s+t+u=0. This
is an on-shell four-point cancellation, NOT a claim that all off-shell
dimension-six operators vanish.

For the explicitly normalized basis

    L_EFT += c (partial_mu phi partial^mu phi)^2,

all 24 derivative assignments give M_contact=2c(s^2+t^2+u^2), and matching yields

    c = g^2/(3840 pi^2 M_chi^4).

The test enumerates these assignments rather than assuming the contact
normalization. Truncations through invariant powers 2, 4, 8 and 12 are compared
at 16 light-scattering points with the full heavy-loop expression. The tail
bound follows from the geometric logarithm series and |x(1-x)|<=1/4:

    |R_N(s)| <= c_(N+1) |s/M_chi^2|^(N+1) / (1-|s|/(4M_chi^2)).

The expansion API requires exact inputs and |s_i|<4M_chi^2. Floating-point
comparisons include a 3e-12 numerical allowance; this is not certified
interval evaluation of the full amplitude.

The forward s^2 coefficient is 4c. Nine mass/coupling samples agree with an
independent dispersion integral using the tree production process
phi phi -> chi chi and its identical-heavy-particle phase space. Both the
right and crossed left cuts are included; omitting the crossed cut fails.
The resulting coefficient is positive for nonzero g and zero when g=0.
This is a heavy-sector check, not a general positivity theorem for a full
massless theory with light-loop infrared cuts.

`scalar_portal_eft_check.py` also checks threshold matching/scale running,
heavy-mass decoupling, crossing and above-threshold heavy-state unitarity.
Eight new groups and all 111 previous groups pass (119 total). JSON records
all 64 truncation comparisons, rational tails and the nine spectral histories.

```
python research/nima/amplitudes/scalar_portal_eft_check.py --output research/nima/results/scalar-portal-eft.json
```

## Scalar tadpole, mass-scheme and LSZ audit

`scalar_mass_renormalization.py` independently audits the tadpole assumptions
used by the earlier massive and portal loop checkpoints. With inverse
propagator p^2-m_R^2-Sigma_R and insertion -i Sigma, define

    T(epsilon) = M^2 Gamma(epsilon)/(1-epsilon)
                 * (4 pi mu^2/M^2)^epsilon
               = M^2[Delta+1-log(M^2/mu^2)] + O(epsilon).

The Wick contraction factor is 1/2 for both phi^4/4! and phi^2 chi^2/(2!2!).
The continued Euclidean integral is J_E=-T/(16 pi^2), so the vertex factor
(-ic/2) gives Sigma_loop=-cT/(32 pi^2), where c=lambda or g. A mass
counterterm adds +delta_m^2 to Sigma. This fixes the sign before testing
cancellation rather than fitting a counterterm to a desired pole.

The Gamma result is compared with a separate proper-time representation
that subtracts six ultraviolet Taylor terms explicitly, retains their
analytic pole terms, and numerically integrates the remainder and tail.
There are 60 comparisons spanning two masses, two scale ratios, five
regulator values and three proper-time splits. A convergent d=1 Euclidean
radial integral fixes the normalization and sign independently. Near d=4,
the tadpole is analytic dimensional continuation, NOT a convergent positive
Euclidean integral; the pole at d=2 must not be ignored.

MSbar removes the Delta term. On-shell subtraction also removes the finite
constant, giving Sigma_R=0 at this order. The tests check:

- Finite-epsilon convergence to the retained Laurent finite part.
- MSbar/on-shell pole-mass conversion and portal tuning to a zero light pole.
- Scale independence after the one-loop mass change
  c M^2/(32 pi^2) log(mu_new^2/mu_old^2), holding reference-order inputs fixed.
- The tadpole mass-derivative identity with the zero-momentum bubble.
- Zero external-momentum derivative of this constant self-energy, hence
  one-loop LSZ residue Z=1. This is not a higher-loop statement.
- The distinction between a portal mass tuning proportional to M_chi^2 and
  a matched derivative operator that decouples as M_chi^-4. No vacuum-stability
  claim or new bound follows from this comparison.

`scalar_mass_renormalization_check.py` adds nine groups; all 128 groups pass.
JSON retains proper-time quadrature/subtraction histories and mass-scheme
records. Transcendental comparisons remain numerical (5e-9 integral
comparison tolerance), with non-certified error estimates. This closes the
finite tadpole audit for the selected scalar sectors, not complete portal
renormalization, general proofs or the Agda bridge.

```
python research/nima/amplitudes/scalar_mass_renormalization_check.py --output research/nima/results/scalar-mass-renormalization.json
```

## Causal above-threshold bubble dispersion checkpoint

`scalar_bubble_dispersion.py` reconstructs the massive bubble above threshold
from its spectral density and the declared MSbar subtraction constant
B(0)=-log(m^2/mu^2). The cut does NOT determine that local constant by itself.
With t=4m^2/(1-v^2) and b=sqrt(1-4m^2/s), the principal-value kernel splits as

    2v^2/(v^2-b^2) = b/(v-b) + (2v+b)/(v+b).

The smooth part is integrated numerically. The singular part contributes
b log((1-b)/b), and the physical upper/lower rim adds +/-i pi b analytically.
No finite numerical i0 is used to define the real-axis result.

`scalar_bubble_dispersion_check.py` supplies:

- 20 above-threshold comparisons among dispersion, closed form and logarithmic
  Feynman-parameter integration.
- Nine direct integrations of the original spectral kernel outside symmetric
  pole windows. Adding the missing smooth window recovers the PV without
  extrapolation; the uncorrected sequence is also checked for convergence.
- Discontinuity agreement with independently evaluated two-body phase space,
  plus hostile omitted-imaginary-part and omitted-boundary-term checks.
- 20 off-axis comparisons between spectral and complex-log parameter
  integration, including Schwarz reflection and the absorptive sign.
- Four finite complex-invariant samples approaching the upper rim. These are
  separate analytic-function evaluations, not replacements for the causal
  real-axis prescription.
- Scale covariance, subtraction-constant dependence and explicit rejection
  of unresolved endpoint-merged pole charts.

Seven new groups and all 128 previous groups pass (135 total). JSON retains
PV, excision, off-axis and approach-to-cut integration histories. The target
quadrature tolerance is 1e-11 and comparisons allow 3e-10; neither estimates
nor comparisons are formally certified. Second-sheet continuation, light-loop
infrared issues and higher-loop amplitudes are not established by these tests.

```
python research/nima/amplitudes/scalar_bubble_dispersion_check.py --output research/nima/results/scalar-bubble-dispersion.json
```

## Advancement gates

1. **Scalar trees:** massless four/six/eight-point and massive cubic/quartic
   four/five/six-point benchmarks now checked computationally. General
   enumeration/factorization proofs and higher mixed-interaction cases remain
   open; the direct mixed six-point reference is not implemented.
2. **Formal integration:** encode physical conventions, labelled diagrams,
   exact propagator domains and recursive rules; connect actual evaluation
   histories to the Agda comparison interface. Prove enumeration and
   reconstruction rather than importing observed numerical agreement as a law.
3. **Spin and gauge:** distinct-flavour elastic scattering, Compton and
   antiparticle annihilation now have spin/trace/invariant and Ward checks.
   Spin-summed analytic crossing is checked at finite points. Full amplitude
   crossing phases, helicity states and physical-parameter numerics remain open.
4. **Non-Abelian gauge theory:** six-point ordered NMHV has independent
   off-shell/BCFW, 3|3 and 2|4 residue, and both leading chiral soft checks.
   Exceptional shift charts remain visible. Full higher-point color assembly,
   subleading limits and general proofs remain separate obligations.
5. **Gravity and matter:** four/five pure-graviton trees now match unordered
   spin-two recursion and off-shell-Yang-Mills KLT. Gravity soft/factorization
   limits, higher multiplicities and an Einstein-action calculation remain
   open; the pure-tree state restriction must not be carried into loops.
6. **Loops:** massive scalar bubbles now have causal dispersion checks below,
   above and off the cut, alongside tadpole, pole-mass and LSZ audits. Next
   executable gate: a massive triangle integral and the heavy-portal
   six-light-scalar one-loop contribution, with labelled diagram counting
   and a separately normalized low-energy phi^6 matching check. Light-loop
   IR, complete portal renormalization and higher loops remain open.
7. **Broader regimes:** a specified heavy-portal EFT now has low-energy
   matching and forward heavy-sector positivity checks. Full light-loop EFT
   matching, symmetry breaking, curved backgrounds and nonperturbative
   amplitudes still require separate assumptions and methods.

At every stage retain the theory, conventions, domain restrictions, complete
calculation histories and comparisons. Mark results as reproduced, newly
computed within a known model, or genuinely new only with appropriate
independent evidence. The earlier graph-backed native-boundary comparison
lift and arbitrary-source boundary obligations remain open.
