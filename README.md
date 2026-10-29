# LearningPython

A small, beginner-friendly project for learning Python one change at a time.

**All simulation timings are invented for practice. They are not actual FinitePDE.ai benchmarks.** This program compares numbers; it does not run a simulation or measure performance.

## Start on your Mac

1. Install a stable Python 3 release using the macOS installer from [python.org](https://www.python.org/downloads/macos/). Open the downloaded installer and follow its steps. If you already have Python 3, check it before installing again.
2. Open Terminal and type `python3 --version`. You should see a Python 3 version. If the command is not found, finish the installation, close Terminal, and open it again.
3. Install [Visual Studio Code](https://code.visualstudio.com/). In VS Code's Extensions view, install **Python** published by Microsoft.
4. Open [this repository](https://github.com/soniapal/LearningPython), choose **Code > Download ZIP**, and double-click the ZIP in Finder to extract it.
5. In VS Code, choose **File > Open Folder** and open the extracted folder containing this README and `lesson_01.py`.
6. Press **Command+Shift+P**, run **Python: Select Interpreter**, and choose your installed Python 3 interpreter.
7. Choose **Terminal > New Terminal**. Run the commands below in that terminal, from the project folder.

No extra packages, pip installation, or virtual environment are required for this lesson. Setup reference: [Microsoft's Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial).

## Run your first program

```bash
python3 lesson_01.py
```

Expected output:

```text
Illustrative timings only - not FinitePDE.ai benchmark results.
Conventional time (seconds): 120
AI time (seconds): 30
Time saved (seconds): 90
Time saved (%): 75.0
The AI simulation is faster in this example.
```

The conventional time is the baseline: (120 - 30) / 120 × 100 = 75%.
This means a 75% reduction in execution time in this invented example.

## Understand the program

Read `lesson_01.py` from top to bottom. Lines beginning with `#` are comments for people; Python ignores them. Blank lines separate ideas.

| Code or idea | Meaning |
| --- | --- |
| `conventional_time = 120` | Store the number 120 in a variable named conventional_time. |
| `ai_time = 30` | Store 30 in another variable. Use seconds for both. |
| `time_saved = conventional_time - ai_time` | Subtract AI time from conventional time. |
| `percentage_saved = time_saved / conventional_time * 100` | Divide by the baseline, then multiply by 100. |
| `print("AI time (seconds):", ai_time)` | Display a text label and the current value. Text needs quotes; a variable name does not. |
| `if ai_time < conventional_time:` | Run the indented instructions if AI time is smaller. |
| `elif ai_time == conventional_time:` | Otherwise, check whether the times are equal. |
| `else:` | Otherwise, run the remaining case: AI time is larger. |
| `<=` and `or` | Less than or equal to; either condition can be true. Used to reject invalid times. |
| `return` | Leave the function immediately, so invalid times never reach the division. |

Other arithmetic operators are `+` (addition) and `*` (multiplication). Python uses `/` for division, not the ÷ character.

### Two small pieces of reusable structure

`def compare_times(conventional_time, ai_time):` defines a **function**: a named group of instructions. The names in parentheses are its inputs (parameters). Defining it does not run it.

The bottom line, `compare_times(conventional_time, ai_time)`, calls that function using the two numbers you set above it.

`if __name__ == "__main__":` means "run this block when this file is executed directly." Leave this line unchanged for now. It lets the tests import the function without automatically running the example. Start your edits with the two numbers inside this block.

### Indentation is part of Python

Use **four spaces** for each level. The function body is indented four spaces. A print inside an if within the function is indented eight spaces. Each `elif` and `else` must line up with its matching `if`.

```python
if ai_time < conventional_time:
    print("AI is faster.")
else:
    print("AI is not faster.")
```

This shorter example combines equal and slower into the else case. The actual program uses `elif` to distinguish them.

## Avoid common errors

| Mistake | Fix |
| --- | --- |
| `else ai_time > conventional_time:` | Use `elif ai_time > conventional_time:` for a condition, or simply `else:` for the remaining case. |
| `if ai_time < conventional_time` | Add the colon at the end. |
| `if ai_time = conventional_time:` | Use `==` to compare. A single `=` assigns a value. |
| An unindented print after `if` | Indent the body four more spaces. |
| An `else:` indented differently from its `if` | Align the two keywords. Don't put an unrelated statement between their blocks. |
| `print("Hello)` | Close the quote and the parenthesis: `print("Hello")`. |
| `AI_time` instead of `ai_time` | Match capitalization exactly. |
| `ai_time = "30"` | Use the number `30`, without quotes. This lesson expects numeric inputs. |
| Pasting curly quotes such as “hello” into code | Use straight quotes: `"hello"`. |
| Mixing tabs and spaces | Use spaces consistently; VS Code can convert indentation to spaces. |

Read the last line of an error message first, then inspect the reported line and the line above it. SyntaxError often means a missing colon, quote, or parenthesis. IndentationError means the spacing structure is wrong. NameError usually means a name is misspelled or used before it is assigned.

If you see `>>>`, you are inside Python's interactive prompt. Type `exit()` before entering terminal commands. If Python cannot open the file, check that VS Code opened the folder containing `lesson_01.py`. Save changes with **Command+S** before running again.

## Practice

Open [EXERCISES.md](EXERCISES.md). Predict the output, change one thing, save, run, and compare your prediction. Restore 120 and 30 whenever you want the original example.

## Run the automated checks

```bash
python3 -m unittest discover -s tests -v
```

The tests use Python's built-in `unittest` module. They check faster, equal, slower, decimal, and invalid times, plus the original runnable example. A successful run ends with **OK**.

The tests import the same function you run, supply known inputs, and check the printed answers. They use `redirect_stdout` to capture printed text and `assertIn` to check expected phrases. These are supporting tools to explore later; you do not need to understand them before starting lesson 1.

Changing the two example numbers is encouraged. One test specifically checks the original 120/30 example, so that test will fail after you change those numbers. Restore them to pass the original checks, or update that test's expected answers intentionally. If you change printed messages, corresponding output checks may also need updating.

## Files

- `lesson_01.py`: the runnable program and comments.
- `EXERCISES.md`: small exercises, hints, and explained answers.
- `tests/test_lesson_01.py`: automated checks.
- `.gitignore`: keeps generated Python cache files out of future commits.

A useful next lesson is asking for numbers with `input()` and converting text to numbers. For now, build confidence editing the variables yourself.
