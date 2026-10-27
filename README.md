\# IDCForge Pro (v1.0.0)  
\#\#\# CCSDS 122.0-B-2 & ISO 15887 Spacecraft Payload Image Data Compression Studio & Bit-Plane Encoder (BPE)

IDCForge Pro is an aerospace-grade developer studio, 2D Discrete Wavelet Transform (DWT) engine, Bit-Plane Encoder (BPE), rate-scalable embedded bitstream serializer, and 10-point normative compliance auditor designed for spacecraft imaging instruments, Earth observation constellations, planetary probes, and ground reception processing pipelines.

\---

\#\# 🌟 Key Capabilities  
\- \*\*2D Discrete Wavelet Transform (DWT)\*\*: 3-level dyadic Mallat subband decomposition implementing both reversible 5/3 integer LeGall lifting (for mathematically lossless compression) and 9/7 floating-point filters.  
\- \*\*Bit-Plane Encoder (BPE)\*\*: 8x8 coefficient block grouping, DC coefficient spatial prediction, AC significance mapping, sign bit isolation, and magnitude refinement bit coding.  
\- \*\*Embedded Rate-Scalable Bitstreams\*\*: Monotonic MSB-to-LSB bit-plane transmission allowing exact telemetry downlink budget enforcement (0.5 to 4.0 bpp or lossless).  
\- \*\*CCSDS Segment Header Serialization\*\*: Bit-exact packing of Part 1A (Essential header with \`0xFF\` sync marker), Part 1B (Image geometry), Part 2 (DWT parameters), Part 3 (Segment blocks), and Part 4 (Rate control).  
\- \*\*Objective Quality Analyzer\*\*: Computes real-time Peak Signal-to-Noise Ratio (PSNR in dB), Root Mean Square Error (RMSE), and Mean Squared Error (MSE).  
\- \*\*10-Point Normative Auditor\*\*: Automated verification engine covering rules \`IDC-001\` through \`IDC-010\` per CCSDS 122.0-B-2 Blue Book specifications.

\---

\#\# 📂 Project Structure  
\`\`\`text  
idc-forge-pro/  
├── source-code/  
│   ├── idc-engine.js           \# Core 2D DWT, BPE, rate controller & PSNR engine  
│   ├── idc-auditor.js          \# 10-point normative compliance auditor  
│   ├── idc\_cli.py              \# Python 3 CLI executable  
│   ├── idc-cli.py              \# Python 3 CLI alias  
│   ├── test\_runner.py          \# 10-suite unit test runner  
│   └── index.html              \# Interactive Mission Control operations console  
├── build/  
│   └── idc-forge-pro-v1.0.0.zip \# Standalone production bundle  
├── documentation/  
│   ├── CCSDS\_IDC\_SPECIFICATION.md \# Normative protocol specification  
│   └── IDC\_COMPLIANCE\_MATRIX.md   \# 10-point requirement traceability  
└── screenshots/  
    ├── architecture-diagram.svg   \# System architecture diagram  
    └── idc-studio-preview.svg     \# Operations studio interface preview  
\`\`\`

\---

\#\# 🚀 Quick Start

\#\#\# Running Automated Tests  
\`\`\`bash  
python3 source-code/test\_runner.py \-v  
\`\`\`

\#\#\# Command Line Interface  
\`\`\`bash  
\# Compress synthesized space pattern to 1.0 bpp  
python3 source-code/idc\_cli.py \--mode compress \--width 64 \--height 64 \--bpp 1.0

\# Compress in exact lossless mode (5/3 Integer DWT)  
python3 source-code/idc\_cli.py \--mode compress \--width 64 \--height 64 \--lossless

\# Run 10-Point Normative Compliance Audit  
python3 source-code/idc\_cli.py \--mode audit  
\`\`\`

\#\#\# Launching the Web Operations Console  
Open \`source-code/index.html\` in any web browser for interactive side-by-side raw sensor and reconstructed image previews, DWT subband visualization, and real-time audit scoring.  
