# Discord Sandwich Bot
## Under Development
Not nearly usable and most features don't exist yet so don't bother trying to use in production.
## Goals:
- A bot from which users can "order" sandwiches
- "chefs" in the official server make (photoshop) and deliver them to the server they were ordered from

Yes, I know bots like this already exist, however most are now defunct and the only one still active just doesn't do it the way I like
## Running the bot
First note that in it's current state the bot is a simple test (pretty much equivalent to a Hello World) and is not ready to be used at all

Also, don't worry about removing your bot token and db information before pushing. The gitignore is set to ignore config.py.
### Heroku
The bot is preconfigured to be run in a Heroku app, however in it's current state there is no reason to do that as it cannot be used in production.

Nonetheless, if for some reason you still want to run it in Heroku, it's very simple.

1. Fork this repository as **private** (very important as otherwise your bot token will be exposed
2. Rename `config.example.py` to `config.py` and insert details into the fields
3. Create a new heroku app and link it to your fork (the creation wizard will prompt you to do so)
4. Add one dyno to the worker process

Your bot should now be running.

### Running manually
If you want to run the bost locally or on a non-heroku server, it's very easy. First, install the (very few) dependencies.
 
#### Dependencies:
```
Python => 3.9.7
Nextcord => 2.0.0a3
mysql-connector-python => 8.0.27
MySQL or MariaDB, with an empty database and full write access
```

To run the bot:
1. Rename `config.example.py` to `config.py` and insert details into the fields
2. **OPTIONAL:** Remove the Heroku environment files (`Procfile`, `requirements.txt`, and `runtime.txt`)
3. Run main.py


