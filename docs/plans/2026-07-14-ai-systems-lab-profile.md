# AI Systems Lab GitHub Profile Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Publish a bilingual, animated, technology-forward GitHub profile for `aiis2` under the AI Systems Lab identity.

**Architecture:** A single GitHub Profile README references repository-hosted raster assets from `assets/`. A generated cinematic hero is converted into a small seamless animation with a strong static first frame, while all essential identity, project, and stack information remains accessible as Markdown text. A lightweight local verification script checks the README contract and media files before publishing.

**Tech Stack:** GitHub Markdown/HTML, OpenAI image generation, Python Pillow, GitHub CLI, Python standard-library validation.

---

### Task 1: Capture the profile content contract

**Files:**
- Create: `tests/test_profile.py`

**Step 1: Write the failing contract test**

Create tests that require:

```python
from pathlib import Path


ROOT = Path(__file__).parents[1]
README = ROOT / "README.md"
HERO = ROOT / "assets" / "ai-systems-lab.gif"


def test_readme_contains_identity_and_sections():
    text = README.read_text(encoding="utf-8")
    required = [
        "AI SYSTEMS LAB",
        "SYSTEM PROFILE",
        "CURRENT SIGNALS",
        "PROJECT MATRIX",
        "TECH STACK",
        "https://github.com/aiis2/datell",
        "https://github.com/aiis2/risk-agent",
        "https://github.com/aiis2/frontend-design-report",
    ]
    assert all(item in text for item in required)


def test_hero_is_repository_hosted_and_bounded():
    text = README.read_text(encoding="utf-8")
    assert "assets/ai-systems-lab.gif" in text
    assert HERO.exists()
    assert HERO.stat().st_size < 5_000_000
```

**Step 2: Run the test to verify it fails**

Run: `python -m unittest discover -s tests -p "test_*.py" -v`

Expected: ERROR because `README.md` does not exist.

**Step 3: Commit the contract**

```bash
git add tests/test_profile.py
git commit -m "test: define profile content contract"
```

### Task 2: Generate the AI Systems Lab hero source

**Files:**
- Create: `assets/ai-systems-lab-source.png`

**Step 1: Invoke the image generation skill**

Use `@imagegen` to generate a wide, text-free cinematic scene with a black technical grid, luminous cyan data streams, electric-green signal accents, a central abstract AI core, precise glass-like interface traces, and clean negative space. Avoid people, logos, illegible pseudo-text, purple dominance, and stock-image styling.

**Step 2: Inspect the generated source**

Render or view the source at original detail. Verify that it is nonblank, has a clear focal point, has safe dark space for exact typography, and contains no malformed text.

**Step 3: Save the selected source**

Copy the selected generated image to `assets/ai-systems-lab-source.png` without recompressing it.

**Step 4: Commit the source**

```bash
git add assets/ai-systems-lab-source.png
git commit -m "art: add AI Systems Lab hero source"
```

### Task 3: Build the optimized animated hero

**Files:**
- Create: `scripts/build_hero.py`
- Create: `assets/ai-systems-lab.gif`

**Step 1: Implement the animation builder**

Use Pillow to crop the source to `1200x420`, apply a subtle 24-frame parallax zoom, animate one cyan scan beam, pulse the core glow, add sparse deterministic signal particles, and overlay exact typography:

```text
AIIS2 // AI SYSTEMS LAB
FULL-STACK AI ENGINEERING · INTELLIGENT SYSTEMS
SYSTEM ONLINE  /  SHANGHAI  /  2026
```

Use a locally available bold sans-serif font, white primary text, cyan secondary text, and a small green online indicator. Export an optimized looping GIF with a 90 ms frame duration and a stable first frame.

**Step 2: Build the hero**

Run: `python scripts/build_hero.py`

Expected: `assets/ai-systems-lab.gif` is created at `1200x420` and remains below 5 MB.

**Step 3: Inspect the animation**

Extract the first, middle, and final frames and inspect them together. Verify typography, crop, motion continuity, contrast, and absence of rapid flashing.

**Step 4: Commit the animation**

```bash
git add scripts/build_hero.py assets/ai-systems-lab.gif
git commit -m "feat: add animated AI Systems Lab hero"
```

### Task 4: Author the bilingual Profile README

**Files:**
- Create: `README.md`

**Step 1: Add the hero and identity**

Reference `assets/ai-systems-lab.gif` with meaningful alt text. Add the English positioning line followed by a concise Chinese translation.

**Step 2: Add SYSTEM PROFILE and CURRENT SIGNALS**

Describe `aiis2` as a full-stack AI engineer and experimental systems lab. Keep the copy concrete: local-first AI analytics, agentic systems, interactive data products, and human-centered AI interfaces.

**Step 3: Add PROJECT MATRIX**

Link directly to:

- `aiis2/datell`: local-first AI data analysis and interactive reports.
- `aiis2/risk-agent`: coordinator/worker ReAct risk coverage analyzer.
- `aiis2/frontend-design-report`: visual report skill and MCP runtime.

**Step 4: Add TECH STACK and footer signal**

Use compact shields for TypeScript, Python, React, Node.js, AI Agents, and local-first systems. End with a restrained status line and a direct GitHub link. Do not add live visitor counters or third-party stats panels.

**Step 5: Run the contract tests**

Run: `python -m unittest discover -s tests -p "test_*.py" -v`

Expected: both tests PASS.

**Step 6: Commit the README**

```bash
git add README.md
git commit -m "feat: launch bilingual AI Systems Lab profile"
```

### Task 5: Verify media and Markdown behavior

**Files:**
- Modify if required: `README.md`
- Modify if required: `scripts/build_hero.py`

**Step 1: Check public project links**

Run:

```powershell
@('datell','risk-agent','frontend-design-report') | ForEach-Object { gh api "repos/aiis2/$_" --jq '.html_url' }
```

Expected: three GitHub repository URLs.

**Step 2: Verify image metadata**

Run a Pillow check that asserts GIF format, animation, `1200x420` dimensions, and size below 5 MB.

**Step 3: Render a local preview**

Render the README to HTML or use GitHub's Markdown API, then capture wide and narrow screenshots. Check hero visibility, wrapping, bilingual hierarchy, and project-link clarity.

**Step 4: Fix only observed issues**

Rebuild the GIF or adjust README markup only when verification reveals a concrete problem.

**Step 5: Re-run all checks and commit fixes**

```bash
git add README.md scripts/build_hero.py assets/ai-systems-lab.gif
git commit -m "fix: polish profile rendering"
```

Skip the commit if no fixes were needed.

### Task 6: Publish the special GitHub profile repository

**Files:**
- No new files expected.

**Step 1: Rename the local branch**

Run: `git branch -M main`

**Step 2: Create the public repository**

Run: `gh repo create aiis2/aiis2 --public --source . --remote origin --push --description "AI Systems Lab · Full-stack AI engineering and intelligent systems"`

Expected: repository `https://github.com/aiis2/aiis2` is created and `main` is pushed.

**Step 3: Verify GitHub recognizes the profile README**

Run: `gh api repos/aiis2/aiis2 --jq '{name,visibility,default_branch,html_url}'`

Expected: a public repository named `aiis2` with `main` as the default branch.

**Step 4: Verify the live asset and README**

Run GitHub API checks for `README.md` and `assets/ai-systems-lab.gif`, then inspect `https://github.com/aiis2` in a browser.

**Step 5: Report the published result**

Provide the live profile URL, summarize the visual/content choices, and mention the completed verification commands.
