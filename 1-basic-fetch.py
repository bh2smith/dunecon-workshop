import dotenv
import os

from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import Query

if __name__ == "__main__":
    query = Query(
        name="Sample Query",
        query_id=1215383,
        params=[
            QueryParameter.text_type(name="TextField", value="Word"),
            QueryParameter.number_type(name="NumberField", value=3.1415926535),
            QueryParameter.date_type(name="DateField", value="2022-05-04 00:00:00"),
            QueryParameter.enum_type(name="ListField", value="Option 1"),
        ],
    )

    dotenv.load_dotenv()
    dune = DuneClient(os.environ["DUNE_API_KEY"])
    print("Fetched results:", dune.refresh(query))

    print("Also available at", query.url())
