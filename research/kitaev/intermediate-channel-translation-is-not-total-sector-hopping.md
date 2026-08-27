# Intermediate-channel translation is not total-sector hopping

Owner: `marici.Kitaev`

## Correction

The earlier first version of the data-reflection packet incorrectly imported
the persistent `B`-reference requirement from the four-anyon total-`A` versus
total-`B` workspace into the three-anyon intermediate `A_L/B_L` channel
problem.

That inference is invalid. The file
`the-data-vacuum-reflection-is-sign-translation-conjugated-exchange.md` has
been corrected.

## Exact distinction

For the four-anyon workspace,

\[
\operatorname{Hom}(A,C^{\otimes4})
\oplus
\operatorname{Hom}(B,C^{\otimes4}),
\]

the two summands have different total charges. A coherent map between them
carries sign charge and needs a compensating port to remain inside one global
superselection sector.

For the three-anyon qutrit,

\[
\operatorname{Hom}(C,C^{\otimes3}),
\]

the labels `A_L,B_L,C_L` describe alternative intermediate channels inside
one fixed total charge `C`. An endomorphism that mixes these basis states is
charge neutral as an operation on the complete three-anyon system.

Therefore:

```text
total A <-> total B       requires global charge compensation
intermediate A_L <-> B_L  does not, by superselection alone
```

The two operations may use similar sign-line diagrams, but they have different
domains and different charge accounting.

## What remains true

The fusion-rule permutation

\[
A\leftrightarrow B,
\qquad
C\longmapsto C
\]

still defines an algebraic unitary `S_B` after fusion frames are chosen, and

\[
S_B(I-2P_B)S_B^*=I-2P_A.
\]

Thus the data reflection remains the sign-label conjugate of native electric
exchange.

What is not established is a physical operation implementing `S_B`. Tensoring
labels by an invertible object is not itself an actuator on the multiplicity
space. The source may realize it through a neutral `B,B` ancilla pair, a
ribbon network, pair-channel deformation, measurement with coherent return,
or full qutrit control. No route is selected by the fusion rule alone.

## Revised source question

The correct finite question is:

> Is there a neutral microscopic constructor whose compression to the
> three-anyon total-`C` fusion space swaps `A_L` and `B_L`, fixes `C_L` up to
> declared phases, and returns every auxiliary charge to vacuum?

This asks for an endomorphism within one superselection sector. If a `B,B`
pair is used, its common vacuum return is a whole-instrument condition, not a
pre-existing external reference-frame requirement.

## General typing rule

Before transferring a reference requirement from one fusion problem to
another, distinguish:

1. external total-charge labels of the whole subsystem;
2. internal fusion-tree labels within a fixed total charge;
3. auxiliary charges temporarily present in a constructor history.

Only the first directly invokes a superselection block between source and
target spaces. The second is protected logical information and can be mixed by
a sufficiently nonlocal neutral endomorphism. The third must close but need
not persist as a reference after the operation.

## Falsifiers

- The three qutrit basis states are assigned different total charges.
- Every fusion-channel-mixing logical gate is said to violate charge
  superselection.
- The four-anyon total-sector bridge is treated as the same typed morphism as
  an intermediate-channel permutation.
- The algebraic sign-label permutation is promoted to a physical gate without
  a constructor.
- An auxiliary `B,B` pair is discarded in channel-dependent states while a
  unitary qutrit operation is claimed.

## Claim boundary

This packet repairs a typing error. It does not construct `S_B` or weaken the
separate theorem that genuine total-`A` to total-`B` sector hopping requires
charge compensation.

No build, checker, or Git operation was used.
