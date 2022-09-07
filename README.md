# Dune Con API Workshop

Tutorial for Dune Con 2022 on using Dune Analytics' officially supported API service.

[Slides from presentation](https://docs.google.com/presentation/d/1w6KsA9UIYZt71psmYrxvB-0nVNcgMdn60sWFe1UlFlM/edit?usp=sharing)

## Requirements

**python >= 3.9**

## Instructions

1. **Clone this repo**

    ```shell
    git clone git@github.com:bh2smith/dunecon-workshop.git
    ```

2. **Install Dune Client**

    ```shell
    pip install -r requirements.txt
    ```
   Note that this also comes along with `python-dotenv` for reading env files.

3. **Create and .env file with `DUNE_API_KEY`**

    ```shell
    mv .env.sample .env
    ```

   and add your `DUNE_API_KEY=xxxxYOURxAPIxKEYxxx` (slack vars can be left empty - but not removed)

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

   **Note that**
    - You would need to [create your own slackbot](https://api.slack.com/apps), but can use empty env vars for now.
    - There is an [open issue](https://github.com/cowprotocol/dune-alerts/issues/33) to integrate Twitter and Telegram.

6. Data Modeling and Scripting

   Sample Query: https://dune.com/queries/1247366 (DuneV2 Engine)

   Forked from Legacy: https://dune.com/queries/867367 (doesn't seem to agree)
   ```shell
   python -m 3-data-modeling
   ```