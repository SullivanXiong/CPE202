class MyGraph:
    """A class that contains the Graph class in order to determine the
    components and bicolorability.
    Attributes:
        filename (str) : The name of the input file containing all the
                         necessary information to create the graph.
        graph (Graph) : The graph class that contains the instance of a graph.
    """

    def __init__(self, filename):
        """reads in the specification of a graph and creates a graph using an
        adjacency list representation. You may assume the graph is not empty
        and is a correct specification. E.g. each edge is represented by a pair of
        vertices between 1 and n. Note that the graph is not directed so each
        edge specified in the input file should appear on the adjacency list of each
        vertex of the two vertices associated with the edge.
        """
        with open(filename, "r") as input_file:
            lines = input_file.readlines()
            num_of_vertices = int(lines[0])
            num_of_edges = int(lines[1])
            self.graph = Graph(num_of_vertices, num_of_edges)
            for i in range(1, num_of_vertices + 1):
                self.graph.insert_vertex(i)
            for i in range(num_of_edges):
                line = lines[i+2].split()
                vertex1 = self.graph.vertices[int(line[0]) - 1]
                vertex2 = self.graph.vertices[int(line[1]) - 1]
                self.graph.insert_edge(vertex1, vertex2)

    def get_conn_components(self):
        """returns a list of lists. For example, if there are three connected
        components then you will return a list of three lists. The order of the
        sub-lists is not important. However each sub-list will contain the vertices
        (in ascending order) in the connected component represented by that list.
        Each vertex is represented by an integer from 1 to n. If a vertex has no
        edges it will be in a connected component containing only itself.
        Returns:
            list : A list of lists. The inner lists contains Vertices that make
                up a component in DFS order.
        """
        connected_components = []
        for vertex in self.graph.vertices:
            if vertex.status is None:
                component = []
                dfs(vertex, component)
                connected_components.append(component)
        return connected_components

    def bicolor(self):
        """returns True if the graph is bicolorable and false otherwise.
        Returns:
            bool : True if the graph is bicolorable otherwise false.
        """
        bicolor = True
        for vertex in self.graph.vertices:
            for edge_vertex in vertex.edges:
                if vertex.color == edge_vertex.color:
                    bicolor = False
        return bicolor


class MyGraphBFS:
    """A class that contains the Graph class in order to determine the
    components and bicolorability.
    Attributes:
        filename (str) : The name of the input file containing all the
                         necessary information to create the graph.
        graph (Graph) : The graph class that contains the instance of a graph.
    """

    def __init__(self, filename):
        """reads in the specification of a graph and creates a graph using an
        adjacency list representation. You may assume the graph is not empty
        and is a correct specification. E.g. each edge is represented by a pair of
        vertices between 1 and n. Note that the graph is not directed so each
        edge specified in the input file should appear on the adjacency list of each
        vertex of the two vertices associated with the edge.
        """
        with open(filename, "r") as input_file:
            lines = input_file.readlines()
            num_of_vertices = int(lines[0])
            num_of_edges = int(lines[1])
            self.graph = Graph(num_of_vertices, num_of_edges)
            for i in range(1, num_of_vertices + 1):
                self.graph.insert_vertex(i)
            for i in range(num_of_edges):
                line = lines[i+2].split()
                vertex1 = self.graph.vertices[int(line[0]) - 1]
                vertex2 = self.graph.vertices[int(line[1]) - 1]
                self.graph.insert_edge(vertex1, vertex2)

    def get_conn_components(self):
        """returns a list of lists. For example, if there are three connected
        components then you will return a list of three lists. The order of the
        sub-lists is not important. However each sub-list will contain the vertices
        (in ascending order) in the connected component represented by that list.
        Each vertex is represented by an integer from 1 to n. If a vertex has no
        edges it will be in a connected component containing only itself.
        Returns:
            list : A list of lists. The inner lists contains Vertices that make
                up a component in DFS order.
        """
        connected_components = []
        for vertex in self.graph.vertices:
            q = Queue(10)
            if vertex.status is None:
                vertex.status = "discovered"
                vertex.color = 0
                q.enqueue(vertex)
            while not q.is_empty():
                v = q.dequeue()
                connected_components.append(v)
                for edge_vertex in v.edges:
                    if edge_vertex.status is None:
                        edge_vertex.status = "discovered"
                        if v.color == 0:
                            edge_vertex.color = 1
                        elif v.color == 1:
                            edge_vertex.color = 0
                        q.enqueue(edge_vertex)
            vertex.status = "done"
        return connected_components

    def bicolor(self):
        """returns True if the graph is bicolorable and false otherwise.
        Returns:
            bool : True if the graph is bicolorable otherwise false.
        """
        bicolor = True
        for vertex in self.graph.vertices:
            for edge_vertex in vertex.edges:
                if vertex.color == edge_vertex.color:
                    bicolor = False
        return bicolor


class Graph:
    """A graph implemented with adjacency list.
    Attributes:

    """

    def __init__(self, num_vertices, num_edges):
        self.vertices = []
        self.num_of_vertices = num_vertices
        self.num_of_edges = num_edges

    def insert_vertex(self, i):
        new_vertex = Vertex(i)
        self.vertices.append(new_vertex)

    def insert_edge(self, vertex1, vertex2):
        vertex1.insert_edge(vertex2)
        vertex2.insert_edge(vertex1)

    def print_vertex(self):
        for vertex in self.vertices:
            print(vertex)


class Vertex:
    """A vertex in a Graph.
    Attribute:

    """

    def __init__(self, key):
        self.id = key
        self.edges = []
        self.color = None
        self.status = None
        self.pred = None

    def __repr__(self):
        repr_str = "Vertex({}, [".format(self.id)
        for i in range(len(self.edges)):
            if i == len(self.edges) - 1:
                repr_str += str(self.edges[i].id) + "], "
            else:
                repr_str += str(self.edges[i].id) + ", "
        repr_str += "{}, {}, {})".format(self.color, self.status, self.pred)
        return repr_str

    def insert_edge(self, other):
        self.edges.append(other)


class Queue():
    """ A Queue implemented with the built in list. Mimics a circular array.

    Attributes:
        capacity(int): The size limit of the queue.
        front(int): Enqueue pointer.
        rear(int): Dequeue pointer.
        items(list): The list that serves as our queue.
        num_items(int): The number of items currently in the Queue.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.items = [None] * (capacity + 1)
        self.num_items = 0

    def __repr__(self):
        return "QueueArray({}, {}, {}, {}, {})".format(self.capacity,
                                                       self.front,
                                                       self.rear,
                                                       self.items,
                                                       self.num_items)

    def __eq__(self, other):
        return (isinstance(self) == isinstance(other) and
                self.capacity == other.capacity and
                self.front == other.front and
                self.rear == other.rear and
                self.items == other.items and
                self.num_items == other.num_items)

    def is_empty(self):
        """ Checks if the queue is empty.

        Args:
            self(QueueArray): The current object referencing this method.

        Returns:
            bool: True if empty, else False.
        """
        return self.front == self.rear

    def is_full(self):
        """ Checks if the queue is full.

        Args:
            self(QueueArray): The current object referencing this method.

        Returns:
            bool: True if full, else False
        """
        return self.rear == (self.front + 1) % (self.capacity + 1)

    def enqueue(self, item):
        """ Adds a node to the end of the queue.

        Args:
            self(QueueArray): The current object referencing this method.
            item(*): The item being added to the queue.

        Returns:
            None: Does not return anything.

        Raises:
            IndexError: If the queue is full raises an error.
        """
        if self.is_full():
            raise IndexError
        if self.is_empty():
            self.items[self.front] = item
            self.front = (self.front + 1) % (self.capacity + 1)
            self.num_items += 1
        else:
            self.items[self.front] = item
            self.front = (self.front + 1) % (self.capacity + 1)
            self.num_items += 1

    def dequeue(self):
        """ Removes the node at the front of the queue.

        Args:
            self(QueueArray): The current object referencing this method.

        Returns:
            *: The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty raises an error.
        """
        if self.is_empty():
            raise IndexError
        item = self.items[self.rear]
        self.rear = (self.rear + 1) % (self.capacity + 1)
        self.num_items -= 1
        return item

    def size(self):
        """ The number of items currently in the queue.

        Args:
            self(QueueArray): The current object referencing this method.

        Returns:
            int: Number of items currently in the queue.
        """
        return self.num_items


def dfs(v, comm):
    v.status = "discovered"
    if v.color is None:
        v.color = 0
    comm.append(v)
    for edge_vertex in v.edges:
        if edge_vertex.status is None:
            edge_vertex.status = "discovered"
            if v.color == 0:
                edge_vertex.color = 1
            dfs(edge_vertex, comm)
    v.status = "done"
    return
