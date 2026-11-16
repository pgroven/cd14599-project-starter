import pytest
from unittest.mock import Mock
from ..order_tracker import OrderTracker

# --- Fixtures for Unit Tests ---



@pytest.fixture
def mock_storage():
    """
    Provides a mock storage object for tests.
    This mock will be configured to simulate various storage behaviors.
    """
    mock = Mock()
    # By default, mock get_order to return None (no order found)
    mock.get_order.return_value = None
    # By default, mock get_all_orders to return an empty dict
    mock.get_all_orders.return_value = {}
    return mock

@pytest.fixture
def order_tracker(mock_storage):
    """
    Provides an OrderTracker instance initialized with the mock_storage.
    """
    return OrderTracker(mock_storage)

#
# --- TODO: add test functions below this line ---
def test_add_order_successfully(order_tracker, mock_storage):
        """Tests adding a new order with default 'pending' status."""
        order_tracker.add_order("ORD001", "Laptop", 1, "CUST001")
        
        # We expect save_order to be called once
        mock_storage.save_order.assert_called_once()

def add_order(self, order_id: str, item_name: str, quantity: int, customer_id: str, status: str = "pending"):
        order = {
            "order_id": order_id,
            "item_name": item_name,
            "quantity": quantity,
            "customer_id": customer_id,
            "status": status
        }
        self.storage.save_order(order_id, order)
def add_order(self, order_id: str, item_name: str, quantity: int, customer_id: str, status: str = "pending"):
        # This is the new logic
        if self.storage.get_order(order_id):
            raise ValueError(f"Order with ID '{order_id}' already exists.")

        order = {
            "order_id": order_id,
            "item_name": item_name,
            "quantity": quantity,
            "customer_id": customer_id,
            "status": status
        }
        self.storage.save_order(order_id, order)
        