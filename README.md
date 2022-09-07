# dunecon-workshop

Dune client tutorial for Dune Con 2022

1. **Clone this repo**

    ```shell
    git clone git@github.com:bh2smith/dunecon-workshop.git
    ```

2. **Install `dune-client`**

    ```shell
    pip install -r requirements.txt
    ```
   note that this also comes along with `python-dotenv` for reading env files.

3. **Create and .env file with `DUNE_API_KEY`**

    ```shell
    touch .env
    ```

   and append `DUNE_API_KEY=xxxxYOURxAPIxKEYxxx`

4. **Run the demo scripts**

    ```shell
    python -m 1-basic-fetch
    ```

5. **Create a Dune Alert**

   Sample Query: https://dune.com/queries/1247175 (CoW Protocol Totals)

   ```shell
   docker run -v ${PWD}/2-volume-counter.yaml:/app/cfg \
      --env-file .env \
      ghcr.io/cowprotocol/dune-alerts:main \
      --query-config cfg
   ```

   Note that
    - You would need to [create your own slackbot](https://api.slack.com/apps), but can use empty env vars for now.
    - There is an [open issue](https://github.com/cowprotocol/dune-alerts/issues/33) to integrate Twitter and Telegram.
