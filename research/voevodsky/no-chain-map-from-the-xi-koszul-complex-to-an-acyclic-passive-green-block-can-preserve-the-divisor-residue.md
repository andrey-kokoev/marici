# No chain map from the Xi Koszul complex to an acyclic passive Green block can preserve the divisor residue

Regard the strict passive block as the two-term complex

\[
C_P(s):\quad X_1\xrightarrow{P(s)}X_0.
\]

On the same-sign passive chart, `P(s)` is invertible, so `C_P(s)` is acyclic at
every parameter, including every Xi zero.

A chain map from

\[
K_\tau:\quad \mathcal L_\theta\xrightarrow{\tau}\mathcal O
\]

to `C_P` consists locally of maps `i,w` satisfying

\[
P(s)i(s)=w(s)\tau(s).
\]

At a zero `s_0` of `tau`, invertibility gives

\[
i(s_0)=0.
\]

More invariantly, the induced map on fibre cohomology has target

\[
H^*(C_P(s_0))=0,
\]

so it annihilates both Koszul residue lines.  It cannot preserve local module
length, and its mapping cone cannot be acyclic as a divisor-preserving
comparison.

This is not repaired by choosing a modified history vector: as long as the
target differential remains the same invertible passive block, every target
cycle is exact and no nonzero residue class exists.  A successful target must
change the differential or enlarge it by a source-derived finite defect whose
cohomology appears exactly on the Xi divisor.

Therefore the next constructor is not another map into the strict passive
block.  It is a genuinely non-acyclic stratified Green complex with a finite
Xi-sensitive defect module, followed by a chain map from `K_tau`.
