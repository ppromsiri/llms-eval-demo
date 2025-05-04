import pandas as pd
import phoenix as px
from phoenix.otel import register

client = px.Client()


def create_dataset():
    # Example usage
    dataset_df = pd.read_csv(
        # "src/agentic/data/default_character_evaluation.csv"
        "src/agentic/data/mage_character_evaluation.csv"
    )

    client.upload_dataset(
        dataframe=dataset_df,
        dataset_name="mage_character",
        input_keys=["user_query"],
        output_keys=["expected_response"],
    )


if __name__ == "__main__":
    create_dataset()
