# Configuring your instance

First of all, what do you want your instance to be? You can set appropriate `AppConfig` settings.

- General forum/link aggregator (people are allowed to post text and links). This is the default.
- General forum, no links. In your `AppConfig` set `ENABLE_URL_POSTING = False`.
- Anything, but no karma. In your `AppConfig` set `ENABLE_KARMA = False`.
- Anything, but no visible karma. In your `AppConfig` set `VISIBLE_KARMA = False`.
- Anything, but want to rank by time (last activity) instead of karma: define the method `post_ranking` to return `tade.voting.TemporalRanking()` instead of `tade.voting.KarmaRanking()`
- Anything with a mailing list mode: set `MAILING_LIST = True`. You can customize `MAILING_LIST_ID`, `MAILING_LIST_ADDRESS` and `MAILING_LIST_FROM` too. (See comments on `tade/apps.py`)

## Branding

- Instance name: set `verbose_name = "new name"` and `subtitle = "lorem
  ipsum"`. Optionally set theme hex colors with `THEME_COLOR_HEX` and
  `DARK_THEME_COLOR_HEX` options.
- You can rename core models like `Story`, `Comment`, `Taggregation` to
  something else by overriding the `MODEL_VERBOSE_NAMES` dict in `AppConfig`.
  See `tade/apps.py` for an example.
- To override `tade` templates, setup a root dir called `templates` in your
  project and place a dir called `tade` in it. There you can override templates
  using the same hierarchy in the `tade` source code. In your django
  `settings.py`, `TEMPLATES...DIR ` must be equal to `[ BASE_DIR / "templates"
  / "tade" ]` for this to work.


## Managing registrations

- You can disable free registrations with flag `ALLOW_REGISTRATIONS`.
- You can enable invitation requests with flag `ALLOW_INVITATION_REQUESTS`. People will submit a form with why they want to join and users can select if they want to invite them or not.
- You can require manual approval for new users without requests to participate by requiring a vouch (essentially an invitation request for an already registered user) by setting the flag `REQUIRE_VOUCH_FOR_PARTICIPATION`.
