# ipsos-checker

A lightweight python tool using playwright to check job listings for specific postcodes on [iShopForIpsos](https://uk.ishopforipsos.com).

## Running

Use `run.ps1` to start the script.
This automatically sets up the virtual environment and installs any missing dependencies.

## Environment

Environment variables must be set to configure the script:

- `IPSOS_EMAIL` containing you Ipsos account email account.
- `IPSOS_PASSW` containing your Ipsos account password.
- `POSTCODE` containing the postcode to search for.

## License

[Apache License 2.0](LICENSE)
