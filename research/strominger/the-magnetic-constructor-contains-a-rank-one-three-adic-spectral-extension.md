# The magnetic constructor contains a rank-one 3-adic spectral extension

Owner: `marici.Strominger`

## Question

What source structure could force every strict maximal-exterior response to lie
on one Plücker line?

## Exact constructor theorem

Let \(C\in GL(4,\mathbb Z)\) be the fixed integral constructor generating
the magnetic grade orbit. Its characteristic polynomial factors exactly as

\[
\det(\lambda I-C)
=(\lambda-1)^2(\lambda^2-147458\lambda+1).
\]

The reciprocal quadratic trace is not a generic integer:

\[
147458-2=147456=3^2 2^{14}.
\]

Thus the fixed sector and reciprocal sector coincide modulo \(3^2\) at the
level of their spectral polynomials.

Define

\[
N=C-I,
\qquad
Q=C^2-147458C+I.
\]

Their exact ranks and 3-adic contents are

\[
\begin{array}{c|c|c}
&\operatorname{rank}&v_3(\operatorname{content})\\
\hline
N&3&1\\
Q&2&2\\
NQ&1&3.
\end{array}
\]

The bridge \(NQ\) is nonzero and equals

\[
55296
\begin{pmatrix}
-1&1&-1&1\\
-1&1&-1&1\\
-1&1&-1&1\\
-1&1&-1&1
\end{pmatrix},
\qquad
55296=3^3 2^{11}.
\]

One additional identity factor kills it:

\[
N^2Q=0,
\qquad
NQ\ne0.
\]

Therefore the two spectral factors do not split semisimply in the integral
constructor. They meet through a one-dimensional extension supported at exact
3-adic depth three.

## Source recurrence

Cayley--Hamilton gives the exact finite recurrence

\[
C^{n+4}
-147460C^{n+3}
+294918C^{n+2}
-147460C^{n+1}
+C^n=0.
\]

This is the first source recurrence capable of replacing the matrix census.
Every grade state, and hence every downstream exterior response, is generated
inside a four-state integral recurrence. Modulo any fixed power of three this
becomes a finite residue automaton.

## Explanatory consequence

The direct bridge explanation is falsified. The normalized increments

\[
(C^{3^r}-I)/3^{r+1}\pmod3
\]

form one constant rank-three matrix, not the rank-one bridge. Therefore the
bridge does not directly carry the source shift direction.

The rank-one extension remains an exact constructor invariant, but any role in
Plücker scalarity requires an additional source-derived map or the derivative
of the nonlinear magnetic readout. The exact result established here is the
constructor's spectral extension, not its compatibility with that readout.

## Claim boundary

This is an exact theorem about the loaded integral constructor \(C\). It does
not yet derive the character \(\chi(n,3^r)\), prove an unbounded cancellation
classification, construct an Ext class, or give a source-derived comparison to
another sector.

## Disposition

The missing explanatory object is no longer unspecified. It is the rank-one
integral spectral bridge

\[
(C-I)(C^2-147458C+I).
\]

The remaining question is whether the magnetic readout preserves this bridge
strongly enough to force the observed Plücker-line character.

## Verification

Run:

```powershell
python research/strominger/checkers/constructor_spectral_extension_checks.py
```

All ten exact gates pass. Machine-readable output is in
`research/strominger/results/constructor_spectral_extension_checks.json`.