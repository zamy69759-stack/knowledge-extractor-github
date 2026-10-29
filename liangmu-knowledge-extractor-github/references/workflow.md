# Workflow and acceptance rules

## Extraction

1. Run `folders` and match the user's exact first-level folder name.
2. Confirm the Chinese and English series names if they cannot be derived unambiguously. Never fabricate them.
3. Run `extract`. The first run registers a stable `PRD-NNN`; later runs reuse it, back up the workbook, and preserve identifiers.
4. Run `associate --series PRD-NNN` to refresh evidence-based candidate image links when necessary.
5. Run `check` and report the workbook, series directory, check report, parsed/failed file counts, Q&A count, image count, pending count, and candidate-link count.
6. Stop for human Excel review. Do not mark rows approved.

## Excel review and indexing

The workbook must contain exactly these seven sheets:

1. `全系列Q&A审核总表`
2. `图片索引`
3. `型号索引`
4. `冲突与待确认`
5. `萃取统计`
6. `更新记录`
7. `原始文件清单`

After the user confirms review is complete, run `reindex`. Index validation failure must not replace the last valid index. Never ask users to edit JSON.

## Query and image return

1. Identify the exact series ID and, where possible, the model.
2. Query approved knowledge by default.
3. Include the source stored in Excel.
4. If the answer needs an image, verify the image path and association review status.
5. Display or link only an existing local file. State clearly when an association remains pending.

## Safety

- Never modify, move, rename, or delete source files.
- Never place the output directory inside the source directory or vice versa.
- Never infer facts from filenames alone.
- Preserve conflicts and parse failures for review.
- Mark macOS `._` AppleDouble files as non-business metadata; do not treat them as source documents or product images.
