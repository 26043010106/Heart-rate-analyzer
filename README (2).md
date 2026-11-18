# Heart Rate Analyzer (Beginner Bioengineering Project)

## Overview
This beginner-friendly project analyzes a **simulated pulse waveform**. It detects waveform peaks, estimates heart rate in beats per minute (BPM), categorizes the estimate, and plots the signal.

> Educational simulation only. It is not a medical device and must not be used to diagnose health conditions.

## Files
- `heart_rate_analyzer.py` — Python signal analysis and graphing
- `sample_data.csv` — simulated pulse waveform data
- `requirements.txt` — Python packages needed
- `build_simulink_model.m` — MATLAB script that builds a simple Simulink pulse generator model
- `Project_Report.docx` / `Project_Report.pdf` — project report

## Run the Python program
1. Install Python 3.
2. Open a terminal in this folder.
3. Install packages: `pip install -r requirements.txt`
4. Run: `python heart_rate_analyzer.py`

The program prints detected beat count, estimated BPM and category, and saves a graph as `heartbeat_plot.png`.


## Simulink model
Open MATLAB with Simulink installed. Run `build_simulink_model.m`. The script creates a simple pulse generator connected to a Scope and a To Workspace block, then saves a model named `HeartRatePulseModel.slx` in the current folder. The Simulink model demonstrates pulse generation; the Python script performs the BPM estimate.


## Method (simple peak detector)
1. Read the time and pulse amplitude columns.
2. Look for a local maximum above the detection threshold.
3. Keep detected peaks separated by a minimum time interval.
4. Estimate BPM from the average interval between peaks: `BPM = 60 / average beat interval (seconds)`.
5. Categorize the result using simple resting-rate bands.

## Limitations
- Data is synthetic, not collected from a person.
- Peak detection is intentionally basic and may not work for noisy real ECG/PPG signals.
- Resting heart-rate bands are simplified; age, activity, symptoms and clinical context matter.
