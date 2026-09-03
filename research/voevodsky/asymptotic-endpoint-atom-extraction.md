# Asymptotic extraction of the endpoint atom

## Question

Can the endpoint range and Schur conditions be derived automatically from remainder Hankel positivity plus the completed-source decay, rather than proved independently at every finite rank?

## Claim boundary

An abstract Hamburger-moment theorem answers yes, provided the full normalized moment asymptotic is derived from the source. Remainder Hankel positivity and that source asymptotic remain unproved.

## Hypotheses

Let \((a_n)_{n\geq0}\) satisfy

\[
(a_{i+j})_{0\leq i,j<N}\geq0
\]

for every \(N\). The Hamburger theorem gives a positive representing measure \(\mu\) on \(\mathbb R\):

\[
a_n=\int y^n\,d\mu(y).
\]

Suppose that for some \(Y>0\) and \(c\geq0\),

\[
\frac{a_n}{Y^n}\longrightarrow c
\]

along the full sequence.

## Step 1: force compact support

The even subsequence is bounded:

\[
\frac{a_{2n}}{Y^{2n}}=O(1).
\]

If \(\mu\) assigned positive mass to \(|y|\geq Y+\varepsilon\), then

\[
\frac{a_{2n}}{Y^{2n}}
\geq
\mu(|y|\geq Y+\varepsilon)
\left(1+\frac{\varepsilon}{Y}\right)^{2n},
\]

which diverges. Hence

\[
\operatorname{supp}\mu\subseteq[-Y,Y].
\]

This also makes the representing measure determinate.

## Step 2: read the endpoint masses

On the compact support, dominated convergence gives

\[
\lim_{n\to\infty}
\frac{a_{2n}}{Y^{2n}}
=
\mu(\{Y\})+
\mu(\{-Y\}),
\]

while

\[
\lim_{n\to\infty}
\frac{a_{2n+1}}{Y^{2n+1}}
=
\mu(\{Y\})-
\mu(\{-Y\}).
\]

Both limits equal \(c\). Therefore

\[
\mu(\{Y\})=c,
\qquad
\mu(\{-Y\})=0.
\]

Thus

\[
\mu-c\delta_Y\geq0.
\]

Every endpoint-subtracted Hankel matrix is consequently positive.

## Gate compression

Assume the remainder sequence associated with the completed formula has:

1. all Hankel matrices positive;
2. a source-derived asymptotic
   \[
   a_n/Y^n\to c.
   \]

Then the representing measure automatically contains the required endpoint atom of mass exactly \(c\). Hence:

- endpoint-vector range inclusion follows;
- every finite-rank Schur inequality follows;
- compatibility across truncation is automatic;
- subtraction leaves a positive residual measure.

The endpoint Schur gate is therefore not independent. It is a consequence of remainder Hankel positivity plus the asymptotic boundary condition.

## Christoffel interpretation

For the rank-\(N\) moment matrix, let

\[
\lambda_N(Y)
=
\inf_{p(Y)=1,\ \deg p<N}
\int |p(y)|^2\,d\mu(y)
\]

be the Christoffel function. Where the inverse formulation is defined,

\[
\lambda_N(Y)
=
\frac1{v_N^*A_N^{-1}v_N}.
\]

The sequence decreases to the endpoint mass:

\[
\lambda_N(Y)\downarrow\mu(\{Y\})=c.
\]

Thus the finite Schur inequalities are truncations of one atom-mass identity.

## Hostile case

Even moments alone do not determine the endpoint sign. They recover only

\[
\mu(\{Y\})+
\mu(\{-Y\}).
\]

The odd subsequence is essential to exclude mass at \(-Y\). Any source argument producing only even asymptotics leaves a two-endpoint ambiguity.

## Source application

The reported source relation is that remainder localizer moments obey

\[
\frac{a_n}{Y^n}\to c
\]

when the completed function decays to zero. That implication must be rederived from the exact endpoint/gamma/prime formula with all coefficients and signs fixed. It cannot be replaced by numerical decay.

Once established, the programme compresses to two gates:

- prove every remainder Hankel cone positive;
- prove the completed-source decay producing the full moment asymptotic.

No separate pseudoinverse estimates are then needed.

## Verification

- `research/voevodsky/asymptotic-endpoint-atom-extraction-v1.json`
- `research/voevodsky/checkers/check_asymptotic_endpoint_atom_extraction.py`
- `research/voevodsky/results/asymptotic_endpoint_atom_extraction.json`
