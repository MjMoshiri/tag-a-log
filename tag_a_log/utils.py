from typing import Callable
import csv

def wrap_with_try_csv(func: Callable) -> Callable:
    def wrapped_function(filename: str):
        try:
            return func(filename)
        except FileNotFoundError:
            raise FileNotFoundError(f"file not found: {filename}")
        except csv.Error as e:
            raise ValueError(f"Error reading CSV file: {e}")
    return wrapped_function
