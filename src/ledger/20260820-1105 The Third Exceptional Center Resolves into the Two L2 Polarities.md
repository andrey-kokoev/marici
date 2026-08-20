# 1105 — The Third Exceptional Center Resolves into the Two L2 Polarities

## Record

After closing the second center in Entry 1104, consider the next frozen
rank-twelve center

\[
(u,v)=(2,4),
\qquad
(a,b)=(0,1).
\]

Sequence claim: `seqclaim-05a969f2f24bcfd07f66db8e`.

## Joint Newton geometry

Use

\[
p=u-2,
\qquad q=v-4,
\qquad A=a,
\qquad B=b-1.
\]

Exact source expansion gives

\[
\boxed{
\nu_J(K)=2,
\qquad
\operatorname{in}_J(K)=16B^2,
}

and

\[
\boxed{
\nu_J(K_1)=1,
\qquad
\operatorname{in}_J(K_1)=32B.
}

The marked initial forms are

\[
L_1=B-p,
\qquad
L_2^+=A+\frac{q-p}{2}.
\]

The source-form orders in the standard twelve-class ordering are

\[
\boxed{
(-1,0,0,3,2,1,2,1,0,1,3,3).
}

## First smoothing coefficient

On the \(p\neq0\) chart the doubled branch is \(B=0\).  Restricting the next
radial coefficient gives

\[
\boxed{
K_3|_{B=0}
=4(2A-q+1)(2A+q-1).
}

These are exactly the two resolved polarities

\[
L_2^+=A+\frac{q-1}{2},
\qquad
L_2^-=A-\frac{q-1}{2},
\]

up to the displayed source-fixed units.  On the same doubled plane,

\[
L_1=-1,
\]

so the first marked wall is a unit and contributes no conductor face.

## Deutsch--Popperian verdict

The conjecture that this center introduces an unlabelled smoothing divisor is
falsified.  Its doubled branch is smoothed precisely by the two
occurrence-resolved \(L_2\) polarities already native to the carrier.

The surviving architecture is

\[
\boxed{
\text{existing occurrence-resolved carrier}
+
\text{center-specific nonuniform coefficient lattice}.
}

No new carrier incidence is indicated.

## Evidence

- `research/benincasa/marici-gm/src/bin/rank12_u2v4_newton.rs`;
- `research/benincasa/rank12-u2-v4-joint-newton.json`.

Epistemic graph admission:
`ev-000000000804-c338c07c-c947-4791-af48-ea75c2ec4cbb`.

## Next falsifier

Normalize the doubled \(B\)-cover and construct the labelled simplex for the
three smoothing factors \(p,L_2^+,L_2^-\).  Verify its deck character and
augmented homology independently rather than importing Entry 1104 by analogy.
