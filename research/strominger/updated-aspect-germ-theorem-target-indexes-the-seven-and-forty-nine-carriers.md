# Updated Aspect germ theorem indexes the seven and forty-nine carriers

## The updated theorem

Aspect's deeper relational calculus separates three gates:

1. **Fiber gate:** the target must be constant on complete fibers of the
   proposed quotient.
2. **Arity gate:** the target must be tested at its native arity; lower-arity
   marginals do not determine a higher relation without a reconstruction
   theorem.
3. **Authority gate:** descent of an observable does not supply a realization
   section or an executable selector.

The marked carrier germ is relative to a declared target family. There is no
target-independent smallest carrier.

## Target-indexed carrier theorem

Let \(\Lambda\) be an abelian source carrier and let

\[
\mathcal T=\{t_i:\Lambda\to Y_i\}
\]

be a finite family of linear targets. Define

\[
K_{\mathcal T}=\bigcap_i\ker t_i.
\]

Then the smallest quotient through which every member of \(\mathcal T\)
factors is

\[
G_{\mathcal T}=\Lambda/K_{\mathcal T}.
\]

Every other quotient supporting all targets in \(\mathcal T\) admits a
canonical quotient map onto this one. Equivalently, every target in the family
factors through this coarsest adequate quotient. This is the exact linear form
of Aspect's fiber gate.

## Three magnetic target families

Work modulo seven with

\[
\ell(x,y)=3x-2y,
\qquad
\ell_X(x,y)=3y-2x.
\]

Define

\[
q_-=\ell-\ell_X=5(x-y),
\qquad
q_+=\ell+\ell_X=x+y.
\]

### Odd target only

For

\[
\mathcal T_-=\{q_-\},
\]

the minimal germ is

\[
G_{\mathcal T_-}=\mathbb F_7^2/\ker q_-\cong\mathbb F_7.
\]

It has seven classes. The 49-class refinement is unnecessary for this target.

### Joint chart target

For

\[
\mathcal T_{\mathrm{joint}}=\{\ell,\ell_X\},
\]

transversality gives

\[
\ker\ell\cap\ker\ell_X=0.
\]

Hence

\[
G_{\mathcal T_{\mathrm{joint}}}=\mathbb F_7^2,
\]

with 49 classes. This is the minimal jointly faithful reflected-chart germ.

### Phase target

The canonical discriminant linking construction is not unary. It pairs a
primal relative class with an independently typed dual relative class:

\[
\lambda:G_{\mathcal T_-}\times G_{\mathcal T_-}^{\vee}
\longrightarrow\mathbb Q/\mathbb Z.
\]

After choosing compatible generators, its finite coordinate has the form

\[
\lambda(a,b)=\frac{3ab}{7}\pmod{\mathbb Z}.
\]

Its input domain has 49 ordered pairs, but its output has only seven phase
values. This 49 is a binary primal--dual domain. It is not the same object as
the unary 49-class joint chart carrier.

## Arity gate

The numerical equality

\[
|G_{\mathcal T_{\mathrm{joint}}}|
=
|G_{\mathcal T_-}\times G_{\mathcal T_-}^{\vee}|
=49
\]

does not authorize an identification. Their types and variances differ:

```text
joint chart germ:      one input, two reconstructed chart coordinates
phase-pairing domain:  primal input and dual input, one bilinear phase output
```

Moreover, the phase map is not faithful on its 49 input pairs. Many pairs
produce the same phase. Thus a phase observation cannot reconstruct either the
joint chart germ or the primal--dual pair.

## Authority gate

The perfect linking form supplies a mathematical binary target. It does not
supply:

- a physical realization of the dual input;
- an instrument coupling to the phase;
- a selector choosing a generator or a source state from a phase value;
- proof that the magnetic source exposes both inputs in one executable domain.

Therefore the physical obstacle survives in a sharper form. It is not a
missing coefficient group and not a missing reflection action. It is the
absence of an authority-bearing realization of the native binary phase target.

## Correct architecture

```text
odd chart distinction ----------> seven-class primal germ ---\
                                                             linking mate ---> phase value
dual discriminant distinction --> seven-class dual germ -----/

even + odd chart targets -------> 49-class joint chart germ
```

The lower and upper lines answer different questions. Neither can replace the
other by cardinality matching.

## Revised obstacle

The next source-side question is:

> Does the magnetic construction provide a dual marked germ and a native
> binary coupling whose restriction is the discriminant linking form?

If yes, the seven-valued phase port is source-derived. If only the unary odd
quotient exists, then the mathematical phase pairing remains non-executable.
If a proposed coupling is inferred merely from the existence of 49 unary
states, Aspect's arity and authority gates reject it.

## Subsequent resolution

The algebraic part of this question is resolved in
`affine-dualization-supplies-the-binary-germ-but-not-its-physical-realization.md`.
Integral dualization of the same affine source map supplies the transpose germ,
and the canonical linking form restricts to the perfect odd pairing

\[
\lambda_-(t,s)=\frac{2ts}{7}\pmod{\mathbb Z}.
\]

Thus the fiber and arity gates close algebraically. The remaining obstacle is
only the authority-bearing physical realization of this binary phase germ.
