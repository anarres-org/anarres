# Wallabag

## Updating

If there is a version upgrade that needs a database migration. The most easy way to do is running the migrate command:

```bash
docker exec -t wallabag /var/www/wallabag/bin/console doctrine:migrations:migrate --env=prod --no-interaction
```
