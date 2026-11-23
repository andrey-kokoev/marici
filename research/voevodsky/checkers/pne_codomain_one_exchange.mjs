// Typed incidence, native words, metric realizations: test separately. No added closing edge.
import {routes,points as radial} from '../../strominger/demos/particle-overlap-tetrahedron/model.mjs';
import {trial} from '../../strominger/demos/particle-overlap-tetrahedron/carrier.mjs';
import {writeFileSync} from 'node:fs';
const [p,n,e]=routes.map(x=>x.nodes),v=[...new Set([...p,...n,...e])],sort=a=>[...a].sort().join('|'),eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b),perms=a=>a.length?a.flatMap(x=>perms(a.filter(y=>x!==y)).map(b=>[x,...b])):[[]];
const laws=perms(v).map(w=>Object.fromEntries(v.map((x,i)=>[x,w[i]]))).filter(f=>v.every(x=>x[0]===f[x][0])&&[[p,e],[e,p],[n,n]].every(([a,b])=>sort(a.map(x=>f[x]))===sort(b)));
if(laws.length!==1)throw Error('not uniquely induced');const f=laws[0],F=a=>a.map(x=>f[x]);
const audit=pts=>{const d=(a,b)=>pts[a].reduce((s,x,j)=>s+(x-pts[b][j])**2,0);return {P_pair_squared_lengths:[d(p[0],p[1]),d(p[1],p[2]),d(p[0],p[2])],E_corresponding_squared_lengths:[d(f[p[0]],f[p[1]]),d(f[p[1]],f[p[2]]),d(f[p[0]],f[p[2]])],preserves_all_distances:v.every(a=>v.every(b=>Math.abs(d(a,b)-d(f[a],f[b]))<1e-9))}};
const rel=(c,m)=>[p,e].filter(w=>w.includes(c)&&w.includes(m)).map(w=>w.find(x=>x[0]==='C'&&x!==c));const o={exchange:f,P_image:F(p),E_word:e,N_image:F(n),swaps_ordered_words:eq(F(p),e),P_image_cyclic_shift_of_E:eq(F(p),[e[2],e[0],e[1]]),other_C_readouts:[[p[0],p[1]],[e[2],e[0]],[e[1],e[0]]].map(([c,m])=>[c,m,rel(c,m)]),original_radial:audit(radial),unfolded:audit(trial.points),P_continuation_image:f[trial.bodies[0].continuation],E_continuation:trial.bodies[2].continuation};console.log(o);writeFileSync(new URL('../results/pne_codomain_one_exchange.json',import.meta.url),JSON.stringify(o,null,2)+'\n');
