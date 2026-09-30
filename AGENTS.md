# Repository Guidelines

## Project Scope

This repository is now a workspace for non-prompt-card image production. The historical Wuhan presenter-card project is archived in `提示卡项目/`. Treat that directory as read-only history and style reference unless the user explicitly asks to revise an archived card.

The general project style is **冷钴蓝稀疏蚀刻建筑插画** (`Cobalt-blue editorial etching illustration`): neutral warm-white paper, one cool cobalt-blue ink, low ink density, generous negative space, graphic simplification, sparse stippling, and a few short hatch marks. It is a modern editorial print illustration, not a historical photograph, a photo filter, or dense realistic copperplate engraving. A product-specific `插画素材规格.md` overrides the general palette and output mode when it exists. For `图片项目/miniprogram-pic/`, that specification is authoritative: deep green `#0E5C3F`, transparent PNG, 3:4 composition, subject anchored near the lower edge, and the upper 30–40% left empty.

## Project Structure & Module Organization

Create each new subject in its own descriptive directory under `图片项目/<主题>/`. Keep the prompt, source or reference record, generated image versions, and any factual boundary notes together. Use `README.md` for project-wide conventions, `kanban.md` for current status and gates, and `提示卡项目/` only for the archived prompt-card work. Do not create a parallel status board.

For a new image project, use these files when they apply:

- `生成提示词.md`: prompt, image role, style constraints, and generation record.
- `来源.md` or `核查.md`: reference-image provenance, licenses, factual sources, and uncertainty boundaries.
- `<主题>-vN.png`: versioned output; do not overwrite an earlier version.

## Visual and Content Boundaries

- Preserve the subject's identity and major spatial relationships when a reference image is supplied; change the medium, color, and illustration treatment only unless the brief authorizes a redesign.
- Keep the paper visible through the subject. Avoid dirty yellow, ochre, brown, sepia, continuous gray gradients, dense cross-hatching, and full-area dark texture.
- Keep factual claims separate from AI-generated visual interpretation. Do not describe an AI-generated image as an archival or historical photograph.
- Record external-image licenses and the permitted use of each reference. Do not commit credentials, private attachments, browser caches, or generated tool output.

## Validation

There is no package manager, build system, or automated test suite. Validation is editorial and asset-based:

1. Inspect filenames and links with `rg --files` and targeted `rg` searches.
2. Run `git diff --check`.
3. Verify PNG format and dimensions with `identify` or another image metadata tool when available.
4. Open or visually inspect the intended output and confirm that the style, subject, and version path match the brief.

## Commit and Delivery

Use short Conventional Commit-style subjects with the Codex marker, for example `feat: add etched illustration 01 [Codex]` or `docs: archive prompt-card project [Codex]`. Keep each commit focused, stage explicit paths, and check for sensitive information before committing. Delivery notes should name the changed files, source boundaries, AI-generated assets, and the verification performed.
