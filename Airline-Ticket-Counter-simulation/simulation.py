from random import random
from llistqueue import Queue
from people import TicketAgent, Passenger


class Simulation:
    """
    class to represent Simulation Process.

    attributes:
    -----------
               _time_length: int
                            total simulation time.
               _service_time: int
                            service time needed for each passenger.
               _arrive_probability: float (0<=x<=1)
                                probability of passenger arrival in each discrete time.
               _busy_agents: list
                            busy agents.
               _free_agents: list
                            free agents.
              _texts: list
                        texts of events occurred during simulation.
              _passengers_queue: Queue()
                                queue which passengers must wait to get service.
              _total_wait_time: int
                                total wait time for all passengers.(initially zero)
              _passengers_serviced: int
                                total number of passengers that get serviced.

    methods:
    -------
            run():
                 runs the simulation which uses for loop for simulating each minute of time.
            _handle_arrival(current_time):
                 handles the arrival of the passenger if the generated random number falls into given probability.
            _handle_begin_service(current_time):
                 handles the beginning phase of the passenger service which if assigns the first passenger of the queue
                 to the first empty agent.
            _handle_end_service(current_time):
                handles the ending phase of the passenger service. if the current time is the stop time of passenger's
                service it frees the agent.
            print_results():
                prints results which contains Number of passengers served, Number of passengers remaining in the queue,
                The average wait time.
            show_texts():
                prints all texts of the whole event occurred during simulation.

    static_methods:
    ---------------
            get_input():
                gets required information from the user.
            _add_passenger_arrival_text(current_time, passenger_id)
                adds text for passenger arrival.
            _add_agent_start_service(current_time, agent_id, passenger_id)
                 adds text for passenger service starting.
            _add_agent_stop_service(current_time, agent_id, passenger_id):
                adds text for passenger service ending.
    """

    def __init__(self, time_length, service_time, number_of_agents, arrival_probability):
        """
         parameters:
         -----------
                    time_length: int
                                total simulation time.
                    service_time: int
                                service time needed for each passenger.
                    number_of_agents: int
                    arrival_probability: float (0=<x<=1)
                                        probability of passenger arrival in each discrete time.

        """
        self._time_length = time_length
        self._service_time = service_time
        self._arrive_probability = arrival_probability
        self._busy_agents = []
        self._free_agents = []
        self._texts = []
        for i in range(number_of_agents):
            # makes agent.
            self._free_agents.append(TicketAgent())

        self._passengers_queue = Queue()
        self._total_wait_time = 0
        self._passengers_serviced = 0

    def run(self):
        """
        Runs the simulation which time is simulated using for loop discrete numbers.
        handles all 3 events and then show the results and texts.
        return None:
        """
        for current_time in range(self._time_length+1):
            self._handle_arrival(current_time)
            self._handle_begin_service(current_time)
            self._handle_end_service(current_time)
        self.print_results()
        self.show_texts()

    def _handle_arrival(self, current_time):
        """
        if the generated random number falls into the given arrive_probability it makes new passenger.
        parameters:
        -----------
                current_time: int

        returns None.
        """
        if random() <= self._arrive_probability:
            passenger = Passenger(current_time)
            self._passengers_queue.enqueue(passenger)
            self._texts.append(Simulation._add_passenger_arrival_text(current_time, passenger.get_id()))

    def _handle_begin_service(self, current_time):
        """
        while there's a passenger in the queue and a free agent, assigns passenger to the free agent.
        parameters:
        ---------
                current_time: int
        returns None.
        """
        while len(self._passengers_queue) > 0 and len(self._free_agents) > 0:
            passenger = self._passengers_queue.dequeue()
            agent = self._free_agents.pop(0)
            agent.start_service(passenger, current_time + self._service_time)
            self._busy_agents.append(agent)
            self._texts.append(Simulation._add_agent_start_service(current_time, agent.get_id(), passenger.get_id()))

        for i in range(len(self._passengers_queue)):
            self._total_wait_time += 1

    def _handle_end_service(self, current_time):
        """
        if the current time is the stop time of the passenger job. it frees the agent.
        just checks busy agents.
        parameters:
        -----------
                    current_time: int
        returns None
        """
        indexes = []
        for index, agent in enumerate(self._busy_agents):
            if agent.is_finished(current_time):
                self._texts.append(Simulation._add_agent_stop_service(current_time, agent.get_id(),
                                                                      agent.get_passenger_id()
                                                                      )
                                   )
                agent.stop_service()
                indexes.append(index)
                self._passengers_serviced += 1

        for index in indexes:
            self._free_agents.append(self._busy_agents.pop(index))

    def print_results(self):
        """
        prints the following information:
                  Number of passengers served,
                  Number of passengers remaining in the queue,
                  The average wait.

        returns None"""
        num_served = self._passengers_serviced - len(self._passengers_queue)
        average_wait_time = float(self._total_wait_time) / num_served
        print()
        print(f'Number of passengers served = {num_served}')
        print(f'Number of passengers remaining in the queue: {len(self._passengers_queue)}')
        print(f'The average wait time was {average_wait_time}')

    def show_texts(self):
        """display all events occurred during simulation."""
        print()
        for text in self._texts:
            print(text)

    @staticmethod
    def get_input():
        """
        getting required information from the user.
        returns Simulation instance with the given information
        """
        info = {}
        print('Enter The following Parameters: ')
        info['time_length'] = int(input('Number of minutes to simulate: '))
        info['number_of_agents'] = int(input('Number of ticket agents: '))
        info['service_time'] = int(input('Average service time per passenger: '))
        arrival_probability = float(input('probability of the passenger arrival: '))
        assert not 0 <= arrival_probability >= 1, 'incorrect probability'
        info['arrival_probability'] = arrival_probability
        return Simulation(**info)

    @staticmethod
    def _add_passenger_arrival_text(current_time, passenger_id):
        """returns text for passenger arrival."""
        return f'Time   {current_time}: Passenger {passenger_id} arrived.'

    @staticmethod
    def _add_agent_start_service(current_time, agent_id, passenger_id):
        """returns text for passenger service starting."""
        return f'Time   {current_time}: Agent {agent_id} started serving passenger {passenger_id}'

    @staticmethod
    def _add_agent_stop_service(current_time, agent_id, passenger_id):
        """returns text for passenger service stopping."""
        return f'Time   {current_time}: Agent {agent_id} stopped serving passenger {passenger_id}'
