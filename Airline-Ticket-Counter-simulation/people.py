class Passenger:
    """
    class to represent each passenger which has unique id, arrival time.

    class attributes:
    -----------------
                     id_Num: int
                            unique identifier for each passenger.

    attributes:
    -----------
            _id_Num: int
                  identifier of each passenger.
            _arrivalTime: int
                        discrete number that passenger arrived.

    methods:
    -------
            get_id():
                    returns passenger id.
    """

    id_Num = 0

    def __init__(self, arrival_time):
        """
        initiates Passenger with the given arrival time.
        parameters:
        ----------
                  arrival_time: int
                              discrete time which passenger arrived.
        """
        Passenger.id_Num += 1
        self._id_Num = Passenger.id_Num
        self._arrivalTime = arrival_time

    def get_id(self):
        """returns passenger id"""
        return self._id_Num


class TicketAgent:
    """
        class to represent each Ticket Agent service the passengers.

        class attributes:
        -----------------
                         id_Num: int
                                unique identifier for each ticket agent.

        attributes:
        -----------
                _id_Num: int
                      identifier of each ticket agent.
                _passenger: passenger
                            passenger that the agent is servicing.
                _stop_time: int
                            discrete time that passenger service will be over.

        methods:
        -------
                start_service(passenger, stop_time):
                            assigns passenger and its stop time for the agent.

                stop_service():
                            ends service for the passenger and becomes free.

                is_free():
                           returns True if the agent is True, False Otherwise.

                is_finished():
                             returns True if the service of the passenger is finished.

                get_passenger_id():
                             returns passenger id that agent is giving service to.

                get_id():
                         returns id of the ticket agent.

        """

    id_Num = 0

    def __init__(self):
        """ initiates ticket agent"""
        TicketAgent.id_Num += 1
        self._id_Num = TicketAgent.id_Num
        self._passenger = None
        self._stop_time = -1

    def start_service(self, passenger, stop_time):
        """
        make agent busy.

        parameters:
        -----------
                    passenger: passenger
                               passenger that is getting service.
                    stop_time: stop_rime
                               stop_time of the passenger service.
        returns None
        """
        self._passenger = passenger
        self._stop_time = stop_time

    def stop_service(self):
        """
        free the agent.

        returns None
        """
        passenger = self._passenger
        self._passenger = None
        return passenger

    def is_free(self):
        """returns True if the agent is free"""
        return self._passenger is None

    def is_finished(self, current_time):
        """returns True if the passenger service is done on the current time"""
        return self._passenger is not None and self._stop_time == current_time

    def get_passenger_id(self):
        """returns passenger id that ticket agent is giving service."""
        return self._passenger.get_id()

    def get_id(self):
        """returns agent id"""
        return self._id_Num
