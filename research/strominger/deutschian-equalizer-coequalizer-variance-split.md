# Equalizer and coequalizer expose the two closure variances

## Branching after the one-path theorem

Contextual monomorphisms compose safely along one path.  The next possible
loss occurs when parallel paths are recombined.

Take the two faithful maps on

\[
C=\mathbb F_7
\]

given by

\[
f(x)=x,
\qquad
g(x)=-x.
\]

Both maps are automorphisms.  What happens next depends on variance.

## Contravariant compatibility: equalizer

The equalizer retains source states on which the two routes agree:

\[
E=\{x\in C:f(x)=g(x)\}.
\]

Since \(2\) is invertible in \(\mathbb F_7\),

\[
E=\{0\}.
\]

No two distinct admitted states are identified.  Instead, the admissible
source domain shrinks.  The equalizer inclusion remains monic.

## Covariant aggregation: coequalizer

The coequalizer identifies record values differing by the route residual:

\[
Q=C/\langle f(x)-g(x):x\in C\rangle.
\]

Here the residual is \(2x\), whose image is all of \(C\).  Therefore

\[
Q=0.
\]

The complete record object collapses even though both incoming routes are
faithful.

## The theorem and the falsifier

The example falsifies the claim that coherent faithful branches remain
faithful under an unspecified merge.  “Merge” has no invariant meaning until
its variance is declared.

It also gives an exact interpretation of the two directed closure towers:

- backward or contravariant closure forms compatibility subobjects and may
  remove inadmissible states;
- forward or covariant closure forms record quotients and may identify
  distinguishable states.

These operations cannot be bundled into one neutral closure constructor.

## Role of a coherence cell

An explicit comparison automorphism can relate the two routes without
coequalizing their values.  Retaining that comparison records the relative
sign.  Replacing it by the equation \(f=g\) forgets the sign and creates the
collapse.

Thus a coherence cell and a quotient enforcing equality are not the same
operation.

## Deutschian rule

> At every branch merge, declare whether the source forms a limit-like
> compatibility domain, a colimit-like record quotient, or a labelled
> comparison cell.  Prove the kernel of that exact construction.  Faithful
> incoming branches supply no default authority for the merge.

This localizes the first larger-net surprise: it occurs at recombination, not
inside the already verified branches.
