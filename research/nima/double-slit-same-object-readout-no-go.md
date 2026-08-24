# Double-slit same-object readout no-go

## Question

Does a normalized positive coherence pairing by itself force

\[
V^2+D^2\le1?
\]

## Countermodel

Take

\[
G=\begin{pmatrix}1&4/5\\4/5&1\end{pmatrix}.
\]

It is strictly positive because

\[
\det G=1-16/25=9/25>0.
\]

The pairing therefore gives the valid visibility \(V=4/5\).  If a
distinguishability readout is independently attached, Gram positivity places
no restriction on it.  Choosing \(D=4/5\) gives

\[
V^2+D^2=32/25>1.
\]

Thus

\[
\boxed{
\text{positive coherence pairing alone does not imply complementarity.}
}
\]

## Surviving structure

Ledger 2026 worked because \(D\) was not independent.  It was derived from
the optimal positive separator of the same two record projectors.  Then

\[
D^2=\det G=1-|\gamma|^2
\]

and the equality follows.

The explanatory requirement is therefore a same-object law:

\[
\boxed{
\text{coherence probe and discrimination probe must be generated from one
positive record object and one admitted dagger/effect structure.}
}

This is exactly the distinction between a framework that permits arbitrary
readout plug-ins and a theory that generates its readouts.

## General mixed-record target

For general records \(\rho_L,\rho_R\), standard quantum mechanics uses

\[
V=F(\rho_L,\rho_R),
\qquad
D=\frac12\|\rho_L-\rho_R\|_1,
\]

and the upper Fuchs--van de Graaf inequality gives

\[
D^2+V^2\le1.
\]

Importing this theorem would not explain the interface.  The Marici target is
to generate from the source:

1. one positive record cone;
2. its dagger/conjugation;
3. normalized states and authorized effects;
4. the induced fidelity and discrimination norm;
5. a forgetful morphism that contracts discrimination and cannot decrease
   fidelity;
6. a source dilation/purification showing both probes descend from the same
   global record object.

The conjecture fails if two independently admissible effect structures on the
same coherence Gram produce different complementarity bounds.

## Verification

```text
python research/nima/checkers/check_double_slit_pairing_only_no_go.py
```

