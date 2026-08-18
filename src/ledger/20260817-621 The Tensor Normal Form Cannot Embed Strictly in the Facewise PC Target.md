---
id: 415
date: 2026-08-17
title: The Tensor Normal Form Cannot Embed Strictly in the Facewise PC Target
---

# The Tensor Normal Form Cannot Embed Strictly in the Facewise PC Target

Entry 414 constructed the canonical 64-generator Tate--Cartier total normal
form. Its proposed next step—compare those generators directly with the
Entry-143 occurrence/Čech generators—is too literal. The two complexes have
different homological amplitudes.

For an Entry-105/143 generator \((S,H)\), with \(H\subseteq S\), the degree is
\[
\deg(S,H)=3-|S|+|H|.
\]
Since \(0\leq |H|\leq |S|\leq3\), every facewise PC generator lies in degrees
zero through three. Using the \(K_6\) face census
\[
(f_0,f_1,f_2,f_3)=(1,9,21,14)
\]
and summing \(\binom{|S|}{|H|}\) gives the established 215-generator profile
\[
\boxed{(14,63,93,45)}.
\]
Removing the two endpoint Boolean packets \((2,6,6,2)\) gives
\[
\boxed{\operatorname{rk}(F_K/F_V)=(12,57,87,43)}.
\]

By contrast, the independent Tate--Cartier tensor totalization has profile
\[
\boxed{(1,6,15,20,15,6,1)}
\]
in degrees zero through six. No global degree shift sends seven occupied
source degrees into the four occupied target degrees. Therefore:
\[
\boxed{\text{there is no degree-shifted strict embedding of the tensor
normal form into }F_K/F_V.}
\]

This is the same structural distinction first exposed locally in Entry 116.
The absolute PC rule \(H\subseteq S\) allows normal circles only on a face
that already contains the corresponding support. The independent Cartier
packet of Entry 115 instead carries external conormal directions even on
the endpoint faces that omit that support. Treating it as a literal tensor
subcomplex of the facewise target overcounts homological degree.

## Consequence

Entry 414 remains a valid normalized coefficient normal form, but it is not
a 64-generator subcomplex waiting to be found inside Entry 143. The desired
realization must transfer or collapse the external Cartier degrees through
the already constructed extraordinary Gysin maps:

1. use Entry 131's purity map to convert an external Cartier direction into
   a shifted facewise costalk;
2. use Entries 396--400's blowdown and exceptional interval to carry the
   connector and retained Tor suspension;
3. totalize only after these transfers, so the target remains in degrees
   zero through three.

An arbitrary chain map can of course kill the excess degrees because the
normal form is contractible. That does not meet the physical requirement:
the generic \(Q\) roof, endpoint residues, and first Cartier symbols must
remain nonzero. The next construction is therefore a transferred chain map,
not a strict inclusion or generatorwise identification.

The executable audit is
\`research/voevodsky/check_total_normal_form_target_amplitude_gate.py\`.
