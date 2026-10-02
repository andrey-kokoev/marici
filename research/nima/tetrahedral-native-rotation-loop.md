# Native rotation-loop test: the extra spinor is not selected

## Question and claim boundary

Operator requested an independent test of the conjecture that the collective
excitation retains rotation-path information requiring the extra spinor factor.
The requested physical discriminator is a relative minus sign for an
orthogonal-half-turn commutator, obtained without inserting spinor transport.

**Disposition:** the native-source version fails in the declared tetrahedral
model. Coherent frame transport and its selected-line restriction give +1.
Bare projector products can give negative amplitudes on other routes, but do
not supply the required commutator phase. The broader physical conjecture is
untested: no independent physical rotation interaction/readout for this
excitation was supplied. This is not a laboratory refutation of spin.

SCC obligation: route compatibility before physical readout descent. Strength:
exact source-model calculation plus an arbitrary-path telescoping identity.
The finite position set is A4; the coefficient field is Q(i sqrt(3)). No
continuous physical path, physical time, or completion is inferred from it.

## Deutsch–Popperian test

- **Problem:** distinguish a physically required degree of freedom from an
  optional representation added to match spinorial behavior.
- **Bold conjecture:** independently specified native coherent operations
  already require a negative commutator return; the doublet is their smallest
  compatible amplitude realization.
- **Rivals:** endpoint vector transport suffices; projector interference creates
  a sign without spinorial composition; an inserted module or apparatus phase
  supplies the desired sign.
- **Risky consequence:** the loop of orthogonal half-turns has relative phase
  pi without using the preceding binary-tetrahedral checker. Consistent vertex
  rephasings cannot change that closed-route discriminator.
- **Strongest available falsifier:** reconstruct native maps and compare all
  six ordered half-turn commutators under three explicitly distinct route
  rules, with gauge and injected-sign controls.
- **Disposition with residual:** the native negative-commutator claim is
  falsified; the physical selection claim stops at the missing interaction.
  Adding an unselected spinor to repair the sign would assume the conclusion.

## Independent source operations

Only the original
[`check_twelve_triangle_positive_geometry.py`](checkers/check_twelve_triangle_positive_geometry.py)
and its triangle-arithmetic dependency are imported. The checker does not
import the Pauli matrices, quaternion lift, or tensor extension.

Let r_x be the source-derived tetrahedral rotations and

\[
v_0=(-2/3,\;1/3+i\sqrt3,\;-1/3+i\sqrt3),\qquad
v_x=r_xv_0,\qquad n=v_0^*v_0=20/3,\qquad P_x=v_xv_x^*/n.
\]

Three distinct mathematical operations are available:

1. Frame transport: \(F_{yx}=r_yr_x^T\).
2. Covariant selected-line transport:
   \(T_{yx}=P_yF_{yx}P_x=v_yv_x^*/n\).
3. Bare projection: apply \(P_y\) without the rotation that carries the
   previous line into the new one.

These are linear maps/filters, not independently realized physical
interactions. Using rule 3 instead of rule 2 changes the operation, not its
presentation.

## Composition first, amplitude second

The source maps obey

\[
F_{zy}F_{yx}=F_{zx},\qquad
T_{zy}T_{yx}=T_{zx},\qquad T_{xx}=P_x.
\]

The second identity follows by cancelling \(v_y^*v_y=n\); the checker also
tests all 1,728 triples for each law. Consequently every closed selected-line
route, of any length, acts as the identity on its starting line. This
arbitrary-length statement follows from the displayed composition law, not
from extrapolating finitely many successful loops.

For a closed route \(x_0,\ldots,x_m=x_0\), define the normalized native
return coefficient by pairing the composed map with \(v_{x_0}\). Frame and
covariant selected-line transport give

\[
a_F=a_T=1.
\]

The bare-projection coefficient is instead

\[
a_P=\frac{v_{x_0}^*P_{x_m}\cdots P_{x_1}v_{x_0}}{n}
=\prod_{j=1}^m\frac{v_{x_j}^*v_{x_{j-1}}{n}.
\]

It is a coherent filter amplitude. Treating its modulus squared as an actual
laboratory probability would additionally require a physical implementation.

## The commutator discriminator

The original half-turn matrices are
\(h_x=\operatorname{diag}(1,-1,-1)\), with the analogous y and z versions.
They commute and square to I. Their reference-line coefficients are

\[
a_x=-13/15,\qquad a_y=a_z=-1/15.
\]

For chronological moves \(h_a,h_b,h_a^{-1},h_b^{-1}\), the endpoint is I.
Every ordered pair of distinct axes gives:

| Rule | Single-loop amplitude | Relative phase |
|---|---:|---:|
| Native frame transport | 1 | 0 |
| Native selected-line transport | 1 | 0 |
| Bare projections, x/y or x/z | 169/50625 | 0 |
| Bare projections, y/z | 1/50625 | 0 |

The projector value is \(a_a^2a_b^2\), strictly positive. Repeating the loop
squares its attenuated coefficient; the coherent transport remains +1. The
proposed spinorial phase pi is absent under every tested native rule.

The model records endpoint rotations. It does not contain the physical
continuous paths between them. If inverse moves are supplied as inverse
continuous half-turn paths, their topological lift is the discriminator
proposed in the conjecture; the source model does not retain or select that
lift. Endpoint factorization is therefore an explanatory limit of the model,
not evidence that physical rotation paths cannot matter.

## The negative-amplitude oddball

The three-step route using x, y, z half-turns also has identity endpoint.
Bare projections give

\[
a_P(x,y,z)=a_xa_ya_z=-13/3375.
\]

Thus a negative return amplitude is already possible without a spinor. Yet
its commutator test gives the positive coefficients above. Shortcutting the
first two projection moves to their endpoint changes the triangle coefficient
to +1/225, while coherent transport still gives +1. These are different
projection routes; no physical homotopy equivalence is asserted.

On this V4 orbit the normalized one-step overlap phases form a scalar
cochain: phase(I)=+1 and phase(h_x)=phase(h_y)=phase(h_z)=-1. Its multiplier

\[
c(a,b)=\lambda(a)\lambda(b)/\lambda(ab)
\]

is a coboundary and is symmetric in a,b. Hence its multiplier commutator is
+1, not the nontrivial spinorial commutator. The triangle sign is explained
projector interference, not evidence for the extra factor.

## Hostile controls

Vertex-frame phases \(v_x\mapsto\lambda_xv_x\), with unit-modulus
\(\lambda_x\), telescope out of closed-route amplitudes. Exact signs and cube
roots of unity were tested; all projectors and both chosen loop coefficients
are unchanged.

Conversely, multiplying one selected-transport edge by -1 creates the desired
commutator return -1 while leaving the local projectors intact. It also makes

\[
\|T_{zy}T_{yx}-T_{zx}\|_F^2=4
\]

on a specific composition cell. This exposes the inserted sign as new
transport data, not a consequence of local-line matching or vertex gauge.
A coherent nontrivial cover is possible with extra data, as the
[binary tetrahedral bridge](binary-tetrahedral-spinor-bridge.md) already
shows; this test does not classify all such enlargements.

## Physical source audit and stop condition

The inspected candidate physical notes do not remove the missing premise:

- [Rotor action](mass-rotor-action-and-external-charge.md) explicitly adds rotor
  variables, inertias, gauge fields, and external coupling as physical inputs.
  It does not provide a spatial rotation-path amplitude for this excitation.
- [Primitive quotient charge](mass-primitive-quotient-charge.md) chooses a new
  external U(1) identification. It supplies neither the required spatial
  double-cover selection nor fermionic statistics.
- [Retained rotor phase transport](retained-rotor-phase-transport.md) obtains
  a negative return conditional on an already specified defining module and
  real Clifford/symplectic realization. Importing that sign here would not be
  an independent derivation. Its checker was not rerun in this audit.

**First missing object:** an independently specified physical interaction that
maps rotation paths to amplitudes for this excitation, together with its
coherent reference/readout. Reopen the physical branch only when that object
is supplied and tested without inserting the desired spinorial phase. No
further hypothetical carrier is proposed to evade the present failure.

## Verification

```text
python research/nima/checkers/check_tetrahedral_native_rotation_loop.py
python research/aspect/scc/scc.py check tetrahedral-native-rotation-loop
python research/aspect/scc/scc.py categorical research/nima/contracts/tetrahedral-native-rotation-loop.json
python research/aspect/scc/scc.py inverse research/nima/contracts/tetrahedral-native-rotation-loop.json native_spinor_selection
```

Results: `results/tetrahedral-native-rotation-loop.json`.
Registration: [`scc-models/tetrahedral-native-rotation-loop.json`](scc-models/tetrahedral-native-rotation-loop.json).
The checker exits zero when the falsification audit succeeds; its
`scientific_disposition` explicitly reports rejection of the native-source
conjecture. The categorical contract is expected to reject
`native_spinorial_return`, with scalar residual 2, and to leave physical
realization unsupported. SCC compares declared map tokens; the exact checker
verifies their scalar reductions from the native matrices.

Verification receipts: direct checker and SCC model check passed; manifest
validation passed; categorical compilation exited 1 with the expected failed
spinorial-return cell; inverse design reported the missing witnesses above.
No physical experiment or newly sourced Hamiltonian was tested.

Durability: preregistration
`ev-000000015674-c2586175-270f-401b-80b7-dcd0ee0abc97` and result
`ev-000000015675-fedb7412-e579-4653-a58e-4fce02625f61` are admitted records,
not truth certifications. This turn's four new checker/packet/contract/manifest
files are untracked. The known uncommitted event interval is 15672–15675,
including the preceding spinor-bridge work. No commit or push was authorized;
no checker remains running.
