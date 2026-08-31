# Localized-quartet flag-refinement no-go: WP1084

## Question

Does the localized \(SU(4)\times SU(2)\) cell refine either WP1080 \(SU(3)\)
triplet to a simple-spectrum ordered flag?

## Common-subgroup branching

Align WP1056's localized \(SU(4)\times SU(2)\) decomposition with WP1080's
\(SU(3)_A\times SU(3)_B\) carrier through

\[
SU(3)_A\times SU(2)_B\times U(1).
\]

The fundamental branches as

\[
6=(3_A,1_B)+(1_A,2_B)+(1_A,1_B).
\]

The localized quartet is the full \(A\)-triplet plus the \(B\)-singlet; the
remaining \(B\)-doublet is the \(SU(2)\) factor.

## Flag spectrum

On the \(A\)-triplet, the common subgroup leaves an irreducible \(3\). A
natural endomorphism is scalar, with one distinct eigenvalue.

On the \(B\)-triplet, localization gives only

\[
3_B=2_B+1_B.
\]

A natural endomorphism has at most two distinct eigenvalues:

\[
A_B=\operatorname{diag}(a,a,b).
\]

For every \(x\), its Krylov history has rank at most two. The checker uses
\(a=2\), \(b=5\), \(x=(1,2,3)\) and verifies

\[
\det[x,A_Bx,A_B^2x]=0.
\]

## Classification

Localized-quartet flag no-go. The existing localization gives an unbroken
\(A\)-triplet and only a \(2+1\) flag on the \(B\)-triplet. Neither supplies a
simple-spectrum evolution, a full ordered three-line eigenflag, or a canonical
cyclic ray.

The remaining successor gate is a source-derived second-stage breaking of the
\(SU(2)\) doublet into two ordered lines, or a different localization
producing a \(1+1+1\) flag, together with cyclic-ray preparation and history
dilation.

Checker: `research/flavor/checkers/wp1084_localized_quartet_flag_refinement_no_go.py`

Result: `results/wp1084_localized_quartet_flag_refinement_no_go.json`
