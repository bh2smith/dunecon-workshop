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