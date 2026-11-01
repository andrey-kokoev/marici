// Audit of source role preservation, not a new color assignment or transport law.
export function analyzeDotCompatibility(claims){
 const groups=new Map();for(const claim of claims){if(!groups.has(claim.point))groups.set(claim.point,[]);groups.get(claim.point).push(claim);}
 const readings=[...groups].map(([point,entries])=>{
  const colours=[...new Set(entries.map(c=>c.colour))].sort((a,b)=>a-b);
  const sourceViolations=entries.filter(c=>c.kind==='requirement'&&c.observedColour!=null&&c.observedColour!==c.colour);
  const retainedMismatches=entries.filter(c=>c.retained&&c.observedColour!=null&&c.observedColour!==c.colour);
  const unknownSources=entries.filter(c=>c.kind==='requirement'&&c.observedColour==null);
  return {point,status:colours.length>1||sourceViolations.length||retainedMismatches.length||unknownSources.length?'unresolved':'no-colour-obstruction-observed',colours,claims:entries,sourceViolations,retainedMismatches,unknownSources,normalStatus:new Set(entries.filter(c=>c.normal).map(c=>JSON.stringify(c.normal.map(x=>Math.round(x*1e9))))).size>1?'multiple-cell-relative-normals':'no-normal-disagreement-observed'};
 });
 return {status:readings.some(r=>r.status==='unresolved')?'unresolved':'no-colour-obstruction-observed',readings,unresolvedVertices:readings.filter(r=>r.status==='unresolved').length,sourceViolations:readings.flatMap(r=>r.sourceViolations),scope:'Conditional role-preserving gluing audit: source A and destination C white; B/D use the source family color; octahedral ring uses that family color. No recoloring, role-changing transport, or common vertex normal is supplied.'};
}
