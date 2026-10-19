// Isotope composition records for display in the R-layer space.
// These are structure data (P/N/e counts and stable member IDs), not a new
// geometric embedding, physical occupation rule, or interaction law.
const definitions={
 hydrogen:{label:'Hydrogen-1',protons:1,neutrons:0,electrons:1},deuterium:{label:'Deuterium',protons:1,neutrons:1,electrons:1},
 helium3:{label:'Helium-3',protons:2,neutrons:1,electrons:2},helium4:{label:'Helium-4',protons:2,neutrons:2,electrons:2},
 lithium6:{label:'Lithium-6',protons:3,neutrons:3,electrons:3},lithium7:{label:'Lithium-7',protons:3,neutrons:4,electrons:3},
 beryllium9:{label:'Beryllium-9',protons:4,neutrons:5,electrons:4},boron10:{label:'Boron-10',protons:5,neutrons:5,electrons:5},boron11:{label:'Boron-11',protons:5,neutrons:6,electrons:5},
 carbon12:{label:'Carbon-12',protons:6,neutrons:6,electrons:6},carbon13:{label:'Carbon-13',protons:6,neutrons:7,electrons:6},nitrogen15:{label:'Nitrogen-15',protons:7,neutrons:8,electrons:7},
 'nitrogen15-local':{label:'Nitrogen-15 · local reference',protons:7,neutrons:8,electrons:7},
 'oxygen16-local':{label:'Oxygen-16 · local reference',protons:8,neutrons:8,electrons:8},'oxygen17-local':{label:'Oxygen-17 · local reference',protons:8,neutrons:9,electrons:8},'oxygen18-local':{label:'Oxygen-18 · local reference',protons:8,neutrons:10,electrons:8},
 'fluorine19-local':{label:'Fluorine-19 · local reference',protons:9,neutrons:10,electrons:9},
 'neon20-local':{label:'Neon-20 · local reference',protons:10,neutrons:10,electrons:10},'neon22-local':{label:'Neon-22 · local reference',protons:10,neutrons:12,electrons:10}
};
const speciesOrder=[['proton','protons'],['neutron','neutrons'],['electron','electrons']];
export const isotopeStructureData=Object.freeze(Object.fromEntries(Object.entries(definitions).map(([id,definition])=>{
  const constituents=speciesOrder.flatMap(([species,key])=>Array.from({length:definition[key]},(_,i)=>Object.freeze({id:`${species[0]}${i+1}`,species,ordinal:i+1})));
  return [id,Object.freeze({id,...definition,massNumber:definition.protons+definition.neutrons,constituents:Object.freeze(constituents),dataKind:'isotope-structure-record',embedding:'not-specified'})];
})));
export const isotopeStructureIds=Object.freeze(Object.keys(isotopeStructureData));
