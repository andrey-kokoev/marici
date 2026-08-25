# Direct native-ququart Wilson compiler

Owner: `marici.Kitaev`

## Bounded question

Can the coherent Wilson extractor be compiled directly in the native ququart
pointer lens without importing the binary \(217T\) circuit?

## Direct interaction

For pointer value \(r\in\mathbf Z_4\) and Wilson residue
\(w_x(a)\in\mathbf Z_4\), extraction applies

\[
i^{r w_x(a)}.
\]

Expand the normalized residue function in Boolean monomials of the three
sector-label bits. Each predicate controls \(Z_4^c\) on the pointer. Exact
mixed qubit--ququart Pauli-normalizer tests show

\[
c=2:\text{ Clifford},
\qquad c=1,3:\text{ non-Clifford}.
\]

Inverse extraction uses the inverse coefficient. Native \(F_4\) contributes
no magic invocation. Shared nonlinear data predicates retain the four-episode
ideal conjunction compiler.

CDFG uses 26 odd non-Clifford and 16 even Clifford hybrid phase invocations
over the full extraction/unextraction cycle. It minimizes the odd count, but
the exact three-coordinate Pareto frontier is

\[
CDFG=(26,16,4),\quad
CDFH=(28,14,4),\quad
CDGH=(30,12,4).
\]

Thus the native lens does not select one family until relative hybrid magic
and Clifford costs are declared. If non-Clifford count is lexicographically
primary, CDFG is selected.

## Claim boundary

This is a native-lens primitive census. It does not assign binary \(T\)-state
costs to the odd hybrid phase species and does not prove that species has a
verified factory. Shared-predicate fault propagation and microscopic exRecs
remain unresolved.

## Falsifiers

- Failure of any Boolean residue reconstruction modulo four.
- A different mixed-Pauli Clifford classification for \(c=1,2,3\).
- A family Pareto calculation omitting inverse extraction.
- A source-derived conversion giving a different hybrid primitive cost.

## Artifacts

- Checker: `checkers/check_s3_native_ququart_wilson_compiler.py`
- Result: `results/s3-native-ququart-wilson-compiler.json`
- Result SHA256:
  `7C526C0638D17298C038DF914ADBC84662D03683C6E0962BED470836B3F9AF29`
- Graph admission: `ev-000000003472-4abf67c2-27df-4786-ae22-4567286e3601`
- Ledger: entry 2511, `seqclaim-cdf18033dfe56a461261bedb`
