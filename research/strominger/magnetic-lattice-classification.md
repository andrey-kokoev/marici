# The magnetic kernel is a sparse exponent-lattice boundary problem

Companion to `checkers/magnetic_lattice_classification_checks.py` (9/9
aggregate gates, exit 0) and
`results/magnetic_lattice_classification.json`. In accordance with the
objective, this packet uses no potentials, residues, logarithms, or physical
interpretation.

## 1. Exact lattice operator

Encode \(z^{-a}\bar z^m\) by the source vertex \((a,m)\). During the
unbarred fold, represent a cleared-denominator numerator monomial by
\((r,t)\leftrightarrow z^r\bar z^t\). Before the step of weight \(s\), the
denominator power is \(s-2\). Direct differentiation gives exactly two moves:

\[
(r,t)\longrightarrow(r-1,t)\quad[r],
\qquad
(r,t)\longrightarrow(r,t+1)\quad[r+s+2].
\]

After \(g\) steps, the numerator has vertices

\[
(r_j,t_j)=(-a-g+j,m+j),\qquad 0\le j\le g,
\]

with integer coefficients

\[
C_j=\binom gj(-1)^{g-j}(a)^{\overline{g-j}}
(4-a)^{\overline j}.
\]

This follows combinatorially: each ordering of \(g-j\) horizontal moves and
\(j\) vertical moves has the same product, and there are \(\binom gj\)
orderings. The checker compares the recurrence and closed formula in 209
\((g,a)\) cases.

Clearing one further denominator, a numerator vertex \((r,t)\) contributes to
the magnetic column by

\[
\begin{array}{c|c}
\text{target}&\text{coefficient}\\ \hline
(r,t-1)&t\\
(r+1,t)&t-g\\
(t-1,r)&-t\\
(t,r+1)&-(t-g).
\end{array}
\]

Adjacent fold vertices collide because \((r_j+1,t_j)=(r_{j+1},t_{j+1}-1)\).
Thus each source column is a finite weighted path, antisymmetrized by swapping
its target exponents. This is the promised sparse integer boundary matrix.

## 2. Components are reflected diagonal pairs

Every unswapped target in the column of \((a,m)\) has exponent difference

\[
r-t=1-g-(a+m).
\]

Swapping reverses its sign. Hence the exact component label is

\[
q=|a+m-(1-g)|.
\]

The source graph decomposes into pairs of diagonals reflected about
\(a+m=1-g\). There are no edges between distinct \(q\)-components.

At \(q=0\), every target is fixed by the swap, so antisymmetrization kills
the whole column. Therefore, for arbitrary integer grade and admitted pole
depth,

\[
\boxed{m=-(g+a-1)\quad\Longrightarrow\quad M_g(a,m)=0.}
\]

The tower diagonal is forced purely by the lattice action, not inferred from
a rank census.

## 3. Cutoffs

Let \(A_k=\{0,2,\ldots,2k\}\) and retain source exponents
\(m_{\min}\le m\le m_{\max}\), while retaining the full target lattice.
Every tower is visible exactly when

\[
m_{\min}\le-(g+a_{\max}-1).
\]

This lower bound is minimal. Upper visibility requires only
\(m_{\max}\ge1-g\), automatically satisfied by the nonnegative upper cutoffs
used here.

A source cutoff restricts the domain columns of a fixed linear map. It cannot
create a dependency: it can only hide a zero column or remove part of the
support of an existing collision vector. Consequently:

- interior classes are kernel vectors whose full support remains after both
  cutoffs move away;
- lower- or upper-boundary sensitivity means an existing class is absent
  because at least one support vertex is cut off;
- there are no truncation-created kernel artifacts unless the target lattice
  is also truncated, which this construction prohibits.

This principle and the explicit visibility rules pass 755 independently
varied cutoff cases.

## 4. The central conjecture is false

The predicted diagonal does not exhaust the sufficiently interior kernel.
There are two collision syzygies at grade 2 in the tested stable range:

\[
E_1=1-\bar z^{-2},
\]

supported in component \(q=1\), and

\[
\boxed{E_2=\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6},}
\]

supported in component \(q=7\). The second is the smallest new interior
counterexample requested by the falsifier:

\[
(g,k,m_{\min},m_{\max})=(2,3,-8,2).
\]

Its three support vertices are \((0,-8),(4,2),(6,0)\). Enlarging either
cutoff preserves the relation. It is therefore a true local collision, not a
boundary artifact. It first becomes admissible at \(k=3\) because pole depth
\(a=6\) is required.

## 5. Corrected bounded stable law

Exact componentwise nullspaces over the requested range

\[
2\le g\le20,\qquad0\le k\le10
\]

and wide automatically sufficient cutoffs contain only visible tower zero
columns and the two grade-2 collision vectors above. Thus, in this certified
finite range,

\[
\dim\ker M_g=|A_k|+\epsilon(g,k),
\]

where

\[
\epsilon(2,k)=1+\mathbf1_{k\ge3},
\qquad
\epsilon(g,k)=0\quad(g\ge3).
\]

This is a finite-cutoff combinatorial theorem, not an unbounded theorem in
\(g\) or \(k\). The move law, component decomposition, diagonal implication,
and cutoff monotonicity are algebraic for arbitrary integer parameters. The
claim that no further collision blocks occur beyond \(g=20,k=10\) remains a
conjecture; proving it requires a symbolic rank argument for the weighted path
polynomials.

## 6. Component classification

Within the certified range, components have three dispositions:

1. **Unmatched center vertices:** the \(q=0\) tower columns; each is zero.
2. **Injective path blocks:** every \(q>0\) component except the two named
   grade-2 blocks.
3. **Exceptional collision blocks:** \((g,q)=(2,1)\) has syzygy \(E_1\), and
   \((g,q)=(2,7)\) has syzygy \(E_2\) once its pole depths and cutoffs admit
   the full support.

No additional cycles or unmatched vertices appear in the checked component
matrices. Any future counterexample must therefore be reported by its first
noninjective \((g,q,A_k)\) path block.

## Verification

`uv run --with sympy python -u research/strominger/checkers/magnetic_lattice_classification_checks.py`
passes 9/9 aggregate gates. Coverage includes 209 stable \((g,k)\) pairs,
755 cutoff variants, 1,254 diagonal columns, 836 component probes, and 209
closed-form move comparisons. All matrices and coefficients are exact
integers; no symbolic integration occurs.
