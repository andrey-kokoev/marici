// Read-only closure. Interfaces change local P orientation, not path length.
export function previewPathRules({bodies,wires,states,interfaces=[],extended=false,protonBranches=false,protonBranchNodes=null,enabledRules=null,sector='main',electronSelfRule=false}){
 const enabled=id=>enabledRules===null||enabledRules.includes(id);
 const roles=new Map(bodies.filter(b=>b.role).map(b=>[b.id,b.role])),initial=new Set(roles.keys());
 const outgoing=new Map(),across=new Map();
 for(const w of wires){if(!outgoing.has(w.from))outgoing.set(w.from,[]);outgoing.get(w.from).push(w);}
 for(const w of interfaces){if(!across.has(w.from))across.set(w.from,[]);across.get(w.from).push(w.to);}
 const known=new Map(),key=s=>JSON.stringify([s.node,s.front,s.suffix,s.pOrientation]);
 for(const s of states){const state={...s,pOrientation:s.pOrientation??(s.front==='−P'?-1:1)};known.set(key(state),state);}
 const blocked=new Set(),conflicts=new Map(),additions=new Map(),rounds=[],interfaceIdentifications=[];
 function accept(proposals,round){
  let changed=false;
  for(const [id,arrivals] of proposals){
   const choices=new Set(arrivals.map(a=>a.role));if(roles.has(id))choices.add(roles.get(id));
   if(choices.size!==1){blocked.add(id);conflicts.set(id,{id,existingRole:roles.get(id)??null,arrivals});continue;}
   if(!roles.has(id)){roles.set(id,arrivals[0].role);additions.set(id,{id,role:arrivals[0].role,round,arrivals:[]});}
   for(const a of arrivals){
    if(known.has(key(a)))continue;
    if(a.kind==='interface-identification')interfaceIdentifications.push(a);
    known.set(key(a),a);changed=true;if(additions.has(id))additions.get(id).arrivals.push(a);
   }
  }
  return changed;
 }
 function propose(map,to,a){if(blocked.has(to)||known.has(key(a)))return;if(!map.has(to))map.set(to,[]);map.get(to).push(a);}
 for(let round=0;;round++){
  // Saturate zero-cost identifications before considering any propagation move.
  for(;;){
   const proposals=new Map();
   for(const s of known.values())for(const to of across.get(s.node)??[]){
    const role=({P:'proton',N:'neutron',E:'electron'})[s.suffix.at(-1)];
    propose(proposals,to,{source:s.node,target:to,node:to,front:s.front,suffix:s.suffix,pOrientation:-s.pOrientation,role,kind:'interface-identification',rule:'Interface: +P ↔ −P; colour and path unchanged'});
   }
   if(!accept(proposals,round))break;
  }
  const proposals=new Map();
  for(const s of known.values())for(const w of outgoing.get(s.node)??[]){
   let role,rule;
   if(sector==='internal'&&electronSelfRule&&s.suffix.endsWith('E')&&w.direction==='E'){role='proton';rule='Internal: E + |E| → P';}
   else if(enabled('P-branch')&&protonBranches&&(!protonBranchNodes||protonBranchNodes.has(s.node))&&s.suffix.endsWith('P')&&['P','E','+N','−N'].includes(w.direction)){role=w.direction==='P'?'proton':w.direction==='E'?'electron':'neutron';rule='P + |x| → x';}
   else if(enabled('E-P')&&extended&&s.suffix.endsWith('E')&&w.direction==='P'){role='neutron';rule='E + |P| → N';}
   else if(enabled('N-nonP')&&extended&&s.suffix.endsWith('N')&&w.direction==='E'){role='electron';rule='N + |E| → E';}
   else if(enabled('N-nonP')&&extended&&s.suffix.endsWith('N')&&['+N','−N'].includes(w.direction)){role='electron';rule='N + |±N| → E';}
   else if(enabled('N-P')&&s.suffix.endsWith('N')&&w.direction==='P'){role='proton';rule='N + |P| → P';}
   else if(enabledRules===null&&s.suffix==='NP'&&['+N','−N'].includes(w.direction)){role='neutron';rule='NP + |±N| → N';}
   else continue;
   const suffix=(s.suffix+({proton:'P',neutron:'N',electron:'E'})[role]).slice(-2);
   propose(proposals,w.to,{source:w.from,target:w.to,node:w.to,direction:w.direction,role,rule,front:s.front,suffix,pOrientation:s.pOrientation,kind:'movement'});
  }
  if(!accept(proposals,round+1))break;
 }
 for(const a of additions.values()){let r=rounds.find(r=>r.round===a.round);if(!r){r={round:a.round,ids:[]};rounds.push(r);}r.ids.push(a.id);}
 const valid=conflicts.size===0;
 return {valid,interfaceIdentifications:valid?interfaceIdentifications:[],candidates:valid?[...additions.values()].filter(a=>!initial.has(a.id)):[],rounds:valid?rounds:[],conflicts:[...conflicts.values()],rules:['N + |P| → P','NP + |±N| → N',...(extended?['E + |P| → N','N + |E| → E','N + |±N| → E']:[]),...(interfaces.length?['Interface: +P ↔ −P; no movement']:[]),...(sector==='internal'&&electronSelfRule?['Internal: E + |E| → P']:[])]};
}
