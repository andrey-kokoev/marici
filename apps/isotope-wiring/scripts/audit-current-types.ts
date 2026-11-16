import { API } from "typescript/unstable/sync";
import { auditProject } from "./type-audit.ts";

export function auditCurrentTypes() {
  const api = new API();
  try {
    const snapshot = api.updateSnapshot({ openProjects: ["tsconfig.json"] });
    try {
      const project = snapshot.getProject("tsconfig.json");
      if (project === undefined) throw new Error("Type-check project did not load");
      return auditProject(project);
    } finally {
      snapshot.dispose();
    }
  } finally {
    api.close();
  }
}
