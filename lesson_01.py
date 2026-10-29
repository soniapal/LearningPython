# These timings are illustrative, not actual FinitePDE.ai benchmarks.
# All times are in seconds.


def compare_times(conventional_time, ai_time):
    # A function groups instructions so we can reuse them with different numbers.
    print("Illustrative timings only - not FinitePDE.ai benchmark results.")

    # Reject zero or negative times before doing division.
    if conventional_time <= 0 or ai_time <= 0:
        print("Please use positive times greater than zero.")
        return

    time_saved = conventional_time - ai_time
    percentage_saved = time_saved / conventional_time * 100

    print("Conventional time (seconds):", conventional_time)
    print("AI time (seconds):", ai_time)
    print("Time saved (seconds):", time_saved)
    print("Time saved (%):", percentage_saved)

    if ai_time < conventional_time:
        print("The AI simulation is faster in this example.")
    elif ai_time == conventional_time:
        print("Both simulations take the same time in this example.")
    else:
        print("The AI simulation is slower in this example.")


# This block runs when you execute this file, but not when tests import it.
if __name__ == "__main__":
    conventional_time = 120
    ai_time = 30
    compare_times(conventional_time, ai_time)
