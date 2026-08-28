# The Selective Sheet Gate Descends Projectively without a Sheet Framing

## Correction from the multiplicity-one transfer

Figueiredo WP867 shows that a multiplicity-one odd character line is preserved
by every equivariant operation. Applied to the real self-adjoint endomorphisms
of one magnetic sheet pair, the reflection-odd line is uniquely spanned by

\[
Z=\operatorname{diag}(-1,1).
\]

Sheet exchange $X$ sends

\[
XZX=-Z.
\]

Entry 3763 correctly identified this as an obstruction to a global linear
choice of $Z$. But $Z$ and $-Z$ differ by a global scalar and therefore
define the same projective operation. Hence

\[
[XZX]=[Z]\quad\text{in }PGL_2.
\]

The physical selective gate descends projectively even when the sheet sign
line has nonzero first Stiefel-Whitney class.

## What the correction does not solve

The actual metaplectic central loop acts as $-I_2$, whose projective class is
the identity. It is not the projective class of $Z$. Projective descent
therefore removes the global framing obstruction but does not derive selective
action from the source loop.

The remaining source question is sharper:

```text
What magnetic constructor maps the central-loop class to the unique
reflection-odd projective involution [Z] on the sheet multiplicity space?
```

## Kato transfer

Figueiredo WP869 supplies the corresponding deformation law. When the odd
line varies inside a gapped family, the Kato unitary transports the actual
projector and detector frame together. For the sheet gate this means that a
source-derived connection could transport $[Z]$ without choosing a fixed
coordinate frame. Holonomy may obstruct a linear lift while leaving the
projective class intact.

This is mathematical parallelization, not execution authority. The detector
or sheet coupling must still be derived from the same magnetic source
connection.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/projective_selective_sheet_gate_descent_checks.py
```
