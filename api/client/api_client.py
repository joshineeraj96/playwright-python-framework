from utils.logger import get_logger

logger = get_logger(__name__)


class APIClient:

    def __init__(self, api_context):
        self.api_context = api_context

    def get(self, endpoint, **kwargs):
        logger.info(f"GET : {endpoint}")

        response = self.api_context.get(endpoint, **kwargs)

        logger.info(f"Response Status : {response.status}")
        return response

    def post(self, endpoint, **kwargs):
        logger.info(f"POST : {endpoint}")
        logger.info(f"Request Body : {kwargs.get('data')}")

        response = self.api_context.post(endpoint, **kwargs)

        logger.info(f"Response Status : {response.status}")
        return response

    def put(self, endpoint, **kwargs):
        logger.info(f"PUT : {endpoint}")
        logger.info(f"Request Body : {kwargs.get('data')}")

        response = self.api_context.put(endpoint, **kwargs)

        logger.info(f"Response Status : {response.status}")
        return response

    def patch(self, endpoint, **kwargs):
        logger.info(f"PATCH : {endpoint}")
        logger.info(f"Request Body : {kwargs.get('data')}")

        response = self.api_context.patch(endpoint, **kwargs)

        logger.info(f"Response Status : {response.status}")
        return response

    def delete(self, endpoint, **kwargs):
        logger.info(f"DELETE : {endpoint}")

        response = self.api_context.delete(endpoint, **kwargs)

        logger.info(f"Response Status : {response.status}")
        return response