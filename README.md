# Traffic-data-analyzer

# 🚦 Traffic Analyzer

A simple Python project that analyzes traffic data from text files.  
Built as a student project to practice Python programming, testing, and CI/CD.

## ✨ Features
- Average cars per hour
- Ratio of empty measurements
- Maximum traffic in a time window
- Number of jams (three or more cars in a row)
- Longest jam length (bonus feature 🎁)

## 📂 Project Structure
src/traffic_analyzer/ → main source code
tests/ → test files and sample data
.github/workflows/ → CI/CD pipeline

## Run with CLI:
python -m traffic_analyzer.cli tests/data/sample/traffic_sample.txt --hour 8

## Run Test:
pytest

