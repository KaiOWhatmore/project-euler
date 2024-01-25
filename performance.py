from Benchmarking.profiling.intrusive import collect_measurements
from Benchmarking import benchmark as mb


# decorate your function to be able to collect measurements.
@collect_measurements(test_case_name="decorated_function", enabled=True)
def slow_method():
    num = 6 ** 6 ** 6
    return len(str(num))


# Run your method.
slow_method()

# Interact with the micro benchmarking object to extract information.
print(mb.test_id)
print(mb.test_case_name)
print(mb.regression.letter_rank)
