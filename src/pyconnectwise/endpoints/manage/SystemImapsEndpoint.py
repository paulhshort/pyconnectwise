from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemImapsIdEndpoint import SystemImapsIdEndpoint
from pyconnectwise.endpoints.manage.SystemImapsCountEndpoint import SystemImapsCountEndpoint
from pyconnectwise.endpoints.manage.SystemImapsInfoEndpoint import SystemImapsInfoEndpoint
from pyconnectwise.models.manage.ImapModel import ImapModel

class SystemImapsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "imaps", parent_endpoint=parent_endpoint)
        
        self.count = self._register_child_endpoint(
            SystemImapsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SystemImapsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemImapsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemImapsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemImapsIdEndpoint: The initialized SystemImapsIdEndpoint object.
        """
        child = SystemImapsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ImapModel]:
        """
        Performs a GET request against the /system/imaps endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ImapModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request(
                "GET",
                params=params
            ),
            ImapModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ImapModel]:
        """
        Performs a GET request against the /system/imaps endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ImapModel]: The parsed response data.
        """
        return self._parse_many(ImapModel, super()._make_request("GET", data=data, params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ImapModel:
        """
        Performs a POST request against the /system/imaps endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ImapModel: The parsed response data.
        """
        return self._parse_one(ImapModel, super()._make_request("POST", data=data, params=params).json())
        