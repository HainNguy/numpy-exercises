
import numpy as np

# Spalten:
# 0: duration_ms
# 1: rows_read
# 2: rows_written
# 3: error_count

etl_jobs = np.array([
    [1200, 10000, 9950, 50],
    [1800, 15000, 14800, 200],
    [900,   8000, 8000, 0],
    [2500, 20000, 19500, 500],
    [1100, 12000, 11900, 100],
    [3000, 25000, 24500, 500]
])

# Teil A
print('shape:', etl_jobs.shape)
print('dim:', etl_jobs.ndim)
print('size:', etl_jobs.size)
print('data type:', etl_jobs.dtype)
print('Anzahl der ETL-Jobs:', etl_jobs.shape[0])

# Teil B

