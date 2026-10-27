#!/usr/bin/env python3
"""
Automated Test Runner for IDCForge Pro
Verifies 2D DWT lifting transforms, perfect lossless reconstruction, bit-plane rate control, PSNR metrics, and 10-point normative auditor.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from idc_cli import forward53_1d, inverse53_1d, forward_dwt2d, inverse_dwt2d, generate_test_pattern, compress, audit

class TestIDCForge(unittest.TestCase):

    def setUp(self):
        self.w = 32
        self.h = 32
        self.img = generate_test_pattern(self.w, self.h)

    def test_01_dwt_1d_roundtrip(self):
        arr = [10, 25, 40, 55, 70, 85, 100, 115]
        coeffs = forward53_1d(arr)
        recon = inverse53_1d(coeffs)
        self.assertEqual(arr, recon)

    def test_02_dwt_2d_lossless_roundtrip(self):
        coeffs = forward_dwt2d(self.img, self.w, self.h, 3)
        recon = inverse_dwt2d(coeffs, self.w, self.h, 3)
        self.assertEqual(self.img, recon)

    def test_03_lossless_compression_metric(self):
        res = compress(self.img, self.w, self.h, lossless=True)
        self.assertIn("Lossless", res["psnr"])
        self.assertEqual(res["rmse"], 0.0)

    def test_04_rate_controlled_lossy_compression(self):
        res = compress(self.img, self.w, self.h, target_bpp=1.0)
        self.assertLessEqual(res["compressed_bytes"], res["original_bytes"])
        self.assertGreater(float(res["achieved_bpp"]), 0.0)

    def test_05_segment_header_sync_marker(self):
        res = compress(self.img, self.w, self.h)
        self.assertTrue(res["header_hex"].startswith("FF"))

    def test_06_compression_ratio_calculation(self):
        res = compress(self.img, self.w, self.h, target_bpp=0.5)
        self.assertTrue(":1" in res["compression_ratio"])

    def test_07_test_pattern_generation(self):
        pat = generate_test_pattern(16, 16)
        self.assertEqual(len(pat), 256)
        for p in pat:
            self.assertTrue(0 <= p <= 255)

    def test_08_normative_auditor_compliance(self):
        report = audit()
        self.assertEqual(report["status"], "PASSED")
        self.assertEqual(report["score"], "10/10 Normative Rules Compliant")
        self.assertEqual(len(report["rules"]), 10)

    def test_09_multi_level_subband_length(self):
        coeffs = forward_dwt2d(self.img, self.w, self.h, 3)
        self.assertEqual(len(coeffs), self.w * self.h)

    def test_10_extreme_dynamic_range_handling(self):
        black_img = [0] * (self.w * self.h)
        res = compress(black_img, self.w, self.h, lossless=True)
        self.assertIn("Lossless", res["psnr"])

if __name__ == "__main__":
    unittest.main()
