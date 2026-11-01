// Exact reference-A routing engine. Standalone: no rendering or dependencies.
export function createPortRouter(input) {
  const data=structuredClone(input),labels=['O','A','B','D','E'];
  const ensure=(ok,message)=>{if(!ok) throw new Error(message);};
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;};
  function Q(v) {
    if(v&&typeof v.n==='bigint') return v;
    const s=String(v);ensure(/^-?\d+(\/\d+)?$/.test(s),'Invalid exact rational');
    const [n,d='1']=s.split('/');return norm(BigInt(n),BigInt(d));
  }
  function norm(n,d) {ensure(d!==0n,'Zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
  const add=(a,b)=>{a=Q(a);b=Q(b);return norm(a.n*b.d+b.n*a.d,a.d*b.d);};
  const mul=(a,b)=>{a=Q(a);b=Q(b);return norm(a.n*b.n,a.d*b.d);};
  const neg=a=>mul(-1,a),sub=(a,b)=>add(a,neg(b));
  const div=(a,b)=>{a=Q(a);b=Q(b);return norm(a.n*b.d,a.d*b.n);};
  const serial=x=>Array.isArray(x)?x.map(serial):(()=>{const q=Q(x);return q.d===1n?String(q.n):`${q.n}/${q.d}`;})();
  const eq=(a,b)=>JSON.stringify(serial(a))===JSON.stringify(serial(b));
  const parse=x=>Array.isArray(x)?x.map(parse):Q(x);
  const identity=()=>parse([[[1,0],[0,1]],[0,0]]);
  const mv=(A,v)=>A.map(row=>add(mul(row[0],v[0]),mul(row[1],v[1])));
  function compose([A,b],[C,d]) {
    return [A.map(row=>[0,1].map(j=>add(mul(row[0],C[0][j]),mul(row[1],C[1][j])))),mv(A,d).map((v,i)=>add(v,b[i]))];
  }
  function inverse([A,b]) {
    const det=sub(mul(A[0][0],A[1][1]),mul(A[0][1],A[1][0]));
    const C=[[div(A[1][1],det),div(neg(A[0][1]),det)],[div(neg(A[1][0]),det),div(A[0][0],det)]];
    return [C,mv(C,b).map(neg)];
  }
  const apply=(f,v)=>[...mv(f[0],v).map((x,i)=>add(x,f[1][i])),...v.slice(2).map(Q)];
  function seamReflection(edge) {
    const [p,r]=parse(edge),t=r.map((v,i)=>sub(v,p[i])),n=[neg(t[1]),t[0]];
    const m=mv(parse([['4/3','-2/3'],['-2/3','4/3']]),n);
    const dot=(a,b)=>add(mul(a[0],b[0]),mul(a[1],b[1]));
    const den=dot(n,m),height=dot(n,p);
    return [[0,1].map(i=>[0,1].map(j=>sub(i===j?1:0,div(mul(2,mul(m[i],n[j])),den)))),m.map(x=>div(mul(2,mul(x,height)),den))];
  }
  const cells=new Map(data.cells.map(c=>[c.id,c])),histories=new Map(data.histories.map(h=>[h.bits,h]));
  ensure(cells.size===14&&histories.size===16,'Unexpected reference geometry');
  const frames=new Map(data.cells.map(c=>[c.id,parse(c.transform)]));
  const ports=new Map(data.ports.map(p=>[p.id,p]));
  const neighbors=new Map(data.cells.map(c=>[c.id,[]])),seams=new Map();
  const key=(a,b)=>[a,b].sort((a,b)=>a-b).join('-');
  const port=(a,b)=>{
    const matches=data.ports.filter(p=>p.cell===a&&p.neighbor===b);
    ensure(matches.length===1,`No unique paired port C${a} → C${b}`);
    return {...matches[0],histories:[...cells.get(a).histories]};
  };
  ensure(ports.size===42&&data.ports.filter(p=>p.external).length===14,'Port census mismatch');
  for(const h of data.histories) {
    ensure(/^[01]{4}$/.test(h.bits),'Invalid four-bit history');
    ensure(eq(parse(h.transform),frames.get(h.cell)),'History frame mismatch');
  }
  const seedLifts={
    centered:[[0,0,0,0],[1,0,0,0],[0,1,0,0],['1/3','1/3',1,0],['1/3','1/3',0,1]],
    asymmetric:[[0,0,0,0],[1,0,0,0],[0,1,0,0],['1/4','1/4',1,0],['1/2','1/4',0,1]],
  };
  for(const c of data.cells) {
    ensure(JSON.stringify([...c.histories].sort())===JSON.stringify(data.histories.filter(h=>h.cell===c.id).map(h=>h.bits).sort()),'Lost cell histories');
    const local=data.ports.filter(p=>p.cell===c.id);
    ensure(local.length===3,'Cell needs three OAB ports');
    ensure(new Set(local.map(p=>p.edge_labels.map(l=>labels.indexOf(l)).sort().join('-'))).size===3,'Repeated local edge port');
    for(const p of local) ensure(p.external===(p.neighbor===null),'Invalid external port status');
    for(const kind of ['centered','asymmetric']) {
      const vs=parse(c.vertices4[kind]);ensure(vs.length===5&&vs.every(v=>v.length===4),'Missing complete simplex');
      ensure(eq(vs,seedLifts[kind].map(v=>apply(frames.get(c.id),parse(v)))),'Full simplex disagrees with declared lift');
      ensure(eq(vs.slice(0,3).map(v=>v.slice(0,2)),c.triangle),'Triangle/frame mismatch');
      const mean=[0,1,2,3].map(j=>div(vs.reduce((s,v)=>add(s,v[j]),Q(0)),5));
      ensure(eq(mean,c.centers4[kind]),'Incorrect full-simplex barycenter');
      for(const p of local) {
        ensure(p.edge_labels.length===2&&p.edge_labels.every(l=>['O','A','B'].includes(l)),'Invalid seam labels');
        const [a,b]=p.edge_labels.map(l=>vs[labels.indexOf(l)]);
        ensure(eq(a.map((v,i)=>div(add(v,b[i]),2)),p.midpoint4),'Port midpoint mismatch');
      }
    }
  }
  for(const s of data.seams) {
    const [a,b]=s.cells;ensure(!seams.has(key(a,b)),'Duplicate seam');
    const S=seamReflection(s.edge);
    ensure(eq(S,s.reflection),'Seam reflection disagrees with edge geometry');
    ensure(eq(S,compose(frames.get(b),inverse(frames.get(a)))),'Seam/frame mismatch');
    ensure(eq(compose(S,S),identity()),'Seam is not involutive');
    ensure(JSON.stringify(s.label_permutation)==='[0,1,2,3,4]','Full label permutation mismatch');
    const pa=port(a,b),pb=port(b,a);
    ensure(!pa.external&&!pb.external&&eq(pa.midpoint4,pb.midpoint4)&&eq(pa.midpoint4,s.midpoint4),'Unpaired seam ports');
    ensure(eq(apply(S,parse(pa.midpoint4)),pa.midpoint4),'Seam moves its port');
    for(const kind of ['centered','asymmetric']) for(let i=0;i<5;i++)
      ensure(eq(apply(S,parse(cells.get(a).vertices4[kind][i])),cells.get(b).vertices4[kind][i]),'Full ordered vertex mismatch');
    seams.set(key(a,b),{...s,map:S});neighbors.get(a).push(b);neighbors.get(b).push(a);
  }
  ensure(seams.size===14,'Seam census mismatch');
  function paths(a,b,seen=[]) {
    const path=[...seen,a];if(a===b) return [path];
    return neighbors.get(a).filter(n=>!path.includes(n)).flatMap(n=>paths(n,b,path));
  }
  function transport(path) {
    let f=identity();
    for(let i=1;i<path.length;i++) {
      const seam=seams.get(key(path[i-1],path[i]));ensure(seam,'Route crosses a non-seam');
      f=compose(seam.map,f);
    }
    return f;
  }
  ensure(data.routes.length===32,'Request census mismatch');
  ensure(new Set(data.routes.map(r=>[r.history_from,r.history_to].sort().join('-'))).size===32,'Duplicate history request');
  let alternatives=0,traversals=0;
  for(const [index,r] of data.routes.entries()) {
    ensure(r.id===index,'Request ID mismatch');
    ensure(histories.get(r.history_from)?.cell===r.source&&histories.get(r.history_to)?.cell===r.target,'Request endpoints mismatch');
    ensure([...r.history_from].filter((b,i)=>b!==r.history_to[i]).length===1,'Request is not a one-bit comparison');
    const actual=paths(r.source,r.target),normalize=ps=>ps.map(p=>JSON.stringify(p)).sort();
    ensure(JSON.stringify(normalize(actual))===JSON.stringify(normalize(r.all_simple_paths)),'Route alternatives mismatch');
    const minimum=Math.min(...actual.map(p=>p.length));
    ensure(actual.filter(p=>p.length===minimum).length===1,'Shortest route is not unique');
    ensure(r.all_simple_paths[0].length===minimum&&r.length===minimum-1,'Selected route is not shortest');
    for(const path of actual) ensure(eq(transport(path),r.transport),'Route transport mismatch');
    alternatives+=actual.length;traversals+=minimum-1;
  }
  function packet({requestId=0,routeIndex=0,reverse=false,position=0,lift='centered',payload={}}={}) {
    ensure(Number.isInteger(requestId)&&requestId>=0&&requestId<data.routes.length,'Unknown request');
    const request=data.routes[requestId];
    ensure(Number.isInteger(routeIndex)&&routeIndex>=0&&routeIndex<request.all_simple_paths.length,'Unknown route');
    ensure(['centered','asymmetric'].includes(lift),'Unknown lift');
    ensure(typeof reverse==='boolean','Invalid reversal');
    const path=[...request.all_simple_paths[routeIndex]];if(reverse) path.reverse();
    ensure(Number.isInteger(position)&&position>=0&&position<path.length,'Invalid route position');
    const prefix=path.slice(0,position+1),current=path[position],source=path[0];
    const f=transport(prefix),endpoint=transport(path);
    const expected=compose(frames.get(current),inverse(frames.get(source)));
    ensure(eq(f,expected),'Prefix transport mismatch');
    const slots=labels.map((label,i)=>{
      const coordinates=serial(apply(f,parse(cells.get(source).vertices4[lift][i])));
      ensure(eq(coordinates,cells.get(current).vertices4[lift][i]),'Payload coordinate mismatch');
      return {label,value:structuredClone(Object.hasOwn(payload,label)?payload[label]:null),coordinates};
    });
    const ingress=position?port(current,path[position-1]):null;
    const egress=position+1<path.length?port(current,path[position+1]):null;
    const paired=egress?port(path[position+1],current):null;
    const polyline4=[cells.get(source).centers4[lift]];
    for(let i=1;i<path.length;i++) polyline4.push(seams.get(key(path[i-1],path[i])).midpoint4,cells.get(path[i]).centers4[lift]);
    return structuredClone({requestId,historyFrom:reverse?request.history_to:request.history_from,
      historyTo:reverse?request.history_from:request.history_to,routeIndex,reverse,lift,path,position,
      visitedRoute:prefix,currentCell:current,cellHistories:cells.get(current).histories,
      ingress,egress,pairedEgress:paired,completed:position===path.length-1,
      sourceFrame:serial(frames.get(source)),currentFrame:serial(frames.get(current)),
      transport:serial(f),endpointTransport:serial(endpoint),slots,polyline4});
  }
  return {packet,audit:Object.freeze({requests:data.routes.length,cells:cells.size,seams:seams.size,
    ports:ports.size,externalPorts:14,simpleRoutes:alternatives,shortestTraversals:traversals}),
    inverse:map=>serial(inverse(parse(map)))};
}
