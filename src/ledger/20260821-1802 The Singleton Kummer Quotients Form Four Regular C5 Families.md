# 1802 — The Singleton Kummer Quotients Form Four Regular \(C_5\) Families

## Question

Do Entry 1801's four Kummer quotient types assemble without an occurrence
defect?

## Assembly

The relative singleton label

\[
d=j-i\pmod5
\]

is preserved by cyclic transport. For each

\[
d=1,2,3,4,
\]

the five labelled occurrences form one free \(C_5\)-orbit. Therefore

\[
\mathcal K_d\simeq\mathbb Q[C_5].
\]

The complete singleton quotient is

\[
\boxed{
\mathcal K_{\rm sing}
\simeq
\mathbb Q[C_5]^{\oplus4}.
}
\]

Its rank and cyclic character are

\[
\operatorname{rank}\mathcal K_{\rm sing}=20,
\qquad
\chi=(20,0,0,0,0).
\]

## Inertia

Each line retains the source-derived square-root character

\[
T_s=-1,
\qquad
N=0.
\]

Cyclic occurrence transport commutes with this Kummer inertia. Hence the
assembled object is the regular occurrence representation tensored with a
sector-specific sign line.

The Kummer deck is not identified with the pair of reflected physical
critical points. Those are distinct structures, and no trace or cancellation
between them is inferred.

## Result

There is no cyclic descent defect, preferred occurrence, or non-regular
character in the singleton-intersection quotient.

## Next falsifier

Pass to non-singleton region walls. Classify their restricted gradients by
rank on the threshold residue sphere and test whether any produces a
quadratic or higher tangency rather than the linear–Morse Kummer germ.

## Evidence

- research/benincasa/checkers/five_site_g5_singleton_kummer_cyclic_assembly.py
- research/benincasa/results/five-site-g5-singleton-kummer-cyclic-assembly.json
- Entry 1801
- allocator claim: seqclaim-15d091cdad5a37c3a2c981c5
