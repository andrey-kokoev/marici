# Green observability cannot come from the theta compact channel

On the Euler-normalized prime basis, the theta sampling operator is diagonal,

$$
S_\theta e_p=\eta_pe_p,
\qquad \eta_p\to0,
$$

and is compact. Let `u_p` be normalized Euler basis vectors. Then

$$
\|u_p\|=1,
\qquad
\|S_\theta u_p\|\to0.
$$

Consequently no Green form built only from the theta sampling channel and bounded postprocessing can satisfy

$$
\|v\|^2\le C b[v,v]
$$

on the completed Euler source. Indeed, for `b[v,v]=||TS_theta v||^2` with bounded `T`, one has `b[u_p,u_p]->0`.

The pointed one-leg arithmetic form is

$$
f(v,v)=\|\Phi\|^2\|v\|^2.
$$

Therefore domination

$$
f(v,v)\le C b(v,v)
$$

requires a complementary noncompact observer in the complete Green packet. The candidate blocks are the retained tail/seam history, wall/jump endpoint channel, and reciprocal arithmetic incidence; compact theta/linking corrections alone cannot provide the essential lower margin.

For a decomposition

$$
b(v,v)=\|Av\|^2+\|Dv\|^2,
$$

where `A` is the compact theta channel, observability is equivalent to a joint lower frame bound

$$
\|Av\|^2+\|Dv\|^2\ge\delta^2\|v\|^2.
$$

In particular, every normalized weakly null sequence with `Av_n->0` must satisfy

$$
\liminf_n\|Dv_n\|>0.
$$

Status: theta-only observability ruled out; the next source test is a lower frame bound for the complementary tail/seam, wall, and reciprocal observer family on theta-invisible prime sequences.
