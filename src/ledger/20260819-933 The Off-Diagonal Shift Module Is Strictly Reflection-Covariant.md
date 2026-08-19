# 933 — The Off-Diagonal Shift Module Is Strictly Reflection-Covariant

## Reflection-label correction

Entry 932 exposed a notation collision rather than a geometric obstruction.
Two distinct source reflections had both been denoted \((24)\):

- Entry 914's maximal-flag reflection is
  \[
  \tau_{\rm max}=(24):
  (s_{14},s_{23},s_{235})
  \mapsto
  (s_{12},s_{34},s_{345});
  \]
- Entry 920's off-diagonal exchange must instead be
  \[
  \tau_{\rm off}=(23),
  \]
  because it fixes \(s_{14}\) and \(s_{235}\) while exchanging
  \(s_{35}\leftrightarrow s_{25}\).

Entry 920 and its durable packet are corrected accordingly. Entry 932's
reflection type gate is withdrawn; its commuting-shift calculation remains
valid.

## Tangential action

The correct off-diagonal reflection acts internally on the tangential
monodromy coordinates:

\[
A_2\leftrightarrow A_3,
\qquad
B_{24}\leftrightarrow B_{34}.
\]

Hence the specialized slice

\[
\{A_2,A_3,B_{24},B_{34}\}
\]

is preserved.

On the ordered dense word basis

\[
(234,243,324,342,423,432),
\]

the induced permutation is

\[
\pi_{23}=(0\ 2)(1\ 3)(4\ 5),
\]

serialized as

\[
(2,3,0,1,5,4).
\]

## Exact covariance

Apply the simultaneous variable exchanges to the exact source row \(r\),
then apply the word permutation. Symbolic reduction gives

\[
\boxed{
\tau_{\rm off}(r)=\pi_{23}r.
}
\]

The two pair shifts are exchanged:

\[
\tau_{\rm off}T_{24}\tau_{\rm off}^{-1}=T_{34},
\qquad
\tau_{\rm off}T_{34}\tau_{\rm off}^{-1}=T_{24}.
\]

Together with Entry 932's strict commutator,

\[
[T_{24},T_{34}]=0,
\]

this proves that the four-character source closure is covariant under the
semidirect action

\[
(\mathbf Z/2)^2\rtimes\langle\tau_{\rm off}\rangle.
\]

The character supports transform as expected:

\[
(-,+)\leftrightarrow(+,-),
\qquad
(+,+)\mapsto(+,+),
\qquad
(-,-)\mapsto(-,-).
\]

## Narrow result

\[
\boxed{
\text{the rank-eight normal-symbol shift module is strictly
off-diagonal-reflection covariant}.
}
\]

No extra unit, associator, or carrier incidence is required. The apparent
failure in Entry 932 was entirely due to conflating two occurrence maps.

## Next falsifier

Complete the cyclic occurrence action on the shift module. Transport the four
character supports through the three maximal-flag charts and test whether the
signed cyclic composition is identity. A nontrivial return automorphism would
be the first genuine discrete coefficient holonomy; identity would establish
a global finite-difference local system on this occurrence orbit.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_shift_coherence.rs;
- packet:
  research/benincasa/string-six-point-shift-coherence.json;
- corrected reflection checker:
  research/benincasa/marici-gm/src/bin/string_six_point_rees_reflection.rs;
- allocator claim:
  seqclaim-2e68dc911910007c6a9e4db6.
- epistemic event:
  ev-000000000550-110cfa8b-4578-4564-97c9-1f62eed441bd.
