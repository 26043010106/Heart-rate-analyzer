import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "sample_data.csv"


def analyze_signal(file_path=DATA_FILE):
    data = pd.read_csv(file_path)
    time = data["time_seconds"].to_numpy()
    signal = data["pulse_signal"].to_numpy()

    # Simple peak detection: local maximum above a threshold.
    threshold = 0.65
    min_gap_seconds = 0.45  # avoids counting the same beat twice
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > threshold and signal[i] >= signal[i - 1] and signal[i] > signal[i + 1]:
            if not peaks or time[i] - time[peaks[-1]] >= min_gap_seconds:
                peaks.append(i)

    if len(peaks) >= 2:
        intervals = [time[peaks[j]] - time[peaks[j - 1]] for j in range(1, len(peaks))]
        bpm = 60 / (sum(intervals) / len(intervals))
    elif len(peaks) == 1:
        bpm = 60.0  # only one detected beat; use a simple fallback estimate
    else:
        bpm = 0.0

    if bpm == 0:
        category = "No beats detected"
    elif bpm < 60:
        category = "Low (below 60 BPM)"
    elif bpm <= 100:
        category = "Normal resting range (60–100 BPM)"
    else:
        category = "High (above 100 BPM)"

    print(f"Detected beats: {len(peaks)}")
    print(f"Estimated heart rate: {bpm:.1f} BPM")
    print(f"Category: {category}")

    plt.figure(figsize=(10, 4))
    plt.plot(time, signal, label="Simulated pulse signal")
    if peaks:
        plt.scatter(time[peaks], signal[peaks], label="Detected beats")
    plt.axhline(threshold, linestyle="--", label="Detection threshold")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Signal amplitude")
    plt.title("Simulated Heartbeat Signal Analysis")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("heartbeat_plot.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    analyze_signal()
