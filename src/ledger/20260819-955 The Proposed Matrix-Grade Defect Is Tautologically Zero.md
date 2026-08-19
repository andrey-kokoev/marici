# 955 — The Proposed Matrix-Grade Defect Is Tautologically Zero

## Correction to Entry 954

Entry 954 proposed the ordered associated grade

\[
\operatorname{gr}_{s_{235}}
\operatorname{gr}_{s_{23}}
\operatorname{gr}_{s_{14}}
\bigl(K_{\rm block}T-K_{\rm dense}\bigr)
\]

as a possible coherence falsifier.

That expression cannot be a falsifier.  In the frozen construction of Entry
905,

\[
T=M_{\rm block}K_{\rm dense},
\qquad
K_{\rm block}=M_{\rm block}^{-1}.
\]

Consequently

\[
K_{\rm block}T-K_{\rm dense}=0
\]

identically on the generic common kinematic ring.  Every ordinary,
associated-graded, or Rees specialization of this difference is therefore
zero by construction.  A nonzero graded defect cannot occur there.

## Exact filtered transition already available

The nontrivial object is the filtered transition matrix itself, not the
defining comparison identity.  The exact Symbolica packet of Entries
912–921 gives:

1. for the ordered diagonal flag
   \[
   (s_{14},s_{23},s_{235})=0,
   \]
   the ordinary maximal-flag coefficient is zero;
2. the first \(s_{14}\)-normal grade is rank one;
3. off-diagonal orders are genuinely order-dependent and require a Rees
   ratio;
4. at the common deeper corner, the regularized diagonal and off-diagonal
   sections have target directions
   \[
   (1,-1),\qquad(0,1),
   \]
   with a generically nonzero \(2\times2\) minor.

Thus the filtered transition distinguishes two coefficient directions even
though its defining inverse identity remains exact.

## Narrow conclusion

\[
\boxed{
\text{Entry 954's matrix-grade defect is tautologically zero and is retired.}
}
\]

This does not repair the determinant mismatch of Entry 954, nor does it
produce a coherence map between the two filtered lines.  It restores the
correct type distinction:

\[
\text{exact basis-change identity}
\neq
\text{filtered transition/coherence datum}.
\]

## Revised falsifier

Do not grade the zero comparison identity.  Instead construct an
independently source-derived marked-incidence, localization, or Rees
specialization morphism whose domain and target are the two lines isolated in
Entry 921.  Compare that morphism with the six branch source columns.  If the
frozen source supplies no such map, retain the rank-two filtered direct sum;
do not manufacture a differential from the basis transition.

## Durable verification

- exact checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_three_normal.rs`;
- exact packet:
  `research/benincasa/string-six-point-three-normal.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_three_normal`;
- allocator claim:
  `seqclaim-3dd815cbe434f598fa5ea6ba`.
- epistemic event:
  `ev-000000000572-714a2055-b488-4436-b9c7-d74a63d4db62`.
