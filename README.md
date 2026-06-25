# 🚦 Traffic Data Analyzer

A Python-based command-line application that analyzes traffic measurement data from a CSV file. The project demonstrates data processing, testing, and continuous integration using GitHub Actions.

## Features

* Calculate the average number of cars during a selected hour
* Determine the ratio of empty traffic measurements
* Find the maximum number of cars in a single measurement
* Detect the number of traffic jams (three or more consecutive cars)
* Find the longest traffic jam
* Command-line interface (CLI)
* Automated unit testing with **pytest**
* Continuous Integration using **GitHub Actions**

---

## Technologies Used

* Python 3
* Pytest
* Git & GitHub
* GitHub Actions (CI)

---

## Project Structure

```
traffic-data-analyzer/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── src/
│   └── traffic_analyzer/
│       ├── __init__.py
│       ├── core.py
│       └── cli.py
│
├── tests/
│   ├── data/
│   │   └── sample/
│   │       └── traffic_sample.csv
│   └── test_core.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Kaspersky006/traffic-data-analyzer.git
cd traffic-data-analyzer
```

Install the required package:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python -m traffic_analyzer.cli tests/data/sample/traffic_sample.csv --hour 8
```

---

## Run the Tests

```bash
pytest
```

---

## Continuous Integration

This project uses **GitHub Actions** to automatically:

* Install project dependencies
* Execute unit tests
* Verify that every push to the repository passes all tests

---

## Learning Outcomes

This project helped me practice:

* Python programming
* File handling
* Modular project structure
* Command-line interfaces
* Unit testing with pytest
* Git and GitHub
* Continuous Integration using GitHub Actions

---

## Future Improvements

* Generate graphical traffic reports
* Export analysis results to PDF
* Support additional traffic statistics
* Interactive web interface using Streamlit

