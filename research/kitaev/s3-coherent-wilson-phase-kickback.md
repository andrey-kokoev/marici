# Four coherent Wilson spectral ports suffice for projector phases

Owner: `marici.Kitaev`

Ledger: Entries 2466--2467  
Graph: `ev-000000003376-ba3c1bc2-f8a7-4099-a76d-055425d917ff`,
`ev-000000003378-3447f8cd-0bf5-4a8c-a614-b50356bd1ebe`

## Bounded question

Can the four Wilson observables that jointly distinguish all eight torus
sectors compile the coherent projector phases needed for protected-control
completion, despite the eight-type lower bound for linear Hamiltonian
synthesis?

## Conditional construction

Choose any minimum faithful family, for example

\[
  (W_C,W_D,W_F,W_G).
\]

Its joint eigenvalue signature \(\sigma(a)\) is different for every sector
\(a\). Assume a coherent nondemolition spectral extractor

\[
  V_\sigma:|a\rangle|0\rangle\longmapsto
  |a\rangle|\sigma(a)\rangle.
\]

For the bus phase \(D_b(t)|\sigma(a)\rangle=
e^{it\delta_{ab}}|\sigma(a)\rangle\), compute--phase--uncompute gives

\[
  V_\sigma^\dagger(I\otimes D_b(t))V_\sigma=e^{itQ_b}.
\]

The exact checker constructs the isometry, verifies its Gram matrix, and
checks the compression symbolically for the completing targets \(A\) and
\(C\). The same construction works for every sector.

## Exact finite extractor from controlled loop evolutions

The oracle need not resolve arbitrary real spectra. Every eigenvalue in all
eight minimum faithful families is integral, and exhaustive reduction finds
that modulus four is minimal for each family. For the chosen family the eight
joint signatures remain distinct after componentwise reduction modulo four.

Consequently a four-level phase-estimation pointer for each \(W_x\), using

\[
  U_x=\exp(2\pi i W_x/4),
\]

extracts the residue exactly. A reversible lookup of the four residues applies
the selected sector phase, after which inverse phase estimation cleans every
pointer. Thus a concrete sufficient gate set is four controlled noncontractible
loop evolutions (and their powers), four coherent ququart pointers, reversible
classical logic, and inverse extraction.

## Strict resource hierarchy

There is no contradiction with the eight-type linear-synthesis lower bound:

\[
\begin{array}{ccl}
4\text{ measured Wilson observables} &\Rightarrow&
  \text{faithful classical label, but dephasing},\\
4\text{ coherent spectral ports} &\Rightarrow&
  \text{arbitrary diagonal sector phase},\\
8\text{ Wilson Hamiltonian types} &\Rightarrow&
  \text{the same phases by linear Hamiltonian synthesis}.
\end{array}
\]

The middle implication is nonlinear: the bus performs a lookup on the joint
signature. Measurement cannot substitute for it. The checker’s negative
control verifies that projective sector readout kills every off-diagonal
matrix unit, whereas phase kickback preserves coherence.

## Unresolved physical typing

The abstract \(V_\sigma\) has now been reduced to a finite exact circuit model,
but that model assumes controlled \(e^{2\pi iW_x/4}\). Abstract Wilson
operators, destructive measurement access, or uncontrolled Wilson evolution
do not provide those controlled noncontractible gates. A physical theorem must
implement them fault tolerantly, keep the topological data coherent, and
uncompute the pointers without residual syndrome.

The falsifier is direct: if two sectors share the selected four-observable
signature, the bus phase cannot isolate either one. Exhaustive enumeration
finds eight faithful four-type families and no faithful family of size three.

## Artifacts

- Checker: `checkers/check_s3_coherent_wilson_phase_kickback.py`
- Result: `results/s3-coherent-wilson-phase-kickback.json`
