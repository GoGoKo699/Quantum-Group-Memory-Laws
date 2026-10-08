"""Infrastructure controls only; original scientific suites remain unchanged."""
from pathlib import Path
import json
import sys
import unittest
import tempfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import verify as v

class RepositoryTests(unittest.TestCase):
    def test_01_all_archive_bytes_and_nested_manifests(self):
        r=v.verify_provenance();self.assertEqual(r['archive_members'],79);self.assertEqual(r['nested_manifests'],5)
    def test_02_document_hashes_and_links(self):
        self.assertGreater(v.verify_docs()['local_document_links'],35)
    def test_03_comparison_records_roundoff(self):
        changes=v.compare_reports({'x':1.0,'ok':True,'n':4},{'x':1.0+1e-13,'ok':True,'n':4})
        self.assertEqual(len(changes),1)
    def test_04_comparison_rejects_wrong_discrete_or_large_values(self):
        for a,b in [(True,1),(4,5),('true','false'),([1],[1,2]),({'a':1},{'b':1}),(1.0,1.001),(1.0,float('nan'))]:
            with self.subTest(a=a,b=b), self.assertRaises(AssertionError):v.compare_reports(a,b)
    def test_05_safe_paths_reject_traversal(self):
        for p in ('../escape','/absolute','a/../../escape','a\\b',''):
            with self.subTest(p=p), self.assertRaises(ValueError):v.safe_path(ROOT,p)
    def test_06_output_cannot_overwrite_sources(self):
        for p in (ROOT,ROOT/'research',ROOT/v.ARCHIVE):
            with self.subTest(p=p), self.assertRaises(ValueError):v.output_location(p)
        self.assertEqual(v.output_location(ROOT/'build/test'),(ROOT/'build/test').resolve())
    def test_07_five_unchanged_suite_paths(self):
        self.assertEqual(sum(s[3] for s in v.SUITES),24)
        for _,s,r,_ in v.SUITES:
            self.assertTrue((ROOT/v.ARCHIVE/s).is_file());self.assertTrue((ROOT/v.ARCHIVE/r).is_file())
    def test_08_scope_and_current_identity(self):
        self.assertIn('GoGoKo699/Quantum-Group-Memory-Laws',(ROOT/'AGENTS.md').read_text())
        self.assertIn('q>q_0',(ROOT/'research/MODEL_AND_CLAIMS.md').read_text())
        self.assertIn('ordinary physical',(ROOT/'research/MODEL_AND_CLAIMS.md').read_text())
    def test_09_no_third_party_binary_or_bootstrap_payload(self):
        names=v.source_files(ROOT)
        self.assertFalse(any(n.endswith(('.pdf','.zip','.xz','.b64')) or n.startswith('.bootstrap/') for n in names))
    def test_10_contact_and_original_license(self):
        self.assertIn('[gogoko699@gmail.com](mailto:gogoko699@gmail.com)',(ROOT/'README.md').read_text())
        self.assertIn('Copyright (c) 2026 Ruge Lin',(ROOT/'LICENSE').read_text())

if __name__=='__main__':unittest.main()
