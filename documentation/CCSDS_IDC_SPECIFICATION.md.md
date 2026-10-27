\# CCSDS 122.0-B-2 Spacecraft Image Data Compression Specification

\#\# 1\. Overview & Operational Scope  
The \*\*Consultative Committee for Space Data Systems (CCSDS)\*\* Recommendation \*\*CCSDS 122.0-B-2\*\* (and international standard \*\*ISO 15887\*\*) defines an image compression algorithm designed specifically for spacecraft payload instruments (optical cameras, imaging spectrometers, star trackers, and planetary probes).

The standard addresses the severe computational, memory, and telemetry bandwidth constraints of satellite flight hardware by combining:  
1\. \*\*2D Discrete Wavelet Transform (DWT)\*\*: A 3-level Mallat tree decomposition using either the reversible \*\*5/3 Integer filter\*\* (for exact lossless reconstruction) or the \*\*9/7 Float filter\*\* (for high-efficiency lossy compression).  
2\. \*\*Bit-Plane Encoder (BPE)\*\*: An embedded block-based bit-plane coder operating on 8x8 coefficient blocks that outputs rate-scalable, embedded bitstreams allowing exact telemetry bandwidth targeting.

\---

\#\# 2\. 2D Discrete Wavelet Transform Stage  
\- \*\*Decomposition\*\*: 3 dyadic levels generating 10 subbands: LL3, HL3, LH3, HH3, HL2, LH2, HH2, HL1, LH1, HH1.  
\- \*\*5/3 LeGall Integer Lifting Steps\*\*:  
  \- Prediction: \$d\[n\] \= x\[2n+1\] \- \\lfloor (x\[2n\] \+ x\[2n+2\])/2 \\rfloor\$  
  \- Update: \$s\[n\] \= x\[2n\] \+ \\lfloor (d\[n-1\] \+ d\[n\] \+ 2)/4 \\rfloor\$  
\- \*\*9/7 Antonini Float Lifting Steps\*\*:  
  \- Implements 4 lifting steps and scaling factors for optimal rate-distortion performance.

\---

\#\# 3\. Segment Header Architecture  
A compressed bitstream is partitioned into independent segments (typically 16 to 4096 blocks) to limit error propagation across cosmic-ray induced bit flips:  
\- \*\*Part 1A (Essential Header)\*\*: Start of Segment marker (\`0xFF\`), 8-bit segment counter, header part presence flags.  
\- \*\*Part 1B\*\*: Image Width (16 bits), Height (16 bits), Dynamic Range (8 bits).  
\- \*\*Part 2\*\*: DWT Filter Type (5/3 vs 9/7), Signed/Unsigned, Decomposition Levels (3).  
\- \*\*Part 3\*\*: Segment block count and DC quantization select.  
\- \*\*Part 4\*\*: Rate control and maximum byte limit.  
