# Many-many corrected-frame refinement gate

Write the corrected frame as

$$
T_\theta=SH,
\qquad
S=\operatorname{diag}(-2,1).
$$

For a refinement map `R`, wall-frame naturality requires

$$
T_\theta R=R^{\rm wall}T_\theta,
$$

hence

$$
R^{\rm wall}=T_\theta R T_\theta^{-1}.
$$

This formula defines the transported wall refinement whenever `R` preserves the common endpoint graph. A refinement that mixes even and odd endpoint coordinates acquires the corresponding factor-two conjugation.

For refinements diagonal in the wall/jump basis, `R_wall=diag(r_even,r_odd)`, the parity sectors remain separated. A refinement diagonal in the original endpoint basis generally mixes wall and jump after Hadamard transport. Mixed wall/jump refinements require an explicit source comparison cell.

Status: corrected-frame transport law fixed; parity-preserving naturality is immediate, mixed refinement remains a source gate.
