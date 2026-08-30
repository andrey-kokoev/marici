# The five-wall observer is not automatically the boundary-triple space

The finite-boundary reduction needs one rank correction. An ordinary boundary triple is not free to inherit every coefficient observer coordinate. Its boundary dimension is fixed by the deficiency indices of the closed symmetric history operator.

Let
\[
S_{\min}\subset S_{\max}=S_{\min}^{*}
\]
be the minimal and maximal oriented history operators. If the local history is scalar and first order, one expects one deficiency coordinate per orientation; reciprocal doubling therefore gives a trace space \(\mathcal B_{\mathrm{hist}}\) of rank at most two. By contrast, the coefficient boundary quotient
\[
\mathcal W=\operatorname{span}\{1,\delta_0,K,V\}
\]
has rank four. These spaces cannot be identified merely because both are called boundary data.

The correct architecture is
\[
\mathcal W
\xrightarrow{\;\mathcal T\;}
\mathcal B_{\mathrm{hist}}
\xrightarrow{\;\gamma(s)\;}
\ker(S_{\max}-s),
\]
where \(\mathcal T\) is the source-derived coefficient-to-trace incidence. The full four-port packet remains a faithful exterior observer, while only the reachable quotient
\[
\mathcal W_{\mathrm{tr}}
=
\mathcal W/\ker\mathcal T
\cong
\operatorname{ran}\mathcal T
\]
can parameterize analytic extensions.

For an ordinary boundary triple
\[
(\mathcal B_{\mathrm{hist}},\Gamma_0,\Gamma_1),
\]
the Green identity is
\[
\langle S_{\max}f,g\rangle-\langle f,S_{\max}g\rangle
=
\langle\Gamma_1f,\Gamma_0g\rangle
-
\langle\Gamma_0f,\Gamma_1g\rangle,
\]
and the joint trace map must be surjective onto the declared analytic boundary space. If the source maps from \(\mathcal W\) are not surjective, or if the trace is only defined on a restricted core, the honest object is a quasi-boundary triple or a linear boundary relation.

The Weyl collision must consequently be formed on the reachable trace space:
\[
(\Theta(s)-M(s))b=0,
\qquad
b\in\mathcal B_{\mathrm{hist}},
\]
not on all five-wall coordinates. The exterior observer then enters through \(\mathcal T\) and its transpose. Coordinates in \(\ker\mathcal T\) may still detect coefficient phenomena, but they are not extension parameters and must not contribute artificial determinant factors.

The next rank audit is finite:

1. freeze \(S_{\min}\) and \(S_{\max}\);
2. compute their deficiency indices;
3. construct the actual trace maps \(\Gamma_0,\Gamma_1\);
4. derive \(\mathcal T:\mathcal W\to\mathcal B_{\mathrm{hist}}\);
5. compute \(\ker\mathcal T\), \(\operatorname{ran}\mathcal T\), and radical compatibility;
6. construct \(M(s)\) only on the reachable trace quotient;
7. derive the arithmetic boundary relation \(\Theta(s)\) there;
8. prove separately that the full four-port observer factors faithfully through the resulting spectral packet.

The smallest hostile stuffs four coefficient ports into a rank-two deficiency space. The resulting determinant has two spurious directions: they either create artificial zeros or hide as a radical removed only after the claimed spectral identity.

Thus the corrected reduction is:

\[
\text{full coefficient observer}
\to
\text{source trace incidence}
\to
\text{reachable deficiency quotient}
\to
\text{Weyl pencil}
\to
\text{zeta identification}.
\]

This preserves the finite Birman--Schwinger strategy while preventing observer rank from being mistaken for extension rank.
