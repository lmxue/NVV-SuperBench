#!/usr/bin/env python3
"""
prepare_demo.py - Prepares demo audio files and demo_data.json for the NVBench
project page.

Reads manifests from the eval_samples directory, selects up to 3 samples per
NVV type across all available types, copies audio, and generates demo_data.json.
"""

import json
import os
import shutil

# ─── Configuration ────────────────────────────────────────────────────────────

BASE_DIR = "/aifs4su/mmcode/lmxue/workspace/non_verbal_events/github/interspeech2026/NVBench"
EVAL_SAMPLES_DIR = (
    "/aifs4su/mmcode/lmxue/workspace/non_verbal_events/huggingface/NVE-BM/"
    "sub_eval_data/eval_samples"
)
AUDIO_OUT_DIR = os.path.join(BASE_DIR, "audio")

MANIFEST_KEYS = ["en-tag", "en-prompt", "zh-tag", "zh-prompt"]
SAMPLES_PER_TYPE = 3

# ─── Load manifests ───────────────────────────────────────────────────────────

def load_manifest(mode_key):
    path = os.path.join(EVAL_SAMPLES_DIR, f"manifest_{mode_key}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_sampled(lang):
    path = os.path.join(EVAL_SAMPLES_DIR, f"sampled_{lang}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ─── Build lookup: id -> metadata ─────────────────────────────────────────────

def build_id_lookup(samples_list):
    return {item["id"]: item for item in samples_list}


# ─── Pick samples for a NVV type ─────────────────────────────────────────────

def pick_samples(nvv_type, manifest, max_samples=SAMPLES_PER_TYPE):
    """
    Return up to max_samples sample_ids that have audio from at least 2 systems.
    """
    by_tag = manifest.get("by_tag", {})
    if nvv_type not in by_tag:
        return []
    tag_data = by_tag[nvv_type]
    sample_ids = tag_data.get("sample_ids", [])
    systems = tag_data.get("systems", {})

    qualified = []
    for sample_id in sample_ids:
        # Count how many systems have a non-null path for this sample_id
        count = 0
        for sys_data in systems.values():
            path = sys_data.get("paths", {}).get(sample_id)
            if path is not None:
                count += 1
        if count >= 2:
            qualified.append(sample_id)
        if len(qualified) >= max_samples:
            break

    if len(qualified) < max_samples:
        for sample_id in sample_ids:
            if sample_id not in qualified:
                qualified.append(sample_id)
            if len(qualified) >= max_samples:
                break

    return qualified


# ─── Copy audio and build entry ───────────────────────────────────────────────

def process_sample(mode_key, nvv_type, sample_id, manifest, id_lookup, source_mode_key=None):
    """
    Copy audio files for all systems for this sample_id and return the
    demo_data entry dict.
    """
    by_tag = manifest.get("by_tag", {})
    tag_data = by_tag[nvv_type]
    systems = tag_data.get("systems", {})

    # Build metadata from lookup
    meta = id_lookup.get(sample_id, {})
    text = meta.get("text", "")
    text_with_mark = meta.get("text_with_mark", "")
    caption = meta.get("caption_with_nvb", "")

    audio_entry = {}
    for sys_key, sys_data in systems.items():
        sys_name = sys_data.get("name", sys_key)
        src_path = sys_data.get("paths", {}).get(sample_id)
        if src_path is None:
            continue  # unsupported / null path
        if not os.path.exists(src_path):
            print(f"  WARNING: file not found: {src_path}")
            continue

        ext = os.path.splitext(src_path)[1]
        dest_dir = os.path.join(AUDIO_OUT_DIR, mode_key, nvv_type, sys_key)
        os.makedirs(dest_dir, exist_ok=True)
        dest_file = f"{sample_id}{ext}"
        dest_path = os.path.join(dest_dir, dest_file)

        shutil.copy2(src_path, dest_path)

        # Use forward slashes for web paths
        rel_path = f"audio/{mode_key}/{nvv_type}/{sys_key}/{dest_file}"
        audio_entry[sys_key] = {
            "name": sys_name,
            "path": rel_path,
        }

    return {
        "id": sample_id,
        "text": text,
        "text_with_mark": text_with_mark,
        "caption": caption,
        "source_mode": source_mode_key or mode_key,
        "audio": audio_entry,
    }


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    # Load all manifests
    manifests = {mk: load_manifest(mk) for mk in MANIFEST_KEYS}
    all_types = sorted({
        nvv_type
        for manifest in manifests.values()
        for nvv_type in manifest.get("by_tag", {}).keys()
    })

    # Load sampled metadata
    sampled_en = load_sampled("en")
    sampled_zh = load_sampled("zh")
    id_lookup_en = build_id_lookup(sampled_en)
    id_lookup_zh = build_id_lookup(sampled_zh)

    id_lookups = {
        "en-tag": id_lookup_en,
        "en-prompt": id_lookup_en,
        "zh-tag": id_lookup_zh,
        "zh-prompt": id_lookup_zh,
    }

    demo_data = {}
    total_files_copied = 0

    for mode_key in MANIFEST_KEYS:
        manifest = manifests[mode_key]
        id_lookup = id_lookups[mode_key]
        demo_data[mode_key] = {}

        print(f"\n=== Processing mode: {mode_key} ===")

        for nvv_type in all_types:
            source_mode_key = mode_key
            source_manifest = manifest

            if nvv_type not in source_manifest.get("by_tag", {}) and mode_key.endswith("-tag"):
                fallback_mode_key = mode_key.replace("-tag", "-prompt")
                fallback_manifest = manifests[fallback_mode_key]
                if nvv_type in fallback_manifest.get("by_tag", {}):
                    source_mode_key = fallback_mode_key
                    source_manifest = fallback_manifest
                    print(f"  [{nvv_type}] FALLBACK: using {fallback_mode_key}")

            sample_ids = pick_samples(nvv_type, source_manifest)
            if not sample_ids:
                print(f"  [{nvv_type}] SKIP: not available in {mode_key}")
                demo_data[mode_key][nvv_type] = {"samples": []}
                continue

            print(f"  [{nvv_type}] sample_ids={sample_ids}")
            entries = []
            for sample_id in sample_ids:
                entry = process_sample(
                    mode_key,
                    nvv_type,
                    sample_id,
                    source_manifest,
                    id_lookup,
                    source_mode_key=source_mode_key,
                )
                n_audio = len(entry["audio"])
                total_files_copied += n_audio
                print(f"    -> {sample_id}: copied {n_audio} audio files: {list(entry['audio'].keys())}")
                entries.append(entry)

            demo_data[mode_key][nvv_type] = {"samples": entries}

    # Write demo_data.json
    out_path = os.path.join(BASE_DIR, "demo_data.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(demo_data, f, ensure_ascii=False, indent=2)

    print(f"\nDone! Copied {total_files_copied} audio files total.")
    print(f"demo_data.json written to: {out_path}")

    # Quick verification
    print("\n--- Verification ---")
    for mode_key in MANIFEST_KEYS:
        available = [t for t in all_types if demo_data[mode_key].get(t, {}).get("samples")]
        print(f"  {mode_key}: {len(available)}/{len(all_types)} types have samples")

    # Count actual audio files on disk
    audio_count = 0
    for root, dirs, files in os.walk(AUDIO_OUT_DIR):
        audio_count += len(files)
    print(f"  Total audio files on disk: {audio_count}")


if __name__ == "__main__":
    main()
