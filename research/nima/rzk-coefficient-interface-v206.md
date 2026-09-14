# v206: local physical normal Gysin has unit residue normalization

The physical normal germ already has a source formula. With `lambda=2 pi i alphaPrime`,

`q(X)=exp(lambda X)` and `kappa_norm(X)=lambda/(exp(lambda X)-1)=U(X)^-1/X`,

where `U(0)=1`. For every coefficient `f` regular in this channel,

`Res_X=0(f(X) kappa_norm(X) dX)=f(0)`.

Moreover `kappa_norm(X)dX=dlog(q(X)-1)-lambda dX`, so the physical loaded pole and logarithmic normal generator define the same residue class; their difference is regular. This gives the selected local normal Gysin comparison with coefficient one. Multiplying by the raw normal factor `(q-1)` instead cancels the pole and gives residue zero, so that rival normalization is excluded.

Consequently the trace formula from v205 acquires no additional local normal Jacobian: on a selected regular coefficient with detector coordinates `(a,b,c)`, the normal residue preserves `-beta(a+(b+c))`.

This is a local normal-line theorem, not the missing spatial map from the normalization source into the K6 supported complex. That map remains necessary to prove that the selected physical Gysin class has coordinates `(a,b,c)`.
