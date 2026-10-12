import statistics

data = [45, 67, 89, 23, 76, 90, 55]

print("Mini Data Analyzer")
print("------------------")
print("Total Values:", len(data))
print("Mean:", round(statistics.mean(data), 2))
print("Median:", statistics.median(data))
print("Maximum:", max(data))
print("Minimum:", min(data))
print("Standard Deviation:", round(statistics.stdev(data), 2))
