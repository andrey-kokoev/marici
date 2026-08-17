---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The Three-Cut Residue Vector Is Closed but Source-Exact

## Question

Entry 362 proposed that the global home of the six singly marked physical
summands might be a nonzero degree-one Cousin class on

\[
D_{\rm Cut}=D_{12}\cup D_{23}\cup D_{31}.
\]

The hard-to-vary claim tested here is

\[
\boxed{
\text{the all-positive six-occurrence residue vector defines a nonzero
class in }H^1\text{ of the full source Cousin complex}.}
\]

The full complex retains the frozen meromorphic pre-residue integration form
in degree zero. Removing that source term before testing exactness is not
allowed.

## Frozen degree-one vector

Use the occurrence order

\[
(12|23),(12|31),(23|31),(23|12),(31|12),(31|23).
\]

The printed source coefficients and cyclic residue orientations are all
positive, so its degree-one residue vector is

\[
c_1=(1,1,1,1,1,1).
\]

The two cyclic orbits have length three, and (c_1) is (C_3)-invariant.
It is primitive over (mathbb Z). Forgetting the lower occurrence gives

\[
(2,2,2),
\]

recovering the previously derived occurrence-identification factor two.

## Pairwise and triple differentials

Let

\[
(u_{12},u_{23},u_{31})
=(q_{\mathcal G_{12}},q_{\mathcal G_{23}},q_{\mathcal G_{31}}).
\]

The six marked-normal Laurent exponents are

\[
(-1,0,0),(-1,0,0),
(0,-1,0),(0,-1,0),
(0,0,-1),(0,0,-1).
\]

Every pairwise Cut residue retains only terms negative in the corresponding
two normal variables. Therefore the complete degree-one differential is

\[
d_1=0_{3\times6}.
\]

No term is negative in all three variables, so the direct triple residue is
also zero. The lower denominators remain occurrence labels and relative
coefficient boundaries. At the generic Cut intersections they are units;
none is an opposite marked-Cut normal.

Consequently

\[
\boxed{d_1c_1=0,}
\]

with no pairwise or triple correction.

## Full-complex exactness

Closedness is not nontriviality. The frozen primary source is itself the
meromorphic degree-zero form

\[
\Omega_{\rm src}
\propto
\frac1{q_{\mathcal G_{12}}}
\left(
\frac1{q_{\mathfrak g_{23}}}
+
\frac1{q_{\mathfrak g_{31}}}
\right)
+\operatorname{cyc},
\]

with the common Cayley--Menger measure and one-site factors understood.
Taking its six labelled first residues gives exactly

\[
d_0\Omega_{\rm src}=c_1.
\]

Hence

\[
\boxed{
c_1\text{ is closed but exact in the full source-defined Cousin complex}.}
\]

The tested nonzero-(H^1) claim is falsified.

If degree zero is truncated away, (c_1) survives as a primitive nonzero
class with residue fingerprint ((1,1,1,1,1,1)). That is an associated
support grade, not the cohomology class of the full complex.

## Narrow result

The source-defined global object is the filtered residue packet

\[
\boxed{
\Omega_{\rm src}
\xrightarrow{\ d_0\ }
c_1
\xrightarrow{\ d_1=0\ }
0,
}
\]

not a Čech-glued degree-zero coefficient object and not an intrinsic nonzero
degree-one Cousin cohomology class.

This preserves the distinction

\[
\text{nonzero associated support grade}
\not\Rightarrow
\text{nonzero class in the untruncated global complex}.
\]

## Classification

| Datum | Classification |
|---|---|
| (Omega_{\rm src}) | frozen global meromorphic coefficient form |
| six first residues | occurrence-resolved Cut support grade |
| pairwise/triple residues | zero |
| (c_1) in positive truncation | primitive (C_3)-invariant class |
| (c_1) in full complex | exact boundary |
| factor two after forgetting | occurrence identification |
| new carrier datum | none |

## Physical qualification

Exactness in the coefficient Cousin complex does not imply that the physical
relative period vanishes. Pairing with a relative integration chain can
retain boundary data. No statement about that pairing is inferred here.

## Evidence

- `research/benincasa/marici-gm/src/bin/three_cut_cousin_cocycle.rs`;
- `research/benincasa/three-cut-cousin-cocycle-certificate.json`;
- the primary six-term source frozen in Entries 161, 188, and 229;
- Entries 356--362.

## Next falsifier

Pair the two-term filtered packet

\[
[\Omega_{\rm src}\to c_1]
\]

with the frozen positive Bunch--Davies relative chain. Compute whether the
chain boundary converts the coefficient-exact residue vector into a nonzero
relative period class, while retaining all six occurrences and their common
orientation.

The finite alternatives are:

1. the relative pairing kills the exact packet, so the global six-term
   assembly contains no additional Cut-supported class; or
2. a canonical boundary pairing survives, locating the physical assembly in
   relative/Borel--Moore homology rather than coefficient Cousin cohomology.

No support summand or transition map may be added to force the second
outcome.
