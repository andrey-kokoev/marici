// Exact integer interpretation of the local translated P/PN template.
// Not a claim that the Number-valued sector API accepts arbitrary integers.
const need=(c,m)=>{if(!c)throw new RangeError(m);};
const dec=s=>{need(typeof s==='string'&&/^-?(0|[1-9][0-9]*)$/.test(s),'exact decimal required');return BigInt(s);};
const key=p=>p.map(String).join(','),vec=s=>s.split(',').map(dec),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const set=a=>[...a].sort(),plus=(a,b)=>a.map((x,i)=>x+b[i]);
export const ID=[0,1,2,3,4],PN=[3,1,2,0,4];
const root={C0:[1n,0n,0n,0n],M0:[0n,1n,0n,0n],C1:[0n,0n,1n,0n],M1:[0n,0n,0n,1n],C2:[-1n,1n,0n,1n]};
export function inversePoint(point){const [x,y,z]=point.map(dec);need((x+y+z)%2n===0n,'not D3');return [-(x+y+z)/2n,(x+y-z)/2n,(x+z-y)/2n,(y+z-x)/2n];}
export function exactContext(point){
 need(Array.isArray(point)&&point.length===3,'point shape');const d=inversePoint(point),references=Object.fromEntries(Object.entries(root).map(([n,v])=>[n,key(plus(d,v))]));
 const namespace='d3:'+point.join(':');
 return {schema:'marici.exact-translated-local-PN.v1',namespace,point:[...point],shift:d.map(String),references,
  source:{id:namespace+'/P',kind:'proton',body:['C0','M0','C1','M1'].map(n=>references[n]),origin:'0',permutation:[...ID]},
  target:{id:namespace+'/N',kind:'neutron',body:['M0','C1','M1','C2'].map(n=>references[n]),origin:'0',permutation:[...PN]},
  transfer:{id:namespace+'/PN',kind:'PN',source:namespace+'/P',target:namespace+'/N',phaseDelta:'0',permutation:[...PN],face:['M0','C1','M1'].map(n=>references[n])}};
}
export function observedPoint(c){const v=vec(c.references.C0);return [v[1]+v[2],v[1]+v[3],v[2]+v[3]].map(String);}
export function verifyContext(c){need(same(c,exactContext(c.point)),'bad exact full context');need(same(observedPoint(c),c.point),'point binding');return true;}
export function prepareExact(radius){
 const n=dec(radius);need(n>=0n,'negative radius');const rows=[];
 for(let x=-n;x<=n;x++)for(let y=-n;y<=n;y++)for(let z=-n;z<=n;z++)if((x+y+z)%2n===0n)rows.push(exactContext([x,y,z].map(String)));
 return {schema:'marici.exact-prepared-region.v1',radius,rows};
}
export function verifyRegion(region){need(same(region,prepareExact(region.radius)),'incomplete or changed exact region');return true;}
export function queryExact(args){
 need(Object.keys(args).sort().join(',')==='colors,letters,palette,region,word','unexpected answer parameter');const {letters,region,word,colors,palette}=args;
 need(letters.length>0&&colors.length===region.rows.length,'input shape');
 need(Number.isSafeInteger(palette)&&palette>0&&colors.every(c=>Number.isSafeInteger(c)&&c>=0&&c<palette),'palette');
 letters.forEach(inversePoint);verifyRegion(region);
 const p=word.reduce((a,i)=>{need(Number.isSafeInteger(i)&&i>=0&&i<letters.length,'word label');return plus(a,letters[i].map(dec));},[0n,0n,0n]);
 const i=region.rows.findIndex(c=>same(c.point,p.map(String)));
 return i<0?{kind:'refused',point:p.map(String),word:[...word],absence:region.rows.map(c=>!same(c.point,p.map(String)))}:
  {kind:'selected',point:p.map(String),word:[...word],context:region.rows[i],color:colors[i],index:i};
}
export function bindLegacy(exact,old){
 verifyContext(exact);const a=exact.references;need(same(old.point.map(String),exact.point),'legacy point');
 const P=old.packet,N=old.PN.target,op=old.PN.operation;
 for(const n of Object.keys(root))need(P.chart.aliases[n]===a[n]&&N.chart.aliases[n]===a[n],'legacy outside reference');
 need(same(set(P.cell.vertices),set(exact.source.body))&&same(set(N.cell.vertices),set(exact.target.body)),'legacy primitive body');
 need(P.cell.owner.kind==='tetrahedron'&&N.cell.owner.kind==='octahedron'&&!P.cell.owner.inverted&&!N.cell.owner.inverted,'legacy owners');
 const d=exact.shift.map(dec),octOrigin=[d[0]-1n,...d.slice(1)];
 need(same(P.cell.owner.origin.map(String),d.map(String))&&same(N.cell.owner.origin.map(String),octOrigin.map(String)),'legacy owner origin');
 need(P.cell.key===set(exact.source.body).join('|')&&N.cell.key===set(exact.target.body).join('|'),'legacy cell keys');
 const units=[root.C0,root.M0,root.C1,root.M1],oct=[];
 for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)oct.push(key(plus(octOrigin,plus(units[i],units[j]))));
 need(P.cell.owner.key===P.cell.key&&N.cell.owner.key===set(oct).join('|'),'legacy full owner keys');
 need(P.chart.species==='proton'&&N.chart.species==='neutron','legacy chart species');
 for(const q of [P,N])need(q.chart.cell===q.cell.id&&q.chart.id==='chart-'+q.packet.chart&&q.packet.origin===0,'legacy scoped pointers');
 need(same(P.packet.permutation,ID)&&same(N.packet.permutation,PN)&&same(op.permutation,PN)&&op.phaseDelta===0&&op.kind==='PN','legacy complete permutation');
 need(op.source===P.packet.id&&op.target===N.packet.id&&same(set(op.face),set(exact.transfer.face)),'legacy PN pointers/face');
 for(const [frame,names,context,chart] of [[old.frame,['C0','M0','C1'],'M1',P.chart],[old.PN.targetFrame,['M0','C1','M1'],'C2',N.chart]]){
  need(same(frame.window.map(o=>o.vertex),names.map(n=>a[n]))&&frame.context.vertex===a[context],'legacy phase frame');
  for(const [o,n] of [...frame.window.map((o,i)=>[o,names[i]]),[frame.context,context]])need(o.role===n[0]&&o.index===Number(n.slice(1)),'legacy occurrence role/index');
  need(frame.id===chart.id+'@0'&&frame.species===chart.species,'legacy frame scope');
 }
 return {scope:exact.namespace,renaming:{cells:[[P.cell.id,exact.source.id],[N.cell.id,exact.target.id]],
  charts:[[P.chart.id,exact.source.id+'/chart'],[N.chart.id,exact.target.id+'/chart']],
  packets:[[P.packet.id,exact.source.id+'/packet'],[N.packet.id,exact.target.id+'/packet']],operations:[[op.id,exact.transfer.id]]},
  original:structuredClone(old),exact:structuredClone(exact),wholeOriginalRetained:true,
  comparison:'full local PN reference/geometry renaming; not identity of seed policies or complete caches'};
}
