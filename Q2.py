class FriendshipGraph:
    def __init__(self):
        self.connections = {}
    
    def add_friend(self, person):
        if person not in self.connections:
            self.connections[person] = set()
    
    def add_connection(self, person1, person2):
        self.add_friend(person1)
        self.add_friend(person2)
        self.connections[person1].add(person2)
        self.connections[person2].add(person1)
    
    def find_common_friends(self, person1, person2):
        if person1 in self.connections and person2 in self.connections:
            return self.connections[person1] & self.connections[person2]
        return set()
    
    def find_connection_level(self, start, end):
        if start not in self.connections or end not in self.connections:
            return -1
        if start == end:
            return 0
        queue = [(start, 0)]
        visited = set([start])
        while queue:
            current, level = queue.pop(0)
            for friend in self.connections[current]:
                if friend == end:
                    return level + 1
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, level + 1))
        return -1

def main():
    graph = FriendshipGraph()
    graph.add_connection('Alice', 'Bob')
    graph.add_connection('Bob', 'Janice')
    graph.add_connection('Alice', 'Clara')
    graph.add_connection('Bob', 'Clara')

    # Find common friends
    print("Common friends of Alice and Bob:", graph.find_common_friends('Alice', 'Bob'))

    # Find connection level
    print("Connection level between Alice and Janice:", graph.find_connection_level('Alice', 'Janice'))
    print("Connection level between Alice and Bob:", graph.find_connection_level('Alice', 'Bob'))

if __name__ == "__main__":
    main()
# time complexity: O(V + E)
# Space Complexity: O(V)