# The eleventh theta quarter-turn closes the local model orbit

## Ordered-port correction

This local orbit closes for a chosen characteristic transfer function. The
current full-Weyl characteristic function is not the theta cross transfer.
Theta closure therefore requires a framed characteristic construction for the
bordered Rosenbrock pencil, with ordered incoming endpoint and outgoing source
ports preserved throughout.

Exact Sz.-Nagy--Foias characteristic-function closure. The tenth turn promotes
Hardy defect memory to a canonical contraction. The eleventh turn uses the
contraction and its two defect ports to reconstruct an analytic transfer
function. For a completely nonunitary contraction, this characteristic
function is a complete unitary invariant up to constant unitary gauges on the
defect spaces.

Thus the local sequence does not grow forever. Once both boundary ports are
retained, it closes back onto the causal inner factor.

## Fixed contraction and defect ports

Let \(A\) be a contraction on \(\mathcal K\), with

\[
D_A
=
\left(I-A^*A\right)^{1/2},
\qquad
D_{A^*}
=
\left(I-AA^*\right)^{1/2}.
\]

Let

\[
\mathcal D_A
=
\overline{\operatorname{Ran}D_A},
\qquad
\mathcal D_{A^*}
=
\overline{\operatorname{Ran}D_{A^*}}.
\]

The two defect spaces are the incoming and outgoing boundary types. Their
separate identities are required for the next turn.

## The eleventh quarter-turn

Define the characteristic function

\[
\Theta_A(z)
=
\left.
\left(
-A
+
zD_{A^*}
\left(I-zA^*\right)^{-1}
D_A
\right)
\right|_{\mathcal D_A},
\qquad
|z|<1.
\]

It maps the incoming defect space to the outgoing defect space:

\[
\Theta_A(z):
\mathcal D_A
\longrightarrow
\mathcal D_{A^*}.
\]

For a completely nonunitary contraction, \(\Theta_A\) is contractive and
analytic. In the finite pure case it is inner.

The state machine and its boundary attachment have rotated back into a causal
transfer object.

## Degree-one closure

For the scalar contraction

\[
A=\overline a,
\qquad
|a|<1,
\]

we have

\[
D_A=D_{A^*}=\sqrt{1-|a|^2}.
\]

Substitution gives

\[
\Theta_A(z)
=
-\overline a
+
\frac{z(1-|a|^2)}{1-az}
=
\frac{z-\overline a}{1-az}.
\]

This is the degree-one Blaschke factor associated with the model state. The
zero, memory eigenvalue, defect ports, unitary dilation, and causal transfer
are different views of one local object.

## Closure up to boundary gauge

If two completely nonunitary contractions are unitarily equivalent, their
characteristic functions differ only by constant unitary identifications of
the incoming and outgoing defect spaces. Conversely, agreement of the
characteristic functions under such defect-space gauges determines the
contraction up to unitary equivalence.

The local orbit is therefore

\[
\Theta
\longrightarrow
\mathcal K_\Theta
\longrightarrow
A_\Theta
\longrightarrow
\left(\mathcal D_A,\mathcal D_{A^*}\right)
\longrightarrow
\Theta_A,
\]

with

\[
\Theta_A
\simeq
\Theta.
\]

The final equivalence is not literal equality until the two boundary gauges
are fixed.

## Meaning of the first closure

The earlier rotations kept producing new objects because each lower-level
view had forgotten a fiber. Here the necessary fiber has been restored:

- the factor supplies causal orientation;
- the model space supplies memory;
- the contraction supplies internal evolution;
- the two defect spaces supply boundary incidence;
- the characteristic function recombines them into transfer.

Once these components coexist, another turn returns to the starting transfer
type. This is the first evidence that a genuine orbit-complete local object
exists.

## Why this still does not explain RH

The closure theorem is universal. Every completely nonunitary contraction has
a characteristic function, and every finite Blaschke product appears in this
way. Hostile zero configurations therefore enjoy the same closed orbit.

The theorem proves architectural completeness, not arithmetic selectivity.

The RH-bearing distinction must enter through the source authority of the
boundary gauges and incidence maps. Generic operator theory permits arbitrary
unitary identifications

\[
V_{\rm in}:\mathcal D_A\longrightarrow\mathcal D_A',
\qquad
V_{\rm out}:\mathcal D_{A^*}\longrightarrow\mathcal D_{A^*}'.
\]

Theta/Tate data must construct the permitted gauges and forbid hostile ones
without inspecting zero locations.

## Relation to the counter-turn

The counter-turn and the forward eleventh turn share the same defect data but
use it differently:

- the counter-turn forms a unitary Julia--Halmos boundary evolution;
- the forward turn forms the analytic characteristic transfer function.

These are complementary projections of one conservative colligation. Their
coherence is the next square to test against the labelled arithmetic source.

## Source coherence square

At each finite theta cutoff, the desired square is

\[
\begin{array}{ccc}
A_X & \longrightarrow & \mathcal J_{A_X}\\
\downarrow & & \downarrow\\
\Theta_{A_X} & \longrightarrow & U_X
\end{array}
\]

where the horizontal arrows expose boundary flow and the vertical arrows form
the characteristic transfer. The square must commute under the source-fixed
incoming and outgoing port identifications.

Scalar agreement of the two lower readouts is not sufficient. The complete
defect-space maps and residue data must agree.

## Finite falsifiers

The claimed source closure fails if:

- the theta boundary currents do not span the two defect spaces;
- the source port gauges differ from those required by the characteristic
  function;
- the Julia and characteristic constructions produce incompatible transfer
  maps;
- the square commutes only after determinant projection;
- or a hostile Blaschke factor satisfies every declared source condition.

## Decisive conclusion

Yes, the tenth object can turn forward into an eleventh. The eleventh turn is
the characteristic function, and it closes the local operator-theoretic orbit
back onto the causal factor up to boundary gauge. This is the first genuine
closure of the rotation programme. It also isolates the remaining arithmetic
question: whether theta/Tate source data canonically fixes the defect ports and
their gauges in a way hostile inner factors cannot imitate.
