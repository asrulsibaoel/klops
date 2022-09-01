# Klops Versioning  
Klops Versioning is a kind of version control based on DVC. It is a wrapper for [DVC](https://dvc.org). This wrapper aimed to make every DVC command become code minded.
```py
from klops.versioning import Versioning

versioning = Versioning()

# Add your DVC repository storage
versioning.add_remote("gs://your-bucket-name/your-path/")

# Track your file into dvc
versioning.add("myfile.csv")

# Run a pipeline
versioning.run("yourfile.sh", "your-pipeline-name", ["your", "dependencies"], ["your", "outputs"])

# Read a binary file
model = versioning.read_binary("file-path/file_binary.pkl")

# Read a dataset.
data = versioning.read_dataset("file-path/dataset.csv")

# Push your changes to DVC
versioning.push()
```   