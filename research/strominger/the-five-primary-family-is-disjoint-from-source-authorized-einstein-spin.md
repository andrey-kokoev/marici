# The Five-Primary Family Is Disjoint from Source-Authorized Einstein Spin

## Correction

The congruence

\[
s\equiv4\pmod5
\]

classifies degeneracies in the formally generalized Laurent family. It does not classify physical sectors of the completed magnetic source without an additional attachment theorem.

The completed Bondi/Einstein source authorizes the radiative graviton at spin two. For that source value,

\[
n=4s-1=7,
\qquad
\gcd(n,5)=1.
\]

Hence the two reflected affine observations are transverse and no primitive odd repair port is required.

The first formal degeneracy occurs at spin four, where (n=15). But the spin-four sparse operator was constructed by replacing the spin-two Laurent factor with its covariant general-spin analogue. Einstein gravity did not supply a propagating spin-four field or an attachment from its state space to that formal operator.

Therefore

\[
\{\text{source-authorized Einstein spins}\}
\cap
\{s:s\equiv4\pmod5\}
=\varnothing.
\]

## What the falsifier established

The failed Deutschean conjecture conflated three objects:

1. a formal parameter (s) in a Laurent boundary operator;
2. an affine coordinate pair ((x,y));
3. a source-constructible physical state.

The sparse-matrix calculation connects the first two. It does not provide the third arrow. Consequently a five-element affine fibre cannot yet be interpreted as five physical alternatives, and the absence of a physical port distinguishing them is not a defect in Einstein gravity.

## Surviving conditional theorem

Let a source theory independently provide:

- a spin-(s) carrier;
- the generalized boundary operator;
- an attachment of source states to the affine lattice;
- reflection acting compatibly on both constructions.

Then, and only then, the arithmetic theorem applies physically. If (s\equiv4\pmod5), the reflected observation packet has a five-element fibre. A single scalar observation restores faithfulness precisely when its restriction to that fibre is nontrivial, equivalently when its coefficients satisfy

\[
u-v\not\equiv0\pmod5.
\]

This is a portable obstruction theorem for a future higher-spin source. It is not a prediction that Einstein gravity contains the missing port.

## Revised explanation

The source-derived explanation in the magnetic theory terminates at spin two:

```text
Bondi/Einstein radiative source
  -> spin-two carrier
  -> modulus seven affine character
  -> two reflected charts, transverse because five is invertible modulo seven
  -> jointly faithful reflected observation
```

The formal extension has a different status:

```text
general-spin Laurent substitution
  -> modulus 4s-1 affine family
  -> five-primary degeneracy when s = 4 mod 5
  -/-> physical higher-spin state carrier
```

The broken arrow is the missing constructor. The five-primary pattern predicts what any successful higher-spin attachment would have to confront; it does not construct that attachment.

## Evidence replay

The checker treats the Einstein spin spectrum as a typed source input and verifies that spin two has modulus seven, that five is invertible there, and that the authorized spectrum has empty intersection with the formal exceptional family through spin one hundred.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/einstein_spin_five_primary_disjointness_checks.py
```

The result is written to `research/strominger/results/einstein_spin_five_primary_disjointness_checks.json`.
