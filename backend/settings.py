import os
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from dotenv import dotenv_values
from models import PublicConfig, TaskConfig

ENV_PATH = Path(__file__).parent / '.env'


def checked_x_url(value):
    parsed = urlparse(value)
    if parsed.scheme != 'https' or parsed.hostname not in {'x.com', 'www.x.com', 'twitter.com', 'www.twitter.com'}:
        raise ValueError('X mission links must be HTTPS x.com or twitter.com links.')
    return value


def public_config():
    # Only explicitly allowlisted, public fields leave this function. .env changes
    # to campaign copy/links are picked up on the next request, without exposing secrets.
    values = {**os.environ, **dotenv_values(ENV_PATH)}
    tasks = []
    for key, title, action in [('follow', 'UPLINK', 'Follow'), ('like', 'SIGNAL', 'Like'),
                               ('repost', 'RELAY', 'Repost'), ('comment', 'VOICE', 'Reply')]:
        prefix = f'X_{key.upper()}'
        url = checked_x_url(values[f'{prefix}_LINK'])
        if key == 'comment' and '/intent/' in urlparse(url).path:
            parts = urlparse(url)
            query = dict(parse_qsl(parts.query))
            query['text'] = values['X_COMMENT_MESSAGE']
            url = urlunparse(parts._replace(query=urlencode(query)))
        tasks.append(TaskConfig(id=key, title=title, text=values[f'{prefix}_TEXT'], url=url, action=action))
    origin = values['PUBLIC_APP_URL'].rstrip('/')
    if urlparse(origin).scheme not in {'https', 'http'}:
        raise ValueError('PUBLIC_APP_URL must be an absolute HTTP(S) URL.')
    return PublicConfig(tasks=tasks, x_profile_url=checked_x_url(values['X_PROFILE_LINK']),
                        comment_message=values['X_COMMENT_MESSAGE'], share_text=values['X_SHARE_TEXT'],
                        share_url=checked_x_url(values['X_SHARE_LINK']), public_url=origin)