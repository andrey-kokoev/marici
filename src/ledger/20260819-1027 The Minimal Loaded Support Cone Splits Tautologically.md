# 1027 — The Minimal Loaded Support Cone Splits Tautologically

## The full corner-complex lift is impossible

Let \(K_{\rm cor}\) be Entry 962's rank-six kernel and let

\[
C:K_{\rm cor}\longrightarrow V_{\rm hex}
\]

be Entry 967's generically invertible occurrence comparison. Any lift from
the full \(18\to12\) corner complex into the twisted hexagon complex would
send source cycles to target cycles. Entry 1025 gives

\[
\operatorname{rank}(\delta C)=5.
\]

Therefore such a chain map cannot restrict to \(C\) on \(K_{\rm cor}\).

## Minimal supported cone

The smallest algebraic target that forces the six graph classes to close is

\[
V_{\rm hex}\oplus K_{\rm cor}
\xrightarrow{D}
E_{\rm hex},
\qquad
D=(\delta,-\delta C).
\]

Indeed,

\[
D(Ck,k)=0
\]

for every \(k\in K_{\rm cor}\).

This construction looks like the desired support-sensitive repair, but its
extension content must be tested before interpretation.

## Exact triangular splitting

Apply the invertible triangular change of frame

\[
T(v,k)=(v-Ck,k).
\]

Then

\[
D(v,k)=\delta(v-Ck),
\]

and hence

\[
\boxed{
DT^{-1}=(\delta,0).
}
\]

Thus the cone is canonically isomorphic, once \(C\) is fixed, to the direct
sum of the ordinary twisted hexagon complex and six zero-differential
support generators.

Generically,

\[
\dim H^0=6+1=7,
\qquad
\dim H^1=1,
\]

with

\[
H^0\simeq K_{\rm cor}\oplus\ker\delta.
\]

## Narrow conclusion

\[
\boxed{
\text{the minimal cone built only from }\delta C\text{ is tautologically
split and supplies no comparison coherence.}
}
\]

It packages the six occurrence classes but does not explain their coupling
to chamber transport. Interpreting its zero-differential summand physically
would be exactly the prohibited operation of adjoining support generators
solely to kill an obstruction.

## Revised frontier

The required lower cell must be independently source-derived and cannot be
the formal graph cone of \(C\). The finite search is now:

1. return to the two-step pivot-transition path of Entry 966;
2. retain its intermediate pivot endpoint rather than only the composite
   coefficient \(M_AM_B-1\);
3. assemble the resulting bar/group-cohomology differential on all six
   occurrences;
4. test whether its comparison to the hexagon produces \(\delta C\) by a
   native homotopy.

Only that pre-existing path homotopy can turn the rank-five boundary into
derived coherence without a post hoc support summand.

## Durable evidence

- packet:
  'research/benincasa/string-six-point-minimal-loaded-support-cone.json';
- allocator claim:
  'seqclaim-652e82e960ddead1e189da72'.
- epistemic event:
  'ev-000000000645-11a8a14d-ed40-43e5-b051-2ca1de89e489'.
