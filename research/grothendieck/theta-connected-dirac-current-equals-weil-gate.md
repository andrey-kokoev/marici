# The correctly connected Dirac current is exactly the Weil gate

Author: marici.Grothendieck

## 1. Completed logarithmic current

Use the Euler-half-plane coordinate

\[
 s=\tfrac12+z,
 \qquad \operatorname{Re}z>\tfrac12.
\]

The completed logarithmic derivative splits exactly as

\[
 F(z)=F_{\mathrm{end}}(z)
     +F_\Gamma(z)
     +F_{\mathrm{prime}}(z),
\]

where

\[
 F_{\mathrm{end}}(z)
 =\frac1{z+1/2}+\frac1{z-1/2},
\]

\[
 F_\Gamma(z)
 =-\frac12\log\pi
  +\frac12\psi\!\left(\frac14+\frac z2\right),
\]

and

\[
 F_{\mathrm{prime}}(z)
 =-\sum_{N\ge2}
 \frac{\Lambda(N)}{\sqrt N}e^{-z\log N}.
\]

These are the endpoint, archimedean, and connected determinant-line currents.

## 2. Their common Green kernel

The reciprocal divided-difference kernel is

\[
 H_\Xi(z,w)
 =\frac{F(z)+\overline{F(w)}}{z+\bar w}.
\]

It splits formally into the same three currents only in the Euler chamber.
The prime summand is

\[
 H_{\mathrm{prime}}(z,w)
 =-\sum_{N\ge2}
 \frac{\Lambda(N)}{\sqrt N}
 \frac{e^{-z\log N}+e^{-\bar w\log N}}
      {z+\bar w}.
\]

After the quarter-turn between right-half-plane and upper-half-plane
coordinates, this is the same connected sine/divided-difference normalization
carried by the corrected reciprocal prime spinors.

Thus

\[
\boxed{
\text{endpoint flux}
+\text{gamma flux}
+\text{connected prime flux}
=H_\Xi.}
\]

The completed Dirac current is not a new positivity functional. It is a
boundary presentation of the canonical Xi Pick/Weil kernel.

## 3. Direct positive summation is impossible

For real \(z>1/2\), one prime-power contribution has diagonal value

\[
 H_N(z,z)
 =-\frac{\Lambda(N)}{\sqrt N}
   \frac{e^{-z\log N}}{z}<0.
\]

Therefore the connected prime spinor cannot be installed as an ordinary
positive orthogonal boundary port with the final orientation. Its formal
positive coefficient measure enters a negatively oriented Krein channel or a
cross term of a larger positive dilation.

The endpoint and prime pieces are also inseparable at \(z=1/2\): the endpoint
pole cancels the zeta logarithmic pole, while the separate prime Dirichlet
series does not continue there.

Hence

\[
\boxed{
\text{completed boundary}
\ne
\text{orthogonal sum of positive local sectors}.}
\]

## 4. Boundary-triple circularity gate

A scalar Weyl function of a positive Hilbert-space boundary triple is
Nevanlinna. Conversely, a meromorphic Nevanlinna function has a positive
Weyl realization.

For the completed source,

\[
 F\text{ is Nevanlinna}
\quad\Longleftrightarrow\quad
H_\Xi\ge0
\quad\Longleftrightarrow\quad
\mathrm{RH},
\]

subject to the fixed coordinate convention and standard analytic hypotheses.

Therefore constructing a boundary triple by declaring \(F\) to be its Weyl
function does not explain RH. It is an inverse realization of the desired
sign. Likewise, assembling the three exact currents and then asserting that
their sum is positive merely restates the Weil criterion.

## 5. What the Dirac construction has genuinely gained

The preceding reductions still establish nontrivial provenance:

1. the quadratic quotient coordinate comes from the minimal Euler operator;
2. reciprocal doubling is forced by its Clifford linearization;
3. the aggregate integer packet must pass through a determinant-line
   logarithm before polarization;
4. that logarithm forces prime-power support and von Mangoldt weights; and
5. endpoint, gamma, and prime currents must be sewn before continuation.

These facts determine the type and ordering of any valid proof. They do not
determine the final sign.

## 6. Surviving explanatory target

The only noncircular operator route is a **direct positive dilation**:
construct a larger source Hilbert space \(\mathcal H_{\mathrm{big}}\), a
positive self-adjoint bulk operator \(\mathbb H\), and a boundary compression
whose Schur/Weyl current is \(F\).

The positivity and self-adjointness of \(\mathbb H\) must follow from local
source operations before computing the scalar Schur complement. The
negatively oriented prime current must arise from elimination of positive
auxiliary degrees of freedom or from a relative boundary subtraction.

Schematically,

\[
\boxed{
\text{positive adelic dilation}
\to
\text{relative Schur boundary}
\to
H_\Xi.}
\]

If the large operator is defined using \(F\), \(\xi\), or the zero divisor,
the construction is circular.

## 7. Sharp next falsifier

On compactly supported logarithmic tests, seek a source-derived block form

\[
 \mathcal Q_{\mathrm{big}}
 =
 \begin{pmatrix}
 Q_{\Gamma+\mathrm{end}}&C\\
 C^*&Q_{\mathrm{aux}}
 \end{pmatrix}
 \ge0
\]

whose Schur complement is the completed Weil form.

The proposal fails immediately if:

1. \(Q_{\mathrm{aux}}\) or \(C\) is fitted from \(H_\Xi\);
2. the prime diagonal sign cannot be produced by Schur elimination;
3. endpoint-pole cancellation fails on the common domain; or
4. the large form is itself positive exactly when the Weil form is positive.

The last condition distinguishes an explanation from a larger restatement.

## 8. Scope

The completed logarithmic split, exact kernel identity, negative prime
diagonal, and endpoint-prime inseparability are exact in their stated domain.
The equivalence with the Weil/Pick positivity gate is established. No direct
positive dilation, self-adjoint completed boundary, Schur factorization, or
RH proof is claimed.
