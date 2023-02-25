"""
https://gist.github.com/magdalini-anastasiadou/1d34fe7a4f54f0d263796bdf82dde81d
https://habr.com/ru/company/ruvds/blog/440654/
"""

import os
import uuid
import argparse
import pandas as pd

from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData


def csv_to_rasa_nlu():
    """Convert data from csv file to rasa NLU format"""
    parser = argparse.ArgumentParser(
        description="Convert data from csv file to rasa NLU"
    )
    parser.add_argument(
        "--file",
        type=str,
        help="csv file with two columns 'intent,message'",
        required=True,
    )
    parser.add_argument(
        "--nlu",
        type=str,
        help="Output folder for the NLU data.",
        default="data/nlu/",
        required=True,
    )
    parser.add_argument(
        "--format",
        type=str,
        help="Output format",
        required=False,
        default="md",
        choices=["md", "json", "yaml"],
    )

    args = parser.parse_args()
    df = pd.read_csv(args.file)
    messages = [
        Message.build(row["message"], row["intent"]) for _, row in df.iterrows()
    ]

    if not os.path.exists(args.nlu):
        os.makedirs(args.nlu)

    unique_filename = str(uuid.uuid4()) + "." + args.format

    with open(os.path.join(args.nlu, unique_filename), "w") as outfile:
        if args.format == "md":
            outfile.write(TrainingData(messages).nlu_as_markdown())
        elif args.format == "json":
            outfile.write(TrainingData(messages).nlu_as_json())
        else:
            outfile.write(TrainingData(messages).nlu_as_yaml())


if __name__ == "__main__":
    csv_to_rasa_nlu()