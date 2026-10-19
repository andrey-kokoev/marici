/* Four attempt-outcome ports. No dependency-to-implication conversion. */
export const PORTS = ['++', '+-', '-+', '--'];
export const PORT_LABELS = {'++':'prove: proved', '+-':'prove: failed to prove', '-+':'reject: rejected', '--':'reject: failed to reject'};
export const portKey = (node, port) => JSON.stringify([node,port]);

export function normalizeImplications(net) {
  const known = new Set(net.nodes.map(n=>n.id)), rules=[], omitted=[];
  const endpoint = e => {
    if (!e || !known.has(e.node) || !PORTS.includes(e.port)) throw Error('Implication has an unknown node or outcome port.');
    return {node:e.node,port:e.port,key:portKey(e.node,e.port)};
  };
  function add(raw, inputs, output) {
    if (typeof raw.id!=='string' || !raw.id || rules.some(r=>r.id===raw.id)) throw Error('Missing or duplicate implication ID.');
    const weight=raw.weight ?? 1;
    if (typeof weight!=='number' || !Number.isFinite(weight) || weight<=0) throw Error('Implication weight must be a finite positive number.');
    const normalized=inputs.map(endpoint);
    if (!normalized.length || new Set(normalized.map(e=>e.key)).size!==normalized.length) throw Error('Implication premises must be nonempty and distinct.');
    rules.push({id:raw.id,inputs:normalized,output:endpoint(output),weight,weightDeclared:raw.weight!==undefined,raw});
  }
  if (net.raw.port_implications!==undefined && !Array.isArray(net.raw.port_implications)) throw Error('port_implications must be an array.');
  for (const r of net.raw.port_implications || []) add(r,r.premises || [r.from],r.to);
  if (net.raw.proof_relations!==undefined && !Array.isArray(net.raw.proof_relations)) throw Error('proof_relations must be an array.');
  for (const r of net.raw.proof_relations || []) {
    // Branch activation is not a formal outcome implication.
    if (r.conclusion_outcome===undefined) {omitted.push({id:r.id,reason:'No conclusion outcome port (e.g. branch activation).',raw:r});continue;}
    const names=r.premises || [r.premise], outcomes=r.premise_outcomes || [r.premise_outcome];
    if (!Array.isArray(names) || !Array.isArray(outcomes) || names.length!==outcomes.length) throw Error('Mismatched premise outcome ports.');
    add(r,names.map((node,i)=>({node,port:outcomes[i]})),{node:r.conclusion,port:r.conclusion_outcome});
  }
  return {rules,omitted};
}

export function reachablePorts(rules, seeds) {
  const reached=new Set(seeds), active=new Set();
  let changed=true;
  while(changed) {
    changed=false;
    for(const r of rules) if(r.inputs.every(e=>reached.has(e.key))) {
      active.add(r.id);
      if(!reached.has(r.output.key)){reached.add(r.output.key);changed=true;}
    }
  }
  return {ports:reached,rules:active};
}
