# The eighth direction exists as a lax completion prism

## Construction attempted

Let

\[
\mathcal Q_X:\{0,1\}^7\to\mathbf{Carrier}
\]

be the finite-regulator seven-axis diagram on `(H,V,D,q,L,C,O)`, and let

\[
\widehat{\mathcal Q}:\{0,1\}^7\to\mathbf{Carrier}
\]

be its proposed completed diagram. The eighth direction is a natural or lax-natural comparison

\[
\kappa:\mathcal Q_X\Longrightarrow\widehat{\mathcal Q}.
\]

It has 128 components

\[
\kappa_v:\mathcal Q_X(v)\to\widehat{\mathcal Q}(v)
\]

and 448 naturality squares: 64 for each of the seven old directions.

The machine-readable registry is `results/vertexwise-eighth-completion-prism.json`.

## Generic face audit

The 448 squares reduce to seven uniform schemas.

| Face | Status | Content |
|---|---|---|
| `R x D` | constructed | star/dagger extends on declared graph completions |
| `R x q` | lax | Fourier-cutoff leakage is the comparison 2-cell |
| `R x L` | constructed on joint graph | closed Mellin multipliers extend as graph coordinates |
| `R x O` | constructed on joint graph | retained closed observation extends and preserves endpoint multiplier naturality |
| `R x H` | constructed | projective exponential seminorms make every finite rooted convolution jointly continuous |
| `R x V` | constructed | cut maps are bounded finite sums of Laurent translations on the localized projective carrier |
| `R x C` | constructed forward | continuous rigged synthesis extends uniquely to retained graph completion; its inverse remains forbidden |

This gives 384 constructed and 64 coherently lax square instances, with no unclassified generic face. Full closure still requires incidence of the arithmetic synthesis into the retained `L/O` joint graph.

## The decisive correction

The eighth object is not presently a strict Boolean cube. The `R x q` face cannot be declared commuting at finite cutoff. Its defect is

\[
\mathfrak A_X=P_X\mathcal F(I-P_X).
\]

A finite witness proves this residual can be nonzero. Under nested cutoffs it obeys the shell cocycle

\[
\mathfrak A_X
=P_X\mathcal F(P_Y-P_X)+P_X\mathcal F(I-P_Y).
\]

Hence the correct eighth-dimensional structure retains `A_X` as a coherent lax 2-cell. Erasing it falsely asserts a finite completed-source intertwiner.

The common Mellin/de Rham graph norm supplies the positive completion mechanism:

\[
\|f\|_{QD}^2=\|f\|_2^2+\|Qf\|_2^2+\|Df\|_2^2,
\]

with the two leakage estimates controlled at order `R^{-1}`. This remains conditional on arithmetic incidence landing continuously in that common graph domain.

## Verdict

Regulator/completion passes the independence and local vertexwise-typing tests. It has six constructed forward/exact generic faces and one constructed lax face. Therefore:

\[
\boxed{R\text{ is a viable eighth directed axis in a lax cubical category}.}
\]

It is not yet a completed strict 8-cube or an 8-simplex coherence theorem.

The shortest route forward is not 128 separate proofs. The `H` family is now closed by the rooted-convolution seminorm theorem. The `V` family is closed after passing to the minimal cut-stable projective Laurent localization. The directed `C` family is also closed because the continuous forward rigged synthesis extends uniquely to the retained graph completion; this does not produce a bounded inverse. The analytic `L/O` common domain is now the closure of the combined multiplier-observation graph. What remains is the cross-axis incidence theorem that the arithmetic synthesis lands continuously in this domain for the required observer family. The `q` family should remain lax and satisfy the shell-cocycle coherence law.
