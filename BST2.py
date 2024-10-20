''' Develop an application for managing events using BST. It is assumed that only two 
events can be scheduled in any given day, Max time allotted for each event is 5 hours. 
Minimum time between two events is 3 hours. Data need to be captured are event 
data and time, event name and number of guests expected. Provide methods to add 
event, provision to cancel event, display the events in descending order and delete 
the events which are completed. Take event time as unique parameter.'''
class Node:
    def __init__(self, event_time, event_name, guests):
        self.event_time = event_time
        self.event_name = event_name
        self.guests = guests
        self.left = None
        self.right = None

class EventManager:
    def __init__(self):
        self.root = None

    def add_event(self, event_time, event_name, guests):
        if not self.root:
            self.root = Node(event_time, event_name, guests)
        else:
            self._add_event(self.root, event_time, event_name, guests)

    def _add_event(self, root, event_time, event_name, guests):
        if event_time < root.event_time:
            if root.left:
                self._add_event(root.left, event_time, event_name, guests)
            else:
                root.left = Node(event_time, event_name, guests)
        else:
            if root.right:
                self._add_event(root.right, event_time, event_name, guests)
            else:
                root.right = Node(event_time, event_name, guests)

    def cancel_event(self, event_time):
        self.root = self._cancel_event(self.root, event_time)

    def _cancel_event(self, root, event_time):
        if not root:
            return root
        if event_time < root.event_time:
            root.left = self._cancel_event(root.left, event_time)
        elif event_time > root.event_time:
            root.right = self._cancel_event(root.right, event_time)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = self._min_value_node(root.right)
            root.event_time = temp.event_time
            root.event_name = temp.event_name
            root.guests = temp.guests
            root.right = self._cancel_event(root.right, temp.event_time)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def display_events_descending(self):
        events = []
        self._inorder_traversal(self.root, events)
        for event in reversed(events):
            print(f"Event Time: {event.event_time}, Event Name: {event.event_name}, Guests: {event.guests}")

    def _inorder_traversal(self, root, events):
        if root:
            self._inorder_traversal(root.left, events)
            events.append(root)
            self._inorder_traversal(root.right, events)

    def delete_completed_events(self, current_time):
        self.root = self._delete_completed_events(self.root, current_time)

    def _delete_completed_events(self, root, current_time):
        if not root:
            return root
        root.left = self._delete_completed_events(root.left, current_time)
        root.right = self._delete_completed_events(root.right, current_time)
        if root.event_time < current_time:
            return self._cancel_event(root, root.event_time)
        return root
def main():
    manager = EventManager()
    
    while True:
        print("\nEvent Manager")
        print("1. Add Event")
        print("2. Cancel Event")
        print("3. Display Events in Descending Order")
        print("4. Delete Completed Events")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            event_time = int(input("Enter event time: "))
            event_name = input("Enter event name: ")
            guests = int(input("Enter number of guests: "))
            manager.add_event(event_time, event_name, guests)
        elif choice == 2:
            event_time = int(input("Enter event time to cancel: "))
            manager.cancel_event(event_time)
        elif choice == 3:
            manager.display_events_descending()
        elif choice == 4:
            current_time = int(input("Enter current time: "))
            manager.delete_completed_events(current_time)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
