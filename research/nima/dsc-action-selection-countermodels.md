# Does DSC force quadraticity or stationarity? Actual-core counterexamples

## Answer for the current core

No: the existing DSC semantic rules admit both the quadratic and quartic
models through the SAME dependent evaluation interface, and admit an execution
whose variational residual is nonzero. These are compiler-checked examples,
not merely an analogy with ordinary function composition.

This refutes automatic selection by the current core alone. It does not rule
out a stronger physical interface expressed using DSC. Admitting an object
into a type theory is not evidence that nature realizes it.

## Actual module and typed test

`agda/DSCActionCountermodels.agda` imports
`research/voevodsky/resolution-net-v1/agda/ResolutionNetDependentSubstitution.agda`
directly. No replacement DSC implementation was written, and the owner source
was not modified. The runner adds its source directory to Agda's include path.

The shared interface is:

    Model = quadratic | quartic
    Input(m) = point q + action value + proof of that evaluation
    Output(m,input) = derivative residual + proof of that evaluation.

This is a dependent family: changing the model or point changes the required
evaluation and residual equations. The real `Dependent.extend` and
`Dependent.execute` assemble and run it. The existing substitution law,
context-extension naturality, associativity and both unit laws are instantiated
on this interface.

The polynomials are the prior graph-action fixture, with q=2*phi_1:

    quadratic: 8*S = 4*q^2 - 8*q,
    quartic: 32*S = 16*q^2 - 32*q + q^4.

Their scales are different and declared; neither vanishing of a derivative
nor the presence of a quartic term depends on a nonzero overall scale.

Agda checks:

- quadratic at q=1 executes with residual 0;
- quadratic at q=2 executes with residual 8;
- quartic at q=1 executes with residual 4;
- the quartic coefficient is 1, not 0.

It also proves explicit contradiction functions:

    (every environment executes with residual zero) -> Empty
    (every admitted model has zero fourth coefficient) -> Empty.

The second statement tests a necessary condition for quadraticity, not a
universal classification of polynomials. The counterexample is an admitted
fourth-degree model. The first statement shows that successful substitution
and dependent execution do not themselves require a stationary point.

## Adding stationarity as a type does not derive it

The module also defines

    StationaryInput(m) = Sigma input. derivative(m,input.point)=0.

The quadratic q=1 case supplies a witness. The q=2 case cannot supply one.
DSC can therefore ENFORCE stationarity when it is put into the input contract,
but the ordinary execution rules did not select that contract or manufacture
the witness. This separates enforcement, witness construction and physical
selection.

These conclusions concern the existing semantic core (types/functions with
dependent application and transport), not a completeness or independence
theorem for a newly specified DSC object-language syntax. No result says that
all possible physical extensions of DSC must admit these alternatives.

## Stronger test: stationary composition still admits quartic actions

Even adding stationary elimination as an operation does not, by itself,
select quadraticity in the following source-free segment interface.
For positive length L and p=2 OR p=4, define

    S_p(L;x,z) = (z-x)^p / (p*L^(p-1)).

Composition joins two segments, adds their actions and eliminates the shared
point y by stationarity. The seam condition is

    ((y-x)/L1)^(p-1) = ((z-y)/L2)^(p-1).

Because p-1 is odd, the real power is injective. The unique stationary point
is

    y = (L2*x + L1*z)/(L1+L2).

Writing v=(z-x)/(L1+L2), the two increments are L1*v and L2*v. Substitution
then gives the exact identity

    stat_y [S_p(L1;x,y)+S_p(L2;y,z)] = S_p(L1+L2;x,z).

Both families are closed under this composition. Length addition also makes
successive elimination associative. For p=4 the reduced action remains
quartic, not quadratic. Both families are invariant under joint endpoint
translation and endpoint exchange. Thus the very same stationary-composition
interface permits distinct homogeneities.

This is a mathematical proof for positive real lengths and these two powers.
The accompanying Python check verifies the seam residual and reduced action
as exact endpoint polynomials for four rational length pairs and three
length triples per degree. It also rejects the nonstationary choice y=x and
the attempt to classify the quartic family as degree-two homogeneous.
These stronger composition results are NOT yet Agda theorems.

### Limits of this stronger test

- The segment model is source-free, unlike the earlier loaded three-vertex
  graph. Arbitrary interior source couplings have not been tested for closure
  in this finite-parameter family.
- Only positive lengths are used. No zero-length energy/unit or full category
  of action kernels is asserted. The DSC function units above are a separate
  checked statement.
- Stationarity is explicitly SUPPLIED as the elimination operation in this
  test. Its successful composition does not derive a physical stationarity
  principle.
- These are mathematical segment costs. Their lengths are not identified with
  physical time or space, and no unit of physical action is derived.

Requiring arbitrary sourced closure, a particular refinement law, physical
units or another interface could distinguish families. Such a requirement
must be independently motivated, not chosen solely to exclude the quartic
counterexample.

## Reproduction and evidence

```powershell
pwsh -NoProfile -File research/nima/checkers/check_dsc_action.ps1
```

The shell runner runs the exact computational audit and freshly compiles the
actual-core Agda example with interfaces ignored. Fresh compilation passed.
Two negative controls fail for the intended type mismatches (exit 42):

- forced stationarity: `8 != 0`;
- forced quadraticity: `1 != 0`.

Files and receipts:

- `agda/DSCActionCountermodels.agda`
- `checkers/check_dsc_action_countermodels.py`
- `results/agda-DSCActionCountermodels.json`
- `results/dsc-action-countermodels.json`
- `results/dsc-action-formal-audit.json`

The computational checker reuses the prior exact polynomial backend; these
are not independent arithmetic-backend validations. Selected source hashes
include the actual DSC source; the fresh compiler log records the checked
import closure. No universal physical inference or new task ownership is
claimed from successful compilation.

## Disposition

The literal conjecture that quadraticity and stationarity follow from current
DSC alone fails this test. DSC remains a language in which additional physical
requirements can be stated and their consequences checked. The next question
is which independently motivated requirement excludes the surviving nonlinear
models, rather than whether dependent substitution already does so.
