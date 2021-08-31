<p align="center">
<img alt="tade - web/mailing list/nntp discussions" title="tade - web/mailing list/nntp discussions" width="321" height="166" src="./tade_logo.svg">
</p>

<p align="center">
<a href="https://github.com/epilys/tade/blob/main/LICENSE"><kbd><b>AGPL-3.0</b></kbd></a> <a href="https://www.python.org/" rel="nofollow"><kbd><b><code>python3</code></b></kbd></a> <a href="https://www.djangoproject.com/" rel="nofollow"><kbd><b><code>django3</code></b></kbd></a> <a href="https://sqlite.org" rel="nofollow"><kbd><b><code>sqlite3</code></b></kbd></a>
</p>

<table align="center">
	<tbody>
		<tr>
			<td><kbd><img src="./screenshot-frontpage.webp?raw=true" alt="frontpage screenshot" title="frontpage screenshot" width="363" height="250"/></kbd></td>
			<td><kbd><img src="./screenshot-frontpage-mobile.webp?raw=true" alt="frontpage on mobile screenshot" width="115" height="250"/></kbd></td>
		</tr>
	</tbody>
</table>

<strong><code>[tade]</code></strong> <sup>†</sup> is a discussion/forum/link aggregator application. It provides three interfaces: a regular web page, a mailing list bridge and an NNTP server.

<sup>†. pronounced *tA-de*, *ta*- as in *tally* and -*de* as in *the*. *τάδε* is a Greek pronoun meaning *this*</sup>

Repository: https://github.com/epilys/tade/

Public instance at https://tade.link (formerly sic.pm) | [Tor hidden service](http://sicpm3hp7dtrwhmf4qlelycqlvie6flqa5qnjnt3snok5xydvxhs4xyd.onion/) | IRC: [`#sic` on Libera Chat](https://libera.chat/) | [[sic] bot on Mastodon](https://botsin.space/@sic)

## In a nutshell

#### Web interface

- No Javascript necessary. An HTML5 compliant browser is enough; it even runs on [`w3m`, the text web browser](http://w3m.sourceforge.net/).
- Lightweight, requires only a `python3` environment and stores its database in a `sqlite3` file.
- Can be deployed with WSGI compatible servers (Apache/NGINX) or even `django`'s development server if need be.

#### Mailing list interface

Optionally, the forum can be used as a mailing list for registered users only. Users receive only posts with tags they are subscribed to, or replies directed to them.

#### NNTP interface

Optionally, the forum can be used with the built-in NNTP `VERSION 2` server. The server supports authentication for posting.

### ✒️ Forum features

- Posts can be text and/or URLs.
- Posts can optionally have any number of tags.
- Latest stories RSS and Atom feeds are provided.
- Post and comment text content support [commonmark Markdown syntax](https://commonmark.org/).
- Posts and comments can optionally have karma. You can turn this off and have posts ranked by latest activity instead.
- Posts can be pinned to the top with a time limit or indefinitely.

### 🏷️ Tag and 🗂️ Aggregation system

- Tags can optionally have any number of parent tags (but cycles are not allowed)
- Tags can optionally be organised in _Aggregations_, which are collections of tags with a common theme. A user's frontpage can be either all stories or their subscribed aggregations' stories.
- Aggregations can optionally be private, public or discoverable by other users.
- Aggregations can be set as "default" by moderators. New users are subscribed to default aggregations.
- Users can create their own aggregations at any time.
- Tags, users and domains can be excluded from an Aggregation via _exclude filters_.
- Users can have their own global exclude filters.

### 🔍 Search system

- Comments and posts are automatically indexed in a separate `sqlite` database file using the `fts5` (full text search) virtual table extension.
- Posts with URLs can optionally have their remote content fetched and indexed with a `django` management command (e.g. from within a cron job).

### 🎛️ Permission and moderation system

- Users can be inactive, active or banned.
- Moderators can set the number of days for which an account is considered new. New accounts cannot add tags or perform other potentially destructive actions.
- Public moderation log.

### 📨 Notification and email system

- Mentioning other users in comments notifies them.
- Users can choose when they receive each kind of notification via email
- Users can optionally enable a weekly digest email.

### 👥 Account system

- Users can either freely sign-up or have to be invited to.
- Users can optionally request for an invitation (this feature can be turned off).
- Users can save any story, comment to their bookmarks along with personal notes and export them at any time.
- Users can add personal metadata in their profile, including an avatar.
- Users can add "hats" to their account, which are decorations that can optionally be added to a comment. For example a moderator user wanting to comment as a moderator and not as a user would use a hat.
- Users have a personalised Atom or RSS feed that shows only their subscriptions.

### 🌐 Web standards

- Posted URLs are notified with [`webmention`](https://www.w3.org/TR/webmention/).
- Users can be retrieved with [`webfinger`](https://webfinger.net/).


## Setup / Deployment

You can use this repository as is by modifying the `tade` package to fit your needs, or install it with `pip` as a Django app.

### Using it directly

```shell
cp tade/local/secret_settings.py{.template,}
vim tade/local/secret_settings.py # REQUIRED: add secret token
vim tade/local/settings_local.py # OPTIONAL: local settings (SMTP etc)
python3 -m venv venv # OPTIONAL: setup virtual python enviroment in 'venv' directory
python3 -m pip install -r requirements.txt # Or 'pip3' install...
python3 manage.py migrate #sets up database
python3 manage.py createsuperuser #selfexplanatory
python3 manage.py runserver # run at 127.0.0.1:8000
python3 manage.py runserver 8001 # or run at 127.0.0.1:8001
python3 manage.py runserver 0.0.0.0:8000 # or run at public-ip:8000
```

For customization options look at the `TadeAppConfig` class in `tade/apps.py`, `style.css` in `tade/static` and the templates in `tade/templates`.

### Installing with `pip`

See [`DEPLOY.md`](DEPLOY.md).

## Code style

See [`CODE_STYLE.md`](CODE_STYLE.md).
