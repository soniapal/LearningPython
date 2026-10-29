"""Small output checks for lesson 1; no third-party packages needed."""

import io
from contextlib import redirect_stdout
from pathlib import Path
import subprocess
import sys
import unittest

from lesson_01 import compare_times


class LessonTests(unittest.TestCase):
    def output_for(self, conventional_time, ai_time):
        output = io.StringIO()
        with redirect_stdout(output):
            compare_times(conventional_time, ai_time)
        return output.getvalue()

    def test_faster(self):
        output = self.output_for(200, 50)
        self.assertIn("Time saved (seconds): 150\n", output)
        self.assertIn("Time saved (%): 75.0\n", output)
        self.assertIn("The AI simulation is faster", output)
        self.assertIn("not FinitePDE.ai benchmark results", output)

    def test_equal(self):
        output = self.output_for(60, 60)
        self.assertIn("Time saved (seconds): 0\n", output)
        self.assertIn("Time saved (%): 0.0\n", output)
        self.assertIn("Both simulations take the same time", output)

    def test_slower(self):
        output = self.output_for(40, 60)
        self.assertIn("Time saved (seconds): -20\n", output)
        self.assertIn("Time saved (%): -50.0\n", output)
        self.assertIn("The AI simulation is slower", output)

    def test_decimal_times(self):
        output = self.output_for(2.5, 1.0)
        self.assertIn("Time saved (seconds): 1.5\n", output)
        self.assertIn("Time saved (%): 60.0\n", output)

    def test_invalid_times(self):
        for conventional_time, ai_time in [(0, 30), (120, 0), (-1, 30), (120, -1)]:
            with self.subTest(conventional_time=conventional_time, ai_time=ai_time):
                output = self.output_for(conventional_time, ai_time)
                self.assertIn("Please use positive times greater than zero.", output)
                self.assertNotIn("Time saved", output)

    def test_original_program_runs(self):
        project_folder = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [sys.executable, str(project_folder / "lesson_01.py")],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Time saved (seconds): 90\n", result.stdout)
        self.assertIn("Time saved (%): 75.0\n", result.stdout)
        self.assertIn("The AI simulation is faster", result.stdout)
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
