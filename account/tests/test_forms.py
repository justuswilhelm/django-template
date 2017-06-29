"""Test for account forms."""
import pytest

from ..forms import (
    PasswordResetForm,
    UserCreationForm,
)


@pytest.mark.django_db
class TestUserCreationForm:
    """Test UserCreationForm."""

    def test_no_email(self):
        """Email must be present."""
        data = {
            'email_confirm': "test@example.com",
            'password1': "verysecurepassword",
            'password2': "verysecurepassword",
        }
        form = UserCreationForm(data)
        assert not form.is_valid()

    def test_no_email_confirm(self):
        """Email confirm must be present."""
        data = {
            'email': "test@example.com",
            'password1': "verysecurepassword",
            'password2': "verysecurepassword",
        }
        form = UserCreationForm(data)
        assert not form.is_valid()

    def test_email_mismatch(self):
        """Email must match."""
        data = {
            'email': "test1@example.com",
            'email_confirm': "test2@example.com",
            'password1': "verysecurepassword",
            'password2': "verysecurepassword",
        }
        form = UserCreationForm(data)
        assert not form.is_valid()


class TestPasswordResetForm:
    """Test PasswordResetForm."""

    def test_send_mail(self):
        """Sending mail is not possible at this moment."""
        with pytest.raises(NotImplementedError):
            PasswordResetForm().send_mail(
                'subject',
                None,
                {},
                'test@example.com',
                'test@example.com',
            )
