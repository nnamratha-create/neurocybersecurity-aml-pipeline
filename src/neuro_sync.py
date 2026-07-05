import numpy as np

class NeuralTelemetrySynchronizer:
    def __init__(self):
        print("[INFO] Initializing Neural Telemetry Synchronizer...")

    def align_time_series(self, raw_neural_data: dict) -> np.ndarray:
        """Converts raw signal lists into organized mathematical matrices."""
        matrix = np.array(raw_neural_data.get("signal_matrix", []))
        channels = raw_neural_data.get("channels", [])
        
        print(f"[SUCCESS] Array Aligned: {matrix.shape[0]} frames across {len(channels)} channels.")
        return matrix
