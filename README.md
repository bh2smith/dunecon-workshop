# Dune Con API Workshop

Tutorial for Dune Con 2022 on using Dune Analytics' officially supported API service.

[Slides from presentation](https://docs.google.com/presentation/d/1w6KsA9UIYZt71psmYrxvB-0nVNcgMdn60sWFe1UlFlM/edit?usp=sharing)

## Requirements

**python >= 3.9**

## Instructions

1. Installation & Setup

    ```shell
   git clone git@github.com:bh2smith/dunecon-workshop.git
   cd dunecon-workshop
   python3 -m venv venv
   source ./env/bin/activate
   pip install -r requirements.txt <--- Contains dune-client and python-dotenv
   cp .env.sample .env             <--- Copy your DUNE_API_KEY here
    ```

2. **Run the demo scripts**

    ```shell
    python -m 1-basic-fetch
    ```
3. Data Modeling & Scripting

   Sample Query: https://dune.com/queries/1247366 (DuneV2 Engine)

   Forked from Legacy: https://dune.com/queries/867367 (doesn't seem to agree)
   ```shell
   python -m 2-data-modeling
   ```

4. **Create a Dune Alert**

   Sample Query: https://dune.com/queries/1247175 (CoW Protocol Totals)

   ```shell
   docker run -v ${PWD}/3-volume-counter.yaml:/app/cfg \
      --env-file .env \
      ghcr.io/cowprotocol/dune-alerts:main \
      --query-config cfg
   ```

   **Note that**
    - To actually post an alert to slack, you would need to [create your own slackbot](https://api.slack.com/apps), but
      the script will run empty credentials until the last possible moment.
    - There is an [open issue](https://github.com/cowprotocol/dune-alerts/issues/33) to integrate Twitter, Telegram and
      Email.
