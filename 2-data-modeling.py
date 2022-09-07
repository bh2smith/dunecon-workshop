from __future__ import annotations
from dataclasses import dataclass

import dotenv
import os

from dune_client.types import QueryParameter, Address, DuneRecord
from dune_client.client import DuneClient
from dune_client.query import Query


@dataclass
class LiquidityProvider:
    # pool: Address
    account: Address
    staked: float
    unstaked: float
    total: float

    @classmethod
    def from_results(cls, recs: list[DuneRecord]) -> list[LiquidityProvider]:
        return [
            LiquidityProvider(
                # pool=Address(r[]),
                account=Address(r["account"]),
                staked=float(r["staked"]),
                unstaked=float(r["unstaked"]),
                total=float(r["total"]),
            )
            for r in recs
        ]

    def __str__(self):
        return (
            f"LiquidityProvider("
            f"account={self.account}, "
            f"staked={self.staked}, "
            f"unstaked={self.unstaked}, "
            f"total={self.total})"
        )


if __name__ == "__main__":
    # DuneV2 Engine: https://dune.com/queries/1247366
    # Forked from Legacy: https://dune.com/queries/867367 (doesn't seem to agree)
    query = Query(
        name="Balancer LP Token Balances",
        query_id=867367,
        # query_id=1247366,  # V2 Engine Fork
        params=[
            QueryParameter.text_type(
                name="PoolAddress", value="0xde8C195Aa41C11a0c4787372deFBbDdAa31306D2"
            ),
            QueryParameter.text_type(
                name="StakingContract",
                value="0x158772f59fe0d3b75805fc11139b46cbc89f70e5",
            ),
        ],
    )

    dotenv.load_dotenv()
    dune = DuneClient(os.environ["DUNE_API_KEY"])
    print("Refreshing query at", query.url())
    raw_results = dune.refresh(query)
    print(f"Got {len(raw_results)} results from query")
    lp_holders = LiquidityProvider.from_results(raw_results)
    print("Parsed results:", list(map(str, lp_holders)))
