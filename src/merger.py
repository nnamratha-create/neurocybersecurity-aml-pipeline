import json
from ingestion import FinancialIngestionNode
from neuro_sync import NeuralTelemetrySynchronizer

class DeterministicTensorMerger:
    def __init__(self):
        self.tx_node = FinancialIngestionNode()
        self.neuro_node = NeuralTelemetrySynchronizer()

    def construct_state_space_packet(self, data_path: str):
        """Loads data, maps tokens, and creates the unified tensor packet."""
        # Load sample mock data
        with open(data_path, 'r') as file:
            payload = json.load(file)

        # Process both pipelines
        tx_state = self.tx_node.parse_transaction(payload)
        neuro_matrix = self.neuro_node.align_time_series(payload["neural_telemetry"])

        # Construct final state packet
        unified_packet = {
            "metadata": tx_state,
            "neural_tensor_shape": neuro_matrix.shape,
            "status": "READY_FOR_INFERENCE_ENGINE"
        }
        
        print(f"\n[PIPELINE COMPLETE] Generated State Space Packet:")
        print(json.dumps(unified_packet, indent=2))
        return unified_packet

if __name__ == "__main__":
    merger = DeterministicTensorMerger()
    merger.construct_state_space_packet("data/sample_payload.json")
