import dotenv

dotenv.read_dotenv(dotenv='.env')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
