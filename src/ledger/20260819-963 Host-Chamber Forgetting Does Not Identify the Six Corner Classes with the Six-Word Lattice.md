# 963 — Host-Chamber Forgetting Does Not Identify the Six Corner Classes with the Six-Word Lattice

## Comparison gate after Entry 962

Entry 962 constructs six primitive supported corner classes.  A rank-six
source and a rank-six target do not determine a comparison.  Before seeking
a period pairing, test the only map supplied by the current combinatorial
packet: forget the corner support and retain its labelled host chamber.

Order the six corner occurrences as

\[
\begin{array}{c|c}
12|35&124356\\
124|35&124356\\
124|35&142356\\
13|25&134256\\
134|25&134256\\
134|25&143256
\end{array}
\]

and the six-word chamber frame as

\[
(123456,124356,132456,134256,142356,143256).
\]

## Host-label matrix

In canonical positive orientations, the resulting integral incidence matrix
is

\[
H=
\begin{pmatrix}
0&0&0&0&0&0\\
1&1&0&0&0&0\\
0&0&0&0&0&0\\
0&0&0&1&1&0\\
0&0&1&0&0&0\\
0&0&0&0&0&1
\end{pmatrix}.
\]

It has Smith invariants

\[
(1,1,1,1,0,0),
\]

and therefore

\[
\ker H\simeq\mathbb Z^2,
\qquad
\operatorname{coker}H\simeq\mathbb Z^2.
\]

Canonical representatives are

\[
e_{12|35}-e_{124|35}^{(124356)},
\qquad
e_{13|25}-e_{134|25}^{(134256)}
\]

in the kernel, while the unhit chamber directions are

\[
123456,qquad132456.
\]

All \(2^6=64\) independent orientation choices preserve rank four and the
four nonzero Smith invariants.

## Narrow conclusion

The common rank six observed in Entry 962 cannot be promoted through the
host-chamber map:

\[
\boxed{
\text{forgetting support reaches only a primitive rank-four sublattice of
the six-word chamber lattice.}
}
\]

This does not prove that the true de Rham--Betti comparison has rank four.
It proves that such a comparison is not contained in the host labels alone.
Any rank-six comparison must include additional source-derived period,
loading, or transition data that mixes corner occurrences with chambers not
hosting those corners.

No new carrier stratum is indicated.  The defect is in the presently absent
coefficient/comparison map.

## Next falsifier

Derive the twisted loading of the six chamber chains and its de Rham period
pairing.  In particular, determine whether transition across a common facet
supplies the two missing chamber directions \(123456\) and \(132456\), and
whether it separates each duplicated host pair.  Do not repair \(H\) by
adjoining arbitrary columns.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_corner_to_chamber.rs`;
- packet:
  `research/benincasa/string-six-point-corner-to-chamber.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_corner_to_chamber`;
- allocator claim:
  `seqclaim-315b717829e5e47d4dc8661d`.
- epistemic event:
  `ev-000000000580-0a9ef693-d561-4c4e-8c6e-be9da5d9de17`.
