# 20260817-350 — Saturated Soft-Support Extension Test at (X_2=0)

## Question

Does the final four-master algebraic--elliptic extension acquire a class supported at the soft intersection

[
E_T=X_2=0
]

that is invisible on the generic total-energy divisor?

## Frozen input

Work in the homogeneous chart

[
X_1=1,qquad u=E_T,qquad y=X_2=rac{u+v}{2}-1.
]

The source-defined algebraic kernel generator degenerates at (u=0,v=2) as

[
v_{m alg}=y^2igl(0,1-y^2,2,-2igr).
]

The supported test therefore uses the saturated generator

[
widetilde v_{m alg}=rac{v_{m alg}}{X_2^2}
]

before specializing to (X_2=0). No carrier cell, support summand, or fitted normalization is added.

## Finite falsifier

1. Reconstruct the exact rational (u)-connection of the final four-master block.
2. Extract its logarithmic residue along (u=0).
3. Conjugate that residue into the regular saturated frame
   [
   (e_6,widetilde v_{m alg},e_7,widetilde e_8).
   ]
4. Expand at the soft normal (v-2=0).
5. Read the kernel-to-quotient principal part. A nonzero principal part would be a soft-supported extension class on the existing soft carrier.

## Result

At both independent finite fields,

[
p_1=2305843009213693951,
qquad
p_2=2305843009213693921,
]

with disjoint deterministic reconstruction streams, every rational fit closes and the Laurent orders agree.

The only soft pole in the saturated total-energy residue lies in the elliptic quotient block:

[
operatorname{PP}_{X_2=0} R_{E_T}
=
egin{pmatrix}
0&0&0&0\
0&0&0&0\
0&0&0&-rac12\
0&0&0&0
end{pmatrix}.
]

The algebraic-to-elliptic extension principal part is

[
oxed{
operatorname{PP}_{X_2=0}
igl(R_{E_T}^{m ext}igr)=0.
}
]

A regular finite off-diagonal coefficient survives:

[
operatorname{FP}_{X_2=0}
igl(R_{E_T}^{m ext}igr)
=
egin{pmatrix}
0&-rac14\
0&0
end{pmatrix}.
]

Thus the test distinguishes vanishing of a supported logarithmic class from vanishing of all finite mixing: only the former is established.

## Narrow conclusion

For the final four-master block, after the source-forced (X_2^2)-saturation of (v_{m alg}), no kernel-to-elliptic extension class is supported at the generic (X_2=0) soft intersection of the total-energy divisor.

The remaining pole is the expected quotient degeneration, and the regular (-1/4) mixing is coefficient-level connection data. This calculation requires no new carrier datum.

Classification:

[
oxed{
	ext{existing soft carrier}
+
	ext{elliptic quotient degeneration}
+
	ext{regular coefficient mixing};
quad
	ext{no new supported extension detected}.
}
]

## Scope

This is a modular, generic fiberwise de Rham calculation in the final four-master sector. It does not establish:

- extension through every discriminant component;
- an integral-lattice statement;
- compatibility with the physical relative integration chain;
- vanishing at the other soft corner (X_1=0);
- vanishing of supported classes in the remaining five algebraic masters;
- the full Cut--nearby comparison.

## Evidence

- `research/benincasa/soft-support-saturated-certificate.json`
- `research/benincasa/soft-support-saturated-replication-certificate.json`
- executable command:
  `cargo run --release --bin marici-gm -- soft-support-test <output.json>`
- replication:
  add `--features replication-prime`

## Next falsifier

Repeat the saturation analysis at the other site-soft branch (X_1=0), then test the complete nine-master algebraic kernel. Any nonzero supported kernel-to-elliptic principal part must be classified as soft-support coefficient data unless it requires an incidence divisor absent from the frozen energy carrier.
