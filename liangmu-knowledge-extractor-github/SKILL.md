---
name: liangmu-knowledge-extractor
description: Operate the local Liangmu enterprise product knowledge system that turns one explicitly selected product-series folder containing PDF, DOCX, XLSX, PPTX, images, text, or CSV into one seven-sheet Excel master knowledge base plus derived JSON indexes. Use when Codex needs to configure paths, list product folders, extract or incrementally update one series, refresh image-to-Q&A candidate associations, rebuild indexes after Excel review, query approved product knowledge, return linked product images, or run knowledge-base integrity checks.
---

# Liangmu Knowledge Extractor

Use the installed deterministic CLI for every parsing or state-changing action. Keep source materials read-only. Treat Excel as the only human-maintained knowledge source; JSON is derived and must never be edited manually. Never generate Markdown product knowledge cards.

## Run the tool

Invoke the bundled wrapper:

```powershell
python "<skill-dir>\scripts\run_liangmu.py" <command> [arguments]
```

The wrapper locates the project from `LIANGMU_TOOL_ROOT`, defaulting to `D:\企业知识萃取`, and uses its `.venv` interpreter.

## Route requests

- Configure source and knowledge roots: `setup [--source PATH --dest PATH]`.
- List current first-level product folders: `folders`. Always rescan; never infer a selection.
- Extract or update exactly one folder: require its exact first-level folder name and confirmed Chinese/English series names, then run `extract --folder NAME --zh-name NAME --en-name NAME`.
- Refresh candidate image associations: `associate --series PRD-NNN`.
- After a user reviews the Excel workbook: run `reindex --series PRD-NNN`.
- Ask product questions: run `query --series PRD-NNN --question TEXT`. Only use `--include-pending` when the user explicitly requests an internal review query, and label the answer unapproved.
- Validate all registered knowledge bases: `check`.

Read [workflow.md](references/workflow.md) before extraction, update, review-index refresh, or publishing an answer with images.

## Enforce evidence and review rules

- Require one exact product folder; never process multiple folders in one request.
- Do not invent series names, models, specifications, compatibility, image descriptions, or visual conclusions.
- Preserve stable PRD, Q&A, and image identifiers during updates.
- Treat automatic Q&A and image links as `待审核`.
- Use only `已通过` Q&A as a formal answer.
- For a linked image, verify the file exists and its image association is approved before presenting it as confirmed evidence.
- If external visual understanding is unavailable or unauthorized, retain the image/OCR/source and report `待视觉分析`; do not upload enterprise files to third parties.
- Report automated test, simulated-data validation, and real-enterprise-data validation separately.

## Handle failures

Preserve existing Excel, history, images, and valid JSON indexes. Diagnose the exact failing file or phase, fix the tool when appropriate, and rerun the same registered series. Never delete source materials or silently start another folder.

