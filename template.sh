# Creating directories
mkdir -p data
mkdir -p src

# Creating top-level files
touch .gitignore
touch requirements.txt
touch .env.example

# Creating data files
touch data/mock_jobs.json

# Creating source files
touch src/__init__.py
touch src/schemas.py
touch src/job_provider.py
touch src/matcher.py
touch src/explainer.py
touch src/app.py 

echo "Directory and files created successfully!"