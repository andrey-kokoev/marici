import { computed, readonly, shallowRef, watch } from "vue";
import { defineStore } from "pinia";
import {
  VersionLibrarySchema,
  VersionNameSchema,
  type VersionLibrary,
} from "../../schemas/named-versions.js";
import {
  VERSION_LIBRARY_PREFIX,
  decodeVersionLibrary,
  saveVersionLibrary,
} from "../../named-version-storage.js";
import { useInspection } from "./inspection.js";
import { useCatalog } from "./catalog.js";

export const useVersions = defineStore("named-versions", () => {
  const inspection = useInspection(),
    catalog = useCatalog();
  const library = shallowRef<VersionLibrary | null>(null);
  const libraryError = shallowRef("");
  const matchingNames = computed(
    () =>
      library.value?.entries
        .filter((entry) => inspection.matchesVersion(entry, catalog.state.initialTurn))
        .map((entry) => entry.name) ?? [],
  );
  const saveBlockedReason = computed(() =>
    library.value === null
      ? "Saved versions are unavailable. Retry reading the library before saving."
      : library.value.entries.length >= 100
        ? "The 100-version limit is reached. Delete a saved version before saving another."
        : "",
  );
  function clearFeedback(): void {
    error.value = "";
    notice.value = "";
  }
  const error = shallowRef(""),
    notice = shallowRef("");
  function refresh(): void {
    library.value = null;
    error.value = "";
    notice.value = "";
    const document = inspection.activeDocument;
    libraryError.value = "";
    if (document === null || typeof window === "undefined") return;
    try {
      library.value = decodeVersionLibrary(
        window.localStorage.getItem(VERSION_LIBRARY_PREFIX + document.id),
        document.id,
      );
    } catch {
      libraryError.value =
        "Saved versions could not be read. Stored data has not been overwritten. Retry reading the library.";
    }
  }
  function save(name: string): boolean {
    error.value = "";
    notice.value = "";
    const checked = VersionNameSchema.safeParse(name),
      document = inspection.activeDocument;
    if (!checked.success) {
      error.value = "Enter a name of 1–80 characters.";
      return false;
    }
    if (document === null) return false;
    if (saveBlockedReason.value) {
      error.value = saveBlockedReason.value;
      return false;
    }
    try {
      const storage = window.localStorage,
        raw = storage.getItem(VERSION_LIBRARY_PREFIX + document.id);
      const current = decodeVersionLibrary(raw, document.id);
      library.value = current;
      if (current.entries.length >= 100) {
        error.value = saveBlockedReason.value;
        return false;
      }
      if (
        current.entries.some((entry) => entry.name.toLowerCase() === checked.data.toLowerCase())
      ) {
        error.value = "That name already exists. Choose another name; nothing was overwritten.";
        return false;
      }
      const snapshot = inspection.captureVersion(checked.data, catalog.state.initialTurn);
      if (snapshot === null) {
        error.value = inspection.editError || "Current diagram cannot be saved.";
        return false;
      }
      const next = VersionLibrarySchema.parse({
        ...current,
        entries: [...current.entries, snapshot],
      });
      saveVersionLibrary(storage, raw, next);
      library.value = next;
      notice.value = `Saved “${snapshot.name}”.`;
      return true;
    } catch {
      error.value =
        "Could not save version. Check browser storage permissions/free space, or refresh if another tab changed it. No existing version was overwritten.";
      return false;
    }
  }
  function load(name: string): boolean {
    error.value = "";
    notice.value = "";
    const document = inspection.activeDocument;
    if (document === null) return false;
    try {
      const current = decodeVersionLibrary(
        window.localStorage.getItem(VERSION_LIBRARY_PREFIX + document.id),
        document.id,
      );
      library.value = current;
      const snapshot = current.entries.find((entry) => entry.name === name);
      if (snapshot === undefined) {
        error.value = "That saved version no longer exists. Refresh the list.";
        return false;
      }
      if (!inspection.restoreVersion(snapshot)) {
        error.value =
          inspection.editError || "Version was not loaded; saved versions were retained.";
        return false;
      }
      catalog.setTurn(snapshot.initialTurn);
      library.value = current;
      notice.value = `Loaded “${snapshot.name}”.`;
      return true;
    } catch {
      error.value =
        "Could not read the saved version. No active edits or saved versions were changed.";
      return false;
    }
  }
  function remove(name: string): boolean {
    error.value = "";
    notice.value = "";
    const document = inspection.activeDocument;
    if (document === null) return false;
    try {
      const storage = window.localStorage,
        raw = storage.getItem(VERSION_LIBRARY_PREFIX + document.id);
      const current = decodeVersionLibrary(raw, document.id);
      library.value = current;
      if (!current.entries.some((entry) => entry.name === name)) {
        error.value = "That saved version no longer exists.";
        return false;
      }
      const next = VersionLibrarySchema.parse({
        ...current,
        entries: current.entries.filter((entry) => entry.name !== name),
      });
      saveVersionLibrary(storage, raw, next);
      library.value = next;
      notice.value = `Deleted “${name}”. Active edits were kept.`;
      return true;
    } catch {
      error.value = "Could not delete version. Stored data has not been overwritten.";
      return false;
    }
  }
  watch(() => inspection.activeDocument?.id, refresh, { immediate: true });
  watch(
    [
      () => inspection.activeDocument?.revision,
      () => inspection.state.selection,
      () => catalog.state.initialTurn,
    ],
    clearFeedback,
    { flush: "sync" },
  );
  return {
    names: computed(() => library.value?.entries.map((entry) => entry.name) ?? []),
    documentId: computed(() => inspection.activeDocument?.id),
    diagramTitle: computed(
      () =>
        inspection.activeDocument?.isotope?.name ??
        inspection.activeDocument?.title ??
        "Current diagram",
    ),
    matchingNames,
    isLibraryReady: computed(() => library.value !== null),
    matchingSummary: computed(() =>
      matchingNames.value.length > 1
        ? `${matchingNames.value.length} saved versions with identical wiring`
        : (matchingNames.value[0] ?? ""),
    ),
    workingStatus: computed(() =>
      library.value === null
        ? "Saved versions unavailable"
        : library.value.entries.length === 0
          ? "No saved versions"
          : matchingNames.value.length
            ? matchingNames.value.length > 1
              ? "Matches saved versions"
              : "Matches saved version"
            : "Differs from saved versions",
    ),
    saveBlockedReason,
    libraryError: readonly(libraryError),
    clearFeedback,
    error: readonly(error),
    notice: readonly(notice),
    refresh,
    save,
    load,
    remove,
  };
});
