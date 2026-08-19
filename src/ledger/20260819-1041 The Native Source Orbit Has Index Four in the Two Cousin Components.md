# 1041 — The Native Source Orbit Has Index Four in the Two Cousin Components

## Hard-to-vary claim

The native two-seed source orbit reaches both connected components of the
loaded Cousin nerve over (mathbb Q), but its integral component augmentation
has Smith invariants

[
oxed{(1,4).}
]

Thus the residual integral cokernel is (mathbb Z/4). The two rational
components neither remain completely unrelated nor glue integrally without
finite index.

## Frozen augmentation

Entry 1030 orders the six source occurrences by the products

[
(P_1Q_2, P_2Q_2, P_3Q_4, P_4Q_4, P_2Q_1, P_4Q_3).
]

Entry 1037 puts occurrences (0,1,4) in the first connected component and
(2,3,5) in the second. Therefore the component augmentation is fixed:

[
epsilon(e_i)=
egin{cases}
h_L,&iin{0,1,4},\
h_R,&iin{2,3,5}.
end{cases}
]

Applying this augmentation to Entry 945's primitive normalized two-seed
((mathbb Z/2)^2)-orbit gives

[
A_{H_0}=
egin{pmatrix}
2&0&0&2&1&-1&-1&1\
2&0&0&-2&3&1&1&-1
end{pmatrix}.
]

No rational character projector enters this construction.

## Smith calculation

The gcd of all entries is (1). The gcd of all (2	imes2) minors is (4).
Hence

[
operatorname{SNF}(A_{H_0})=(1,4),
]

and

[
operatorname{coker}(A_{H_0})
congmathbb Z/4.
]

Over (mathbb Q), (A_{H_0}) has rank two, agreeing with Entry 1038.
Integrally, the order-four remainder is exactly the scale already warned
about by the unresolved character projector.

## Narrow conclusion

The first surviving obstruction is not a new rational Cousin class. It is a
finite integral gluing defect between the native source orbit and the two
component generators:

[
oxed{
mathbb Z^8_{m source orbit}
longrightarrow
mathbb Zlangle h_L,h_Rangle
longrightarrow
mathbb Z/4
longrightarrow0.
}
]

This is an algebraic source-lattice statement. It does not yet identify the
(mathbb Z/4) with an integral Betti, twisted-homology, or physical
amplitude class.

## Next falsifier

Derive the integral regularized-cycle lattice from the source Pochhammer
construction and compare its component augmentation with (A_{H_0}). If its
orientation and branch data saturate the index-four quotient, the defect is
a presentation artifact. If the quotient persists in the source-normalized
Betti lattice, it is genuine two-primary string-sector coefficient data.

## Durable artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_loaded_cousin_integral_h0.rs`
- `research/benincasa/string-six-point-loaded-cousin-integral-h0.json`

Epistemic event: `ev-000000000660-53aa5647-523f-4831-8b9a-1ee7058e4c36`.
