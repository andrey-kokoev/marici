import { computed, readonly, shallowRef } from "vue";
import { defineStore } from "pinia";
import { z } from "zod";
import { isotopeCatalog } from "../../examples/catalog.js";
import { DiagramDocumentSchema } from "../../schemas/document.js";
import { TurnSchema } from "../../schemas/traversal.js";
import { useInspection } from "./inspection.js";

const CatalogStateSchema = z.strictObject({
  selected: z.string(),
  open: z.boolean(),
  docked: z.boolean(),
  query: z.string(),
  element: z.string(),
  mass: z.string(),
  references: z.array(DiagramDocumentSchema),
  history: z.array(z.string()),
  historyIndex: z.int().nonnegative(),
  initialTurn: TurnSchema,
  speed: z.enum(["0.5", "1", "2", "4"]),
  showCounts: z.boolean(),
});
export const useCatalog = defineStore("catalog", () => {
  const inspection = useInspection();
  const current = shallowRef(
    CatalogStateSchema.parse({
      selected: "Neon-20",
      open: true,
      docked: true,
      query: "",
      element: "",
      mass: "",
      references: [],
      history: ["Neon-20"],
      historyIndex: 0,
      initialTurn: inspection.savedInitialTurn ?? "left",
      speed: "1",
      showCounts: true,
    }),
  );
  const selected = computed(() =>
    isotopeCatalog.find((entry) => entry.name === current.value.selected),
  );
  const results = computed(() =>
    readonly(
      isotopeCatalog.filter(
        (entry) =>
          entry.name.toLowerCase().includes(current.value.query.trim().toLowerCase()) &&
          (!current.value.element || entry.element === current.value.element) &&
          (!current.value.mass || entry.mass === Number(current.value.mass)),
      ),
    ),
  );
  const elements = readonly([...new Set(isotopeCatalog.map((entry) => entry.element))]);
  function activate(name: string): void {
    inspection.loadDiagram(name);
    if (inspection.savedInitialTurn !== undefined)
      current.value = { ...current.value, initialTurn: inspection.savedInitialTurn };
  }
  function select(name: string): void {
    if (!isotopeCatalog.some((entry) => entry.name === name) || current.value.selected === name)
      return;
    const history = [...current.value.history.slice(0, current.value.historyIndex + 1), name];
    current.value = {
      ...current.value,
      selected: name,
      history,
      historyIndex: history.length - 1,
      open: current.value.docked && current.value.open,
    };
    activate(name);
  }
  function navigate(offset: number): void {
    if (!Number.isInteger(offset)) return;
    const index = current.value.historyIndex + offset,
      name = current.value.history[index];
    if (name === undefined) return;
    current.value = {
      ...current.value,
      selected: name,
      historyIndex: index,
    };
    activate(name);
  }
  function setFilter(field: "query" | "element" | "mass", value: string): void {
    current.value = { ...current.value, [field]: CatalogStateSchema.shape[field].parse(value) };
  }
  function resetFilters(): void {
    current.value = {
      ...current.value,
      query: "",
      element: "",
      mass: "",
    };
  }
  function setOpen(open: boolean): void {
    current.value = { ...current.value, open };
  }
  function toggleDock(): void {
    current.value = { ...current.value, docked: !current.value.docked };
  }
  function toggleCounts(): void {
    current.value = { ...current.value, showCounts: !current.value.showCounts };
  }
  function setTurn(value: string): void {
    const result = TurnSchema.safeParse(value);
    if (result.success && inspection.setInitialTurn(result.data))
      current.value = { ...current.value, initialTurn: result.data };
  }
  function setSpeed(value: string): void {
    const result = CatalogStateSchema.shape.speed.safeParse(value);
    if (result.success) current.value = { ...current.value, speed: result.data };
  }
  function pin(): void {
    const document = inspection.activeDocument;
    if (document === null) return;
    const found = current.value.references.some((item) => item.id === document.id);
    current.value = {
      ...current.value,
      references: found
        ? current.value.references.filter((item) => item.id !== document.id)
        : [...current.value.references, DiagramDocumentSchema.parse(document)],
    };
  }
  function unpin(id: string): void {
    current.value = {
      ...current.value,
      references: current.value.references.filter((item) => item.id !== id),
    };
  }
  return {
    state: readonly(current),
    selected,
    results,
    elements,
    select,
    navigate,
    setFilter,
    resetFilters,
    setOpen,
    toggleDock,
    toggleCounts,
    setTurn,
    setSpeed,
    pin,
    unpin,
  };
});
