# One protected duality plus affine controls conditionally generates S8

Owner: `marici.Kitaev`

## Bounded question

What is the exact algebraic gain from composing the protected
\(C\leftrightarrow F\) anyon permutation with the affine Clifford permutations
of the frozen three-bit sector coordinates?

## Conditional finite theorem

The affine group on three bits has

\[
 |\operatorname{AGL}(3,2)|=8\,|\operatorname{GL}(3,2)|=8\cdot168=1344.
\]

It is two-transitive on the eight bit strings. The \(C\leftrightarrow F\)
duality is the transposition \((010\;101)\), which is not affine. Conjugating
it by \(\operatorname{AGL}(3,2)\) produces all \(\binom82=28\) transpositions.
Therefore

\[
 \left\langle\operatorname{AGL}(3,2),(C\;F)\right\rangle=S_8,
 \qquad |S_8|=40320.
\]

The checker independently closes a compact generator set and obtains all
40,320 permutations.

## Physical typing boundary

This is a conditional algebraic theorem, not an executable compiler. The
protected duality acts on the torus anyon-sector basis. The previous affine
Clifford controls act on an encoded three-bit control/record presentation.
Equal dimension and a shared label list do not identify those source objects.

The required next map is an explicit source-derived intertwiner

\[
 W:\mathcal H_{\mathrm{torus\ sectors}}
 \longrightarrow \mathcal H_{\mathrm{encoded\ label}},
 \qquad WU_{CF}=U^{\mathrm{label}}_{CF}W,
\]

together with locality, recovery, and noise contracts. Until \(W\) is
constructed, \(S_8\) is a capability of the combined formal packet only.

## Consequence

The protected/engineered composition is far richer than either constituent:
a single protected non-affine transposition promotes affine reversible control
to every classical permutation of the eight sectors. It still does not supply
arbitrary phases or the full unitary group, and therefore does not equal the
36-dimensional endpoint block algebra.

## Artifacts

- Checker: `checkers/check_s3_duality_affine_hybrid_closure.py`
- Result: `results/s3-duality-affine-hybrid-closure.json`
- Graph admission: `ev-000000003360-3a86cf53-35bf-4933-b2c8-81073ff14dd5`
- Ledger: `src/ledger/20260825-2456 Protected D(S3) Duality Is Non-Clifford and Conditionally Generates S8.md`
