# Django settings for project cmsproject.
import os

# Absolute path to the directory that holds the project.
# Example: "/var/www/vhosts/foo.bar/"
PROJECT_DIR = os.path.abspath( os.path.join(os.path.dirname(__file__),'../') )# "../" because we are in a package

try:
    from cmsproject.settings.secrets import *
except ImportError:
    pass

SITE_ID = 1

DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = False
TEMPLATE_DEBUG = DEBUG
IS_DEV_SERVER = False
IS_HTTP_SERVER = False
PREPEND_WWW = False
FORCE_SCRIPT_NAME = ''

ADMINS = (
     ('My Admin', 'admin@example.com'),
)

MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1', )

DEFAULT_FROM_EMAIL = 'noreply@example.com'
SERVER_EMAIL = 'django@%s' % os.uname()[1]

CACHE_MIDDLEWARE_KEY_PREFIX = 'cmsproject-%s-' % SITE_ID

# only activate cached sessions if suitable CACHE_BACKEND is available
#SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de'

DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y H:i'
TIME_FORMAT = 'H:i'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'j. F'

ugettext = gettext = lambda s: s

LANGUAGES = (
  ('de', 'Deutsch'),
  ('en', 'English'),
)
CMS_LANGUAGES = LANGUAGES

DEFAULT_LANGUAGE = 0

SITE_ID = 1

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/siteinfo/login/"

# Define URLs which should be accessible for anonymous even when 
# siteinfo.middleware.login_required.RequireLoginMiddleware is active.
PUBLIC_URLS = (
#    r'^admin/(.*)',
    r'^admin/filer/clipboard/operations/upload/',
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_DIR + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# slows down performance.
USE_ETAGS = False

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "cms.context_processors.media",
    "multilingual.context_processors.multilingual",
    "siteinfo.context_processors.siteinfo",
#    "sitemedia.media_context",
    "django.core.context_processors.request",
    "news.context_processors.news_processor",
]

MIDDLEWARE_CLASSES = [
#    'django.middleware.cache.UpdateCacheMiddleware',
#    'siteinfo.middleware.sites.SiteRedirectMiddleware',
#    'django.middleware.gzip.GZipMiddleware',  # this fucks up swf files when delivered by the dev server!
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.contrib.csrf.middleware.CsrfMiddleware',  # THIS SHOULD BE REACTIVATED IF WE CAN RESOLVE THE ISSUES
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'multilingual.middleware.DefaultLanguageMiddleware',
    'siteinfo.middleware.login_required.RequireLoginMiddleware',
#    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'cmsproject.urls'

TEMPLATE_DIRS = [
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR + '/templates',
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'divioadmin', # must be before admin to override base template
    'django.contrib.admin',
#    'django.contrib.sitemaps',
# tools
    'south',
    #'debug_toolbar',
# dependencies
    'appmedia',
#    'dbtemplates',
#    'filebrowser',
    'mptt',
    'multilingual',
    'siteinfo',
    'sorl.thumbnail',
    'tagging',
    'tinymce',
    'uni_form',
    'cms',
    #'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.snippet',
    #'cms.plugins.teaser',
    'cms.plugins.text',
    'cms.plugins.twitter',
    'cms.plugins.video',
    'contactform',
    'news',
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'rosetta',
    'newsletter',
    'simplegallery',
    'publisher',
    #'reversion',
    'cmsproject',
]

# filebrowser settings

FILEBROWSER_URL_WWW = MEDIA_URL + "uploads"
FILEBROWSER_URL_FILEBROWSER_MEDIA = MEDIA_URL + "filebrowser/"
FILEBROWSER_SAVE_FULL_URL = False
FILEBROWSER_EXTENSIONS = {
    'Folder':[''],
    'Image':['.jpg', '.jpeg', '.gif','.png','.tif','.tiff'],
    'Video':['.mov','.wmv','.mpeg','.mpg','.avi','.rm','.flv','.f4v'],
    'Document':['.pdf','.doc','.rtf','.txt','.xls','.csv','.zip'],
    'Sound':['.mp3','.mp4','.wav','.aiff','.midi'],
    'Code':['.html','.py','.js','.css']
}
FILEBROWSER_MAX_UPLOAD_SIZE = 20 * 1024 * 1024
FILEBROWSER_USE_IMAGE_GENERATOR = False


# filer settings
FILER_UPLOAD_ROOT = 'private/filer'

# sorl.thumbnail settings
THUMBNAIL_BASEDIR = 'tmp'
THUMBNAIL_QUALITY = 95

# django-tinymce settings
TINYMCE_JS_URL = MEDIA_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = dict(
    theme = "advanced",
    skin = "o2k7",
    plugins = "advimage,advlink,table,searchreplace,contextmenu,paste,save,spellchecker,autosave",
    # Appearance
    width = "640",
    height = "300",
    theme_advanced_buttons1 = "formatselect,separator,pastetext,pasteword,separator,bold,italic,separator,removeformat,separator,bullist,numlist,"
    + "separator,unlink,anchor,separator,separator,code,cleanup,separator,styleselect",
    theme_advanced_buttons2 = "",#"search,replace,cleanup,separator,formatselect,separator,help",
    theme_advanced_buttons3 = "",
    theme_advanced_blockformats = "p,h2,h3,h4",
    theme_advanced_toolbar_location = "top",
    theme_advanced_toolbar_align = "left",
    theme_advanced_statusbar_location = "bottom",
    theme_advanced_resizing = False,
    # Styles
    paste_remove_styles = True,
    paste_remove_spans = True,
    content_css = MEDIA_URL + 'css/text.css',
    show_styles_menu = False,
    # (X)HTML
    convert_urls = False,
    forced_root_block = 'p',
    extended_valid_elements = 'a[class|name|href|title|onclick],img[class|src|alt=image|id|title|onmouseover|onmouseout],p[id|style|dir|class],span[class|style]',
    object_resizing = False,
    invalid_elements = "font,strike,u",
    convert_fonts_to_spans = False,
    removeformat_selector = 'b,strong,em,i,span,ins',
    gecko_spellcheck = True,
)
# spellchecking plugin has to be installed manually
TINYMCE_SPELLCHECKER = False
TINYMCE_FILEBROWSER = True

# WYM Editor settings
WYM_CLASSES = ""
#    "{'name': 'date', 'title': 'PARA: Date', 'expr': 'p'}," + \
#    "{'name': 'hidden-note', 'title': 'PARA: Hidden note', 'expr': 'p[@class!=\"important\"]'}"
    
WYM_STYLES = ""
#    "{'name': '.hidden-note', 'css': 'color: #999; border: 2px solid #ccc;'}," + \
#    "{'name': '.date', 'css': 'background-color: #ff9; border: 2px solid #ee9;'}"

WYM_CONTAINERS = "" + \
    "{'name': 'P', 'title': 'Paragraph', 'css': 'wym_containers_p'}," +\
    "{'name': 'H2', 'title': 'Heading_2', 'css': 'wym_containers_h2'}," +\
    "{'name': 'H3', 'title': 'Heading_3', 'css': 'wym_containers_h3'}," +\
    "{'name': 'H4', 'title': 'Heading_4', 'css': 'wym_containers_h4'}," +\
    "{'name': 'H5', 'title': 'Heading_5', 'css': 'wym_containers_h5'}," +\
    "{'name': 'H6', 'title': 'Heading_6', 'css': 'wym_containers_h6'}," +\
    "{'name': 'PRE', 'title': 'Preformatted', 'css': 'wym_containers_pre'}," +\
    "{'name': 'BLOCKQUOTE', 'title': 'Blockquote', 'css': 'wym_containers_blockquote'},"

# django-cms settings
CMS_TEMPLATES = (
#    ('col_one.html', gettext('one column')),
    ('col_two.html', gettext('two columns')),
    ('col_two_sidebar_right.html', gettext('two columns sidebar right')),
    
    ('col_two_header.html', gettext('two columns with header')),
    ('col_two_header_sidebar_right.html', gettext('two columns with header sidebar right')), 
    
    ('col_three_header.html', gettext('three columns with header')),
    
#    ('col_three.html', gettext('three columns')),
)
CMS_PLACEHOLDER_CONF = {    
    'feature_top': {
        'plugins': ('SimpleGalleryPublicationPlugin', 'FilerImagePlugin', 'FlashPlugin', 'TextPlugin', 'VideoPlugin', ),
        'name': gettext('feature top'),
    },
    
    'col_left': {
        'plugins': ('TextPlugin', 'FilerImagePlugin', 'FilerTeaserPlugin', 'FilerFilePlugin', 'FlashPlugin', 'VideoPlugin', 'ContactFormPlugin', \
            'SimpleGalleryPublicationPlugin', 'GoogleMapPlugin', 'RelatedNewsPlugin', 'LatestNewsPlugin', 'NewsArchivePlugin', 'LinkPlugin',
            'NewsletterSubscribePlugin',),
        'name': gettext("left column"),
    },

    'col_right': {
        'plugins': ('TextPlugin', 'FilerImagePlugin', 'FilerTeaserPlugin', 'FilerFilePlugin', 'FlashPlugin', 'VideoPlugin', 'ContactFormPlugin', \
            'SimpleGalleryPublicationPlugin', 'GoogleMapPlugin', 'RelatedNewsPlugin', 'LatestNewsPlugin', 'NewsArchivePlugin', 'LinkPlugin',
            'NewsletterSubscribePlugin',),
        'name': gettext('right column'),
    },
    # 'LatestNewsPlugin', 'NewsArchivePlugin', 'SnippetPlugin',

    'col_middle': {
        'plugins': ('TextPlugin', 'FilerImagePlugin', 'FilerTeaserPlugin', 'FilerFilePlugin', 'FlashPlugin', 'VideoPlugin', 'ContactFormPlugin', \
            'SimpleGalleryPublicationPlugin', 'GoogleMapPlugin', 'RelatedNewsPlugin', 'LatestNewsPlugin', 'NewsArchivePlugin', 'LinkPlugin',),
        'name': gettext('middle column'),
    },
        
}
CMS_APPLICATIONS_URLS = (
    ('news.urls', 'news application'),
    ('newsletter.urls', 'newsletter application'),
)

CMS_PAGE_MEDIA_PATH = 'uploads/cms_page_media/'
CMS_SOFTROOT = True
CMS_FLAT_URLS = False
CMS_REDIRECTS = True
CMS_SEO_FIELDS = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_USE_TINYMCE = True
CMS_PERMISSION = True
CMS_MODERATOR = False

JQUERY_URL = "http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"
JQUERY_UI_PATH = "http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.1/jquery-ui.min.js"

#PLUGIN: TEASER
CMSPLUGIN_FILER_TEASER_STYLE_CHOICES = (
    ('boxbg','Mit Hintergrundverlauf'),
    ('plugin_teaser_picleft','Bild Links'),
)

#PLUGIN: SIMPLE GALLERY
CMSPLUGIN_SIMPLE_GALLERY_STYLE_CHOICES = (
    ('infobottom','Bildbeschriftung unten'),
)

IMAGE_ASPECT_RATIO_CHOICES = (
    (1, '1:1'),
    (1.33333, '4:3'),
    (1.77777, '16:9'),
    (2.33333, '21:9'),
)

THUMBNAIL_EXTENSION = 'png' # fix transparent pngs losing transparency when converted to jpeg

VIDEO_PLUGIN_ENABLE_ADVANCED_SETTINGS = False # disable color settings etc
