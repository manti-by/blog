import logging
from django.conf import settings
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    if settings.MY_FIRST_VAR == settings.MY_SECOND_VAR:
        logger.info(f"MY_FIRST_VAR: {settings.MY_SECOND_VAR}")
    else:
        logger.info(f"MY_FIRST_VAR: {settings.MY_THIRD_VAR}")

    logger.info(f"MY_ENV_VAR: {settings.MY_ENV_VAR}")
    if request.GET.get("key") == "test":
        return HttpResponse("Posts with test key")
    return HttpResponse("Posts index view")
