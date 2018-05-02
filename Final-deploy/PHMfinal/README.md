# optimus

By default we use online Postresql DB, which is hardcoded in `settings.py`.

If you want to use a local DB, create a `local_settings.py` file in the `optimus` package and specify your local DB settings their.
They would override the settings in the main `settings.py` module.