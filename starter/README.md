# README REFLECTION


The project is intentionally structured as a small, testable order-tracking app rather than a production system:

- **Separate HTTP handling from business logic.** `app.py` translates Flask requests into calls to `OrderTracker`, then returns JSON and HTTP status codes. This keeps route behavior distinct from order-management rules.
- **Keep storage replaceable.** `order_tracker.py` depends on a storage object with a small set of methods, not on a specific database. `in_memory_storage.py` supplies that interface with a dictionary, making the starter easy to run without database setup. The tradeoff is that orders disappear when the process restarts.
- **Use a dictionary keyed by order ID.** This makes lookup and update straightforward. Storage returns copies of order data so callers can’t accidentally mutate the stored record without saving it.
- **Test the layers separately.** `test_order_tracker.py` uses a mock storage to test business behavior in isolation; `test_api.py` exercises the Flask endpoints. The `project README` frames implementation as a Red → Green → Refactor TDD exercise.
- **Keep the frontend lightweight.** `index.html` and `script.js` provide a simple browser UI that talks to the JSON API, without adding a frontend framework.

These choices favor clarity and low setup cost for a learning project.

TESTING INSIGHTS
The unit tests in `test_order_tracker.py` check `OrderTracker` independently of Flask or real storage. A mock storage object records calls and supplies test data, so each test can focus on the tracker’s behavior.

They cover:
- **Adding an order:** checks that storage is called to save it.
- **Getting an order:** checks that an existing order is returned and a missing one returns `None`.
- **Updating status:** checks that the status changes and the updated order is saved; also verifies that a missing order is not saved. A parameterized test runs this for two status transitions.
- **Listing orders:** checks that all orders are returned, including when there are none.
- **Filtering by status:** checks that only matching orders are returned, including when there are no matches.

The tests in `test_api.py` are separate: they exercise the Flask endpoints, so they’re API-level tests rather than unit tests. 

NEXT STEP IMPROVEMENT
 This application does not have persistent storage and comprehensive request validation. 

Udatracker Starter Code
The project is intentionally structured as a small, testable order-tracking app


Read 
Completed with input: {
  "path": "C:\\Users\\Admin\\git\\cd14599-project-starter\\README.md"
}

Read 
Completed with input: {
  "path": "C:\\Users\\Admin\\git\\cd14599-project-starter\\starter\\README.md"
}

Read 
Completed with input: {
  "path": "C:\\Users\\Admin\\git\\cd14599-project-starter\\starter\\backend\\app.py"
}

Read 
Completed with input: {
  "path": "C:\\Users\\Admin\\git\\cd14599-project-starter\\starter\\backend\\in_memory_storage.py"
}

Read 
Completed with input: {
  "path": "C:\\Users\\Admin\\git\\cd14599-project-starter\\starter\\backend\\order_tracker.py"
}

Read 
Completed with input: {
  "path": "C:\\Users\\Admin\\git\\cd14599-project-starter\\starter\\backend\\tests\\test_api.py"
}

Read 
Completed with input: {
  "path": "C:\\Users\\Admin\\git\\cd14599-project-starter\\starter\\backend\\tests\\test_order_tracker.py"
}

Read 
Completed with input: {
  "path": "C:\\Users\\Admin\\git\\cd14599-project-starter\\starter\\frontend\\js\\script.js"
}

Read 
Completed with input: {
  "path": "C:\\Users\\Admin\\git\\cd14599-project-starter\\starter\\frontend\\css\\style.css"
}

Read 
Completed with input: {
  "path": "C:\\Users\\Admin\\git\\cd14599-project-starter\\starter\\frontend\\index.html"
}

This directory contains the starter code for the Udatracker project. The initial structure of directories and files is described below.

```
.
├── backend
│   ├── __init__.py
│   ├── app.py
│   ├── in_memory_storage.py
│   ├── order_tracker.py
│   ├── requirements.txt
│   └── tests
│       ├── __init__.py
│       ├── test_api.py
│       └── test_order_tracker.py
├── frontend
│   ├── css
│   │   └── style.css
│   ├── index.html
│   └── js
│       └── script.js
├── pytest.ini
└── README.md
```
