# 4147 — A Source-Fixed Integral Lattice Repairs the Two-Adic Barcode

## Scope

This entry corrects the parameter-family interpretation of Entries 4139 and 4143. Their Smith profiles remain exact for the separately normalized numerical fibers, but those fiberwise primitive presentations are not specializations of one integral parameter-ring matrix.

## Typing defect

The previous source-presentation checker cleared denominators and then divided every row by its numerical content after substituting the external point. Numerical content division does not commute with specialization. Consequently, the resulting primitive fiber lattices cannot be assembled into a single module over the parameter ring.

The contradiction was finite: the two tested all-odd fibers had identical reduction modulo \(2\), while their claimed common high-valuation tail had different determinant parity. This is impossible for specializations of one fixed integral matrix.

Therefore the old data establish only fiberwise arithmetic invariants. They do not authorize Fitting ideals over the parameter ring.

## Source-fixed repair

The physical de Rham relations carry the fixed Kummer coefficient \(-1/2\). The repaired structural lattice therefore:

- multiplies every de Rham row by the same source-fixed denominator \(2\);
- retains each multiplication relation with its source unit;
- performs no point-dependent content division.

This normalization is defined before external specialization.

The two repaired matrices have shape

\[
14422\times2278.
\]

At the two all-odd points \((5,7,11)\) and \((7,11,17)\), their reductions modulo \(2\) have exactly the same rank and pivot certificate:

\[
\operatorname{rank}_{\mathbf F_2}=1715,
\qquad
\dim\operatorname{coker}_{\mathbf F_2}=563,
\]

with common pivot hash

```text
f12489f3368046fc198e8be954a5f26885885ec6b61b4a46ab9ab7b9007a680f
```

Good-prime ranks are \(2194\) at both points, hence the free quotient rank remains \(84\).

## Structural two-adic profiles

The common low-valuation profile is

\[
v_2=0,1,2,3,4
\quad\text{with multiplicities}\quad
1715,420,45,10,2.
\]

The terminal profiles are

\[
(5,7,11):\qquad v_2=8\text{ with multiplicity }2,
\]

and

\[
(7,11,17):\qquad v_2=8,12\text{ with multiplicity }1\text{ each}.
\]

Both profiles reach cumulative rank \(2194\), leaving free rank \(84\).

Thus parameter-dependent higher two-adic variation survives the repair. It now occurs inside fibers of one specialization-compatible source lattice, rather than being manufactured by independent fiberwise normalization.

## Narrow conclusion

The maximal mixed-incidence block carries a genuine two-adic barcode over the tested all-odd locus:

- its mod-\(2\) associated grade is constant at the two fibers;
- its rational rank is constant;
- its high two-adic elementary divisors vary.

This authorizes a parameter-ring Fitting/localization calculation for the repaired structural lattice. It does not yet identify the determinantal support polynomial or prove global constancy away from it.

## Supersession

Entries 4139 and 4143 remain valid as fiberwise computations and as localization evidence. Any statement there treating their pointwise primitive matrices as fibers of one parameter-ring module is superseded by this entry.

## Next falsifier

Construct the maximal-block structural matrix over the parameter ring before specialization, compute its first two relevant determinantal/Fitting ideals, and test whether their specializations reproduce the valuation-\(8\) versus valuation-\(12\) split without introducing a fitted support factor.
