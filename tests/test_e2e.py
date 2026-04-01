import multiprocessing
import time
from typing import Generator
import uvicorn
import pytest
from playwright.sync_api import Playwright, APIRequestContext, expect

from app.main import app

# Define the host and port for the test server
TEST_HOST = "127.0.0.1"
TEST_PORT = 8008
BASE_URL = f"http://{TEST_HOST}:{TEST_PORT}"

def run_server():
    """Target function to run the Uvicorn server."""
    uvicorn.run(app, host=TEST_HOST, port=TEST_PORT, log_level="info")

@pytest.fixture(scope="session")
def live_server():
    """Fixture to run the FastAPI app in a background process for testing."""
    proc = multiprocessing.Process(target=run_server, daemon=True)
    proc.start()
    # Give the server a moment to start up
    time.sleep(3)
    yield BASE_URL
    proc.terminate()

@pytest.fixture
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    """Fixture to create and cleanly dispose of a Playwright APIRequestContext."""
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()

def test_invoice_data_endpoint(api_request_context: APIRequestContext, live_server):
    """
    Tests the /api/v1/invoice-data endpoint using Playwright's request context.
    This simulates a client application making a POST request to the running API.
    """
    # A mock Base64 string for a dummy file. The content doesn't matter for this test
    # as the backend logic is currently mocked.
    mock_base64_file = "data:application/pdf;base64,JVBERi0xLjQKJ..."

    response = api_request_context.post(
        f"{live_server}/api/v1/invoice-data",
        data={"file": mock_base64_file, "provider": "mock"},
    )

    # Use Playwright's built-in assertions to check the response
    expect(response).to_be_ok()

    response_json = response.json()
    assert response_json["source"] == "gsp"
    assert "invoice_number" in response_json
    assert "INV-" in response_json["invoice_number"]
    assert len(response_json["items"]) == 3
    item = response_json["items"][0]
    assert item["name"] == "Paracetamol 500mg (10x10)"
    assert item["quantity"] == 100
    assert response_json["confidence"] == 0.95