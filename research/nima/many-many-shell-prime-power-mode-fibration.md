# Many-many shell / prime-power mode fibration

Use a two-level mode assignment. The consecutive-prime shell index is `j`, with shell

$$
S_j=[\log p_j,\log p_{j+1}].
$$

Assign disjoint base bands `Omega_j=[j,j+1)` to shells and explicit disjoint subbands

$$
\Omega_{j,k}=\left[j+2^{-k},\ j+2^{-k}+2^{-(k+1)}\right)
$$

inside `Omega_j` to prime-power grade `k`: 

$$
\Omega_{j,k}\subset\Omega_j,
\qquad
\Omega_{j,k}\cap\Omega_{j',k'}=\varnothing
\text{ for }(j,k)\ne(j',k').
$$

The attenuation is shell-controlled with optional grade refinement:

$$
\widetilde V_{t,u}|_{\Omega_{j,k}}=t^j u^k I.
$$

Setting `u=1` recovers the countable shell coherencer. Varying `u` supplies a second calibrated probe for prime-power grade.

This fibration preserves both shell and grade labels and prevents the mode rank from being confused with the source attenuation exponent.

Status: two-level shell/grade mode architecture defined.
