# The Clark–Grushin comparison is generated on the bulk solution cone

## Constructor-level finding

The characteristic border and the unrestricted observation cone impose different equations. The border retains the bulk equation P x=W c. The observation cone [X->F] records O x and permits arbitrary x in its graph domain.

On an invertible bulk chart, their shared closure is obtained by restricting the observation to the bulk solution graph. The comparison then has explicit chain maps and a contracting homotopy. This gives the common attachment diagram at local-chart strength.

## Source records and domains

The characteristic packet supplies

D = [[P,-W],[-O,0]] : X direct-sum F -> Y direct-sum F,

where P=P_plus direct-sum P_minus, F=C^2, W=W_01 S_Cl*, and its proposed characteristic observation is O_char=W_Cl^times. The independent Green record supplies O_green=S_Cl O_01 on the graph domain X.

Use a chart on which P:X->Y is boundedly invertible, with X carrying its declared graph norm. Require W:F->Y and O:X->F bounded. The following construction is valid for any such O; it does not presume equality of O_char and O_green.

The completed seam may fail the invertibility hypothesis. That chart limitation remains explicit throughout.

## 1. Bulk solution attachment

Define

Z_PW = {(x,c) in X direct-sum F : P x=W c}.

The source evaluation a:F->Z_PW is a(c)=(P^-1 Wc,c), with inverse the second projection. The Green observation on this generated source is

o(x,c)=-O x.

Its two-term cone [Z_PW -> F], in degrees -1 and 0, identifies with

[F --S--> F], S=-O P^-1 W.

Thus the two routes are concrete:

- form the bordered bulk-and-output complex, then contract the invertible bulk;
- solve the bulk attachment, then take the cone of its output.

Both come from the same P,W,O operations before taking a determinant.

## 2. Explicit contraction of the border

Let C_D=[X direct-sum F --D--> Y direct-sum F] and C_S=[F --S--> F]. Define

i_-1(c)=(P^-1 Wc,c), i_0(f)=(0,f),

r_-1(x,c)=c, r_0(y,f)=f+O P^-1 y.

Direct multiplication gives D i_-1=i_0 S, r_0 D=S r_-1, and r i=I.

The degree-minus-one homotopy is h(y,f)=(P^-1 y,0). It satisfies

h D=I-i_-1 r_-1, D h=I-i_0 r_0.

Hence C_D deformation-retracts onto C_S. These equations construct the cofiber comparison at the chain level, including the bulk residual component.

## 3. Why restriction changes the earlier edge audit

When X has finite dimension n and O:X->C^2 is surjective, the unrestricted observation cone retains an (n-2)-dimensional kernel. An invertible border has zero cohomology. Those complexes cannot be equivalent in that fixture.

The exact checker uses n=3 and gives a one-dimensional unrestricted observation kernel while the border and its Schur matrix are invertible. The solution restriction is therefore substantive attachment data.

For instance, a source-preserving degree-minus-one map x->(x,c(x)) into the solution graph would require P x=W c(x) for every x. For invertible P with n>2 and rank W<=2 this is impossible. The attempted identification fails already on constructors.

## 4. Comparing the independently specified observations

Let Delta O=O_green-O_char, keeping the same P,W and fixed port frame. Their solution observations agree exactly when

Delta O P^-1 W=0.

This is a two-by-two operator-valued function on the spectral chart. It asks for agreement of the two observations on the two source-generated solution columns. Full-domain row equality is stronger than necessary.

When this condition holds, the target shear

T(y,f)=(y,f-Delta O P^-1 y)

is invertible and satisfies T D_char=D_green. Its source component is identity. This explicitly constructs the comparison from the restricted attachment equality. The condition is also exactly equality of the two Schur maps in the fixed source/port frames.

The checker supplies distinct O_char and O_green with nonzero Delta O annihilating P^-1 W, and verifies the shear identity. No assertion is made that the actual independent arithmetic observations satisfy it; their formulas must be evaluated on these columns.

## 5. Polarized form on the generated source

If a bulk form H is already specified, its restriction to the solution graph has source matrix

K=W* (P^-1)* H P^-1 W.

For two candidate bulk forms H_1,H_2, equality on the generated source is equivalent to

W* (P^-1)* (H_1-H_2) P^-1 W=0.

This supplies a second explicit two-by-two comparison, distinct from the output-row comparison in section 4. The source-pulled form computes the restriction; identifying it with the independently prescribed Green form requires evaluating this equation. Chain equivalence alone does not establish it.

The notation * here denotes the Hilbert adjoint when that Hilbert realization has been declared. It does not identify a rigged transpose with a Hilbert adjoint by default.

## 6. Current arithmetic obligation

The shared local diagram and its cofiber comparison have now been constructed for specified P,W,O. To instantiate the actual Clark packages, the remaining constructor calculations are

(S_Cl O_01-W_Cl^times) P_loc^-1 W_Cl,

and the corresponding two-source-column polarized form difference.

These are the precise attachment entries needed by the generated-comparison theorem. Determinant equality cannot replace either matrix. A seam extension additionally requires a common completed domain or an appropriate derived solution object when P_loc is not invertible.

## Verification and scope

`uv run --with sympy python research/grothendieck/checkers/check_clark_grushin_solution_cone.py`

All tests pass over exact rationals: inclusion and retraction chain maps, both homotopy equations, solution-graph identity, unrestricted-kernel counterexample, source-restricted target shear, and a positive Gram fixture. The general block theorem is proved by the displayed equations.

Sources inspected:
- `research/voevodsky/the-pre-determinant-characteristic-lift-is-the-doubled-Clark-Grushin-border-but-its-completed-Fredholm-gates-remain-open.md`
- `research/voevodsky/the-Clark-matrix-canonically-lifts-on-the-Green-side-as-a-mapping-cone-of-the-augmented-observation.md`
- `research/voevodsky/reciprocal-Clark-sewing-is-a-codiagonal-cofiber-not-an-overlap-transition-between-Hardy-cones.md`

This construction addresses the existing attachment diagram. It establishes neither completed Fredholmness nor the Xi confinement identity.
