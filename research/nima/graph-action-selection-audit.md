# From retained graph data to an action: first selection audit

Successor: [actual DSC counterexamples](dsc-action-selection-countermodels.md)
shows that the current dependent-substitution core admits both action models
and a nonstationary execution. Even a source-free stationary segment-composition
test retains a quartic alternative.

## Outcome

We can assemble a static graph-field functional, obtain its graph Poisson
stationarity equation, and retain the comparison in the existing RRC.
However, locality, additive composition, edge symmetry and constant-field
shift covariance do NOT select the quadratic action: a quartic alternative
passes those requirements too. Quadraticity is a genuinely additional input.
No gravitational dynamics has been derived from RRC by this experiment.

This is an action FUNCTIONAL experiment, not the periodic Hamiltonian action
variable integral p dq. There is no physical time or unit of action attached
to the graph. For now S is a dimensionless static functional; multiplying it
by a nonzero overall scale leaves its stationary points unchanged.

## Frozen inputs and calculation

Use a three-vertex path 0--1--2 with edge weights 1 and 3 and source
j=(0,2,0). These graph, weight and source choices are supplied, not generated
by RRC. For the quadratic candidate,

    S(phi) = 1/2 sum_edges w_ij (phi_i-phi_j)^2 - sum_i j_i phi_i.

Exact polynomial differentiation gives

    dS/dphi = L phi - j,
    L = [[1,-1,0],[-1,4,-3],[0,-3,3]].

Impose Dirichlet values phi_0=phi_2=0 and vary ONLY phi_1. Stationarity then
gives 4 phi_1=2, so phi_1=1/2. The boundary residuals need not vanish.
With all three vertices free, there is no stationary point for this source:
summing the three equations gives 0=sum j=2. The checker explicitly detects
that obstruction rather than hiding it by pinning a gauge in an incompatible
closed problem.

Stationarity is a supplied dynamical/variational principle here. Neither RRC
composition nor the existence of S implies that physical configurations must
be stationary.

## Alternatives that discriminate the assumptions

Compare:

    screened: S + (mu^2/2) sum_i phi_i^2, with mu^2=2;
    quartic:  S + (1/4) sum_edges (phi_i-phi_j)^4.

| Requirement | Quadratic | Screened | Quartic |
|---|---|---|---|
| Local vertex/edge contributions | yes | yes | yes |
| Additive assembly and order independence | yes | yes | yes |
| Edge orientation reversal | yes | yes | yes |
| Bulk constant-shift covariance | yes | no | yes |
| Source-free degree-two homogeneity | yes | yes | no |

With a source, the correct shift identity is

    S(phi+c*1)=S(phi)-c*sum_i j_i,

not strict invariance. The identity is tested before fixing boundaries;
a constant shift is not an allowed variation of fixed Dirichlet values
unless those boundary values are shifted too. The screened term violates
this identity by additional field-dependent terms. Quartic differences do
not. Thus shift covariance distinguishes screening but leaves nonlinearity.

For the Dirichlet example, the screened solution is phi_1=1/3 rather than
1/2. The quartic equation is

    4 phi_1 + 2 phi_1^3 = 2,

so phi_1=1/2 is not stationary (residual 1/4). These are explicit alternatives
with different predictions, not just different labels on the same action.

## What DOES select the quadratic edge form?

Take an arbitrary edge polynomial of total degree at most two,

    E(u,v)=a*u^2+b*u*v+c*v^2+d*u+e*v+f.

Joint constant-shift invariance implies b=-2a, c=a and e=-d. Exchange symmetry
E(u,v)=E(v,u) then gives d=e=0. Normalization E(u,u)=0 removes f. Consequently

    E(u,v)=a*(u-v)^2.

Positivity, if required, gives a>=0, but neither this argument nor RRC fixes
the weights a. Degree-two homogeneity is one way of supplying the polynomial
restriction; linear response is another related condition in this model.
The quartic counterexample shows that the restriction cannot be inferred from
the other listed requirements. Positivity alone also does not exclude quartic
edge energies. The source coupling remains separately specified as linear.

The coefficient classification is a written algebraic argument, with an exact
symbolic check of the resulting family. It is NOT a machine-checked universal
classification of all local actions, nonpolynomial functionals, or RRC rules.

## RRC and formal scope

`agda/GraphAction.agda` implements integer formal polynomial addition,
multiplication and differentiation. Its generic `pAdd-comm` proves composition
order independence for coefficient-list addition. Fixed calculations prove
edge reversal, the action derivative/incidence comparison, and the two
alternative nonzero residuals.

For exact integer encoding, q=2*phi_1:

    8*S_quadratic = 4*q^2-8*q,
    derivative = 8*q-8 = 2*(L*q-2*j)_1.

The screened candidate has 8*S_screened=6*q^2-8*q. The quartic comparison uses
32*S_quartic=16*q^2-32*q+q^4. Both have nonzero derivative 4 at q=1 in their
respective scaled encodings. No integer division or false scaling equivalence
is used.

The three energy/source polynomials are actual RRC complete packages.
`Pi-rule` retains their complete family; `actionOfHistory` reads this typed
retained endpoint and assembles S. `retained-action` checks the result.
`compare-rule` retains the proved equality between the differentiated action
and twice the independent incidence residual. The combined history is reified
with checked recovery, retaining the action and coordinate scale factors.

This is a bounded action readout for ONE typed family, not a canonical action
on all RRC derivations. Different derivation histories may have the same
readout. RRC does not construct stationarity, locality, quadraticity or a
physical interpretation merely by retaining these proofs. No formal theorem
connects arbitrary polynomial lists to real differentiation; the finite
coefficient identities themselves are compiler-checked.

## Gravity boundary and sign convention

The positive graph Laplacian L corresponds, under a suitable spatial
refinement, to MINUS the Euclidean Laplacian. Therefore L*phi=j is not yet
Delta Phi=4*pi*G*rho with j identified with positive mass density. That
identification would require the appropriate sign, cell-volume weights and
normalization (schematically j=-4*pi*G*rho). Our positive source j=2 is an
abstract graph load, NOT a positive gravitational mass claim.

Recovering Newtonian gravity still needs justified geometry/weights, an
appropriate continuum limit, physical units and coupling, boundary data and
the acceleration readout. No claim is made that any of these follows from
the three-vertex calculation.

## Verification and reproduction

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graph_action.ps1
```

`checkers/check_graph_action_selection.py` uses exact multivariate Fraction
polynomials to check the full three-vertex gradient, Hessian, symbolic shift
and dilation identities, alternative solutions, the closed-source obstruction,
and double-counted-edge/missing-mixed-term hostiles. No floating-point optimizer
is used. Composition counts each supplied contribution: repeating an edge
changes the action, and must not be silently quotiented away.

The fresh Agda closure check passed. Compiler rejection controls fail with
the intended `[UnequalTerms]` errors: screened stationarity `4 != 0`, and
incorrect derivative coefficient `2 != 1` (both exit 42).

Receipts:

- `results/graph-action-selection.json`
- `results/agda-GraphAction.json`
- `results/graph-action-formal-audit.json`

## Next discriminating question

Can an independently motivated source/composition/refinement condition force
quadratic response, or only make it a leading small-field approximation?
The current result does not supply that condition. Merely asserting a linear
response because Poisson is desired would reintroduce the target assumption.
