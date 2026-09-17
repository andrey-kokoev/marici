# qRB microstep 88: full prime-readout extension

The finite prime channel is

$$
P_L(f)=
-\sum_{\log n\le2L}
\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle f,T_{\log n}f\rangle.
$$

For a polarized pair `f,g`, define the full candidate by the limit of finite cutoffs:

$$
P_\infty(f,g)=
-\lim_{L\to\infty}
\sum_{\log n\le2L}
\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle f,T_{\log n}g\rangle.
$$

The correct convergence test is not absolute summability of the coefficients alone. It is convergence of this translated-correlation series on the declared graph core, with the regulator and endpoint terms retained.

If the resulting bilinear form is bounded in the common logarithmic graph norm, it extends continuously to the wall completion. The compact identity fixes every finite cutoff term; only the infinite-tail bound remains.

Status: full prime-readout defined as a regulated limit; graph-bounded convergence remains to be proved.
