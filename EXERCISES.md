# Lesson 1 practice

All numbers here are illustrative, not real FinitePDE.ai results.
For each exercise: predict, edit, save, run. Change the two variables at the bottom of lesson_01.py unless told otherwise.

## 1. Change the inputs

Use conventional_time = 200 and ai_time = 50.
How many seconds and what percentage are saved?

Hint: subtract first, then divide by the conventional time and multiply by 100.

<details><summary>Answer and explanation</summary>

150 seconds and 75.0%. The calculation is (200 - 50) / 200 * 100. The faster branch runs because 50 is less than 200.

</details>

## 2. Take equal time

Set both times to 60. Predict the message.

<details><summary>Answer and explanation</summary>

0 seconds, 0.0%, and "Both simulations take the same time in this example."
The first condition is false; the elif equality condition is true.

</details>

## 3. Make AI slower

Use conventional_time = 40 and ai_time = 60.

<details><summary>Answer and explanation</summary>

-20 seconds and -50.0%. Negative savings mean the AI example takes 20 seconds longer, a 50% increase relative to the conventional baseline. Both earlier conditions are false, so else runs.

</details>

## 4. Fix a syntax error

In a separate scratch file, correct this snippet before running it:

```python
ai_time = 30
conventional_time = 120
if ai_time < conventional_time
print("AI is faster.")
else ai_time >= conventional_time:
    print("AI is not faster.")
```

Hint: there are three problems: a colon, indentation, and an else condition.

<details><summary>Correct version</summary>

```python
ai_time = 30
conventional_time = 120
if ai_time < conventional_time:
    print("AI is faster.")
else:
    print("AI is not faster.")
```

else has no condition. It covers all remaining cases. Both print lines are indented four spaces.

</details>

## 5. Try zero, then decimals

Try 0 and 30. Then try 2.5 and 1.0.

<details><summary>Answer and explanation</summary>

With 0 and 30, the program asks for positive times and returns before division. A conventional time of zero would make the percentage calculation invalid.

With 2.5 and 1.0, it reports 1.5 seconds saved and 60.0%. Decimal numbers are called floats. Some decimal calculations can display tiny rounding differences because computers store floats approximately.

</details>

## 6. Add a new calculation

Inside the function, immediately after percentage_saved is calculated, add a variable for conventional_time / ai_time. Print it with the label "Illustrative speedup factor:".

<details><summary>One solution</summary>

```python
    speedup = conventional_time / ai_time
    print("Illustrative speedup factor:", speedup)
```

Keep four spaces before these lines because they belong to the function. With 120 and 30, the factor is 4.0: the conventional example takes four times as long. This is different from the 75% reduction in time. The validation above already prevents division by zero for either input.

</details>

When done, restore 120 and 30 and run the tests. Optional extra: copy an existing test and add a check for the new speedup output.
