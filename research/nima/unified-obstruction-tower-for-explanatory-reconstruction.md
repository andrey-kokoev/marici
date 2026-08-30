# Unified obstruction tower for explanatory reconstruction

## Status

This packet unifies local hidden deformations, global sheet ambiguity,
monodromy, and completion escape as distinct failures of one quotient
observation map. It supplies a global-inverse criterion and a finite audit order.

## 1. Quotient observation map

Let \(\mathcal E\) be a typed realization space, let \(G\) be the authorized
gauge action, and define the explanatory quotient

\[
X=\mathcal E/G.
\]

Let \(Y\) be the complete contextual record space and let

\[
N:X\longrightarrow Y
\]

be the experimental nerve. Explanatory reconstruction asks whether \(N\) has a
well-defined, stable inverse on its image.

The problem is therefore not merely kernel computation. It is an inverse
problem on a quotient space.

## 2. The obstruction tower

Four logically ordered obstructions can prevent reconstruction.

### Gate 0: quotient typing

The action of \(G\) must be declared and \(N\) must be constant on its orbits.
If an authorized gauge transformation changes the record, the interface is
unsound. If an unauthorized source difference is placed in \(G\), the quotient
has erased the claim before observation begins.

### Gate 1: local ramification

At a regular realization \(x\), the induced derivative

\[
DN_x:T_xX\longrightarrow T_{N(x)}Y
\]

must be injective on the claimed tangent directions. A nonzero vector in its
kernel is a local hidden modulus.

This is the infinitesimal full-abstraction gate.

### Gate 2: global multiplicity

Even if every derivative is injective, a fibre

\[
N^{-1}(y)
\]

may contain several points. These can form a finite torsor, disconnected rivals,
or a higher-dimensional component missed by the chosen local chart.

This is the global fibre gate.

### Gate 3: monodromy

Local inverse branches may fail to glue. Lifting a closed loop in \(N(X)\) can
return to a different source sheet. The resulting deck action records a global
frame obstruction.

This is the continuation gate.

### Gate 4: nonproper or ill-conditioned escape

There may be a sequence \(x_n\) leaving every controlled source region while
\(N(x_n)\) converges, or normalized source differences may have vanishing
observational separation. Then the inverse is discontinuous or unbounded even
when exact fibres are singletons.

This is the completion-stability gate.

## 3. Covering criterion

Suppose \(X\) and \(N(X)\) are connected, locally path-connected Hausdorff
spaces, and

\[
N:X\longrightarrow N(X)
\]

is a proper local homeomorphism. Then \(N\) is a covering map with finite fibres
over compact base regions.

Consequently:

1. the number of source sheets is locally constant;
2. continuation around loops acts on each fibre by monodromy;
3. if \(N(X)\) is simply connected, every connected covering has one sheet;
4. under that additional hypothesis, \(N\) is a homeomorphism onto its image.

This criterion turns the obstruction tower into explicit proof obligations:
local invertibility, properness, connectedness, and trivial covering data.

## 4. Smooth quantitative criterion

Let \(X\) and \(Y\) be finite-dimensional metric manifolds of equal dimension.
Assume \(N\) is continuously differentiable, proper, and has invertible
derivative everywhere. Then \(N\) is a local diffeomorphism and hence a covering
of its image under the usual connectedness hypotheses.

If the image is simply connected, \(N\) is globally one-to-one on each connected
source component.

For stable reconstruction, add an authorized metric lower bound

\[
\|DN_xv\|_Y\ge c_K\|v\|_X
\]

on every declared compact regime \(K\subseteq X\). A global positive constant is
needed only when the programme claims global uniform stability.

Thus topology controls sheet multiplicity, while the derivative bound controls
conditioning.

## 5. Classification by failed hypothesis

The common hostile examples now have exact locations.

### Sign sheet

\[
x^2=1,
\qquad
N(x)=x^2.
\]

The source is disconnected and the fibre has two points. Local rigidity holds;
global uniqueness fails at Gate 2.

### Power map

\[
N(z)=z^m,
\qquad
z\neq0.
\]

The derivative is invertible, but the map is an \(m\)-sheet covering with
nontrivial deck action. Gates 2 and 3 fail.

### Cubic cusp

\[
N(x)=x^3.
\]

The map is globally injective, but the derivative vanishes at zero and the local
inverse is not Lipschitz there. Gate 1 fails quantitatively without producing a
global rival.

### Escaping inverse

\[
N_N=
\begin{pmatrix}
1&0\\
0&N^{-1}
\end{pmatrix}.
\]

Every finite map is bijective, but the inverse norms diverge. Gate 4 fails under
completion.

## 6. Properness as the missing finite-to-limit bridge

Finite injectivity does not prevent normalized source states from escaping into
directions whose records converge. Properness forbids this by requiring compact
record sets to have compact source preimages.

In linear Hilbert settings, bounded-below quotient observation is the relevant
analogue:

\[
\|Nx\|\ge c\,\operatorname{dist}(x,K).
\]

In rigged or nonlinear settings, one should instead state compactness or graph
closedness in the source-authorized topology. Bounded Hilbert-space language
must not be imposed when the constructor is only a Schwartz-to-boundary trace.

The shared question is whether convergence of records forces controlled
convergence of source classes.

## 7. Three-lens factorization

Let

\[
X_{\mathrm{ord}}
\xrightarrow{q_1}
X_{\mathrm{phase}}
\xrightarrow{q_2}
X_{\mathrm{add}}
\]

represent ordered holonomy, determinant-line phase, and additive current
forgetting. The complete scalar record factors through

\[
N_{\mathrm{add}}q_2q_1.
\]

Each forgetful map can fail at a different gate:

- \(q_1\) can identify nonconjugate ordered words with the same determinant;
- \(q_2\) can identify opposite phase or orientation sheets;
- completion of \(N_{\mathrm{add}}\) can lose properness without any finite
  algebraic kernel.

The total scalar fibre is assembled from these successive fibres. A scalar
zero, equality, or positivity statement cannot identify which layer created the
ambiguity without typed intermediate records.

## 8. Toric-code instantiation

For local syndrome readout on a fixed torus, let \(\mathcal P/\mathcal S\)
denote Pauli errors modulo stabilizers and let \(\mathcal Y_{\mathrm{syn}}\)
denote local syndromes. The map

\[
N_{\mathrm{syn}}:\mathcal P/\mathcal S\longrightarrow\mathcal Y_{\mathrm{syn}}
\]

has a four-point logical fibre. The failure is global and discrete, not
infinitesimal.

Adding two independent loop probes refines the target so that each logical fibre
becomes one stabilizer class. This repairs Gate 2 on the finite logical-state
claim.

Across growing lattices, implementation noise can still make the criticism
margin collapse. Gate 2 remains repaired algebraically while Gate 4 can fail
physically.

## 9. Operator-algebra instantiation

Central Wilson data can be locally and globally faithful only on the centre. It
has a genuine fibre on the endpoint block algebra. Flux-resolved endpoint ports
refine the nerve and reduce that fibre.

For \(D(S_3)\), one transposition and one three-cycle port generate the full
endpoint block algebra. This is an algebraic Gate 2 repair for block control.
It does not prove proper physical implementation or a nonvanishing executable
margin, so Gate 4 remains separate.

## 10. Finite audit order

Every sector should run the gates in this order:

1. freeze the source quotient and authorized gauge;
2. verify observation invariance under gauge;
3. compute local deformation kernels;
4. compute exact global fibres on the finite packet;
5. classify deck actions and source frames;
6. identify the smallest authorized context splitting each non-gauge fibre;
7. compute metric-typed local criticism margins;
8. test properness, closed range, or graph closure through completion;
9. state algebraic and executable cost profiles separately.

Skipping directly to a smallest eigenvalue conflates Gates 0, 1, and 4.
Checking only finite fibres misses Gate 4. Checking only derivatives misses Gates
2 and 3.

## 11. Unified falsifier schema

A bounded obstruction certificate should report:

- the claimed quotient \(X\);
- the contextual map \(N\);
- the first failed gate;
- a tangent vector, fibre pair, monodromy loop, or escaping sequence;
- the authorized gauge comparison;
- the smallest additional source context known to repair the defect;
- whether the repair is algebraic, topological, analytic, or executable.

The first failed gate matters because later repairs cannot compensate for an
earlier typing error.

## 12. Unified DPC

An explanation is reconstructively adequate over a declared regime when its
complete contextual nerve descends to the authorized source quotient, is locally
faithful, has one global sheet, has trivial non-gauge monodromy, and admits a
stable inverse in the source-authorized completion topology.

Equivalently, explanatory failure is classified by the first obstruction among
typing, ramification, multiplicity, monodromy, and escape.

## 13. Critic

This criterion can become too strong if explanation does not require source
reconstruction. A theory may explain a robust quotient while deliberately
leaving microscopic states many-to-one.

The repair is to apply the tower only to the quotient explicitly claimed by the
explanation. Many-to-one projection below that quotient is allowed. Many-to-one
projection inside the claimed object must be typed as gauge, torsor, or unresolved
moduli rather than ignored.

## 14. Bottom line

The previously separate problems are one inverse problem viewed at different
scales:

- derivative kernels are local failures;
- logical sectors and sign sheets are global fibres;
- phase transport produces monodromy;
- disappearing singular values and escaping states are failures of properness
  or stable inversion.

The programme now has a single question for every proposed explanatory
interface:

> At which gate does reconstruction first fail, and what source-authorized
> context repairs exactly that obstruction without importing authority from a
> stronger lens?
