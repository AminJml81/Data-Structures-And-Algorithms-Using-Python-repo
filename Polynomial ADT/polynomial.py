class Polynomial:
    """class to represent polynomials
       # Note: I use sorted linked list for implementing polynomial which
       the first node shows linked list degree and it's corresponding coefficient
       nodes are sorted in descending order by degree
       this ADT only stores positive degrees and non zero coefficient


    attributes
    ----------
    _head: int
          polynomial head (biggest degree with it's coefficient)
    _tail: int
               polynomial tail (lowest degree with it's coefficient)
    _size: int
                polynomial size(number of terms)

    methods
    -------

    """
    def __init__(self, degree=None, coefficient=None):
        """
        if degree and coefficients are None it will make an empty polynomial.
        otherwise it will make a polynomial with the given degree and coefficient.

        parameters
        ----------
        degree: int >=0
               polynomial degree
        coefficient: int !=0
                    coefficient of the given term
        """
        if degree:
            if degree >= 0 and coefficient > 0:
                self._head = _PolyTermNode(degree, coefficient)
        else:
            self._head = None
        self._tail = self._head
        self._size = 0

    def degree(self):
        """
        returns polynomial degree (first node degree) or
        -1 if it is and empty polynomial.
        """
        if self._head:
            return self._head.degree
        return -1

    def evaluate(self, scalar):
        """
        evaluate the polynomial with the given scalar
        parameter
        ---------
        scalar: int
                given scalar to evaluate the polynomial with it

        returns the calculated number
        """
        assert scalar is not None, 'Theres is no scalar to evaluate the polynomial '
        if scalar == 0:
            # if the scalar is 0 it should return the the coefficient of the degree 0 term if the polynomial has it.
            if self._tail.degree == 0:
                return self._tail.coefficient
            # otherwise it returns 0 since zero is multiplying to them.
            return 0

        calculated_number = 0
        tmp_node = self._head
        while tmp_node:
            calculated_number += tmp_node.coefficient * (scalar ** tmp_node.degree)
            tmp_node = tmp_node.next

        return calculated_number

    def add_term(self, degree, coefficient):
        """
        adding new term with the given degree and coefficient
        if the given degree is already in the list it updates its coefficient
        parameters
        ----------
        degree: int >=0
              new term degree
        coefficient: int !=0
                   new term coefficient
        returns None
        """
        assert degree is not None or coefficient is not None, "Required parameters are not provided"

        assert degree >= 0, 'degree must be positive'

        if coefficient != 0:

            if degree > self.degree():
                self._prepend_term(degree, coefficient)

            elif degree < self._tail.degree:
                self._append_term(degree, coefficient)

            else:
                # since it updates the coefficient if the degree is in the list
                # it starts traversing from the first node
                current_node = self._head
                previous_node = None
                while current_node.degree > degree:
                    previous_node = current_node
                    current_node = current_node.next
                if current_node.degree == degree:
                    # updating the coefficient if the degree is already in the list.
                    current_node.coefficient = coefficient
                else:
                    new_node = _PolyTermNode(degree, coefficient)
                    previous_node.next = new_node

                self._size += 1

    def remove_term(self, degree):
        """
        removes the term with the given degree
        parameters
        ----------
        degree: int >=0
        returns None:
        """
        assert degree >= 0, "degree must be larger than or equal to zero"
        current_node = self._head
        previous_node = None
        while current_node.degree > degree:
            previous_node = current_node
            current_node = current_node.next
        previous_node = current_node.next
        current_node = None
        self._size -= 1

    def _append_term(self, degree, coefficient):
        """
        adding the term to the tail of the list
        parameters
        ----------
        degree: int >=0
               new term degree
        coefficient: int !=0
                   new term coefficient
        returns None:
        """

        new_node = _PolyTermNode(degree, coefficient)
        if self._size == 0:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def _prepend_term(self, degree, coefficient):
        """
        adding the term to the head of the list
        parameters
        ----------
        degree: int >=0
        coefficient: int !=0
        returns None:
        """
        new_node = _PolyTermNode(degree, coefficient)
        new_node.next = self._head
        if self._size == 0:
            self._tail = new_node
        self._head = new_node
        self._size += 1

    def __add__(self, other_poly):
        """adding two polynomials with the + operator
        if other_poly is just a single integer it adds that.
        otherwise it checks both polynomial degree by degree
        until the degree in one polynomial is larger than the another one,
        it adds that degree and it's corresponding coefficient
        if the current degree in both polynomial are the same , it adds both polynomials coefficients

        when the first while terminates we should check if there's any element left in one of the polynomials
        the next two while loops are responsible for that.

        although there are many while loops but they just traverse both list's once O(n+m)
        n the size of first polynomial and m the size of the second polynomial

        parameters
        ----------
        other_poly: Polynomial
                    second polynomial to be added with the first one
        returns the result in a Polynomial object
        """
        resulting_polynomial = Polynomial()

        if type(other_poly) == int:
            # if other poly is only a single integer we just need to copy first polynomial
            # and change or add the zero degree coefficient.
            resulting_polynomial = self
            if resulting_polynomial._tail.degree == 0:
                resulting_polynomial._tail.coefficient += other_poly
            else:
                resulting_polynomial._append_term(0, other_poly)

            return resulting_polynomial

        poly1_node = self._head
        poly2_node = other_poly._head

        while poly1_node and poly2_node:

            while poly1_node and poly1_node.degree > poly2_node.degree:
                degree = poly1_node.degree
                coefficient = poly1_node.coefficient
                poly1_node = poly1_node.next
                resulting_polynomial._append_term(degree, coefficient)

            while poly2_node and poly2_node.degree > poly1_node.degree:
                degree = poly2_node.degree
                coefficient = poly2_node.coefficient
                poly2_node = poly2_node.next
                resulting_polynomial._append_term(degree, coefficient)

            while poly1_node and poly2_node and poly1_node.degree == poly2_node.degree:
                # both polynomials have this degree
                degree = poly2_node.degree
                coefficient = poly1_node.coefficient + poly2_node.coefficient
                poly1_node = poly1_node.next
                poly2_node = poly2_node.next
                resulting_polynomial._append_term(degree, coefficient)

        while poly1_node:
            # adding other elements of the first polynomial
            degree = poly1_node.degree
            coefficient = poly1_node.coefficient
            resulting_polynomial._append_term(degree, coefficient)
            poly1_node = poly1_node.next

        while poly2_node:
            # adding other elements of the second polynomial
            degree = poly2_node.degree
            coefficient = poly2_node.coefficient
            resulting_polynomial._append_term(degree, coefficient)
            poly2_node = poly2_node.next

        return resulting_polynomial

    def __sub__(self, other_poly):
        """subbing two polynomial with the - operator
        Notes are the same as __add__ method but if the degree is just in the other_poly we just multiply -1 to it.

        parameters
        ----------
        other_poly: Polynomial

        returns the result in a Polynomial object
        """

        resulting_polynomial = Polynomial()

        if other_poly is isinstance(other_poly, int):
            # if other poly is only a single integer we just need to copy first polynomial
            # and change or subtract the zero degree coefficient.
            resulting_polynomial = self
            if resulting_polynomial._tail.degree == 0:
                resulting_polynomial._tail.coefficient -= other_poly
            else:
                resulting_polynomial._append_term(0, -1 * other_poly)

            return resulting_polynomial

        poly1_node = self._head
        poly2_node = other_poly._head

        while poly1_node and poly2_node:

            while poly1_node and poly1_node.degree > poly2_node.degree:
                degree = poly1_node.degree
                coefficient = poly1_node.coefficient
                poly1_node = poly1_node.next
                resulting_polynomial._append_term(degree, coefficient)

            while poly2_node and poly2_node.degree > poly1_node.degree:
                degree = poly2_node.degree
                coefficient = poly2_node.coefficient
                poly2_node = poly2_node.next
                resulting_polynomial._append_term(degree, -1 * coefficient)

            while poly1_node and poly2_node and poly1_node.degree == poly2_node.degree:
                # both polynomials have this degree
                degree = poly2_node.degree
                coefficient = poly1_node.coefficient - poly2_node.coefficient
                poly1_node = poly1_node.next
                poly2_node = poly2_node.next
                resulting_polynomial._append_term(degree, coefficient)

        while poly1_node:
            # adding other elements of the first polynomial
            degree = poly1_node.degree
            coefficient = poly1_node.coefficient
            resulting_polynomial._append_term(degree, coefficient)
            poly1_node = poly1_node.next

        while poly2_node:
            # adding other elements of the second polynomial
            degree = poly2_node.degree
            coefficient = poly2_node.coefficient
            resulting_polynomial._append_term(degree, -1 * coefficient)
            poly2_node = poly2_node.next

        return resulting_polynomial

    def __mul__(self, other):
        pass

    def __getitem__(self, degree):
        """
        getting the coefficient of the given degree
        parameters
        ----------
        degree:
        returns the coefficient of the given degree if it is actually in the list or 0 otherwise.
        """
        assert degree >= 0, 'degree must be larger than or equal to zero'
        if degree > self._head.degree or degree < self._tail.degree:
            return 0

        elif degree == self._tail.degree:
            return self._tail.coefficient
        else:
            tmp_node = self._head
            while tmp_node and tmp_node.degree > degree:
                tmp_node = tmp_node.next

            if tmp_node and tmp_node.degree == degree:
                return tmp_node.coefficient

            else:
                return 0

    def __str__(self):
        polynomial_string = ''
        tmp_node = self._head
        while tmp_node:
            polynomial_string += f'{tmp_node.coefficient}x^{tmp_node.degree} + '
            tmp_node = tmp_node.next
        return polynomial_string.rstrip(' + 0x^0 ')


class _PolyTermNode:
    """
    class to initialize Nodes for representing Polynomials.
    each node is used for representing each polynomial term.

    attributes
    ----------
    degree: int
          term's degree
    coefficient: int
          term's coefficient

    """
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None