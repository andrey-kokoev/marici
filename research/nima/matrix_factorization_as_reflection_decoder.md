# Matrix factorization as a reflection-depth error-correction decoder

## Source-derived differential

Benincasa's normalized odd maps form the exact matrix factorization

\[
(-6z)(-z/6)=z^2.
\]

On the doubled carrier \(A=\mathbb Q[z]/(z^2)\), use these maps alternately
between adjacent reflection depths. For the four-constructor tower, put

\[
C_n=A^{4^n},
\]

and let \(d_n:C_n\to C_{n-1}\) send every child word to its parent with
coefficient \(-6z\) or \(-z/6\), according to parity of \(n\). Since every
two-step composite contains \(z^2\),

\[
d_{n-1}d_n=0.
\]

This is the first source-derived differential coupling reflection depths.

## Exact homology

Over \(\mathbb Q\), multiplication by a nonzero multiple of \(z\) on
\(A\) has rank one. The parent-folding matrix is surjective, so

\[
\operatorname{rank}_{\mathbb Q}d_n=4^{n-1}.
\]

For every interior grade \(n\ge1\),

\[
\begin{aligned}
\dim H_n
&=\dim C_n-\operatorname{rank}d_n-operatorname{rank}d_{n+1}\\
&=2\cdot4^n-4^{n-1}-4^n\\
&=3\cdot4^{n-1}.
\end{aligned}
\]

At grade zero,

\[
\dim H_0=1.
\]

For a finite truncation ending at depth \(N\), the apparent top homology is

\[
\dim H_N^{\rm top}=2\cdot4^N-4^{N-1}=7\cdot4^{N-1}.
\]

After adding the next reflection layer, \(4^N\) of those directions become
boundaries, leaving the stable interior value

\[
7\cdot4^{N-1}-4^N=3\cdot4^{N-1}.
\]

## Error-correction interpretation

The matrix factorization acts as a genuine decoder:

- the missing-next-layer part of the finite frontier is corrected exactly;
- one linear combination per parent is absorbed by the incoming boundary;
- three sibling-difference directions per parent survive.

Thus the stable syndrome space is

\[
\boxed{H_n\simeq\text{three relative branch directions per parent}.}
\]

The Cartier factorization alone would make a one-branch ray exact in positive
degrees. The surviving homology is created by the interaction between that
source decoder and the four-to-one branching of self-modeling.

## Consequence

Recursive self-modeling is neither pure replication nor complete healing.
With a source-derived recovery differential it separates:

\[
\text{frontier artifact}
\oplus
\text{correctable syndrome}
\oplus
\text{stable relative information}.
\]

This is the first operational error-correction behavior in the micro-Carrier.
The next typing question is whether the stable three-dimensional sibling
quotient corresponds to a predeclared Marici relative-support or coherence
object, rather than merely to the chosen four-letter constructor alphabet.

