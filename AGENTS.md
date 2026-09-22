# Repository Guidelines

## Project Structure & Module Organization

This repository contains presenter prompt cards for Wuhan architectural walks. Each location has one numbered directory, such as `29-英文楚报馆旧址/`. Keep the location's generated PNGs, presenter prompt Markdown, fact-check notes, image-generation prompt, and relevant local research together. Use `README.md` for project-wide conventions and current highlights; use `kanban.md` for active status and next steps; use `placenumber.md` for the route sequence. Do not create a parallel status board.

## Build, Test, and Development Commands

There is no package manager, build system, or automated test suite. Changes are edited directly as Markdown or image assets. Before submitting work, inspect links and filenames with `rg --files`, review Markdown changes with `git diff --check`, and verify generated PNG dimensions and format with an image metadata tool such as `identify` when available. Update `README.md` only when a new location or notable project convention needs to be surfaced.

## Coding Style & Naming Conventions

Use UTF-8 Markdown with concise headings and plain, presenter-friendly Chinese prose. Preserve the established numbered directory format: `<number>-<地点名>/`. Name assets descriptively, for example `提词卡初稿.md`, `核查.md`, `生成提示词.md`, and `<地点名>-v2.png`. Increment image versions instead of overwriting earlier variants. Keep source claims separate from AI-generated visual interpretation, and record source boundaries in the fact-check notes.

## Testing Guidelines

Validation is editorial and asset-based rather than unit-test based. Check that every factual claim in a prompt card is supported by the accompanying `核查.md`, that external or AI-generated material is identified, that Markdown links resolve to tracked files, and that the intended PNG version opens at the expected dimensions. For a new location, confirm the number and name against `placenumber.md`.

## Commit & Pull Request Guidelines

Use short Conventional Commit-style subjects such as `feat: add Wuhan guide card 30`, `docs: update fact check`, or `chore: retire unversioned card filename`; existing commits append `[Codex]` when authored by Codex. Keep each commit focused and include only related files. Pull requests should explain the location and asset changes, identify fact-check sources and any AI-generated imagery, link relevant README/KANBAN updates, and include image previews when visual layout changed.

## Security & Configuration Tips

Do not commit credentials, private source attachments, browser caches, or generated tool output. Respect the existing `.gitignore`. Treat AI-generated building imagery as stylized illustration, not historical photography, unless independently verified evidence supports a different claim.
