
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Reference dataset
reference_data = pd.DataFrame({
    "age": [20, 22, 25, 28, 30],
    "salary": [20000, 25000, 30000, 35000, 40000]
})

# Current dataset
current_data = pd.DataFrame({
    "age": [35, 38, 40, 42, 45],
    "salary": [45000, 50000, 55000, 60000, 65000]
})

# Create Evidently report
report = Report(metrics=[
    DataDriftPreset()
])

# Generate report
result = report.run(
    reference_data=reference_data,
    current_data=current_data
)

# Save HTML report
result.save_html("monitoring_report.html")

print("Evidently monitoring completed!")
print("Monitoring report generated successfully!")
