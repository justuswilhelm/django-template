"""Dashboard tests."""
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestDashboardView:
    """Test DashboardView."""

    @pytest.fixture
    def resource_url(self):
        """URL to resource."""
        return reverse("dashboard:dashboard")

    def test_get(self, client, resource_url):
        """Test GET."""
        response = client.get(resource_url)
        assert response.status_code == 200
