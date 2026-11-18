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

def test_add_order_successfully(order_tracker, mock_storage):
        """Tests adding a new order with default 'pending' status."""
        order_tracker.add_order("ORD001", "Laptop", 1, "CUST001")
        
        # We expect save_order to be called once
        mock_storage.save_order.assert_called_once()


def test_get_order_by_id_found(order_tracker, mock_storage):
    order = {"order_id": "ORD001", "status": "pending"}
    mock_storage.get_order.return_value = order

    assert order_tracker.get_order_by_id("ORD001") == order
    mock_storage.get_order.assert_called_once_with("ORD001")


def test_get_order_by_id_not_found(order_tracker, mock_storage):
    assert order_tracker.get_order_by_id("missing") is None
    mock_storage.get_order.assert_called_once_with("missing")


@pytest.mark.parametrize(
    ("old_status", "new_status"),
    [("pending", "shipped"), ("shipped", "delivered")],
)
def test_update_order_status_success(
    order_tracker, mock_storage, old_status, new_status
):
    mock_storage.get_order.return_value = {
        "order_id": "ORD001",
        "item_name": "Laptop",
        "status": old_status,
    }
    expected_order = {
        "order_id": "ORD001",
        "item_name": "Laptop",
        "status": new_status,
    }

    assert order_tracker.update_order_status("ORD001", new_status) == expected_order
    mock_storage.get_order.assert_called_once_with("ORD001")
    mock_storage.save_order.assert_called_once_with("ORD001", expected_order)


def test_update_order_status_not_found(order_tracker, mock_storage):
    assert order_tracker.update_order_status("missing", "shipped") is None
    mock_storage.get_order.assert_called_once_with("missing")
    mock_storage.save_order.assert_not_called()


def test_list_all_orders(order_tracker, mock_storage):
    orders = {
        "ORD001": {"order_id": "ORD001", "status": "pending"},
        "ORD002": {"order_id": "ORD002", "status": "shipped"},
    }
    mock_storage.get_all_orders.return_value = orders

    assert order_tracker.list_all_orders() == list(orders.values())
    mock_storage.get_all_orders.assert_called_once_with()


def test_list_all_orders_returns_empty_list(order_tracker, mock_storage):
    assert order_tracker.list_all_orders() == []
    mock_storage.get_all_orders.assert_called_once_with()


def test_list_orders_by_status(order_tracker, mock_storage):
    pending1 = {"order_id": "ORD001", "status": "pending"}
    shipped = {"order_id": "ORD002", "status": "shipped"}
    pending2 = {"order_id": "ORD003", "status": "pending"}
    mock_storage.get_all_orders.return_value = {
        "ORD001": pending1,
        "ORD002": shipped,
        "ORD003": pending2,
    }

    assert order_tracker.list_orders_by_status("pending") == [pending1, pending2]
    mock_storage.get_all_orders.assert_called_once_with()


def test_list_orders_by_status_empty(order_tracker, mock_storage):
    mock_storage.get_all_orders.return_value = {
        "ORD001": {"order_id": "ORD001", "status": "pending"}
    }

    assert order_tracker.list_orders_by_status("shipped") == []
    mock_storage.get_all_orders.assert_called_once_with()