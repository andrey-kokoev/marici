# Minimal boundary attachment forces a relative determinant

## Mixed moments are Markov parameters

For boundary dynamics \(A\), primitive incidence \(b\), and return readout
\(c\), the mixed moments

\[
m_j=cA^jb
\]

are exactly the Markov parameters of the boundary transfer

\[
h(t)=c(I-tA)^{-1}b.
\]

The previous determinant audit showed that the primitive Euler factor is
unchanged precisely when every \(m_j\) vanishes.

## Controllability closes the escape

Suppose the incidence is cyclic:

\[
\operatorname{span}\{b,Ab,\ldots,A^{N-1}b\}=H.
\]

If every mixed moment vanishes, then \(c\) annihilates a spanning family.
Consequently

\[
c=0.
\]

Thus a controllable boundary attachment cannot be both:

- determinant-preserving; and
- equipped with a nonzero return readout.

The multi-input version is identical. If the controllability matrix

\[
\mathcal C=[B,AB,\ldots,A^{N-1}B]
\]

has full row rank, then \(CA^jB=0\) for every \(j\) forces \(C=0\).

## Minimal realization verdict

A comparison system intended to expose all boundary states should be
controllable from the arithmetic incidence and observable at the return port.
For such a minimal realization, its transfer cannot vanish identically.
Therefore it necessarily contributes a nontrivial relative determinant.

The only determinant-preserving nonzero couplings live on unreachable or
unobserved subspaces. They may be algebraically nonzero, but they do not form
a faithful two-way comparison.

This corrects the attachment architecture:

1. the primitive one-cycle carries the Euler factor;
2. the lossless doubled cut carries boundary state;
3. a faithful two-way comparison produces a relative transfer determinant;
4. that determinant must be retained as the chart-change object.

It cannot be erased while simultaneously claiming faithful incidence and
return.

## Delayed relative factor

For a length-\(N\) shift with incidence at one end and return at the other,
the controllability matrix is full rank. The first nonzero Markov parameter
appears at depth \(N-1\), so low-grade tests still pass. The relative factor
is nevertheless forced.

This explains why finite primitive and square checks can look exact while a
later cyclic grade reveals the boundary attachment.

## Source gate

The theta/Euler problem now asks for the actual realization

\[
(A,B,C).
\]

At every cutoff, compute:

1. controllability rank from the labelled prime incidences;
2. observability rank of the boundary return;
3. the first nonzero Markov parameter;
4. the corresponding relative determinant coefficient;
5. compatibility of these data under cutoff refinement and reciprocal
   exchange.

If the realization is minimal, a relative determinant is compulsory. If it
is not minimal, the unreachable or unobservable quotient must be typed before
any scalar comparison.

## DPC verdict

Resolved:

- determinant preservation plus controllability forces zero return;
- a faithful minimal attachment necessarily carries a relative determinant;
- apparently harmless nonzero determinant-preserving couplings are confined
  to unreachable or unobserved sectors.

Withheld:

- source construction of the actual theta/Euler realization;
- its minimality;
- the explicit relative determinant;
- completion and zero-state implications.

The finite falsifier is a claimed controllable, nonzero-return attachment with
all Markov parameters zero. Linear algebra makes those declarations
incompatible.

## Verification

The checker `check_minimal_attachment_relative_determinant.py` verifies the
cyclic-shift theorem, the delayed first return, and a nonminimal coupling whose
zero transfer is explained by an unreachable readout sector.
