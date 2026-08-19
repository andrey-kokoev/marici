# 1025 — Rank-One Koba--Nielsen Twisting Cannot Close the Six Loaded Columns

## Frozen twisted hexagon

Entry 1015 gives the unspecialized oriented chamber cycle

\[
(0,1,4,5,3,2)
\]

with edge transports

\[
(B_{34},B_{24},X,B_{34}^{-1},B_{24}^{-1},X^{-1}).
\]

Their product is one. Hence this rank-one Koba--Nielsen local system has
trivial total holonomy around the hexagon.

## Twisted cocycle rank

For any rank-one local system on a connected cycle, the vertex cocycle
equations have the form

\[
v_{k+1}=u_kv_k.
\]

All six values are determined by \(v_0\). A nonzero global section exists
exactly when

\[
\prod_{k=0}^{5}u_k=1.
\]

That condition holds here, so the twisted cellular differential satisfies

\[
\operatorname{rank}\delta^{\rm KN}_0=5,
\qquad
\dim\ker\delta^{\rm KN}_0=1.
\]

Since Entry 967's loaded comparison \(C\) is generically invertible,

\[
\boxed{
\dim\ker(\delta^{\rm KN}_0C)=1.
}
\]

This conclusion is independent of vertex-frame rescalings and orientation
conventions. Those operations conjugate the differential by invertible
diagonal matrices and cannot change its rank.

## Narrow conclusion

\[
\boxed{
\text{rank-one Koba--Nielsen twisting cannot make the six loaded corner
columns into independent hexagon cocycles.}
}
\]

Thus the first option left open by Entry 1024 is ruled out for an ordinary
rank-one local system on the connected chamber hexagon. The failure is
structural: a connected rank-one local system has at most one independent
vertex flat section, whereas the occurrence comparison has rank six.

This does not reject the Koba--Nielsen loading. It rejects placing the six
occurrence classes directly in its global vertex cohomology.

## Surviving coefficient architecture

The comparison must retain support before globalization. Viable typed targets
are now restricted to:

1. a constructible coefficient system with separate corner/transition
   costalks;
2. a mapping cone retaining the five nonzero boundary directions;
3. the full corner-to-edge comparison before taking cellular cohomology.

The highest-information finite test is the third: lift Entry 967 from the six
corner kernels to Entry 962's full \(18\to12\) complex and solve for an edge
map into the twisted hexagon complex. Its cone will determine whether the
five boundary directions are canonical support data or an obstruction.

## Durable evidence

- packet:
  'research/benincasa/string-six-point-rank-one-twisted-hexagon-gate.json';
- allocator claim:
  'seqclaim-bc35a25ca410424d4d1700ac'.
- epistemic event:
  'ev-000000000644-d94fad18-b294-43ac-a894-de4d99ed8128'.
