#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prepare a V2 layered-feature manifest while REUSING the existing text features
and pointing speech paths to the newly re-extracted V2 speech feature root.

This script never copies or rewrites text feature files. It preserves the
existing `text_layered_feature_path` values from the base manifest.
"""

import argparse
from pathlib import Path

import pandas as pd


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument(
        "--base_manifest",
        required=True,
        help=(
            "Existing layered/cached manifest that already contains the old "
            "text_layered_feature_path column."
        ),
    )
    p.add_argument(
        "--new_speech_root",
        required=True,
        help="New V2 speech root, e.g. .../dca_moe_v2_no_temporal_transformer/speech_layered",
    )
    p.add_argument("--output_manifest", required=True)
    p.add_argument(
        "--dataset",
        default="all",
        choices=["all", "ADReSS", "ADReSSo", "TAUKADIAL", "NCMMSC"],
    )
    p.add_argument(
        "--text_root",
        default=None,
        help=(
            "Fallback only if base_manifest has no text_layered_feature_path. "
            "Paths will be <text_root>/<dataset>/<sample_id>.pt."
        ),
    )
    p.add_argument(
        "--strict",
        action="store_true",
        help="Fail if any reused text or new speech feature file is missing.",
    )
    return p.parse_args()


def main():
    args = parse_args()
    base_manifest = Path(args.base_manifest)
    new_speech_root = Path(args.new_speech_root)
    output_manifest = Path(args.output_manifest)

    if not base_manifest.exists():
        raise FileNotFoundError(f"Base manifest not found: {base_manifest}")

    df = pd.read_csv(base_manifest)
    required = [
        "sample_id",
        "dataset",
        "split",
        "label",
        "lang_id",
        "text_expert_group",
    ]
    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    if args.dataset != "all":
        df = df[df["dataset"].astype(str) == args.dataset].copy()
        if df.empty:
            raise ValueError(
                f"No rows found for dataset={args.dataset!r} in {base_manifest}."
            )
    else:
        df = df.copy()

    if "text_layered_feature_path" not in df.columns:
        if args.text_root is None:
            raise ValueError(
                "base_manifest has no text_layered_feature_path. Provide --text_root."
            )
        text_root = Path(args.text_root)
        df["text_layered_feature_path"] = [
            str(text_root / str(ds).strip() / f"{str(sid).strip()}.pt")
            for ds, sid in zip(df["dataset"], df["sample_id"])
        ]

    # Keep a trace of the old speech path if the base manifest had one.
    if "speech_layered_feature_path" in df.columns:
        old_speech = df["speech_layered_feature_path"].astype(str).copy()
        df["speech_layered_feature_path_v1_original"] = old_speech
    else:
        old_speech = None

    new_speech_paths = [
        str(new_speech_root / str(ds).strip() / f"{str(sid).strip()}.pt")
        for ds, sid in zip(df["dataset"], df["sample_id"])
    ]
    df["speech_layered_feature_path"] = new_speech_paths

    # Explicitly enforce the user's isolation requirement.
    if old_speech is not None:
        same = old_speech.reset_index(drop=True) == pd.Series(new_speech_paths)
        if bool(same.any()):
            bad = int(same.sum())
            raise RuntimeError(
                f"Isolation violation: {bad} V2 speech path(s) are identical to the old path(s). "
                "Choose a different --new_speech_root."
            )

    df["text_feature_reused_from_previous_version"] = True
    df["speech_feature_version"] = "v2_reextract_no_temporal_transformer_experiment"
    df["model_speech_temporal_transformer"] = False
    df["model_speech_position_encoding"] = "none"

    missing_text = []
    missing_speech = []
    for _, row in df.iterrows():
        tp = Path(str(row["text_layered_feature_path"]))
        sp = Path(str(row["speech_layered_feature_path"]))
        if not tp.exists():
            missing_text.append(str(tp))
        if not sp.exists():
            missing_speech.append(str(sp))

    print("=" * 100)
    print("[V2 MANIFEST AUDIT]")
    print(f"base manifest : {base_manifest}")
    print(f"dataset       : {args.dataset}")
    print(f"rows          : {len(df)}")
    print(f"new speech root: {new_speech_root}")
    print(f"missing reused text : {len(missing_text)}")
    print(f"missing new speech  : {len(missing_speech)}")
    print("Text feature paths are preserved/reused; speech paths point only to the V2 root.")
    print("=" * 100)

    if missing_text[:10]:
        print("[FIRST MISSING TEXT PATHS]")
        for x in missing_text[:10]:
            print(x)
    if missing_speech[:10]:
        print("[FIRST MISSING SPEECH PATHS]")
        for x in missing_speech[:10]:
            print(x)

    if args.strict and (missing_text or missing_speech):
        raise FileNotFoundError(
            f"Strict audit failed: missing_text={len(missing_text)}, "
            f"missing_speech={len(missing_speech)}"
        )

    output_manifest.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_manifest, index=False, encoding="utf-8-sig")
    print(f"[SAVE] {output_manifest}")


if __name__ == "__main__":
    main()
