import requests
from django.conf import settings
from django.core.cache import cache


class IBANService:
    api_key = settings.IBANAPI_API_KEY
    api_url = "https://api.ibanapi.com/v1"

    @classmethod
    def validate_iban(cls, iban):
        iban = cls.format_iban(iban)

        cache_key = f"iban_valid_{iban}"
        cached_result = cache.get(cache_key)
        if cached_result is not None:
            return cached_result

        response = requests.get(f"{cls.api_url}/validate/{iban}", params={"api_key": cls.api_key})
        result = False if response.status_code != 200 else True
        cache.set(cache_key, result)
        return result

    @classmethod
    def format_iban(cls, iban):
        return ''.join(iban.split())