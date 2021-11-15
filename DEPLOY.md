# How to deploy [tade]

## Basic setup

```shell
make # this will create a dist/ directory with a tarball: dist/tade-0.1.tar.gz
cd /path/to/your/project
python3 -m venv venv # OPTIONAL: setup virtual python enviroment in 'venv' directory
source venv/bin/activate # activate virtual env
python3 -m pip install /path/to/tade-0.1.tar.gz # Or 'pip3' install...
django-admin startproject mysite # creates mysite directory
```

In `INSTALLED_APPS`, add the following lines:

```python
'django.contrib.sites',
'django.contrib.flatpages',
'django.contrib.humanize',
'mysite.apps.MySiteAppConfig',
```

We will create this class later.

Below `INSTALLED_APPS`, add the following:

```python
SITE_ID = 1

AUTH_USER_MODEL = "tade.User"
```

And in `TEMPLATES['OPTIONS']['context_processors']` add the following line:

```python
"tade.auth.auth_context",
```

Edit or create the file `mysite/apps.py` and add the following:

```python
from django.utils.safestring import mark_safe
from tade.apps import TadeAppConfig

class MySiteAppConfig(TadeAppConfig):
    verbose_name = "mysite"  # full human readable name, override this
    subtitle = "is a community."

    @property
    def html_label(self):
        """Override this to change HTML label used in static html"""
        return mark_safe("<strong>mysite</strong>")
    @property
    def html_subtitle(self):
        return mark_safe("is a community.")
```

See `tade/apps.py` for other options you can override in your `AppConfig`.

In `mysites/urls.py` include the following:


```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('', include('tade.urls')),
  path("admin/", admin.site.urls),
]
```

Finally, do the following to setup the database and your first user:

```shell
python3 manage.py migrate #sets up database
python3 manage.py createsuperuser #selfexplanatory
```

## Development

You can use django's development server:

```shell
python3 manage.py runserver # run at 127.0.0.1:8000
python3 manage.py runserver 8001 # run at 127.0.0.1:8001
python3 manage.py runserver 0.0.0.0:8000 # run at public-ip:8000
```

Any IPs you use with `runserver` must be in your `ALLOWED_HOSTS` settings.

## Production

Put local settings in `/local/` in `settings_local.py`. Optionally install `memcached` and `pymemcache`.

### `mysite/settings.py`

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = "noreply@example.com"

DEBUG=False

ALLOWED_HOSTS = [ "127.0.0.1", "example.com", ] # you can add extra hosts too e.g. "example.onion"
ADMINS = [('user', 'webmaster@example.com'), ]

STATIC_ROOT = "/path/to/collected/static/"
```

### Static files

(Optional: see `tools/tag-input-wasm/README.md`)

Issue `python3 manage.py collectstatic` to put all static files in your defined `STATIC_ROOT` folder.

### `apache2` and `modwsgi`

```text
<VirtualHost *:80>
  ServerName example.com
  ServerAdmin webmaster@example.com
  ErrorLog ${APACHE_LOG_DIR}/mysite-error.log
  CustomLog ${APACHE_LOG_DIR}/mysite-access.log combined
  RewriteEngine on
  RewriteCond %{SERVER_NAME} =example.com
  RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

<VirtualHost *:443>
  <Directorymatch "^/.*/\.git/">
    Order deny,allow
    Deny from all
  </Directorymatch>
  ServerAdmin webmaster@example.com
  ServerName example.com
  Alias /static /PATH/TO/static

  <Directory /PATH/TO/static>
    Require all granted
  </Directory>


  WSGIScriptAlias / /PATH/TO/tade/mysite/wsgi.py
  WSGIDaemonProcess examplecom user=debian python-home=/PATH/TO/tade/venv python-path=/PATH/TO/tade/mysite processes=2 threads=3
  WSGIProcessGroup examplecom

  <Directory /PATH/TO/tade/mysite>
    <Files wsgi.py>
    Require all granted
    </Files>
  </Directory>

    <IfModule mod_expires.c>
      # Activate mod
      ExpiresActive On
      <IfModule mod_headers.c>
        Header append Cache-Control "public"
      </IfModule>
      AddType application/font-sfnt            otf ttf
      AddType application/font-woff            woff
      AddType application/font-woff2           woff2

      ExpiresByType text/css "access plus 1 hour"
      ExpiresByType application/font-sfnt "access plus 1 month"
      ExpiresByType application/font-woff "access plus 1 month"
      ExpiresByType application/font-woff2 "access plus 1 month"
    </IfModule>

    LogLevel info

    ErrorLog ${APACHE_LOG_DIR}/mysite-ssl-error.log
    CustomLog ${APACHE_LOG_DIR}/mysite-ssl-access.log combined

    SSLCertificateFile /etc/letsencrypt/live/example.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/example.com/privkey.pem
    Include /etc/letsencrypt/options-ssl-apache.conf
    Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains; preload"
    <LocationMatch ^((?!(tags/graph-svg.*)).)*$>
    Header always set X-Frame-Options DENY
    </LocationMatch>
    Header always set X-Content-Type-Options nosniff

    <IfModule mod_headers.c>
      Header always set Strict-Transport-Security "max-age=15552000; includeSubDomains; preload"
    </IfModule>
</VirtualHost>
```

### `memcached`

Add the following to `settings_local.py`:

```
# Optional
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
        'OPTIONS': {
            'no_delay': True,
            'ignore_exc': True,
            'max_pool_size': 4,
            'use_pooling': True,
        }
    }
}
```

Configure memcache systemd service to restart along with apache2:

```shell
systemctl edit memcached
```

And add:

```
[Unit]
PartOf=apache2.service
WantedBy=apache2.service
```
