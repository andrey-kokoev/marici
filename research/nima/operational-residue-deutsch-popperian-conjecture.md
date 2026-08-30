# Deutsch--Popperian operational-residue conjecture

## Problem

Across software control systems and the current Marici sectors, an admitted
operation can produce information that an ordinary success value does not
contain: a domain rejection, curvature, boundary residue, extension class,
relation cell, or missing homotopy.  Calling all of these “errors” erases
their typing.  Calling them one universal obstruction object erases their
different degrees, supports, and composition laws.

The explanatory question is whether the recurrence has one hard-to-vary
structure, or whether it is only a verbal family resemblance.

## Deutsch--Popperian conjecture

Let \(\mathsf{Op}\) be the category of source-admitted operations.  Every
operation \(f\) that participates in a physical or computational composition
has a source-derived **resolved result object** \(\widetilde R_f\), equipped
with:

1. an ordinary-value projection \(v_f:\widetilde R_f\to Y_f\);
2. an operation-specific residue grade, fiber, or branch \(O_f\);
3. typed composition maps over composable operations;
4. coherence cells making those compositions associative at the declared
   level;
5. an independently specified readout or augmentation.

Schematically,

\[
\boxed{
\widetilde R_g\;\widetilde\circ\;\widetilde R_f
\longrightarrow \widetilde R_{g\circ f}
\longrightarrow Y_{g\circ f}.
}
\]

The residue is the information required to explain why composition at the
ordinary-value level fails to be conservative, strictly coherent, or
extendable.  It is not required to be an alternative to the value: depending
on the operation, it may be a coproduct branch, a fiber, a shifted grade, or
an extension cell.

The conjecture is Deutschian because it proposes one explanatory constraint:
lawful composition must preserve enough typed information to account for its
own failures.  It is Popperian because the existence, source derivation, and
coherence of \(\widetilde R_f\) are independently falsifiable for every
chosen operation pair.

## Prohibitions

The conjecture does not permit:

- manufacturing a residue after observing the desired readout;
- treating an unauthorized or mistyped attempt as an operational residue;
- replacing operation-specific residue types by one scalar error score;
- retaining the whole source input merely to make reconstruction tautological;
- changing the target category until a failed composition closes;
- inferring physical observability from the existence of a residue.

## Falsifiers

For a frozen composable pair \((f,g)\), the conjecture fails if:

1. no source-derived resolved result object exists;
2. its proposed residue depends on a gauge, splitting, or presentation not
   preserved by the source symmetry;
3. one of the mixed value/residue compositions is undefined;
4. associativity requires a new post-hoc cell;
5. ordinary projection cannot recover the established operation;
6. the proposed readout is not independently authorized;
7. the only conservative resolution is the trivial one that stores the
   complete input history.

## Attack 1: the universal coproduct is false

The earlier provisional shape

\[
\mathsf{Result}_f=Y_f\sqcup O_f
\]

is already too narrow.  In the exact filtered-jet pilot, multiplication at
depth two has an ordinary value in

\[
A_2=k[x]/(x^3)
\]

and a simultaneous next-grade residue

\[
B(u,v)=u_1v_2+u_2v_1.
\]

The pairs

\[
(u,v)=(1+x,1+x^2),
\qquad
(u',v')=(1,1+x+x^2)
\]

have the same ordinary depth-two product

\[
1+x+x^2,
\]

but residues \(1\) and \(0\).  Returning the success branch loses information
needed for the next extension; returning only the obstruction branch loses
the current value.  Here the correct result is an extension/product-like
object containing both.

The checker also verifies that the lifted value-plus-residue multiplication
is associative and exactly reproduces multiplication through degree three.
Thus the naive universal sum is falsified, while the resolved-result
conjecture survives its first attack.

## What the first attack explains

“Normal-channel obstruction” is not fundamentally an error protocol.  It is
a projection phenomenon:

\[
\boxed{
\text{resolved lawful result}
\longrightarrow
\text{ordinary visible result},
}
\]

whose forgotten relative information may appear as an error branch in one
system and as a coherence grade in another.  Sonar's discriminated RPC result
and Marici's next-grade cocycle are therefore not the same container.  They
are two realizations of the stronger rule that the ordinary readout need not
be conservative.

## Next hostile test

The jet algebra is only a positive toy model.  Freeze one genuine Marici
composition square—preferably restriction followed by Gysin/Čech sewing—and
construct its source-derived resolved result.  Export the mixed branch/grade
compositions and associator.  If the existing principal or seam cell closes
them without a fitted correction, the conjecture gains physical-sector
content.  If not, retire universality and retain only the software analogy.

## Evidence

- `research/nima/checkers/check_operational_residue_result_shapes.py`
- `research/nima/results/operational-residue-result-shapes.json`
- `research/nima/filtered-interaction-jet-pilot.md`
- `research/nima/carrier-remote-local-operational-module-conjecture.md`

## Attack 2: the physical \(C_3\) result is a nonsplit filtered object

The cyclic soft-star/Tate packet supplies the first source-derived Marici
test.  Let

\[
A=\mathbf F_3[C_3],
\qquad
\varepsilon:A\to\mathbf F_3,
\qquad
I=\ker\varepsilon.
\]

Ordinary source sewing is \(\varepsilon\).  The retained supported residue is

\[
H_{\rm Tate}=I/(g-1)I.
\]

The exact sequence

\[
0\longrightarrow I\longrightarrow A
\xrightarrow{\varepsilon}\mathbf F_3\longrightarrow0
\]

does not split \(C_3\)-equivariantly.  Indeed, every invariant vector of the
regular module is a multiple of the norm vector

\[
N=(1,1,1),
\]

but in characteristic three

\[
\varepsilon(N)=3=0.
\]

An equivariant section of \(\varepsilon\) would have to send \(1\) to an
invariant vector of augmentation one, and no such vector exists.  Therefore
the resolved result cannot be canonically factorized as

\[
\text{visible scalar}\oplus\text{residue}.
\]

It must remain the nonsplit filtered/derived object.

The source-derived cyclic soft-star Gysin map is

\[
G_{\rm soft}=1_A.
\]

It preserves \(I\), commutes with \(g-1\), and hence induces the identity on
\(H_{\rm Tate}\).  At the same time,

\[
\varepsilon G_{\rm soft}|_I=0.
\]

Thus one legal physical operation transports a nonzero supported residue
through the ordinary source module even though the final scalar readout
annihilates it.  No representative of the Tate quotient and no splitting of
the augmentation sequence is chosen.

This closes the first genuine Marici composition square:

\[
\begin{array}{ccc}
I & \xrightarrow{G_{\rm soft}} & I\\
\downarrow & & \downarrow\\
I/(g-1)I & \xrightarrow{1} & I/(g-1)I,
\end{array}
\qquad
\varepsilon G_{\rm soft}|_I=0.
\]

### Disposition after Attack 2

The conjecture survives, but its type is sharper:

\[
\boxed{
\text{resolved result}=
\text{operation-indexed filtered/derived object, generally nonsplit}.
}
\]

The “value” and “residue” are views, grades, or quotients of that object—not
necessarily independent branches or fields.  This is the first point at
which the Sonar analogy and the physical mathematics diverge usefully:
software commonly serializes a discriminated response, whereas the Marici
source can carry a nonsplit extension whose scalar serializer destroys a
real supported class.

New exact certificate:

- `research/nima/checkers/check_operational_residue_c3_nonsplit.py`;
- `research/nima/results/operational-residue-c3-nonsplit.json`.

## Attack 3: nonidentity deck composition produces a residue law

The finite-deck Mackey calculus supplies a nonidentity composition test.  For
a surjective finite deck map \(q:G\twoheadrightarrow H\) of degree
\(d_q=|\ker q|\), unnormalized transfer satisfies

\[
q_!q^*=d_q\,\operatorname{id}.
\]

Relative to the requested strict retraction, define the typed norm residue

\[
E_q=q_!q^*-\operatorname{id}
=(d_q-1)\operatorname{id}.
\]

For composable quotients

\[
G\xrightarrow{q}H\xrightarrow{r}K,
\]

covering degrees multiply.  Hence the scalar residue coordinate
\(e_q=d_q-1\) obeys

\[
\boxed{
e_{rq}=e_q+e_r+e_qe_r.
}
\]

This operation is associative and has unit zero because it is multiplication
transported through \(e\mapsto1+e\).  The residue therefore composes, but not
by naive accumulation.  It remembers the multiplicative geometry of the
cover.

The readout boundary is equally sharp.  Unnormalized transfer preserves the
frozen identity selector,

\[
q_!\delta_{0,G}=\delta_{0,H},
\]

while normalized transfer \(d_q^{-1}q_!\) removes \(E_q\) only by changing
that selected value to \(d_q^{-1}\delta_{0,H}\).  The residue cannot be
“repaired” without changing the independently frozen readout, except when
\(d_q=1\).

This is a positive nonidentity test of the operational-residue conjecture at
the algebraic Carrier-calculus level:

- the residue is derived before the readout;
- it has an exact associative composition law;
- it distinguishes unnormalized integral transport from rational splitting;
- erasing it changes a source-fixed selector.

It is not yet a physical-sector pushforward theorem.  The existing Marici
sources do not authorize arbitrary quotient-cover pushforward on relative
chains.  Thus the authority gate itself remains part of the conjecture:
algebraic composability does not manufacture physical admission.

New exact certificate:

- `research/nima/checkers/check_operational_residue_deck_composition.py`;
- `research/nima/results/operational-residue-deck-composition.json`.

## Attack 4: the physical three-wall jet derives its principal residue

The physical cosmology wall family supplies an authority-sensitive test that
does not assume a quotient-cover pushforward.  Its three fiber normals fit the
source-derived exact sequence

\[
0\longrightarrow T_{\rm fiber}
\xrightarrow{J}N_{\rm walls}
\xrightarrow{\lambda}P
\longrightarrow0,
\]

with

\[
J=\begin{pmatrix}0&1\\1&0\\1&1\end{pmatrix},
\qquad
\lambda=(-1,-1,1).
\]

External base motion acts on the wall equations through

\[
B=
\begin{pmatrix}
0&-1&-1\\
-1&0&-1\\
0&0&1
\end{pmatrix}.
\]

The exact obstruction identity is

\[
\boxed{
\lambda B=\kappa=(1,1,3)=d(x+y+3z).
}
\]

Thus the resolved first-jet result is not an arbitrary pair.  It lands in the
graph object

\[
\widetilde R
=\{(n,p)\in N_{\rm walls}\oplus P:\lambda n=p\},
\]

by

\[
v\longmapsto(Bv,\kappa v).
\]

The residue is the derivative of the already present source function

\[
p=x+y+3z,
\qquad
-q_1-q_2+q_3=p.
\]

It is therefore source-derived before any desired rank or readout is
inspected.  Moreover, its restrictions to the pairwise wall intersections
are forced:

\[
q_3|_{W_1\cap W_2}=p,
\qquad
q_2|_{W_1\cap W_3}=-p,
\qquad
q_1|_{W_2\cap W_3}=-p.
\]

The exact checker verifies the sequence, the graph condition, the
solvability criterion for homogeneous fiber correction, and all three
pair-intersection signs.  Generic motion cannot be repaired inside
\(T_{\rm fiber}\); it closes only after retaining the principal grade.

### Honest disposition

This is a positive physical-source first-jet realization of the resolved
result architecture.  It is **not** yet a full success for the conjecture.
The universal logarithmic nearby line on \(p=0\) has since been constructed.
What remains unconstructed is the full twisted Čech/nearby-cycle totalization,
so the total differential

\[
D=\delta+(-1)^p\partial
\]

has not yet been proved to satisfy \(D^2=0\) with this principal cell.
Accordingly:

\[
\boxed{
\text{source derivation and first-jet closure: passed;}
\qquad
\text{higher coherence: open.}
}
\]

This is the first attack that reaches the conjecture's actual failure gate.
If the twisted supported totalization cannot absorb the derived \(p\)-cell
without an additional fitted correction, the operational-residue conjecture
fails in its strong form.

New exact certificate:

- `research/nima/checkers/check_operational_residue_three_wall_graph.py`;
- `research/nima/results/operational-residue-three-wall-graph.json`.

## Attack 5: principal residue composes with the canonical nearby line

The source identity

\[
q_3=q_1+q_2+p
\]

gives the exact logarithmic circuit formula

\[
\omega_{23}-\omega_{13}+\omega_{12}
=p\,\frac{dq_1\wedge dq_2}{q_1q_2q_3}.
\]

After division by \(p\) and specialization, its transverse coefficient is
one and its oriented pair-symbol vector is

\[
\ell=(1,-1,1).
\]

Consequently the moving-normal residue from Attack 4 composes canonically
with the nearby-line constructor:

\[
T_{\rm base}
\xrightarrow{\kappa}N_p
\xrightarrow{\ell}L_{\rm nearby},
\]

with matrix

\[
\ell^T\kappa
=
\begin{pmatrix}1\\-1\\1\end{pmatrix}
\begin{pmatrix}1&1&3\end{pmatrix}.
\]

This map has rank one and is fixed entirely by the source wall equations and
the oriented logarithmic circuit.  No basis vector in the pair-symbol space
is selected afterward.

The physical readout then supplies a distinct final gate.  In the literal
positive chamber,

\[
p=X_1+X_2+3X_3>0,
\]

so the chamber has no generic support on \(p=0\).  The algebraic nearby line
is therefore nonzero while the frozen literal-chain readout annihilates it.
This is the same resolved-result architecture seen in Attack 2, now with a
nonidentity source-derived composition:

\[
\boxed{
\text{base motion}
\to\text{principal residue}
\to\text{nearby line}
\to\text{zero literal-chain readout}.
}
\]

### Remaining falsifier after Attack 5

The support and vertical nearby-cycle composition are now constructed.  The
remaining strong-form gate is horizontality: combine the nearby line with the
twisted Gauss--Manin differential and verify the mixed square, or exhibit its
source-derived homotopy.  Until then the result is a source-typed vertical
composition, not a horizontal local system or physical period class.

New exact certificate:

- `research/nima/checkers/check_operational_residue_three_wall_nearby_composition.py`;
- `research/nima/results/operational-residue-three-wall-nearby-composition.json`.

## Attack 6: the obvious horizontal filler fails source typing

The existing moving-localization calculation tests the natural next
candidate more strongly than the vertical nearby-line census.  Its mixed
curvature

\[
\Theta=dF+A_CF-FA_A
\]

has directionwise rank one and stable raw support.  The proposed filler tried
to identify that raw rank-two parity space with the supported graph-principal
space derived from the normal jets.

Exact replicated reduction shows instead

\[
\dim P_{\rm raw}=2,
\qquad
\dim P_{\rm graph}=2,
\qquad
P_{\rm raw}\cap P_{\rm graph}=0.
\]

For both parameter axes,

\[
\operatorname{rank}
\bigl(\Theta-(\Theta i)\pi_J\bigr)=1.
\]

Neither the raw rank-two projection nor the full rank-three jet projection
has connection-invariant kernel, and the raw modular covector is
nonhorizontal.  Therefore the proposed \(P_{02}\) principal filler does not
define a source-derived bicomplex.  Its putative \(D^2\) is not a typed object.

This is a genuine negative result for the operational-residue programme:

\[
\boxed{
\text{vertical source residue}
\not\Rightarrow
\text{horizontal resolved-result lift}.
}
\]

The nearby line from Attack 5 remains valid vertically, and the literal
positive-chain readout remains zero.  What fails is the claim that the
currently available graph-principal cell absorbs its horizontal transport.

### Popperian correction

The statement “every remaining failure is itself a higher residue” would make
the conjecture immune to refutation.  It is prohibited.  A nonzero residual
counts as supporting the conjecture only when its target object and boundary
map were independently derived before the residual was inspected.

Accordingly, the strong existential version is superseded by the
**constructive operational-residue conjecture**:

> An admitted operation has a resolved-result interpretation only when the
> source calculus independently supplies the filtered/derived target, the
> residue map, and their composition laws; the proposed resolution must then
> pass source typing and coherence without enlargement after failure.

For the present three-wall horizontal system the disposition is:

\[
\boxed{
\text{vertical resolved result: established;}
\quad
\text{tested horizontal resolution: falsified;}
\quad
\text{alternative: not predeclared.}
}
\]

No new filler is sought inside this test.  Reopening requires a distinct
relative-support complex derived from source geometry independently of the
rank-one residual, with its maps frozen before evaluation.

Durable negative certificate:

- `research/nima/physical-theta-graph-principal-cell.md`;
- `research/nima/checkers/certify_physical_theta_graph_cell.py`;
- `research/nima/results/physical_theta_graph_cell_certificate.json`.
