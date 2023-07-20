from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ScheduleHolidayListsIdEndpoint import ScheduleHolidayListsIdEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidayListsCopyEndpoint import ScheduleHolidayListsCopyEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidayListsCountEndpoint import ScheduleHolidayListsCountEndpoint
from pyconnectwise.models.manage.HolidayListModel import HolidayListModel

class ScheduleHolidayListsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "holidayLists", parent_endpoint=parent_endpoint)
        
        self.copy = self._register_child_endpoint(
            ScheduleHolidayListsCopyEndpoint(client, parent_endpoint=self)
        )
        self.count = self._register_child_endpoint(
            ScheduleHolidayListsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ScheduleHolidayListsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleHolidayListsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleHolidayListsIdEndpoint: The initialized ScheduleHolidayListsIdEndpoint object.
        """
        child = ScheduleHolidayListsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[HolidayListModel]:
        """
        Performs a GET request against the /schedule/holidayLists endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[HolidayListModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request(
                "GET",
                params=params
            ),
            HolidayListModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[HolidayListModel]:
        """
        Performs a GET request against the /schedule/holidayLists endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[HolidayListModel]: The parsed response data.
        """
        return self._parse_many(HolidayListModel, super()._make_request("GET", data=data, params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> HolidayListModel:
        """
        Performs a POST request against the /schedule/holidayLists endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            HolidayListModel: The parsed response data.
        """
        return self._parse_one(HolidayListModel, super()._make_request("POST", data=data, params=params).json())
        