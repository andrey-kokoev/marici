export function quartetCellCoherence(roles){
 if(roles.length!==3||roles.some(r=>!['neutron','proton','electron'].includes(r)))throw Error('Three face-connected colours required');
 const neutrons=roles.filter(r=>r==='neutron').length;
 if(neutrons!==1&&neutrons!==2)throw Error('Quartet must contain two N and two non-N cells');
 return {pattern:'2N + 2 non-N',role:neutrons===2?'proton':'neutron'};
}
