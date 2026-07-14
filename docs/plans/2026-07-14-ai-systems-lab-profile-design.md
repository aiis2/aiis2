# AI Systems Lab GitHub Profile Design

## Goal

Turn the empty `aiis2` GitHub profile into a distinctive bilingual identity that combines a full-stack AI engineer with a future-facing independent lab. The profile should feel cinematic and technical without becoming noisy, slow, or dependent on fragile third-party cards.

## Visual Direction

The visual system is named **AI Systems Lab**. It uses a near-black background, cyan and electric-green signals, crisp white typography, fine grid lines, and restrained terminal motifs. A custom wide hero image establishes the brand as `AIIS2 // AI SYSTEMS LAB` and depicts an abstract intelligent data core rather than a generic stock illustration.

Motion is purposeful and lightweight: a short seamless hero loop adds scanning light, flowing data, subtle particles, and status pulses. It must remain legible when viewed as a static first frame and should avoid rapid flashes.

## Content Architecture

1. **Hero signal**: animated custom hero with the AI Systems Lab identity.
2. **System profile**: concise English positioning followed by a Chinese translation.
3. **Current signals**: a compact terminal-style block describing current focus areas.
4. **Project matrix**: three selected public projects with clear outcomes and repository links: Datell, Risk Agent, and Frontend Design Report.
5. **Technology stack**: grouped badges for AI systems, application engineering, and platform tools.
6. **Footer status**: direct GitHub contact and a minimal signal animation.

## Assets And Hosting

All custom assets live in the profile repository under `assets/`. The hero is generated as a high-resolution raster image, then adapted into an optimized animated format. Repository-hosted assets are preferred over external widget services so the page remains stable.

The README uses GitHub-compatible Markdown and limited HTML only for alignment and responsive image markup. It does not rely on custom JavaScript, which GitHub README pages do not execute.

## Resilience

- The animation has a meaningful static first frame and descriptive alt text.
- Asset paths are relative so forks and local previews remain coherent.
- Animation size is kept modest to reduce slow loading.
- No essential information is embedded only inside the image.
- Public repository links are checked before publishing.
- Unsupported HTML, CSS, and scripts are avoided.

## Verification

- Render the README locally and inspect desktop and narrow-width screenshots.
- Confirm generated assets are nonblank, correctly cropped, and readable.
- Check Markdown links and repository asset paths.
- Push the special `aiis2/aiis2` public repository and confirm GitHub recognizes it as the profile README.
- Inspect the live profile for image loading, animation playback, text hierarchy, and mobile wrapping.

## Success Criteria

The live `github.com/aiis2` profile immediately communicates AI Systems Lab, presents an English-Chinese engineering identity, highlights the strongest public work, and delivers a polished motion-led technology aesthetic without sacrificing readability or reliability.
