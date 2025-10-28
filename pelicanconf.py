import datetime
from pathlib import Path

CURRENT_YEAR = datetime.datetime.now().year

AUTHOR = 'SIGANN'
SITENAME = 'LAW XX: The 20th Linguistic Annotation Workshop'
SITEURL = ''  # TODO: update once the final GitHub Pages URL is known

WORKSHOP_TITLE = 'The 20th Linguistic Annotation Workshop'
WORKSHOP_TAGLINE = 'Co-located with ACL 2026 in San Diego'
WORKSHOP_LOGO = 'static/images/logo.svg'
WORKSHOP_CONTACT = 'lgessler+law@iu.edu'

PATH = 'content'
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = ()
SOCIAL = ()
DEFAULT_PAGINATION = False
RELATIVE_URLS = True

STATIC_PATHS = ['static']
STATIC_SAVE_AS = '{path}'
STATIC_URL = '{path}'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['asciidoc_reader', 'plugins.bibliography_plugin']
READERS = {'asc': 'asciidoc_reader.AsciiDocReader'}
ASCIIDOC_OPTIONS = []
ASCIIDOC_CMD = 'asciidoctor'
ASCIIDOC_BACKEND = 'html5'

DIRECT_TEMPLATES = []
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Home', '/index.html'),
    ('Call for Papers', '/cfp.html'),
    ('Program', '/program.html'),
    ('Accepted Papers', '/accepted.html'),
    ('Invited Speakers', '/invited.html'),
    ('Committees', '/committees.html'),
)

CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''

ARTICLE_PATHS = []
PAGE_PATHS = ['']

PATH_METADATA = r'(?P<path_no_ext>.*)\..*'
SLUG_REGEX_SUBSTITUTIONS = [(r'[^\w/]+', '-')]
PAGE_URL = '{path_no_ext}.html'
PAGE_SAVE_AS = '{path_no_ext}.html'
INDEX_URL = '{path_no_ext}/index.html'
INDEX_SAVE_AS = '{path_no_ext}/index.html'

SLUGIFY_SOURCE = 'basename'
TRANSLATION_ID_METADATA = 'path'
FORMATTED_FIELDS = ['summary', 'title', 'path', 'url', 'save_as']


def content_filter(path: str, metadata: dict) -> bool:
    """Handle AsciiDoc paths so Pelican emits flat HTML files."""
    if path.endswith('index.adoc'):
        metadata['save_as'] = path.replace('index.adoc', 'index.html')
        url = path.replace('index.adoc', '')
        metadata['url'] = url or '/'
        return True
    if path.endswith('.adoc'):
        html_path = path.replace('.adoc', '.html')
        metadata['save_as'] = html_path
        metadata['url'] = html_path
        return True
    return False


PROCESS_METADATA = content_filter
THEME = 'themes/lawxx'

# Convenience helpers
ROOT_DIR = Path(__file__).parent
CONTENT_DIR = ROOT_DIR / PATH
