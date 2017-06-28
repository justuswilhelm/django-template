"""Landing tests."""
import pytest
from django.urls import reverse


@pytest.fixture(
    scope="module",
    params=(
        "landing:faq",
        "landing:imprint",
        "landing:landing",
        "landing:tos",
    ),
)
def resource_url(request):
    """Iterate over all landing resources."""
    return reverse(request.param)


@pytest.mark.django_db
def test_get(resource_url, client):
    """Assert we can GET resource_url."""
    response = client.get(resource_url)
    assert response.status_code == 200
