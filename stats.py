import math
def calculateStats(numbers):
  # implement the computation of statistics here and return the results
  if not numbers:
    return {"avg": math.nan, "min": math.nan, "max": math.nan}
  
  return {
        "avg": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }
