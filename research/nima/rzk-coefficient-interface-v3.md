# Rzk coefficient interface v3: derived versus strict certificates

## Question and scope

Operator instruction: add a derived-equivalence proof route without weakening source-admissible filler requirements. This extends v1 and v2; it changes neither Fact_n nor the generic Rzk core. The records below are specification pseudocode, not checked Rzk terms.

Source packet: research/chatgpt/source-derived-branch-comparision/source_defined_branch_comparison.md. Its polynomial conductor-road comparison supplies the mathematical test case. Its complete geometric PC/Rees/Gysin identification remains unverified.

## Two certificate types

StrictHomotopyCertificate(context,f,g) contains a displayed homotopy with its exact boundary and all declared admissibility witnesses. A strict deformation-retraction certificate additionally types its section and homotopy and proves the required identities. For an A-linear strict certificate, an R-linear ambient homotopy is insufficient. v2's support, localization, multigrading, and symmetry requirements remain in force for prescribed fillers and higher comparisons.

DerivedEquivalenceCertificate(context,p) contains:
- an admissible chain map p with source/target, coefficient actions, grading, and source operation declared;
- the intended derived category and weak-equivalence class;
- a proof that p belongs to that class, for example an exact kernel sequence with an acyclic kernel, or an acyclic cone;
- admissibility and exactness evidence for the selected route in that category;
- source authority for using this derived equivalence in the physical interpretation, or an explicit missing comparison.

For a degreewise short exact sequence 0 -> K -> P -> C -> 0 of A-complexes, A-linear acyclicity of K certifies that p:P -> C is an equivalence in D(A). It does not assert an A-linear strict section or ambient deformation retraction on these representatives. A contraction of K is sufficient but not necessary: a valid acyclicity proof also suffices. The inverse in the localization need not be a strict chain map C -> P on the displayed representatives.

An underlying quasi-isomorphism is not by itself an equivalence in every filtered, supported, or equivariant category. State that category's equivalence criterion and verify it. Do not infer a filtered-equivalence theorem merely from ordinary acyclicity. Conversely, do not demand an extra strict ambient splitting when the selected derived criterion has already been proved.

## Source example and exact distinction

Let A=R[x,y]/(xy), N=R[x] plus R[y], J=xR[x] plus yR[y]. The source packet defines p:P_R -> C_R, with the full roads and endpoints retained, and

0 -> [J --id--> J] -> P_R --p--> C_R -> 0.

The two copies of J occur in homological degrees two and one. This is an A-linear exact sequence. Its identity kernel contraction is A-linear and yields the derived A-module equivalence. Road and endpoint maps remain unchanged.

The ambient constant inclusion j and positive-tail homotopy h satisfy dh+hd=1-jp as R-linear maps. They are not A-linear. On a sheet generator s=(1,0), h(s)=0, but h(x s)=x in the node relation while x h(s)=0. This must fail the strict A-linear certificate, without invalidating the derived certificate via the kernel.

Source naturality, action, and readout compatibility are additional evidence, not consequences of the two-copy kernel calculation alone. Our regression isolates the normalization block and does not independently reconstruct all roads, D3 actions, or physical connectors.

## Scope of the branch-collision regression

v1's pair (1,1), (1+x,1) remains a counterexample to injectivity of common conductor value on the kernel problem Q=[N -> R] in cohomological degrees zero and one. There is no preceding node-relation degree in that problem.

In the relative normalization problem [A -> N], A is in homological degree two and N in degree one as embedded in P_R. Both pairs are boundaries: nu(1) and nu(1+x). They do not become the primitive road-normalized unit. The primitive unit requires a sheet difference matching the road sum. A change of source operation must be recorded as a new problem, with its actual differential, probe, and readout; it is not a contradiction or a retroactive rewrite of the kernel calculation.

Thus the regression registry now distinguishes kernel_readout_collision from relative_quotient_branch_boundary. The first rejects a false equivalence; the second accepts a justified derived removal of those directions. Neither permits ignoring coefficient-base polynomials retained in R.

## Tests and disposition

Governing conjecture: separate certificate constructors reject an inadmissible strict homotopy while admitting a valid derived equivalence. Rivals: any integer or R-linear contraction certifies an A-linear strict equivalence; every derived equivalence must exhibit such a strict splitting; the old branch collision prohibits all branch reduction.

The standard-library checker verifies the normalization-block chain comparison and R-linear contraction on untruncated polynomial inputs, its identity kernel contraction and A-linearity on test inputs, and the explicit failure of ambient A-linearity. It also checks both old collision pairs are actual boundaries in the relative model. General kernel acyclicity follows from the identity differential, not from enumerating bounded polynomial degrees. The formulas nu(a)=a nu(1) and p(a s)=a(0)p(s) prove linearity coefficientwise; bounded samples are implementation regression tests, not a universal proof by sampling.

Checker: research/nima/checkers/check_rzk_coefficient_interface_v3.py. Results: research/nima/results/rzk_coefficient_interface_v3.json. Command: python research/nima/checkers/check_rzk_coefficient_interface_v3.py through structured-command. No new formal Rzk term is compiled; the test is not an implementation of a complete certificate validator. No generic core or other-owner files change. Git remains prohibited.
