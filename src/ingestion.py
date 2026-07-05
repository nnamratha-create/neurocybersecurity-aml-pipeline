import json

class FinancialIngestionNode:
    def __init__(self):
        print("[INFO] Initializing Financial Event Ingestion Node...")

    def parse_transaction(self, raw_payload: dict) -> dict:
        """Extracts standard compliance tokens from financial metadata."""
        tx_metadata = {
            "tx_id": raw_payload.get("transaction_id"),
            "value": raw_payload.get("amount_usd"),
            "timestamp": raw_payload.get("timestamp")
        }
        print(f"[SUCCESS] Parsed Transaction State: {tx_metadata['tx_id']}")
        return tx_metadata
