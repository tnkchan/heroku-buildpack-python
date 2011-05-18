
##########
# BEGIN HEROKU PYTHON/DJANGO LANGUAGE PACK
# Dynamically set DATABASES from ENV vars

import os, urlparse
urlparse.uses_netloc.append("postgres")
key_re = re.compile(r"^(?P<name>[A-Z_]+)_URL$")

for k,v in os.environ.items():
    url = urlparse.urlparse(v)
    matches = key_re.match(k)
    if not matches or url.scheme != "postgres":
        continue

    DATABASES[matches.group("name")] = {
        "ENGINE":   "django.db.backends.postgresql_psycopg2",
        "NAME":     url.path[1:],
        "USER":     url.username,
        "PASSWORD": url.password,
        "HOST":     url.hostname,
        "PORT":     url.port,
    }

# alias "default" to DATABASE_URL
if DATABASES["DATABASE"]:
    DATABASES["default"] = DATABASES["DATABASE"]

#
# END HEROKU PYTHON/DJANGO LANGUAGE PACK
##########
