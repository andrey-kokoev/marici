# The positive regulator cone does not select the C8 rank-four circuit chamber

## Frozen source prescription

The published boundary value assigns

\[
X_i\mapsto X_i-i\epsilon_{X_i},
\qquad
y_e\mapsto y_e-i\epsilon_{y_e},
\qquad
\epsilon_{X_i},\epsilon_{y_e}>0.
\]

It fixes common negativity, not equality of regulator magnitudes. No hierarchy is added.

## Labelled rank-four arrangements

Each of the 36 cyclic orbit representatives (288 labelled occurrences) contains seven labelled partial-energy forms but has rank four in the eight internal-edge variables. After source-base reduction there are four edge-elimination patterns.

### Correction: relation bases are not circuit sets

The first audit selected a three-vector nullspace basis for one representative of each edge-elimination pattern. Such a basis is not invariant under a change of labelled presentation and is not the set of matroid circuits. That "twelve circuits / four chambers" description is retracted.

Enumerating every support-minimal dependence gives the invariant census

\[
\begin{array}{c|ccccc}
\text{minimal circuits per orbit}&3&4&6&8&9\\
\text{orbit count}&4&12&16&2&2.
\end{array}
\]

Every orbit is free of size eight, producing 288 distinct labelled occurrences. Transport around each orbit preserves its circuit arrangement and chamber count.

For a circuit \(c\) among the seven \(y\)-normals,

\[
c^TN_y=0,
\]

while the corresponding displacement of the coincident labelled poles is

\[
\operatorname{Im}(c^Tq)
=-c^TN_X\epsilon_X.
\]

## Exact chamber test

Among the 190 minimal circuits on the 36 orbit representatives, 130 vectors \(c^TN_X\) contain both positive and negative coefficients. The remaining 60 have fixed sign. Thus some individual circuit orientations are source-selected, but the complete joint chamber never is.

The machine packet supplies, for every circuit, two explicit positive integer vectors \(\epsilon_X^+,\epsilon_X^-\) satisfying

\[
(c^TN_X)\epsilon_X^+>0,
\qquad
(c^TN_X)\epsilon_X^-<0.
\]

The labelled-occurrence census is

\[
1520\text{ minimal circuits},\qquad
1040\text{ mixed},\qquad
480\text{ fixed}.
\]

Exact linear-real satisfiability over the normalized positive cone

\[
\epsilon_{X_i}>0,
\qquad
\sum_i\epsilon_{X_i}=1
\]

gives the orbit-sensitive chamber census

\[
\begin{array}{c|rrrr}
\text{joint chambers per orbit}&4&5&6&8\\
\text{orbit count}&20&2&10&4.
\end{array}
\]

Equivalently, the 288 labelled occurrences split as \(160,16,80,32\) occurrences with \(4,5,6,8\) feasible chambers. Thus the ambiguity is finite, but it is not a uniform four-chamber object.

## Narrow conclusion

\[
\boxed{
\text{The published positive regulator cone does not select a unique labelled circuit chamber at any C8 rank-four pattern.}
}
\]

Therefore Entry 1918's rank-one complex fold coefficient cannot yet be promoted to an occurrence-resolved physical pairing. A chamber-independent sewn combination could still exist; that must be derived across the full source sum rather than assumed term by term.

No new carrier stratum is implicated. The missing datum is relative-chain/regulator coherence over an already frozen non-simple incidence center.

## Artifact

- `checkers/eight_site_rank4_regulator_normals.py`
- `results/eight-site-rank4-regulator-normals.json`
- `checkers/eight_site_rank4_labelled_expansion.py`
- `results/eight-site-rank4-labelled-expansion.json`
