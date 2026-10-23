// Relative compiler: point/context coupling is a separate, explicit source gate.
const need=(c,m)=>{if(!c)throw new RangeError(m);};
const keys=(o,k)=>need(Object.keys(o).sort().join(',')===[...k].sort().join(','),'unexpected argument');
const point=p=>{need(Array.isArray(p)&&p.length===3,'point shape');return p.map(x=>{need(typeof x==='string'&&/^-?(0|[1-9][0-9]*)$/.test(x),'exact decimal coordinates required');return BigInt(x);});};
const str=p=>p.map(String),equal=(a,b)=>a.every((x,i)=>x===b[i]);
export function phi(letters,word){const points=letters.map(point);return str(word.reduce((p,i)=>{need(Number.isSafeInteger(i)&&i>=0&&i<points.length,'invalid letter');return p.map((x,j)=>x+points[i][j]);},[0n,0n,0n]));}
export function relativeQuery(args){
 keys(args,['letters','rows','word','colors','palette']);const {letters,rows,word,colors,palette}=args;
 need(Array.isArray(letters)&&letters.length>0&&Array.isArray(rows)&&Array.isArray(word),'task shape');
 need(Number.isSafeInteger(palette)&&palette>0&&colors.length===rows.length&&colors.every(c=>Number.isSafeInteger(c)&&c>=0&&c<palette),'invalid complete color array');
 const p=point(phi(letters,word)),found=rows.findIndex(r=>equal(point(r.declaredPoint),p));
 if(found<0)return {kind:'refused',word:[...word],point:str(p),absence:rows.map(r=>!equal(point(r.declaredPoint),p)),retainedRows:rows};
 return {kind:'selected',word:[...word],point:str(p),index:found,context:rows[found].context,color:colors[found],retainedRows:rows};
}
export function assertSectorBinding(rows){
 for(const row of rows){const b=row.context.frame.window[0].vertex.split(',').map(BigInt),actual=[b[1]+b[2],b[1]+b[3],b[2]+b[3]];
  need(equal(actual,point(row.declaredPoint)),'declared point not realized by supplied sector context');}
 return true;
}
export function substitute(letters,template,a){
 need(template.every(x=>x===null||(Number.isSafeInteger(x)&&x>=0&&x<letters.length)),'invalid template');
 const fixed=phi(letters,template.filter(x=>x!==null)),m=template.filter(x=>x===null).length,s=point(letters[a]);
 const expected=point(fixed).map((x,j)=>x+BigInt(m)*s[j]);
 return {word:template.map(x=>x===null?a:x),base:fixed,multiplicity:m,point:str(expected)};
}
