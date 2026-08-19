# 1024 — Only One Loaded Corner Combination Is a Hexagon Cellular Cocycle

## Reintroducing the canonical source complex

Entry 1023 observes that Entry 967 does not itself declare a source
differential. Entry 962 does provide a canonical complex before passing to
its six corner-kernel classes:

\[
\bigoplus_{r=1}^6\mathbb Z^3
\xrightarrow{\oplus d_{\rm cor}}
\bigoplus_{r=1}^6\mathbb Z^2,
\qquad
\ker d_{\rm cor}
=
\mathbb Z\langle(1,1,1)\rangle.
\]

This permits a sharper test. If Entry 967's loaded matrix \(C\) were the
cohomological part of a chain map into the ordinary hexagon cellular
cochains, every image of a corner-kernel generator would have to be closed
under

\[
\delta_0:C^0_{\rm hex}\longrightarrow C^1_{\rm hex}.
\]

## Exact rank test

Away from the four source walls, Entry 967 gives

\[
\operatorname{rank}C=6.
\]

The connected hexagon has

\[
\operatorname{rank}\delta_0=5,
\qquad
\ker\delta_0
=
\mathbb K\langle(1,1,1,1,1,1)\rangle.
\]

Consequently

\[
\boxed{
\operatorname{rank}(\delta_0C)=5.
}
\]

In particular, none of the six individual loaded columns is closed.
The entire closed preimage is one-dimensional. With Entry 967's conventions,
a generator is

\[
\boxed{
\left(
\frac2{f_1},
-\frac1{f_2},
\frac1{f_2},
\frac2{f_3},
-\frac1{f_4},
\frac1{f_4}
\right)^T,
}
\]

and \(C\) sends it to the constant vertex cocycle
\((1,1,1,1,1,1)^T\).

## Narrow conclusion

\[
\boxed{
\text{Entry 967 does not map the six corner-kernel classes into ordinary
hexagon cellular cohomology.}
}
\]

The obstruction has rank five, not merely one missing orientation sign.
Thus endpoint choices cannot repair it by a unimodular triangular gauge.

This preserves Entry 967's determinant theorem: \(C\) remains a valid
occurrence-module comparison. It also preserves Entry 1022's cellular
endomorphism cocycle. What fails is their direct cohomological composition.

## Surviving frontier

A bridge can exist only after one of the following is derived independently:

1. a twisted coefficient differential for which the six loaded images are
   cycles;
2. a mapping-cone target retaining the nonclosed cellular boundaries;
3. a chain-level lift from the full eighteen-to-twelve corner complex whose
   target includes additional degree-one comparison data.

The first finite falsifier is the native loaded hexagon differential. It must
be derived from the same Koba--Nielsen local system and tested on all six
columns. The ordinary incidence differential is now ruled out.

## Durable evidence

- packet:
  'research/benincasa/string-six-point-loaded-cocycle-rank.json';
- allocator claim:
  'seqclaim-273260c41f622b4415524412'.
- epistemic event:
  'ev-000000000643-f939b9cc-01a3-4881-af5c-1a64e560476d'.
