# Labelled Log-Node Odd Counit and the Literal Six-Functor Gate

Date: 2026-08-15  
Status: proved in the finite labelled log/Kato--Nakayama endpoint model.
The literal mixed-variance six-functor source realization, the simultaneous
three-normal or \(\mathbb P^2\)-vertex Beck--Chevalley theorem, and the
physical endpoint/\(Q\) mapping fibre remain unconstructed. No epistemic
graph admission is claimed.

## Correction to the endpoint gate

Entry 194 proved that its finite endpoint equivariance presentation has
cokernel \(\mathbb Z/2\), and that one endpoint-supported boundary of odd
coefficient is the minimal algebraic repair. It did not prove that the
labelled Rees/log geometry lacks such a boundary. Its central-support
restriction was explicitly a declared zero input.

The labelled log node already supplies the missing odd coefficient in the
finite local model. Consequently entry 194 remains a valid no-go for the
unenlarged finite endpoint presentation, but it is not a no-go against the
logarithmic endpoint counit constructed here.

## Labelled Rees rigidity

Work on the selected Rees chart

\[
B=\mathbb Z[x_5,t_5],
\qquad
u_5=x_5t_5,
\]

with \(x_5,u_5,t_5\) retained as labelled sections. If an automorphism fixes
\(x_5\) and \(u_5\), then

\[
x_5\bigl(\phi(t_5)-t_5\bigr)=0.
\]

The chart is \(x_5\)-torsion-free, hence \(\phi(t_5)=t_5\). Thus the
rescaling ambiguity available on the isolated exceptional fibre does not
extend to an automorphism of the labelled Rees chart.

Equivalently, when a local generator is replaced by
\(t'_5=a t_5\), its inverse-line generator changes by
\((t'_5)^\vee=a^{-1}t_5^\vee\). The evaluation

\[
I_{t_5}^{\vee}\otimes I_{t_5}\longrightarrow\mathcal O,
\qquad
t_5^\vee(t_5)=1,
\]

is invariant. This is line evaluation, not a fitted scalar trivialization or
an inversion of \(t_5\).

## Relative logarithmic sign lattice

For the divisorial log node use the characteristic-monoid map

\[
P=\mathbb N\langle u_5\rangle
\longrightarrow
Q=\mathbb N\langle x_5\rangle\oplus
\mathbb N\langle t_5\rangle,
\qquad
1\longmapsto(1,1).
\]

Its relative characteristic group is

\[
L_{\log}
=Q^{\rm gp}/P^{\rm gp}
=\mathbb Z^2/\mathbb Z(1,1)
\simeq\mathbb Z.
\]

The branch-labelled functional

\[
\delta_{t_5}([a,b])=b-a
\]

is well defined and primitive:

\[
\delta_{t_5}([e_{t_5}])=+1,
\qquad
\delta_{t_5}([e_{x_5}])=-1.
\]

Exchanging the two branches sends \(\delta_{t_5}\) to
\(-\delta_{t_5}\). Hence \(L_{\log}\) is the required integral sign
line, not merely a rank-one module with an arbitrarily chosen generator.

## Canonical Kato--Nakayama cut

Over a fixed base angle the local Kato--Nakayama fibre is

\[
T_{\rm KN}
=
\{(h(x_5),h(t_5)):h(x_5)h(t_5)=h(u_5)\}
\simeq S^1.
\]

Entry 105 already assumes that the positive real chamber fixes the radial
basepoint on every oriented normal circle. Therefore \(h(u_5)=1\) is not
new fitted endpoint data. The labelled sections

\[
h(t_5)=1,
\qquad
h(x_5)=1
\]

meet at the same marked point of \(T_{\rm KN}\), while distinguishing its
two branch germs. Cutting at this marked point, orienting by
\(\delta_{t_5}\), and taking the pair relative to the \(x_5\)-side gives

\[
C_*^{\rm BM}(I,\partial_{x_5}I)
=
\left[
\mathbb Z\langle e\rangle
\xrightarrow{+1}
\mathbb Z\langle v_{t_5}\rangle
\right].
\]

This is the literal one-normal Boolean shape in entry 143:

\[
e\longmapsto[S,H=\{5\}],
\qquad
v_{t_5}\longmapsto[S,H=\varnothing],
\]

and its boundary \(+1\) is the target normal-removal differential. The
positive-real basepoint and the two labelled branch germs remove the
otherwise unpointed choice of a cut.

## Primitive odd boundary

Entry 192 supplies the special class and deformation Bockstein

\[
z=t_5g-h,
\qquad
\beta_\lambda([z])=-t_5p.
\]

At the node \(t_5=0\), the interval edge maps as \(z\mapsto-h\).
Its Boolean boundary is therefore \(-p\). On the coefficient side,
tensoring the Bockstein with \(I_{t_5}^{\vee}\) and applying the canonical
evaluation gives the same result:

\[
I_{t_5}^{\vee}\otimes I_{t_5}\langle p\rangle
\longrightarrow\mathbb Z\langle p\rangle,
\qquad
t_5^\vee(-t_5p)=-p.
\]

Thus the finite branch-selected log endpoint counit has coefficient
\(m=-1\), or \(+1\) after reversing the declared branch orientation. In
either convention it is primitive and odd, so it satisfies exactly entry
194's minimal repair criterion.

## Shifts and rotated edge purity

In homological conventions the relative log fibre contributes \([1]\),
while extraordinary restriction along the selected \(t_5\)-branch
contributes \([-1]\). These cancel. The remaining shift is the
\(x_5\)-Cartier coorientation shift \([-1]\), transported from entry 131.

Entry 105 proves strict \(D_3\) covariance of the target support complex.
Cyclic relabelling transports entry 131's normalized \(x_3\)-edge purity
to the rotated \(x_5\)-edge with sign \(+1\). The generator square above
then has both composites equal to \(-p\); no endpoint sign is fitted.

This cyclic transport is target-side only. Entry 131 is an
original/Borel--Moore Cartier costalk on the whole edge \(x_5=0\), where
\(t_5\) remains free. The log source is supported at the branch centre
\((x_5,t_5)=0\) and begins in reciprocal-regular
normalization/conductor variance. Rotation does not manufacture the
mixed-variance source functor.

## Exact boundary of the theorem

The theorem constructs the finite labelled log/KN coefficient and cellular
endpoint correspondence. It does not yet construct a literal morphism

\[
\operatorname{Sp}^{\log,!}_{x_5,t_5}
\bigl(\mathcal S^{\rm norm,reg}_{v_+}\bigr)
\longrightarrow
E_{v_+}^{\rm BM,\check C}
\]

in a common six-functor category. In particular, still unconstructed are:

1. the sheaf-level realization transporting entry 105's positive-real
   basepoint from the target BM model to the reciprocal-regular
   normalization source;
2. extraordinary/proper base change identifying the branch-centre support
   with every lower term of entry 143's BM--Cech endpoint object;
3. the simultaneous three-normal, or exceptional \(\mathbb P^2\)-vertex,
   Beck--Chevalley comparison needed to prove compatibility of the three
   local odd counits at \(v_+\);
4. the polarity-conjugate \(v_-\) realization and its reflection square;
5. the based generic \(Q\) comparison, two connector cells, and the actual
   endpoint/\(Q\) mapping fibre.

Therefore \(p_{\partial,Q}\) and its polarity Bockstein remain undefined.
The new theorem removes the local coefficient-parity obstruction; it does
not select the global butterfly point.

## Falsifiers

The finite theorem is falsified if:

- a nontrivial labelled Rees automorphism fixes \(x_5\) and \(u_5\) but
  changes \(t_5\);
- \(\delta_{t_5}\) fails to descend through \(\mathbb Z(1,1)\), is
  nonprimitive, or is reflection-even;
- entry 105 does not supply the positive-real radial basepoint;
- the relative cut interval has boundary other than \(+1\);
- its Boolean image differs from entry 143's normal-removal coefficient;
- the two routes from \(z\) give different multiples of \(p\);
- the log and \(t_5\)-extraordinary shifts fail to cancel; or
- cyclic transport changes entry 131's normalized target purity sign.

A failure of the still-unconstructed six-functor or
\(\mathbb P^2\)-vertex comparison does not falsify this scoped finite
theorem.

## Provenance and validation

Exact certificate:

- `research/voevodsky/check_d03_labelled_log_odd_counit.rs`
- SHA-256
  `1e8b26ff441c0d9196ecf3c468d09d1c9efc04a36a912a4877fae86945f470ef`

Worker MCP validation, run
`run-7335fdec10f148b0a26af3cb366c5ba1`:

~~~text
rustfmt --edition 2021 --check: pass
rustc --edition=2021 -D warnings --emit=metadata: pass
temporary .rmeta removed and confirmed absent
~~~

Runtime assertions were not executed because the host MSVC linker is
unavailable. The warnings-denied metadata compilation validates the exact
source and typechecks every assertion.

Dependencies are entries 105, 131, 143, 173, 190, 192, and 194. No graph
admission is claimed.

## Outcome contract

~~~json
{
  "claim": "In the finite labelled log/Kato-Nakayama endpoint model for u5=x5*t5, the labelled Rees chart is rigid, the relative characteristic lattice is the polarity sign line, entry105's positive-real basepoint gives a canonical branch cut whose relative interval is entry143's one-normal Boolean factor, and the entry192 Bockstein followed by the canonical t5-line dual evaluation gives a primitive odd endpoint counit compatible with the cyclicly rotated entry131 target purity.",
  "status": "proved_scoped_finite_labelled_log_endpoint",
  "scope": "finite labelled log/Kato-Nakayama coefficient and cellular endpoint model only; no literal mixed-variance six-functor source realization, simultaneous P2-vertex Beck-Chevalley theorem, physical mapping fibre, or graph admission",
  "factorization": {
    "rees_chart": "u5=x5*t5",
    "labelled_chart_rigid": true,
    "dual_evaluation_rescaling_invariant": true,
    "relative_characteristic": "Z^2/Z(1,1)=Z_or",
    "branch_functional": "delta_t5([a,b])=b-a",
    "branch_swap": -1,
    "positive_real_basepoint": "declared input from entry105",
    "KN_relative_interval": "[Z --+1--> Z]",
    "entry143_normal_boolean_match": true,
    "DNC_Bockstein": "beta_lambda([z])=-t5*p",
    "dual_evaluation": "t5^vee(-t5*p)=-p",
    "odd_counit_coefficient": -1,
    "log_t_extraordinary_net_shift": 0,
    "remaining_x5_purity_shift": -1,
    "rotated_entry131_target_sign": 1,
    "literal_six_functor_source_realization": "unconstructed",
    "P2_vertex_Beck_Chevalley": "unconstructed",
    "physical_mapping_fiber": "unconstructed",
    "physical_p_partial_Q": "undefined",
    "physical_Bockstein": "undefined"
  },
  "checker_sha256": "1e8b26ff441c0d9196ecf3c468d09d1c9efc04a36a912a4877fae86945f470ef",
  "evidence_refs": [
    "research/voevodsky/check_d03_labelled_log_odd_counit.rs",
    "src/ledger/20260814-105 Absolute Support Complex, Shift-Corrected Purity, and the Marked-Correspondence Obstruction.md",
    "src/ledger/20260814-131 D03 Cartier Edge Purity and the Scoped PC Promotion.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-173 Component-Supported Semistable Node and the vplus Coefficient Counit.md",
    "src/ledger/20260815-192 Flat DNC Log-Node Bockstein and the Toric Framing Gate.md",
    "src/ledger/20260815-194 Endpoint Equivariant Splitting No-Go and the Odd Counit Gate.md"
  ],
  "counterevidence": [
    "The finite KN interval does not itself instantiate a sheaf-level mixed-variance source functor.",
    "Cyclic transport proves the target x5 purity sign but not branch-centre-to-edge base change.",
    "Compatibility of three local counits at the full endpoint vertex is not proved.",
    "No generic Q leg or endpoint connector cell is constructed."
  ],
  "minimal_remaining_geometry": "A literal log/extraordinary six-functor realization of the finite branch-cut correspondence, followed by simultaneous P2-vertex Beck-Chevalley, polarity reflection, and the based Q connector.",
  "next_experiment": "Construct the simultaneous three-normal log blowup at v_plus and prove its vertex Beck-Chevalley restrictions are the three finite odd counits before forming the reflected endpoint or Q mapping fibre."
}
~~~
