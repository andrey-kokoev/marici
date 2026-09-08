# Coefficient interface v7: secondary cochain compatibility

## Checked increment

`rzk/12-relative-cochain-secondary.rzk.md` adds eight definitions to the
13-definition v6 dependency. It works in the degree window needed for the
secondary test, with explicit additive/subtractive laws and differential
compatibility witnesses; it adds no global axioms.

The relative differential on primitives is

\[
D(t,k)=(d_Mt,r(t)-d_Nk).
\]

For a supplied ambient primitive d_M s=f, the module constructs witnesses
in both directions between

\[
\exists(t,k):\quad d_Mt=f,\quad r(t)-d_Nk=h
\]

and

\[
\exists(z,k):\quad d_Mz=0,\quad h-r(s)=r(z)-d_Nk.
\]

These existential displays abbreviate the implemented dependent pairs; no
propositional truncation or homology quotient is implemented. Forward uses
t=s+z; reverse uses z=t-s. The theorems preserve higher boundary correction k
and allow every replacement ambient primitive. They prove existence in both
directions, not uniqueness or equivalence of the full witness spaces.

The module also proves the residual is closed when r(f)=d_Nh and restriction
commutes with differential. It proves the boundary component of D-squared is
zero; the ambient component is the supplied d_M-squared law. The adapter is a
degree window, not an implementation of unbounded complexes or RHom.

## Verification and controls

Command:

`pwsh -NoProfile -File research/nima/rzk/check-boundary-framed.ps1 -Module 12-relative-cochain-secondary`

Fresh headless check passed, exit 0, `Everything is ok!`: 13 prior plus eight
new definitions. The two-file closure and source/executable digests are in
`results/12-relative-cochain-secondary.typecheck.json`; execution reference
`structured_command_execution:e_39824_1788729105093936900_9`.
The persistent LSP attempt timed out; no successful LSP diagnostic is claimed.
The runner now accepts either module name and writes a module-named result.
The historical v6 result remains intact.

`checkers/check_relative_cochain_secondary.py` independently tests an integer
cochain model with d_M(a,b)=a, r(a,b)=2a+6b and d_N(k)=4k. Its secondary
quotient is Z/2, by parity and the all-integer identity 2m=6m-4m. The residual
2 requires both an ambient closed correction and a higher boundary correction;
omitting either incorrectly rejects it. The same ambient map with h=0 or h=1
also distinguishes framings. This Z/2 is a synthetic control, not physical
parity or an identification with the packet's marked-normal torsor.

The checker passed 7,416 assertions; results are in
`results/relative-cochain-secondary-control.json`. Execution reference:
`structured_command_execution:e_39824_1788729163544848300_10`.
This is not a formal Rzk integer instance.

## Remaining concrete adapter

To use this theorem for the spatial construction, instantiate its carriers
and algebra laws with admissible maps of the full support/coefficient diagram,
then provide the restriction squares, actual f and the independently derived
Q/endpoint homotopy h. Relate its dependent-pair witness to the selected
chain model and ultimately to the v6 mapping-space fibre. No equivalence
between chain equality and mapping-space homotopy is assumed here.

The target restriction E -> Q + V[1], the full-support fibre B, its concrete
222-to-208 contraction, and normalization/Rees secondary quotient calculations
have not yet been formalized by these eight definitions. The physical Gysin
identification remains external work; its outcome has not been selected.
