def run_timing():
    # Asks the user repeatedly for numeric input. Prints the average time an
    # d number of runs.
    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 km run time: ')
        # If one_run is an empty string, stop.
        if not one_run:
            break
        # it’s an infinite loop! It might seem weird to have
        # “while True,” and it’s a very bad idea to have such a loop
        # without any “break” statement to exit when a condition
        # is reached. But as a general way of getting an unknown
        # number of inputs from the users, I think it’s totally fine.

        number_of_runs += 1
        total_time += float(one_run)

    average_time = total_time / number_of_runs
    print(f'Average of {average_time}, over {number_of_runs} runs')


run_timing()
